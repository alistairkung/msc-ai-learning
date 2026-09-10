# Study Session Workflow

This file is the canonical operational protocol for a tutor/model/agent working with this learning repository.

The goal is to preserve learning continuity without turning repository maintenance into a second study task.

## Core rule

**Markdown captures nuance. YAML captures structured dashboard state.**

`learning_progress.yaml` is **not generated from the Markdown files**. A tutor/model must make an explicit judgement about whether a session materially changed the structured learning state and update the YAML when appropriate.

Do not infer mastery mechanically from the existence of code, tests, lesson logs, or wording in `LEARNING_STATE.md`.

---

## Repository structure / where logs belong

`lesson_logs/` contains two deliberately different kinds of learning record.

### Cross-course preparation sequence

Numbered lessons and reconstructed historical foundations stay directly under `lesson_logs/`:

```text
lesson_logs/
  lessonNN_*.md
  historical_*.md
```

These records belong to the learner's cross-course preparation sequence rather than to one MSc module. Their implementation/test evidence normally lives in the relevant topic directory such as `foundations/`, `machine_learning/`, `classical_ai/` or `deep_learning/`.

### Live MSc course records

Course-specific lecture/tutorial/assignment/project/reflection material belongs under a folder named with the course code:

```text
lesson_logs/
  aims5701/
  aims5702/
  aims5704/
  ftec5660/
```

A course folder may contain a `README.md` or `course_context.md` plus focused lecture, tutorial, assignment, project and reflection logs.

**Do not create a separate top-level `notes/` hierarchy for live-course material.** If a new course-specific note is needed, put it in the matching `lesson_logs/<course_code>/` folder.

When locating context for a live course, start in that course folder and read the smallest relevant file. Use `lesson_logs/INDEX.md` for coverage/discovery. Course folders are organisational boundaries, not evidence boundaries: still distinguish lecturer-supported material, learner synthesis, pre-reading and independently demonstrated learning.

---

## Starting a study session

Read context in this order:

1. `LEARNING_STATE.md` — current operational handover: active work, strengths, fragile points, parked topics and next step.
2. Relevant upcoming weeks in `MSC_SYLLABUS_MAP.md` — what the MSc is about to demand.
3. `LEARNING_ROADMAP.md` when choosing between competing priorities or checking longer-term dependencies.
4. Relevant exercise/test implementation as evidence of what has actually been built.
5. Relevant lesson log:
   - numbered/historical prep: `lesson_logs/lessonNN_*.md` or `lesson_logs/historical_*.md`;
   - live-course work: `lesson_logs/<course_code>/...`.
6. `learning_progress.yaml` when dashboard state or structured topic/readiness status is relevant.

Do not let the most recent conversation or newest lesson silently override parked topics, upcoming MSc demand, or longer-term prerequisite work.

---

## During the session

Preferred tutoring behaviour:

- one small question/exercise at a time;
- cold retrieval before explanation where useful;
- make the learner construct important implementations rather than copy them;
- hints and scaffolding before full solutions;
- immediate feedback;
- distinguish arithmetic/syntax slips from conceptual gaps;
- re-test fragile concepts with changed examples;
- use concrete shapes, computations and implementation to ground theory;
- keep ordinary retrieval reviews around 10–15 minutes unless a deeper review is requested.

### Retrieval stays within the taught boundary

When reviewing or cold-retrieving a lesson, test what the learner was actually taught and what the lesson log records as learned, demonstrated or fragile. **Do not treat every concept that appears in code, an API, or an adjacent topic as something the learner is expected to know.**

In particular:

```text
concept appears in code ≠ concept was taught
adjacent concept / natural extension ≠ fair retrieval expectation
```

Novel questions are encouraged when they can be reasoned through entirely from concepts the learner has already learned. For example, changing the numbers, shapes or scenario is useful retrieval. But if answering a question requires a new concept that has not yet been taught, treat that as **new teaching**, not as a failed retrieval attempt.

If an interesting untaught extension arises during review, either leave it for the planned curriculum or explicitly introduce it as new material. Do not silently use it to judge mastery of the reviewed lesson.

For live-course notes, preserve source boundaries explicitly:

```text
what lecturer/material actually covered
    ≠ pre-reading of later supplied material
    ≠ learner's post-lecture synthesis
    ≠ independently demonstrated mastery
```

### Rich tutor context, sparse learner interface

The tutor/model may read substantial repository context privately in order to choose the right next question. Do **not** dump that context back to the learner as a large explanation unless it is genuinely needed.

The normal learner-facing loop should stay narrow:

```text
question / small task
    → learner attempt
    → concise feedback
    → next question / task
```

A rich lesson log or detailed implementation record is there to help the tutor choose the next intervention. It is **not** a script to read back to the learner.

### Learner owns the implementation

When writing the implementation is itself the learning exercise, **do not provide completed implementation code for the learner to copy or ask the learner to reproduce a tutor-written method**.

Instead, preserve the reasoning work for the learner. For example, when several already-built helpers need to be composed into `run_experiment()`, ask the learner to decide and write the orchestration incrementally rather than presenting the finished function.

Use this escalation ladder:

```text
1. Ask the question / set the implementation task
2. Give a conceptual hint
3. Give a stronger or more specific hint
4. Provide a partial scaffold / signature / pseudocode
5. Provide the minimum missing syntax or API detail
6. Give a full solution only when genuinely necessary or explicitly requested
```

Do not skip directly to step 6 merely because the remaining code appears to be “glue code”. Composing previously learned pieces is often the conceptual exercise.

Small syntax/API snippets are appropriate when the syntax is incidental to the concept being tested. Examples include reminding the learner of an unfamiliar library method name, function signature, or boilerplate that is not the learning objective. Even then, provide the smallest useful snippet rather than solving the surrounding task.

If the learner explicitly asks for the full solution, provide it, but distinguish that from successful independent retrieval/implementation when updating learning state.

Exercises and tests are learning evidence, not proof of durable cold-recall mastery.

---

# End-of-session protocol

A user instruction such as:

> **“Session’s over. Update the learning state, lesson log, and learning progress YAML if anything materially changed.”**

should trigger the following workflow.

## 1. Exercise and test

If implementation changed during the lesson, preserve the lesson's implementation and matching test.

For numbered learning exercises, maintain the lesson identity convention:

```text
lessonNN_topic.py

test_lessonNN_topic.py
```

The exercise/test pair records what was actually implemented.

Live-course scratch work does not automatically need a numbered lesson identity. If it becomes durable implementation evidence, store it in the most sensible topic/code directory and link it from the course log.

## 2. Lesson/course log — normally update

For a numbered/preparatory session, create or update the relevant root `lesson_logs/lessonNN_*.md`.

For a live MSc course session, create or update the relevant file under:

```text
lesson_logs/<course_code>/
```

Capture:

- what was learned;
- what was implemented;
- important conceptual distinctions;
- what the learner demonstrated confidently;
- fragile or incomplete points;
- useful future cold-retrieval prompts;
- the bridge to the next lesson/topic;
- for live courses, what came from the lecturer/material versus pre-reading or learner synthesis.

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

Keep it concise and current. Historical detail belongs in lesson/course logs.

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

When YAML stores source file paths, keep them synchronized with repository moves such as course-folder reorganisations.

## 5. `MSC_SYLLABUS_MAP.md` — conditional

Update only when course-facing readiness or timing materially changes, for example:

- a previously unprepared upcoming topic becomes meaningfully prepared;
- lecture/assignment reality changes urgency;
- the actual teaching sequence differs from the stored plan;
- a new prerequisite is discovered.

Do not rewrite this after every ordinary lesson. File-path references to course logs should still be updated when the repository structure changes.

## 6. `LEARNING_ROADMAP.md` — rare

Update only when strategy or dependency structure materially changes, for example:

- a major learning track is completed;
- a prerequisite needs to be accelerated;
- course plans change;
- a new major learning track is added;
- priorities are materially reordered.

Do not use the roadmap as a chronological diary. Structural path references should still remain valid after file moves.

## 7. Validate and propose repository changes

Before presenting session bookkeeping as complete:

- ensure lesson references and filenames are internally consistent;
- ensure live-course notes are under the correct `lesson_logs/<course_code>/` folder;
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
| Root `lesson_logs/lessonNN_*.md` + `historical_*.md` | Cross-course prep/retrieval record | Each substantive preparatory lesson |
| `lesson_logs/<course_code>/` | Live-course lecture/tutorial/project/reflection context | Each substantive course session |
| `LEARNING_STATE.md` | Current operational handover | Every substantive session |
| `learning_progress.yaml` | Structured dashboard state | Only when state materially changes |
| `MSC_SYLLABUS_MAP.md` | Course-facing readiness/timing | When readiness/timing materially changes |
| `LEARNING_ROADMAP.md` | Long-term strategy/dependencies | Rarely |

---

# Source-of-truth boundaries

Use the right source for the right claim:

- **Implemented?** Inspect exercise/test code.
- **What should be retrievable from a numbered lesson?** Inspect the root numbered lesson log.
- **What happened in a particular live course?** Inspect `lesson_logs/<course_code>/` and preserve lecturer/pre-read/synthesis boundaries.
- **Where is the learner right now?** Use `LEARNING_STATE.md`.
- **What structured status should the dashboard show?** Use `learning_progress.yaml`.
- **What does the MSc demand soon?** Use `MSC_SYLLABUS_MAP.md`.
- **Why is this in the curriculum / what does it unlock?** Use `LEARNING_ROADMAP.md`.

If these sources disagree, do not silently reconcile them. Inspect the evidence and update the appropriate source.

A particularly important distinction is:

```text
code exists ≠ cold-recall mastery
concept appears in code ≠ concept was taught
pre-read material ≠ lecture-covered material
lesson completed ≠ dashboard status must change
Markdown changed ≠ YAML changes automatically
full solution received ≠ independently demonstrated mastery
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
