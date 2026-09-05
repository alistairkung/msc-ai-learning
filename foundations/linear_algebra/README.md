# Linear algebra foundations — historical JHU sequence

This directory records the linear-algebra foundation learned through the Johns Hopkins Coursera **Linear Algebra from Elementary to Advanced** specialization in 2025, before the repository's numbered lesson workflow existed.

The specialization was completed before the MSc and is treated here as **established historical learning with retrieval decay**, not as new/developing material. The purpose of this directory is to make that foundation recoverable when a later MSc topic needs it.

These sessions are intentionally **not retroactively assigned numbered lessons**. Lessons 01–31 describe the repository's implementation chronology; inventing earlier lesson numbers would distort that history.

## Durable retrieval records

The historical sequence is split into four focused lesson logs:

1. `lesson_logs/historical_linear_algebra_01_linear_systems_vector_spaces.md`
   - linear systems, elimination/RREF, pivots/free variables, parametric/vector solutions, span, independence, basis and subspaces;
2. `lesson_logs/historical_linear_algebra_02_matrices_eigenvalues_diagonalization.md`
   - matrix algebra, determinants, eigenvalues/eigenvectors/eigenspaces and diagonalization;
3. `lesson_logs/historical_linear_algebra_03_orthogonality_projections_least_squares.md`
   - orthogonality, orthonormal bases, Gram–Schmidt, projections, residuals and least squares;
4. `lesson_logs/historical_linear_algebra_04_symmetric_quadratic_forms.md`
   - symmetric matrices, orthogonal diagonalization, orthogonal matrices and quadratic forms.

## Reconstructed learning arc

```text
linear systems
→ elimination / RREF
→ pivot + free variables
→ parametric vector form
→ span / independence / basis / subspaces
→ matrix algebra + determinants
→ eigenvalues / eigenvectors / eigenspaces
→ diagonalization
→ orthogonality / orthonormal bases
→ Gram–Schmidt
→ orthogonal projection + residual
→ least squares / normal equations
→ symmetric matrices
→ orthogonal diagonalization
→ quadratic forms
```

## Why this matters for the MSc

This is not a separate maths curriculum to restart from zero. It is a reusable prerequisite layer for:

- AIMS5702 vector/matrix/tensor operations;
- linear and logistic models;
- least-squares/regression geometry;
- neural-network shape reasoning;
- covariance/PCA/SVD intuition when encountered;
- AIMS5704 Machine Learning Theory, which explicitly assumes linear algebra;
- later optimisation, kernels, Gram matrices and quadratic-form reasoning.

## Retrieval policy

Normal use should be **cold retrieval first**, not rereading.

A tutor/model should:

1. choose the relevant historical log;
2. ask one small question at a time;
3. change numbers/examples from the historical work;
4. distinguish arithmetic slips from conceptual gaps;
5. probe the recorded fragile points;
6. stop once retention is clear.

A 10–15 minute retrieval is enough for ordinary maintenance. If familiarity has materially decayed, use the log's rebuild sequence to reconstruct the topic in layers rather than replaying the entire JHU course.

## Evidence boundary

This is a conservative historical reconstruction from recoverable tutoring context, later learning records and demonstrated cold-retrieval work. It is **not a transcript** and should not be treated as evidence that every topic in the full Coursera specialization was discussed in chat or retained equally well.

No exercise/test pair is fabricated for the historical JHU material because the original work was primarily conversational and pen-and-paper. Later NumPy, regression, tensor and PyTorch lessons provide executable evidence for many downstream applications of the same linear-algebra ideas.
