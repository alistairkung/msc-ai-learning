# Study Session Workflow

This file is the canonical operational protocol for a tutor/model/agent working with this learning repository.

The goal is to preserve learning continuity without turning repository maintenance into a second study task.

## Core rule

**Markdown captures nuance. YAML captures structured dashboard state.**

`learning_progress.yaml` is **not generated from the Markdown files**. A tutor/model must make an explicit judgement about whether a session materially changed the structured learning state and update the YAML when appropriate.

Do not infer mastery mechanically from the existence of code, tests, lesson logs, or wording in `LEARNING_STATE.md`.

---

## Starting a study session

Read context in this order:

1. `LEARNING_STATE.md` — current operational handover: active work, strengths, fragile points, parked topics and next step.
2. Relevant upcoming weeks in `MSC_SYLLABUS_MAP.md` — what the MSc is about to demand.
3. `LEARNING_ROADMAP.md` when choosing between competing priorities or checking longer-term dependencies.
4. Relevant exercise/test implementation as evidence of what has actually been built.
5. Relevant `lesson_logs/lessonNN_*.md` when continuing or cold-retrieving an earlier lesson.
6. `learning_progress.yaml` when dashboard state or structured topic/readiness status is relevant.

Do not let the most recent conversation or newest lesson silently override parked topics, upcoming MSc demand, or longer-term prerequisite work.

---

## During the session

Preferred tutoring behaviour:

- one small question/exercise at a time;
- cold retrieval before explanation where useful;
- hints and scaffolding before full solutions;
- immediate feedback;
- distinguish arithmetic/syntax slips from conceptual gaps;
- re-test fragile concepts with changed examples;
- use concrete shapes, computations and implementation to ground theory;
- keep ordinary retrieval reviews around 10–15 minutes unless a deeper review is requested.

Exercises and tests are learning evidence, not proof of durable cold-recall mastery.

---

# End-of-session protocol

A user instruction such as:

> **“Session’s over. Update the learning state, lesson log, and learning progress YAML if anything materially changed.”**

should trigger the following workflow.

## 1. Exercise and test

If implementation changed during the lesson, preserve the lesson's implementation and matching test.

For learning exercises, maintain the lesson identity convention:

```text
lessonNN_topic.py

test_lessonNN_topic.py
```

The exercise/test pair records what was actually implemented.

## 2. Lesson log — normally update

Create or update the relevant `lesson_logs/lessonNN_*.md` when the session creates reusable understanding.

Capture:

- what was learned;
- what was implemented;
- important conceptual distinctions;
- what the learner demonstrated confidently;
- fragile or incomplete points;
- useful future cold-retrieval prompts;
- the bridge to the next lesson/topic.

Record outcomes, not a transcript.

## 3. `LEARNING_STATE.md` — always update after a substantive study session

This is the operational handover for the next session.

Record only what matters for continuation:

- completed/current work;
- what is now comfortable;
- what remains fragile;
- anything newly parked or unparked;
- unresolved blockers;
- the next logical session;
- whether roadmap/syllabus priorities changed.

Keep it concise and current. Historical detail belongs in lesson logs.

## 4. `learning_progress.yaml` — update only when structured state materially changed

This file drives the learning dashboard.

It is maintained deliberately by the tutor/model; it is **not parsed or generated from the Markdown**.

Update it when the session materially changes one or more of:

- a topic's learning status;
- a topic's retrieval status;
- known gaps;
- current / next / then / longer-term focus;
- MSc readiness or syllabus runway;
- the learning timeline because a new lesson was added.

Examples of meaningful changes:

- A* moves from `retrieval: due` to current after successful cold retrieval.
- A known gap such as admissibility/consistency is removed after the learner demonstrates it.
- Lesson 31 moves from developing/incomplete to established after completing and explaining the full train/validation/test workflow.
- Decision trees move from planned to developing after the first substantive lesson.

Do **not** update YAML merely because a lesson occurred. Avoid cosmetic churn and fake precision.

Do not invent numeric mastery percentages. Prefer qualitative states backed by observed learning evidence.

## 5. `MSC_SYLLABUS_MAP.md` — conditional

Update only when course-facing readiness or timing materially changes, for example:

- a previously unprepared upcoming topic becomes meaningfully prepared;
- lecture/assignment reality changes urgency;
- the actual teaching sequence differs from the stored plan;
- a new prerequisite is discovered.

Do not rewrite this after every ordinary lesson.

## 6. `LEARNING_ROADMAP.md` — rare

Update only when strategy or dependency structure materially changes, for example:

- a major learning track is completed;
- a prerequisite needs to be accelerated;
- course plans change;
- a new major learning track is added;
- priorities are materially reordered.

Do not use the roadmap as a chronological diary.

## 7. Validate and propose repository changes

Before presenting session bookkeeping as complete:

- ensure lesson references and filenames are internally consistent;
- run relevant tests when code changed;
- ensure `learning_progress.yaml` remains valid for the dashboard when YAML changed;
- keep generated `dashboard/site/` output out of Git;
- use a PR for repository changes unless the user explicitly chooses another workflow.

GitHub Actions should then validate tests/dashboard generation. After merge to `main`, the dashboard deployment workflow regenerates GitHub Pages automatically.

---

# File responsibilities at a glance

| File/source | Purpose | Typical update cadence |
|---|---|---|
| Exercise + test | Evidence of implementation | When implementation changes |
| `lesson_logs/` | Durable conceptual/retrieval record | Each substantive lesson |
| `LEARNING_STATE.md` | Current operational handover | Every substantive session |
| `learning_progress.yaml` | Structured dashboard state | Only when state materially changes |
| `MSC_SYLLABUS_MAP.md` | Course-facing readiness/timing | When readiness/timing materially changes |
| `LEARNING_ROADMAP.md` | Long-term strategy/dependencies | Rarely |

---

# Source-of-truth boundaries

Use the right source for the right claim:

- **Implemented?** Inspect exercise/test code.
- **What should be retrievable from a lesson?** Inspect the lesson log.
- **Where is the learner right now?** Use `LEARNING_STATE.md`.
- **What structured status should the dashboard show?** Use `learning_progress.yaml`.
- **What does the MSc demand soon?** Use `MSC_SYLLABUS_MAP.md`.
- **Why is this in the curriculum / what does it unlock?** Use `LEARNING_ROADMAP.md`.

If these sources disagree, do not silently reconcile them. Inspect the evidence and update the appropriate source.

A particularly important distinction is:

```text
code exists ≠ cold-recall mastery
lesson completed ≠ dashboard status must change
Markdown changed ≠ YAML changes automatically
```

---

# Maintenance principle

The repository exists to make learning more durable, not more bureaucratic.

Prefer the smallest update that accurately preserves:

1. what was learned;
2. current observed readiness;
3. what must happen next;
4. any material change visible on the dashboard or MSc plan.

If bookkeeping starts competing with study time, simplify it.