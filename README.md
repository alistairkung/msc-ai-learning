# MSc AI Learning Repository

This repository is the durable record and planning system for my MSc AI preparation and study.

## [📊 Open the Learning Dashboard](https://alistairkung.github.io/msc-ai-learning/)

**Live view of current focus, MSc readiness, the knowledge map, retrieval state and the Lessons 01–31+ learning timeline.** The dashboard is generated from `learning_progress.yaml` and updates after relevant changes are merged to `main`.

It serves two purposes at once:

1. **Evidence of learning** — exercises and tests show what I have actually implemented.
2. **Continuity of learning** — context files and lesson logs preserve where I am, why we are learning each topic, what has been parked, what the MSc will demand next, and how to retrieve prior lessons later.

The repository exists because a long-running tutoring conversation is excellent for interactive learning but is not a reliable place to keep the entire evolving curriculum in active context. The repo is therefore the persistent source of truth that future study sessions can reload.

> **Tutor/model/agent:** read `SESSION_WORKFLOW.md` for the canonical start-of-session and end-of-session protocol. In particular, `learning_progress.yaml` is deliberately maintained from observed learning outcomes; it is **not automatically generated from the Markdown files**.

---

## Repository structure

```text
.
├── README.md
├── SESSION_WORKFLOW.md
├── LEARNING_ROADMAP.md
├── LEARNING_STATE.md
├── MSC_SYLLABUS_MAP.md
├── learning_progress.yaml
├── dashboard/
├── foundations/
│   ├── calculus/      (historical pre-repo retrieval blueprint)
│   ├── linear_algebra/ (historical JHU retrieval sequence)
│   ├── python/        (lessons 01-07)
│   ├── dsa/           (lessons 08-09)
│   ├── numpy/         (lessons 10-11, 15)
│   ├── pandas/        (lessons 18-20)
│   └── retrieval/     (lessons 13, 17)
├── machine_learning/
│   ├── fundamentals/  (lessons 12, 14, 16)
│   ├── classification/logistic_regression/ (lessons 21-22)
│   └── regression/    (lesson 23)
├── classical_ai/
│   └── search/        (lessons 24-26)
├── deep_learning/
│   ├── tensor_operations/     (lesson 27)
│   ├── autograd/              (lesson 28)
│   ├── pytorch_fundamentals/  (lesson 29)
│   └── mlp/                   (lessons 30-31)
└── lesson_logs/
    ├── historical_calculus_foundations.md
    ├── historical_linear_algebra_01_linear_systems_vector_spaces.md
    ├── historical_linear_algebra_02_matrices_eigenvalues_diagonalization.md
    ├── historical_linear_algebra_03_orthogonality_projections_least_squares.md
    ├── historical_linear_algebra_04_symmetric_quadratic_forms.md
    ├── lesson30_binary_classification.md
    └── ...
```

Each numbered topic directory holds a lesson's exercise and its test side by side (`lessonNN_topic.py` + `test_lessonNN_topic.py`), so a topic folder is self-contained.

Important pre-repository maths is intentionally different: the historical calculus and JHU linear-algebra tracks were learned interactively through chat/pen-and-paper before the numbered exercise/test workflow existed. They are preserved as retrieval blueprints rather than being assigned invented lesson numbers or fabricated tests.

### Topic directories

The implementation record, organised by knowledge domain rather than chronology. Each numbered lesson's exercise module and its test module live together in the same topic folder.

An exercise proves that a topic was implemented at least once. It does **not by itself prove cold-recall mastery**.

Tests provide a concrete definition of whether an implementation behaves as expected. Not every future ML experiment needs to become a unit test, but pytest remains useful for deterministic contracts, shape checks, pipeline behaviour and small end-to-end learning checks.

Historical foundation directories such as `foundations/calculus/` and `foundations/linear_algebra/` instead explain what was learned before the repo workflow, where the retrieval logs live, the evidence boundary, and how to rebuild familiarity later without pretending the historical study happened as numbered code lessons.

### `lesson_logs/`

The conceptual and retrieval record for individual lessons and historical foundation blocks. A lesson log should capture what was learned and implemented, why it matters, important distinctions, known fragile points, cold-retrieval prompts, mastery signals and the bridge to the next lesson.

The aim is that months later I can say **“Cold retrieve lesson 30”**, **“Cold retrieve calculus foundations”**, or **“Cold retrieve linear algebra: projections and least squares”** and a tutor/model can recreate useful interactive questioning without needing the original conversation.

Lesson logs are not transcripts. They should be compact retrieval blueprints.

---

# Context and state files

These files deliberately operate at different timescales.

## `LEARNING_STATE.md` — operational / current

This is the **first learning-state file to read when resuming study**. It answers where I am now, what is comfortable or fragile, what is active or parked, and what the next session should probably do.

It contains the important **`PARKED / MUST RETURN`** register so an intentionally paused topic cannot silently disappear from the curriculum.

**Update frequency:** every substantive study session. Keep it concise; it is a handover, not a history book.

## `learning_progress.yaml` — structured / dashboard-facing

This is the structured state used to generate the learning dashboard. It records qualitative topic state, retrieval state, known gaps, current priorities, MSc readiness and the lesson timeline.

**It is not generated from `LEARNING_STATE.md` or lesson logs.** The tutor/model assesses the evidence from the session and updates YAML only when structured state materially changes.

Examples include a retrieval-due topic becoming current after successful cold retrieval, a known gap being resolved, an upcoming topic moving from planned to developing, or a new lesson being added to the timeline.

Do not invent numeric mastery percentages and do not churn this file after every session when nothing meaningful changed.

**Update frequency:** only when dashboard-relevant state materially changes.

## `MSC_SYLLABUS_MAP.md` — tactical / course-facing

This maps preparation against the actual MSc teaching sequence: what each course is about to expect, prerequisites, current readiness and what should be learned before that week arrives.

It supports a roughly **1–2 week learning buffer** ahead of live course content while protecting longer-range prerequisites, especially maths for Machine Learning Theory.

**Update frequency:** when lecture reality, syllabus timing, an assignment, readiness, or course priorities materially change. Do not rewrite it after every ordinary lesson.

## `LEARNING_ROADMAP.md` — strategic / long-term

This is the slow-changing master curriculum: major learning tracks, prerequisites, dependencies, what topics unlock and the longer-term destination beyond the next lecture.

**Update frequency:** only when strategy genuinely changes — for example a major track is completed, a prerequisite dependency is discovered, course plans change, or priorities are materially reordered.

---

# How a normal study session uses the repo

`SESSION_WORKFLOW.md` is the canonical detailed protocol. The short version is below.

## Before the session

1. Read `SESSION_WORKFLOW.md` if the workflow is not already known.
2. Read `LEARNING_STATE.md`.
3. Check the next 1–2 relevant MSc weeks in `MSC_SYLLABUS_MAP.md`.
4. Consult `LEARNING_ROADMAP.md` if choosing between competing longer-term priorities.
5. Inspect relevant exercise/test and lesson log when building on prior work; for pre-repo maths, inspect the matching historical retrieval log instead.
6. Choose the highest-value intersection of upcoming MSc demand, prerequisite weakness, cold-recall fragility and long-term AI/ML engineering value.

## During the session

Preferred teaching style:

- one small question at a time;
- cold retrieval before explanation where appropriate;
- concrete examples and tensor shapes;
- derive the idea before hiding it behind an API;
- hints/scaffolding rather than immediately providing full solutions;
- immediate feedback;
- distinguish a mental/arithmetic slip from a conceptual gap;
- re-test missed concepts soon afterwards with changed numbers/context;
- use implementation and debugging to make abstract ideas concrete;
- use pytest when a clear executable contract helps define “working”.

Retrieval should normally be timeboxed to around **10–15 minutes** so it maintains older knowledge without consuming the whole session.

For historical maths foundations, retrieval should normally begin from the smallest relevant blueprint rather than replaying the whole course. If familiarity has genuinely decayed, follow the recorded rebuild sequence from concrete examples back to the abstraction.

## After the session

A user instruction such as:

> **“Session’s over. Update the learning state, lesson log, and learning progress YAML if anything materially changed.”**

means:

1. Preserve new/updated exercise and matching test files when implementation changed.
2. Create/update the relevant `lesson_logs/lessonNN_*.md` retrieval blueprint (or the relevant historical foundation log for pre-repo maths).
3. **Always update `LEARNING_STATE.md` after a substantive session** with outcomes, fragile points, parked/unparked work, blockers and the next logical step.
4. **Update `learning_progress.yaml` only if structured dashboard state materially changed** — topic status, retrieval status, known gaps, current/next focus, MSc readiness, or the timeline.
5. Update `MSC_SYLLABUS_MAP.md` only if course-facing readiness/timing materially changed.
6. Update `LEARNING_ROADMAP.md` only if strategy/dependencies materially changed.
7. Validate relevant tests/dashboard generation and propose the changes through a PR unless the user explicitly chooses another workflow.

The important boundary is:

```text
Markdown captures nuance.
YAML captures structured dashboard state.
Markdown changed ≠ YAML changes automatically.
Code exists ≠ cold-recall mastery.
Historical reconstruction ≠ invented transcript or fabricated implementation evidence.
Lesson completed ≠ dashboard status must change.
```

The maintenance step should stay lightweight. If updating context starts feeling like homework, the system is becoming too heavy.

---

# Instructions for tutor models / AI assistants

Do not treat every file as interchangeable context. They have different roles and authority. Follow `SESSION_WORKFLOW.md` for the full operational contract.

## Recommended read order when resuming a learning session

1. `SESSION_WORKFLOW.md` — workflow contract, if not already known.
2. `LEARNING_STATE.md` — operational handover.
3. Relevant part of `MSC_SYLLABUS_MAP.md` — upcoming MSc demand and urgency.
4. `LEARNING_ROADMAP.md` — strategic dependencies when making curriculum choices.
5. Relevant exercise/test — implementation evidence when the topic has a numbered repo lesson.
6. Relevant `lesson_logs/` file — retrieval blueprint or lesson continuation, including historical foundation logs when applicable.
7. `learning_progress.yaml` — structured dashboard state when relevant.

The planning question is:

> **Given what the learner knows today, what the MSc is about to demand, and the longer-term goal of strong AI/ML engineering competence, what is the highest-value thing to work on next?**

Do not let conversational recency dominate this decision.

## Source-of-truth hierarchy

| Question | Primary source |
|---|---|
| What did I actually implement? | Exercise + test code |
| What should I be able to explain/retrieve from a lesson or historical foundation? | `lesson_logs/` |
| Where am I right now? | `LEARNING_STATE.md` |
| What structured status should the dashboard show? | `learning_progress.yaml` |
| What is coming in the MSc and how ready am I? | `MSC_SYLLABUS_MAP.md` |
| Why are we learning this and what does it unlock? | `LEARNING_ROADMAP.md` |

If these appear to disagree, **do not silently reconcile them**. Inspect the evidence and update the appropriate source.

## How to run cold retrieval

When asked to cold retrieve a lesson or historical foundation:

1. Fetch that lesson/foundation log.
2. Inspect its exercise/test if useful and if one genuinely exists.
3. Do **not** dump a summary first.
4. Ask one question at a time.
5. Change numbers/examples so recall is conceptual rather than memorised.
6. Start with core concepts, then probe known fragile points.
7. If an answer is wrong, give concise feedback and re-test the concept shortly afterwards.
8. Stop once retention is clear; do not mechanically exhaust the entire question bank.
9. Timebox normal retrieval to ~10–15 minutes unless a deeper review is requested.

For a broad historical linear-algebra rebuild, follow the four logs in order; for ordinary maintenance, select only the relevant one.

## How to choose the next lesson

Before choosing, check:

1. **Upcoming demand** — what appears in the next 1–2 MSc weeks?
2. **Dependencies** — what prerequisite unlocks several later topics?
3. **Fragility** — what previously learned concept is decaying under cold recall?
4. **Application** — can theory and implementation be joined in one exercise?
5. **Long-range risk** — especially probability/statistics/linear algebra for Machine Learning Theory.
6. **Parked topics** — does anything in `PARKED / MUST RETURN` now have a timing reason to reactivate?

Do not simply continue the newest topic indefinitely.

---

# Design principles

### Durable, not exhaustive

Preserve the pieces that matter for future decisions and retrieval, not every conversational detail.

### Evidence + understanding

Code/tests show implementation; lesson logs and learning state capture understanding. Historical chat/pen-and-paper learning is represented honestly as retrieval blueprints rather than fabricated code evidence. We need those boundaries to stay explicit.

### Retrieval over rereading

Lesson logs should enable active recall rather than become another set of notes to passively reread.

### Syllabus-aware, not syllabus-limited

Preparation should help immediate MSc demands while still building toward strong practical AI/ML engineering and the mathematical foundations needed later.

### Depth before indiscriminate breadth

Being able to explain why a training loop works, trace tensor shapes, derive a gradient, reason about a projection/least-squares fit, or compare search algorithms is more valuable than briefly touching many advanced topics with no durable mental model.

### Lightweight maintenance

The workflow exists to improve learning, not to create administrative overhead.
