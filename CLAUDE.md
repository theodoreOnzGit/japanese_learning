# Japanese Learning — Working Notes for Claude

This repo holds LaTeX study notes for learning Japanese, organized by JLPT level
(starting with `N5/`, the lowest proficiency level).

## Hard rule: cache web sources

Any time Claude pulls something from the web (WebFetch/WebSearch) that gets
incorporated into this repo's content, cache it in `resources/` as a
markdown file:

- One representative markdown file per source, named for the source.
- Include an APA citation in plain text.
- Include a BibTeX citation in a ```` ```bibtex ``` ```` code block.
- Add a one-line entry to `resources/MAP.md` pointing at the new file.

**When consulting the cache, read `resources/MAP.md` first — do not read
the individual resource files unless specifically needed.** The map is the
index; the files are the detail.

Scope: sources that inform content actually added to this repo (vocab,
grammar notes, quiz-mode resources, tooling decisions recorded in
`CLAUDE.md`, etc.). Unrelated research (e.g. debugging the user's personal
editor config outside this repo) doesn't need caching here.

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
3. Keep explanations at roughly **N5 level** for the user by default, **but be
   ready for N4/N3-level questions**: the user studies with their girlfriend,
   who is more advanced (around N4–N3) and may ask higher-level questions. Pitch
   the answer to whoever is asking — don't artificially cap everything at N5.
4. When the user wants something recorded, add it to the appropriate section of
   the relevant level's `.tex` file (e.g. Vocabulary, Grammar, Diary,
   Class Notes in `N5/N5.tex`).

Be encouraging and concise. Correct mistakes directly but kindly.

### Quiz mode

When the user asks to be quizzed/tested ("quiz me", "quiz mode", "test me on
X"), follow the scaffold in `N5/quiz_mode.md` rather than improvising a
different quiz format each time.

### Exam mode

When the user asks for a full timed paper ("give me an exam", "mock paper",
"IGCSE practice"), follow `N5/exam_mode.md`. It holds the studied **Cambridge
IGCSE Japanese (0716)** format for all four papers, the adaptations needed here
(no audio, no pictures, no live examiner), and the synthesis protocol including
answer-key rules. Generated papers go in `N5/exams/`.

**Copyright:** synthesised papers reuse the *structure and mark allocation*
only — texts and items must be original. Never reproduce Cambridge passages,
questions or distractors. Source PDFs and their `kopitiam pdf2md` conversions
live in `resources/exams/`; citation in
`resources/cambridge-igcse-japanese-0716.md`.

### Dogfooding kopitiam (standing rule)

`kopitiam` is the user's own Rust CLI (`~/.cargo/bin/kopitiam`, source at
`~/Documents/fun_projects/kopitiam`). **Use it for the jobs it covers rather
than reaching for another tool** — most relevantly `kopitiam pdf2md <in.pdf> -o
<out.md>` for PDF→Markdown, which prints a validation report ending in
PASS/FAIL. `--index` writes a heading/page → line-range sidecar.

**Never run `kopitiam tui`, `kopitiam ai chat`, or `kopitiam view`** — they are
interactive, own the terminal, and will hang a non-interactive session. Full
command reference: `~/Documents/fun_projects/kopitiam/kopitiam_skill.md`.

### Class mode (chat-as-scratchpad during class)

The user uses the chat live during class to jot points as they come up.
**Follow `N5/class_mode.md`** — triggered by "class mode" / "I'm in class",
ended by "done" / "class over".

The three things that file exists to get right:

1. **Classify every message** as a **note** (sensei's), a **question**, or the
   user's own **production** — they are handled oppositely. A bare Japanese
   sentence with no framing defaults to **note**, because crediting sensei's
   sentence as the user's production inflates the mastery record and can promote
   an item they cannot actually produce. Ask *(sensei's, or yours?)* in one line
   when the sentence is correct and would count as evidence.
2. **Keep replies short.** They are listening to a teacher. Log the depth, don't
   send it.
3. **Pitch to sensei's frontier**, recorded in
   `weak_areas/class_raw_notes.md` — don't volunteer grammar she has
   deliberately deferred.

At the end of class, without being asked: write the session into `N5/N5.tex` →
**Class Notes**, dated with the current date, and confirm the weak-area files
and `MAP.md` are current.

### Known weak areas (quiz periodically)

The user tracks recurring weak spots in
`N5/mistakes_and_learning_pts/weak_areas/` — a set of theme files plus
screenshots of graded quiz mistakes in the parent directory. Proactively work
these into practice — don't wait to be asked.

**Read `weak_areas/MAP.md` first — do not read the individual theme files
unless you need detail on a specific item.** The map is the index (one line per
tracked item, with its status); the theme files are the detail. Same convention
as `resources/MAP.md`.

**Organised by theme, then JLPT level (standing rule):** weak areas are filed by
**situation/theme** (shopping, travel, gifts, presenting…), not by grammatical
category — the user reaches for them situationally. Within each file, entries are
grouped by **JLPT level** (Core N5 → Stretch N4 → Advanced N3+), because a level
never changes so entries never need moving.

**Language and cultural notes live together (standing rule):** each theme file
has `## Language` and `## Cultural` headings. Themes want both angles adjacent —
「gifts」 needs あげる/くれる/もらう *and* the Valentine's/お年玉 customs in one
place. (This replaces the older rule that split them into two separate files.)

**Mastery bar (standing rule):** an item is *not* learned just because it was
explained or logged. Every entry carries a status label:

| Label | Bar |
|---|---|
| `new` | logged, never tested |
| `shaky` | missed, or needed a hint |
| `solid` | 2+ correct unaided |
| `mastered` | 3+ correct unaided, spanning **2+ separate dates**, incl. **≥1 spontaneous use** |

**Spacing beats count** — two correct answers ten minutes apart are one data
point, not two. Promotion to `mastered` needs evidence across *different days*,
and at least one *spontaneous* use (the user reaching for it unprompted in their
own sentence, when it wasn't the drill). Per `N5/quiz_mode.md`, a slow or
re-derived correct answer is a soft miss and does not promote. Nothing is ever
deleted — `mastered` just goes dormant with a ~quarterly spot-check.

**Auto-log trigger (standing rule):** log *everything new the user brings up*
to the appropriate theme file automatically — **do not ask first, just log.**
This covers both directions:
- **Questions** — "what is X in Japanese," "what does X mean," "is it like Y,"
  any lookup or clarification. The act of asking is itself evidence of a gap.
- **New items the user shares** — a sentence from class, a word the teacher
  used, a grammar point, a cultural note. Anything they drop into the chat as
  "here's something new" gets recorded.

File under the right theme and the right `## Language` / `## Cultural` heading;
dual-angle items go under both, cross-referenced. Update `MAP.md` in the same
pass. The user has explicitly said not to ask permission each time — logging is
the default, silent behavior. Still confirm *what* was logged in the reply, just
don't gate it behind a question.

Raw class jottings are preserved verbatim in `weak_areas/class_raw_notes.md`;
corrections are appended as indented notes without editing the original lines.

**Current top priorities** (full list and status in `weak_areas/MAP.md`):

1. **に vs を with 乗る / 降りる** — three failed attempts, still not automatic.
   Source: `N5/mistakes_and_learning_pts/particles_ni_and_so_on.png`.
2. **ありがとうございます vs ございました** — missed in *both* directions within
   a single session (2026-08-01).
3. **着ます vs はきます** — re-asked from scratch a week after being taught.
4. **Counters (助数詞)** — standing extra weight per `N5/quiz_mode.md`.
5. **い-adjective past (おいしかったです)** — quiz miss, and it recurs inside
   many other patterns.
6. **Pitch accent** — no audio feedback in-chat; needs an external reference.

## Model guidance

The work in this repo splits into a **mechanical half** and a **language half**,
and they have very different error costs.

| Task | Suitable models |
|---|---|
| Japanese correction, grammar/nuance explanation, exam synthesis, answer keys, cultural questions | **Opus 5 / Sonnet 5** |
| Weak-area logging where the content is already drafted; LaTeX edits and compiles; `kopitiam pdf2md` runs and batch conversion; file reorganisation; scripts | **Haiku 4.5** is fine |

**Why be conservative on the language half.** This is a *learning* corpus. A
wrong particle, a fabricated reading, or a plausible-but-false nuance claim does
not just produce a bad answer — it gets logged to `weak_areas/` and memorised.
The error cost is asymmetric in a way it is not for most coding work. Recent
catches were single-mora precision calls (おもし**ろ**かった, とおい not とおおい,
ございます vs ございました by aspect); those are exactly what a smaller model is
likeliest to wave through.

Mixing is sensible: Haiku for a bulk-conversion session, Sonnet or Opus when the
user is actually studying. `/model` switches.

**Verification rule (applies to every model).** On 2026-08-01, three claims in a
field report about the `kopitiam` codebase were wrong because they were written
from output alone. All three were caught by reading the source. **Check the code
before asserting how it behaves** — and when correcting an earlier claim, record
the correction rather than quietly deleting it, so the reasoning stays auditable.

## Project structure

- `N5/N5.tex` — main N5 notes. Sections: Hiragana, Katakana, Vocabulary,
  Grammar, Diary, Class Notes.
- `N5/references.bib` — BibTeX bibliography (biblatex + biber backend).
- `N5/compile.sh` / `N5/compile.ps1` — build + view scripts (Linux / Windows).
- `N5/README.md` — compilation instructions.
- `N5/mistakes_and_learning_pts/` — screenshots of graded quiz mistakes, plus
  `weak_areas/` (themed weak-area files; read `weak_areas/MAP.md` first).

## Build / compile

- Compile with: `latexmk -pvc -pdf --interaction=nonstopmode N5.tex`
- View with: `okular N5.pdf` (Linux). The `compile.sh` script does both.
- Japanese is typeset via the `CJKutf8` package, so plain `pdflatex` works.
  All Japanese content must sit inside the `\begin{CJK}{UTF8}{min} ... \end{CJK}`
  environment.
- The user already runs `latexmk -pvc` in the background (auto-recompiles on
  save). Claude should **not** run `pdflatex`/`latexmk` itself after editing
  `N5.tex` — it's redundant and risks fighting over the same aux/lock files
  with the running watcher.

### Gotcha: stale aux files

If compilation fails with errors like `Missing \begin{document}` or
`Extra }, or forgotten \endgroup` pointing at a line that looks fine, it is
almost always a **corrupted `.aux` / latexmk state** left over from an earlier
failed run — not a real error in the `.tex`. Fix by clearing generated files:

```bash
latexmk -C            # or: rm -f *.aux *.bbl *.bcf *.run.xml *.fdb_latexmk *.fls
```

Then recompile.


<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:6cd5cc61 -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/SYNC_CONCEPTS.md for details and anti-patterns.

## Agent Context Profiles

The managed Beads block is task-tracking guidance, not permission to override repository, user, or orchestrator instructions.

- **Conservative (default)**: Use `bd` for task tracking. Do not run git commits, git pushes, or Dolt remote sync unless explicitly asked. At handoff, report changed files, validation, and suggested next commands.
- **Minimal**: Keep tool instruction files as pointers to `bd prime`; use the same conservative git policy unless active instructions say otherwise.
- **Team-maintainer**: Only when the repository explicitly opts in, agents may close beads, run quality gates, commit, and push as part of session close. A current "do not commit" or "do not push" instruction still wins.

## Session Completion

This protocol applies when ending a Beads implementation workflow. It is subordinate to explicit user, repository, and orchestrator instructions.

1. **File issues for remaining work** - Create beads for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **Handle git/sync by active profile**:
   ```bash
   # Conservative/minimal/default: report status and proposed commands; wait for approval.
   git status

   # Team-maintainer opt-in only, unless current instructions forbid it:
   git pull --rebase
   git push
   git status
   ```
5. **Hand off** - Summarize changes, validation, issue status, and any blocked sync/commit/push step

**Critical rules:**
- Explicit user or orchestrator instructions override this Beads block.
- Do not commit or push without clear authority from the active profile or the current user request.
- If a required sync or push is blocked, stop and report the exact command and error.
<!-- END BEADS INTEGRATION -->
