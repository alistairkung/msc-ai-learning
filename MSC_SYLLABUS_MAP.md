# MSc Syllabus Preparation Map

_Last reviewed: 2026-09-08_
_Readiness calibrated against the exercise repository, completed Lesson 31 workflow, reconstructed historical JHU maths foundations, the one-week AIMS5701 start delay, and live FTEC5660 Lecture 1 / Prompt Chaining material_

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

# FTEC5660 — Agentic AI in Finance / FinTech

**Term:** Sep–Dec 2026  
**Live status:** Lecture 1 completed on **2026-09-08**; Pattern 1 Prompt Chaining taught, with tutorial progress through successful JSON parsing.  
**Detailed course context:** `lesson_logs/ftec5660_course_context.md`  
**Introduction retrieval log:** `lesson_logs/ftec5660_lecture01_introduction.md`  
**Pattern 1 retrieval/tutorial log:** `lesson_logs/ftec5660_pattern01_prompt_chaining.md`

This course is being taught through the lens of automating finance/fintech/business workflows rather than purely through autonomous software engineering. Prior cross-border payments, KYC/onboarding and AML experience should be used deliberately as an interpretation layer.

## Lecture-1 overview of future course coverage

Lecture 1 showed a catalogue of **21 named agentic design patterns** as an introductory overview of material the course will cover. The slide groups them around orchestration, enterprise knowledge/system access, multi-agent collaboration, decision intelligence, and governance/safety/operational control.

The names shown were:

- prompt chaining;
- routing;
- parallelisation;
- planning;
- goal setting and monitoring;
- tool use / function calling;
- Model Context Protocol;
- memory management;
- knowledge retrieval;
- multi-agent collaboration;
- inter-agent communication;
- reflection;
- learning and adaptation;
- reasoning;
- exploration and discovery;
- exception handling and recovery;
- human in the loop;
- resource-aware optimisation;
- guardrails;
- evaluation and monitoring;
- prioritisation.

### Important learning boundary

This list is **orientation, not a 21-item readiness table and not a cold-recall target from Lecture 1**.

Do not ask the learner to enumerate the full catalogue. Do not assign Green/Amber/Red readiness to individual patterns merely because their names appeared on the overview slide. Add a pattern to active readiness/retrieval tracking only when later lectures, labs or projects teach/apply it substantively.

Prompt Chaining is now the first pattern to cross that boundary.

## Pattern 1 — Prompt Chaining current boundary

**Current readiness:** **Concept Amber/Green; LangChain syntax Amber/Red.**

Conceptual baseline now fair for retrieval:

```text
complex task
    -> focused stage
    -> structured/checkable handoff
    -> focused stage
    -> final result
```

Important distinctions:

- chaining is useful when stages are stable, sequential and independently checkable;
- structured outputs and explicit interfaces make intermediate state inspectable;
- deterministic code/validation can sit between LLM stages — a chain is not necessarily LLM -> LLM -> LLM;
- additional stages trade latency/cost/maintenance complexity for control and diagnosability;
- routing, parallelisation or a true agent are better fits when the task shape itself is not a fixed sequential chain.

### Tutorial progress

The supplied notebook goes considerably beyond class progress. Current evidence stops at/around the successful expense-ledger **LLM parse into JSON**.

Syntax encountered so far:

- `ChatDeepSeek(...)` and `.invoke(...)`;
- `ChatPromptTemplate.from_template(...)`;
- LCEL pipe composition with `|`;
- `StrOutputParser()` vs `JsonOutputParser()`;
- invocation dictionaries matching prompt placeholders;
- mapping an earlier extraction sub-chain into a later prompt variable.

Not yet a fair taught/mastery target from later notebook cells:

- substantive `RunnablePassthrough.assign(...)` use;
- `RunnableLambda(...)` in the completed ledger pipeline;
- full `parse -> compute -> explain` wiring;
- later validation gates / repair loops in code;
- TaxCalcBench workflow.

### Immediate preparation task

Schedule one dedicated session **this week** to reconstruct the LangChain syntax from memory using the same incremental approach used for NumPy:

1. explain object roles;
2. rebuild a one-stage `prompt -> llm -> parser` chain from a blank file;
3. change to structured JSON output;
4. build a two-stage chain that passes one result into the next;
5. repeat using a small payments/KYC/AML-flavoured example rather than copying the tutorial.

Do not mark syntax established until it can be produced and explained independently.

## Lecture-1 conceptual baseline

The useful first-lecture readiness target remains:

- explain what makes a system agentic;
- explain the perceive → reason/plan → act → learn/escalate loop;
- explain why multi-step agent behaviour creates reliability/coordination problems;
- understand the rough complexity progression from reasoning core to connected/strategic/collaborative agents;
- recognise that the remaining pattern catalogue is the roadmap for later teaching rather than material already mastered.

## Personal learning strategy for this course

When a specific pattern is actually taught:

1. recover the lecturer's definition first;
2. place it beside the closest conventional SWE concept;
3. reinterpret it through payments/KYC/AML;
4. ask what genuinely improves by making the workflow agentic;
5. identify the new failure/verification/governance burden.

This is a deliberate course-learning method, not extra material to memorise.

## Assessment / workload planning

**Learner recollection from class — verify against official assessment documentation:**

- two major project-style assessments: a **hackathon** and a **final project**;
- recollection is that they account for **roughly 80% of the module grade combined**.

Even before the exact weighting is verified, treat FTEC5660 as a **high-variance Term-1 workload source**. Project periods may temporarily consume much more time than ordinary lecture weeks.

### Planning implications

- Do **not** pre-study or memorise the 21-pattern overview simply because the list exists; let live lectures/projects determine which patterns deserve depth.
- After each lecture, use a short retrieval block focused on concepts actually taught and preserve only durable personal synthesis.
- When a live tutorial introduces a library syntax layer, distinguish **concept understood** from **syntax independently retrievable** and schedule a bounded practice session when needed.
- When project dates/scope become known, add them explicitly to the planning state.
- During heavy FTEC5660 project weeks, allow the general preparation buffer to shrink, but preserve a **minimum January maths continuity lane** for AIMS5704 rather than dropping maths entirely.
- Use the projects as opportunities to connect newly taught agentic patterns with real financial-domain/system-reliability questions rather than treating them as isolated demo builds.

---

# AIMS5704 — Machine Learning Theory

**Starts:** 11 Jan 2027

This course explicitly assumes **linear algebra, probability and statistics**. Its maths preparation must run during Term 1 rather than waiting until January.

Both prerequisite areas are **not first exposure**. JHU linear algebra and two JHU probability modules were completed in 2025 and are now preserved as historical retrieval blueprints. The Term-1 job is to reactivate them and connect them to ML notation while learning the genuinely new theory layer.

FTEC5660's project-heavy assessment structure creates a competing Term-1 time demand. The response should be to **scale the maths lane during peak project weeks, not erase it**.

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
