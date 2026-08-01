# Japanese Learning

LaTeX study notes for learning Japanese, organized by JLPT level (starting
with `N5/`). See `N5/README.md` for compilation instructions and
`CLAUDE.md` for how this repo is worked on with Claude Code.

## Committing changes with git

The everyday loop, run from the repo root
(`~/Documents/learning/japanese_learning`):

```bash
git status                       # what changed / what's staged
git add N5/N5.tex                # stage specific files...
git add -A                       # ...or stage everything that changed
git commit -m "Log にvs を with 乗る/降りる"   # commit with a message
git push                         # send it to GitHub (origin/main)
```

**Always pass `-m "message"`.** A bare `git commit` opens a text editor to
type the message in, and with no `core.editor` or `$EDITOR` configured on
this machine git falls back to `vi` — which is the usual way to get stuck.

### If you're stuck in vi/vim

The editor is waiting for you; git is not frozen. Either:

- **Finish the commit** — type the message, then press `Esc`, then type
  `:wq` and press `Enter` (write + quit).
- **Abandon the commit** — press `Esc`, then type `:q!` and press `Enter`.
  Git sees an empty message and aborts; nothing is committed and nothing is
  lost. Your changes stay staged, so you can just rerun `git commit -m "..."`.

To avoid vi entirely, set a friendlier editor once:

```bash
git config --global core.editor nano   # or: vim, code --wait, nvim
```

### Other ways to get stuck

| Symptom | Fix |
|---|---|
| `Please tell me who you are` | `git config --global user.name "Your Name"` and `git config --global user.email "you@example.com"` |
| `nothing to commit` but files did change | Nothing was staged — run `git add -A` first |
| `Aborting commit due to empty commit message` | You quit the editor without typing a message; rerun with `-m "..."` |
| `Updates were rejected... fetch first` on push | Remote has commits you don't — `git pull --rebase` then `git push` |
| A pager (`git log`, `git diff`) won't exit | Press `q` |
| `index.lock` exists | A previous git process died; `rm .git/index.lock` |
| `error: unrecognized subcommand 'hooks'` | A beads hook incompatibility — see below |

### The beads `unrecognized subcommand 'hooks'` error

This repo sets `core.hooksPath` to `.beads/hooks`, so git runs beads' hooks
instead of `.git/hooks`. Those hooks (integration v1.1.0) call
`bd hooks run <event>`, but the Rust beads build in use here
(`beads-rs`, installed via cargo at `~/.cargo/bin/bd`) has no `hooks`
subcommand. Clap exits **2**, the hook only tolerates exit codes 3 and
124/142, so it propagates the failure and **git aborts the commit** — and
the `pre-push` hook blocks pushing the same way.

Fixed here by adding a capability guard to each file in `.beads/hooks/`:

```sh
if command -v bd >/dev/null 2>&1 && bd hooks --help >/dev/null 2>&1; then
```

If `bd` lacks `hooks`, the whole block is skipped and the hook exits 0. It's
self-healing — if `bd` later gains the subcommand, the check passes and the
hooks resume working, no further edit needed.

Caveat: the hook files are marked *"managed by beads"*, so running
`bd setup` again may overwrite them and reintroduce the problem. If commits
suddenly start failing this way again, re-apply the guard. A backup of the
original (unpatched) hooks is not kept in the repo.

Nuclear option if you'd rather not use the hooks at all —
`git config --unset core.hooksPath`. Beads still works fine from the CLI;
you only lose its automatic export/sync around git operations.

### Undoing things (before pushing)

```bash
git restore --staged <file>    # unstage a file, keep the edits
git restore <file>             # discard edits to a file — destructive
git commit --amend -m "New message"   # reword the last commit
```

Don't `--amend` or otherwise rewrite a commit that's already been pushed.

## Knowledge management philosophy

Three things involved in building this repo, each with different strengths
and limits:

- **Humans** — limited by fatigue and working memory/context, but strong at
  reasoning and synthesis (judging what actually matters, catching a wrong
  nuance, deciding what's worth tracking).
- **AI** — limited by token budget/context window, in two distinct ways:
  literally (cost and hard limits scale with tokens used — this matters on
  its own, not just as a proxy for something else) and qualitatively
  (long context gets lossy well before it's technically full — a
  quality-decay failure, separate from simply running out of room). Strong
  at summarization *and* real evaluative reasoning, not just summary —
  provided the context that reasoning needs is already explicit and in
  front of it. Correction to the "humans reason, AI summarizes" framing:
  the split isn't the *kind* of cognition, it's *what's available as
  context*. A human's reasoning is backed by a lifetime of context that's
  never been externalized anywhere — tacit judgment, values, physical
  experience — and structurally can't be handed to anyone else, including a
  file. AI's reasoning is only as good as whatever's already explicit in
  the conversation or repo. That synthesis is also not clean by default —
  it can hallucinate, stating something fluently that isn't true. The main
  mitigation is the same thing that makes the reasoning good in the first
  place: feeding it the right context directly (e.g. agentic reading of the
  actual repo/files) rather than letting it reason from recalled or assumed
  state. Grounding in explicit, checkable context cuts hallucination risk;
  reasoning from memory alone doesn't.
  *Agentic* AI (tool-using, not just chat) adds another edge on top of
  that: it can synthesize and keep several files consistent with each other
  in one pass — e.g. adding a weak spot to the right `weak_areas/` theme file and updating its
  one-line summary in `CLAUDE.md` in the same turn, or adding a cached
  source to `resources/` and linking it from both `MAP.md` and whatever
  file cited it. A human can do the same cross-file update by hand —
  nothing here is beyond human capability — but has to remember every
  place a fact is duplicated and go update each one manually; an agentic
  AI does it as part of the same action, at least faster than a human
  would. Agentic action also carries risk beyond synthesis errors: it can
  take wrong *actions* with real side effects, not just write wrong text.
  This session had two real examples — installing the wrong `beads` npm
  package before checking its `package.json`, and `bd init` auto-committing
  to git without being asked. More context doesn't make that risk go away;
  it needs periodic manual spot-checking of what the agent actually *did*,
  not just what it says it did.
- **Programs / plain files** — effectively unlimited memory and retrieval
  speed, but produce nothing on their own; they need precise, deliberate
  input to be useful (garbage in, garbage sitting there indefinitely). Code
  can also keep multiple files in sync — this repo already does it: `\cite`
  in `N5.tex` pulls from `references.bib` as a single source of truth, and
  biber regenerates a consistent bibliography every compile, no manual
  duplication involved. The difference from agentic AI is upfront cost:
  LaTeX's cross-referencing needed someone to design that mechanism once;
  the weak-areas/`CLAUDE.md`/`resources/` sync has no such mechanism
  and instead relies on the AI doing it correctly, ad hoc, every time.
  Determinism isn't free of its own failure mode, either: a program
  enforces whatever rules it was given, even after those rules go stale.
  biber will happily and consistently format a citation style nobody wants
  anymore, with no signal that anything's wrong — silent staleness, just a
  different flavor of silent failure than an AI's hallucination or an
  agent's stray action.

The structure in this repo leans on that division of labor: `CLAUDE.md`,
`N5/mistakes_and_learning_pts/weak_areas/` (read `MAP.md` first),
`N5/quiz_mode.md`, and
`resources/` (with `resources/MAP.md` as an index, read before the full
cache) are the "unlimited memory" layer — neither a human's memory nor an
AI's context window has to keep re-deriving this state every session. The
AI's job narrows to synthesis at write-time and cheap retrieval at read-time
(check the map, not the whole cache); the human's job narrows to judgment —
deciding what's worth recording and catching it when something written down
is wrong.

The caveat: unlike a program, these files don't enforce their own
correctness. A bad citation or a wrong grammar rule just sits there looking
authoritative until someone catches it. The "precision" this layer offers
is only as good as the verification that went into it — structure isn't a
substitute for that.

That gap is exactly what a real program closes. The `\cite`/`references.bib`
mechanism in `N5.tex` is a small existing example: someone wrote the sync
logic once (in this case, biblatex/biber), and it now enforces consistency
deterministically, no ad hoc judgment required per edit. The same could be
done for `CLAUDE.md`/the weak-areas files/`resources/` — a small tool (Rust,
given that's the author's language of choice elsewhere) that parses the
cross-references and fails loudly if `MAP.md` drifts from the files it
indexes, instead of trusting an agentic AI to keep them in sync correctly
every time. Not done here — the volume doesn't yet justify writing and
maintaining that tool — but it's the natural next step if this repo's
knowledge base outgrows ad hoc syncing.
