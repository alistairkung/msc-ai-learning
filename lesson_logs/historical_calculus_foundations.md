# Historical calculus foundations — retrieval blueprint

**Status:** Historical reconstruction  
**Period:** Pre-repository calculus preparation, culminating before Lesson 28  
**Format at the time:** Interactive chat + pen-and-paper rather than a repository exercise/test pair

## Why this record exists

The calculus foundation was learned before the repository's durable lesson workflow existed. As a result, later files correctly recorded that the concepts were understood, but the actual learning progression was missing from the lesson-log history.

This file backfills that progression conservatively. It is a **retrieval blueprint, not an invented transcript**.

## Learning objective

Build calculus from an intuitive idea of **change and local sensitivity** until the learner could understand gradients, gradient descent, chain rule and manual backpropagation well enough for those ideas to become executable in PyTorch autograd.

The emphasis was ML-relevant intuition rather than a broad traditional calculus syllabus.

## Reconstructed progression

### 1. Change and slope between two points

The sequence began with functions and change rather than derivative notation.

```text
slope = change in y / change in x
```

The learner first reasoned about the slope between two points on a curve, then confronted the problem that a curve does not have one constant slope.

### 2. Slope at a point and intuitive limits

The key conceptual move was to place a second point increasingly close to the target point and observe what happened to the secant slope. For `y = x²` at `x = 2`, increasingly close points were used to see the slope approach `4` as the gap shrank.

This established the derivative as the **local slope / local rate of change**, with limits introduced as the idea of what a quantity approaches rather than formal epsilon-delta analysis.

### 3. Difference quotient for `x²`

The intuition was connected to algebra through:

```text
((x + Δx)² - x²) / Δx
```

Expanding and simplifying gives `2x + Δx`, which approaches `2x` as `Δx → 0`.

This bridged “I can see the slope approaching something” to “a derivative rule can be derived rather than memorised.”

### 4. Power rule

```text
d/dx x^n = n x^(n-1)
```

Practice included ordinary positive powers and later negative/fractional powers. The intended mental model was that the rule is a compressed reusable result; the difference quotient explains why such a rule makes sense.

### 5. Product rule

```text
(uv)' = u'v + uv'
```

Practice involved identifying `u`, `u'`, `v`, `v'`, applying the rule, then expanding/simplifying polynomial expressions. A representative practice structure used `u = 2x² + 3` and `v = x³ - x`.

A useful observation was that **algebraic simplification could be shakier than the differentiation concept itself**. Arithmetic/algebra slips should not automatically be diagnosed as calculus misunderstanding.

### 6. Partial derivatives

The work moved from one-variable functions toward the multivariable setting needed for ML.

> When taking the partial derivative with respect to one variable, treat the other variables as constants.

This prepared the move from a single derivative to multiple local sensitivities of the same output/loss. Constant factors still need to be preserved when differentiating with respect to the active variable.

### 7. Gradients as local sensitivities

The gradient was introduced as the collection/vector of partial derivatives. For a scalar loss `L`, each component answers:

> If this parameter changes a tiny amount, how sensitive is the loss locally, and in which direction does it move?

“Local sensitivity” became an especially effective mental model and should be reused in future retrieval.

The learner understood the sign intuition: a positive derivative means increasing the parameter locally increases the output/loss; a negative derivative means it locally decreases it; magnitude indicates strength of local sensitivity.

### 8. Gradient descent

```text
parameter_new = parameter_old - learning_rate * gradient
```

The important reasoning was directional rather than merely formulaic: subtracting the gradient moves opposite the direction of local increase. This connected calculus directly to minimising an ML loss.

### 9. Chain rule and computation graphs

Nested functions introduced the need to propagate sensitivities through intermediate quantities. The chain rule was learned as multiplying local sensitivities along a dependency path rather than only as symbolic notation.

```text
x → intermediate → output/loss
```

To understand how the final output responds to `x`, combine the local sensitivities along that path. This became the conceptual foundation for backpropagation.

Derivative direction notation matters: e.g. `dz/dw` is not interchangeable with `dw/dz`.

### 10. Manual backpropagation → autograd

The culmination was understanding that backpropagation repeatedly applies the chain rule through a computation graph. That made Lesson 28 a continuation rather than a fresh start: PyTorch's `.backward()` automated a process already understood conceptually.

Lesson 28 then provided executable evidence for scalar autograd, multivariable gradients, `.backward()`, `.grad`, gradient accumulation/zeroing, manual gradient-descent updates, and manually parameterised linear-model training.

## What was understood well

By the bridge into autograd, the learner had demonstrated conceptual understanding of derivative as local slope/rate of change; why shrinking the gap leads to the derivative idea; power and product rules; partial derivatives; gradients as local sensitivities; gradient-descent direction; chain rule through nested dependencies; manual backpropagation as repeated chain rule; and why these ideas matter for ML optimisation.

## Known fragile points

1. **Derivative direction notation** — `dz/dw` versus `dw/dz` can be mixed up under pressure.
2. **Constant factors in partial derivatives** — preserve coefficients/constants multiplying the active variable's expression.
3. **Powers during substitution** — do not accidentally drop an exponent when substituting numerical values.
4. **Algebraic expansion/simplification** — polynomial arithmetic has sometimes been rustier than the calculus reasoning.
5. **Chain-rule fluency** — concept is understood, but short cold retrieval is useful so the mechanics remain automatic.

Do not classify a simple arithmetic or expansion slip as a conceptual calculus failure without probing the underlying reasoning.

## Cold-retrieval blueprint

Normal review should be interactive and roughly 10–15 minutes. Ask **one question at a time** and do not begin with a summary.

A useful progression:

1. Give two points on a simple function and ask for the slope between them.
2. Ask what must change if we want the slope *at* one point.
3. Use a changed function/value and ask what a derivative means in words before calculating it.
4. Ask for a simple power-rule derivative.
5. Give a product of two simple functions and ask for `u`, `u'`, `v`, `v'` before differentiating.
6. Give a two-variable scalar function and ask for each partial derivative.
7. Ask what the resulting gradient means rather than only its components.
8. Give a parameter value, gradient sign and learning rate and ask which way gradient descent moves and why.
9. Give a tiny computation graph such as `x → u → L` and ask for the sensitivity of `L` to `x` from local sensitivities.
10. Ask how that manual calculation relates to PyTorch `.backward()`.

Change numbers/functions from the historical examples. The goal is conceptual retrieval, not remembered arithmetic.

Useful diagnostics include: “What does `dL/dw` mean in plain English?”, “If `dL/dw` is positive, why does gradient descent subtract it?”, “When taking `∂L/∂x`, what happens to `y`?”, “Why can't we multiply arbitrary derivatives in either direction?”, and “What exactly is PyTorch automating when we call `.backward()`?”

## Mastery signal

Treat this foundation as **established but retrieval-worthy**, not permanently mastered because it was once understood.

A strong cold-retrieval signal is that the learner can explain derivative and gradient semantically; correctly differentiate simple powers/products; compute simple partial derivatives; trace a short chain-rule path with correct derivative direction; explain the gradient-descent sign/update; connect manual chain rule to backprop/autograd; and recover from arithmetic slips without needing the concept re-taught.

## Bridge forward

```text
Historical calculus foundations
    ↓
Lesson 28 — PyTorch autograd + manual gradient descent
    ↓
Lesson 29 — nn.Linear + MSELoss + SGD
    ↓
Lesson 30 — MLP binary classification
    ↓
Lesson 31 — real-data train/validation/test workflow
```

Future calculus expansion should be driven by ML need. Useful later extensions already identified in the roadmap include logs/exponentials, vector-valued derivatives/Jacobian intuition, curvature/second derivatives, and optimisation/convergence reasoning. These are **future work**, not claims about what the historical sessions completed.
