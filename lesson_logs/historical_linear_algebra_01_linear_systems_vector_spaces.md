# Historical linear algebra 01 — linear systems and vector spaces

**Status:** Historical reconstruction  
**Period:** JHU Coursera linear algebra preparation, 2025  
**Format at the time:** Interactive chat + pen-and-paper rather than a repository exercise/test pair

## Why this record exists

The first part of the JHU sequence built the language needed to reason about systems, solution sets and vector spaces. This predates the numbered repository workflow, so this log preserves the conceptual/retrieval spine without inventing lesson numbers or implementation evidence.

## Learning objective

Move from solving individual systems of equations to understanding the geometry and structure of their solution sets: pivots, free variables, span, linear independence, bases and subspaces.

## Reconstructed progression

### 1. Linear systems and augmented matrices

Systems of equations were represented as augmented matrices and solved with elementary row operations.

The key distinction that needed reinforcement was:

- **row echelon form**: pivots step to the right and entries below pivots are zero;
- **reduced row echelon form (RREF)**: pivot entries are 1 and are the only nonzero entries in their columns.

A historical fragile point was stopping once echelon form had been reached and forgetting to clear entries **above** pivots when RREF was required.

### 2. Pivot and free variables

Once a matrix is reduced, pivot columns determine basic variables while non-pivot columns correspond to free variables.

A system with free variables does not have one isolated solution. Its solutions form a family parameterised by one or more free variables.

### 3. Parametric/vector form

A representative historical solution took the form:

```text
(x1, x2, x3) = (-4 - x3, -1 + x3, x3)
```

The important conceptual move was to let the free variable be a parameter, for example `x3 = t`, then separate the solution into:

```text
particular solution + t * direction vector
```

For the example above:

```text
[-4, -1, 0] + t[-1, 1, 1]
```

The learner initially found the algebraic factoring into this geometric form less obvious than solving the equations themselves. Future retrieval should therefore test the conversion explicitly.

### 4. Span and membership

Span was learned as the set of all linear combinations of a collection of vectors.

To test whether a vector belongs to a span, set up coefficients and solve:

```text
a v1 + b v2 + ... = target
```

If the resulting system is consistent, the target lies in the span.

### 5. Linear independence

A set of vectors is linearly independent if the only way to make the zero vector is the trivial combination where every coefficient is zero.

Operationally, independence is tied to pivots/free variables when the vectors are arranged as matrix columns.

### 6. Basis and dimension

A basis combines two conditions:

- the vectors span the space/subspace;
- the vectors are linearly independent.

Dimension is the number of vectors in a basis.

The useful mental shift is that a basis is not a unique set of vectors. Many different bases can describe the same subspace.

### 7. Subspaces

Subspaces are subsets of a vector space that remain closed under vector addition and scalar multiplication and contain the zero vector.

This became important later because column spaces, null spaces and eigenspaces are all subspaces.

## What was understood well

The learner could perform row operations and solve systems, identify free-variable structure, reason about span membership and work with basis/independence ideas once the matrix representation was clear.

The strongest intuition came from connecting algebraic manipulations to what the solution set **is geometrically**, rather than treating RREF as an isolated procedure.

## Known fragile points

1. **Echelon vs RREF** — do not stop before clearing above pivots when reduced form is required.
2. **Free-variable interpretation** — a free variable means a family of solutions, not a missing final calculation.
3. **Parametric vector form** — separate constants from the parameter coefficient correctly.
4. **Span vs independence** — spanning a space does not automatically mean the set is independent.
5. **Basis** — must satisfy both span and independence.

Arithmetic slips should not be treated as conceptual failure unless the structural reasoning is also missing.

## Cold-retrieval blueprint

Normal review: roughly 10–15 minutes, one question at a time.

1. Reduce a small 2×3 or 3×4 augmented matrix and ask whether the result is echelon or RREF.
2. Identify pivot and free variables.
3. Convert a system with one free variable into parametric vector form.
4. Given two or three vectors and a target, decide whether the target is in their span by setting up a system.
5. Ask what linear independence means without using the phrase “not dependent”.
6. Given a spanning set with a redundant vector, ask whether it is a basis and why.
7. Ask for the relationship among column space, span and matrix columns at an intuitive level.

Change all numbers from the historical examples.

## Rebuild sequence if cold recall is weak

```text
solve one system
→ identify pivots/free variables
→ write parametric solution
→ rewrite as point + directions
→ use same system idea for span membership
→ connect pivots/free variables to independence
→ define basis = span + independence
```

Do not restart with abstract definitions if the procedural/geometric bridge is missing; rebuild from a concrete system.

## Mastery signal

Treat this foundation as retrieved when the learner can reduce a small system accurately; distinguish echelon from RREF; identify pivot/free variables; produce parametric vector form; test span membership; and explain basis as an independent spanning set.

## Bridge forward

```text
systems + solution sets
→ matrix algebra / transformations
→ null space and column space
→ eigenvectors/eigenspaces
→ orthogonality and least squares
```
