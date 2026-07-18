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

### Chat-as-scratchpad during class

The user sometimes uses the chat live during class to jot down points as they
come up. In that mode: don't wait to be asked each time — when the session
winds down (the user says something like "done" or otherwise signals it's
over), write the class notes (or a summary of the discussion) into the
**Class Notes** section of `N5/N5.tex`, dated with the current date.

### Known weak areas (quiz periodically)

The user tracks recurring weak spots in `N5/mistakes_and_learning_pts/` —
both screenshots of graded quiz mistakes and a running
`weak_areas.md` list. Proactively work these into practice — don't wait to
be asked, and check `weak_areas.md` at the start of a tutoring session if
it's been a while.

**Mastery bar (standing rule):** an item is *not* considered learned just
because it was explained or logged. The user's bar is that they can (1) be
quizzed on it and (2) write correct sentences using it, unaided. Until an item
clears both, keep it in the active quiz rotation — logging to `weak_areas.md`
is the *start* of learning it, not the end. Don't retire an item from rotation
on the strength of a single correct answer; look for repeated correct use
across quizzing and sentence production before treating it as solid.

**Auto-log trigger:** whenever the user asks "what is X in Japanese" (a
translation/vocab lookup), add X to `weak_areas.md` automatically — the act
of asking is itself evidence of a gap, no need to wait for a mistake or to
be asked separately to log it.

Current items:

- **に vs を with 乗る (noru, "board") / 降りる (oriru, "get off")** — 乗る
  takes に (電車に乗る, moving *onto/into* the vehicle — に marks the goal),
  but 降りる takes を, not に (電車を降りる, moving *out of* the vehicle — を
  marks separation, same pattern as 家を出る). The user's instinct is to use
  に for both. Source: `N5/mistakes_and_learning_pts/particles_ni_and_so_on.png`.
- **Pitch accent / intonation** — no audio feedback available in-chat; needs
  an external reference to practice against.
- **Reading dates (日, days of the month)** — days 1–10 (plus 14, 20, 24)
  have irregular readings that don't follow number+にち.
- **Reading months (月)** — 4月/7月/9月 use irregular readings (しがつ /
  しちがつ / くがつ) instead of the expected number+がつ pattern.
- **Counting with counters (助数詞)** — sokuon/rendaku sound shifts on
  counters like 本, 匹, 個 depending on the preceding number (e.g. いっぽん,
  さんぼん, ろっぴき) are inconsistent and need per-counter drilling.
- **Positional nouns (位置名詞)** — 上/下/中/前/後ろ/横/隣/近く/間 etc.
  (pattern: [もの]の[position]に). 間 (あいだ, "between") is the odd one
  out, needing two nouns joined by と before の.
- **椅子 (いす, "chair") vs いつ ("when")** — easy to typo/misread つ↔す;
  mnemonic is that いす shares its kanji (椅子) with Mandarin yǐzi.

Full detail on each: `N5/mistakes_and_learning_pts/weak_areas.md`.

## Project structure

- `N5/N5.tex` — main N5 notes. Sections: Hiragana, Katakana, Vocabulary,
  Grammar, Diary, Class Notes.
- `N5/references.bib` — BibTeX bibliography (biblatex + biber backend).
- `N5/compile.sh` / `N5/compile.ps1` — build + view scripts (Linux / Windows).
- `N5/README.md` — compilation instructions.
- `N5/mistakes_and_learning_pts/` — screenshots of graded quiz mistakes,
  used to build the "known weak areas" list above.

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
