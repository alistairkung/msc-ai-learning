# Lesson Log Index

_Last audited: 2026-09-05_

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

See `historical_calculus_foundations.md`, `foundations/calculus/README.md`, the four `historical_linear_algebra_*.md` logs and `foundations/linear_algebra/README.md`.

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

For “cold retrieve calculus foundations”, use `historical_calculus_foundations.md` in the same way.

For linear algebra, choose the smallest relevant historical log rather than loading the entire subject. For a broad refresh, follow the four logs in order. There is no historical exercise/test pair because the original JHU work was primarily conversational and pen-and-paper.

For current study direction, do **not** infer priority from this index. Read `LEARNING_STATE.md` first, then `MSC_SYLLABUS_MAP.md`, with `LEARNING_ROADMAP.md` for longer-term choices.
