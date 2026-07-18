# Weak Areas

Standing list of areas to quiz proactively — see `CLAUDE.md` ("Known weak
areas") for the instruction to work these into practice without being asked.
Add to this file as new weak spots come up (quiz mistakes, self-identified,
or flagged by the girlfriend/teacher).

## Vocab: 椅子 (いす, isu, "chair")

Flagged from class (2026-07-11). Mnemonic: same kanji as Mandarin 椅子
(yǐzi, "chair") — that's also why the pronunciation is reminiscent
("isu" ≈ "yi zi"). Watch for confusing it with **いつ (itsu, "when")** —
different word, つ vs す is the easy typo/misreading here.

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

## Vocab: すっかり (sukkari, "completely / entirely")

Flagged from class (2026-07-18) — sensei used すっかり忘れました ("completely
forgot"). Adverb meaning *completely / thoroughly*, with a nuance of a **full
change into a new state** (not just "very"). Pairs naturally with verbs of
becoming/finishing/forgetting: すっかり忘れました, すっかり元気になりました
("fully recovered"), すっかり春ですね ("it's completely spring now").

Nuance vs neighbors:
- **すっかり** — completely, with a sense of *transformation into a new state*.
- **完全に** (かんぜんに) — completely, neutral/clinical ("100%, perfectly").
- **全然** (ぜんぜん) — "(not) at all," usually needs a negative (全然わからない).

## Grammar: あげます (agemasu, "to give") + giving/receiving verbs

Flagged from class (2026-07-18). **Pattern: [giver は] [person に] [thing を]
あげます** — に marks the recipient ("to [person]"), を marks the thing given.

> （私は）友達に プレゼントを あげます。
> *(watashi wa) tomodachi ni purezento wo agemasu.*
> "I give a present to my friend."

**Key trap — direction matters.** あげる = give *outward, away from me/my side*.
Works for: I → someone else (私は彼にあげます), or third party → third party
(田中さんは山田さんにあげます). But you **cannot** use あげる for someone giving
*to you* — "my friend gives me a present" is NOT 友達は私にあげます; that switches
to **くれます**. The giving/receiving trio:

| Verb | Direction | Meaning |
|---|---|---|
| あげます | I / someone → outward (away from me) | give |
| くれます | someone → me / my in-group | give (to me) |
| もらいます | I → receive from someone | receive |

Today's focus is あげます; just remember くれます exists for gifts coming *your*
way, and もらいます for receiving.

## Interjections: へえ / え〜 / えっ / ええ (surprise sounds)

Flagged from class chat (2026-07-18). These あいづち/interjections sound similar
but do different jobs — easy to blur.

- **へえ（〜）** — *impressed / "didn't know that, interesting!"* — positive-ish
  surprise. Reaction to a fun fact. NOT English "hey" (false friend — "hey"
  gets attention; へえ is a *response*). Closest English: "ohh / huh / TIL."
  へえ〜 stretched = more impressed.
- **えっ！** (short, sharp) — *"Huh?! What?!"* startled/shocked.
  えっ！本当ですか？
- **え〜** (stretched, the whiny "ehhhh") — *surprise + doubt / reluctance /
  dismay*: disbelief (え〜、うそでしょ！ "you're kidding!"), reluctance
  (え〜、行きたくない〜 "ehh, I don't wanna~"), disappointment
  (え〜、もう終わり？ "ehh, over already?").
- **ええ** (two-mora, flat — NOT drawn out) — soft polite **"yes"** (warmer than
  うん): ええ、そうです。

Key contrast: **へえ** = "oh cool, TIL" (positive); **え〜** = "ehh, really…? /
awww / ugh" (doubt/reluctance). Fun fact → へえ〜; bad news / hard to believe →
え〜. And watch ええ ("yes") vs え〜 ("ehh, doubt") — same kana neighbors, opposite
meanings, told apart by length + pitch.

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
