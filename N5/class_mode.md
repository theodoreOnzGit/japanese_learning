# Class Mode

Live scaffold for when the user is **in class** and using the chat as a
scratchpad. Sibling to `quiz_mode.md` (short drilling rounds) and `exam_mode.md`
(full timed papers).

**Trigger on:** "class mode", "class mode on", "I'm in class", "starting class".
**Trigger off:** "class over", "done", "class mode off", "finished", or the user
otherwise signalling the lesson has ended.

While class mode is on, assume every message is a fast, low-effort jotting made
under time pressure. Typos are expected and are not necessarily errors worth
logging (see *Typos* below).

---

## 1. The three message types

Every incoming message is one of these. **Identify which before replying** — the
handling differs sharply.

| Type | What it is | Handling |
|---|---|---|
| **Note** | Something sensei said, or a word/phrase from the lesson | Log it. Reply in one or two lines. |
| **Question** | The user asking about Japanese | Answer at sensei's level. Log the underlying gap. |
| **Production** | The user's *own* attempt at Japanese | Correct it, **and record it as evidence** toward the mastery bar. |

### Signals

**Note:** "from class:", "sensei said", "more class notes:", "also:", "and:",
a bare item with no question mark, a vocabulary gloss ("つかれました means got
tired").

**Question:** ends in "?", "right?", "is it…", "how do I say", "what's the
difference", "can I use…".

**Production:** "I would say…", "can I say…", "I wrote…", "is this okay:", or a
Japanese sentence given in direct answer to a drill Claude set.

### The ambiguous case — and the default

A **bare Japanese sentence with no framing** is the hard case. It could be
sensei's example or the user's own attempt, and the two are handled oppositely.

**Default: treat it as a NOTE (class input), not production.**

Rationale: the costs are asymmetric. Logging sensei's sentence as the user's
production **inflates the mastery record** and can promote an item the user
cannot actually produce — corrupting the exact thing the tracking exists to
measure. Failing to credit real production merely delays a promotion, which the
next spaced repetition fixes anyway.

**When it matters, ask — in one short line, at the end of the reply.** The user
has explicitly said clarifying is welcome during class time:

> *(sensei's, or yours?)*

Ask when the sentence is **correct and would count as evidence**. Don't ask when
it contains an error — an error is worth correcting regardless of origin, and the
question can wait.

---

## 2. Reply length

**Short.** The user is listening to a teacher. A long explanation is unreadable
mid-lesson and competes with the actual class.

- **Note:** one line confirming what was logged and where.
- **Question:** the answer, plus at most one line of why. Detail goes in the
  weak-areas file, not the reply.
- **Production:** the correction, and what was right. Praise the specific thing
  that worked, not the attempt in general.

Skip: full conjugation tables, etymology, register ladders, cultural background,
cross-references to five other files. **All of that still gets logged** — it just
doesn't go in the reply.

If something genuinely needs a long explanation, say so and offer it:

> That one has a longer answer — want it now, or after class?

---

## 3. Pitch to sensei's level

`weak_areas/class_raw_notes.md` records **sensei's current teaching frontier**:
what is expected, what has been introduced but capped, and what is beyond class.
Keep replies inside that line during a lesson.

Volunteering material sensei has deliberately deferred is unhelpful mid-class —
it competes with what the user is meant to be absorbing. Log the deeper version
silently; offer it when asked or after class.

Update the frontier table whenever sensei introduces, caps, or corrects
something.

---

## 4. Logging

The standing auto-log rule from `CLAUDE.md` applies unchanged: **log everything,
don't ask permission.** In class mode, additionally:

- **Deduplicate silently.** Live jotting produces repeats. If an item is already
  filed, say so in one line and add nothing. Don't re-explain it.
- **Batch where sensible.** Several related items in a row can share one entry
  rather than fragmenting across the files.
- **Record attribution explicitly** in every entry — "from class", "sensei's
  example", "self-produced, unprompted". This is what makes the mastery bar
  meaningful later, and it cannot be reconstructed after the fact.

### Typos

Fast typing produces slips that are *not* learning gaps. Distinguish:

- **Log it** when the error reveals a real gap — a wrong reading, a missing mora
  in a word they know (とおおい, おもしかった), a wrong particle, a wrong
  adjective type.
- **Don't log it** when it is plainly mistyping — a Latin-alphabet slip, a
  transposed character in a word used correctly elsewhere in the same message.

When unsure, log it. A false positive costs one quiz question; a false negative
costs a missed gap.

---

## 5. End of class

When the user signals the lesson is over, **without being asked**:

1. Write the session into `N5.tex` → **Class Notes**, dated with the current date.
   Cover what sensei taught, worked examples, and anything corrected.
2. Confirm the weak-area files and `weak_areas/MAP.md` are current.
3. Give a short summary: what was covered, what was logged, and the one or two
   items most worth drilling before the next lesson.
4. Note any item where attribution was left unresolved, so it can be settled
   while the user still remembers.

Do not run a quiz unprompted at this point — the user has just finished a lesson.
Offer one.
