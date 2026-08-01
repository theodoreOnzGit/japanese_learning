#!/usr/bin/env python3
"""Compress a PDF by downsampling its embedded images.

The Fukushima deck embeds phone photos at full sensor resolution (4284x5712)
while displaying them at ~3cm, so almost all of the file size is pixels nobody
will ever see. This downsamples them to a sane DPI for the way the PDF is
actually used.

Usage:
    ./compress_pdf.py fukushima_trip.pdf                 # -> fukushima_trip_small.pdf
    ./compress_pdf.py fukushima_trip.pdf -p screen       # smaller, for email
    ./compress_pdf.py fukushima_trip.pdf --dpi 200       # pick the DPI yourself
    ./compress_pdf.py fukushima_trip.pdf -o out.pdf      # explicit output name

Presets (image DPI):
    screen   100   email / upload; fine for projecting
    ebook    150   default; good on a laptop screen
    print    300   keeps photos sharp if anyone prints it

Requires Ghostscript (`gs`), which is already installed on this machine.
Never overwrites the input, and refuses to write a result that lost pages.
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

PRESETS = {"screen": 100, "ebook": 150, "print": 300}


def human(n: int) -> str:
    """Format a byte count the way a human reads it."""
    size = float(n)
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024 or unit == "GB":
            return f"{size:.1f} {unit}" if unit != "B" else f"{int(size)} B"
        size /= 1024
    return f"{size:.1f} GB"


def page_count(pdf: Path) -> int | None:
    """Page count via pdfinfo, or None if pdfinfo isn't available."""
    if not shutil.which("pdfinfo"):
        return None
    try:
        out = subprocess.run(
            ["pdfinfo", str(pdf)], capture_output=True, text=True, check=True
        ).stdout
    except subprocess.CalledProcessError:
        return None
    for line in out.splitlines():
        if line.startswith("Pages:"):
            return int(line.split()[1])
    return None


def compress(src: Path, dst: Path, dpi: int) -> None:
    """Run Ghostscript, downsampling every image stream to `dpi`."""
    subprocess.run(
        [
            "gs",
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.7",
            "-dNOPAUSE",
            "-dBATCH",
            "-dQUIET",
            # Downsample all three image classes to the target DPI.
            "-dDownsampleColorImages=true",
            "-dDownsampleGrayImages=true",
            "-dDownsampleMonoImages=true",
            f"-dColorImageResolution={dpi}",
            f"-dGrayImageResolution={dpi}",
            f"-dMonoImageResolution={dpi}",
            "-dColorImageDownsampleType=/Bicubic",
            "-dGrayImageDownsampleType=/Bicubic",
            # Keep text crisp: subset-embed fonts rather than rasterising them.
            "-dEmbedAllFonts=true",
            "-dSubsetFonts=true",
            f"-sOutputFile={dst}",
            str(src),
        ],
        check=True,
    )


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Compress a PDF by downsampling embedded images.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="presets: " + ", ".join(f"{k}={v}dpi" for k, v in PRESETS.items()),
    )
    ap.add_argument("pdf", type=Path, help="input PDF")
    ap.add_argument("-o", "--output", type=Path, help="output PDF (default: <name>_small.pdf)")
    ap.add_argument("-p", "--preset", choices=PRESETS, default="ebook", help="quality preset")
    ap.add_argument("--dpi", type=int, help="explicit image DPI (overrides --preset)")
    args = ap.parse_args()

    src: Path = args.pdf
    if not src.is_file():
        print(f"error: no such file: {src}", file=sys.stderr)
        return 1
    if not shutil.which("gs"):
        print("error: Ghostscript (gs) not found — install it with: sudo pacman -S ghostscript",
              file=sys.stderr)
        return 1

    dst: Path = args.output or src.with_name(f"{src.stem}_small.pdf")
    if dst.resolve() == src.resolve():
        print("error: refusing to overwrite the input file", file=sys.stderr)
        return 1

    dpi = args.dpi or PRESETS[args.preset]
    before = src.stat().st_size
    print(f"{src.name}: {human(before)} → downsampling images to {dpi} dpi…")

    try:
        compress(src, dst, dpi)
    except subprocess.CalledProcessError as exc:
        print(f"error: Ghostscript failed (exit {exc.returncode})", file=sys.stderr)
        dst.unlink(missing_ok=True)
        return 1

    # Ghostscript silently drops pages on some malformed inputs; don't hand back
    # a smaller file that quietly lost slides.
    pages_in, pages_out = page_count(src), page_count(dst)
    if pages_in is not None and pages_out is not None and pages_in != pages_out:
        print(f"error: page count changed ({pages_in} → {pages_out}); keeping original",
              file=sys.stderr)
        dst.unlink(missing_ok=True)
        return 1

    after = dst.stat().st_size
    if after >= before:
        print(f"{dst.name}: {human(after)} — no smaller than the original, deleting.")
        print("The PDF is probably already optimised, or is mostly text/vector.")
        dst.unlink()
        return 0

    saved = 100 * (1 - after / before)
    pages = f", {pages_out} pages intact" if pages_out is not None else ""
    print(f"{dst.name}: {human(after)}  ({saved:.0f}% smaller{pages})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
