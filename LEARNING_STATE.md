# Learning State — Current Handover

_Last maintained: 2026-09-10. Learning evidence through 2026-09-10._

Read `SESSION_WORKFLOW.md` for tutoring rules. `learning_progress.yaml` is the structured dashboard projection; focused lesson/course notes remain the detailed evidence source. Do not infer mastery from code presence alone.

## Three parallel commitments

| Lane | Next useful work | Why / boundary |
|---|---|---|
| Continue | **Search guarantees / complexity consolidation** | Lesson 33 completed the BFS/DFS/UCS/A* implementation block. Do not immediately rewrite all four algorithms again. |
| Parallel | **AIMS5702 live-course consolidation** | First AI in Practice lecture begins 10 Sep. Pre-lecture bridge covered new dtype/memory/storage concepts; post-lecture review should follow what was actually emphasized. |
| Protect | **A small relevant maths retrieval block** | Keep January AIMS5704 prerequisites alive without turning them into a broad restart. |

These lanes coexist; they are not one sequential queue. FTEC5660 remains deliberately parked until one day before its next lecture.

## Course timing / planning uncertainty

- MSc Term 1 is recorded as **7 Sep–4 Dec 2026**.
- **AIMS5701 Fundamentals** is reported to start one week later than originally planned; exact revised dates are not independently confirmed.
- **AIMS5702 Artificial Intelligence in Practice:** first live lecture is 10 Sep 2026. Course-specific notes now live under `notes/aims5702/` rather than being forced into the numbered preparatory lesson sequence.
- **AIMS5704 Machine Learning Theory** starts **11 Jan 2027** in the stored syllabus.
- FTEC5660 remains a useful learning source, but continued enrolment is uncertain because the learner may be unable to commit to the hackathon final/pitch day. Course-specific FTEC work is deliberately parked for now.
- **Return trigger for Agentic AI:** one day before the next FTEC5660 lecture. The exact calendar date is intentionally not invented here.

## AIMS5702 — pre-lecture bridge completed 10 Sep

Source: `notes/aims5702/lecture01_02_prelecture_bridge.md` plus prior Lessons 10, 11, 27–31.

### Existing preparation that transferred cleanly

Cold recall before introducing new material showed that the learner could retrieve:

- tabular `(samples, features)` shape semantics;
- reduction/axis reasoning: the reduced dimension disappears;
- broadcasting a `(features,)` vector across `(samples,features)`;
- matrix-multiplication output shapes and sample preservation;
- reduction shapes after tensor transformations.

This confirms that much of the supplied Lecture 2 tensor manipulation material overlaps existing NumPy/tensor preparation rather than being wholly new. Image/channel conventions were explicitly treated as **new course material**, not falsely cold-tested as prior learning.

### New systems foundation introduced

The genuinely new block was dtype/storage reasoning:

```text
8 bits = 1 byte
float32 = 4 bytes/value
float16 = 2 bytes/value
int8 = 1 byte/value
number of elements = product(shape)
memory bytes = elements * bytes per element
```

The learner successfully solved changed memory-estimation examples after one initial bytes-vs-GB unit slip.

Floating-point representation was introduced only at course-preview depth:

```text
more exponent bits -> wider range
more mantissa/significand bits -> greater precision
```

Exact IEEE encoding remains new/not required by today's evidence.

### Tensor storage / stride / views

New mental model:

```text
tensor view = shape + stride + offset over flat underlying storage
```

The learner successfully reasoned through 2D contiguous strides and experimentally verified PyTorch transpose behaviour:

```text
x:   shape (2,3), stride (3,1), contiguous
x.T: shape (3,2), stride (1,3), non-contiguous
```

Mutation through the transpose changed the original tensor, confirming shared storage. Basic slicing and explicit index-list selection were contrasted experimentally.

**Fresh fragile point:** when a slice changes shape, the learner initially recalculated strides as if the sliced tensor had been repacked contiguously. Example: for a view of shape `(2,2,4)`, `(8,4,1)` was predicted rather than retaining the original-storage walk `(12,4,1)`. Durable correction:

> Shape alone does not determine a view's stride. For views, reason from the underlying storage and transformation history.

Transpose-axis reasoning improved during the session: `transpose(a,b)` swaps only those axes and their associated stride entries.

### Einstein summation

Introduced at the supplied deck's basic level. Learner can read simple expressions by identifying surviving and contracted indices:

```text
ij->i      keep i, sum j
ij->j      keep j, sum i
ij,j->i    matrix-vector product
```

A numerical example expanded `ij,j->i` into elementwise products followed by a sum. Treat this as newly taught/guided, not independent mastery.

### AIMS5702 next step

After the first lecture, record what the lecturer actually emphasized. A later short cold check should prioritize:

1. dtype/model-memory arithmetic;
2. contiguous stride derivation;
3. view stride after slicing/transpose;
4. shared storage vs contiguity;
5. basic einsum reading;
6. CPU/GPU memory/device movement if the lecture makes it an active expectation.

Do not restart NumPy wholesale unless post-lecture evidence shows a real gap.

## Search — implementation block completed through Lesson 33

Sources: `lesson_logs/search_reactivation_2026_09_06.md`, Lessons 24–26, and `lesson_logs/lesson33_search_reconstruction.md`.

### BFS

- FIFO / `popleft()` and level-order behaviour were cold-recalled correctly.
- The learner correctly explained that BFS gives a fewest-edge path on an unweighted graph because of its frontier ordering.
- BFS remains the strongest independent search evidence from the 6 September reconstruction.
- During today's reconstruction, the **moving path-reconstruction cursor** fragility recurred: a moving cursor was created but fixed `current` was initially used inside the loop. This should remain a cold-recall probe.
- A small `path.reverse` vs `path.reverse()` Python slip also appeared.

### DFS

- LIFO / `pop()` behaviour, branch-deepening intuition, and non-shortest-path behaviour were recalled correctly.
- DFS was reconstructed from the BFS skeleton and all practice tests passed after one indentation correction (`return None` had initially remained inside the search loop).
- This is stronger current evidence than the earlier guided BFS→DFS derivation, but it followed immediate BFS recall and targeted debugging support. Keep DFS as **guided/refreshed implementation evidence**, not pristine cold independence.

### UCS

Lesson 33 introduced and implemented UCS using a priority queue.

Cold-retrievable model:

```text
frontier entry = (g, node)
g = accumulated cost from start to node
cost_so_far[node] = cheapest known g for that node
```

The learner correctly stated the key update condition conceptually: update when the neighbour is unseen **or** the new accumulated cost is cheaper.

Passing practice tests cover lowest-cost path, start==goal, unreachable goal, cheaper-path replacement, and preferring lower cost over fewer edges.

Support was needed for `heapq` mechanics, tuple unpacking, neighbour/edge-cost roles, unseen-or-cheaper syntax, and pushing `(new_cost, node)`. A trace also exposed an accumulated-cost slip (`2 + 3` initially treated as `3`). Therefore UCS is **successfully implemented with guided derivation**, not independent yet.

### A*

A* was derived directly from UCS:

```text
UCS priority = g(n)
A* priority  = f(n) = g(n) + h(n)
```

The learner understood that the heap must preserve both priority and true path cost, leading to entries shaped as `(f, g, node)`.

Passing practice tests cover lowest-cost path, start==goal, unreachable goal, cheaper-path replacement, heuristic-driven frontier priority, and `h=0` reducing A* to UCS.

Support was needed for initial heap shape, tuple unpacking, using the **neighbour's** heuristic, and keeping `g` separate from `h`. Therefore A* is current implemented/guided evidence rather than new cold-independent evidence.

### Compact comparison to retain

```text
BFS  -> FIFO / discovery order
DFS  -> LIFO / most recently discovered
UCS  -> lowest g
A*   -> lowest g + h
```

### Search theory still due

Next search block should cover completeness/optimality, UCS non-negative-cost assumptions, A* admissibility vs consistency, goal popped vs discovered, and qualitative/formal time-memory complexity as required by AIMS5701. Only later use one short changed-graph reconstruction to test whether UCS/A* have moved from guided to independent retrieval.

## FTEC5660 / LangChain — parked after Lesson 32

Sources: `lesson_logs/ftec5660_pattern01_prompt_chaining.md`, `lesson_logs/ftec5660_lcel_guided_practice_2026_09_09.md`, `lesson_logs/lesson32_lcel_basics.md`, and `lesson_logs/ftec5660_tutorial01_study_plan.md`.

- Prompt chaining concept is taught: stable sequential stages, checkable handoffs, deterministic processing between LLM stages, and cost/latency/failure trade-offs.
- Lesson 32 implemented prompt templates, string/JSON parsers, invocation dictionaries and simple two-stage LCEL mapping with changed-example tests.
- LCEL remains **guided**, because two-stage composition required support and Python/API role slips (`fn` vs `fn()`, parser class vs instance) recurred.
- Prompt-design cold-recall target remains `Task / Input / Constraints / Output structure`.
- Tutorial 1 follow-up remains parked. Resume one day before the next FTEC5660 lecture with only a 5–10 minute Lesson 32 cold check, then move into `RunnablePassthrough.assign` → `RunnableLambda` → gates using payments/KYC examples.

## Established foundations / remaining uncertainty

- **Python / NumPy / pandas:** substantial practice in Lessons 01–20 and 27. Python syntax/API fluency can still be less automatic than the learner's long-used backend languages.
- **Linear algebra:** historical JHU foundation established; retrieve small relevant blocks rather than restart.
- **Probability/statistics:** Bayes, distributions, joint moments, inequalities and CLT/inference have strong historical evidence. Markov chains and Poisson remain diagnostic-needed rather than proven current mastery.
- **Calculus:** slope → derivatives → partials → gradients → chain rule/backprop is historically established.
- **Practical ML:** linear/logistic regression and the Lesson 31 train/validation/test workflow are implemented; transfer should be tested on changed tasks.
- **AIMS5702 systems/tensor representation:** dtype memory, flat storage, stride/view/contiguity and basic einsum are **newly introduced 10 Sep** and need later retrieval before any mastery claim.
- **January extensions:** likelihood/MLE, exponential families, formal generalisation/concentration, convergence assumptions and proof-style derivations remain genuinely new work.

## Parked / must return

- **AIMS5701:** next consolidate search guarantees/complexity; light logic preview before W1; trees/random forests before W3; Bayes retrieval before W4; Markov diagnostic before W5.
- **AIMS5702:** after Lecture 1/2, consolidate only the new/fragile systems concepts under `notes/aims5702/`; later CNN/RNN and deployment/GPU work should follow the actual course sequence.
- **FTEC5660:** deliberately parked. Resume **one day before the next lecture** from `ftec5660_tutorial01_study_plan.md`; do not replay Lesson 32 in full.
- **Maths:** selective LA/calculus/probability maintenance; later MLE and formal-theory extensions.

## Handover discipline

After the next substantive session, update its focused log/course note and this handover. `learning_progress.yaml` remains due for structured-dashboard maintenance: Lesson 33 materially changed UCS/A* evidence, and today's AIMS5702 work adds a newly taught systems/tensor-representation area that should not be mislabeled as prior mastery.
