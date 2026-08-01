# Reading Traps

Cross-cutting file: words that *sound* alike, kanji with more than one reading,
and pronunciation itself. These don't belong to any one situation — they're a
recurring failure mode in their own right.

**The pattern is now well established:** six separate same-reading confusions
have been logged since 2026-07-11, and the rate is increasing (three on
2026-08-01 alone). Worth
drilling **readings explicitly**, rather than assuming they'll come along with
meaning.

Status labels: `new` · `shaky` · `solid` · `mastered` — see `MAP.md`.

## Language

### Same reading, different word

| # | Pair | Reading | Distinction | Logged | Status |
|---|---|---|---|---|---|
| 1 | 椅子 / いつ | いす / いつ | "chair" vs "when" — つ↔す typo | 2026-07-11 | `shaky` |
| 2 | 速い / 早い | はやい | fast (speed) vs early (time) | 2026-07-25 | `shaky` |
| 3 | 着ます / 来ます | きます | wear vs come | 2026-08-01 | `new` |
| 4 | 少ない / 好き | すくない / すき | misread 少ない as ~~すきない~~ | 2026-08-01 | `shaky` |
| 5 | 梨 / 無し | なし | "pear" vs "without/none" | 2026-08-01 | `new` |
| 6 | 熱い / 暑い / 厚い | あつい | hot-to-touch vs hot-weather vs thick | 2026-08-01 | `new` |

#### 1. 椅子 (いす) vs いつ — `shaky`

From class 2026-07-11. Mnemonic: same kanji as Mandarin 椅子 (yǐzi), which is also
why the pronunciation is reminiscent ("isu" ≈ "yi zi"). Watch for **いつ (itsu,
"when")** — different word; つ vs す is the easy slip.

#### 2. 速い vs 早い — `shaky`

Both **はやい**. 速い = fast (speed), 早い = early (time). Flagged on
速いですね！about the shinkansen. Also in `travel_and_transport.md`.

#### 3. 着ます vs 来ます — `new`

Both **きます**. Told apart only by particle: シャツ**を**着ます (object) vs
学校**に**来ます (destination). Likely the underlying cause of the recurring
wearing-verb confusion — see `clothing.md`.

#### 4. 少ない misread as すきない — `shaky`

2026-08-01. The kana is す**く**ない. Interference from 好き (すき), a far more
frequent word. Also in `describing_and_sentence_building.md`.

#### 5. 梨 (なし) vs 無し (なし) — `new`

Both **なし**. 梨 = pear; 無し = "without / none" (砂糖なし, 予約なし). Price tags
usually write the fruit as 梨 or ナシ to avoid the clash. See `food_and_drink.md`.

#### 6. 熱い / 暑い / 厚い — `new`

All three read **あつい** — the kanji carries the entire distinction:

| Kanji | Meaning | Example |
|---|---|---|
| 熱い | hot to the **touch** | 熱いお茶 |
| 暑い | hot **weather/air** | 暑い日 |
| 厚い | thick | 厚い本 |

Mirrors the cold side, which uses two *different words* instead
(つめたい touch / さむい ambient) — so the same semantic split is lexical for cold
and orthographic for hot. Full entry: `food_and_drink.md`.

### One kanji, two readings

#### 金 — かね vs きん — `shaky`

2026-08-01, misread お金 as ~~おきん~~.

| Word | Reading | Meaning |
|---|---|---|
| お金 | お**かね** | money (kun-reading) |
| 金 | **きん** | gold (on-reading) |
| 金曜日 | **きん**ようび | Friday (on-reading) |

Cross-check trick: the honorific prefix agrees with the reading type —
**訓読み → お**, **音読み → ご**. かね is kun-reading, hence お金. Full entry in
`shopping.md`.

#### 人 — ひと vs にん vs じん — `new`

Flagged 2026-08-01 via ひとが少ない. Three readings by context:

| Form | Reading | Note |
|---|---|---|
| 人 (alone) | **ひと** | "person / people" |
| 三人、五人 | **にん** | the counter — but 一人 ひと**り**, 二人 ふた**り** are irregular |
| 日本人、外国人 | **じん** | nationality suffix |
| 人口、人生 | **じん** | Sino-Japanese compounds |

The counter irregularities (ひとり/ふたり) are also in `numbers_time_dates.md`.

#### 国 — くに vs こく/ごく — `new`

2026-08-01. くに standing alone, こく (or voiced ごく) in compounds:

| Form | Reading | Meaning |
|---|---|---|
| 国 | **くに** | country (alone) |
| 外国 | がい**こく** | foreign country |
| 中国 | ちゅう**ごく** | China (voiced) |
| 国語 | **こく**ご | national language |

Same kun-alone / on-in-compound pattern as 人 and 金.

#### 年 — ねん vs とし — `new`

去年 きょ**ねん** / 来年 らい**ねん**, but 今年 こ**とし** / 毎年 まい**とし**.
Inconsistent within the same small set. See `numbers_time_dates.md`.

### Irregular readings that ignore the component kanji

今日 きょう · 今朝 けさ · 今年 ことし · 明日 あした · 一昨日 おととい ·
八百屋 やおや · 一人 ひとり · 二人 ふたり · 大人 おとな

These simply have to be memorised as whole words — the kanji don't predict them.
Individual entries in `numbers_time_dates.md` and `shopping.md`.

### Production slips (not reading — output)

- **科学者 → 「くがくがくしゃ」** (2026-07-25) — garbled under production
  pressure. See `nuclear_and_science.md`.
- **セオドウ vs セオドア** — セオドア is the conventional katakana for "Theodore."

## Pronunciation

### Intonation / pitch accent — `new` (untestable here)

Japanese is a pitch-accent language: each mora is high or low, and minimal pairs
can differ *only* in pitch —

> 箸 (はし) "chopsticks" · 橋 (はし) "bridge" · 端 (はし) "edge"

**No audio feedback is available in this chat.** Practice needs an external
reference — a native speaker, or Gemini TTS as a listening reference (see
`../../resources/gemini-3.1-flash-tts.md`).

Claude can annotate accent type/pattern on new vocabulary if asked, but **cannot
judge the user's own pronunciation**. Per `quiz_mode.md`, pitch questions are
asked as *written recall* ("what's the pitch pattern of 箸?"), never judged aloud.

## Cultural

Not applicable — this file is mechanical.
