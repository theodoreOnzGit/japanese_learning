# Textbooks

Reference textbook PDFs used for study. Unlike compiled LaTeX output
(gitignored via `*.pdf`), files in this folder are **deliberately tracked**
— see the negation rule in the repo's `.gitignore`.

## いろどり — Irodori: Japanese for Life in Japan (`irodori/`)

**Publisher:** The Japan Foundation, Japanese-Language Institute, Urawa
(国際交流基金 日本語国際センター)
**Level in this repo:** Beginner 2 (初級2), Lessons 1–4
**License:** Creative Commons Attribution-NonCommercial 4.0 International
(CC BY-NC 4.0) — attribution required, non-commercial use only. Confirmed
against the Japan Foundation's official Irodori distribution terms; the
individual lesson PDFs uploaded here don't carry an in-file colophon/license
page (they start directly at lesson content), so the license status rests on
the publisher's official terms, not text printed on these specific pages.
**Files:**
- `irodori_beginner2_L01.pdf` — 第1課 先週、日本に来たばかりです (topic: 私の周りの人たち, "People around me")
- `irodori_beginner2_L02.pdf` — 第2課 まじめそうな人ですね (topic: 私の周りの人たち)
- `irodori_beginner2_L03.pdf` — 第3課 アレルギーがあるので、食べられないんです (topic: レストランで, "At a restaurant")
- `irodori_beginner2_L04.pdf` — 第4課 しょうゆをつけないで食べてください (topic: レストランで)

### APA Citation

The Japan Foundation, Japanese-Language Institute, Urawa. (n.d.). *Irodori:
Japanese for life in Japan* (Beginner 2) [PDF]. The Japan Foundation.
Licensed under CC BY-NC 4.0.

### BibTeX

```bibtex
@misc{irodori_beginner2,
  author       = {{The Japan Foundation, Japanese-Language Institute, Urawa}},
  title        = {Irodori: Japanese for Life in Japan (Beginner 2 / 初級2), Lessons 1--4},
  howpublished = {PDF},
  note         = {Licensed under CC BY-NC 4.0},
}
```

### Notes

- These four lesson chapters cover practical, situational Japanese
  (introducing coworkers, describing people, restaurant ordering and
  etiquette) at roughly N5–early N4 level — a good match for the
  `roleplay_coach_prompt.md` / `listening_mode.md` scenario style already
  used in this repo (hotel, restaurant, directions).
- Not yet converted to markdown via `kopitiam pdf2md`. If content from these
  gets pulled into `N5.tex` or a `weak_areas/` file, cite this file per the
  usual convention.
