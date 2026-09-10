# Learning System Architecture

This repository is not only a collection of exercises and notes. It is a **durable learning system** designed to preserve tutoring continuity across long-running study, changing course demands, and new model/chat contexts.

The architecture has one central goal:

> A future tutor/model should be able to reconstruct the useful learning state from the repository without depending on the original conversation context.

The system therefore separates **evidence**, **current state**, **course demand**, **long-term strategy**, and **dashboard projection** instead of collapsing them into one giant context file.

---

# 1. High-level architecture

```text
                   LIVE COURSE REALITY
            lectures / tutorials / projects
             assignments / timing changes
                         |
                         v
                MSC_SYLLABUS_MAP.md
             near-term course demand
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
      CONTINUE        PARALLEL       PROTECT
   main next work    live-course     long-term
                     follow-up       prerequisites
          |              |              |
          +--------------+--------------+
                         |
                         v
                    STUDY SESSION
            retrieve -> teach -> build
                  -> test -> reflect
                         |
                         v
                 LEARNING EVIDENCE
          +--------------+--------------+
          |              |              |
          v              v              v
   exercises/tests    lesson_logs/   observed support,
 implementation       durable record  fragility, transfer
          |              |              |
          +--------------+--------------+
                         |
                         v
                 LEARNING_STATE.md
              current operational handover
                         |
            material state change only
                         v
              learning_progress.yaml
               reviewed structured state
                         |
                         v
                   Learning Atlas
```

The arrows are **information flow**, not automatic generation. In particular, Markdown does not automatically become YAML and passing tests do not automatically become mastery.

---

# 2. The major layers

## A. Evidence layer — what actually happened

This is the most concrete layer.

### Exercise and test code

Implementation lives in topic directories such as:

```text
foundations/
machine_learning/
classical_ai/
deep_learning/
agentic_ai/
```

Exercise/test pairs answer questions such as:

- What code exists?
- What behaviour is tested?
- What implementation was successfully produced?

They **do not** by themselves answer:

- Was it written independently?
- Was substantial guidance required?
- Is it still retrievable after a delay?
- Was every concept appearing in the code actually taught?

### Lesson/course logs

`lesson_logs/` is the durable conceptual and pedagogical evidence layer.

It records:

- what was taught;
- what the learner demonstrated;
- support required;
- fragile points;
- useful cold-retrieval prompts;
- source boundaries;
- personal synthesis worth preserving;
- the intended bridge to later work.

This is the main source for deciding what is a **fair future retrieval target**.

---

## B. Operational-state layer — where learning is now

### `LEARNING_STATE.md`

This is the short-lived operational handover.

It answers:

- What is active now?
- What was just completed?
- What is fragile?
- What is parked?
- What should the next session do?

It should remain much smaller than the complete learning history. Historical detail belongs in focused logs.

The state uses three concurrent planning lanes:

```text
CONTINUE
    main next learning task

PARALLEL
    live-course or other useful concurrent work

PROTECT
    prerequisite work that must not silently disappear
```

These are deliberately **not one FIFO backlog**. An urgent live-course task may temporarily dominate without deleting a protected longer-term objective.

---

## C. Course-demand layer — what the MSc is about to require

### `MSC_SYLLABUS_MAP.md`

This is the tactical bridge between the learning record and the actual MSc sequence.

It answers:

- What will each course require soon?
- Which foundations already exist?
- Which requirements remain genuinely new?
- Where is timing uncertain?

Its normal planning horizon is roughly the **next 1–2 course weeks**.

A course topic being listed here does not mean it has been taught or mastered. The map may contain future requirements and intentionally unknown scope.

---

## D. Strategy layer — why the system is heading somewhere

### `LEARNING_ROADMAP.md`

This is the slow-changing dependency and priority model.

It answers:

- What long-term capabilities matter?
- Which prerequisites unlock several later topics?
- Why should one learning lane be protected despite short-term pressure?
- What should not be pre-studied yet?

It changes much less often than `LEARNING_STATE.md`.

Useful timescale distinction:

```text
LEARNING_STATE.md       -> now / next session
MSC_SYLLABUS_MAP.md     -> coming weeks
LEARNING_ROADMAP.md     -> months / dependency strategy
```

---

## E. Structured-projection layer — reviewed machine-readable state

### `learning_progress.yaml`

This is a **reviewed projection** of selected learning evidence used by the dashboard.

It is intentionally not generated automatically from Markdown or tests.

Why?

Because these transformations require judgement:

```text
passing test
    != independent implementation

lecture mentioned topic
    != topic taught

historically studied
    != currently retrievable

received solution
    != demonstrated mastery
```

The YAML exists so the dashboard can be structured without pretending that learning state can be inferred mechanically.

### `dashboard/`

The Learning Atlas is a **read-only presentation layer** over the structured state.

The dashboard should make evidence and uncertainty legible. It must not silently invent confidence, mastery percentages, readiness or automatic priority changes.

---

# 3. Repository memory architecture

The repository acts as **external long-term memory for the tutoring process**.

The system does not try to load everything into every conversation. Instead, a tutor/model reconstructs context by selective retrieval.

```text
new model / new chat
      |
      v
SESSION_WORKFLOW.md
      |
      v
LEARNING_STATE.md
      |
      +--> relevant syllabus slice
      |
      +--> smallest relevant lesson/course log
      |
      +--> code/test evidence if needed
      |
      +--> roadmap/YAML only when relevant
```

This is deliberate context compression.

The repository should preserve enough information that loss of a long-running chat is inconvenient rather than catastrophic.

## Context should be loaded lazily

Do not load every course, lesson and historical record simply because it exists.

Prefer:

> **smallest useful context first; expand only when needed.**

Examples:

- cold-retrieving Lesson 30 -> read Lesson 30 log, then implementation/test only if useful;
- discussing AIMS5702 Lecture 1 -> start in `lesson_logs/aims5702/`;
- deciding what to study next across courses -> read state + syllabus + roadmap;
- updating dashboard state -> inspect the relevant evidence plus YAML/dashboard guidance.

---

# 4. Learning-record namespaces

`lesson_logs/` contains two different kinds of history.

## Cross-course learning sequence

```text
lesson_logs/
  lessonNN_*.md
  historical_*.md
```

These belong to the learner's broader preparation sequence rather than one MSc module.

Examples include Python, NumPy, ML, search, PyTorch and reconstructed pre-repository maths foundations.

## Live-course namespaces

```text
lesson_logs/
  aims5701/
  aims5702/
  aims5704/
  ftec5660/
```

These hold course-specific material such as:

- course context;
- lecture logs;
- tutorial logs;
- assignment/project notes;
- pre/post-lecture synthesis;
- course-specific study plans.

Do not recreate a parallel top-level `notes/` hierarchy for course material.

Course folders are an **organisational namespace**, not evidence of mastery.

---

# 5. Evidence provenance model

A core architectural feature is preserving **where a claim came from**.

The system routinely distinguishes:

```text
LECTURER / COURSE MATERIAL
    actually taught or directly supported by supplied material

PRE-READ / PREVIEW
    studied ahead of the live course

GUIDED LEARNING
    learner understood/implemented with support

INDEPENDENT DEMONSTRATION
    learner produced/explained the result with little/no conceptual support

HISTORICAL EVIDENCE
    previously studied with evidence, but current retention may be unknown

PERSONAL SYNTHESIS
    learner's own interpretation, analogy or working hypothesis

PLANNED / NEW
    future requirement; not yet learned
```

These categories matter because otherwise a future model can accidentally turn exposure into mastery.

Important invariants:

```text
code exists ≠ independent mastery
lecture slide exists ≠ lecture covered it
pre-read ≠ live-course teaching
historically studied ≠ currently fluent
personal synthesis ≠ lecturer claim
new syllabus requirement ≠ failed recall
```

---

# 6. Study-session lifecycle

The normal learning loop is interactive:

```text
retrieve
   -> learner attempt
   -> diagnose gap
   -> hint / teach smallest missing idea
   -> changed example
   -> implement / calculate / explain
   -> test or inspect
   -> reflect
```

The tutor should distinguish:

```text
conceptual misunderstanding
vs
notation slip
vs
arithmetic mistake
vs
API/syntax rust
vs
representation-translation cost
```

Those imply different interventions.

For example, difficulty translating an MLP diagram into tensor shapes should not automatically be recorded as failure to understand parameter counting if the same learner can reason correctly once the diagram is translated.

## End-of-session write path

After substantive learning:

```text
implementation changed?
    -> update exercise/test

reusable understanding created?
    -> update focused lesson/course log

current continuation changed?
    -> update LEARNING_STATE.md

structured learning state materially changed?
    -> update learning_progress.yaml

course timing/readiness changed?
    -> update MSC_SYLLABUS_MAP.md

long-term strategy changed?
    -> update LEARNING_ROADMAP.md
```

Not every session should churn every file.

---

# 7. Retrieval is an architectural feature, not just a study technique

The system assumes that durable learning requires **reconstruction after forgetting**, not permanent conversational context.

Focused logs therefore contain retrieval blueprints and fragile points so a later model can generate changed questions rather than merely rereading answers.

A useful distinction is:

```text
recognition
    "I remember seeing this"

retrieval
    "I can reconstruct/explain it without looking"

transfer
    "I can use it in a changed problem"
```

Implementation/tests can support this process, but tests should not be mistaken for retrieval evidence unless the learning record says how the implementation was produced.

---

# 8. Representation translation

The learning system should preserve successful internal representations rather than forcing one canonical style of reasoning.

When a course uses a different representation, train **translation**.

For example, AIMS5702 exposed a useful recurring bridge:

```text
network diagram
    ↕
tensor shapes
    ↕
index notation
    ↕
PyTorch code
    ↕
parameter count
```

If tensor shapes are the strongest reasoning anchor, keep them as the anchor and build fluency translating into and out of lecturer notation.

This is a general principle:

> When performance drops under a new representation, first determine whether the concept is weak or whether the learner is paying a translation cost.

---

# 9. Failure modes the architecture is designed to prevent

## Context-window dependence

**Failure:** the learning plan only exists in one long-running chat.

**Countermeasure:** durable state, focused logs, roadmap and syllabus map.

## Latest-topic capture

**Failure:** the newest interesting topic silently replaces previously planned priorities.

**Countermeasure:** Continue / Parallel / Protect lanes plus syllabus/roadmap checks.

## Exposure inflation

**Failure:** supplied slides, copied code or guided exercises become recorded as mastery.

**Countermeasure:** provenance/evidence boundaries and explicit support records.

## Repository archaeology

**Failure:** future tutors must read hundreds of files before doing anything useful.

**Countermeasure:** state-first loading, course namespaces, focused logs and lazy retrieval.

## Dashboard authority inversion

**Failure:** a UI/status field is treated as more authoritative than the underlying evidence.

**Countermeasure:** YAML is explicitly a reviewed projection; lesson logs/code remain evidence sources.

## Documentation sprawl

**Failure:** every reflection creates a new top-level context system.

**Countermeasure:** defined responsibilities for architecture, workflow, state, syllabus, roadmap, logs and YAML.

---

# 10. Document responsibilities

| Source | Architectural role | Main question answered |
|---|---|---|
| `ARCHITECTURE.md` | System design | How do all the learning-system pieces fit together? |
| `SESSION_WORKFLOW.md` | Operating protocol | How should a tutor/model run and maintain a session? |
| Exercise + tests | Implementation evidence | What has actually been built/tested? |
| `lesson_logs/` | Durable learning evidence | What was taught/demonstrated, with what support and fragility? |
| `LEARNING_STATE.md` | Current handover | Where are we now and what happens next? |
| `MSC_SYLLABUS_MAP.md` | Tactical course demand | What will the MSc require soon? |
| `LEARNING_ROADMAP.md` | Long-term strategy | What dependencies/priorities matter over months? |
| `learning_progress.yaml` | Reviewed structured projection | What selected state should the dashboard display? |
| `dashboard/` | Presentation | How is structured state visualised? |

If two sources conflict, do not silently choose one. Resolve the conflict using the evidence hierarchy and update the appropriate document.

---

# 11. Model/tutor onboarding

For a model that is **new to the repository**, read:

```text
1. ARCHITECTURE.md       understand the system
2. SESSION_WORKFLOW.md   understand operating rules
3. LEARNING_STATE.md     understand current position
```

Then load only the context needed for the task:

```text
course task        -> relevant lesson_logs/<course_code>/ file
numbered lesson    -> relevant lessonNN log
historical maths   -> smallest relevant historical log
planning decision  -> syllabus + roadmap
implementation     -> exercise/test
structured/UI work -> YAML + dashboard guidance
```

For a model already familiar with the architecture, routine study sessions normally begin with `SESSION_WORKFLOW.md` and `LEARNING_STATE.md`; there is no need to reread this entire file every turn.

---

# 12. Evolution principle

The architecture should evolve only when a recurring problem appears.

Good reasons to change it:

- a new class of source cannot be represented cleanly;
- models repeatedly put information in the wrong place;
- context recovery is too expensive or unreliable;
- evidence provenance is being lost;
- state and strategy are becoming conflated.

Bad reason:

- one conversation produced an interesting detail.

The repository should remain a **learning aid, not a bureaucracy**.

The system is successful when a future tutor can quickly answer:

```text
What has been learned?
How strong is the evidence?
What remains fragile or unknown?
What does the MSc need next?
What should we do in this session?
```

without needing the original conversation that created the record.
