# Japanese Learning

LaTeX study notes for learning Japanese, organized by JLPT level (starting
with `N5/`). See `N5/README.md` for compilation instructions and
`CLAUDE.md` for how this repo is worked on with Claude Code.

## Knowledge management philosophy

Three things involved in building this repo, each with different strengths
and limits:

- **Humans** — limited by fatigue and working memory/context, but strong at
  reasoning and synthesis (judging what actually matters, catching a wrong
  nuance, deciding what's worth tracking).
- **AI** — limited by token budget/context window, but strong at
  summarization and structuring scattered input into something organized.
  *Agentic* AI (tool-using, not just chat) adds another edge on top of
  that: it can synthesize and keep several files consistent with each other
  in one pass — e.g. adding a weak spot to `weak_areas.md` and updating its
  one-line summary in `CLAUDE.md` in the same turn, or adding a cached
  source to `resources/` and linking it from both `MAP.md` and whatever
  file cited it. A human doing that by hand has to remember every place a
  fact is duplicated and go update each one; an agentic AI can just do it
  as part of the same action.
- **Programs / plain files** — effectively unlimited memory and retrieval
  speed, but produce nothing on their own; they need precise, deliberate
  input to be useful (garbage in, garbage sitting there indefinitely).

The structure in this repo leans on that division of labor: `CLAUDE.md`,
`N5/mistakes_and_learning_pts/weak_areas.md`, `N5/quiz_mode.md`, and
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
