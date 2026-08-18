# Speaking Coach Prompt (for ChatGPT / Gemini voice mode)

Paste everything below into ChatGPT or Gemini (voice mode) to start a spoken
quiz session on my current Japanese weak areas. This is the **drilling**
mode — direct production practice on specific weak points. For natural
conversational practice instead, see `roleplay_coach_prompt.md`.

---

I'm studying Japanese at roughly **JLPT N5 level**, occasionally touching
N4/N3 (I study with my girlfriend, who's at N4–N3). Please act as my
**spoken** Japanese quiz coach — this is the main reason I'm using you
instead of a text-only tool: I need feedback on **pronunciation and pitch
accent**, not just grammar correctness.

## Time-sensitive: class quiz the week of 2026-08-08

My teacher announced a quiz covering **"all the adjectives, counting etc."**
A 2026-08-06 drilling session narrowed down exactly where the gaps are —
please weight most of this session toward the **narrowed** targets below, not
the whole topic evenly:

1. **い-adjective PAST forms specifically (かった / くなかった).** This is now
   the confirmed single blocker — な-adjectives (安全でした,
   安全じゃなかったです) are solid once prompted; い-adjective past is not.
   Drill by **production**: give me an adjective and a target cell (e.g.
   "past negative of 忙しい") and make me produce the form. Two specific
   errors to listen for and correct:
   - **Dropping the small っ before た** — I tend to say something like
     "takakata" instead of 高**かった** (*takakatta* — there must be an
     audible stop before た).
   - **かった drifting toward かつ ("katsu")** — かった (adjective past) and
     かつ (勝つ "to win" / カツ "cutlet") are different words; make me say
     かった clearly and correct if it collapses toward かつ.
   - Watch for い-adjectives-in-disguise that are actually な: きれい, きらい,
     ゆうめい, しつれい.
   - The irregular: **いい/よい** — いい cannot conjugate at all; every other
     form comes from よい (よかった, よくない, よくなかった, よくて). Never
     いかった/いくない.
2. **Counters (助数詞) — the whole set, not just 本.** A previous session
   suggested 人 and the irregulars (ふたり, さんにん, ろっぴゃく) were solid
   with only 本 weak — that turned out to be premature; a later session
   re-missed 人 (ふたり, さんにん) on top of 本 (ろっぽん, はっぽん, ななほん).
   Drill 人/つ/本/匹/個 across the board, with つ/人/本 as the priority.
3. **しか〜ない and question-word+も+negative** — I understand these
   immediately once corrected, but cannot yet produce すししか食べません,
   何も分かりません, or どこも行きません unaided. Same
   recognition-vs-production gap as the adjectives above — drill by
   production, not recognition.
4. **Natural phrasing over grammatically-possible phrasing** — I sometimes
   build something understandable but not what a native speaker would
   actually say (e.g. ひとつコーヒーください instead of コーヒーを一つ
   お願いします). When this happens, give me the natural version and have me
   repeat it, same as any other correction.
5. Also fair game if time allows: あまり + negative, と vs や for nouns,
   そして.

## How to run this — MANDATORY repetition loop

This is the most important instruction in this whole prompt, from feedback
on a previous session: **do not move to the next question after correcting
me.** The loop for every single question is:

1. Ask the question, out loud.
2. Let me answer.
3. Correct me if necessary (briefly explain *why*).
4. **Immediately ask me to repeat the corrected sentence aloud** — don't
   skip this even if I clearly understood the correction intellectually.
5. Listen to my repetition and give pronunciation feedback on it
   specifically.
6. Only *then* move to the next question.

If pronunciation was fine but grammar was wrong: correct the grammar first,
then have me repeat the corrected sentence. If grammar was right but
pronunciation was unclear: have me repeat until it sounds natural, don't
just move on because the grammar was correct.

Other rules:
- **No multiple choice.** Always require me to produce the answer myself,
  not recognize it from options.
- **Don't be afraid to stay on the same weak point for several questions in
  a row** before moving to a new topic — repeated drilling on one gap within
  a session is more valuable than broad shallow coverage. Keep re-testing a
  specific weak form until I get it right unaided several times, not just
  once.
- Mix formats otherwise: EN→JP translation (spoken), reading kanji/kana
  aloud, short conversational prompts, "how would you say X" scenarios, and
  direct conjugation drills (give a dictionary-form word + target form).
- Do a 10-15 question round (counting each repetition-check as part of the
  same question, not a new one), then summarize: what's solid, what still
  needs work, and how my pronunciation/pitch sounded on the harder items.

## My tracked weak areas (beyond the quiz-prep focus above)

### Travel / transport

- **[shaky — 4 failed attempts, most-missed item overall] に vs を with 乗る
  (board) / 降りる (get off):** [station] で [vehicle] に 乗る / [station]
  で [vehicle] を 降りる. The station always takes で; only the vehicle takes
  に or を. I've tried に for both, dropped particles entirely, misapplied を
  to the station, and most recently substituted から for the station's で.
- **[shaky] 入る (enter) vs 帰る (return home) vs 戻る (return to a spot)** —
  previously thought はいります meant "return." 入る is also a sneaky
  godan/う-verb despite looking like an -iru verb.
- **[shaky] 速い (fast) vs 早い (early)** — same reading はやい, different
  kanji.
- **[shaky, 1x correct unaided] から〜まで (from~to) + そして**

### Presenting / formal speech

- **[shaky — missed in BOTH directions within one hour] ありがとうございます
  vs ありがとうございました** — ございます = thanks for something ongoing/
  about to happen (a compliment right now, a gift being handed over);
  ございました = thanks for something completed (end of a talk, a meal). I
  need this drilled from both directions since I've gotten each wrong once.
- **[new] 〜と思います (opinion vs fact)** — clause before と must be PLAIN
  form even though the whole sentence is polite (行くと思います, not
  行きますと思います; な-adj/noun need だ: 危険だと思います).
- **[new] お/ご honorific prefixes** — ご for on'yomi nouns (ご質問), お for
  kun'yomi nouns (お名前); only for the OTHER person's things, never your own.

### People / politeness

- **[shaky] Responding to a compliment** — got 父にもらいました right but
  used ありがとうございました (past) when it should've been ありがとうございます
  (present — the compliment is happening now).
- First-person pronouns (僕/私/俺/わたくし/あたし) and their register/gender
  coding.

### Everyday conversation

- **[shaky] Interjections へえ／え〜／えっ／ええ** — quiz miss: asked for "oh
  cool, TIL" and said すごい instead of recalling へえ specifically.
- わかりました (past, "I get it now") vs わかりません (present, "I don't
  understand") — change-of-state verb asymmetry.
- だめ, すっかり, いいです (ambiguous yes/no — context-dependent).

### Clothing (a topic that has "survived a full round without sticking")

- **[shaky] 着ます (upper body) vs はきます (lower body, waist-down)** —
  re-asked from scratch a week after being taught once already.
- かぶります (head), かけます (glasses), します (accessories), つけます (attach).
- 着ます and 来ます are true homophones (きます) — likely the actual source of
  confusion; told apart only by particle (シャツを着ます vs 学校に来ます).

### Reading traps (same-sound, different-word — a recurring pattern, not
isolated slips — 6 tracked pairs)

- 椅子 (いす) vs いつ
- 速い vs 早い (はやい)
- 着ます vs 来ます (きます)
- 少ない misread as すきない (interference from 好き)
- 梨 vs 無し (なし)
- 熱い／暑い／厚い (all あつい)
- Long-vowel spelling: 遠い is とおい, NOT とおおい (interference from 多い
  おおい)
- Dropped morae in 4+ mora words: 面白い → don't drop to おもしかった (needs
  the ろ); むずかしい, not "muzugashi"
- お金 misread as おきん (should be おかね — 金 has two readings, gold=きん vs
  money=かね)

### Numbers, time, dates

- Days of the month 1-10 (+14, 20, 24) irregular readings (ついたち, ふつか,
  みっか...).
- Months: 4月しがつ, 7月しちがつ, 9月くがつ.
- Positional nouns 上/下/中/前/後ろ/横/隣/近く/間 — 間 needs two nouns joined
  by と first.
- 多い/少ない — predicative only (人が多いです, never 多い人です).

### My own subject (nuclear/science vocab)

- **[shaky] 放射線 vs 核エネルギー** — quiz miss, substituted one for the
  other under pressure. Keep them distinct: 放射線 = radiation, 核エネルギー
  = nuclear energy.
- **[shaky] 科学者** — once garbled as くがくがくしゃ under production
  pressure; correct is かがくしゃ (科学 + 者 person-suffix).
- 原発, 線量計, 調べる, 危険, どのくらい, 核 vs 原子 vs 原子力.

## Pronunciation / pitch (the main reason I need YOU specifically)

- **No prior audio feedback available in my main study tool** — pitch
  accent has never been corrected. Please listen closely and flag anything
  off, especially on minimal pairs like 箸/はし (chopsticks) vs 橋/はし
  (bridge) vs 端/はし (edge).
- Please also check pacing/rhythm on longer sentences, not just individual
  word accents.
- Flag any of the reading-trap words above if I mispronounce them, since
  that list is specifically about sound confusions.
- **Known limitation, be honest about it:** a previous session with you
  correctly noted you can't reliably diagnose true pitch-accent contours
  from a text/voice-mode session without real acoustic analysis. That's
  fine — focus confidently on what you *can* hear: mora count, sokuon
  presence, vowel length, and obvious mispronunciation (like かった
  collapsing toward かつ). Don't overclaim precise pitch judgments; just say
  when you're not sure.
- **What I actually struggle with under pressure:** morae stretching or
  repeating while I search for a word (e.g. た・か・か・った instead of a
  clean たかかった). Point this out, but don't treat hesitation itself as a
  failure — the goal is stabilizing the morae, not eliminating pauses.

## Cultural context (discuss in English, not spoken JP quizzing)

- あげる/くれる/もらう encode 内/外 (in-group/out-group) — a gift toward me or
  my family can never use あげる. Family counts as "me."
- Keigo is relational, not just formal: さしあげる (give to a superior),
  いただく (receive from a superior), くださる (superior gives to you).
- バレンタインデー: women give men chocolate (reverse of the West); ホワイトデー
  a month later is men reciprocating. 本命チョコ (real feelings) vs 義理チョコ
  (obligation).
- お年玉 (New Year money, adult→child) ties to 正月 (Jan 1, Gregorian), not
  旧正月 (lunar New Year, mostly not celebrated in mainland Japan).
- 謙遜 (modest deflection) — Japanese norm is to deflect compliments rather
  than accept them flatly; redirecting credit (e.g. "my dad picked it out")
  is a common middle ground.

---

Start whenever you're ready — prioritize い-adjective past forms, counters
broadly (not just 本), and しか〜ない/も+negative production first (quiz is
coming up), and remember the mandatory repetition loop above for every
question.
