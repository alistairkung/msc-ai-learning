# Learning State — Current Handover

_Last maintained: 2026-09-11. Learning evidence through 2026-09-11._

Read `SESSION_WORKFLOW.md` for tutoring rules. `learning_progress.yaml` is the structured dashboard projection; focused lesson/course notes remain the detailed evidence source. Do not infer mastery from code presence alone.

## Three parallel commitments

| Lane | Next useful work | Why / boundary |
|---|---|---|
| Continue | **Search guarantees / complexity consolidation** | Lesson 33 completed the BFS/DFS/UCS/A* implementation block. Do not immediately rewrite all four algorithms again. |
| Parallel | **AIMS5702 representation translation + light tensor maintenance** | Lecture 1 exposed a diagram/index-notation translation cost. Shape reasoning remains the anchor. A 45-minute tensor cold review on 11 Sep found slicing/API rust but strong broadcasting/reduction reasoning. |
| Protect | **A small relevant maths retrieval block** | Keep January AIMS5704 prerequisites alive without turning them into a broad restart. |

These lanes coexist; they are not one sequential queue. FTEC5660 remains deliberately parked until one day before its next lecture.

## Course timing / planning uncertainty

- MSc Term 1 is recorded as **7 Sep–4 Dec 2026**.
- **AIMS5701 Fundamentals** is reported to start one week later than originally planned; exact revised dates are not independently confirmed.
- **AIMS5702 Artificial Intelligence in Practice:** first live lecture was 10 Sep 2026. Only the introductory/Lecture 1 material was covered in class; the dtype/memory/stride/einsum material studied beforehand remains a pre-read preview of later supplied slides.
- AIMS5702 course-specific logs live under `lesson_logs/aims5702/`. Live-course material for other modules follows the same `lesson_logs/<course_code>/` convention.
- **AIMS5704 Machine Learning Theory** starts **11 Jan 2027** in the stored syllabus.
- FTEC5660 remains a useful learning source, but continued enrolment is uncertain because the learner may be unable to commit to the hackathon final/pitch day. Course-specific FTEC work is deliberately parked for now.
- **Return trigger for Agentic AI:** one day before the next FTEC5660 lecture. The exact calendar date is intentionally not invented here.

## AIMS5702 — Lecture 1 + tensor maintenance state

Sources: `lesson_logs/aims5702/lecture01_02_prelecture_bridge.md`, `lesson_logs/aims5702/tensor_cold_review_2026_09_11.md`, plus prior Lessons 10, 11, 27–31.

### Representation translation remains an explicit objective

Lecture 1 used mathematical `i/j/...` index notation heavily and presented MLP/parameter-count reasoning through network/flowchart diagrams. The learner reasons more naturally through tensor shapes and does **not** want to replace that representation.

Preferred bridge remains:

```text
network diagram
    ↕
tensor shapes          <- primary reasoning anchor
    ↕
index notation
    ↕
PyTorch operations / modules
    ↕
parameter count
```

For simple implementation, keep ordinary shape reasoning and `@`/`matmul` as the natural code representation. `einsum` is a bridge to index/contraction notation and more general tensor contractions, not a replacement for successful shape-first reasoning.

### 11 Sep tensor cold review

A 45-minute no-lecture maintenance session cold-refreshed slicing, broadcasting, transpose/permute, reshape and reductions.

**Retrieved well:**

- semantic shape reasoning;
- right-aligned broadcasting (`equal` or one dimension is `1`);
- reduction semantics and identifying which dimensions disappear;
- feature-wise centring logic;
- transpose producing a non-contiguous tensor/view;
- full-axis `permute` ordering after the distinction was surfaced.

**Rusty but recovered quickly:**

- Python `start:stop:step` syntax, especially `::2`, negative slicing and stop exclusivity;
- placing a slice on the intended semantic axis (`batch,tokens,features`);
- operation-name distinction among `transpose`, `permute` and `reshape`;
- minor PyTorch API spelling/convention (`mean`/`dim`).

Do not turn these slips into a broad tensor-foundation downgrade. The conceptual broadcasting/reduction model remained substantially stronger than the surface syntax.

**Newly introduced today:**

- `keepdim=True`: retain the reduced axis as size `1` to preserve a useful broadcasting shape;
- multi-axis reduction with tuple dimensions, e.g. `x.mean(dim=(0,1))`.

`keepdim` was explicitly reported as unseen before, so it is **new teaching, not failed recall**. Immediately after introduction, the learner independently recognised that `(64,16)` would not broadcast back over `(64,5,16)` and selected the need to keep the token dimension, giving `(64,1,16)`.

A later tensor maintenance check should be only 5–10 minutes using changed examples; do not replay today's whole block.

### Pre-read systems foundation — still not lecture-covered

Before the 10 Sep class, later supplied slides were previewed. These concepts remain **guided pre-read evidence**, not material actually taught in Lecture 1:

- dtype/model-memory arithmetic;
- exponent range vs mantissa/significand precision intuition;
- flat storage, stride and offset;
- views/copies/contiguity;
- basic `einsum` reading.

Fresh prior fragile point remains: a sliced view's stride was initially recomputed from its new shape as though storage had been repacked. Durable correction:

> Shape alone does not determine a view's stride. For views, reason from the underlying storage and transformation history.

### AIMS5702 next step

Do not restart NumPy/PyTorch wholesale. Next substantive course-facing work should still prioritise actual Lecture 1 representation translation:

1. diagram -> layer widths -> tensor shapes;
2. shapes -> parameter counts;
3. shapes -> index notation and index notation -> shapes;
4. shapes/index notation -> ordinary PyTorch and, where useful, equivalent `einsum`.

When Lecture 2 systems material is actually taught, cold-check the pre-read rather than replaying it from scratch. Tensor syntax maintenance can be sampled briefly alongside course work.

## Search — implementation block completed through Lesson 33

Sources: `lesson_logs/search_reactivation_2026_09_06.md`, Lessons 24–26, and `lesson_logs/lesson33_search_reconstruction.md`.

### BFS / DFS / UCS / A*

- BFS FIFO/level-order and fewest-edge reasoning have the strongest current independent evidence.
- DFS was successfully reconstructed from the BFS skeleton with guided/refreshed evidence.
- UCS was implemented with a priority queue and cheaper-path replacement; support was needed for `heapq` mechanics, tuple unpacking and some syntax/API details.
- A* was derived from UCS with `f=g+h`; support was needed for heap shape, neighbour heuristic choice and keeping `g` separate from `h`.

Treat UCS/A* as implemented/guided rather than cold-independent.

### Search theory still due

Next search block should cover completeness/optimality, UCS non-negative-cost assumptions, A* admissibility vs consistency, goal popped vs discovered, and qualitative/formal time-memory complexity as required by AIMS5701. Only later use one short changed-graph reconstruction to test whether UCS/A* have moved from guided to independent retrieval.

## FTEC5660 / LangChain — parked after Lesson 32

Sources: `lesson_logs/ftec5660/pattern01_prompt_chaining.md`, `lesson_logs/ftec5660/lcel_guided_practice_2026_09_09.md`, `lesson_logs/lesson32_lcel_basics.md`, and `lesson_logs/ftec5660/tutorial01_study_plan.md`.

- Prompt chaining concept is taught: stable sequential stages, checkable handoffs, deterministic processing between LLM stages, and cost/latency/failure trade-offs.
- Lesson 32 implemented prompt templates, string/JSON parsers, invocation dictionaries and simple two-stage LCEL mapping with changed-example tests.
- LCEL remains guided because two-stage composition required support and Python/API role slips (`fn` vs `fn()`, parser class vs instance) recurred.
- Prompt-design cold-recall target remains `Task / Input / Constraints / Output structure`.
- Resume one day before the next FTEC5660 lecture with only a 5–10 minute Lesson 32 cold check, then continue the stored Tutorial 1 plan.

## Established foundations / remaining uncertainty

- **Python / NumPy / pandas:** substantial practice in Lessons 01–20 and 27. Python syntax/API fluency can still be less automatic than the learner's long-used backend languages; today's slicing/API rust is consistent with this boundary.
- **Linear algebra:** historical JHU foundation established; retrieve small relevant blocks rather than restart.
- **Probability/statistics:** Bayes, distributions, joint moments, inequalities and CLT/inference have strong historical evidence. Markov chains and Poisson remain diagnostic-needed rather than proven current mastery.
- **Calculus:** slope → derivatives → partials → gradients → chain rule/backprop is historically established.
- **Practical ML:** linear/logistic regression and the Lesson 31 train/validation/test workflow are implemented; transfer should be tested on changed tasks.
- **AIMS5702 tensor operations:** broadcasting/reductions/semantic shapes are currently stronger than slicing/API fluency. `keepdim` and tuple-dimension reductions are newly introduced 11 Sep.
- **AIMS5702 representation translation:** shape reasoning is the anchor; index/diagram fluency should be trained as translation, not replacement.
- **AIMS5702 systems/tensor representation:** dtype memory, flat storage, stride/view/contiguity and basic einsum remain guided pre-read material from 10 Sep.
- **January extensions:** likelihood/MLE, exponential families, formal generalisation/concentration, convergence assumptions and proof-style derivations remain genuinely new work.

## Parked / must return

- **AIMS5701:** next consolidate search guarantees/complexity; light logic preview before W1; trees/random forests before W3; Bayes retrieval before W4; Markov diagnostic before W5.
- **AIMS5702:** next substantive review should train diagram/index/shape translation from Lecture 1 examples. Later tensor maintenance should be short changed-example checks, not full re-teaching.
- **FTEC5660:** deliberately parked. Resume one day before the next lecture from `lesson_logs/ftec5660/tutorial01_study_plan.md`.
- **Maths:** selective LA/calculus/probability maintenance; later MLE and formal-theory extensions.

## Handover discipline

After the next substantive session, update its focused log/course note and this handover. Update `learning_progress.yaml` only when the structured dashboard state materially changes; today's maintenance review sharpens evidence boundaries but does not require a broad mastery/status upgrade.
