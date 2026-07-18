# Language Weak Areas

Standing list of **language** weak spots to quiz proactively — kana, vocab,
grammar, readings, particles (things about *how Japanese works*). See `CLAUDE.md`
("Known weak areas") for the instruction to work these into practice without
being asked. Add to this file as new language gaps come up (quiz mistakes,
self-identified, or flagged by the girlfriend/teacher).

**Cultural** weak spots (customs, etiquette, social context) live in the sibling
file `cultural_weak_areas.md`. Items with both angles are logged in both,
cross-referenced.

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
  四人 よにん... (only 1 and 2 are irregular). Formal counter for people is
  **名 (めい)** — 一名 いちめい, 二名 にめい (regular readings, no shifts);
  most polite (staff→customer) is 名様, e.g. 二名様（にめいさま）.
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

**Worked example (class, 2026-07-18) — watch the double に:**

> わたしは バレンタインデーに かれに チョコレートを あげます。
> *watashi wa barentaindē ni kare ni chokorēto wo agemasu.*
> "I give chocolate to my boyfriend on Valentine's Day."

The key point: に appears **twice with different jobs** — バレンタインデー**に** =
*time* ("on Valentine's Day," same に as 7時に), かれ**に** = *recipient* ("to
him"). Same particle, two functions (に marks the point/target something lands on,
whether a time or a person). Direction is correct: あげます (you → outward), not
くれます. Cultural angle: `cultural_weak_areas.md` → "バレンタインデー / ホワイトデー".

Second worked example, same double-に shape (class, 2026-07-18):

> 旧正月に こどもに お年玉を あげます。
> *kyū-shōgatsu ni kodomo ni otoshidama wo agemasu.*
> "On Lunar New Year, I give children New Year's money."

旧正月**に** = *time*, こども**に** = *recipient*. Vocab logged below (Vocab:
旧正月 / お年玉); cultural angle: `cultural_weak_areas.md` → "お年玉 / 正月 vs 旧正月".

**もらいます / もらいました (receive) — the inward verb** (class, 2026-07-18).
Pattern: **[receiver は] [giver に／から] [thing を] もらいます**. に (or から,
clearer "from") marks the giver/source; を marks the thing received.

> 友達に プレゼントを もらいました。
> *tomodachi ni purezento wo moraimashita.*
> "I received a present from my friend."

So に now has a *third* job across these verbs: **time** (バレンタインデーに),
**recipient/goal** (かれに あげます, "to"), **source** (友達に もらいます, "from").
Direction comes from the verb: あげます = outward ("to"), もらいます = inward
("from"). Trap: もらう allows に→から, but あげる's recipient に **cannot** become
から — から only works with もらう. Past-tense parallel with です: noun/copula
です→でした, verb もらいます→もらいました (both "polite past," different word types).

**Direction rule — 私にあげました is ALWAYS wrong** (class, 2026-07-18). Since
あげる flows *outward, away from the speaker*, 私 (the speaker) can never be its
recipient. "My friend gave me chocolate" has two correct forms, never あげる:

| | Sentence | Logic |
|---|---|---|
| ✅ A | 友達が 私に チョコを **くれました** | くれる = someone gives *toward me* (giver = subject) |
| ✅ B | 私は 友達に チョコを **もらいました** | もらう = *I received* (receiver = subject) |
| ❌ | ~~友達が 私に チョコを あげました~~ | あげる can't point at 私 |

Same event, different viewpoint: くれました tells it from the giver's side
(友達が…), もらいました from the receiver's side (私は…). Memory hook: gift **away
from me** → あげる; gift **toward me** → くれる (giver's view) / もらう (my view);
**私に + あげる = always wrong.**

**Extends to family / in-group (内 uchi)** (class, 2026-07-18): the "toward me"
boundary is not just literally 私 — it covers your whole **in-group** (family,
people on your side). Someone giving to your mother/brother counts as giving
*toward you*, so it also takes くれる / もらう, never あげる:

- ✅ 田中さんが 母に 花を **くれました** (giver's view)
- ✅ 母は 田中さんに 花を **もらいました** (receiver's view)
- ❌ ~~田中さんが 母に 花を あげました~~ — 母 is 内 (in-group), あげる can't
  point at her.

This is the **内 (uchi, in-group) / 外 (soto, out-group)** axis: family counts as
"me" for direction. あげる only works when the gift leaves your whole in-group to
an outsider, or passes between two outsiders. (Cultural angle:
`cultural_weak_areas.md` → "Hierarchy dictates verb choice (keigo)" — uchi/soto
is the same relational logic that governs keigo.)

**Keigo ladder — hierarchy changes the verb, not just the ending** (class,
2026-07-18). You **cannot** say あげます to a senior/superior — あげる implies
"doing them a favor" and sounds presumptuous aimed upward. The verb itself
shifts by social level. Cultural angle: `cultural_weak_areas.md` → "Hierarchy
dictates verb choice (keigo)".

- **Giving (me → other), by recipient's status:** やる (juniors/animals/plants,
  plain) → **あげる** (equals, neutral) → **さしあげる (差し上げる)** (seniors/
  superiors/customers, humble 謙譲語). "I give to a teacher" = 先生に … を
  **さしあげます**, not あげます.
- **Receiving (I receive):** **もらう** (from equals) → **いただく (頂く)** (from
  a superior, humble). 先生に 本を **いただきました**. (Same いただく as
  いただきます before eating — "I humbly receive.")
- **Other gives to me:** **くれる** (equal/junior → me) → **くださる (下さる)**
  (superior → me, honorific 尊敬語). 先生が … を **くださいました**. (Same
  くださる as ください, "please give me.")

One-liner: to a senior → **さしあげる** (not あげる); from a senior → **いただく**
(not もらう); a senior gives you → **くださる** (not くれる). 謙譲語 lowers *your*
action; 尊敬語 raises *their* action.

## です past tense: でした (+ the い-adjective trap)

Learnt in class (2026-07-18) as the past of です. です (polite copula, "is") has
a tidy four-form grid:

| | Affirmative | Negative |
|---|---|---|
| Non-past ("is") | です | じゃないです / ではありません |
| Past ("was") | **でした** | じゃなかったです / ではありませんでした |

- 学生でした。"I was a student." / 昨日は雨でした。"It was rainy yesterday."
- **Trap:** でした attaches to **nouns and な-adjectives**, NOT い-adjectives.
  い-adjectives carry their own past: おいしい → **おいしかったです** ("was
  delicious"), NOT ~~おいしいでした~~. So 静かでした ✓ (な-adj), 先生でした ✓
  (noun), but よかったです ✓ / ~~いいでした~~ ✗ (い-adj).

## Vocab: だめ (駄目, "no good / not allowed / no")

Learnt in class (2026-07-18). だめ (usually written だめ or ダメ; kanji 駄目) =
"no good, not allowed, must not, hopeless." Uses:
- **"No / not allowed":** だめです ("that's not OK / you can't"). Refusing or
  forbidding — stronger/blunter than a soft いいえ.
- **"No good / broken / hopeless":** このペンはだめです ("this pen is no good").
- Pairs with てはいけない grammar later (〜てはだめ = "must not …").

Note it's a な-adjective/noun, so past = だめでした ("was no good"), negative =
だめじゃない.

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

## Vocab: 旧正月 / お年玉

Flagged from class (2026-07-18), via 旧正月に こどもに お年玉を あげます.

- **旧正月（きゅうしょうがつ）** — "Lunar New Year." 旧 (きゅう, "old/former") +
  正月 (しょうがつ, "New Year"). Reading note: 正月 = しょう**がつ**. Contrast
  plain **正月（しょうがつ）** = the *Gregorian* New Year (Jan 1, the big Japanese
  holiday) vs **旧正月** = the *lunar* one (Chinese/Korean/Vietnamese 春節 style).
  Cultural detail: `cultural_weak_areas.md` → "お年玉 / 正月 vs 旧正月".
- **お年玉（おとしだま）** — "New Year's money gift for children." お (polite) +
  年 (とし, "year") + 玉 (だま, rendaku from たま, "ball/gem"). The custom itself
  is logged under Culture.

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
