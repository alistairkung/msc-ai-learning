# Learning State — Current Handover

_Last maintained: 2026-09-10. Learning evidence through 2026-09-10._

Read `SESSION_WORKFLOW.md` for tutoring rules. `learning_progress.yaml` is the structured dashboard projection; focused lesson/course notes remain the detailed evidence source. Do not infer mastery from code presence alone.

## Three parallel commitments

| Lane | Next useful work | Why / boundary |
|---|---|---|
| Continue | **Search guarantees / complexity consolidation** | Lesson 33 completed the BFS/DFS/UCS/A* implementation block. Do not immediately rewrite all four algorithms again. |
| Parallel | **AIMS5702 representation translation** | Lecture 1 exposed a diagram/index-notation translation cost. Preserve shape reasoning as the anchor and practise diagram ↔ shapes ↔ indices ↔ PyTorch/parameter count. |
| Protect | **A small relevant maths retrieval block** | Keep January AIMS5704 prerequisites alive without turning them into a broad restart. |

These lanes coexist; they are not one sequential queue. FTEC5660 remains deliberately parked until one day before its next lecture.

## Course timing / planning uncertainty

- MSc Term 1 is recorded as **7 Sep–4 Dec 2026**.
- **AIMS5701 Fundamentals** is reported to start one week later than originally planned; exact revised dates are not independently confirmed.
- **AIMS5702 Artificial Intelligence in Practice:** first live lecture was 10 Sep 2026. Only the introductory/Lecture 1 material was covered in class; the dtype/memory/stride/einsum material studied beforehand remains a pre-read preview of later supplied slides.
- AIMS5702 course-specific notes live under `notes/aims5702/` rather than being forced into the numbered preparatory lesson sequence.
- **AIMS5704 Machine Learning Theory** starts **11 Jan 2027** in the stored syllabus.
- FTEC5660 remains a useful learning source, but continued enrolment is uncertain because the learner may be unable to commit to the hackathon final/pitch day. Course-specific FTEC work is deliberately parked for now.
- **Return trigger for Agentic AI:** one day before the next FTEC5660 lecture. The exact calendar date is intentionally not invented here.

## AIMS5702 — Lecture 1 reflection + pre-read bridge

Source: `notes/aims5702/lecture01_02_prelecture_bridge.md` plus prior Lessons 10, 11, 27–31.

### Representation translation is now an explicit learning objective

Lecture 1 used mathematical `i/j/...` index notation heavily and presented MLP/parameter-count reasoning through network/flowchart diagrams. The learner reports reasoning much more naturally through tensor shapes and does **not** want to replace that representation.

Treat this as a translation gap rather than automatically as a conceptual gap. Existing preparation already supports shape tracing and MLP parameter counting.

Preferred strategy:

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

Example bridge:

```text
X_ij                    -> X.shape = (i,j)
W_jk                    -> W.shape = (j,k)
Σ_j X_ij W_jk           -> (i,j) @ (j,k)
Y_ik                    -> Y.shape = (i,k)
```

When semantic labels help:

```text
i = batch/sample
j = input feature
k = output feature
```

For simple implementation, keep ordinary shape reasoning and `@`/`matmul` as the natural code representation. `einsum` is useful as a bridge to index/contraction notation and for more general tensor contractions; it should not displace the learner's successful shape-first reasoning.

### Existing preparation that transferred cleanly

Cold recall before class showed that the learner could retrieve:

- tabular `(samples, features)` shape semantics;
- reduction/axis reasoning: the reduced dimension disappears;
- broadcasting a `(features,)` vector across `(samples,features)`;
- matrix-multiplication output shapes and sample preservation;
- reduction shapes after tensor transformations.

This aligns with Lessons 10, 11 and 27. Image/channel conventions were explicitly treated as new course material, not falsely cold-tested as prior learning.

### Pre-read systems foundation — not yet lecture-covered

Before class, later supplied slides were previewed. These concepts are **guided pre-read evidence**, not material actually taught in Lecture 1:

```text
8 bits = 1 byte
float32 = 4 bytes/value
float16 = 2 bytes/value
int8 = 1 byte/value
number of elements = product(shape)
memory bytes = elements * bytes per element
```

The learner successfully solved changed memory-estimation examples after one initial bytes-vs-GB unit slip.

Floating-point intuition was introduced only at preview depth:

```text
more exponent bits -> wider range
more mantissa/significand bits -> greater precision
```

The new tensor-storage model was:

```text
tensor view = shape + stride + offset over flat underlying storage
```

The learner experimentally verified transpose/view/contiguity behaviour in PyTorch. Fresh fragile point: a sliced view's stride was initially recomputed from its new shape as though it had been repacked contiguously. Durable correction:

> Shape alone does not determine a view's stride. For views, reason from the underlying storage and transformation history.

Basic `einsum` reading was also introduced as guided preview:

```text
ij->i      keep i, sum j
ij->j      keep j, sum i
ij,j->i    matrix-vector product
```

### AIMS5702 next step

Do **not** abandon shape reasoning or restart NumPy wholesale. Next AIMS5702 study block should use actual Lecture 1-style MLP diagrams and practise translation:

1. diagram -> layer widths -> tensor shapes;
2. shapes -> parameter counts;
3. shapes -> index notation and index notation -> shapes;
4. shapes/index notation -> ordinary PyTorch (`@`, `nn.Linear`) and, where useful, equivalent `einsum`;
5. distinguish a failure to translate representations from a failure to understand the underlying operation.

When Lecture 2 systems material is actually taught, cold-check the pre-read rather than replaying it from scratch.

## Search — implementation block completed through Lesson 33

Sources: `lesson_logs/search_reactivation_2026_09_06.md`, Lessons 24–26, and `lesson_logs/lesson33_search_reconstruction.md`.

### BFS

- FIFO / `popleft()` and level-order behaviour were cold-recalled correctly.
- The learner correctly explained that BFS gives a fewest-edge path on an unweighted graph because of its frontier ordering.
- BFS remains the strongest independent search evidence from the 6 September reconstruction.
- During today's reconstruction, the moving path-reconstruction cursor fragility recurred: a moving cursor was created but fixed `current` was initially used inside the loop. This should remain a cold-recall probe.
- A small `path.reverse` vs `path.reverse()` Python slip also appeared.

### DFS

- LIFO / `pop()` behaviour, branch-deepening intuition, and non-shortest-path behaviour were recalled correctly.
- DFS was reconstructed from the BFS skeleton and all practice tests passed after one indentation correction (`return None` had initially remained inside the search loop).
- Keep DFS as guided/refreshed implementation evidence, not pristine cold independence.

### UCS

Lesson 33 introduced and implemented UCS using a priority queue.

```text
frontier entry = (g, node)
g = accumulated cost from start to node
cost_so_far[node] = cheapest known g for that node
```

The learner correctly stated the key update condition conceptually: update when the neighbour is unseen or the new accumulated cost is cheaper. Passing practice tests cover lowest-cost path, start==goal, unreachable goal, cheaper-path replacement, and preferring lower cost over fewer edges.

Support was needed for `heapq` mechanics, tuple unpacking, neighbour/edge-cost roles, unseen-or-cheaper syntax, and pushing `(new_cost, node)`. A trace also exposed an accumulated-cost slip. Therefore UCS is successfully implemented with guided derivation, not independent yet.

### A*

A* was derived directly from UCS:

```text
UCS priority = g(n)
A* priority  = f(n) = g(n) + h(n)
```

Passing practice tests cover lowest-cost path, start==goal, unreachable goal, cheaper-path replacement, heuristic-driven frontier priority, and `h=0` reducing A* to UCS. Support was needed for initial heap shape, tuple unpacking, using the neighbour's heuristic, and keeping `g` separate from `h`. Treat as implemented/guided evidence rather than new cold-independent evidence.

### Search theory still due

Next search block should cover completeness/optimality, UCS non-negative-cost assumptions, A* admissibility vs consistency, goal popped vs discovered, and qualitative/formal time-memory complexity as required by AIMS5701. Only later use one short changed-graph reconstruction to test whether UCS/A* have moved from guided to independent retrieval.

## FTEC5660 / LangChain — parked after Lesson 32

Sources: `lesson_logs/ftec5660_pattern01_prompt_chaining.md`, `lesson_logs/ftec5660_lcel_guided_practice_2026_09_09.md`, `lesson_logs/lesson32_lcel_basics.md`, and `lesson_logs/ftec5660_tutorial01_study_plan.md`.

- Prompt chaining concept is taught: stable sequential stages, checkable handoffs, deterministic processing between LLM stages, and cost/latency/failure trade-offs.
- Lesson 32 implemented prompt templates, string/JSON parsers, invocation dictionaries and simple two-stage LCEL mapping with changed-example tests.
- LCEL remains guided because two-stage composition required support and Python/API role slips (`fn` vs `fn()`, parser class vs instance) recurred.
- Prompt-design cold-recall target remains `Task / Input / Constraints / Output structure`.
- Tutorial 1 follow-up remains parked. Resume one day before the next FTEC5660 lecture with only a 5–10 minute Lesson 32 cold check, then move into `RunnablePassthrough.assign` → `RunnableLambda` → gates using payments/KYC examples.

## Established foundations / remaining uncertainty

- **Python / NumPy / pandas:** substantial practice in Lessons 01–20 and 27. Python syntax/API fluency can still be less automatic than the learner's long-used backend languages.
- **Linear algebra:** historical JHU foundation established; retrieve small relevant blocks rather than restart.
- **Probability/statistics:** Bayes, distributions, joint moments, inequalities and CLT/inference have strong historical evidence. Markov chains and Poisson remain diagnostic-needed rather than proven current mastery.
- **Calculus:** slope → derivatives → partials → gradients → chain rule/backprop is historically established.
- **Practical ML:** linear/logistic regression and the Lesson 31 train/validation/test workflow are implemented; transfer should be tested on changed tasks.
- **AIMS5702 representation translation:** newly identified learning need. Shape reasoning is the anchor; index/diagram fluency should be trained as translation, not replacement.
- **AIMS5702 systems/tensor representation:** dtype memory, flat storage, stride/view/contiguity and basic einsum are guided pre-read material from 10 Sep and need later retrieval when the course reaches them.
- **January extensions:** likelihood/MLE, exponential families, formal generalisation/concentration, convergence assumptions and proof-style derivations remain genuinely new work.

## Parked / must return

- **AIMS5701:** next consolidate search guarantees/complexity; light logic preview before W1; trees/random forests before W3; Bayes retrieval before W4; Markov diagnostic before W5.
- **AIMS5702:** next course-specific review should train diagram/index/shape translation from Lecture 1 examples. Later systems/GPU work should follow the actual course sequence.
- **FTEC5660:** deliberately parked. Resume one day before the next lecture from `ftec5660_tutorial01_study_plan.md`; do not replay Lesson 32 in full.
- **Maths:** selective LA/calculus/probability maintenance; later MLE and formal-theory extensions.

## Handover discipline

After the next substantive session, update its focused log/course note and this handover. `learning_progress.yaml` remains due for structured-dashboard maintenance: Lesson 33 materially changed UCS/A* evidence, and AIMS5702 now has a course-specific representation-translation target plus guided pre-read systems material.
