# Learning State — Current Handover

_Last updated: 2026-09-03_  

> Update this file at the end of **every study session**. Keep it short. It should answer: **Where am I now, what is fragile, what is parked, and what should happen next?**

## Current phase

- MSc Term 1: **7 Sep–4 Dec 2026**.
- Immediate courses: **Fundamentals in AI (AIMS5701)** and **AI in Practice (AIMS5702)**.
- **Machine Learning Theory (AIMS5704)** starts **11 Jan 2027**; probability/statistics/LA preparation must run during Term 1.
- Strategy: stay roughly **1–2 syllabus weeks ahead** while keeping a small January-maths lane alive.
- Lesson-log backfill is now complete: **Lessons 01–31 all have retrieval logs**; `lesson_logs/INDEX.md` is the coverage index.

## Verified learning position

### Python / DSA / data
- Core Python containers/functions/comprehensions and DSA patterns practised in lessons 01–09.
- NumPy/Pandas foundations substantial (10–20, 27).
- pytest is comfortable and remains useful as learning scaffolding.

### Classical ML
- sklearn logistic regression/classification workflow (21–22) and linear regression (23) implemented.
- Linear/logistic regression need consolidation, not first exposure; decision trees/random forests are still new.

### Search
- BFS, DFS and A* implemented in lessons 24–26.
- Search remains deliberately parked pending **cold retrieval + comparison/theory + UCS + heuristic properties**.

### Calculus / optimisation / PyTorch
- Power/product rules, partial derivatives, gradients, chain rule and manual backprop understood.
- Autograd/manual GD (28), standard linear training loop (29), synthetic binary MLP (30) implemented.

### Lesson 31 — real-data ML workflow (IN PROGRESS)
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
- Existing tests currently cover data loading/splitting/scaling/tensor conversion plus a classifier-shape test.
- **Resolved:** `test_lesson31_real_data.py` was importing `make_classifier` from Lesson 30 (10-input classifier) instead of Lesson 31's own 30-input classifier, causing `test_make_classifier` to fail with a shape mismatch on `(32, 30)` input. Fixed by importing `make_classifier` from `lesson31_real_data` directly; all tests now pass.
- End-to-end training/validation/test evaluation has **not yet been completed**, so Lesson 31 remains active.

## Fragile under cold recall

- `nn.Linear(in, out).weight.shape == (out, in)`; batch dimension occasional quick slips.
- Standardisation: mean ≈ 0, std ≈ 1 on TRAIN; validation/test use TRAIN scaler stats and need not themselves have mean 0/std 1.
- `len(train_loader)` = number of batches; `train_loader.batch_size` = samples per normal batch.
- Epoch loss bookkeeping: simple current approach averages batch-average losses via `/ len(train_loader)`; final partial-batch weighting is a later refinement.
- Accuracy requires comparing predictions to targets; `predictions.mean()` only measures fraction predicted class 1.
- Keep logit → probability → class distinction automatic.
- Search theory completeness/optimality/time/memory and heuristic properties remain non-automatic.

## Active highest-value sequence

1. **Finish Lesson 31 real-data ML workflow** — the `make_classifier` import bug is now fixed; extend/confirm training/evaluation tests, run train/validation/test evaluation and inspect generalisation.
2. **Search reactivation** — BFS/DFS/A* cold recall; compare them; add UCS/heuristic theory and light logic preview.
3. **Fundamentals Week-3 buffer** — linear/logistic retrieval, then decision trees/random forests.

# PARKED / MUST RETURN

- [~] **BFS / DFS / A\*** — implemented lessons 24–26; reactivation pending.
- [ ] **Logic/reasoning** — Fundamentals Week 1 preview.
- [ ] **Decision trees / random forests** — Fundamentals Week 3.
- [~] **Real-data PyTorch classification** — Lesson 31 active/incomplete.
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
- W1–2: simple ML + vector/matrix/tensor/NumPy → current prep is strong.
- W3: representations + SciPy/matplotlib/PyTorch → PyTorch strong enough; plotting/SciPy not yet systematic.
- W4: MLP/CNN/RNN → MLP ahead; CNN/RNN pending.
- W5: housing-price prediction → regression workflow needs real-data/NN practice.

### ML Theory — January risk lane
- Probability/statistics is the main prerequisite gap.
- GD/backprop mechanics are an advantage, but convergence/generalisation theory is not yet prepared.

## Next session target

> Lesson 31's `make_classifier` import bug is fixed and the full suite is green. Resume by finishing the end-to-end training/evaluation workflow (run the training loop across the real train/val split and inspect held-out test accuracy).

After Lesson 31, **do not sacrifice the search reactivation session** before/around classes.

## End-of-session update

- **Completed:** durable lesson-log reconstruction for Lessons 01–29; all Lessons 01–31 now have retrieval logs. Lesson 31 implementation state audited against repo.
- **Now comfortable with:** durable curriculum can now be recovered lesson-by-lesson rather than relying on chat memory.
- **Still fragile:** Lesson 31 has not been run end-to-end; epoch-loss averaging/accuracy syntax and some reduced-axis shape intuition still deserve retrieval; search theory remains pending.
- **Newly parked / unparked:** no strategy change. Real-data classification remains active; search remains next major reactivation.
- **Next session:** fix Lesson 31 import bug interactively, finish Lesson 31, then search reactivation.
- **Roadmap/syllabus change needed?** roadmap audit wording updated; no strategic course change.
