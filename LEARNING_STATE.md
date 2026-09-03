# Learning State — Current Handover

_Last updated: 2026-09-03_  
_Repo audit completed against `alistairkung/msc-ai-learning` main on 2026-09-03_

> Update this file at the end of **every study session**. Keep it short. It should answer: **Where am I now, what is fragile, what is parked, and what should happen next?**

## Current phase

- MSc Term 1: **7 Sep–4 Dec 2026**.
- Immediate courses to prepare around: **Fundamentals in AI (AIMS5701)** and **AI in Practice (AIMS5702)**.
- **Machine Learning Theory (AIMS5704)** starts **11 Jan 2027**; probability/statistics/LA preparation must run during Term 1.
- Strategy: stay roughly **1–2 syllabus weeks ahead** while keeping a small January-maths lane alive.

## Verified learning position

### Python / DSA / data
- Core Python containers, functions, comprehensions, sorting/lambdas: practised in repo lessons 01–07.
- DSA: hash/set lookup, two-sum, two pointers, anagrams, fixed + variable sliding window (08–09).
- NumPy: shapes, indexing, masks, vectorisation, axes, broadcasting, standardisation, reshape/transpose, linear layers and repeated retrieval (10–17, 27).
- Pandas: selection/filtering, `loc`/`iloc`, derived columns, missing data, sorting, groupby/aggregation, merges (18–20).
- pytest is comfortable and remains useful as learning scaffolding.

### Classical ML
- sklearn logistic regression + train/test split, stratification, thresholding, confusion matrix, accuracy/precision/recall (21–22).
- sklearn linear regression + MAE/MSE/R² (23).
- Linear/logistic regression therefore need **consolidation**, not first exposure.
- Decision trees/random forests are still new.

### Search
- **BFS implemented** with FIFO `deque`, seen set, parent map/path reconstruction (24).
- **DFS implemented** with LIFO `pop`, seen set, parent map/path reconstruction (25).
- **A\* implemented** with `heapq`, `cost_so_far`, parent map, and priority `g+h` (26).
- Search was deliberately parked after implementation. It now needs **cold retrieval + comparison/theory**, not a restart from zero.

### Calculus / optimisation
- Power/product rules, partial derivatives, gradients, chain rule and manual backprop are understood.
- PyTorch autograd/manual GD/manual linear training implemented (28).
- Standard `nn.Linear` + MSE + SGD loop implemented (29).

### Neural networks / PyTorch
- ReLU/nonlinearity, MLP shape flow, logits/sigmoid/BCE understood.
- Binary MLP with `BCEWithLogitsLoss`, `TensorDataset`, `DataLoader`, mini-batches/epochs, SGD and accuracy implemented (30).
- Synthetic classifier successfully learned the toy rule; current evaluation was on training data, so **generalisation has not yet been demonstrated**.

## Fragile under cold recall

- `nn.Linear(in, out).weight.shape == (out, in)`.
- Preserve the batch dimension while tracing network shapes.
- Parameter `.grad` has the same shape as the parameter.
- Chain-rule derivative direction (`df/du`, `du/dx`).
- Keep constant factors in partial derivatives and exponents during substitution.
- Algebra can fail even when calculus reasoning is right.
- Distinguish logit → probability → class.
- Distinguish samples, batch size, batches/epoch, epochs and total updates.
- Search theory: completeness/optimality/time/memory and heuristic properties are not yet automatic.

## Active highest-value sequence

Because only a few prep sessions may remain before classes, prioritise **syllabus lead**, not breadth:

1. **Real-data ML workflow** — consolidate the practical thread already in motion.
2. **Search reactivation** — BFS/DFS/A* from cold recall; compare them; add UCS/heuristic theory and light logic preview.
3. **Fundamentals Week-3 buffer** — linear/logistic retrieval, then decision trees/random forests.

Once term starts, use the rolling 1–2 week syllabus buffer.

# PARKED / MUST RETURN

Do not remove an item until it is explicitly completed or moved to a dated plan.

- [~] **BFS / DFS / A\*** — implemented in repo lessons 24–26; **reactivation pending**. Need cold reconstruction, algorithm comparison, UCS and A* heuristic properties.
- [ ] **Logic/reasoning** — Fundamentals Week 1 preview.
- [ ] **Decision trees / random forests** — Fundamentals Week 3.
- [ ] **Real-data PyTorch classification** — split/scaling/DataLoader/train+val evaluation.
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
- GD/backprop mechanics are an advantage, but **convergence/generalisation theory is not yet prepared**.

## Next session target

If today remains the planned ML session:

> Take one real dataset from inspection → split → preprocessing → loaders/model → training → validation/evaluation, keeping pytest for implementation contracts.

If a session is lost before classes, **do not sacrifice the search reactivation session**; Fundamentals search is the most time-sensitive parked thread.

## End-of-session update

Update only these fields unless strategy genuinely changed:

- **Completed:**
- **Now comfortable with:**
- **Still fragile:**
- **Newly parked / unparked:**
- **Next session:**
- **Roadmap/syllabus change needed?** yes/no
