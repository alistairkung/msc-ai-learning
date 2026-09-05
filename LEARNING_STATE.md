# Learning State — Current Handover

_Last updated: 2026-09-05_

> Update this file at the end of **every study session**. Keep it short. It should answer: **Where am I now, what is fragile, what is parked, and what should happen next?**

## Current phase

- MSc Term 1: **7 Sep–4 Dec 2026**.
- Immediate courses: **Fundamentals in AI (AIMS5701)** and **AI in Practice (AIMS5702)**.
- **Machine Learning Theory (AIMS5704)** starts **11 Jan 2027**; probability/statistics/LA preparation must run during Term 1.
- Strategy: stay roughly **1–2 syllabus weeks ahead** while keeping a small January-maths lane alive.
- Lesson-log backfill is complete: **Lessons 01–31 all have retrieval logs**; `lesson_logs/INDEX.md` is the coverage index.
- Historical pre-repo maths is now documented in three durable tracks: calculus, JHU linear algebra, and JHU probability/statistics.

## Verified learning position

### Python / DSA / data
- Core Python containers/functions/comprehensions and DSA patterns practised in lessons 01–09.
- NumPy/Pandas foundations substantial (10–20, 27).
- pytest is comfortable and remains useful as learning scaffolding.

### Linear algebra
- JHU Coursera **Linear Algebra from Elementary to Advanced** was completed in 2025; this is established prior learning, not an unfinished prerequisite.
- Historical retrieval logs preserve: systems/RREF/free variables/span/basis; determinants/eigenvalues/eigenvectors/diagonalization; orthogonality/Gram–Schmidt/projections/least squares; symmetric matrices/orthogonal diagonalization/quadratic forms.
- Current cold retrieval shows the conceptual structure survives, with arithmetic/procedural slips more likely than complete conceptual loss.
- Treat LA as a **maintenance/application lane** during Term 1, not a course to restart.

### Probability / statistics
- Two JHU probability modules were completed in late 2025. The historical core is now reconstructed from multiple prior chats rather than treated as unstudied.
- Strong recoverable evidence covers: counting/sample spaces, probability axioms, conditional probability, independence, total probability, Bayes; random variables, geometric waiting time, expectation/variance, continuous variables, PDF/CDF, Uniform/Exponential/Normal; joint/marginal distributions, linearity of expectation/indicators, covariance/correlation, Markov/Chebyshev inequalities; CLT, sampling distributions, standard error and introductory hypothesis testing/p-values.
- **Evidence boundary:** Markov chains and Poisson are distinctly remembered as studied, but the recoverable worked trail is too weak to claim demonstrated mastery. Treat their next encounter as a cold diagnostic and create fresh evidence.
- Probability/statistics is therefore an **established but higher-priority retrieval/application lane**, not a first-exposure gap. The genuinely new January work is more likely to be likelihood/MLE, exponential families, formal concentration/generalisation and proof-style derivations.

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
- Repo contains `deep_learning/mlp/lesson31_real_data.py`, `deep_learning/mlp/test_lesson31_real_data.py`, and `lesson_logs/lesson31_real_data_workflow.md`.
- Implemented: real sklearn breast-cancer data; stratified 60/20/20 train/validation/test split; train-only `StandardScaler`; NumPy→float32 tensors; labels `(n,) -> (n,1)`; `TensorDataset`/`DataLoader`; `30 -> 16 -> ReLU -> 1` classifier; SGD + `BCEWithLogitsLoss`; train/validation losses; sigmoid/threshold accuracy; final held-out evaluation.
- Verified on 2026-09-04: Lesson 31 plus dashboard tests pass (`9 passed`).
- Optional continuation only: retain and restore the best-validation checkpoint if early stopping/model selection is added later.

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

### Probability/statistics retrieval targets
- Joint probability vs posterior/conditional probability in Bayes; construct the denominator from all evidence-producing routes.
- Geometric `n-1`: reconstruct the preceding failures instead of memorising the exponent.
- PDF density vs point probability; CDF as accumulated probability.
- Expectation/variance as probability-weighted quantities; linearity of expectation does not require independence.
- Joint → marginal distribution via summation/integration over the other variable.
- Covariance vs correlation; zero covariance does not generally imply independence.
- Markov vs Chebyshev inequalities and what information each uses.
- CLT applies to the sampling distribution of the mean, not to raw observations becoming Normal.
- Standard deviation vs standard error; p-value is not the probability that `H0` is true.
- **Diagnostic needed:** Markov chains and Poisson.

### Practical ML / tensor retrieval targets
- `nn.Linear(in, out).weight.shape == (out, in)`; batch dimension occasional quick slips.
- Standardisation: mean ≈ 0, std ≈ 1 on TRAIN; validation/test use TRAIN scaler stats and need not themselves have mean 0/std 1.
- `len(train_loader)` = number of batches; `train_loader.batch_size` = samples per normal batch.
- Accuracy requires comparing predictions to targets; `predictions.mean()` only measures fraction predicted class 1.
- Keep logit → probability → class distinction automatic.
- Search theory completeness/optimality/time/memory and heuristic properties remain non-automatic.

## Active highest-value sequence

1. **Search reactivation** — BFS/DFS/A* cold recall; compare them; add UCS/heuristic theory and light logic preview.
2. **Fundamentals Week-3 buffer** — linear/logistic retrieval, then decision trees/random forests.
3. **Probability runway for Weeks 4–5 + January** — short Bayes/random-variable retrieval first; diagnose Markov chains/Poisson before HMM/particle-filtering work; then extend toward likelihood/MLE as AIMS5704 approaches.
4. **January maths maintenance** — insert short LA/calculus retrieval where upcoming material invokes it.

# PARKED / MUST RETURN

- [~] **BFS / DFS / A\*** — implemented lessons 24–26; reactivation pending.
- [ ] **Logic/reasoning** — Fundamentals Week 1 preview.
- [ ] **Decision trees / random forests** — Fundamentals Week 3.
- [x] **Real-data PyTorch classification** — Lesson 31 complete; best-validation-checkpoint restoration is optional continuation work.
- [~] **Historical linear algebra retrieval** — JHU foundation established and documented; retrieve in short targeted blocks rather than relearn from zero.
- [~] **Historical probability/statistics retrieval** — core JHU foundation established and documented; Bayes/distributions/joint moments/CLT are strong historical evidence; Markov chains and Poisson require diagnostic retrieval before being treated as current.
- [ ] **Likelihood / log-likelihood / MLE** — extend historical probability/statistics for AIMS5704.
- [ ] **NN regression / housing-price workflow** — AI in Practice Week 5.
- [ ] **CNN/RNN architecture preview** — AI in Practice Week 4.
- [ ] **Formal complexity / graph-tree DSA** — reinforce around search.
- [ ] **Vector/Jacobian calculus** — defer until needed.

## Near-term syllabus runway

### Fundamentals
- W1: introduction, logic, reasoning, learning → logic is the immediate unfamiliar piece.
- W2: uninformed/informed/multi-agent search → BFS/DFS/A* already coded; reactivate and deepen.
- W3: linear/logistic regression, decision trees, random forests → first two practised; trees/forests are the gap.
- W4: Bayesian networks/inference/sampling → conditional probability/Bayes foundation is historical established knowledge; reactivate before the week, then learn graphical-model semantics/inference.
- W5: HMMs/particle filtering → probability foundation exists, but Markov-chain recall must be diagnosed rather than assumed.

### AI in Practice
- W1–2: simple ML + vector/matrix/tensor/NumPy → current prep is strong; historical JHU LA means the matrix layer is retrieval/application rather than first exposure.
- W3: representations + SciPy/matplotlib/PyTorch → PyTorch strong enough; plotting/SciPy not yet systematic.
- W4: MLP/CNN/RNN → MLP ahead; CNN/RNN pending.
- W5: housing-price prediction → regression workflow needs real-data/NN practice.

### ML Theory — January risk lane
- Linear algebra and core probability/statistics are both established historical foundations with retrieval due.
- The larger January gaps are **new extensions**: likelihood/log-likelihood/MLE/exponential-family notation, formal risk/generalisation/concentration, convergence assumptions and proof-style derivations.
- Markov chains/Poisson should be diagnostically retrieved because course memory is stronger than recoverable worked evidence.
- GD/backprop mechanics are an advantage.

## Next session target

> **Reactivate search:** cold-retrieve BFS, DFS and A*, compare completeness/optimality/time/memory, then add UCS and heuristic admissibility/consistency.

The historical maths backfill should not displace immediate Week-1/2 MSc preparation. Pull from linear algebra/probability tactically as live course material calls for it.

## End-of-session update

- **Completed:** historical JHU linear-algebra and probability/statistics foundations reconstructed into focused retrieval logs; repository context/dashboard aligned with completed 2025 maths preparation.
- **Now represented accurately:** probability/statistics is established prior learning with retrieval due, not an unstudied prerequisite; evidence strength is explicit by topic.
- **Still fragile:** LA procedural details and probability notation/interpretation under cold recall; Markov chains/Poisson specifically require diagnostics; likelihood/MLE and formal ML Theory material remain genuine future extensions.
- **Immediate priority unchanged:** search reactivation remains first.
