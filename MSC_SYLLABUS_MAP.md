# MSc Syllabus Preparation Map

_Last reviewed: 2026-09-03_  
_Readiness calibrated against the exercise repository on 2026-09-03_

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
| W3 | Linear regression, logistic regression, decision trees, random forests | **Linear/logistic Green/Amber; trees Red** | Repo 21–23: sklearn logistic/linear pipelines + metrics; earlier manual linear models | Consolidate model maths; learn decision trees + random forests before W3 |
| W4 | Bayesian networks, inference, sampling | **Red/Amber** | Prior probability study gives a hook | Probability/Bayes refresh; conditional independence; graph semantics; sampling intuition |
| W5 | Hidden Markov Models, particle filtering | **Red** | Sequence/state intuition only | Conditional probability, Markov property, filtering and sampling foundations |
| W6 | KNN, K-means, SVM, gradient boosting | **Red/Amber** | Distance/vector and classification workflow foundations | Fast conceptual + implementation survey; focus on model assumptions/trade-offs |
| W7 | Neural networks | **Green/Amber** | Repo 27–30: tensor ops, autograd, SGD, MLP binary classifier | Real-data repetition; deeper architecture vocabulary |
| W8 | Backpropagation and SGD | **Green/Amber** | Manual autograd/GD + standard PyTorch loops; chain rule/backprop derived by hand | Keep chain-rule notation warm; theory of convergence still later |
| W9 | Computer vision | **Red/Amber** | Tensor/shape base | Image tensor semantics + CNN basics; AI in Practice should lead this |
| W10 | NLP | **Red/Amber** | General software/LLM familiarity | Formal text representation/embedding/sequence-model basics |
| W11 | Reinforcement learning, recommendation | **Amber/Red** | Exploration/exploitation hooks from black-box optimisation/agentic study | MDP/value/policy/Q basics; recommendation formulation |
| W12 | Generative models | **Amber/Red** | NN foundation; generative-AI familiarity | Probabilistic/generative modelling foundations; keep preview light |

### Fundamentals next priorities

1. **Search reactivation cannot disappear again.** Code exists; now build exam/lecture-level conceptual comparison.
2. **Decision trees/random forests** create the Week-3 buffer.
3. Start probability refresh early enough that W4–5 and January ML Theory reinforce one another.

---

# AIMS5702 — Artificial Intelligence in Practice

**Term:** Sep–Dec 2026

| Week | MSc topic | Current readiness | Evidence / existing hook | Main gap before lecture |
|---|---|---|---|---|
| W1 | Intro + simple ML example | **Green** | Repo has sklearn classification/regression and PyTorch training pipelines | Do one genuine dataset end-to-end |
| W2 | Vector, matrix, tensor ops; NumPy | **Green/Amber** | Repo 10–17 + 27 extensively practises shapes, axes, masks, broadcasting, standardisation, reshape/transpose | Keep PyTorch weight orientation/batch-shape retrieval active |
| W3 | 1D/2D signals; image/audio/text/video/sequential representation; SciPy, matplotlib, PyTorch | **Amber** | PyTorch/tensor base strong | SciPy/matplotlib + modality representations not yet systematic |
| W4 | MLP, CNN, RNN | **MLP Green/Amber; CNN/RNN Red** | Repo 28–30 gives autograd, SGD, MLP classifier | CNN/RNN architecture intuition before W4; do not need mastery yet |
| W5 | Housing-price prediction (Boston House Dataset) | **Amber/Green** | sklearn regression already done (repo 23); MLP/MSE mechanics known | Real-data preprocessing + NN regression + proper validation |
| W6 | Data prep + data loading optimisation | **Amber/Green** | `TensorDataset`/`DataLoader`, mini-batches, shuffle already used in repo 30 | Workers/pinning/loading efficiency are new |
| W7 | Fashion-MNIST visual classification | **Red/Amber** | MLP + DataLoader base | CNN practical training before/around W7 |
| W8 | Parallel / multi-GPU / distributed training | **Amber conceptually** | Strong distributed-systems/SWE background | PyTorch-specific parallel/distributed APIs |
| W9 | IMDB sentiment analysis | **Red/Amber** | Classification pipeline base | Text preprocessing/embeddings/sequence model practice |
| W10 | Model optimisation + on-device deployment | **Amber** | Strong production engineering base | ML export/quantisation/performance tooling |
| W11 | Foundation models / diffusion / LLM / segmentation | **Amber** | Modern-AI familiarity | Framework-specific practical work; foundations should be sufficient by then |
| W12 | Project presentation | **TBD** | Engineering/project communication strength | Keep experiments/reproducibility tidy from the start |

### AI in Practice next priorities

1. **Real dataset now**: split, scaling, training, validation, error inspection.
2. **NN regression** before W5, building on repo 23 + 29–30.
3. **CNN/RNN preview** before W4; deeper CNN before Fashion-MNIST.

---

# AIMS5704 — Machine Learning Theory

**Starts:** 11 Jan 2027

This course explicitly assumes **linear algebra, probability and statistics**. Its maths preparation must run during Term 1 rather than waiting until January.

| Week | Theory topic | Current readiness | Main gap | Term-1 preparation |
|---|---|---|---|---|
| W1 | Probability + Linear Algebra tools | **Amber** | Probability/statistics not recently exercised; LA needs retrieval | Weekly probability/LA refresh; norms and notation |
| W2 | MLE, exponential-family models | **Red/Amber** | Likelihood/log-likelihood/exponential-family form not yet systematic | Logs/exponentials, distributions, likelihood/MLE |
| W3 | Empirical vs population risk; uniform convergence | **Red** | Current generalisation knowledge is practical, not formal | Translate train/val intuition into risk notation; concentration intuition |
| W4 | VC dimension + generalisation bounds | **Red** | Capacity/proof/bounds are new | VC-dimension intuition + inequality/proof-reading practice |
| W5 | GD + convergence analysis | **Mechanics Green; theory Amber/Red** | GD implemented and understood; convergence assumptions/derivations new | Convexity/smoothness/learning-rate effects; simple convergence derivations |
| W6 | SGD, AdaGrad, Adam | **SGD Green/Amber; adaptive Red** | Mini-batch SGD known; adaptive algorithms/theory new | Compare update rules; learn Adam/AdaGrad later in Term 1 |
| W7 | Representer theorem + kernels | **Red** | Kernel theory new | Feature maps, kernels, Gram matrices, norms |
| W8 | NTK + deep-learning generalisation/optimisation | **Red** | Advanced | Do not pre-master; secure W7 and optimisation foundations |
| W9 | Regret + expert advice | **Amber/Red** | Formal online-learning/regret new | Exploration/exploitation hook exists; learn regret notation later |
| W10 | Greedy / ε-greedy | **Amber** | Bandit formalism new | Expected reward/regret + ε-greedy |
| W11 | UCB + Thompson sampling | **Amber** | UCB hook from prior BBO; Thompson sampling theory new | Probability/Bayesian refresh makes this much easier |
| W12 | Score functions / score-based generative modelling | **Red** | Gradients of log densities + probability gap | Probability + logs + gradients must be solid first |
| W13 | Langevin dynamics / diffusion sampling | **Red** | Advanced stochastic/calculus material | Leave until foundations are ready; preview in Dec if bandwidth exists |

## January-entry minimum standard

By 11 Jan, aim to be able to:

- manipulate vectors/matrices and common norms without shape panic;
- use conditional probability, Bayes rule, expectation/variance and common distributions comfortably;
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
