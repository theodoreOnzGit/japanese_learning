# Weak Areas

Standing list of areas to quiz proactively — see `CLAUDE.md` ("Known weak
areas") for the instruction to work these into practice without being asked.
Add to this file as new weak spots come up (quiz mistakes, self-identified,
or flagged by the girlfriend/teacher).

## Intonation / pitch accent

Japanese is a pitch-accent language: each mora is either high or low, and
minimal pairs can differ only in pitch (箸/はし "chopsticks" vs 橋/はし
"bridge" vs 端/はし "edge"). No native audio feedback available in this repo
— practice needs an external reference (native speaker, or Gemini TTS as a
listening reference; see `resources/gemini-3.1-flash-tts.md`). Claude can
annotate accent type/pattern on new vocab going forward if asked, but can't
judge the user's own pronunciation.

## Reading dates: days of the month (日)

Days 1–10 (and a few others) have **irregular** readings that don't follow
the regular Sino-Japanese number + 日(にち) pattern — these are the ones that
trip people up:

| Day | Reading | Romaji |
|---|---|---|
| 1日 | ついたち | tsuitachi |
| 2日 | ふつか | futsuka |
| 3日 | みっか | mikka |
| 4日 | よっか | yokka |
| 5日 | いつか | itsuka |
| 6日 | むいか | muika |
| 7日 | なのか | nanoka |
| 8日 | ようか | youka |
| 9日 | ここのか | kokonoka |
| 10日 | とおか | tooka |
| 14日 | じゅうよっか | juuyokka |
| 20日 | はつか | hatsuka |
| 24日 | にじゅうよっか | nijuuyokka |

Everything else (11, 12, 13, 15–19, 21–23, 25–31) is regular: number +
にち, e.g. 11日 じゅういちにち, 17日 じゅうしちにち.

## Reading months (月)

Mostly regular (number + がつ), but three months use an irregular reading
instead of the expected one:

| Month | Reading | Not |
|---|---|---|
| 4月 (April) | しがつ | ~~よんがつ~~ |
| 7月 (July) | しちがつ | ~~なながつ~~ |
| 9月 (September) | くがつ | ~~きゅうがつ~~ |

## Counting: counters (助数詞)

The base numbers are fine; the trip point is that **counter words change
sound** depending on the number before them (sokuon っ insertion, and
rendaku-style voicing shifts). Same underlying counter, different surface
form:

- **人 (people):** 一人 ひとり, 二人 ふたり, then regular: 三人 さんにん,
  四人 よにん... (only 1 and 2 are irregular)
- **つ (general/small objects):** ひとつ, ふたつ, みっつ, よっつ, いつつ,
  むっつ, ななつ, やっつ, ここのつ, とお
- **本 (long thin objects — pens, bottles):** いっぽん, にほん, さんぼん,
  よんほん, ごほん, ろっぽん, ななほん, はっぽん, きゅうほん, じゅっぽん —
  the ほん/ぼん/ぽん shift depending on the preceding number is the hard part
- **匹 (small animals):** いっぴき, にひき, さんびき, よんひき, ごひき,
  ろっぴき, ななひき, はっぴき, きゅうひき, じゅっぴき — same shifting pattern
- **個 (small objects, general counter):** いっこ, にこ, さんこ, よんこ,
  ごこ, ろっこ, ななこ, はっこ, きゅうこ, じゅっこ

Rule of thumb: the sokuon (っ) shows up after 1, 6, 8, 10 with certain
counters (本, 匹, 個, 分...), and 本/匹 additionally voice to ぼん/びき after
certain numbers. There's no single universal rule — this one mostly comes
down to drilling each counter's pattern individually.

## Positional nouns (位置名詞)

Flagged from class (2026-07-11) — うえ and the rest of this family are
unclear. These are relational nouns used to describe *where* something is;
they behave like nouns (not verbs/adjectives), so they always take の from
whatever they're positioned relative to, and に when there's a verb
(あります/います) rather than です.

**Pattern: [もの]の[position]に + あります／います／です**

| Word | Kana | Meaning |
|---|---|---|
| 上 | うえ | on top of / above |
| 下 | した | under / below |
| 中 | なか | inside |
| 外 | そと | outside |
| 前 | まえ | in front of |
| 後ろ | うしろ | behind |
| 横 | よこ | beside (side-by-side) |
| 隣 | となり | next to (same category of thing, e.g. neighboring building) |
| 近く | ちかく | near |
| 間 | あいだ | between (two things — takes と between the two reference nouns, then の, see example below) |

Examples:
- 机の上に本があります。(Tsukue no ue ni hon ga arimasu.) — "There's a book
  on the desk."
- コンビニは駅の隣です。(Konbini wa eki no tonari desu.) — "The convenience
  store is next to the station."

### あいだ (between) — class example

間 (あいだ) is the odd one out: it needs **two** reference nouns joined by
と before の, since "between" inherently relates two things:

> コンビニは　パンやと　ラーメンやの　あいだです。
> *Konbini wa pan-ya to raamen-ya no aida desu.*
> "The convenience store is between the bakery and the ramen shop."

Breakdown:
- パンや (pan-ya) — "bakery" (パン "bread" + や, the shop-name suffix seen
  in 花屋/hanaya "flower shop", 本屋/honya "bookshop")
- ラーメンや (raamen-ya) — "ramen shop"
- パンや**と**ラーメンや — "the bakery **and** the ramen shop"
- （パンやとラーメンや）**の**あいだ — "the between **of** (the bakery and
  the ramen shop)" → "between the bakery and the ramen shop"
