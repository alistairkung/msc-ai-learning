# Historical linear algebra 04 — symmetric matrices and quadratic forms

**Status:** Historical reconstruction  
**Period:** JHU Coursera linear algebra preparation, 2025  
**Format at the time:** Interactive chat + pen-and-paper rather than a repository exercise/test pair

## Learning objective

Connect diagonalization to the special structure of real symmetric matrices, then use quadratic forms to translate that matrix structure into scalar geometry relevant to optimisation, statistics and machine learning.

## Reconstructed progression

### 1. Symmetric matrices

A real square matrix is symmetric when:

```text
A = A^T
```

The important payoff is the spectral theorem: real symmetric matrices have real eigenvalues and admit an orthonormal eigenbasis.

So a symmetric matrix can be orthogonally diagonalized:

```text
A = Q D Q^T
```

where the columns of `Q` are orthonormal eigenvectors and `D` contains the matching eigenvalues.

### 2. Orthogonal diagonalization

The ordinary diagonalization workflow still applies:

1. find eigenvalues;
2. find eigenvectors from `null(A - λI)`;
3. match eigenvectors to eigenvalues.

For a symmetric matrix, normalize the eigenvectors and arrange them as columns of `Q`.

Because `Q` is orthogonal:

```text
Q^-1 = Q^T
```

This is the practical simplification over a general `P D P^-1` decomposition.

A historical example used:

```text
A = [[1,-5],[-5,1]]
```

with eigenvectors proportional to `[-1,1]` and `[1,1]`, and eigenvalues `6` and `-4`. The corresponding diagonal entries must follow the same order as the chosen eigenvector columns.

### 3. Orthogonal matrices

The defining test is:

```text
Q^T Q = I
```

Equivalently, the columns form an orthonormal basis.

For a real orthogonal matrix:

```text
det(Q) = ±1
```

But the converse is false: determinant `±1` is **necessary, not sufficient**, for orthogonality. A matrix can preserve volume while still shearing or stretching one direction and compressing another.

So determinant alone is not an orthogonality test.

### 4. Symmetry and orthogonal diagonalizability

For real matrices:

```text
A is symmetric  ⇔  A is orthogonally diagonalizable
```

This is a stronger statement than simply saying distinct eigenspaces happen to be orthogonal. The useful exam/test shortcut is: if a real matrix is visibly symmetric, orthogonal diagonalization is guaranteed.

### 5. Quadratic forms

A quadratic form has the structure:

```text
Q(x) = x^T A x
```

For a vector `x`, the result is a scalar.

A reliable hand-calculation route is:

```text
1. compute Ax
2. compute x^T(Ax)
```

A historical example used:

```text
A = [[0,2,1],
     [2,1,0],
     [1,0,-1]]
x = [2,-1,1]^T
```

giving `Ax = [-1,3,1]^T` and therefore `Q(x) = -4`.

Again, future retrieval should change the numbers.

### 6. Cross terms and the symmetric matrix representation

For a symmetric 3×3 matrix, the expanded quadratic form is:

```text
Q(x) = a11 x1^2 + a22 x2^2 + a33 x3^2
     + 2a12 x1x2 + 2a13 x1x3 + 2a23 x2x3
```

The factor of 2 appears because an off-diagonal contribution occurs twice in `x^T A x`.

So if the polynomial contains:

```text
-6 x1 x3
```

then:

```text
a13 = a31 = -3
```

This coefficient-splitting rule was an explicit point of retrieval.

### 7. Why diagonalization helps quadratic forms

If `A = Q D Q^T` and `y = Q^T x`, then:

```text
x^T A x = y^T D y
```

The cross terms disappear in the eigenbasis:

```text
λ1 y1^2 + λ2 y2^2 + ...
```

This makes the geometry of the quadratic form visible through the eigenvalues.

### 8. ML-relevant interpretation

The later purpose is not to become fast at arbitrary quadratic-form algebra. These ideas can later support:

- curvature/Hessian reasoning in optimisation;
- positive definite / semidefinite matrices;
- covariance and variance in directions;
- PCA/eigenvector intuition;
- Gram matrices and kernel methods;
- quadratic loss geometry.

These are **future applications/extensions**, not automatic retrieval expectations from this historical block unless separately evidenced or taught.

## What was understood well

The learner remembered the diagonalization workflow, quickly understood why symmetry makes `P^-1` become `Q^T`, and connected orthogonal diagonalization to eigenvector normalization.

The quadratic-form computation `x^T A x` and the off-diagonal cross-term rule became clear once written as explicit matrix multiplication rather than memorised polynomial bookkeeping.

## Known fragile points

1. **Symmetric vs merely square** — orthogonal diagonalization requires real symmetry.
2. **Normalize the eigenvectors** when constructing `Q`; normalization is not generally required for ordinary `P D P^-1` diagonalization.
3. **Column/eigenvalue ordering** must remain matched in `Q` and `D`.
4. **`det(Q)=±1` is not a sufficient orthogonality test**; check `Q^TQ=I`.
5. **Quadratic-form cross terms** — halve the polynomial coefficient when placing it symmetrically off diagonal.
6. **Matrix multiplication order** — compute `Ax`, then dot with `x`, rather than treating `x^T A x` as three unrelated objects.

## Cold-retrieval blueprint

1. Give several small matrices and ask which are symmetric.
2. Ask what symmetry guarantees about eigenvalues/eigenvectors.
3. Orthogonally diagonalize one 2×2 symmetric matrix.
4. Ask why `Q^-1 = Q^T` and what must be true of `Q`.
5. Give a matrix with determinant 1 that is not orthogonal and ask why determinant alone fails.
6. Compute one quadratic form using `Ax` then `x^T(Ax)`.
7. Convert a polynomial quadratic form into its symmetric matrix representation, including one cross term.
8. Ask what diagonalizing the symmetric matrix does to the cross terms.

## Rebuild sequence if cold recall is weak

```text
ordinary diagonalization
→ symmetric matrix
→ orthogonal eigenvectors
→ normalize → Q
→ Q^-1 = Q^T
→ A = Q D Q^T
→ x^T A x
→ cross-term matrix representation
→ change into eigenbasis
```

## Future extension — not part of historical retrieval mastery

When later ML Theory or optimisation work actually introduces it, connect the eigenvalue signs of a symmetric quadratic form to positive-definite/semidefinite reasoning and curvature. Until then, do not use that extension to judge retrieval of this historical lesson.

## Mastery signal

The learner can identify symmetry, explain the spectral-theorem consequence at an intuitive level, construct a small orthogonal diagonalization, correctly distinguish determinant ±1 from true orthogonality, evaluate `x^T A x`, and reconstruct the symmetric matrix from quadratic cross terms.

## Bridge forward

```text
symmetric matrices + quadratic forms
→ future: positive definite / semidefinite reasoning
→ covariance / PCA intuition
→ Hessian / optimisation curvature
→ kernels / Gram matrices
→ AIMS5704 mathematical foundations
```
