# Learning State — Current Handover

_Last updated: 2026-09-08_

> Update this file at the end of **every study session**. Keep it short. It should answer: **Where am I now, what is fragile, what is parked, and what should happen next?**

## Current phase

- MSc Term 1: **7 Sep–4 Dec 2026**.
- **AIMS5701 Fundamentals start has been delayed by one week**, creating an extra preparation week before live Fundamentals teaching begins.
- Immediate courses: **Fundamentals in AI (AIMS5701)** and **AI in Practice (AIMS5702)**.
- **Machine Learning Theory (AIMS5704)** starts **11 Jan 2027**; probability/statistics/LA preparation must run during Term 1.
- Strategy: stay roughly **1–2 syllabus weeks ahead** while keeping a small January-maths lane alive. Use the extra Fundamentals runway to make search durable rather than merely rush through it.
- Lessons **01–31** all have retrieval logs; historical pre-repo maths is documented separately for calculus, JHU linear algebra and JHU probability/statistics.

## Verified learning position

### Python / DSA / data
- Core Python containers/functions/comprehensions and DSA patterns practised in lessons 01–09.
- NumPy/Pandas foundations substantial (10–20, 27).
- pytest is comfortable and remains useful as learning scaffolding.

### Linear algebra
- JHU Coursera **Linear Algebra from Elementary to Advanced** was completed in 2025; treat this as established prior learning with retrieval due, not a prerequisite to restart.
- Four historical logs preserve the evidenced sequence from systems/vector spaces through eigen/diagonalization, orthogonality/projections/least squares, and symmetric matrices/quadratic forms.
- Current role: **maintenance/application lane**. Use the relevant historical log for detailed fragile points and retrieval prompts.

### Probability / statistics
- Two JHU probability modules were completed in late 2025; the recoverable historical core is established prior learning with retrieval due.
- Strong evidence covers conditional probability/Bayes, random variables/distributions, expectation/variance, joint/marginal distributions, covariance/correlation, Markov/Chebyshev inequalities, CLT, standard error and introductory hypothesis testing/p-values.
- **Evidence boundary:** Markov chains and Poisson are distinctly remembered as studied but lack enough recovered worked evidence to claim current mastery. Diagnose them cold before relying on them.
- Current role: **higher-priority retrieval/application lane**; likelihood/MLE, exponential families and formal generalisation/concentration remain genuine extensions.

### Classical ML
- sklearn logistic regression/classification workflow (21–22) and linear regression (23) implemented.
- Historical least-squares work gives useful geometry underneath regression.
- Linear/logistic regression need consolidation, not first exposure; decision trees/random forests are new.

### Search — reactivation in progress
- BFS, DFS and A* were originally implemented in lessons 24–26.
- **2026-09-06 theory reactivation complete:** BFS/DFS traversal intuition survived; A* `g/h/f` recovered; UCS introduced; admissibility, consistency, completeness and optimality added at course-appropriate introductory depth.
- **2026-09-06 implementation continuation:** BFS was reconstructed incrementally without inspecting the old implementation; DFS was correctly derived from the same skeleton by changing frontier removal to LIFO `pop()` and reasoning about neighbour-order reversal.
- **Independent BFS reconstruction is now complete:** the retained skipped practice test was used successfully without committing the solution. Future BFS reconstruction should be periodic maintenance, not an immediate repeat.
- UCS implementation is the next genuinely new coding step; A* follows as UCS + heuristic priority.
- AIMS5701 Week 2 also includes **“searching with other agents”**, which remains genuinely new. Plan a dedicated adversarial/multi-agent search block after closing UCS/A*; confirm the course framing from lecture materials when available rather than assuming more detail than the syllabus title supports.

### Calculus / optimisation / PyTorch
- Power/product rules, partial derivatives, gradients, chain rule and manual backprop understood.
- Autograd/manual GD (28), standard linear training loop (29), synthetic binary MLP (30) and real-data classification workflow (31) implemented.
- Lesson 31 includes stratified train/validation/test splitting, train-only scaling, tensor/DataLoader preparation, MLP training/validation and held-out evaluation; verified tests/dashboard passed on 2026-09-04.

## Fragile under cold recall

- **Linear algebra:** procedural details around RREF/free variables, determinant/eigen arithmetic, Gram–Schmidt/projections, least-squares equations and quadratic-form representation. See `lesson_logs/historical_linear_algebra_*.md`.
- **Probability/statistics:** Bayes conditioning direction/denominator, PDF vs probability, expectation weighting, covariance vs correlation, CLT/sampling-distribution interpretation and p-value language. Markov chains/Poisson are diagnostic-needed. See `lesson_logs/historical_probability_statistics_*.md`.
- **Practical ML/tensors:** `nn.Linear` weight orientation, batch/reduction shapes, train-only scaler semantics, loader length vs batch size, binary accuracy and logit → probability → class distinction.
- **Search:** keep variable roles explicit during path reconstruction; keep graph adjacency separate from discovered-state membership; UCS/A* implementation remains to be demonstrated; theory fragilities remain `h(n)` semantics, consistency and guarantee assumptions.

## Active highest-value sequence

1. **UCS implementation** — weighted neighbours, priority queue, accumulated `g`, `cost_so_far`, cheaper-path updates and path reconstruction.
2. **A* reconstruction** — derive directly from UCS by adding heuristic priority `g+h` rather than rereading the old implementation.
3. **Search theory consolidation** — short re-test of completeness/optimality/admissibility/consistency plus time/space complexity and assumptions where useful.
4. **Searching with other agents** — dedicated new-material block before the delayed Week-2 lecture. If the course means standard adversarial search, build game-tree intuition → minimax → alpha-beta pruning; use actual course materials to confirm scope when available.
5. **Integrated pre-lecture search review** — choose/trace algorithms across unweighted, weighted, heuristic and multi-agent scenarios; do not repeat full BFS drilling.
6. **Then use remaining buffer** for Week-1 logic/reasoning and the Week-3 decision-tree/random-forest gap.
7. **Probability runway for Weeks 4–5 + January** — short Bayes/random-variable retrieval; diagnose Markov chains/Poisson before HMM/particle-filtering work; then extend toward likelihood/MLE.

# PARKED / MUST RETURN

- [~] **BFS / DFS / A\*** — BFS independent reconstruction complete; DFS mechanics derived; A* reconstruction follows UCS.
- [~] **UCS** — concept introduced and traced correctly; implementation is next.
- [~] **Search guarantees / heuristic theory** — admissibility, consistency, completeness and optimality introduced; consolidate after implementation and attach assumptions carefully.
- [ ] **Searching with other agents** — AIMS5701 Week 2; genuinely new. Confirm exact lecture scope, likely adversarial/game-tree search if course materials support that interpretation.
- [ ] **Logic/reasoning** — Fundamentals Week 1 preview; extra start-delay runway means this can follow the core search implementation work without being rushed.
- [ ] **Decision trees / random forests** — Fundamentals Week 3.
- [x] **Real-data PyTorch classification** — Lesson 31 complete; best-validation-checkpoint restoration is optional continuation work.
- [~] **Historical linear algebra retrieval** — established and documented; retrieve in short targeted blocks rather than relearn from zero.
- [~] **Historical probability/statistics retrieval** — core foundation established; Markov chains and Poisson require diagnostics before being treated as current.
- [ ] **Likelihood / log-likelihood / MLE** — extend historical probability/statistics for AIMS5704.
- [ ] **NN regression / housing-price workflow** — AI in Practice Week 5.
- [ ] **CNN/RNN architecture preview** — AI in Practice Week 4.
- [ ] **Formal complexity / graph-tree DSA** — reinforce around search.
- [ ] **Vector/Jacobian calculus** — defer until needed.

## Near-term syllabus runway

### Fundamentals
- **Start delayed by one week:** use the added runway to close single-agent search implementation/theory and begin the untouched “searching with other agents” branch before it appears live.
- W1: introduction, logic, reasoning, learning → logic remains unfamiliar; preview after the immediate UCS/A* implementation block rather than displacing it.
- W2: uninformed/informed/searching with other agents → BFS/DFS reactivated; UCS/A* implementation next; guarantees/complexity consolidation after; multi-agent/adversarial branch still new.
- W3: linear/logistic regression, decision trees, random forests → first two practised; trees/forests are the gap.
- W4: Bayesian networks/inference/sampling → historical Bayes/probability foundation exists; reactivate, then learn graphical-model semantics/inference.
- W5: HMMs/particle filtering → diagnose Markov-chain recall before relying on it.

### AI in Practice
- W1–2: simple ML + vector/matrix/tensor/NumPy → strong preparation; historical JHU LA makes the matrix layer retrieval/application rather than first exposure.
- W3: representations + SciPy/matplotlib/PyTorch → PyTorch base strong; plotting/SciPy not systematic.
- W4: MLP/CNN/RNN → MLP ahead; CNN/RNN pending.
- W5: housing-price prediction → transfer Lesson 31's preprocessing/validation discipline to regression.

### ML Theory — January risk lane
- Linear algebra and core probability/statistics are established historical foundations with retrieval due.
- Larger new gaps: likelihood/log-likelihood/MLE/exponential-family notation, formal risk/generalisation/concentration, convergence assumptions and proof-style derivations.
- GD/backprop mechanics are an advantage.

## Next session target

> **Continue directly into UCS implementation.** Do not repeat the BFS practice or restart broad theory retrieval. Build weighted neighbours, priority frontier, accumulated `g` and cheaper-path updates incrementally; then derive A* as `g+h`.

After UCS/A*, consolidate guarantees/complexity briefly, then use the extra Fundamentals week to cover the Week-2 “searching with other agents” branch before the lecture. Use course materials to confirm its exact scope when they become available.

## End-of-session update

- **Timing change:** AIMS5701 Fundamentals has been delayed by one week, giving an extra preparation week.
- **Plan change:** use the extra runway to make search durable: UCS → A* → guarantees/complexity → searching with other agents → integrated review.
- **State correction:** independent BFS reconstruction has already succeeded; do not schedule it again immediately.
- **Immediate next:** UCS implementation, then A* reconstruction.
