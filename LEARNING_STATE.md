# Learning State — Current Handover

_Last maintained: 2026-09-21. Learning evidence through 2026-09-21._

Read `SESSION_WORKFLOW.md` for tutoring rules. `learning_progress.yaml` is the structured learning-evidence projection; `deadlines.yaml` is the separate delivery-planning record used for explicit workload constraints. Focused lesson/course notes remain the detailed evidence source. Do not infer mastery from code presence or deadline urgency.

## Three parallel commitments

| Lane | Next useful work | Why / boundary |
|---|---|---|
| Continue | **FTEC5660 receipts homework vertical slice** | AIMS5702 Assignment 1 implementation is complete and all supplied notebook tests are green. Receipts is due 29 Sep; next build the constrained image → structured extraction → validation → deterministic calculation → aggregation path. |
| Parallel | **AIMS5701 search JIT → regression/trees + hackathon planning** | Tuesday includes the hackathon planning meeting. Keep AIMS5701 search/trees preparation alive without displacing the receipts deadline. |
| Protect | **Small probability / ML-theory maintenance lane** | Keep this deliberately small while assessed implementation work is active; do not create a new standalone equation-vectorisation curriculum. |

These lanes coexist; they are not one sequential queue. Delivery dates can temporarily resize them, but a deadline is not itself learning evidence.

## Delivery constraints — separate from learning evidence

Canonical structured copy: `deadlines.yaml`. AIMS5702 Assignment 1 was submitted on 21 Sep. Remaining upcoming assessed work is FTEC5660 receipts homework (29 Sep), then the FTEC5660 solo hackathon (19 Oct). Keep delivery planning distinct from `learning_progress.yaml`.

## AIMS5702 — Assignment 1 preparation and lecture calibration, 17 Sep

Sources: `lesson_logs/aims5702/lecture01_02_prelecture_bridge.md`, `lesson_logs/aims5702/tensor_cold_review_2026_09_11.md`, `lesson_logs/aims5702/assignment01_tensor_vectorisation_plan_2026_09_17.md`, `lesson_logs/aims5702/lecture_reflection_2026_09_17.md`, and `practice/aims5702_assignment01/`.

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

### Post-lecture calibration

The lecture changed the priority of several low-level representation topics. The lecturer appears willing to probe dtype/storage/indexing mechanics explicitly, so these should no longer be treated as incidental API details.

#### Dtype representation

The lecturer asked how `int8` handles negative values; the learner did not follow the explanation confidently. Floating-point terminology around mantissa/significand and exponent also moved too quickly to feel understood or retrievable.

Keep two evidence categories separate:

```text
storage-size reasoning
    vs
bit-level value representation
```

Positive live evidence: the learner correctly calculated VRAM/storage for a `float32` example during the lecture.

Not established: signed `int8` representation and floating-point sign/exponent/mantissa intuition.

#### Strides, contiguity and slicing

Strides/contiguity remain active weaknesses and should receive more deliberate drilling. Future review should connect:

```text
shape
→ flat storage
→ stride
→ indexing/slicing
→ view
→ contiguity
```

The lecturer also used a specific slicing/indexing "trick" or formula that the learner expects may be quiz-relevant. The exact formula was not retained confidently, so recover the lecturer's exact notation from course material before drilling it rather than inventing a substitute.

#### Singleton-axis insertion

The lecturer demonstrated a manual indexing-based way to insert a singleton dimension rather than teaching `unsqueeze()` directly. The learner remembers syntax approximately like `[:, new_dim, :]`, but this is not exact evidence. Recover the actual lecture example first, then connect its semantics to singleton-axis insertion and, only secondarily, to convenience APIs such as `unsqueeze()`.

#### Interpolation sequencing

Do not move directly into interpolation yet. The learner wants a deeper cold review first:

```text
cold tensor/dtype review
    ↓
dtype representation
    ↓
stride / contiguity / slicing
    ↓
singleton-axis insertion / indexing
    ↓
then interpolation
```

### Evidence boundary for 17 Sep

The pairwise implementations are strong **same-session guided-to-independent implementation evidence**, not delayed cold mastery.

Strong current evidence:

- understands a single dot product as elementwise multiply + sum;
- understands pairwise dot products as every x-row paired with every y-row;
- can explain why output shape is `(m,n)` and why `k` disappears;
- can relate the two-loop, broadcasting and einsum versions as three representations of the same computation;
- successfully transferred broadcasting shapes and einsum index notation to changed dimensions/examples during the session;
- correctly performed a `float32` VRAM/storage calculation in live lecture context.

Still fragile / needs delayed retrieval:

- Python allocation/iteration syntax (`range(len(...))`, tensor allocation) was not cold;
- slicing integer-index vs slice dimension preservation recovered quickly but was initially rusty;
- `unsqueeze` API name/axis manipulation was initially guided;
- broadcasting expression construction initially needed reminders about returned tensors and specifying the reduction dimension;
- einsum is newly learned and only has same-session transfer evidence;
- signed integer representation and floating-point sign/exponent/mantissa intuition are not established;
- strides/contiguity and lecturer-specific slicing/indexing mechanics need deeper drilling;
- no evidence yet for vectorised advanced indexing or bilinear interpolation;
- the actual Assignment 1 functions have not been independently attempted and must not be marked complete from the practice code.

### AIMS5702 next step / 18 Sep plan

Tomorrow's substantive study session should focus on **AIMS5702 Assignment 1** rather than splitting the block across courses.

Before breaking down interpolation, begin with a bounded cold review/drill of dtype representation, strides/contiguity, slicing/indexing and singleton-axis insertion, using the lecturer's exact notation where course material is available. Then continue into the assignment scaffold and independent attempt.

FTEC5660 receipts homework is intentionally deferred to the next substantial block planned for Monday; this is workload sequencing, not a change in its evidence state or importance.

## AIMS5702 — 18 Sep representation checkpoint + interpolation bridge

Detailed source: `lesson_logs/aims5702/assignment01_interpolation_bridge_2026_09_18.md`.

The planned prerequisite checkpoint was completed before attempting interpolation implementation.

### Representation evidence

- Storage-size reasoning was retrieved with an initial bits/bytes unit slip; a changed float16 example was then correct.
- Signed `int8` / two's-complement representation was genuinely new at the start of the session. The learner derived the `-128..127` range after teaching and decoded a changed signed bit pattern successfully. This is immediate-transfer evidence only.
- Floating-point sign/exponent/significand roles were clarified. Exponent-range vs significand-precision was initially reversed, then transferred correctly to a changed hypothetical format.
- Stride/contiguity received substantial changed-example drilling. The learner now explains contiguity through logical traversal vs compact underlying storage rather than merely memorising API outcomes.
- The lecturer's storage-index and base-offset formulas were supplied from memory and applied to changed examples.
- A useful fragility was exposed: slice start affects base offset, while slice step affects the view stride. This distinction recovered after correction.
- `start:stop:step` syntax was not initially retrievable when all three fields appeared, then recovered on immediate changed examples.
- `np.newaxis` / `None` singleton insertion was connected to PyTorch `unsqueeze`; changed shape examples were correct.

Do not promote any of this same-session corrected/guided representation work to delayed cold mastery yet.

### Bilinear interpolation

Bilinear interpolation moved from **planned/no evidence** to **conceptually demonstrated with guided derivation and successful manual changed-example execution**.

Current mental model:

```text
normalised query coordinate
    ↓
scale to grid coordinate
    ↓
lower/upper row + column indices
    ↓
row/column fractions
    ↓
gather four neighbouring grid values
    ↓
linear interpolation across top and bottom
    ↓
linear interpolation between those results
```

The learner manually completed a changed bilinear example to the correct final value and understood that the same scalar interpolation expression can operate elementwise over `(N,)` tensors.

Advanced paired indexing `grid[rows, cols]` was introduced as the mechanism for gathering one value per query point without a Python loop. Pairing semantics were understood, although reading values from the toy grid produced a couple of lookup slips.

The supplied Assignment 1 Test 1 harness was also understood: SciPy `RegularGridInterpolator` is the trusted oracle; `x_ref/y_ref` are normalised `[0,1)` query coordinates; `h-1/w-1` scale them into grid space; the student loop/no-loop implementations are compared with the reference within tolerance.

### Current Assignment 1 boundary

Established today:

- conceptual 1D interpolation;
- conceptual bilinear interpolation;
- lower/upper neighbour selection and fractional position;
- conceptual vectorisation path through paired indexing + elementwise arithmetic;
- understanding of the first interpolation test harness.

Not established:

- independent `interp2d_forloop` implementation;
- independent `interp2d_nofor` implementation;
- boundary/edge handling;
- passing interpolation tests;
- delayed cold retrieval of today's new representation/interpolation material.

### AIMS5702 next step

Do not replay today's full lesson.

Next focused block (~2–3 hours expected):

1. brief changed-example retrieval of the fragile pieces;
2. map the supplied loop implementation/context onto lower/upper indices, four neighbours and fractions;
3. learner implements/reconstructs the loop version;
4. lift scalar-per-point variables into `(N,)` tensors;
5. learner implements the no-loop version with advanced indexing and elementwise interpolation;
6. run supplied tests and diagnose boundary/indexing failures.

## AIMS5702 — Assignment 1 implementation complete, 21 Sep

Detailed source: `lesson_logs/aims5702/assignment01_completion_2026_09_21.md`. The learner also supplied the completed notebook as the authoritative Assignment 1 artifact for this session.

Verified notebook evidence:

- all three pairwise-dot-product implementations are present: two-loop, no-loop singleton-axis/vectorised, and einsum;
- supplied pairwise tests are green across changed dimensions, a larger float32 case and invalid-shape cases;
- `interp2d_nofor` is complete;
- supplied interpolation tests are green against SciPy `RegularGridInterpolator`, exact corner/centre cases and invalid-input cases.

### Interpolation implementation evidence

After the weekend, lower/upper neighbour selection and fractions retrieved cold, while the scalar interpolation formula itself needed the cue `start + fraction * (end - start)` before transferring correctly.

The lecturer's matrix bilinear notation was then translated into the geometric model:

```text
x1/x2 -> lower/upper x
y1/y2 -> lower/upper y
Qij   -> corner location
f(Qij)-> value at that corner
```

The learner understood that the four-corner weighted sum is the algebraically expanded version of horizontal top/bottom interpolation followed by vertical interpolation.

For the no-loop implementation, the learner derived the central vectorisation move: promote each per-query scalar into an `(N,)` tensor and process all query points together. Paired advanced indexing gathers the four `(N,)` corner-value tensors, followed by elementwise weighted arithmetic to produce the `(N,)` result.

Targeted support/debugging was needed for `.long()` after `floor`, `torch.clamp(..., max=...)`, device/dtype conversion, corner-gather insertion and ordinary typos. Paired advanced indexing was not initially retrieved after the weekend. `dtype`, `device` and `.to(...)` were newly taught rather than assumed.

### Evidence boundary

Assignment 1 is **implemented, submitted, and supplied tests are green**, but do not mark the interpolation/vectorisation skill as delayed cold-independent mastery. The implementation was guided/debugged and no later blank-file reconstruction has occurred.

The transferable target to maintain is notation/scalar algorithm → tensor shapes → vectorised indexing/arithmetic, not memorisation of the bilinear formula.

AIMS5702 Assignment 1 can leave the active implementation queue unless submission/admin work remains.

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

- **Python / NumPy / PyTorch:** Assignment 1 now has verified green implementations for pairwise vectorisation and no-loop bilinear interpolation. This is guided implementation evidence rather than delayed cold mastery; paired advanced indexing was reactivated on 21 Sep, while dtype/device/.to handling was newly taught.
- **Linear algebra:** historical JHU foundation established; retrieve selectively.
- **Probability/statistics:** strong historical evidence across major foundations; Markov chains/Poisson remain diagnostic-needed.
- **Calculus:** historical derivative/gradient/chain-rule/backprop foundation established.
- **Practical ML:** linear/logistic regression and train/validation/test workflow implemented; changed-task transfer still useful.
- **Agentic/LCEL:** stateful composition/gates have guided implementation evidence; routing conceptually retrieved; `RunnableBranch` implementation and later Tutorial 2 parts remain open.
- **January extensions:** likelihood/MLE, exponential families, formal generalisation/concentration, convergence assumptions and proof-style derivations remain new work.

## Handover discipline

After the next substantive assessed-work block, update the relevant focused log and this handover. Assignment 1 is submitted; do not reopen it merely to manufacture mastery evidence. Update `learning_progress.yaml` only when the structured learning-evidence state materially changes. Update `deadlines.yaml` whenever assessed-work dates/statuses change. Do not promote same-session corrected/guided tensor work to delayed cold mastery, and do not treat practice implementations as evidence that the actual assignment has been independently completed.
