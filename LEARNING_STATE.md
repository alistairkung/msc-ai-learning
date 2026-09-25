# Learning State — Current Handover

_Last maintained: 2026-09-25. Learning evidence through 2026-09-25._

Read `SESSION_WORKFLOW.md` for tutoring rules. `learning_progress.yaml` is the structured learning-evidence projection; `deadlines.yaml` is the separate delivery-planning record used for explicit workload constraints. Focused lesson/course notes remain the detailed evidence source. Do not infer mastery from code presence or deadline urgency.

## Three parallel commitments

| Lane | Next useful work | Why / boundary |
|---|---|---|
| Continue | **24 Sep: AIMS5702 Lecture 3 bridge → lecture** | The planned AIMS5701 reconciliation is complete. Use the remaining pre-lecture study time on 5702 Deep Learning Basics: linear-layer notation/shapes, cross-entropy/objective notation, gradient-descent/SGD mapping, then nonlinearity/MLP/CNN motivation. |
| Parallel | **25/28 Sep: finish FTEC5660 receipts before opening a new build context** | Friday is receipts-only. Continue validation/Decimal normalisation → batching → homework interface → public E2E eval. Monday is contingency if needed; do not switch to trees until receipts is complete. |
| Protect | **After receipts: AIMS5701 trees bridge for next week's lecture** | Once receipts is closed, retrieve linear/logistic classification briefly, then learn split intuition → Gini/entropy/information gain → recursive decision trees → stopping/overfitting → random forests. Search now moves to spaced maintenance rather than consuming another JIT block. |

These lanes coexist; they are not one sequential queue. Delivery dates can temporarily resize them, but a deadline is not itself learning evidence.

## Delivery constraints — separate from learning evidence

Canonical structured copy: `deadlines.yaml`. AIMS5702 Assignment 1 was submitted on 21 Sep. Remaining upcoming assessed work is FTEC5660 receipts homework (29 Sep), then the FTEC5660 solo hackathon (19 Oct). Keep delivery planning distinct from `learning_progress.yaml`.

## AIMS5701 — Search guarantees + adversarial-search bridge, 23 Sep

Detailed source: `lesson_logs/aims5701/search_guarantees_reactivation_2026_09_23.md`.

The afternoon block completed the planned search-theory bridge without repeating BFS/DFS implementation. UCS goal-popped termination and admissibility returned cold. Consistency is improving and is now connected to nondecreasing `f=g+h`, but still had one changed-example label inversion. Completeness vs optimality is understood conceptually. Branching-factor complexity was introduced: BFS `O(b^d)` time/space and DFS `O(b^m)` time, `O(bm)` space are understood intuitively, although `d` vs `m` slipped on immediate recap.

Adversarial search was introduced as pre-lecture preparation. The useful translation key is `MAX = one agent / MAX's turn`, `MIN = opposing agent / MIN's turn`, with terminal utility measured from MAX's perspective. Turn ownership initially caused repeated inversions; after a deliberate reset the learner correctly solved changed minimax trees. Alpha-beta was then derived from player-choice irrelevance before attaching alpha/beta notation. Changed pruning examples were handled with some correction, including one whole-subtree cutoff where MIN's control of the choice was initially forgotten.

Do not promote minimax/alpha-beta to established or independent mastery yet: this is same-session introductory evidence and no implementation has been attempted. The actual Lecture 2 deck did **not** cover minimax/alpha-beta, so park implementation unless a later live-course requirement brings adversarial search back.

Implementation-maintenance decision: do not immediately rebuild BFS/DFS/UCS/A* merely for completeness. Prior implementation evidence already exists; use later changed-problem blank-file reconstruction as an operational spot check when useful.

The 24 Sep reconciliation is now complete. Smaller lecture gaps were swept: state abstraction, graph-vs-tree search, iterative deepening, greedy best-first, relaxed-problem heuristics/dominance and graph-search duplicate handling. Iterative deepening needed one reteach of the actual repeated depth-limited DFS mechanism, after which the learner correctly reasoned why repeated shallow work is cheap relative to deeper exponential growth.

The difficult A* guarantee material materially improved. Consistency is now grounded in the local-edge intuition “heuristic drop cannot exceed step cost”; changed examples were classified correctly. The learner reconstructed consistency ⇒ admissibility on a changed path, reconstructed the A* blocking proof to `f(n) <= f(A) < f(B)` with scaffolding at the first inequality, and connected consistency ⇒ nondecreasing `f` ⇒ safe permanent closing. Admissibility’s exact role in the optimality proof needed one correction, so this is **guided proof reconstruction**, not delayed cold proof mastery.

Search now moves to spaced maintenance. Next AIMS5701 JIT: brief linear/logistic retrieval, then decision-tree split/impurity/information-gain intuition and random forests — but only after the receipts homework is complete.

## Immediate execution plan — 24 to 28 Sep

This short-horizon sequence is intentionally serial to reduce context switching:

```text
24 Sep
AIMS5701 reconciliation — COMPLETE
-> AIMS5702 targeted pre-lecture study — NEXT
-> AIMS5702 Lecture 3

25 Sep
FTEC5660 receipts only

28 Sep
receipts contingency until complete
-> then AIMS5701 decision-tree bridge
```

Detailed AIMS5702 preparation source: `lesson_logs/aims5702/lecture03_deep_learning_basics_prelecture_bridge_2026_09_24.md`.

The supplied Lecture 3 deck overlaps strongly with existing PyTorch/MLP training evidence. Do not re-teach train/validation/test, overfitting, DataLoader basics or generic training-loop mechanics from zero. Highest-value pre-lecture targets are:

- translate `y_j = Σ_i w_ij x_i + b_j` into index meaning, shapes and code semantics;
- unpack one-hot/cross-entropy and dataset-level objective notation;
- map formal gradient-descent/SGD notation onto the already-known PyTorch loop;
- explain why stacked linear maps need nonlinearity;
- preview locality + weight sharing as the motivation for CNNs.

Friday/Monday receipts work retains the existing constrained architecture and scope rule. Trees begin only once receipts is closed.

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

## FTEC5660 / LangChain — receipts HW1 complete

Detailed sources:
- `lesson_logs/ftec5660/hw1_receipt_chain_session_2026_09_21.md`
- `lesson_logs/ftec5660/hw1_receipt_chain_session_2026_09_22.md`
- `lesson_logs/ftec5660/hw1_receipt_chain_completion_2026_09_25.md`

The receipts homework is complete and submitted. The final public path passed 27/27 deterministic tests, processed all seven public receipts, and produced both correct aggregate answers.

The completed architecture separates probabilistic vision extraction from deterministic validation/calculation. `ReceiptValidator` normalises money to Decimal and reconciles item/discount/subtotal/rounding invariants. Real batch evaluation exposed legitimate zero-value marker lines and stochastic model errors including quantity unit-price vs extended-total confusion; the validator and prompt rules were corrected from that evidence.

The learner pushed the per-receipt path into a composed LCEL runnable:

```text
prompt | llm | JsonOutputParser | RunnableLambda(validate)
                              -> semantic retry on ValueError
```

This is meaningful changed-domain transfer of LCEL composition. The broader Runnable API and `RunnableBranch` remain outside cold-independent evidence.

The final grader policy also introduced a deliberate availability trade-off: validated/retrying extraction is preferred, but after bounded retries a raw extraction fallback prevents one stubborn receipt from crashing the entire batch and suppressing `results.csv`.

The lecturer's single-file submission requirement forced the clean modular implementation into `hw1.py` for submission. After submission, the learner froze that repository and created a separate attributed `receipt-agent` project to restore modular extractor/validator/calculator boundaries and add a cleaner standalone pipeline/CLI. Treat this as post-submission engineering reflection, not additional course mastery.

Receipts should now leave the active build queue. Next FTEC5660 delivery pressure is the 19 Oct solo hackathon; next JIT learning priority remains the AIMS5701 regression -> decision trees -> random forests bridge.

## AIMS5701 / search and trees

Detailed source: `lesson_logs/aims5701/search_guarantees_reactivation_2026_09_23.md`.

The 23 Sep morning block provided delayed search evidence without replaying implementations:

- BFS mechanics, parents-as-seen/predecessor, FIFO and shortest-by-edges reasoning retrieved strongly.
- DFS LIFO/depth-first behaviour and lack of shortest-path guarantee retrieved strongly.
- UCS initially picked up A*'s heuristic by mistake, then recovered lowest-`g(n)` selection and the cheaper-route update rule.
- UCS termination needed a substantive correction: optimality is guaranteed when the goal is **popped as the minimum-cost frontier item**, not when it is first discovered.
- A* core `g/h/f` definitions, lowest-`f` selection and `h=0 -> UCS` were retrieved correctly after the UCS/A* contamination was corrected.

Guarantee analysis then moved forward. Admissibility was initially inverted, then transferred correctly on changed examples: `h(n) <= h*(n)`. Consistency was the main new/fragile concept and required repeated examples. The current useful model is:

```text
h(B)          = estimated cost still remaining
h(A) - h(B)   = estimated progress
c(A,B)        = actual cost paid

consistent when:
h(A) - h(B) <= c(A,B)
```

After this distinction landed, the learner correctly classified changed consistency examples, including equality, separated admissibility from consistency on an admissible-but-inconsistent example, and connected inconsistency with decreasing `f=g+h` along an edge.

Do not promote guarantee analysis to independent mastery: admissibility was initially inverted and consistency stabilised only after several same-session examples. Completeness/time/space complexity and the stronger consistency→admissibility relationship remain open.

Next search block: briefly cold-check UCS goal-popped, admissibility direction and consistency intuition, then continue with A* assumptions/optimality and completeness/time/memory complexity. Do not replay BFS/DFS. After Week-2 search pressure, shift JIT preparation toward Week-3 regression + decision trees/random forests; trees remain new material.

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
