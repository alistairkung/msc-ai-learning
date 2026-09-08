# MSc AI Learning Repository

This repository is the durable learning record and planning system for my MSc AI preparation and study.

## [Open the Learning Atlas](https://alistairkung.github.io/msc-ai-learning/)

**What I can explain, what I have demonstrated, what remains uncertain, and the next useful action.** The dashboard separates concept evidence from performance, maps course requirements without invented mastery percentages, and shows three parallel study lanes.

> **Tutor/model/agent:** read `SESSION_WORKFLOW.md`, then `LEARNING_STATE.md` and the relevant syllabus/log. For dashboard changes, read `dashboard/README.md`. The YAML is deliberately maintained from evidence; it is not inferred automatically from Markdown or passing tests. A private local `LEARNER_PROFILE.md` may be available in the learner's own workspace; never copy private profile content into this public repository or dashboard.

## What the repository preserves

**Implementation evidence:** exercises and tests record what was built. **Learning continuity:** lesson logs preserve demonstrations, support needed, fragile points and taught boundaries. **Direction:** the syllabus and roadmap connect current work with future demands, especially January Machine Learning Theory.

Code existing does not prove cold-recall mastery. Receiving a solution does not prove independent performance. A topic appearing in code or on an overview slide does not mean it was taught. Historical learning is not automatically current fluency, and unknown retention is not failure.

## Structure

```text
SESSION_WORKFLOW.md       tutoring and maintenance contract
LEARNING_STATE.md         concise operational handover
MSC_SYLLABUS_MAP.md       course weeks, requirements and uncertainty
LEARNING_ROADMAP.md       long-term goals and dependencies
learning_progress.yaml   structured, reviewed evidence projection

dashboard/               static builder, interface and validation tests
foundations/
  calculus/              historical chat-based preparation
  linear_algebra/        historical JHU retrieval blocks
  probability_statistics/ historical JHU retrieval blocks
  python/                lessons 01–07
  dsa/                   lessons 08–09
  numpy/                 numerical foundations
  pandas/                data preparation
  retrieval/             mixed retrieval checkpoints
machine_learning/        manual ML, classification and regression
classical_ai/search/     BFS, DFS, A* and solution-free practice
deep_learning/          tensors, autograd, training loops and MLPs
lesson_logs/             numbered, historical and live-course records
```

Each numbered exercise and its matching test normally live together in their topic directory. Historical chat/pen-and-paper learning is preserved as retrieval blueprints, not fabricated exercise/test pairs or invented lesson numbers. The coverage index is [`lesson_logs/INDEX.md`](lesson_logs/INDEX.md).

## How to resume study

Read the workflow and current handover. Consult the upcoming **course-specific** syllabus weeks, then the smallest relevant lesson log. Use the roadmap when choosing among longer-term priorities. Inspect code privately when useful, but do not reveal an old solution before independent reconstruction.

Choose work from the intersection of upcoming course demand, prerequisite gaps, observed fragility and long-term AI/ML engineering value. Do not let the newest topic displace deliberately parked work. Keep live-course follow-up and protected maths continuity alongside the main implementation task rather than behind one endless queue.

## How tutoring works

Use one small question or task at a time: **task → learner attempt → concise feedback → next task**. Retrieve before explaining where appropriate. Distinguish conceptual gaps from algebra, notation and incidental API slips. Escalate from a question through hints and a partial scaffold before a full solution. The learner writes the important implementation, including composition or orchestration when that is the exercise.

Novel questions using learned concepts are useful. Questions requiring an untaught concept are new teaching, not failed retrieval. Keep normal maintenance retrieval around 10–15 minutes unless a deeper review is requested; stop when enough evidence is available.

The logs support commands such as “cold retrieve Lesson 30”, “retrieve calculus foundations”, or “retrieve Bayes”. For historical maths choose a focused block; diagnose weakly recovered topics such as Markov chains/Poisson instead of assuming mastery or restarting whole courses.

## End-of-session workflow

> Session's over. Update the learning state, lesson log, and learning progress YAML if anything materially changed.

Preserve code/tests if implementation changed, update the focused log, and update the operational handover after every substantive session. Update the YAML only for materially changed evidence, next actions, course requirements or study lanes. Update the syllabus when course reality changes and the roadmap only when strategy changes. Validate the relevant code/dashboard and normally propose a PR unless a different workflow is explicitly requested.

| Source | Authority | Cadence |
|---|---|---|
| Exercise + test | What implementation exists | When code changes |
| Lesson logs | What was taught/demonstrated, support and fragile points | Substantive sessions |
| Learning state | Immediate continuation and active/parked work | Substantive sessions |
| Progress YAML | Reviewed structured evidence used by the UI | Material evidence/planning changes |
| Syllabus map | Course-facing sequence, requirements and uncertainty | Course/timing/readiness changes |
| Roadmap | Long-term goals and dependency strategy | Infrequently |

Conflicts require an explicit evidence check, not silent reconciliation. `learning_progress.yaml` schema v2 replaces the old single `status` / `retrieval` model; the workflow's qualitative examples are not literal v2 field names. See the dashboard guide before editing it.

## Dashboard views

**Knowledge:** filterable evidence matrix with source-backed topic details, learning paths and history. **Course runway:** available anchors, actual remaining requirements and unmapped scope, not a weakest-topic “ready” score. **Study queue:** Continue, Parallel and Protect lanes.

The page is static and read-only. It makes no model calls, loads no external assets and does not book calendar events. Generated `dashboard/site/` output stays out of Git. GitHub Actions builds a PR preview artifact and deploys Pages only after changes reach `main`.

```bash
python -m pytest dashboard/test_build.py
python dashboard/build.py
python -m http.server 8000 --directory dashboard/site
```

Open the local server in a browser. Run the repository's complete suite with `python -m pytest`. Browser checks and schema-maintenance instructions are in [`dashboard/README.md`](dashboard/README.md).

## Maintenance principle

Preserve useful evidence, not every conversational detail. The system should make learning durable and easier to resume—not turn infrastructure maintenance into a second course.
