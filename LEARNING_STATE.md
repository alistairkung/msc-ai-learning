# Learning State — Current Handover

_Last updated: 2026-09-06_

> Update this file at the end of **every study session**. Keep it short. It should answer: **Where am I now, what is fragile, what is parked, and what should happen next?**

## Current phase

- MSc Term 1: **7 Sep–4 Dec 2026**; school starts Monday and the first AIMS5701 Fundamentals class is Wednesday.
- Immediate courses: **Fundamentals in AI (AIMS5701)** and **AI in Practice (AIMS5702)**.
- **Machine Learning Theory (AIMS5704)** starts **11 Jan 2027**; probability/statistics/LA preparation must run during Term 1.
- Strategy: stay roughly **1–2 syllabus weeks ahead** while keeping a small January-maths lane alive.
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
- **2026-09-06 implementation continuation:** BFS was reconstructed incrementally without inspecting the old implementation: `parents={start: None}`, FIFO `deque([start])`, `popleft()`, neighbour discovery, parent recording, enqueueing, goal detection and backwards parent-chain path reconstruction were all recovered with light syntax prompting. DFS was then correctly derived from the same skeleton by changing frontier removal to LIFO `pop()`; the learner also correctly reasoned about neighbour-order reversal.
- A skipped pytest practice exercise now exists for independent BFS implementation before continuing. This is deliberately practice-only and must not block CI.
- UCS implementation is the next genuinely new coding step; A* follows as UCS + heuristic priority.

### Calculus / optimisation / PyTorch
- Power/product rules, partial derivatives, gradients, chain rule and manual backprop understood.
- Autograd/manual GD (28), standard linear training loop (29), synthetic binary MLP (30) and real-data classification workflow (31) implemented.
- Lesson 31 includes stratified train/validation/test splitting, train-only scaling, tensor/DataLoader preparation, MLP training/validation and held-out evaluation; verified tests/dashboard passed on 2026-09-04.

## Fragile under cold recall

- **Linear algebra:** procedural details around RREF/free variables, determinant/eigen arithmetic, Gram–Schmidt/projections, least-squares equations and quadratic-form representation. See `lesson_logs/historical_linear_algebra_*.md`.
- **Probability/statistics:** Bayes conditioning direction/denominator, PDF vs probability, expectation weighting, covariance vs correlation, CLT/sampling-distribution interpretation and p-value language. Markov chains/Poisson are diagnostic-needed. See `lesson_logs/historical_probability_statistics_*.md`.
- **Practical ML/tensors:** `nn.Linear` weight orientation, batch/reduction shapes, train-only scaler semantics, loader length vs batch size, binary accuracy and logit → probability → class distinction.
- **Search:** independent full-code reconstruction still needs evidence; deque syntax needed a small prompt; path reconstruction initially omitted the goal and included `None` before the append-before-parent-lookup pattern was derived. Theory fragilities remain `h(n)` semantics, consistency and guarantee assumptions.

## Active highest-value sequence

1. **BFS independent practice** — implement BFS against the skipped practice test without rereading `lesson24_bfs.py`.
2. **Search implementation continuation** — review the BFS attempt, then implement UCS with accumulated `g` and cheaper-path updates; reconstruct A* as `g+h`.
3. **Search theory consolidation** — after implementation, briefly re-test completeness/optimality/admissibility/consistency and add time/memory complexity if useful for AIMS5701.
4. **Fundamentals Week-3 buffer** — linear/logistic retrieval, then decision trees/random forests.
5. **Probability runway for Weeks 4–5 + January** — short Bayes/random-variable retrieval; diagnose Markov chains/Poisson before HMM/particle-filtering work; then extend toward likelihood/MLE.
6. **January maths maintenance** — retrieve LA/calculus tactically when upcoming material invokes it.

# PARKED / MUST RETURN

- [~] **BFS / DFS / A\*** — BFS guided reconstruction and DFS derivation completed 2026-09-06; independent BFS practice is next, then A* after UCS.
- [~] **UCS** — concept introduced and traced correctly; implementation not yet written.
- [~] **Search guarantees / heuristic theory** — admissibility, consistency, completeness and optimality introduced; consolidate after implementation and attach assumptions carefully.
- [ ] **Logic/reasoning** — Fundamentals Week 1 preview.
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
- W1: introduction, logic, reasoning, learning → logic is the immediate unfamiliar piece.
- W2: uninformed/informed/multi-agent search → theory reactivated; BFS/DFS implementation mechanics now reconstructed with independent practice pending; UCS/A* coding next.
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

> **First, attempt the skipped BFS practice test independently without rereading the old BFS implementation.** Use the test as a specification, not as a timed memory exam. Review any failures to distinguish syntax from conceptual gaps. Then continue forward into UCS implementation (`g`, priority queue, cheaper-path updates) and derive A* as `g+h`.

Do not begin the next session with another broad cold theory retrieval. Continue from today's implementation work.

## End-of-session update

- **Completed:** guided BFS implementation reconstruction and BFS → DFS transformation, following the earlier theory/UCS/heuristics session.
- **Demonstrated:** parent-map-as-seen-state reasoning, FIFO frontier mechanics, neighbour discovery, parent-chain path reconstruction after one correction, DFS as a frontier-policy change, and DFS neighbour-order implications.
- **Still fragile:** independent end-to-end BFS implementation; exact deque syntax; path reconstruction details without scaffolding; UCS/A* implementation remains undone.
- **Next:** independent BFS practice exercise, then continue directly to UCS rather than repeating conceptual retrieval.
