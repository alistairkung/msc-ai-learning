# MSc Syllabus Preparation Map

_Last reviewed: 2026-09-08_
_Readiness calibrated against the exercise repository, completed Lesson 31 workflow, reconstructed historical JHU maths foundations, and the one-week AIMS5701 start delay_

## Use

This is the bridge between the **actual MSc sequence** and preparation. Read it with `LEARNING_STATE.md` before choosing a session.

Readiness key:
- **Green** — already practised; mainly retrieval/application needed.
- **Amber** — foundation exists but not yet automatic or complete.
- **Red** — genuinely new / prerequisite gap.

---

# AIMS5701 — Fundamentals in Artificial Intelligence

**Term:** Sep–Dec 2026  
**Timing update:** the course start has been delayed by **one week**. Preserve the syllabus week ordering below; use the added pre-course runway to deepen search preparation rather than shifting the topic labels themselves.

| Week | MSc topic | Current readiness | Evidence / existing hook | Main gap before lecture |
|---|---|---|---|---|
| W1 | Introduction, Logic, Reasoning and Learning | **Amber/Red** | General AI/ML vocabulary strong enough | Formal logic/reasoning vocabulary is new; preview propositions/rules/inference at a light level |
| W2 | Uninformed search, informed search, searching with other agents | **Amber/Green overall; multi-agent Red** | BFS/DFS reactivated; historical A* implementation exists; UCS/admissibility/consistency/completeness/optimality now introduced | Finish UCS implementation and A* reconstruction; consolidate guarantees/time/memory; then explicitly learn the untouched “searching with other agents” branch, using course materials to confirm its exact framing |
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

1. **Exploit the extra pre-course week without over-drilling BFS.** Independent BFS reconstruction is already evidenced; move forward.
2. **Close single-agent search:** UCS implementation → A* reconstruction → short guarantees/complexity consolidation.
3. **Cover the missing Week-2 branch:** “searching with other agents” is genuinely new. If course materials confirm standard adversarial search, prepare game trees/minimax/alpha-beta at introductory depth; do not assume beyond the available syllabus/materials.
4. Run one integrated search review shortly before the W2 lecture rather than repeatedly reconstructing the same algorithms.
5. Use remaining buffer for W1 logic/reasoning and then **decision trees/random forests** for W3.
6. Before W4, cold-retrieve the historical Bayes/random-variable foundation rather than relearning probability from zero.
7. Before W5, run a diagnostic on remembered Markov-chain material and rebuild only what does not return.

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
- follow basic proof/inequality arguments without notation becoming the primary blocker.
