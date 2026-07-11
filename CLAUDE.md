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
3. Keep explanations at roughly **N5 level** for the user by default, **but be
   ready for N4/N3-level questions**: the user studies with their girlfriend,
   who is more advanced (around N4–N3) and may ask higher-level questions. Pitch
   the answer to whoever is asking — don't artificially cap everything at N5.
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
