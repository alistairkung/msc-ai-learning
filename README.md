# MSc AI Learning Repository

This repository is the durable record and planning system for my MSc AI preparation and study.

It serves two purposes at once:

1. **Evidence of learning** — exercises and tests show what I have actually implemented.
2. **Continuity of learning** — context files and lesson logs preserve where I am, why we are learning each topic, what has been parked, what the MSc will demand next, and how to retrieve prior lessons later.

The repository exists because a long-running tutoring conversation is excellent for interactive learning but is not a reliable place to keep the entire evolving curriculum in active context. The repo is therefore the persistent source of truth that future study sessions can reload.

---

## Repository structure

```text
.
├── README.md
├── LEARNING_ROADMAP.md
├── LEARNING_STATE.md
├── MSC_SYLLABUS_MAP.md
├── foundations/
│   ├── python/        (lessons 01-07)
│   ├── dsa/            (lessons 08-09)
│   ├── numpy/          (lessons 10-11, 15)
│   ├── pandas/         (lessons 18-20)
│   └── retrieval/      (lessons 13, 17)
├── machine_learning/
│   ├── fundamentals/   (lessons 12, 14, 16)
│   ├── classification/logistic_regression/ (lessons 21-22)
│   └── regression/     (lesson 23)
├── classical_ai/
│   └── search/         (lessons 24-26)
├── deep_learning/
│   ├── tensor_operations/     (lesson 27)
│   ├── autograd/               (lesson 28)
│   ├── pytorch_fundamentals/   (lesson 29)
│   └── mlp/                    (lessons 30-31)
└── lesson_logs/
    ├── lesson30_binary_classification.md
    └── ...
```

Each topic directory holds a lesson's exercise and its test side by side (`lessonNN_topic.py` + `test_lessonNN_topic.py`), so a topic folder is self-contained. `STRUCTURE_PROPOSAL.md` records the design rules behind this layout.

### Topic directories (`foundations/`, `machine_learning/`, `classical_ai/`, `deep_learning/`)

The implementation record, organised by knowledge domain rather than chronology. Each lesson's exercise module and its test module live together in the same topic folder.

Examples include Python fundamentals, DSA patterns, NumPy/Pandas, sklearn pipelines, BFS/DFS/A*, autograd, PyTorch training loops and neural networks.

An exercise proves that a topic was implemented at least once. It does **not by itself prove cold-recall mastery**.

Tests provide a concrete definition of whether an implementation behaves as expected. They are particularly useful while learning because they answer the question: **"How do I know what I wrote actually works?"**

Not every future ML experiment needs to become a unit test, but pytest remains useful for deterministic contracts, shape checks, pipeline behaviour and small end-to-end learning checks.

### `lesson_logs/`

The conceptual and retrieval record for individual lessons.

A lesson log should capture:

- what was learned;
- what was implemented;
- why each concept matters;
- important distinctions or misconceptions;
- known fragile points;
- a bank/style of cold-retrieval questions;
- the mastery signal for that lesson;
- any bridge into the next lesson.

The aim is that months later I can say:

> **"Cold retrieve lesson 30."**

and a tutor/model can recreate the same style of interactive questioning without needing the original conversation.

Lesson logs are not transcripts. They should be compact **retrieval blueprints**.

---

# The three context files

These files deliberately operate at different timescales.

## `LEARNING_STATE.md` — operational / current

This is the **first file to read when resuming study**.

It should answer:

- Where am I right now?
- What am I comfortable with?
- What is still fragile?
- What is actively being learned?
- What has been deliberately parked?
- What should the next session probably do?

It contains the important **`PARKED / MUST RETURN`** register so an intentionally paused topic cannot silently disappear from the curriculum.

**Update frequency:** every study session.

Keep this file concise. It is a handover, not a history book.

---

## `MSC_SYLLABUS_MAP.md` — tactical / course-facing

This maps preparation against the actual MSc teaching sequence.

It should answer:

- What is each course about to expect?
- What prerequisites does that topic need?
- How ready am I today?
- What should be learned before that week arrives?
- Where can two courses reinforce each other?

This is the main tool for maintaining a roughly **1–2 week learning buffer** ahead of live course content while also protecting longer-range prerequisite work, especially the maths needed for Machine Learning Theory.

**Update frequency:** when lecture reality, syllabus timing, an assignment, readiness, or course priorities materially change.

Do not rewrite it after every ordinary lesson.

---

## `LEARNING_ROADMAP.md` — strategic / long-term

This is the slow-changing master curriculum.

It should answer:

- What are the major learning tracks?
- Why are we learning them?
- What prerequisites and dependencies connect them?
- What later concepts does each topic unlock?
- What is the longer-term destination beyond the next lecture?

It prevents local session choices from gradually distorting the overall curriculum.

**Update frequency:** only when strategy genuinely changes — for example a major track is completed, a prerequisite dependency is discovered, course plans change, or priorities are materially re-ordered.

---

# How a normal study session uses the repo

## Before the session

1. Read `LEARNING_STATE.md`.
2. Check the next 1–2 relevant MSc weeks in `MSC_SYLLABUS_MAP.md`.
3. Consult `LEARNING_ROADMAP.md` if choosing between competing longer-term priorities.
4. If the session builds directly on an earlier lesson, inspect its exercise/test and lesson log.
5. Choose the highest-value intersection of:
   - upcoming MSc demand;
   - prerequisite weakness;
   - cold-recall fragility;
   - long-term AI/ML engineering value.

## During the session

The preferred teaching style is:

- one small question at a time;
- cold retrieval before explanation where appropriate;
- concrete examples and tensor shapes;
- derive the idea before hiding it behind an API;
- hints/scaffolding rather than immediately providing full solutions;
- immediate feedback after answers;
- distinguish a mental/arithmetic slip from a conceptual gap;
- re-test missed concepts soon afterwards with changed numbers/context;
- use implementation and debugging to make abstract ideas concrete;
- use pytest when a clear executable contract helps define "working".

Retrieval should normally be **timeboxed to around 10–15 minutes** so it maintains older knowledge without consuming the whole session.

## After the session

Use this short protocol:

1. Commit new/updated exercise and test files.
2. Create or update the relevant `lesson_logs/lessonNN_*.md` retrieval blueprint.
3. Update `LEARNING_STATE.md`:
   - completed;
   - now comfortable with;
   - still fragile;
   - newly parked/unparked;
   - next logical step.
4. Update `MSC_SYLLABUS_MAP.md` only if readiness/course timing materially changed.
5. Update `LEARNING_ROADMAP.md` only if the strategy/dependency map materially changed.

The maintenance step should stay lightweight. If updating context starts feeling like homework, the system is becoming too heavy.

---

# Instructions for tutor models / AI assistants

If you are an AI tutor/model helping with this repository, **do not treat every file as interchangeable context**. They have different roles and authority.

## Recommended read order when resuming a learning session

### 1. Read `LEARNING_STATE.md` first

Use it as the operational handover.

It tells you what is current, fragile, parked and next. Do not choose a new learning direction solely from the most recent exercise or from whatever topic appears most interesting.

### 2. Read the relevant part of `MSC_SYLLABUS_MAP.md`

Use it to understand what the MSc is about to demand and how urgent the topic is.

The planning question is:

> **Given what the learner knows today, what the MSc is about to demand, and the longer-term goal of strong AI/ML engineering competence, what is the highest-value thing to work on next?**

### 3. Read `LEARNING_ROADMAP.md` when making strategic choices

Use it to preserve prerequisite chains and longer-term goals. It should prevent tunnel vision around whatever was taught most recently.

### 4. Read the relevant exercise/test files as implementation evidence

These answer **what has actually been coded**.

Do not assume that because code exists, every underlying concept is now fluent under cold recall. Conversely, do not claim a topic was never studied if a verified exercise exists.

### 5. Read the relevant `lesson_logs/` file for retrieval or lesson continuation

This is especially important when asked things such as:

- "cold retrieve lesson 30";
- "review the BFS lesson";
- "continue where we left off in lesson N".

Use the lesson log to recover the intended conceptual distinctions, fragile points and question style.

---

## Source-of-truth hierarchy

Use these sources for different claims:

| Question | Primary source |
|---|---|
| What did I actually implement? | `exercises/` + `tests/` |
| What should I be able to explain/retrieve from a lesson? | `lesson_logs/` |
| Where am I right now? | `LEARNING_STATE.md` |
| What is coming in the MSc and how ready am I? | `MSC_SYLLABUS_MAP.md` |
| Why are we learning this and what does it unlock? | `LEARNING_ROADMAP.md` |

If these appear to disagree, **do not silently reconcile them**. Inspect the evidence and update the appropriate context file.

A useful distinction:

- exercise exists = **implemented/practised**;
- lesson log mastery signal = **intended understanding**;
- learning state = **current observed readiness**.

Current observed readiness should not be inferred from code alone.

---

## How to run cold retrieval

When asked to cold retrieve a lesson:

1. Fetch that lesson's log.
2. Also inspect its exercise/test if useful.
3. Do **not** dump a summary first.
4. Ask one question at a time.
5. Change numbers/examples so recall is conceptual rather than memorised.
6. Start with core concepts, then probe known fragile points.
7. If an answer is wrong, give concise feedback and re-test the concept shortly afterwards.
8. Stop once retention is clear; do not mechanically exhaust the entire question bank.
9. Timebox a normal retrieval to ~10–15 minutes unless the learner asks for a deeper review.

If a lesson does not yet have a lesson log, reconstruct it from the exercise/test plus available learning context, then create one at the end of the session.

---

## How to choose the next lesson

Do not simply continue the newest topic indefinitely.

Before choosing, check:

1. **Upcoming demand** — what appears in the next 1–2 MSc weeks?
2. **Dependencies** — what prerequisite unlocks several later topics?
3. **Fragility** — what previously learned concept is decaying under cold recall?
4. **Application** — can theory and implementation be joined in one exercise?
5. **Long-range risk** — especially probability/statistics/linear algebra for Machine Learning Theory.
6. **Parked topics** — does anything in `PARKED / MUST RETURN` now have a timing reason to reactivate?

Do not let conversational recency dominate this decision.

---

## How to update the files

### Update `LEARNING_STATE.md` after every substantive study session

Record outcomes, not a transcript.

Prefer statements like:

> "BFS implementation cold-recalled successfully; completeness/optimality comparison still fragile."

rather than:

> "We spent 40 minutes talking about BFS and answered 12 questions."

### Update `MSC_SYLLABUS_MAP.md` only when course-facing readiness changes

Examples:

- a topic moves Red → Amber after a first lesson;
- lecture notes reveal a deeper maths requirement;
- an assignment makes a topic urgent;
- actual course sequencing differs from the original syllabus.

### Update `LEARNING_ROADMAP.md` sparingly

Examples:

- discovering that probability must be accelerated before ML Theory;
- completing a whole learning track;
- adding/removing a major course;
- changing the long-term destination.

Do not turn it into a chronological diary.

### Create/update a `lesson_logs/` file when a lesson creates reusable understanding

The log should be detailed enough that another tutor can recreate a useful cold review months later, but short enough to scan quickly.

---

# Design principles

### Durable, not exhaustive

The repository should preserve the pieces that matter for future decisions and retrieval, not every conversational detail.

### Evidence + understanding

Code/tests show implementation; lesson logs and learning state capture understanding. We need both.

### Retrieval over rereading

The goal of lesson logs is to enable active recall, not to create another set of notes to passively reread.

### Syllabus-aware, not syllabus-limited

Preparation should help with immediate MSc demands while still building toward strong practical AI/ML engineering and the mathematical foundations needed later.

### Depth before indiscriminate breadth

Being able to explain why a training loop works, trace tensor shapes, derive a gradient, or compare search algorithms is more valuable than briefly touching many advanced topics with no durable mental model.

### Lightweight maintenance

The workflow exists to improve learning, not to create administrative overhead.
