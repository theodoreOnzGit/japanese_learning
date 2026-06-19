# Japanese Notes --- JLPT N5

LaTeX notes for the JLPT N5 level (the lowest level of Japanese proficiency).

## Files

- `N5.tex` --- the main notes document
- `references.bib` --- BibTeX bibliography for citations
- `compile.sh` --- build + view script (Linux/macOS)
- `compile.ps1` --- build + view script (Windows)

## Compiling (Linux/macOS)

This document is compiled with `latexmk` in continuous preview mode:

```bash
latexmk -pvc -pdf --interaction=nonstopmode N5.tex
```

`-pvc` watches the source files and recompiles automatically on every save.

Then view the PDF in [okular](https://okular.kde.org/):

```bash
okular N5.pdf
```

Or just run the provided script, which does both:

```bash
./compile.sh          # compiles N5.tex
./compile.sh other.tex
```

(Make it executable once with `chmod +x compile.sh`.)

Both scripts run `latexmk -C` first to clear any stale generated files (a
common cause of misleading compile errors) before starting the preview loop.

## Compiling (Windows)

A PowerShell equivalent is provided:

```powershell
.\compile.ps1          # compiles N5.tex
.\compile.ps1 other.tex
```

It runs the same `latexmk` command and opens the resulting PDF in your
default PDF viewer.

## Notes

- The document uses `biblatex` with the `biber` backend for citations. Add
  entries to `references.bib` and cite them with `\cite{key}`.
- Japanese text is handled via the `CJKutf8` package so it works with
  `pdflatex`. If you prefer, you can compile with `lualatex`/`xelatex` and a
  Japanese font package instead.
