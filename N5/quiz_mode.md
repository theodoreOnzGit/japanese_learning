# Quiz Mode

A scaffold for on-demand quizzing. Triggered by the user asking to be
quizzed/tested (e.g. "quiz me", "quiz mode", "test me on X", "quiz me until
I say stop") — Claude should follow this format rather than improvising a
different one each time.

## Current focus

- **Counting (助数詞, counters)** — flagged as especially weak. Include at
  least 1–2 counting questions per round (drill individual counters: つ, 人,
  本, 匹, 個, etc. and their sound shifts) on top of the normal weak-area
  rotation below, until the user says this has improved enough to drop back
  to normal weighting.

## Source priority

1. **Known weak areas first** — `mistakes_and_learning_pts/weak_areas.md`
   and the mistake screenshots in that folder. Weight questions toward these.
2. **Vocabulary / Grammar sections** of `N5.tex` (or the relevant level's
   `.tex` file) for general coverage.
3. If the user names a topic ("quiz me on counters", "quiz me on と vs か"),
   scope the whole round to that topic instead of the default mix.

## Format

- **One question at a time.** Ask, then wait for the user's answer before
  revealing the correct one or moving to the next question — don't dump a
  batch of Q&A at once.
- **Mix question types**:
  - EN→JP translation, JP→EN translation
  - fill-in-the-blank (particles, verb conjugations, counters)
  - reading practice (dates/months/numbers/counters)
  - reading comprehension, short — a couple of sentences in Japanese
    followed by 1–2 comprehension questions
  - reading comprehension, long — a few paragraphs in Japanese followed by
    several comprehension questions; keep vocab/grammar at the target level
    (N5 by default) so it's decodable, not just a translation exercise
    - Resource: [Tadoku](https://tadoku.org/japanese/) — free graded
      readers (150+ simplified books with furigana, illustrations, audio),
      organized by level; a good source for level-appropriate passages
      (cached: `resources/tadoku.md`)
  - occasional multiple choice for variety
- **Round length**: 5 questions by default, unless the user asks for a
  different number or an open-ended round ("keep going until I say stop").
- **Level**: N5 by default; N4/N3 if quizzing the girlfriend or if the user
  explicitly asks for harder questions (see `CLAUDE.md` tutoring workflow).

## Feedback per question

- Confirm right/wrong immediately after each answer.
- If wrong: give the correct answer and briefly explain *why*, tied to the
  underlying grammar rule — not just "wrong, it's X."
- If the mistake matches a tracked weak area, say so explicitly (e.g. "this
  is the に/を mix-up again") instead of treating it as a new, unrelated
  error.

### Recall friction (self-reported)

Claude has no access to real timestamps or to what the user does outside
the chat, so this is self-reported, not measured. By default, assume an
answer is unaided/from memory. If the user mentions hesitating a long time,
forgetting/re-deriving vocab, or looking something up, treat that as a
**soft weak-area signal even when the final answer is correct** — a slow or
searched "correct" still means the word/grammar isn't fluent yet. Log these
distinctly from outright mistakes (e.g. "recall latency on X" rather than
"incorrect usage of X") when capturing at end of round.

## End of round

- Give a quick score summary (e.g. "4/5").
- **Capture every miss.** For each wrong answer during the round: if it
  matches an existing `weak_areas.md` entry, no need to duplicate — it's
  already covered. If it doesn't match anything tracked, add a new entry to
  `weak_areas.md` at the end of the round (don't wait for the mistake to
  recur first — one miss during a quiz is enough to log it).
- If a tracked weak area was answered correctly several times in a row,
  mention the improvement — but don't remove it from tracking unless asked.

## Placement quiz (separate mode)

Trigger: "placement quiz", "test my level", "where do I stand". This is a
different goal from a normal round — breadth and escalating difficulty to
find the current frontier, not drilling known weak areas.

- Start at core N5 (basic particles, simple vocab, kana reading) and
  escalate through N5 → N4 → N3 territory as long as the user keeps
  answering correctly.
- Stop escalating a topic once mistakes cluster there (roughly 2–3 misses
  in the same area) — that's the frontier for that topic. Move on to
  probe a different area rather than hammering the same one.
- Longer than a normal round: aim for 10–15 questions across multiple
  grammar/vocab domains for breadth, not the narrow 5-question weak-area mix.
- At the end: give an assessed level per domain (e.g. "solid N5 grammar,
  shaky on N4 conditionals"), and apply the same "capture every miss" rule
  from **End of round** above to log newly found gaps into `weak_areas.md`.

## Out of scope

- No audio. Pitch-accent/intonation questions are asked as written recall
  (e.g. "what's the pitch accent pattern of 箸?") rather than judged aloud —
  see the note in `mistakes_and_learning_pts/weak_areas.md`.
