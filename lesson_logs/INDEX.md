# Lesson Log Index

_Last audited: 2026-09-10_

This directory is the durable conceptual/retrieval record for the learning sequence. Exercise/test files are the implementation evidence; these logs explain what should be understood and how to cold-retrieve it later.

## Organisation

`lesson_logs/` contains two different kinds of record:

```text
lesson_logs/
  aims5701/      live-course logs for AIMS5701
  aims5702/      live-course logs for AIMS5702
  aims5704/      live-course logs for AIMS5704
  ftec5660/      live-course logs for FTEC5660

  lessonNN_*.md  numbered cross-course preparation lessons
  historical_*.md  reconstructed pre-repo foundation records
```

Live-course material belongs in the matching course folder. Numbered preparation lessons and historical foundation logs stay at the root because they deliberately span course boundaries.

A future tutor/model should use this index for discovery, then read the smallest relevant file rather than loading an entire course folder by default.

## Historical pre-repo learning

Some important learning happened interactively in chat before the numbered repository lesson workflow existed. These records are kept separately rather than being assigned invented lesson numbers.

| Record | Topic | Log status |
|---|---|---|
| Historical calculus foundations | Slope/local rate → limits/difference quotient → power/product rules → partial derivatives → gradients → gradient descent → chain rule/manual backprop | Reconstructed from recoverable tutoring context; bridges directly into Lesson 28 |
| Historical linear algebra 01 | Linear systems → RREF → pivots/free variables → parametric solutions → span/independence/basis/subspaces | Reconstructed from recoverable JHU tutoring context |
| Historical linear algebra 02 | Matrix algebra/determinants → eigenvalues/eigenvectors/eigenspaces → diagonalization | Reconstructed from recoverable JHU tutoring context |
| Historical linear algebra 03 | Orthogonality → projections → Gram–Schmidt → least squares/normal equations | Reconstructed from recoverable JHU tutoring + notebook evidence |
| Historical linear algebra 04 | Symmetric matrices → orthogonal diagonalization → orthogonal matrices → quadratic forms | Reconstructed from recoverable JHU tutoring evidence |
| Historical probability/statistics 01 | Counting/sample spaces → axioms → conditional probability → independence → total probability → Bayes | Strong recoverable JHU tutoring evidence |
| Historical probability/statistics 02 | Random variables → geometric distribution → expectation/variance → PDF/CDF → Uniform/Exponential/Normal | Strong recoverable JHU tutoring evidence |
| Historical probability/statistics 03 | Joint/marginal distributions → linearity/indicators → covariance/correlation → Markov/Chebyshev inequalities | Strong recoverable JHU tutoring + notebook evidence |
| Historical probability/statistics 04 | CLT → sampling distributions → standard error → hypothesis testing/p-values; Markov-chain/Poisson evidence boundary | Strong evidence for CLT/testing; Markov chains and Poisson recorded as historically studied but diagnostic-needed |

See the historical foundation directories under `foundations/` and the corresponding logs in this directory. Historical records are retrieval blueprints, not invented transcripts or fabricated exercise/test evidence.

## Live MSc course records

### AIMS5701 — Fundamentals in AI

Folder: `lesson_logs/aims5701/`

No substantive live-course lesson log yet. Use the folder `README.md` plus `MSC_SYLLABUS_MAP.md` until lecture-specific material is recorded.

### AIMS5702 — Artificial Intelligence in Practice

Folder: `lesson_logs/aims5702/`

| Record | Topic | Log status |
|---|---|---|
| `README.md` | Course-folder purpose and links back to existing preparation | Active course index |
| `lecture01_02_prelecture_bridge.md` | Lecture 1 reflection plus pre-read bridge into dtype/memory/stride/einsum; diagram/index ↔ shape translation strategy | Lecture 1 attended; later systems material explicitly remains guided pre-read until taught |

For AIMS5702, preserve tensor **shape reasoning as the learner's anchor** and train translation between network diagrams, shapes, index notation, PyTorch and parameter count. Do not mistake a representation-translation cost for a conceptual gap.

### AIMS5704 — Machine Learning Theory

Folder: `lesson_logs/aims5704/`

No live-course lesson log yet. Historical maths preparation remains in the root/foundation records until the course starts.

### FTEC5660 — Agentic AI in Finance / FinTech

Folder: `lesson_logs/ftec5660/`

| Record | Topic | Log status |
|---|---|---|
| `README.md` | Course-folder navigation and source-boundary reminder | Active course index |
| `course_context.md` | Course spine, assessment/workload notes, personal learning lens, durable synthesis across lectures | Active course-level context; distinguish lecture-supported content from personal working hypotheses |
| `lecture01_introduction.md` | Agentic AI introduction: goal-directed systems, perceive/reason/act/escalate loop, pattern catalogue, complexity levels, multi-agent framing; plus SWE/finance reinterpretation | Original lecture + post-lecture synthesis log; introductory pattern catalogue is a reference map rather than a list-recall target |
| `pattern01_prompt_chaining.md` | Pattern 1 prompt chaining: decomposition, checkable stage interfaces, context engineering, trade-offs; LangChain/LCEL tutorial through successful JSON parsing | **Concept taught; tutorial partial.** Later workbook sections remain separate from what class actually reached |
| `lcel_guided_practice_2026_09_09.md` | Guided LCEL reconstruction: prompt templates, parsers, invocation and build/run-time separation | Taught/guided evidence; records support needs before Lesson 32 exercises |
| `tutorial01_study_plan.md` | Plain-English follow-up route through Tutorial 1: state enrichment, Python runnables, gates, compact payments/KYC workflow, generated-code concept and routing bridge | **Parked plan.** Resume one day before the next FTEC5660 lecture; notebook itself is not committed |

For FTEC5660, future lecture/project logs should preserve the same source boundary: **what the lecturer/material supports** vs **the learner's own synthesis or hypothesis**. Tutorial logs must also preserve the actual in-class stopping point: code appearing later in a supplied notebook is not automatically learned material.

## Numbered lesson coverage

All numbered lessons **01–33 now have a lesson log**.

| Lesson | Topic | Log status |
|---|---|---|
| 01 | Python lists | Reconstructed |
| 02 | Dictionaries | Reconstructed |
| 03 | Sets | Reconstructed |
| 04 | Strings | Reconstructed |
| 05 | Comprehensions | Reconstructed |
| 06 | `key=` functions / lambdas | Reconstructed |
| 07 | Function arguments | Reconstructed |
| 08 | DSA: hash lookup + two pointers | Reconstructed |
| 09 | Sliding window | Reconstructed |
| 10 | NumPy foundations | Reconstructed |
| 11 | Broadcasting + standardisation | Reconstructed |
| 12 | Manual linear model | Reconstructed |
| 13 | Cold retrieval checkpoint | Reconstructed |
| 14 | NumPy classification pipeline | Reconstructed |
| 15 | NumPy challenge | Reconstructed |
| 16 | Composed ML pipeline | Reconstructed |
| 17 | Mixed retrieval checkpoint | Reconstructed |
| 18 | pandas fundamentals | Reconstructed |
| 19 | pandas challenge | Reconstructed |
| 20 | NumPy + pandas refresher | Reconstructed |
| 21 | sklearn classification intro | Reconstructed |
| 22 | sklearn classification pipeline + thresholds | Reconstructed |
| 23 | sklearn linear regression | Reconstructed |
| 24 | BFS | Reconstructed |
| 25 | DFS | Reconstructed |
| 26 | A* | Reconstructed |
| 27 | Tensor/shape operations | Reconstructed |
| 28 | PyTorch autograd + manual GD | Reconstructed |
| 29 | Standard PyTorch linear training loop | Reconstructed |
| 30 | PyTorch binary classification | Original detailed session log |
| 31 | Real-data classification workflow | Original detailed session log — **complete** |
| 32 | LangChain / LCEL basics | Original session log — **guided implementation + changed-example pytest complete; cold reconstruction due** |
| 33 | Search reconstruction: BFS / DFS / UCS / A* | Original session log — **integrated suite passes; UCS/A* guided derivation; guarantees/complexity next** |

“Reconstructed” means the available implementation evidence and recoverable tutoring context are used conservatively. These are not invented transcripts.

## Useful groupings

```text
Historical calculus  slope → derivative → differentiation rules → gradients → chain rule/backprop
Historical linear algebra  systems/vector spaces → matrices/eigen → orthogonality/least squares → symmetric/quadratic forms
Historical probability/statistics  counting/Bayes → random variables/distributions → joint moments/inequalities → CLT/inference
AIMS5701 live course  lesson_logs/aims5701/
AIMS5702 live course  lesson_logs/aims5702/
AIMS5704 live course  lesson_logs/aims5704/
FTEC5660 live course  lesson_logs/ftec5660/
01–07  Python language fluency
08–09  DSA patterns
10–17  NumPy / shape / manual ML + retrieval
18–20  pandas / data workflow
21–23  sklearn classical ML
24–26  original classical-search lessons
27–30  tensors, autograd and PyTorch training
31     real-data PyTorch workflow (complete)
32     LangChain / LCEL basics (guided; later cold reconstruction)
33     integrated search reactivation: BFS/DFS recall → UCS → A*
```

## How to use

For “cold retrieve Lesson N”:
1. read the root `lesson_logs/lessonNN_*.md`;
2. inspect its exercise/test if needed;
3. ask one question at a time;
4. change numbers/context instead of repeating tests verbatim;
5. probe known fragile points;
6. stop once retention is clear.

For a live MSc course:
1. open `lesson_logs/<course_code>/`;
2. read its `README.md`/`course_context.md` if broad orientation is needed;
3. otherwise read only the smallest relevant lecture/tutorial/project log;
4. preserve distinctions between lecture-covered, pre-read, learner synthesis and independently demonstrated material;
5. do not create course notes in a separate top-level `notes/` folder.

For search after Lesson 33:
1. do not immediately replay all four implementations;
2. consolidate completeness/optimality and assumptions;
3. retrieve admissibility vs consistency;
4. add time/memory complexity;
5. later use one short changed-graph UCS/A* reconstruction as the next independence check;
6. keep the repeated path-reconstruction cursor fragility in the recall pool.

For FTEC5660 specifically:
1. read the relevant file under `lesson_logs/ftec5660/`;
2. cold-retrieve **course material** first;
3. sample only a few **personal-synthesis** prompts per session rather than replaying the whole discussion;
4. connect the concept to a familiar payments/KYC/AML example;
5. for code tutorials, quiz only syntax/mechanisms that the class or a later independent practice session actually reached;
6. when resuming Tutorial 1 after Lesson 32, follow `lesson_logs/ftec5660/tutorial01_study_plan.md` rather than rereading the tax notebook line by line;
7. update `lesson_logs/ftec5660/course_context.md` only when a cross-lecture synthesis thread materially changes.

For historical maths, choose the smallest relevant log rather than loading the whole subject. For broad rebuilds, follow that subject's logs in order.

Probability/statistics has an explicit evidence boundary: Markov chains and Poisson are remembered historical study but do **not** yet have the worked trail needed to claim demonstrated mastery. Treat their next use as a cold diagnostic and update the record from new evidence.

For current study direction, do **not** infer priority from this index. Read `LEARNING_STATE.md` first, then `MSC_SYLLABUS_MAP.md`, with `LEARNING_ROADMAP.md` for longer-term choices.
