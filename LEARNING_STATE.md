# Learning State — Current Handover

_Last maintained: 2026-09-10. Learning evidence through 2026-09-10._

Read `SESSION_WORKFLOW.md` for tutoring rules. `learning_progress.yaml` is the structured dashboard projection; focused lesson logs remain the detailed evidence source. Do not infer mastery from code presence alone.

## Three parallel commitments

| Lane | Next useful work | Why / boundary |
|---|---|---|
| Continue | **Search guarantees / complexity consolidation** | Lesson 33 completed the BFS/DFS/UCS/A* implementation block. Do not immediately rewrite all four algorithms again. |
| Parallel | **Short AIMS5701 logic preview** | Agentic AI remains deliberately parked until one day before the next FTEC5660 lecture. |
| Protect | **A small relevant maths retrieval block** | Keep January AIMS5704 prerequisites alive without turning them into a broad restart. |

These lanes coexist; they are not one sequential queue.

## Course timing / planning uncertainty

- MSc Term 1 is recorded as **7 Sep–4 Dec 2026**.
- **AIMS5701 Fundamentals** is reported to start one week later than originally planned; exact revised dates are not independently confirmed.
- **AIMS5704 Machine Learning Theory** starts **11 Jan 2027** in the stored syllabus.
- FTEC5660 remains a useful learning source, but continued enrolment is uncertain because the learner may be unable to commit to the hackathon final/pitch day. Course-specific FTEC work is deliberately parked for now.
- **Return trigger for Agentic AI:** one day before the next FTEC5660 lecture. The exact calendar date is intentionally not invented here.

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

Passing practice tests cover:

- lowest-cost path;
- start==goal;
- unreachable goal;
- cheaper-path replacement;
- preferring lower cost over fewer edges.

Support was needed for `heapq` mechanics, tuple unpacking, neighbour/edge-cost roles, unseen-or-cheaper syntax, and pushing `(new_cost, node)`. A trace also exposed an accumulated-cost slip (`2 + 3` initially treated as `3`). Therefore UCS is **successfully implemented with guided derivation**, not independent yet.

### A*

A* was derived directly from UCS:

```text
UCS priority = g(n)
A* priority  = f(n) = g(n) + h(n)
```

The learner understood that the heap must preserve both priority and true path cost, leading to entries shaped as:

```text
(f, g, node)
```

Passing practice tests cover:

- lowest-cost path;
- start==goal;
- unreachable goal;
- cheaper-path replacement;
- heuristic-driven frontier priority;
- `h=0` reducing A* to UCS.

Support was needed for initial heap shape, tuple unpacking, using the **neighbour's** heuristic, and keeping `g` separate from `h`. Therefore A* is current implemented/guided evidence rather than new cold-independent evidence.

### Compact comparison to retain

```text
BFS  -> FIFO / discovery order
DFS  -> LIFO / most recently discovered
UCS  -> lowest g
A*   -> lowest g + h
```

```text
g(n) = real accumulated cost from start to n
h(n) = estimated remaining cost from n to goal
f(n) = g(n) + h(n)
```

### Search theory still due

Implementation success does **not** establish the guarantees/complexity material.

Next search block should cover:

1. completeness and optimality across BFS / DFS / UCS / A*;
2. assumptions behind UCS optimality, especially non-negative edge costs;
3. admissibility vs consistency for A*;
4. why UCS/A* stop when the goal is **popped**, not merely discovered;
5. qualitative then formal time/memory complexity as required by AIMS5701;
6. confirm what the course means by “searching with other agents” before teaching it.

Only later use one short changed-graph reconstruction to test whether UCS/A* have moved from guided to independent retrieval.

## FTEC5660 / LangChain — parked after Lesson 32

Sources: `lesson_logs/ftec5660_pattern01_prompt_chaining.md`, `lesson_logs/ftec5660_lcel_guided_practice_2026_09_09.md`, `lesson_logs/lesson32_lcel_basics.md`, and `lesson_logs/ftec5660_tutorial01_study_plan.md`.

- Prompt chaining concept is taught: stable sequential stages, checkable handoffs, deterministic processing between LLM stages, and cost/latency/failure trade-offs.
- Lesson 32 implemented prompt templates, string/JSON parsers, invocation dictionaries and simple two-stage LCEL mapping with changed-example tests.
- LCEL remains **guided**, because two-stage composition required support and Python/API role slips (`fn` vs `fn()`, parser class vs instance) recurred.
- Prompt-design cold-recall target remains:

```text
Task
Input
Constraints
Output structure
```

- Tutorial 1 follow-up remains parked. Resume one day before the next FTEC5660 lecture with only a 5–10 minute Lesson 32 cold check, then move into `RunnablePassthrough.assign` → `RunnableLambda` → gates using payments/KYC examples.
- The large US-tax notebook remains an architecture illustration, not something to memorise or reproduce.

## Established foundations / remaining uncertainty

- **Python / NumPy / pandas:** substantial practice in Lessons 01–20 and 27. Python syntax/API fluency can still be less automatic than the learner's long-used backend languages.
- **Linear algebra:** historical JHU foundation established; retrieve small relevant blocks rather than restart.
- **Probability/statistics:** Bayes, distributions, joint moments, inequalities and CLT/inference have strong historical evidence. Markov chains and Poisson remain diagnostic-needed rather than proven current mastery.
- **Calculus:** slope → derivatives → partials → gradients → chain rule/backprop is historically established.
- **Practical ML:** linear/logistic regression and the Lesson 31 train/validation/test workflow are implemented; transfer should be tested on changed tasks.
- **January extensions:** likelihood/MLE, exponential families, formal generalisation/concentration, convergence assumptions and proof-style derivations remain genuinely new work.

## Parked / must return

- **AIMS5701:** next consolidate search guarantees/complexity; light logic preview before W1; trees/random forests before W3; Bayes retrieval before W4; Markov diagnostic before W5.
- **AIMS5702:** scientific-Python/representation work before W3; CNN/RNN preview before W4; transfer the real-data workflow to neural regression before W5.
- **FTEC5660:** deliberately parked. Resume **one day before the next lecture** from `ftec5660_tutorial01_study_plan.md`; do not replay Lesson 32 in full.
- **Maths:** selective LA/calculus/probability maintenance; later MLE and formal-theory extensions.

## Handover discipline

After the next substantive session, update its focused log and this handover. `learning_progress.yaml` should also be updated when the structured dashboard is next maintained: Lesson 33 materially changes UCS/A* evidence and the continue-lane target from implementation to guarantees/complexity. Historical detail belongs in focused logs, not this handover.
