# Learning State — Current Handover

_Last updated: 2026-09-03_  

> Update this file at the end of **every study session**. Keep it short. It should answer: **Where am I now, what is fragile, what is parked, and what should happen next?**

## Current phase

- MSc Term 1: **7 Sep–4 Dec 2026**.
- Immediate courses: **Fundamentals in AI (AIMS5701)** and **AI in Practice (AIMS5702)**.
- **Machine Learning Theory (AIMS5704)** starts **11 Jan 2027**; probability/statistics/LA preparation must run during Term 1.
- Strategy: stay roughly **1–2 syllabus weeks ahead** while keeping a small January-maths lane alive.

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
- Cold retrieval at session start covered PyTorch shapes, logits/sigmoid/BCE, generalisation, train/validation/test roles, overfitting, early stopping and `zero_grad()`.
- Using sklearn breast-cancer dataset as a built-in real-data classification exercise.
- Implemented locally during session:
  - `load_data()` using `load_breast_cancer(return_X_y=True)`; observed X `(569, 30)`, y `(569,)`.
  - `split_data()` with stratified 60/20/20 train/validation/test split by splitting 60/40 then remainder 50/50; shapes train 341, val 114, test 114.
  - `scale_data()` using `StandardScaler`: fit/fit_transform TRAIN only; transform validation/test with frozen train statistics.
  - scaling tests: training feature means ≈ 0 and stds ≈ 1 using `np.allclose(..., atol=1e-7)`.
  - `to_tensors()` converts features/labels to `torch.float32`, reshaping labels `(n,) -> (n,1)`.
  - `make_dataloader()` with `TensorDataset`, shuffled mini-batches; 341 samples / batch 32 gives 11 batches, final batch 21.
  - `make_classifier()` intended architecture `30 -> 16 -> ReLU -> 1`.
  - training-loop structure: epoch loop around batch loop; SGD + BCEWithLogitsLoss; average batch losses per epoch; validation once per epoch under `torch.no_grad()`; store train/val loss histories.
  - `classification_accuracy()` concept: logits -> sigmoid -> threshold -> compare predictions with y -> float mean, under no-grad.
- **Current local blocker at pause:** `test_make_classifier()` is failing even though intended test/model shown in chat are logically compatible:
  - test creates `X = torch.randn(32, 30)`, runs `logits = model(X)`, expects `(32,1)`.
  - model shown: `nn.Sequential(nn.Linear(30,16), nn.ReLU(), nn.Linear(16,1))`.
  - Exact failure traceback/message was NOT captured. Next session should inspect the actual local failure before changing code; likely surrounding/import/file-state issue rather than the shown architecture itself.
- Lesson 31 is **not complete yet** and no lesson31 repo exercise/log was found on GitHub at session end; local work may be uncommitted.

## Fragile under cold recall

- `nn.Linear(in, out).weight.shape == (out, in)`; batch dimension occasional quick slips.
- Standardisation: mean ≈ 0, std ≈ 1; validation/test use TRAIN scaler stats and need not themselves have mean 0/std 1.
- `len(train_loader)` = number of batches; `train_loader.batch_size` = samples per normal batch.
- Epoch loss bookkeeping: sum batch-average losses then divide by number of batches (simple current approach).
- Accuracy requires comparing predictions to targets; `predictions.mean()` only measures fraction predicted class 1.
- Keep logit → probability → class distinction automatic.
- Search theory completeness/optimality/time/memory and heuristic properties remain non-automatic.

## Active highest-value sequence

1. **Finish Lesson 31 real-data ML workflow** — first diagnose failing classifier test, then run training and final train/val/test evaluation; inspect learning/generalisation.
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

> Resume Lesson 31 by getting the **exact traceback from `test_make_classifier()`**. The shown architecture and expected `(32,1)` output agree, so diagnose before editing. Once green, complete training/evaluation and consolidate what the real-data workflow added beyond Lesson 30.

After Lesson 31, **do not sacrifice the search reactivation session** before/around classes.

## End-of-session update

- **Completed:** Lesson 31 data pipeline through load → stratified split → train-only scaling → tensors → DataLoader; classifier/training/evaluation concepts mostly built.
- **Now comfortable with:** train-only preprocessing, leakage rationale, tensor conversion/label reshape, DataLoader batch shapes, train-vs-validation roles, overfitting pattern.
- **Still fragile:** epoch-loss averaging details; accuracy comparison syntax; some NumPy reduced-axis shape intuition; exact local classifier-test failure unresolved.
- **Newly parked / unparked:** Real-data classification is active/incomplete, not parked. Search remains next major reactivation.
- **Next session:** diagnose classifier test, finish Lesson 31, then search reactivation.
- **Roadmap/syllabus change needed?** no — today advanced the existing real-data ML workflow track.