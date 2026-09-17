# Learning State — Current Handover

_Last maintained: 2026-09-17. Learning evidence through 2026-09-17._

Read `SESSION_WORKFLOW.md` for tutoring rules. `learning_progress.yaml` is the structured learning-evidence projection; `deadlines.yaml` is the separate delivery-planning record used for explicit workload constraints. Focused lesson/course notes remain the detailed evidence source. Do not infer mastery from code presence or deadline urgency.

## Three parallel commitments

| Lane | Next useful work | Why / boundary |
|---|---|---|
| Continue | **AIMS5702 Assignment 1 scaffold, then independent attempt** | Assignment 1 is due 24 Sep and is now the nearest assessed deadline. Pairwise dot-product representations have been implemented in changed-example practice; next gap is vectorised indexing / bilinear interpolation. |
| Parallel | **FTEC5660 receipts homework + routing / conditional-workflow bridge** | Receipts homework is due 29 Sep. Resume as the dominant delivery lane after the AIMS5702 submission; use coursework as the main implementation vehicle where possible. |
| Protect | **AIMS5701 search JIT → regression/trees + small probability maintenance** | Search theory remains due, then decision trees/random forests for Week 3. Keep probability small until Bayesian/HMM pressure increases. |

These lanes coexist; they are not one sequential queue. Delivery dates can temporarily resize them, but a deadline is not itself learning evidence.

## Delivery constraints — separate from learning evidence

Canonical structured copy: `deadlines.yaml`. Current order is AIMS5702 Assignment 1 (24 Sep), FTEC5660 receipts homework (29 Sep), then FTEC5660 solo hackathon (19 Oct). Keep delivery planning distinct from `learning_progress.yaml`.

## AIMS5702 — Assignment 1 preparation, 17 Sep

Sources: `lesson_logs/aims5702/lecture01_02_prelecture_bridge.md`, `lesson_logs/aims5702/tensor_cold_review_2026_09_11.md`, `lesson_logs/aims5702/assignment01_tensor_vectorisation_plan_2026_09_17.md`, and `practice/aims5702_assignment01/`.

### Pre-lecture retrieval / refresh

The learner began with changed tensor examples before the 17 Sep maths lecture.

Evidence observed:

- reduction output shapes were retrieved correctly immediately, though the first semantic description mixed up the reduced time axis with the feature axis;
- integer indexing vs one-element slicing was rusty on first retrieval (`x[:, 1]` was initially predicted to retain a singleton dimension), then corrected and immediately transferred to `1:2` slice examples;
- broadcasting output shapes were generally retrieved correctly; semantic descriptions became reliable once values were attached to axes;
- singleton-axis meaning was understood as “reuse/broadcast along this axis”; sample/time/feature roles were successfully traced on changed examples;
- `unsqueeze` was not initially retrieved by name (`reshape` was proposed), but after introduction the learner correctly chose `unsqueeze(0)` / `unsqueeze(1)` on changed examples.

Do not promote slicing/`unsqueeze` API syntax to cold-independent based on immediate corrected retrieval.

### Pairwise dot products — concept and implementations

The learner built the operation from first principles:

```text
x: (m, k)
y: (n, k)

for each x row and y row:
    multiply matching k features
    sum over k

result: (m, n)
```

Durable mathematical model:

```text
z[m,n] = sum_k x[m,k] * y[n,k]
```

Equivalent linear-algebra description: the pairwise dot-product matrix is `X Y^T`, though the practice deliberately avoids matrix-multiplication shortcuts.

#### Single dot product

The learner implemented independently after the test contract was isolated:

```python
return (x * y).sum()
```

Key understanding: dot product = elementwise multiplication followed by reduction over the feature dimension.

#### Two-loop representation

The learner independently proposed the core construction:

```text
for each row m of x:
    for each row n of y:
        result[m,n] = dot_product(x[m], y[n])
```

Python/API support was needed for:

- `range(len(x))` rather than iterating over `len(x)` directly;
- allocating the result buffer with `torch.zeros((len(x), len(y)))` rather than the initially recalled `arange`-like idea.

Final implementation uses exactly two Python loops; the feature axis is handled inside `dot_product`, not by a third Python loop.

#### Broadcasting representation

The learner first derived the shape plan interactively, including one correction for the `y` singleton placement, then transferred it correctly to changed dimensions:

```text
(m, k) -> (m, 1, k)
(n, k) -> (1, n, k)

multiply -> (m, n, k)
sum k   -> (m, n)
```

During initial expression writing, the learner needed reminders that `unsqueeze` returns a tensor rather than mutating the original and that `.sum()` without a dimension would reduce everything. After that correction, the learner wrote the complete changed-example expression independently:

```python
(x.unsqueeze(1) * y.unsqueeze(0)).sum(axis=2)
```

and later implemented the practice function directly from recall.

Current conceptual heuristic:

> Broadcasting replaces the two outer Python loops by representing the x-row and y-row pairings as tensor axes; reduction consumes the feature axis.

#### Einsum representation

`einsum` moved from guided pre-read into guided implementation with successful immediate transfer.

The learner correctly reasoned that:

- output indices survive;
- an input index omitted from the output is reduced/summed;
- `ij->i` reduces `j`, `ij->j` reduces `i`, and `ij->ji` transposes;
- pairwise row dot products can be described as `mk,nk->mn` (or equivalent letters).

The learner transferred this to a changed customer/product example (`ik,jk->ij`) and then implemented:

```python
return torch.einsum("mk,nk -> mn", x, y)
```

### Evidence boundary for 17 Sep practice

The implementations are present on the practice branch and the learner reported pushing them after working through the red-test sequence. This is strong **same-session guided-to-independent implementation evidence**, not delayed cold mastery.

Strong current evidence:

- understands a single dot product as elementwise multiply + sum;
- understands pairwise dot products as every x-row paired with every y-row;
- can explain why output shape is `(m,n)` and why `k` disappears;
- can relate the two-loop, broadcasting and einsum versions as three representations of the same computation;
- successfully transferred broadcasting shapes and einsum index notation to changed dimensions/examples during the session;
- wrote the final broadcasting and einsum practice implementations without the solution being supplied as assignment code.

Still fragile / needs delayed retrieval:

- Python allocation/iteration syntax (`range(len(...))`, tensor allocation) was not cold;
- slicing integer-index vs slice dimension preservation recovered quickly but was initially rusty;
- `unsqueeze` API name/axis manipulation was initially guided;
- broadcasting expression construction initially needed reminders about returned tensors and specifying the reduction dimension;
- einsum is newly learned and only has same-session transfer evidence;
- no evidence yet for vectorised advanced indexing or bilinear interpolation;
- the actual Assignment 1 functions have not been independently attempted and must not be marked complete from the practice code.

### AIMS5702 next step

Do not over-drill pairwise dot products immediately.

Next useful sequence:

1. attend/reconcile the 17 Sep maths lecture against this pre-lecture scaffold;
2. on a later block, briefly cold-retrieve one changed pairwise example rather than replaying the full lesson;
3. move to vectorised indexing: floor/integer coordinate indices, gathering many grid values with tensor indices, and shape prediction;
4. build 1D interpolation intuition, then one 2D bilinear interpolation example;
5. trace the supplied loop reference and ask what shape each scalar-per-point variable would have if all points were represented simultaneously;
6. only then attempt the actual Assignment 1 notebook independently, using hints/debugging rather than copied solutions.

## FTEC5660 / LangChain — current boundary

Lesson 34 has successful guided implementation + passing tests + immediate state tracing + architectural synthesis, but not delayed cold-independent implementation. Tutorial 1 is conceptually learned with implementation only partially learned. On 17 Sep, a changed-domain cold session retrieved the core decomposition and structural-vs-semantic validation distinction well; callable timing recovered after probing, while `.assign()` syntax and nested-state access still required correction. Routing was retrieved conceptually as execution-path selection rather than mere state enrichment; actual `RunnableBranch` syntax remains to be cold-retrieved. Tutorial 2 progress is through the end of **Part 1: Routing** only; parallelisation/reflection have not yet been covered.

Near-term delivery: receipts homework due 29 Sep; detailed project plan is in `lesson_logs/ftec5660/hw1_receipt_chain_project_plan_2026_09_15.md`. Hackathon due 19 Oct, solo by learner choice.

## AIMS5701 / search and trees

- BFS has strongest current independent evidence.
- DFS was reconstructed with refreshed/guided evidence.
- UCS/A* are implemented with passing practice tests but remain guided rather than cold-independent.
- Next search block: completeness/optimality, UCS non-negative-cost assumptions, A* admissibility vs consistency, goal popped vs discovered, and qualitative/formal complexity.
- After the Week-2 search pressure, shift JIT preparation toward Week-3 regression + decision trees/random forests; trees remain new material.

## Established foundations / remaining uncertainty

- **Python / NumPy / PyTorch:** conceptual shape reasoning often leads syntax/API fluency. Slicing, allocation and axis-manipulation APIs should continue to be recovered through implementation rather than memorised in isolation.
- **Linear algebra:** historical JHU foundation established; retrieve selectively.
- **Probability/statistics:** strong historical evidence across major foundations; Markov chains/Poisson remain diagnostic-needed.
- **Calculus:** historical derivative/gradient/chain-rule/backprop foundation established.
- **Practical ML:** linear/logistic regression and train/validation/test workflow implemented; changed-task transfer still useful.
- **Agentic/LCEL:** stateful composition/gates have guided implementation evidence; routing conceptually retrieved; `RunnableBranch` implementation and later Tutorial 2 parts remain open.
- **January extensions:** likelihood/MLE, exponential families, formal generalisation/concentration, convergence assumptions and proof-style derivations remain new work.

## Handover discipline

After substantive AIMS5702 Assignment 1 work, update the focused assignment plan and this handover. Update `learning_progress.yaml` only when the structured learning-evidence state materially changes. Update `deadlines.yaml` whenever assessed-work dates/statuses change. Do not promote same-session corrected/guided tensor work to delayed cold mastery, and do not treat practice implementations as evidence that the actual assignment has been independently completed.
