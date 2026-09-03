# MSc AI Learning Roadmap

_Last reviewed: 2026-09-03_  
_Verified against `alistairkung/msc-ai-learning` (main) on 2026-09-03_

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

---

# Verified exercise history

The repository now gives us a reliable spine for what has actually been implemented.

| Repo lessons | What was practised | Status |
|---|---|---|
| 01–07 | Lists, dictionaries, sets, strings, comprehensions, key/lambda functions, function arguments | Established |
| 08 | Hash/set patterns, duplicate detection, two-sum, anagrams, two pointers, in-place reversal | Established; retrieve periodically |
| 09 | Fixed + variable sliding window | Established once; not yet broad DSA fluency |
| 10–17 | NumPy shapes/indexing/masks/axes, vectorisation, broadcasting, standardisation, linear layers, MSE, classification scores/argmax, repeated cold retrieval | Strong practical foundation; shape recall still fragile in places |
| 18–20 | Pandas selection, filtering, `loc`/`iloc`, derived columns, missing values, sorting, `groupby`/`agg`, merge, challenge/refresher | Established |
| 21–22 | sklearn logistic regression, train/test split, stratification, probabilities/thresholds, confusion matrix, accuracy/precision/recall | Established practical intro |
| 23 | sklearn linear regression, train/test split, MAE/MSE/R² | Established practical intro |
| 24–26 | **BFS, DFS and A\*** with path reconstruction; deque/stack behaviour; heap frontier; A* cost + heuristic | **Implemented, then deliberately parked for reactivation** |
| 27 | Tensor batch means, centring, flattening, transpose, linear layer | Established; keep shape retrieval active |
| 28 | PyTorch autograd, scalar/multivariable gradients, manual GD, single-weight training, manual linear-model training | Strong conceptual milestone |
| 29 | `nn.Linear` + `MSELoss` + SGD training loop | Established |
| 30 | MLP binary classifier, ReLU, `BCEWithLogitsLoss`, `TensorDataset`, `DataLoader`, mini-batches/epochs, sigmoid/threshold accuracy | Established on synthetic data; real-data workflow next |

This table is an **audit anchor**, not a lesson log. Details belong in code/tests; this roadmap tracks dependencies and direction.

---

# Major learning tracks

## Track A — Python, data tooling and algorithmic fluency

### Why
Python should consume as little working memory as possible while learning AI. DSA is also directly useful for Fundamentals search and general algorithmic reasoning.

### Current position
**Green/Amber.** Core Python, NumPy and Pandas are no longer blockers. Repo evidence includes substantial vectorised NumPy work, dataframe manipulation and repeated retrieval exercises.

DSA already practised:
- hash/set lookup patterns;
- two-sum;
- two pointers;
- fixed/variable sliding windows;
- BFS/DFS graph traversal;
- priority queue/heap use inside A*.

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

### Why
Shapes/matrix operations are the common language of AI in Practice, neural networks and later kernel/optimisation theory.

### Current position
**Green/Amber.** Implemented and repeatedly retrieved:
- indexing/slicing, boolean masks and axis reductions;
- feature centring/standardisation via broadcasting;
- reshape/flatten/transpose;
- matrix multiplication and linear layers;
- classification score matrices and `argmax`;
- batch semantics and hidden-feature semantics.

### Fragile points
- PyTorch stores `nn.Linear(in, out).weight` as **`(out, in)`**; manual `X @ W` intuition often uses `(in, out)`.
- occasionally losing the batch dimension when predicting output shapes;
- parameter gradient tensor has **the same shape as its parameter**;
- deeper shape tracing must stay semantic, not rote.

### Later extensions before ML Theory
- vector/matrix norms;
- quadratic forms and projections as needed;
- kernel feature maps / Gram matrices;
- Jacobian/vector-calculus view only when useful.

---

## Track C — Calculus → gradients → backprop → optimisation

### Why
This is the maths behind neural-network training and later ML Theory convergence work.

### Current position
**Conceptually Green/Amber.** We have covered:
- slope/local rate of change;
- power and product rules;
- partial derivatives;
- gradients as local sensitivities;
- gradient-descent update;
- chain rule through nested functions;
- manual backprop through computation graphs;
- autograd and manual/optimizer-based parameter updates.

Repo lesson 28 verifies scalar/multivariable autograd, manual gradient descent and hand-built linear training; lesson 29 transitions this to standard PyTorch SGD.

### Fragile points
- derivative direction notation (`dz/dw` vs `dw/dz`);
- preserving constant factors in partial derivatives;
- preserving powers during substitution;
- algebraic expansion is rustier than the calculus idea;
- chain-rule fluency should be maintained by short cold retrieval, not by repeatedly restarting calculus.

### Next maths
1. Keep derivatives/partials/chain rule alive with brief retrieval.
2. Logs/exponentials + derivatives.
3. Probability/statistics becomes the main maths priority during Term 1.
4. Later: convexity/smoothness/convergence intuition for ML Theory.

---

## Track D — Classical AI: logic, search and agents

### Why
Fundamentals starts with logic/reasoning and immediately moves into uninformed/informed/multi-agent search.

### Current position
**Search implementation exists; conceptual reactivation is urgent.**

Verified in repo:
- `lesson24_bfs.py`: BFS with `deque.popleft()`, `seen`, parent map and path reconstruction;
- `lesson25_dfs.py`: DFS with LIFO `pop()`, same explored/parent machinery;
- `lesson26_astar.py`: `heapq` frontier, `cost_so_far`, parent map, and priority `g + h`.

### What remains before Fundamentals Week 2
- cold-recall the implementations rather than relearn from zero;
- explicitly compare BFS vs DFS vs uniform-cost vs A*;
- completeness, optimality, time/memory intuition;
- branching factor/depth intuition;
- A* heuristic meaning, admissibility and consistency at course-appropriate depth;
- state/action/goal/path-cost vocabulary;
- multi-agent search preview once lecture framing is known.

### Logic/reasoning
Still largely **unstarted**. Preview Week-1 vocabulary before/around the first Fundamentals lecture, then use lecture notes to decide how deep to go.

---

## Track E — Classical machine learning

### Why
Fundamentals compresses a broad classical-ML survey into Weeks 3–6. We want recognition and working intuition before each lecture.

### Current position
Higher than previously recorded:

**Linear regression — Green/Amber**
- manual `X @ W + b` and MSE work;
- sklearn `LinearRegression` pipeline;
- train/test split;
- MAE, MSE and R².

**Logistic/binary classification — Green/Amber**
- sklearn `LogisticRegression`;
- train/test split + stratification;
- `predict_proba` and thresholding;
- confusion matrix, accuracy, precision, recall;
- later neural-network view: logit → sigmoid → BCE.

### Immediate gap: Fundamentals Week 3
- **Decision trees — Red**: splits, impurity, leaves, depth, overfitting.
- **Random forests — Red**: bootstrap/bagging, feature subsampling, voting/averaging, variance reduction.

### Later gaps
- Bayesian networks / inference / sampling;
- HMMs / particle filters;
- KNN / K-means / SVM / gradient boosting;
- RL / recommendation / generative models.

---

## Track F — Practical deep learning / PyTorch

### Why
AI in Practice reaches PyTorch in Week 3, MLP/CNN/RNN structures in Week 4 and housing-price prediction in Week 5.

### Current position
**MLP mechanics Green/Amber.** Verified progression:
- tensor operations and linear layers;
- autograd and `.grad`;
- manual GD and manual linear training;
- `nn.Linear`, MSE, SGD;
- ReLU and need for nonlinearity;
- `nn.Sequential` MLP;
- logits/sigmoid/BCE;
- `BCEWithLogitsLoss`;
- `TensorDataset` + `DataLoader`;
- mini-batches, epochs, shuffling;
- `torch.no_grad()` evaluation;
- synthetic binary classifier >90% test threshold in pytest (observed ~99.5% training accuracy).

### Important unfinished practical thread
The PyTorch classifier is still **synthetic and evaluated on its training data**. Next high-value task:

1. real dataset;
2. train/validation/test split;
3. feature scaling fitted correctly on training data;
4. DataLoaders;
5. train + validation metrics across epochs;
6. inspect errors/generalisation;
7. then convert the workflow to **regression** for housing-price preparation.

### Later
- CNN/RNN overview before AI in Practice Week 4;
- housing-price regression before Week 5;
- DataLoader optimisation Week 6;
- Fashion-MNIST/CNN before Week 7;
- parallel/distributed training, text analysis, deployment when course timing approaches.

---

## Track G — Probability, statistics and January ML Theory readiness

### Why
This is the largest medium-term mathematical risk. AIMS5704 explicitly assumes linear algebra, probability and statistics and begins with them immediately.

### Current position
**Amber/Red because it has not had recent deliberate practice.** The repo has no dedicated probability/statistics sequence, which is a useful warning: current retrieval work has overwhelmingly focused on Python/NumPy/calculus/ML implementation.

Existing hooks:
- previous probability/statistics study;
- black-box optimisation experience with Gaussian Processes, UCB/EI and exploration/exploitation;
- practical train/validation/generalisation intuition;
- strong gradient-descent/backprop mechanics.

### Term-1 maths lane
**Sep–Oct**
- probability notation, conditional probability, Bayes rule;
- random variables, expectation, variance/covariance;
- common distributions;
- linear algebra/norm refresh;
- logs/exponentials.

**Oct–Nov**
- likelihood and log-likelihood;
- MLE;
- sampling/estimators intuition;
- convexity + GD/SGD convergence intuition.

**Nov–Dec**
- empirical vs population risk;
- concentration intuition;
- VC dimension/capacity preview;
- kernel/feature-map intuition;
- short proof/derivation reading practice.

### January destination
Enter ML Theory able to follow definitions and short derivations rather than learning prerequisite notation during lectures.

---

# Dependency map

```text
Python / NumPy / Pandas
   ├──> data workflows ──> sklearn / PyTorch practice
   └──> DSA ──> BFS/DFS/A* ──> multi-agent search

Linear algebra + shapes
   ├──> linear/logistic models
   ├──> MLP ──> CNN/RNN
   └──> kernels / ML Theory

Calculus
   └──> partials ──> gradients ──> chain rule ──> backprop ──> SGD/Adam

Probability/statistics
   ├──> Bayes/inference ──> HMM/particle filters
   ├──> likelihood/MLE ──> exponential families
   ├──> generalisation theory
   └──> bandits / diffusion theory

Evaluation discipline
   └──> train/val/test + metrics + generalisation
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

These are intentionally preserved. “Parked” does **not** necessarily mean “never learned”.

- **BFS / DFS / A\*** — **implemented in lessons 24–26**, deliberately parked; must now be reactivated for Fundamentals Week 2. Add UCS + trade-off/heuristic theory rather than rewriting from scratch.
- **Logic/reasoning** — Week 1 Fundamentals; not yet properly studied.
- **Decision trees / random forests** — Week 3 Fundamentals; not present in repo yet.
- **Real-data PyTorch workflow** — lesson 30 is synthetic; real split/scaling/validation still pending.
- **NN regression / housing-price workflow** — needed before AI in Practice Week 5.
- **CNN/RNN preview** — needed before AI in Practice Week 4.
- **Probability/statistics refresh** — mandatory parallel Term-1 lane for ML Theory Jan 11.
- **Formal complexity + graph/tree DSA** — search works in code, but theory/complexity is not yet systematic.
- **Vector/Jacobian calculus** — defer until deeper NN/theory work actually needs it.
