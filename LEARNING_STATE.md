# Learning State — Current Handover

_Last updated: 2026-09-05_

> Update this file at the end of **every study session**. Keep it short. It should answer: **Where am I now, what is fragile, what is parked, and what should happen next?**

## Current phase

- MSc Term 1: **7 Sep–4 Dec 2026**.
- Immediate courses: **Fundamentals in AI (AIMS5701)** and **AI in Practice (AIMS5702)**.
- **Machine Learning Theory (AIMS5704)** starts **11 Jan 2027**; probability/statistics/LA preparation must run during Term 1.
- Strategy: stay roughly **1–2 syllabus weeks ahead** while keeping a small January-maths lane alive.
- Lesson-log backfill is complete: **Lessons 01–31 all have retrieval logs**; `lesson_logs/INDEX.md` is the coverage index.
- Historical pre-repo maths is now documented in two durable tracks: calculus and the completed 2025 JHU linear-algebra sequence.

## Verified learning position

### Python / DSA / data
- Core Python containers/functions/comprehensions and DSA patterns practised in lessons 01–09.
- NumPy/Pandas foundations substantial (10–20, 27).
- pytest is comfortable and remains useful as learning scaffolding.

### Linear algebra
- JHU Coursera **Linear Algebra from Elementary to Advanced** was completed in 2025; this is established prior learning, not an unfinished prerequisite.
- Historical retrieval logs now preserve: systems/RREF/free variables/span/basis; determinants/eigenvalues/eigenvectors/diagonalization; orthogonality/Gram–Schmidt/projections/least squares; symmetric matrices/orthogonal diagonalization/quadratic forms.
- Current cold retrieval shows the conceptual structure survives, with arithmetic/procedural slips more likely than complete conceptual loss.
- Treat LA as a **maintenance/application lane** during Term 1, not a course to restart. Use short retrieval before AIMS5702/AIMS5704 topics that invoke it.

### Classical ML
- sklearn logistic regression/classification workflow (21–22) and linear regression (23) implemented.
- Historical least-squares/normal-equation work gives the geometric/mathematical foundation under linear regression.
- Linear/logistic regression need consolidation, not first exposure; decision trees/random forests are still new.

### Search
- BFS, DFS and A* implemented in lessons 24–26.
- Search remains deliberately parked pending **cold retrieval + comparison/theory + UCS + heuristic properties**.

### Calculus / optimisation / PyTorch
- Power/product rules, partial derivatives, gradients, chain rule and manual backprop understood.
- Autograd/manual GD (28), standard linear training loop (29), synthetic binary MLP (30) implemented.

### Lesson 31 — real-data ML workflow (COMPLETE)
- Repo now contains `deep_learning/mlp/lesson31_real_data.py`, `deep_learning/mlp/test_lesson31_real_data.py`, and `lesson_logs/lesson31_real_data_workflow.md`.
- Implemented in the exercise:
  - `load_data()` using sklearn breast-cancer data; X `(569,30)`, y `(569,)`.
  - stratified 60/20/20 train/validation/test split; shapes train 341, val 114, test 114.
  - `StandardScaler` fit on TRAIN only; validation/test transformed with frozen train statistics.
  - NumPy → float32 tensors; binary labels reshaped `(n,) -> (n,1)`.
  - shuffled `TensorDataset`/`DataLoader` helper.
  - `make_classifier()` architecture `30 -> 16 -> ReLU -> 1`.
  - epoch/batch training loop with SGD + `BCEWithLogitsLoss`, average train loss per epoch, validation loss under `torch.no_grad()`.
  - binary accuracy: logits → sigmoid → threshold → compare to targets.
- Tests cover data loading/splitting/scaling/tensor conversion, classifier shape, prepared split shapes, and the end-to-end experiment contract.
- **Resolved:** `test_lesson31_real_data.py` was importing `make_classifier` from Lesson 30 (10-input classifier) instead of Lesson 31's own 30-input classifier, causing `test_make_classifier` to fail with a shape mismatch on `(32, 30)` input. Fixed by importing `make_classifier` from `lesson31_real_data` directly; all tests now pass.
- Completed `prepare_data()` and `run_experiment()` integration: the real dataset now flows through split/scaling/tensor/DataLoader preparation, training with per-epoch train/validation histories, and one final held-out test-accuracy evaluation.
- Verified on 2026-09-04: Lesson 31 plus dashboard tests pass (`9 passed`).
- Optional continuation only: retain and restore the best-validation checkpoint if early stopping/model selection is added later; this is not required to close Lesson 31.

## Fragile under cold recall

### Linear algebra retrieval targets
- Echelon form vs RREF; pivot/free-variable interpretation and parametric vector form.
- Determinant/characteristic-polynomial sign arithmetic; use trace/determinant checks for 2×2 eigenvalue work.
- Eigenvector sign/scaling equivalence and keeping `P` column order matched with `D`.
- Gram–Schmidt: subtract projections; scaling orthogonal basis directions is fine.
- Projection residual: a scaled normal vector stays perpendicular but is no longer the exact `z = y - y*`.
- Least squares: keep `A^T A x = A^T b`, the inverse form, and residual condition `A^T r = 0` distinct from diagonalization.
- Orthogonal matrix test is `Q^TQ=I`; determinant ±1 alone is not sufficient.
- Quadratic-form cross terms split across symmetric off-diagonal entries.

### Practical ML / tensor retrieval targets
- `nn.Linear(in, out).weight.shape == (out, in)`; batch dimension occasional quick slips.
- Standardisation: mean ≈ 0, std ≈ 1 on TRAIN; validation/test use TRAIN scaler stats and need not themselves have mean 0/std 1.
- `len(train_loader)` = number of batches; `train_loader.batch_size` = samples per normal batch.
- Epoch loss bookkeeping: simple current approach averages batch-average losses via `/ len(train_loader)`; final partial-batch weighting is a later refinement.
- Accuracy requires comparing predictions to targets; `predictions.mean()` only measures fraction predicted class 1.
- Keep logit → probability → class distinction automatic.
- Search theory completeness/optimality/time/memory and heuristic properties remain non-automatic.

## Active highest-value sequence

1. **Search reactivation** — BFS/DFS/A* cold recall; compare them; add UCS/heuristic theory and light logic preview.
2. **Fundamentals Week-3 buffer** — linear/logistic retrieval, then decision trees/random forests.
3. **January maths lane** — probability/statistics is the main new prerequisite gap; insert short linear-algebra/calculus retrieval where upcoming material invokes it.
4. **Optional Lesson 31 continuation** — add best-validation-checkpoint restoration if revisiting early stopping/model selection.

# PARKED / MUST RETURN

- [~] **BFS / DFS / A\*** — implemented lessons 24–26; reactivation pending.
- [ ] **Logic/reasoning** — Fundamentals Week 1 preview.
- [ ] **Decision trees / random forests** — Fundamentals Week 3.
- [x] **Real-data PyTorch classification** — Lesson 31 complete; best-validation-checkpoint restoration is optional continuation work.
- [~] **Historical linear algebra retrieval** — JHU foundation established and documented; retrieve in short targeted blocks rather than relearn from zero. Strengthen norms, positive-definite/semidefinite and Gram-matrix/kernel applications when ML Theory requires them.
- [ ] **NN regression / housing-price workflow** — AI in Practice Week 5.
- [ ] **CNN/RNN architecture preview** — AI in Practice Week 4.
- [ ] **Probability/statistics refresh** — recurring Term-1 lane for ML Theory January.
- [ ] **Formal complexity / graph-tree DSA** — reinforce around search.
- [ ] **Vector/Jacobian calculus** — defer until needed.

## Near-term syllabus runway

### Fundamentals
- W1: introduction, logic, reasoning, learning → logic is the immediate unfamiliar piece.
- W2: uninformed/informed/multi-agent search → BFS/DFS/A* already coded; reactivate and deepen.
- W3: linear/logistic regression, decision trees, random forests → first two practised; trees/forests are the gap.

### AI in Practice
- W1–2: simple ML + vector/matrix/tensor/NumPy → current prep is strong; historical JHU LA means the matrix layer is retrieval/application rather than first exposure.
- W3: representations + SciPy/matplotlib/PyTorch → PyTorch strong enough; plotting/SciPy not yet systematic.
- W4: MLP/CNN/RNN → MLP ahead; CNN/RNN pending.
- W5: housing-price prediction → regression workflow needs real-data/NN practice.

### ML Theory — January risk lane
- Probability/statistics is the main prerequisite gap.
- Linear algebra is established historically but needs periodic retrieval and ML-specific reactivation (norms, quadratic forms, positive definiteness, Gram matrices/kernels).
- GD/backprop mechanics are an advantage, but convergence/generalisation theory is not yet prepared.

## Next session target

> **Reactivate search:** cold-retrieve BFS, DFS and A*, compare completeness/optimality/time/memory, then add UCS and heuristic admissibility/consistency.

The linear-algebra backfill is now complete as a retrieval resource; it should not displace immediate Week-1/2 MSc preparation. Pull from it tactically when live course material calls for the maths.

## End-of-session update

- **Completed:** historical JHU linear-algebra foundation reconstructed into four retrieval logs plus a foundations index; README, roadmap, syllabus map and dashboard state aligned with the fact that the course was completed in 2025.
- **Now represented accurately:** linear algebra is established prior learning with retrieval due, not a developing/unlearned prerequisite.
- **Still fragile:** arithmetic/procedural details under cold recall (RREF, determinant signs, GS subtraction, exact residuals, eigenvalue/eigenvector ordering, least-squares mechanics) deserve short retrieval; probability/statistics remains the larger January gap.
- **Newly parked / unparked:** historical linear algebra added as a recurring targeted retrieval lane; immediate search priority unchanged.
- **Next session:** BFS/DFS/A* cold retrieval and comparison, then UCS plus admissibility/consistency.
- **Roadmap/syllabus change needed?** yes — both now distinguish completed JHU LA from genuinely new Term-1 maths work.
