# Exam Mode

A scaffold for synthesising full mock exams in the **Cambridge IGCSE Japanese
(0716)** format, with answer keys. Sibling to `quiz_mode.md` — that file is for
short, targeted drilling; this one is for sit-down timed papers.

**Trigger:** "give me an exam", "mock paper", "IGCSE practice", "exam mode",
"make me a reading paper".

Source papers (2027 specimen set, converted with `kopitiam pdf2md`):
`../resources/exams/markdown/`. Citation and copyright note:
`../resources/cambridge-igcse-japanese-0716.md`.

**Copyright rule:** synthesised papers must be *original* — same structure, mark
allocation and question types, **new** texts and items. Never reproduce Cambridge
question text, passages or distractors. The format is the template; the content
is ours.

---

## Part 1 — The format (studied from the 2027 specimen set)

### Overview

| Paper | Skill | Time | Marks | Format |
|---|---|---|---|---|
| 1 | Listening | ~50 min (incl. 6 min transfer) | 40 | 37 MC questions |
| 2 | Reading | 1 hour | 40 | matching + MC + open Japanese answers |
| 3 | Speaking | ~10 min (+10 min prep) | not stated on candidate card | role play + 2 topic conversations |
| 4 | Writing | 1 h 15 min | 45 | form + short composition + long composition |

Standing conventions across all papers: **no dictionaries**; rubrics are in
Japanese; marks shown in square brackets `[1]`; each section ends with a
`[ごうけい: N]` subtotal; harder kanji carry furigana.

### Paper 1 — Listening (40 marks, 37 questions)

| Qs | Task | Options | Audio | Marks |
|---|---|---|---|---|
| 1–8 | Picture MC — eight short conversations | A–D | each heard twice | 8 |
| 9–14 | Monologue (e.g. a tour guide), split in two | A–D | twice | 6 |
| 15–19 | Match statements to items (e.g. places in a town) | A–F | twice | 5 |
| 20–28 | Conversation in two halves | A–C | twice | 9 |
| 29–34 | Conversation in two parts | A–D | twice | 6 |
| 35–37 | **Choose TWO** correct statements per segment | A–E | twice | 6 (2 each) |

Notes that matter when synthesising:
- Difficulty climbs: concrete objects/times early → opinions, reasons and
  inference late. Q29–34 asks about *meaning and intent* (e.g. what a gesture
  signified); Q35–37 requires holding several facts at once.
- Split-audio sections print `[休止]` (pause) between halves.
- Every section says 話を聞く前に、もんだいを読みなさい (read the questions first).
- **We have no audio.** In this repo, Paper 1 is delivered as a *transcript-based*
  paper: give the script, then the questions. Flag it as an adaptation.

### Paper 2 — Reading (40 marks)

| Q | Task | Options | Marks |
|---|---|---|---|
| 1 | Match sentences to pictures | A–F | 5 |
| 2 | Match sentences to signs/displays (e.g. supermarket) | A–H | 5 |
| 3 | MC on a short first-person diary text | A–C | 7 |
| 4 | Open questions, **answered in Japanese**, on an informative text | — | 12 |
| 5 | Open questions, **answered in Japanese**, on a longer text | — | 11 |

- Q1–2 are pure vocabulary recognition; Q3 is gist plus detail; Q4–5 require
  producing Japanese, not selecting it.
- Q4–5 texts run 300–500 characters, first-person or descriptive, on a concrete
  topic (a town, a school, a hobby).
- Occasional two-part items: `(g)(i)`/`(g)(ii)`, and "文中から二つ書いてください"
  (give two, one mark each).
- **Since pictures can't be drawn here**, Q1–2 are adapted: replace images with
  short labelled text descriptions (see Part 2).

### Paper 3 — Speaking (~10 min, 10 min preparation)

Three parts, on a candidate card:

1. **ロールプレイ** (~2 min) — a scenario, one line of setup, plus who plays whom.
   Specimen scenarios are small everyday negotiations: 動物園に行きたい,
   映画館に行きたい, talking to another traveller.
2. **会話 1** (4 min) — topic conversation, examiner opens.
3. **会話 2** (4 min) — second topic conversation, examiner opens.

The card gives the candidate *only* the scenario — never the questions. Rubric
is always 先生が会話をはじめます。ぜんぶのしつもんにこたえてください。

### Paper 4 — Writing (45 marks, 1 h 15)

| Q | Task | Length | Marks |
|---|---|---|---|
| 1 | Fill in a form in Japanese (e.g. a homestay form) | words/phrases | 5 |
| 2 | Short composition from 4 bullet prompts | 160–180 字 | 12 |
| 3 | **Choose (a) or (b)** — long composition from 5 bullet prompts | 250–300 字 | 28 |

**The bullet prompts follow a fixed escalation.** This is the single most
reusable pattern in the whole exam:

*Question 2 (4 bullets):* describe something present → a habit → another habit
or a "how do you…" → a future wish **with a reason**.

*Question 3 (5 bullets):* past event → past detail → habit **+ why** → future
desire → **a general/societal question** (どんな食生活が体にいいですか /
どんな旅行がかんきょうにいいですか).

That last bullet is always abstract and always the discriminator — it's where the
28-mark question separates candidates. Both 3(a) and 3(b) in the specimen follow
it exactly.

Question 1 forms ask for: 名前・国・年・ペット・しゅみ（2つ）・好きな食べ物・
アレルギー — single words or short phrases, not sentences.

---

## Part 2 — Adaptations for this repo

Three things the real papers rely on that we can't reproduce. Always state which
adaptation is in force at the top of a synthesised paper.

| Real paper | Our adaptation |
|---|---|
| **Audio** (Paper 1) | Print the transcript. Either let them read it twice then hide it, or have them answer from the text. Note it changes the skill being tested. |
| **Pictures** (P1 Q1–8, P2 Q1–2) | Replace each image with a bracketed English description: `A [a house by the sea]`. Keep the letter labels and the matching mechanic. |
| **Live examiner** (Paper 3) | Claude plays 先生. Give the candidate card, allow 10 minutes' preparation, then run the role play turn by turn in chat. |

---

## Part 3 — Synthesis protocol

### Choosing a level

IGCSE sits around **CEFR A2–B1 ≈ JLPT N4**, above the user's working level. Every
synthesised paper declares one of:

- **`N5`** — vocabulary and grammar capped at N5. Keeps the IGCSE *structure* but
  lowers the content. The default.
- **`N5+`** — N5 core with a stretch section (usually the last reading text or the
  28-mark composition). **Recommended** — matches how the real papers escalate.
- **`IGCSE`** — faithful to the specimen level, i.e. N4-ish throughout. Use for
  the study partner, or when the user explicitly wants the real thing.

### Building the paper

1. **Pick the paper** (1/2/3/4) and level. If unspecified, default to Paper 2 at
   `N5+` — reading is the most useful format without audio.
2. **Mine the weak areas.** Read `mistakes_and_learning_pts/weak_areas/MAP.md`
   and seed items from `shaky` entries first. An exam is worth more when it
   double-counts as targeted drilling. Aim for **at least a third** of items to
   touch a tracked weak area, and note which in the key.
3. **Match the mark allocation exactly** — 5/5/7/12/11 for Paper 2, 5/12/28 for
   Paper 4, and so on. Print `[1]` per item and `[ごうけい: N]` per section.
4. **Keep the rubrics in Japanese**, copied in *form* from the specimen
   (つぎの文章を読みなさい。/ ただしい文字を書きなさい。/ 日本語でしつもんに
   こたえなさい。) — these are generic instructions, not protected content.
5. **Furigana on anything above the declared level.** The specimen does this
   constantly; it's how a paper stays fair while using a hard word.
6. **Write the texts fresh.** Concrete, first-person or descriptive, on an
   everyday topic. The user's own interests are fair game — a passage about
   双葉町 or a dosimeter is more engaging than a generic one, and reuses vocabulary
   already logged.
7. **Escalate within the paper**, as the specimen does: recognition → gist →
   detail → inference → production.

### Answer keys

Every synthesised paper ships with a key, in a **separate section under a clear
`---` break** so it can be scrolled past. The key gives, per item:

- the **answer**;
- for open-response items, the **acceptable range** — Cambridge marks meaning,
  not exact wording, so list what else scores (e.g. "にんじゃ / にんじゃで有名
  — either accepted; 忍者 in kanji accepted");
- **one line of why**, tied to a grammar point or a tracked weak area;
- a **weak-area tag** where relevant: `→ travel_and_transport.md: 乗る/降りる`.

For the compositions (P4 Q2/Q3) a key is not an answer — supply instead:
- a **model answer** at the target length;
- the **bullet-coverage checklist** (all bullets must be addressed — missing one
  is the most common lost mark);
- a short **mark-band guide**: content/coverage, accuracy, range of structures.

### After marking

Apply the `quiz_mode.md` end-of-round rule: **every miss gets logged.** Demote
the matching weak-area entry to `shaky` with the date, or create a new entry in
the right theme file, and update `weak_areas/MAP.md` in the same pass.

---

## Part 4 — Reusable question stems

Lifted in *shape* from the specimen (generic instructions, not content):

**Matching:** `(a)–(e) の 文について、ただしい 文字（A–F）を □に 書きなさい。`
**MC:** `それぞれの しつもんの ただしい こたえを えらんで、（A–C）に を 書きなさい。`
**Open reading:** `つぎの 文章を 読んで、日本語で しつもんに こたえなさい。`
**Two answers required:** `文中から 二つ 書いてください。`
**Choose two:** `それぞれの しつもんの ただしい こたえを 二つ えらんで、（A–E）に を 書きなさい。`
**Composition:** `げんこうようしに、160–180 字の 日本語で 書きなさい。`
**Choice question:** `下の 3(a) と 3(b) から 一つ えらびなさい。`
**Role play:** `先生が 会話を はじめます。ぜんぶの しつもんに こたえてください。`

Common question words for Q4/Q5 open items: 何で / どうして / どこに / どんな /
いつ / どうやって / だれが / 何を.

---

## Part 5 — Output conventions

- One paper per file under `N5/exams/`, named
  `paper<N>-<level>-<NN>.md` (e.g. `paper2-n5plus-01.md`).
- Front matter block at the top: paper, level, time, total marks, adaptations in
  force, date generated.
- Answer key in the same file, below a `---` and a `# Answer Key` heading, so the
  paper can be attempted first without seeing it.
- Plain Markdown, not LaTeX — these are practice papers, not repo notes. Anything
  worth keeping gets distilled into `N5.tex` or a weak-areas file afterwards.
