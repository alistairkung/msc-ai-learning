# MSc Syllabus Preparation Map

_Last reviewed: 2026-09-05_
_Readiness calibrated against the exercise repository, completed Lesson 31 workflow, and reconstructed historical JHU maths foundations_

## Use

This is the bridge between the **actual MSc sequence** and preparation. Read it with `LEARNING_STATE.md` before choosing a session.

Readiness key:
- **Green** — already practised; mainly retrieval/application needed.
- **Amber** — foundation exists but not yet automatic or complete.
- **Red** — genuinely new / prerequisite gap.

---

# AIMS5701 — Fundamentals in Artificial Intelligence

**Term:** Sep–Dec 2026

| Week | MSc topic | Current readiness | Evidence / existing hook | Main gap before lecture |
|---|---|---|---|---|
| W1 | Introduction, Logic, Reasoning and Learning | **Amber/Red** | General AI/ML vocabulary strong enough | Formal logic/reasoning vocabulary is new; preview propositions/rules/inference at a light level |
| W2 | Uninformed search, informed search, searching with other agents | **Amber/Green** | Repo 24–26 implements BFS, DFS, A* | Reactivate from cold recall; add UCS; compare completeness/optimality/time/memory; heuristic admissibility/consistency; multi-agent search new |
| W3 | Linear regression, logistic regression, decision trees, random forests | **Linear/logistic Green/Amber; trees Red** | Repo 21–23 + Lessons 30–31 classification/evaluation work + historical least-squares/normal-equation foundation | Consolidate model maths; learn decision trees + random forests before W3 |
| W4 | Bayesian networks, inference, sampling | **Amber** | Historical JHU probability strongly covers conditional probability, independence, total probability, Bayes, random variables and joint/marginal distributions | Cold-retrieve Bayes/conditioning; then learn graphical-model semantics, conditional independence in graphs and inference/sampling algorithms |
| W5 | Hidden Markov Models, particle filtering | **Amber/Red** | Historical probability foundation established; learner remembers Markov chains but recoverable worked evidence is weak | Diagnose Markov-chain recall first; then Markov property, transition/state reasoning, filtering and particle sampling |
| W6 | KNN, K-means, SVM, gradient boosting | **Red/Amber** | Distance/vector and classification workflow foundations | Fast conceptual + implementation survey; focus on model assumptions/trade-offs |
| W7 | Neural networks | **Green/Amber** | Repo 27–31, including the completed real-data workflow | Deeper architecture vocabulary |
| W8 | Backpropagation and SGD | **Green/Amber** | Manual autograd/GD + standard PyTorch loops; chain rule/backprop derived by hand | Keep chain-rule notation warm; theory of convergence still later |
| W9 | Computer vision | **Red/Amber** | Tensor/shape base | Image tensor semantics + CNN basics; AI in Practice should lead this |
| W10 | NLP | **Red/Amber** | General software/LLM familiarity | Formal text representation/embedding/sequence-model basics |
| W11 | Reinforcement learning, recommendation | **Amber/Red** | Exploration/exploitation hooks from black-box optimisation/agentic study | MDP/value/policy/Q basics; recommendation formulation |
| W12 | Generative models | **Amber/Red** | NN foundation; generative-AI familiarity | Probabilistic/generative modelling foundations; keep preview light |

### Fundamentals next priorities

1. **Search reactivation cannot disappear again.** Code exists; now build exam/lecture-level conceptual comparison.
2. **Decision trees/random forests** create the Week-3 buffer.
3. Before W4, cold-retrieve the historical Bayes/random-variable foundation rather than relearning probability from zero.
4. Before W5, run a diagnostic on remembered Markov-chain material and rebuild only what does not return.

---

# AIMS5702 — Artificial Intelligence in Practice

**Term:** Sep–Dec 2026

| Week | MSc topic | Current readiness | Evidence / existing hook | Main gap before lecture |
|---|---|---|---|---|
| W1 | Intro + simple ML example | **Green** | sklearn classification/regression plus completed Lesson 31 real-data train/validation/test pipeline | Retrieve and apply the workflow in a new context |
| W2 | Vector, matrix, tensor ops; NumPy | **Green/Amber** | Completed 2025 JHU linear algebra foundation + Repo 10–17 + 27 + Lesson 31 scaling/axis/tensor conversion | Cold-retrieve notation/matrix mechanics as needed; keep PyTorch weight orientation and NumPy reduction-shape retrieval active |
| W3 | 1D/2D signals; image/audio/text/video/sequential representation; SciPy, matplotlib, PyTorch | **Amber** | PyTorch/tensor base strong | SciPy/matplotlib + modality representations not yet systematic |
| W4 | MLP, CNN, RNN | **MLP Green/Amber; CNN/RNN Red** | Repo 28–30 + Lesson 31 MLP workflow | CNN/RNN architecture intuition before W4; do not need mastery yet |
| W5 | Housing-price prediction (Boston House Dataset) | **Amber/Green** | sklearn regression (23), MLP/MSE mechanics, completed Lesson 31 preprocessing/validation workflow | Transfer the same split/scaling/validation discipline to NN regression |
| W6 | Data prep + data loading optimisation | **Amber/Green** | `TensorDataset`/`DataLoader`, mini-batches, shuffle retrieved again in Lesson 31 | Workers/pinning/loading efficiency are new |
| W7 | Fashion-MNIST visual classification | **Red/Amber** | MLP + DataLoader base | CNN practical training before/around W7 |
| W8 | Parallel / multi-GPU / distributed training | **Amber conceptually** | Strong distributed-systems/SWE background | PyTorch-specific parallel/distributed APIs |
| W9 | IMDB sentiment analysis | **Red/Amber** | Classification pipeline base | Text preprocessing/embeddings/sequence model practice |
| W10 | Model optimisation + on-device deployment | **Amber** | Strong production engineering base | ML export/quantisation/performance tooling |
| W11 | Foundation models / diffusion / LLM / segmentation | **Amber** | Modern-AI familiarity | Framework-specific practical work; foundations should be sufficient by then |
| W12 | Project presentation | **TBD** | Engineering/project communication strength | Keep experiments/reproducibility tidy from the start |

### AI in Practice next priorities

1. **Search reactivation remains the cross-course primary next session**; Lesson 31 no longer blocks this course's introductory workflow readiness.
2. **NN regression** before W5, transferring the same leakage-safe preprocessing and validation workflow.
3. **CNN/RNN preview** before W4; deeper CNN before Fashion-MNIST.

### Lesson 31 readiness gain

New practical concepts implemented end to end:
- 60/20/20 train/validation/test split with stratification;
- train-only fitted `StandardScaler` and data-leakage reasoning;
- validation/test transformed with frozen training statistics;
- float32 tensor conversion and `(n,) -> (n,1)` target reshape;
- DataLoader batch arithmetic including final partial batch;
- one train-loss + one validation-loss value per epoch;
- validation under `torch.no_grad()` without parameter updates;
- overfitting recognised from falling train loss + rising validation loss;
- held-out test set reserved for final evaluation.

Optional continuation: retain and restore the best-validation checkpoint when early stopping/model selection is introduced.

---

# AIMS5704 — Machine Learning Theory

**Starts:** 11 Jan 2027

This course explicitly assumes **linear algebra, probability and statistics**. Its maths preparation must run during Term 1 rather than waiting until January.

Both prerequisite areas are **not first exposure**. JHU linear algebra and two JHU probability modules were completed in 2025 and are now preserved as historical retrieval blueprints. The Term-1 job is to reactivate them and connect them to ML notation while learning the genuinely new theory layer.

| Week | Theory topic | Current readiness | Main gap | Term-1 preparation |
|---|---|---|---|---|
| W1 | Probability + Linear Algebra tools | **Amber/Green retrieval** | Both foundations are established but cold retrieval is due; proof/notation fluency is less automatic | Short LA retrieval plus probability retrieval: Bayes, RVs/distributions, expectation/variance/covariance, CLT; diagnose Markov/Poisson separately |
| W2 | MLE, exponential-family models | **Red/Amber** | Likelihood/log-likelihood/exponential-family form not yet systematically evidenced | Logs/exponentials, distributions, likelihood/MLE; build on established probability rather than restart it |
| W3 | Empirical vs population risk; uniform convergence | **Red/Amber** | Lesson 31 strengthens practical generalisation intuition; formal risk/concentration notation remains new | Translate validation/generalisation intuition into empirical/population risk; concentration intuition |
| W4 | VC dimension + generalisation bounds | **Red** | Capacity/proof/bounds are new | VC-dimension intuition + inequality/proof-reading practice; historical Markov/Chebyshev work is an early concentration hook |
| W5 | GD + convergence analysis | **Mechanics Green; theory Amber/Red** | GD implemented and understood; convergence assumptions/derivations new | Convexity/smoothness/learning-rate effects; simple convergence derivations; quadratic-form/positive-definite intuition when useful |
| W6 | SGD, AdaGrad, Adam | **SGD Green/Amber; adaptive Red** | Mini-batch SGD known; adaptive algorithms/theory new | Compare update rules; learn Adam/AdaGrad later in Term 1 |
| W7 | Representer theorem + kernels | **Red** | Kernel theory new | Feature maps, kernels, Gram matrices, norms; reactivate inner-product/projection intuition |
| W8 | NTK + deep-learning generalisation/optimisation | **Red** | Advanced | Do not pre-master; secure W7 and optimisation foundations |
| W9 | Regret + expert advice | **Amber/Red** | Formal online-learning/regret new | Exploration/exploitation hook exists; learn regret notation later |
| W10 | Greedy / ε-greedy | **Amber** | Bandit formalism new | Expected reward/regret + ε-greedy; expectation foundation already exists |
| W11 | UCB + Thompson sampling | **Amber** | UCB hook from prior BBO; Thompson sampling theory new | Bayes/expectation refresh should make the formalism easier |
| W12 | Score functions / score-based generative modelling | **Red** | Gradients of log densities + formal probability gap | Probability + logs + gradients must be solid first |
| W13 | Langevin dynamics / diffusion sampling | **Red** | Advanced stochastic/calculus material | Leave until foundations are ready; preview in Dec if bandwidth exists |

## January-entry minimum standard

By 11 Jan, aim to be able to:

- manipulate vectors/matrices and common norms without shape panic;
- retrieve core LA geometry when invoked rather than relearning it;
- retrieve conditional probability/Bayes, random variables/distributions, expectation/variance/covariance and CLT without rebuilding the whole JHU course;
- diagnose/rebuild Markov-chain and Poisson material if needed;
- derive a simple likelihood and log-likelihood;
- differentiate composite scalar objectives and reason about gradients;
- explain GD vs SGD and learning-rate behaviour;
- express training/generalisation as empirical vs population risk at an introductory level;
- read a short mathematical derivation without every symbol becoming a blocker.

---

# Rolling buffer policy

During term:

1. Update `LEARNING_STATE.md` after each study session/lecture.
2. Look **1–2 syllabus weeks ahead** across both Term-1 courses.
3. Choose one **upcoming prerequisite bottleneck** + one **implementation/application**.
4. Protect a small recurring **ML Theory maths lane** each week.
5. Any intentionally paused topic stays in `PARKED / MUST RETURN` until explicitly reactivated or rescheduled.
