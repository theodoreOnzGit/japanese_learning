# Weak Areas — Map

**Read this file first.** It lists everything currently tracked, one line per
item. Open an individual theme file only when you need the detail on that item.
Same convention as `resources/MAP.md`.

Organised by **situation/theme**, then by **JLPT level** within each file, with a
**mastery label** on every entry.

## Status labels

| Label | Bar | Quiz behaviour |
|---|---|---|
| `new` | logged, never tested | high priority |
| `shaky` | missed, or needed a hint | **highest priority** |
| `solid` | 2+ correct unaided | occasional |
| `mastered` | 3+ correct unaided, spanning **2+ separate dates**, incl. **≥1 spontaneous use** | dormant — spot-check ~quarterly |

**Spacing beats count.** Two correct answers ten minutes apart is one data point,
not two — same-session repetition measures short-term memory. Promotion to
`mastered` requires evidence across *different days*.

**"Spontaneous"** means used in a sentence of the user's own, unprompted, when
that item wasn't the drill — not producing it correctly right after being told
the answer.

**Caveats.** Claude can't see what happens outside this chat, so spacing evidence
is only as good as what gets logged. Per `../../quiz_mode.md`, a *slow* or
*re-derived* correct answer counts as a soft miss — it stays `solid` rather than
promoting. Nothing is deleted at `mastered`; it just goes dormant.

## Theme files

### [shopping.md](shopping.md)
Buying, comparing, trying on, asking staff.
- `shaky` お金 (おかね) — misread as おきん; 金 has two readings
- `shaky` 安い — missing は on ホテルは安いですね
- `shaky` より / と同じ — comparison; word order; 1× clean unaided use 2026-08-06, one more clears it
- `new` 買います — and its potential 買えます
- `new` スーパー + clipped loanwords (パソコン, コンビニ…)
- `new` 〜屋 shop suffix — 八百屋（やおや）, パン屋, 花屋…
- `new` 試着 — trying clothes on; 試着室 not 着替え室
- `new` 〜てもいいですか — asking permission
- `new` 〜てみる — trying something out
- `new` もっといいの（が）ありますか

### [travel_and_transport.md](travel_and_transport.md)
Trains, routes, going and returning.
- `shaky` **に vs を with 乗る / 降りる — 4 failed attempts, most-missed item**
- `shaky` 入る / 帰る / 戻る — mixed up; 入る is a sneaky う-verb
- `shaky` 速い vs 早い — same reading はやい
- `shaky` から〜まで + そして — 1× correct unaided
- `new` 行きます + 〜館 buildings (美術館, 図書館, 映画館…)
- `new` に with point-in-time, NOT with duration
- `new` そのうち + いました (not ありました)

### [gifts_and_giving.md](gifts_and_giving.md)
あげる/くれる/もらう, and the customs around gifting. **Densest topic.**
- `shaky` The giving/receiving trio — direction decides the verb
- `shaky` 私にあげました is ALWAYS wrong
- `shaky` Extends to family / in-group (内 uchi)
- `shaky` The double に — time vs recipient vs source
- `new` 〜てもらう — receiving an *action*
- `new` Keigo ladder — さしあげる / いただく / くださる
- `new` 旧正月 / お年玉 vocab
- `new` *Cultural:* バレンタインデー / ホワイトデー — 本命 vs 義理
- `new` *Cultural:* お年玉; 正月 vs 旧正月
- `new` *Cultural:* 内/外 (uchi/soto) as an obligatory viewpoint
- `new` *Cultural:* hierarchy dictates verb choice (keigo)

### [presenting_and_formal.md](presenting_and_formal.md)
Talks, openings and closings, opinions, addressing a teacher.
- `shaky` **ありがとうございます vs ございました — missed in *both* directions on 2026-08-01**
- `new` 〜と思います — opinion vs fact; the plain-form trap
- `new` お / ご honorific prefixes on nouns
- `new` 何か + は for softening a question
- `new` ご清聴ありがとうございました — presentation-specific closing
- `new` Formal sentence-final か must be explicit, not just rising intonation
- `new` 自分で
- `new` AI (エーアイ) / 人工知能 + 使う; disclosing AI use to a teacher
- `new` *Cultural:* audience/teacher as 外 (out-group)

### [people_and_politeness.md](people_and_politeness.md)
Pronouns, family terms, compliments.
- `solid` Family terms — 父 vs お父さん (first clean spontaneous 内/外 use)
- `shaky` Responding to a compliment
- `new` 国 / お国はどちらですか — asking where someone's from
- `new` First-person pronouns — 僕 / 私 / 俺 / わたくし / あたし
- `new` *Cultural:* accepting vs deflecting compliments (謙遜)

### [everyday_conversation.md](everyday_conversation.md)
Reactions, agreeing and refusing, joining ideas.
- `shaky` Interjections へえ / え〜 / えっ / ええ — quiz miss on へえ
- `new` **いいです is ambiguous — "yes fine" *or* "no thanks"**
- `new` と vs や — exhaustive vs representative "and"
- `new` ほんとに / ほんとうに — casual clipping; used correctly 2026-08-01
- `new` *Cultural:* 歌舞伎 — 女形, 隈取, 見得; vs 能
- `new` こちら / そちら / あちら / どちら — the polite こそあど
- `new` わかりました (past) vs わかりません (present)
- `new` アルバイト ← German *Arbeit*; the German-loanword set
- `new` **お疲れさまでした** — sign-off; past = completed effort; ご苦労さま is downward-only
- `new` ひま (暇) — free/not busy; な-adj, vs い-adj 忙しい
- `new` だめ (駄目)
- `new` すっかり

### [food_and_drink.md](food_and_drink.md)
Eating, ordering, describing food and temperature.
- `new` **つめたい vs さむい** — cold-to-touch vs cold-air (and 熱い/暑い mirroring it)
- `new` なし（梨）— pear; homophone with 無し "without"
- `new` Hotel breakfast vocab — 朝ごはん, 魚, 卵焼き, みそしる…
- `new` *Cultural:* いただきます / ごちそうさまでした

### [numbers_time_dates.md](numbers_time_dates.md)
Counting, counters, dates. **Extra quiz weight per `quiz_mode.md`.**
- `shaky` Days of the month — 1–10, 14, 20, 24 are irregular
- `shaky` Months — 4月 しがつ / 7月 しちがつ / 9月 くがつ
- `shaky` Counters (助数詞) — 人 / つ / 本 / 匹 / 個 sound shifts
- `new` Large numbers — 300 さんびゃく, 600 ろっぴゃく, 800 はっぴゃく…
- `new` Decimals — てん
- `new` Relative days — きのう set; no particle
- `new` Relative weeks — 先週/今週/来週; 先・今・来 across units
- `new` 週末 — 先週末/今週末/来週末; は on time words is fine
- `new` Relative years — 今年 ことし; 年 reads ねん or とし

### [describing_and_sentence_building.md](describing_and_sentence_building.md)
Conjugation grids, adjectives, connectors, positions.
- `new` **が vs は — new information sits before が, after は**; は/が never stack (miss: ご質問がはありますか, 2026-08-06)
- `new` **が / でも / けど — "but"**; が-conjunction vs が-subject disambiguated by position
- `shaky` **Location particle dropped before place names — 3 instances**
- `shaky` **い / な adjective conjugation — full grid** (self-identified as hard in class, 2026-08-01)
- `shaky` です past でした + **the い-adjective trap** (quiz miss 2026-07-25)
- `shaky` Positional nouns — 上/下/中/前/後ろ/横/隣/近く/間
- `shaky` 多い / 少ない — misread as すきない; predicative (人が多い), not 多い人
- `shaky` Potential form 買えます — 1× correct unaided
- `new` ます-form four-way grid
- `new` **だけ / しか〜ない — "only"**; だけ displaces が/を like も and は
- `new` 両親 / ご両親 — parents
- `new` **あまり / 全然 + negative** — negative-polarity family; あまり softens, 全然 is blunt
- `new` **Qn word + も + negative** — total negation; も replaces が/を; いつも trap; か/も/でも system
- `new` 測る / 高度
- `new` **Connector map** — と/や nouns · 〜くて い-adj · 〜で な-adj · て-form verbs · そして/でも/が sentences (sensei: と for adjectives is だめ)
- `new` 〜くて — い-adjective connector
- `new` で — linking form of です
- `new` に興味がある + から reason clause
- `new` から — one particle, four jobs (origin / time / range / reason)
- `new` 〜が欲しい / 〜たい — the が shift

### [clothing.md](clothing.md)
Which verb goes with which garment. **Survived a full round without sticking.**
- `shaky` 着ます vs はきます — the waist line
- `shaky` かぶります / かけます / します / つけます (class notes say かくます — wrong)
- `new` 着ます and 来ます are homophones — likely the real cause

### [nuclear_and_science.md](nuclear_and_science.md)
The user's own subject; source of the Fukushima deck.
- `shaky` 放射線 vs 核エネルギー — quiz miss, substituted one for the other
- `shaky` 科学者 — garbled as くがくがくしゃ
- `new` 原発 (げんぱつ)
- `new` 線量計 / 調べる / 危険 / どのくらい
- `new` 核 vs 原子 vs 原子力
- `new` Reading units and letters aloud
- `new` *Cultural:* talking about Fukushima; 風評被害

### [reading_traps.md](reading_traps.md)
Cross-cutting: homophones, multi-reading kanji, pronunciation.
- `shaky` **Six same-reading pairs logged since July — a pattern, not accidents**
- `shaky` 椅子 / いつ · 速い / 早い · 少ない / 好き
- `new` 着ます / 来ます · 梨 / 無し · 熱い / 暑い / 厚い
- `shaky` 金 — かね vs きん
- `new` 年 — ねん vs とし
- `new` 人 — ひと vs にん vs じん
- `new` 国 — くに vs こく/ごく
- `shaky` **おお vs おう long vowels** — 遠い written as とおおい; 多い interference
- `shaky` **Dropped morae in 4+ mora words** — とおおい · おもしかった · muzugashi, 3× on 2026-08-01
- `new` Irregular whole-word readings — 今日, 今年, 八百屋, 一人…
- `new` 双葉 vs 二子玉川 — place-name substitution risk (flagged by Gemini)
- `new` Pitch accent — tested externally 2026-08-06 (Gemini/ChatGPT voice); pronunciation improving fast per feedback

### [class_raw_notes.md](class_raw_notes.md)
The user's unedited class jottings, kept verbatim as source of truth, with
corrections appended without altering the original lines. **Also records
sensei's current teaching frontier** — what is expected, what is capped, and
what is beyond class — so explanations can be pitched to it during live lessons.

## Current priorities

Highest-value drilling right now, by evidence:

1. **に vs を with 乗る / 降りる** — four failed attempts (most recently
   substituting から for で at the station, 2026-08-06), still not automatic.
2. **ありがとうございます vs ございました** — missed in both directions in a
   single session (2026-08-01).
3. **着ます vs はきます** — re-asked from scratch a week after being taught.
4. **Counters** — standing extra weight per `quiz_mode.md`.
5. **い / な adjective conjugation (full grid)** — self-identified 2026-08-01 as
   hard in class; already a quiz miss; recurs inside many other patterns.
