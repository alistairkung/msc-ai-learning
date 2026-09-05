# Historical linear algebra 02 — matrices, eigenvalues and diagonalization

**Status:** Historical reconstruction  
**Period:** JHU Coursera linear algebra preparation, 2025  
**Format at the time:** Interactive chat + pen-and-paper rather than a repository exercise/test pair

## Learning objective

Understand matrices as linear transformations, use determinants as structural information, then identify the special directions preserved by a transformation through eigenvalues/eigenvectors and use those directions to diagonalize a matrix.

## Reconstructed progression

### 1. Matrix algebra and transformations

Matrix multiplication was treated as composition/application of linear transformations rather than only a symbol-manipulation rule.

Shape compatibility matters:

```text
(m × n)(n × p) → (m × p)
```

The columns of a matrix are also the images of the standard basis vectors, which later supports column-space and transformation reasoning.

### 2. Determinants

For a 2×2 matrix:

```text
det([[a,b],[c,d]]) = ad - bc
```

The determinant was used as a test for invertibility (`det(A) != 0`) and as a geometric volume/area scaling factor.

A recurring arithmetic trap was the sign on the second product. For example, with off-diagonal entries `-2` and `-2`, their product is `+4`, but the determinant still subtracts that product.

### 3. Characteristic equation and eigenvalues

Eigenvalues solve:

```text
det(A - λI) = 0
```

For 2×2 matrices, useful checks are:

```text
sum of eigenvalues = trace(A)
product of eigenvalues = det(A)
```

These checks are especially useful for catching sign/expansion slips before continuing.

### 4. Eigenvectors and eigenspaces

For each eigenvalue `λ`, solve:

```text
(A - λI)v = 0
```

So the eigenvectors form the null space of `A - λI` (excluding the zero vector itself as an eigenvector).

The key geometric idea is:

> An eigenvector is a direction that the transformation does not turn away from itself; the eigenvalue is the scale factor along that direction.

### 5. Eigenvector scaling and sign

If `v` is an eigenvector, then any nonzero scalar multiple `cv` is an eigenvector for the same eigenvalue.

A historical example made this explicit: `[-1, 2]` and `[1, -2]` describe the same eigendirection. A sign difference from an MCQ answer is therefore not automatically an error.

### 6. Eigenbasis

If enough linearly independent eigenvectors exist to form a basis, they can be used as the columns of a change-of-basis matrix `P`.

The order matters only in the sense that it must stay consistent with the diagonal matrix.

Example structure:

```text
P = [v1 v2]
D = diag(λ1, λ2)
```

If the columns of `P` are reversed, the corresponding eigenvalues in `D` must also be reversed.

### 7. Diagonalization

For a diagonalizable matrix:

```text
A = P D P^-1
```

Equivalently:

```text
A P = P D
```

The second identity is often the easiest conceptual explanation: applying `A` to each column eigenvector simply multiplies it by its matching eigenvalue.

The diagonal entries of `D` are therefore not independently computed from the eigenbasis; they are the eigenvalues corresponding to the columns of `P`.

## What was understood well

The learner developed good geometric intuition for eigenvectors as invariant directions and remembered the basic diagonalization recipe:

1. find eigenvalues;
2. find null spaces of `A - λI` to obtain eigenvectors;
3. place independent eigenvectors in `P`;
4. put matching eigenvalues in `D`;
5. use `A = P D P^-1`.

The learner also correctly recognised that normalization belongs specifically to **orthogonal diagonalization**, not ordinary diagonalization.

## Known fragile points

1. **Determinant sign errors** during characteristic-polynomial expansion.
2. **Eigenvalue sanity checks** — use trace/product to catch slips.
3. **Eigenvector sign/scaling** — scalar multiples are equivalent eigendirections.
4. **Ordering** — columns of `P` and entries of `D` must correspond.
5. **Diagonalization vs least squares** — both involve matrix algebra but solve completely different problems; eigenvalues/eigenvectors are not part of the normal least-squares procedure.
6. **Normalization** — optional for ordinary diagonalization; required when constructing an orthonormal eigenbasis for orthogonal diagonalization.

## Cold-retrieval blueprint

1. Give a 2×2 matrix and ask for its characteristic polynomial.
2. Before solving it, ask for trace and determinant as future eigenvalue checks.
3. Find the eigenvalues.
4. For one eigenvalue, solve the null space of `A - λI`.
5. Ask whether a sign-flipped/scaled proposed eigenvector is also valid and why.
6. Construct `P` and `D`, explicitly checking their ordering.
7. Ask what `A = P D P^-1` means geometrically.
8. Give a reversed eigenbasis and ask how `D` changes.

## Rebuild sequence if cold recall is weak

```text
determinant
→ characteristic equation
→ eigenvalues
→ null(A - λI)
→ eigendirections
→ eigenbasis
→ D from matching eigenvalues
→ A = P D P^-1
```

## Mastery signal

The learner can calculate eigenvalues/eigenvectors for a small matrix, use trace/determinant checks, recognise scalar-equivalent eigenvectors, assemble a consistent `P` and `D`, and explain diagonalization as expressing the transformation in its eigenbasis.

## Bridge forward

```text
eigenbasis + diagonalization
→ symmetric matrices
→ orthogonal eigenbasis
→ Q^-1 = Q^T
→ quadratic forms / spectral geometry
```
