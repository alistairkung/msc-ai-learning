# Historical linear algebra 03 — orthogonality, projections and least squares

**Status:** Historical reconstruction  
**Period:** JHU Coursera linear algebra preparation, 2025  
**Format at the time:** Interactive chat + pen-and-paper rather than a repository exercise/test pair

## Learning objective

Build the geometry of perpendicular directions and orthogonal bases, then use that geometry to understand projection and least squares as the problem of finding the closest point in a subspace.

## Reconstructed progression

### 1. Orthogonality and orthonormality

Two vectors are orthogonal when their dot product is zero:

```text
u · v = 0
```

An orthogonal set becomes orthonormal when every vector is also normalized to length 1.

Normalization changes magnitude, not direction:

```text
u_hat = u / ||u||
```

### 2. Projection onto a line

For a nonzero vector `u`, the projection of `y` onto `span{u}` is:

```text
proj_u(y) = (y·u / u·u) u
```

The coefficient answers how much of `y` lies in the `u` direction.

### 3. Projection onto a subspace with an orthogonal basis

If `W` has an orthogonal basis `{u1, ..., up}`:

```text
y* = Σ (y·ui / ui·ui) ui
```

The projection `y*` lies in `W`.

The residual is:

```text
z = y - y*
```

and satisfies:

```text
z ⟂ W
```

That means `z` has dot product zero with every vector in the subspace. Geometrically, `y*` is the foot of the perpendicular dropped from `y` to the plane/subspace.

### 4. Exact residual vs scaled direction

A useful historical distinction:

- multiplying `z` by a nonzero scalar preserves its **direction** and therefore its perpendicularity;
- but the decomposition `y = y* + z` requires the **exact** residual with the correct magnitude.

So a scaled vector can still be normal to the plane while no longer being the actual displacement from `y*` to `y`.

### 5. Gram–Schmidt

Gram–Schmidt converts a spanning set into an orthogonal one spanning the same subspace.

```text
u1 = v1
u2 = v2 - proj_u1(v2)
u3 = v3 - proj_u1(v3) - proj_u2(v3)
...
```

The conceptual rule is:

> For each new vector, subtract all components lying in directions already kept.

After orthogonalization, vectors may be rescaled by nonzero constants for cleaner arithmetic without losing orthogonality or changing the span.

If a new Gram–Schmidt vector becomes zero, the original vector was already in the span of the earlier ones; it does not add a new basis direction.

### 6. Why orthogonal bases help projections

For arbitrary non-orthogonal spanning vectors, projection coefficients interact with one another. With an orthogonal basis, each component can be calculated independently using dot products and added.

This was the practical motivation for learning Gram–Schmidt immediately after projection geometry.

### 7. Least squares as projection

When `Ax = b` has no exact solution, least squares chooses `x*` so that `Ax*` is the closest vector in `Col(A)` to `b`.

```text
b = Ax* + r
r = b - Ax*
r ⟂ Col(A)
```

Since `r` is orthogonal to every column of `A`:

```text
A^T r = 0
```

Substituting `r = b - Ax*` gives the normal equations:

```text
A^T A x* = A^T b
```

### 8. Solving the normal equations

Two equivalent routes were practised.

Solve the linear system directly:

```text
(A^T A)x* = A^T b
```

or, when `A^T A` is invertible:

```text
x* = (A^T A)^-1 A^T b
```

The inverse formula is not a separate least-squares method; it is one way of solving the same normal equations.

A worked historical regression-style example produced:

```text
x* = [2/3, 1/2]^T
```

and the residual was checked by verifying `A^T r = 0`.

Another cold-retrieval example used:

```text
A = [[1,3],
     [1,-1],
     [1,1]]
b = [4,2,0]^T
```

leading to:

```text
A^T A = [[3,3],[3,11]]
A^T b = [6,10]^T
x* = [3/2,1/2]^T
```

The value of the example is the procedure and geometry, not memorising these numbers.

## What was understood well

The learner formed a strong geometric model of projection as dropping a perpendicular to a subspace and understood least squares as the same geometry applied to the column space of a matrix.

The learner could use Gram–Schmidt, projection formulas and normal equations after short retrieval, and could verify a least-squares result using residual orthogonality.

## Known fragile points

1. **Projection arithmetic** — carefully preserve the actual vector entries when computing dot products.
2. **Gram–Schmidt subtraction** — computing a projection is not yet the new basis vector; it must be subtracted from the original vector.
3. **Scaling during Gram–Schmidt** — safe for an orthogonal basis direction; keep later projection denominators consistent with the scaled vector.
4. **Residual scaling** — scaling preserves perpendicular direction but breaks the exact identity `y = y* + z`.
5. **Least squares vs diagonalization** — least squares uses normal equations, not eigenvalues/eigenvectors.
6. **`A^T b` arithmetic** — treat it as column-wise dot products with `b`.
7. **Normal equations vs inverse formula** — direct elimination and `(A^T A)^-1 A^T b` solve the same equation when the inverse exists.

## Cold-retrieval blueprint

A good 10–15 minute sequence:

1. Ask what projection onto a plane means geometrically before giving a formula.
2. Project a vector onto one line.
3. Given an orthogonal basis for a plane, project a vector onto the plane and calculate the residual.
4. Verify the residual is orthogonal to each basis vector.
5. Perform one Gram–Schmidt step, explicitly separating “projection” from “subtract projection”.
6. Ask what a zero Gram–Schmidt output would mean.
7. Given a small overdetermined `Ax=b`, construct `A^T A` and `A^T b`.
8. Solve the normal equations.
9. Calculate `r = b - Ax*` and verify `A^T r = 0`.
10. Ask in words why that orthogonality means the fit is closest.

## Rebuild sequence if cold recall is weak

```text
dot product → perpendicularity
→ projection onto one vector
→ projection onto orthogonal basis
→ residual perpendicular to subspace
→ Gram–Schmidt builds orthogonal basis
→ Col(A) as target subspace
→ least squares = project b onto Col(A)
→ A^T(b - Ax*) = 0
→ normal equations
```

This conceptual chain is more important than memorising the final formula in isolation.

## Mastery signal

The learner can explain projection geometrically, compute projection onto an orthogonal basis, form and interpret the exact residual, execute a small Gram–Schmidt problem, derive/recall the normal equations, solve a small least-squares system and verify residual orthogonality.

## Bridge forward

```text
orthogonal bases + projections
→ least-squares regression geometry
→ symmetric A^T A / Gram matrices
→ orthogonal diagonalization
→ PCA/SVD/kernel intuition when needed
```
