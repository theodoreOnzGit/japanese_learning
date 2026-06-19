# Japanese Learning — Working Notes for Claude

This repo holds LaTeX study notes for learning Japanese, organized by JLPT level
(starting with `N5/`, the lowest proficiency level).

## Tutoring workflow (primary mode of work)

The user is learning Japanese. The default way we work together:

1. **The user states something they want to express** (usually in English).
2. **Claude tutors them** rather than just handing over the answer. That means:
   - Give the Japanese (with kana, and kanji where appropriate).
   - Show **romaji** and a literal/structural breakdown so the user understands
     *why* it's built that way, not just what it is.
   - Explain the relevant grammar point, particle, or politeness level briefly.
   - Flag common mistakes or spelling gotchas (e.g. the topic particle は is
     written `は` but pronounced "wa").
   - Where it aids practice, leave a blank for the user to attempt and then
     check their answer (collaborative "Learning" style).
3. Keep explanations at roughly **N5 level** unless the user signals otherwise.
4. When the user wants something recorded, add it to the appropriate section of
   the relevant level's `.tex` file (e.g. Vocabulary, Grammar, Diary in
   `N5/N5.tex`).

Be encouraging and concise. Correct mistakes directly but kindly.

## Project structure

- `N5/N5.tex` — main N5 notes. Sections: Hiragana, Katakana, Vocabulary,
  Grammar, Diary.
- `N5/references.bib` — BibTeX bibliography (biblatex + biber backend).
- `N5/compile.sh` / `N5/compile.ps1` — build + view scripts (Linux / Windows).
- `N5/README.md` — compilation instructions.

## Build / compile

- Compile with: `latexmk -pvc -pdf --interaction=nonstopmode N5.tex`
- View with: `okular N5.pdf` (Linux). The `compile.sh` script does both.
- Japanese is typeset via the `CJKutf8` package, so plain `pdflatex` works.
  All Japanese content must sit inside the `\begin{CJK}{UTF8}{min} ... \end{CJK}`
  environment.

### Gotcha: stale aux files

If compilation fails with errors like `Missing \begin{document}` or
`Extra }, or forgotten \endgroup` pointing at a line that looks fine, it is
almost always a **corrupted `.aux` / latexmk state** left over from an earlier
failed run — not a real error in the `.tex`. Fix by clearing generated files:

```bash
latexmk -C            # or: rm -f *.aux *.bbl *.bcf *.run.xml *.fdb_latexmk *.fls
```

Then recompile.
