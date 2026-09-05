# MSc AI Learning Roadmap

_Last reviewed: 2026-09-05_
_Verified against the current learning record, Lesson 31 implementation/tests, and reconstructed historical JHU linear-algebra foundation_

## Purpose

This is the **slow-changing master plan**. It answers:

> **Given what I know today, what the MSc is about to demand, and my longer-term goal of becoming strong in AI/ML engineering, what is the highest-value thing to work on next?**

The aim is not to pre-learn the whole MSc. The aim is to:

- stay roughly **1–2 weeks ahead** of live course content where practical;
- build prerequisites before they become blockers;
- keep maths attached to models and code;
- preserve deliberately parked threads so they cannot disappear;
- maintain a **Term-1 maths lane** so Machine Learning Theory in January is not a sudden jump.

## Learner profile / learning rules

- Experienced software engineer: strong debugging, systems reasoning, decomposition and code-reading skills.
- Python is now usable for ML work, but not yet as automatic as long-used backend languages.
- Formal maths is the higher-risk lane, especially probability/statistics and proof-style derivations.
- Best learning pattern: **small interactive steps → retrieval → concrete example → derive by hand → implement → inspect/debug**.
- Prefer hints/scaffolding over complete solutions.
- `pytest` remains a useful scaffold because it gives a concrete definition of “this implementation works”.
- Library API recall is secondary to conceptual recall. PyTorch syntax may be looked up; the computation underneath should be explainable.
- Shapes should always be interpreted semantically: e.g. `(32, 10)` = **32 samples represented by 10 features**.
- Historical calculus work predates the numbered repo workflow and is preserved separately in `lesson_logs/historical_calculus_foundations.md`.
- Historical JHU linear algebra also predates the numbered workflow and is preserved as four focused retrieval blueprints plus `foundations/linear_algebra/README.md`.
- Lesson-log backfill is complete through Lesson 31; `lesson_logs/INDEX.md` is the coverage index for numbered and historical records.

---

# Verified learning history

The numbered repository lessons give us a reliable spine for what has actually been implemented. Important pre-repo learning is recorded separately rather than assigned invented lesson numbers. Lesson 31 now provides a completed end-to-end real-data classification workflow.

| Learning record | What was practised | Status |
|---|---|---|
| Historical calculus foundations | Slope/local rate, intuitive limits and difference quotient, power/product rules, partial derivatives, gradients, gradient descent, chain rule and manual backprop | **Established conceptually; retrieval-worthy; bridges into Lesson 28** |
| Historical JHU linear algebra | Linear systems/RREF/free variables; span/independence/basis; matrix algebra/determinants; eigenvalues/eigenvectors/diagonalization; orthogonality/Gram–Schmidt/projections/least squares; symmetric matrices/orthogonal diagonalization/quadratic forms | **Established through 2025 JHU specialization; retrieval due after long gap; now documented** |
| 01–07 | Lists, dictionaries, sets, strings, comprehensions, key/lambda functions, function arguments | Established |
| 08 | Hash/set patterns, duplicate detection, two-sum, anagrams, two pointers, in-place reversal | Established; retrieve periodically |
| 09 | Fixed + variable sliding window | Established once; not yet broad DSA fluency |
| 10–17 | NumPy shapes/indexing/masks/axes, vectorisation, broadcasting, standardisation, linear layers, MSE, classification scores/argmax, repeated cold retrieval | Strong practical foundation; shape recall still fragile in places |
| 18–20 | Pandas selection, filtering, `loc`/`iloc`, derived columns, missing values, sorting, `groupby`/`agg`, merge, challenge/refresher | Established |
| 21–22 | sklearn logistic regression, train/test split, stratification, probabilities/thresholds, confusion matrix, accuracy/precision/recall | Established practical intro |
| 23 | sklearn linear regression, train/test split, MAE/MSE/R² | Established practical intro |
| 24–26 | **BFS, DFS and A\*** with path reconstruction; deque/stack behaviour; heap frontier; A* cost + heuristic | **Implemented, then deliberately parked for reactivation** |
| 27 | Tensor batch means, centring, flattening, transpose, linear layer | Established; keep shape retrieval active |
| 28 | PyTorch autograd, scalar/multivariable gradients, manual GD, single-weight training, manual linear-model training | Strong conceptual milestone; executable continuation of historical calculus work |
| 29 | `nn.Linear` + `MSELoss` + SGD training loop | Established |
| 30 | MLP binary classifier, ReLU, `BCEWithLogitsLoss`, `TensorDataset`, `DataLoader`, mini-batches/epochs, sigmoid/threshold accuracy | Established on synthetic data |
| 31 | Real-data classification: stratified train/val/test split, train-only scaling, tensor conversion, DataLoader, train/validation histories, held-out evaluation discipline | **Complete; end-to-end preparation/training/evaluation integration tested** |

All numbered Lessons **01–31 have a lesson log**. Historical calculus and linear algebra are intentionally indexed outside that numbering because they were learned through interactive chat and pen-and-paper before the repository workflow existed. Reconstructed logs use recoverable tutoring context conservatively; they are retrieval blueprints, not invented transcripts.

This table is an **audit anchor**, not a lesson log. Details belong in code/tests and `lesson_logs/`; this roadmap tracks dependencies and direction.

---

# Major learning tracks

## Track A — Python, data tooling and algorithmic fluency

### Why
Python should consume as little working memory as possible while learning AI. DSA is also directly useful for Fundamentals search and general algorithmic reasoning.

### Current position
**Green/Amber.** Core Python, NumPy and Pandas are no longer blockers. DSA already practised includes hash/set lookup, two-sum, two pointers, fixed/variable sliding windows, BFS/DFS graph traversal and priority-queue use inside A*.

### Still to build
- complexity reasoning that is explicit rather than intuitive;
- recursion/tree fluency;
- systematic graph/search trade-offs;
- reading unfamiliar scientific-Python code efficiently;
- plotting/SciPy when AI in Practice Week 3 approaches.

### Unlocks
Search → classical AI; data pipelines → AI in Practice; implementation fluency across the MSc.

---

## Track B — Linear algebra, NumPy and tensor/shape intuition

### Current position
**Historical theory established; practical matrix/tensor use Green/Amber; deliberate retrieval due.** The JHU Coursera linear-algebra specialization was completed in 2025, covering the durable chain from systems/vector spaces through eigen/diagonalization, orthogonality/projection/least squares, symmetric matrices and quadratic forms. That work is now preserved under `lesson_logs/historical_linear_algebra_*.md` and `foundations/linear_algebra/README.md`.

The later repository implementation adds repeated practical use: indexing/slicing, masks and axis reductions; feature centring/standardisation; reshape/transpose; matrix multiplication and linear layers; classification scores; batch and hidden-feature semantics.

Lesson 31 adds a useful real-data shape bridge: sklearn arrays `(samples, features)` → train/val/test splits → scaled NumPy arrays → float32 PyTorch tensors → `(batch, features)` DataLoader batches.

The current goal is **retrieval and application, not restarting linear algebra from zero**.

### Strong conceptual anchors
- systems and RREF expose pivots, free variables and solution-set structure;
- basis = independent spanning set;
- eigenvectors are directions preserved up to scale by a transformation;
- diagonalization expresses a transformation in an eigenbasis;
- orthogonal projection finds the closest point in a subspace;
- Gram–Schmidt replaces a spanning set with orthogonal directions spanning the same space;
- least squares projects `b` onto `Col(A)` and gives `A^T A x = A^T b`;
- symmetric matrices admit orthogonal diagonalization `A = Q D Q^T`;
- quadratic forms `x^T A x` connect symmetric-matrix structure to scalar geometry.

### Fragile points
- echelon form versus true RREF; identifying/parameterising free variables;
- determinant/characteristic-polynomial sign arithmetic;
- remembering that scaled/sign-flipped eigenvectors are equivalent, while `P`/`D` ordering must stay matched;
- Gram–Schmidt requires subtracting the projection, not merely computing it;
- scaling an orthogonal basis vector is fine, but scaling an exact residual breaks `y = y* + z` even though perpendicular direction is preserved;
- diagonalization and least squares can cross-wire under cold recall because both involve matrix algebra but solve different problems;
- PyTorch stores `nn.Linear(in, out).weight` as `(out, in)`; manual `X @ W` intuition often uses `(in, out)`;
- occasionally losing the batch dimension when predicting output shapes;
- NumPy reductions such as `(341,30).mean(axis=0)` return `(30,)` by default, not `(1,30)`;
- deeper shape tracing must stay semantic, not rote.

### Term-1 retrieval / extensions before ML Theory
1. Periodically cold-retrieve the historical logs in small chunks rather than replaying the full JHU course.
2. Keep vectors/matrices, common norms and notation automatic enough for AIMS5702/AIMS5704.
3. Revisit projections/least squares when regression invokes them.
4. Revisit eigen/symmetric/quadratic-form ideas when covariance, PCA, curvature or optimisation invokes them.
5. Add/strengthen positive definite/semidefinite reasoning and Gram-matrix/kernel applications when AIMS5704 needs them.
6. Jacobian/vector-calculus extensions only when useful.

---

## Track C — Calculus → gradients → backprop → optimisation

### Current position
**Conceptually Green/Amber and now historically documented.** The pre-repo chat/pen-and-paper sequence built the chain from slope and local rate of change through intuitive limits/difference quotients, power/product rules, partial derivatives, gradients, gradient descent, chain rule and manual backpropagation.

That sequence is now preserved in `lesson_logs/historical_calculus_foundations.md`, including a cold-retrieval blueprint and known fragile points. It should be treated as genuine historical learning evidence, but not as a fabricated numbered code lesson.

Lesson 28 is the executable continuation: it connects those manual derivatives and chain-rule ideas to `requires_grad`, `.backward()`, `.grad`, no-grad parameter updates and gradient clearing. Lesson 29 then abstracts the mechanics into the standard PyTorch `nn.Linear`/MSE/SGD loop.

### Strong conceptual anchors
- derivative = local slope / local rate of change;
- gradient = vector of local sensitivities;
- gradient-descent update moves opposite local increase;
- chain rule combines local sensitivities along a dependency path;
- backpropagation repeatedly applies that chain rule through a computation graph;
- `.backward()` automates the gradient propagation already understood manually.

### Fragile points
- derivative direction notation such as `dL/dw` versus its inverse;
- preserving constants and powers during differentiation/substitution;
- algebraic expansion/simplification can be shakier than the underlying calculus reasoning;
- chain-rule fluency should be maintained by short retrieval, not restarted from zero.

### Next maths
1. Periodically cold-retrieve the historical calculus foundations, especially derivative meaning → partials → gradient → chain rule → backprop.
2. Logs/exponentials + derivatives.
3. Probability/statistics becomes the main maths priority during Term 1.
4. Later: vector/Jacobian intuition and convexity/smoothness/convergence when ML Theory needs them.

---

## Track D — Classical AI: logic, search and agents

### Current position
**Search implementation exists; conceptual reactivation is urgent.** Repo 24–26 verifies BFS, DFS and A* implementations; dedicated lesson logs preserve each algorithm's frontier/data-structure logic and explicitly flag the missing theory layer.

### What remains before Fundamentals Week 2
- cold-recall implementations rather than relearn from zero;
- compare BFS vs DFS vs uniform-cost vs A*;
- completeness, optimality, time/memory intuition;
- branching factor/depth intuition;
- A* heuristic meaning, admissibility and consistency;
- state/action/goal/path-cost vocabulary;
- multi-agent search preview once lecture framing is known.

### Logic/reasoning
Still largely **unstarted**. Preview Week-1 vocabulary before/around the first Fundamentals lecture, then use lecture notes to decide depth.

---

## Track E — Classical machine learning

### Current position
**Linear regression — Green/Amber.** Manual linear mechanics plus sklearn regression and MAE/MSE/R². Historical JHU least-squares work provides the projection/normal-equation geometry underneath the model.

**Logistic/binary classification — Green/Amber.** sklearn logistic workflow plus neural-network view of logit → sigmoid → BCE. Lesson 22 introduced probability thresholding; Lesson 31 completes the move into proper train/validation/test evaluation and leakage-safe preprocessing.

### Immediate gap: Fundamentals Week 3
- **Decision trees — Red**: splits, impurity, leaves, depth, overfitting.
- **Random forests — Red**: bootstrap/bagging, feature subsampling, voting/averaging, variance reduction.

### Later gaps
Bayesian networks/inference/sampling; HMMs/particle filters; KNN/K-means/SVM/gradient boosting; RL/recommendation/generative models.

---

## Track F — Practical deep learning / PyTorch

### Current position
**MLP mechanics Green/Amber; real-data workflow established.** Verified progression through lessons 27–31: tensor operations, autograd, manual GD, `nn.Linear`, SGD, ReLU, MLP, logits/sigmoid/BCE, DataLoader and real-data evaluation.

### Lesson 31 progress
Repo implementation currently contains:
- real sklearn breast-cancer dataset loading;
- stratified 60/20/20 train/validation/test split;
- `StandardScaler` fitted on **training only** to avoid leakage;
- validation/test transformed with frozen training statistics;
- standardisation behaviour tested (`mean≈0`, `std≈1` on train);
- NumPy arrays converted to float32 tensors; labels reshaped `(n,) -> (n,1)`;
- TensorDataset/DataLoader helper;
- `30 -> 16 -> ReLU -> 1` classifier;
- epoch/batch training loop with train + validation losses;
- binary accuracy via sigmoid/threshold/target comparison;
- held-out test evaluation connected in the executable experiment.

### Completion and optional continuation
The classifier import now uses Lesson 31's intended 30-input model. `prepare_data()` composes the full data pipeline, while `run_experiment()` trains, records train/validation histories and performs final held-out evaluation. Lesson 31 and dashboard validation pass (`9 passed` on 2026-09-04).

Best-validation-checkpoint restoration is an optional extension for future early stopping/model-selection work, not a blocker. The primary next session is search reactivation.

### After Lesson 31
- convert the workflow to **NN regression / housing-price prediction** before AI in Practice Week 5;
- CNN/RNN overview before Week 4;
- deeper CNN before Fashion-MNIST;
- later DataLoader optimisation, distributed training, text analysis and deployment.

---

## Track G — Probability, statistics and January ML Theory readiness

### Current position
**Amber/Red because it has not had recent deliberate practice.** The repo still has no dedicated probability/statistics sequence.

Linear algebra is a different situation: it was completed formally through the JHU specialization and is now a **retrieval/application lane**, not an unlearned prerequisite.

### Term-1 maths lane
**Sep–Oct:** conditional probability/Bayes; random variables; expectation/variance/covariance; common distributions; short historical LA/norm retrieval; logs/exponentials.

**Oct–Nov:** likelihood/log-likelihood; MLE; estimators/sampling; convexity + GD/SGD convergence intuition; reactivate quadratic-form/positive-definite ideas when useful.

**Nov–Dec:** empirical vs population risk; concentration intuition; VC/capacity; kernels/Gram matrices; short proof/derivation reading.

### January destination
Enter ML Theory able to follow definitions and short derivations rather than learning prerequisite notation during lectures.

---

# Dependency map

```text
Python / NumPy / Pandas
   ├──> data workflows ──> sklearn / PyTorch practice
   └──> DSA ──> BFS/DFS/A* ──> multi-agent search

Historical linear algebra
   └──> systems/basis + matrix algebra
          ├──> eigen/symmetric/quadratic forms ──> covariance / optimisation / ML Theory
          └──> orthogonality/projection/least squares ──> regression / Gram matrices / kernels

Linear algebra + practical shape reasoning
   ├──> linear/logistic models
   ├──> MLP ──> CNN/RNN
   └──> kernels / ML Theory

Historical calculus foundations
   └──> derivative/local sensitivity ──> partials/gradients ──> chain rule
          └──> manual backprop ──> Lesson 28 autograd ──> SGD/Adam

Probability/statistics
   ├──> Bayes/inference ──> HMM/particle filters
   ├──> likelihood/MLE ──> exponential families
   ├──> generalisation theory
   └──> bandits / diffusion theory

Evaluation discipline
   └──> train/val/test + leakage-safe preprocessing + metrics + generalisation
          └──> reliable AI/ML engineering
```

---

# Priority policy

Choose the next study topic by asking, in order:

1. Is it required in the **next 1–2 MSc weeks**?
2. Is it a prerequisite that unlocks several later topics?
3. Is it fragile under cold recall?
4. Can one exercise connect theory + implementation + syllabus?
5. Does it preserve January ML-Theory readiness without derailing Term 1?

---

# PARKED / MUST RETURN

- **BFS / DFS / A\*** — **implemented in lessons 24–26**, deliberately parked; reactivate for Fundamentals Week 2. Add UCS + trade-off/heuristic theory rather than rewriting from scratch.
- **Logic/reasoning** — Week 1 Fundamentals; not yet properly studied.
- **Decision trees / random forests** — Week 3 Fundamentals; not present in repo yet.
- **Real-data PyTorch workflow** — **Lesson 31 complete**; best-validation-checkpoint restoration remains optional continuation work.
- **Historical calculus retrieval** — foundation is established and documented; periodically cold-retrieve rather than reteach. Extend with logs/exponentials and vector/Jacobian calculus only when upcoming ML work needs them.
- **Historical linear algebra retrieval** — JHU foundation is established and now documented across four focused logs; use short cold retrieval before relevant MSc topics rather than replaying the course. Strengthen norms, positive definite/semidefinite and Gram-matrix/kernel applications as ML Theory approaches.
- **NN regression / housing-price workflow** — needed before AI in Practice Week 5.
- **CNN/RNN preview** — needed before AI in Practice Week 4.
- **Probability/statistics refresh** — mandatory parallel Term-1 lane for ML Theory Jan 11.
- **Formal complexity + graph/tree DSA** — search works in code, but theory/complexity is not yet systematic.
