# Lesson Log Index

_Last audited: 2026-09-08_

This directory is the durable conceptual/retrieval record for the learning sequence. Exercise/test files are the implementation evidence; these logs explain what should be understood and how to cold-retrieve it later.

## Historical pre-repo learning

Some important learning happened interactively in chat before the numbered repository lesson workflow existed. These records are kept separately rather than being assigned invented lesson numbers.

| Record | Topic | Log status |
|---|---|---|
| Historical calculus foundations | Slope/local rate → limits/difference quotient → power/product rules → partial derivatives → gradients → gradient descent → chain rule/manual backprop | Reconstructed from recoverable tutoring context; bridges directly into Lesson 28 |
| Historical linear algebra 01 | Linear systems → RREF → pivots/free variables → parametric solutions → span/independence/basis/subspaces | Reconstructed from recoverable JHU tutoring context |
| Historical linear algebra 02 | Matrix algebra/determinants → eigenvalues/eigenvectors/eigenspaces → diagonalization | Reconstructed from recoverable JHU tutoring context |
| Historical linear algebra 03 | Orthogonality → projections → Gram–Schmidt → least squares/normal equations | Reconstructed from recoverable JHU tutoring context |
| Historical linear algebra 04 | Symmetric matrices → orthogonal diagonalization → orthogonal matrices → quadratic forms | Reconstructed from recoverable JHU tutoring context |
| Historical probability/statistics 01 | Counting/sample spaces → axioms → conditional probability → independence → total probability → Bayes | Strong recoverable JHU tutoring evidence |
| Historical probability/statistics 02 | Random variables → geometric distribution → expectation/variance → PDF/CDF → Uniform/Exponential/Normal | Strong recoverable JHU tutoring evidence |
| Historical probability/statistics 03 | Joint/marginal distributions → linearity/indicators → covariance/correlation → Markov/Chebyshev inequalities | Strong recoverable JHU tutoring + notebook evidence |
| Historical probability/statistics 04 | CLT → sampling distributions → standard error → hypothesis testing/p-values; Markov-chain/Poisson evidence boundary | Strong evidence for CLT/testing; Markov chains and Poisson recorded as historically studied but diagnostic-needed |

See the historical foundation directories under `foundations/` and the corresponding logs in this directory. Historical records are retrieval blueprints, not invented transcripts or fabricated exercise/test evidence.

## Live MSc course lecture records

Live lecture records are intentionally separate from the numbered implementation lessons. They can preserve lecturer material, course-level planning context and personal synthesis without inventing a numbered coding lesson.

| Record | Topic | Log status |
|---|---|---|
| `ftec5660_course_context.md` | FTEC5660 course spine, assessment/workload notes, personal learning lens, durable synthesis across lectures | Active course-level context; distinguish lecture-supported content from personal working hypotheses |
| `ftec5660_lecture01_introduction.md` | Agentic AI introduction: goal-directed systems, perceive/reason/act/escalate loop, pattern catalogue, complexity levels, multi-agent framing; plus SWE/finance reinterpretation | Original lecture + post-lecture synthesis log; introductory pattern catalogue is a reference map rather than a list-recall target |
| `ftec5660_pattern01_prompt_chaining.md` | Pattern 1 prompt chaining: decomposition, checkable stage interfaces, context engineering, trade-offs; LangChain/LCEL tutorial through successful JSON parsing | **Concept taught; tutorial partial.** Includes a bounded syntax-reconstruction plan for this week and explicitly excludes later notebook cells from current mastery |

For FTEC5660, future lecture/project logs should preserve the same source boundary: **what the lecturer/material supports** vs **my own synthesis or hypothesis**. Tutorial logs must also preserve the actual in-class stopping point: code appearing later in a supplied notebook is not automatically learned material.

## Numbered lesson coverage

All numbered lessons **01–31 now have a lesson log**.

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

“Reconstructed” means the available implementation evidence and recoverable tutoring context are used conservatively. These are not invented transcripts.

## Useful groupings

```text
Historical calculus  slope → derivative → differentiation rules → gradients → chain rule/backprop
Historical linear algebra  systems/vector spaces → matrices/eigen → orthogonality/least squares → symmetric/quadratic forms
Historical probability/statistics  counting/Bayes → random variables/distributions → joint moments/inequalities → CLT/inference
FTEC5660 live course  course material → pattern-focused logs → personal SWE/finance synthesis
01–07  Python language fluency
08–09  DSA patterns
10–17  NumPy / shape / manual ML + retrieval
18–20  pandas / data workflow
21–23  sklearn classical ML
24–26  classical search
27–30  tensors, autograd and PyTorch training
31     real-data PyTorch workflow (complete)
```

## How to use

For “cold retrieve Lesson N”:
1. read that lesson log;
2. inspect its exercise/test if needed;
3. ask one question at a time;
4. change numbers/context instead of repeating tests verbatim;
5. probe known fragile points;
6. stop once retention is clear.

For an FTEC5660 lecture/pattern:
1. read the relevant focused log;
2. cold-retrieve **course material** first;
3. sample only a few **personal-synthesis** prompts per session rather than replaying the whole discussion;
4. connect the concept to a familiar payments/KYC/AML example;
5. for code tutorials, quiz only syntax/mechanisms that the class or a later independent practice session actually reached;
6. update `ftec5660_course_context.md` only when a cross-lecture synthesis thread materially changes.

For historical maths, choose the smallest relevant log rather than loading the whole subject. For broad rebuilds, follow that subject's logs in order.

Probability/statistics has an explicit evidence boundary: Markov chains and Poisson are remembered historical study but do **not** yet have the worked trail needed to claim demonstrated mastery. Treat their next use as a cold diagnostic and update the record from new evidence.

For current study direction, do **not** infer priority from this index. Read `LEARNING_STATE.md` first, then `MSC_SYLLABUS_MAP.md`, with `LEARNING_ROADMAP.md` for longer-term choices.
