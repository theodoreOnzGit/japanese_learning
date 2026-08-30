# Listening Mode

A scaffold for listening-comprehension practice, adapted from the user's own
roadmap document (provided 2026-08-30). Triggered by "listening practice",
"listening mode", "let's do listening", or similar — follow this rather than
improvising a different format each time.

This directly addresses the standing top priority in
`mistakes_and_learning_pts/weak_areas/MAP.md` → **listening comprehension**:
production is currently ahead of listening (see that file for the evidence).

## Goal

Build listening comprehension from short, familiar N5-style sentences toward
simple real-world conversations, and eventually short native content —
**in small, repeatable layers**. Do not jump from short beginner sentences
straight to full native articles.

## Where the user is now

Comfortable, recognized-by-ear patterns:

> X は Y です ／ X は 何ですか ／ X は どこですか ／ X が ありますか ／
> X を 使います ／ X で 買います ／ X まで 行きたいです ／ X と Y ／
> X から Y まで

Struggles: longer sentences, unfamiliar vocabulary, formal/service Japanese,
noun-modifying clauses, connected grammar, natural conversational phrasing.
Example of the jump in difficulty:

> コンビニで材料を買います。 ← comfortable
> コンビニで買った飲み物を組み合わせるのが人気です。 ← substantially harder

This suggests difficulty is currently driven by **sentence structure and
processing load**, not just individual vocabulary — so stages below control
structural complexity as a separate axis from vocabulary difficulty.

## The seven stages

Move to the next stage only when the current one is comfortable (see
Progression criterion below) — don't force pace.

1. **Short familiar sentences** (5–10 words). Loop: listen once → identify
   main meaning → ask for repetition if needed → hear again → repeat aloud →
   explain key vocab/grammar only if asked. Don't require perfect
   word-for-word comprehension. Example: コンビニで牛乳を買います。
2. **Two-sentence chains.** Two short sentences in sequence, then simple
   て-form sequencing: コーヒーを作って、飲みます。
3. **Practical roleplay listening** — hotel, restaurant, café, convenience
   store, train station, directions, shopping. Goal: recognize the *other
   person's* question without needing English every time. Example:
   お部屋番号をお願いします。→ 302号室です。 (This is the same scenario set
   `roleplay_coach_prompt.md` uses for production — listening mode is the
   comprehension-first mirror of it.)
4. **Controlled natural Japanese** — introduce more natural structures only
   once the simple form is solid, one new grammar feature at a time.
   駅まで行きたいです。どのバスですか。 (simple) before
   駅まで行きたいんですけど、どのバスですか。 (natural). Same sequencing
   already established for production in
   `mistakes_and_learning_pts/weak_areas/describing_and_sentence_building.md`
   → 〜んですけど.
5. **Noun modification** — currently hard (コンビニで買った飲み物). Build it
   progressively rather than expecting spontaneous comprehension: 飲み物 →
   コンビニで買います。→ コンビニで買った → コンビニで買った飲み物. Many
   examples before testing cold.
6. **Short authentic-style content** — short news items, simple articles,
   ads, menus, travel info, short social-media-style text. Never start with
   a full article: pick 3–5 short sentences, practice each, then gradually
   restore the original phrasing.
7. **Short native content** — 20–30 second clips, simple conversations,
   short announcements, easy news, travel videos. Comprehension ladder for
   these: (1) what's this generally about? (2) what information did you
   catch? (3) what specific words/phrases did you hear? (4) what does the
   whole sentence mean?

## Daily routine (10–15 minutes), if the user wants a structured session

1. **Warm-up (2 min)** — review 3–5 familiar expressions: ありますか／
   どこですか／何ですか／いくらですか／行きたいです.
2. **Micro-listening (5 min)** — 3–5 short sentences: listen → give time to
   respond → ask what they understood → repeat if needed → explain only the
   difficult part → have them repeat.
3. **One new grammar pattern (3 min)** — exactly one new structure, 2–3
   examples.
4. **Mini roleplay (3–5 min)** — the day's vocabulary in a realistic
   situation, where the user has to understand the *other* person's
   Japanese, not just produce their own lines.

## Difficulty control

- 🟢 **Green** — understood immediately → continue.
- 🟡 **Yellow** — understood after one repetition or small explanation →
  this is the ideal training zone, stay here.
- 🔴 **Red** — understood very little → **simplify the sentence**, don't
  just repeat it louder or slower.

## When the user says 分かりません

1. Repeat slowly.
2. Break the sentence into chunks.
3. Identify one or two key words.
4. Give a short English explanation.
5. Try the Japanese again.

Example — 朝食は朝7時から10時までです。 breaks down as 朝食=breakfast /
朝7時=7am / から=from / 10時=10am / まで=until — then reconstruct the whole
sentence.

## What to avoid

- Starting with full native news articles.
- Introducing several new grammar structures simultaneously.
- Assuming reading comprehension equals listening comprehension.
- Translating everything before giving the user a chance to actually listen.
- Long explanations mid-roleplay.
- Constantly increasing difficulty after a single successful answer.
- Penalizing clarification requests — asking for repetition is a tracked
  *strength* (`weak_areas/MAP.md`), not a weakness.

## Progression criterion

Move to the next stage when the user understands **roughly 80%** of the
current material without English assistance. If comprehension falls
substantially below that, reduce sentence length or vocabulary difficulty
rather than pushing through.

## Session logging — into the existing weak-areas system, not a separate one

At the end of a listening session, log into
`mistakes_and_learning_pts/weak_areas/` exactly as any other mode does (see
`quiz_mode.md` → End of round, and the standing auto-log rule in
`CLAUDE.md`) — new entries or status updates in the relevant theme file(s),
plus a `MAP.md` line, using the same `new`/`shaky`/`solid`/`mastered` labels.

When capturing a miss, **distinguish the failure type** — these are
different problems and should be logged as such:

- "I don't know the word" (vocabulary gap)
- "I know the word but didn't recognize it spoken" (listening-specific
  recognition gap, distinct from the vocab gap above)
- "I understood the words but not the sentence structure" (parsing/grammar
  gap, not vocabulary)

A session that was mostly 🟢/🟡 with no real misses is still worth a short
log note (what stage, what held up) even without a "miss" to record —
useful for tracking stage progression over time.

## Current priority

Per the roadmap and `weak_areas/MAP.md`:

1. Short sentence listening (Stage 1)
2. Familiar N5 grammar in spoken form
3. Practical conversation (Stage 3 — shares scenarios with
   `roleplay_coach_prompt.md`)
4. Numbers and time
5. Hotel/service vocabulary
6. Sentence chaining (Stage 2/4)
7. Gradual introduction of noun modification (Stage 5)
8. Only later: authentic news/article listening (Stage 6/7)

Near-term goal: **understand simple Japanese conversations without needing
English translation for every sentence.**
