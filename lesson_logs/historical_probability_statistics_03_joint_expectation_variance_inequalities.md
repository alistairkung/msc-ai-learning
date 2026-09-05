# Historical probability/statistics 03 — joint distributions, expectation, covariance and inequalities

**Status:** Historical reconstruction with strong recoverable tutoring evidence  
**Period:** Late November 2025  
**Format at the time:** Interactive chat + Coursera study + Python notebook work

## Learning objective

Extend from one random variable to several, understand dependence through joint/marginal distributions and covariance/correlation, then use expectation and variance to reason about sums and probabilistic bounds.

## Reconstructed progression

### 1. Joint random variables

A concrete urn experiment was translated into Python.

Historical setup:

```text
3 red, 4 white, 5 blue balls
choose 3 without replacement
```

The elementary outcomes were physical-ball selections, so the total number of equally likely triples was:

```text
C(12, 3) = 220
```

A useful historical question was why the implementation enumerated **indices/physical balls** rather than only colour strings. The answer was that balls of the same colour are still distinct elementary objects in the combinatorial sample space.

Random variables such as:

```text
X = number of red balls drawn
Y = number of white balls drawn
```

were then used to build a joint PMF.

### 2. Joint and marginal distributions

A joint distribution describes probabilities of pairs `(X,Y)`.

Marginals are obtained by summing over the other variable:

```text
P(X=x) = Σ_y P(X=x, Y=y)
```

and similarly for `Y`.

This gave a computational bridge between raw outcome enumeration and abstract joint-distribution notation.

### 3. Linearity of expectation

A durable result:

```text
E[X + Y] = E[X] + E[Y]
```

and more generally:

```text
E[Σ Xi] = Σ E[Xi]
```

Importantly, **independence is not required** for linearity of expectation.

Indicator variables were a useful way to turn counting problems into sums of 0/1 random variables so expectation could be computed component-wise.

### 4. Variance as an expectation

A historical example used a random variable taking `+100` or `-100` with equal probability.

The learner asked why each squared deviation was multiplied by `1/2`. The repair was to reconnect variance to expectation:

```text
Var(X) = E[(X - E[X])^2]
```

so every possible squared deviation is weighted by the probability of that outcome.

### 5. Covariance

Covariance was introduced through:

```text
Cov(X,Y) = E[(X-E[X])(Y-E[Y])]
```

and the useful computational identity:

```text
Cov(X,Y) = E[XY] - E[X]E[Y]
```

Interpretation:

- positive covariance: variables tend to move together;
- negative covariance: they tend to move oppositely;
- near zero: little linear co-movement, though not necessarily independence.

Covariance depends on the variables' units/scales.

### 6. Correlation

Correlation normalizes covariance:

```text
ρ(X,Y) = Cov(X,Y) / (σX σY)
```

so it is dimensionless and constrained to `[-1,1]`.

A useful distinction was made between:

- Pearson correlation as the **strength/direction of linear association**;
- a significance test/p-value as a different question about evidence under a null hypothesis.

### 7. Markov inequality

For a non-negative random variable `X` and `a>0`:

```text
P(X ≥ a) ≤ E[X] / a
```

The conceptual use is to get a worst-case upper bound using only the mean and non-negativity.

### 8. Chebyshev inequality

Chebyshev uses mean and variance:

```text
P(|X-μ| ≥ kσ) ≤ 1/k^2
```

or equivalently:

```text
P(|X-μ| < kσ) ≥ 1 - 1/k^2
```

Recoverable drills included bounds such as `1/9`, `1/16` and complementary interval probabilities such as `8/9`.

The learner explicitly asked whether Chebyshev should always be tighter than Markov. The important answer is **no universal domination claim**: they use different assumptions/information and can be applied to different transformed variables/events.

## What was understood well

The learner was able to move between physical sample spaces, joint random-variable notation and Python enumeration, and developed good intuition for expectation as weighted averaging.

The dependence layer—joint/marginal distributions, covariance and correlation—became clearer when connected to concrete examples rather than formulas in isolation.

## Known fragile points

1. **Elementary outcomes with duplicate labels** — distinguish physical objects from colour/category labels.
2. **Marginalisation** — sum the joint PMF over the other variable.
3. **Linearity of expectation** — does not require independence.
4. **Variance weighting** — squared deviations are probability-weighted because variance is an expectation.
5. **Covariance vs correlation** — covariance has units/scale; correlation is normalized.
6. **Zero covariance vs independence** — not equivalent in general.
7. **Correlation vs significance** — effect/association size and evidence are different questions.
8. **Markov vs Chebyshev** — do not assume one mechanically supersedes the other.

## Cold-retrieval blueprint

1. Give a small urn/card/dice experiment and ask what the elementary outcomes are.
2. Define two random variables on the experiment and build a tiny joint table.
3. Recover one marginal by summing the joint probabilities.
4. Use linearity of expectation on a sum without assuming independence.
5. Calculate variance for a two- or three-value random variable, explicitly showing probability weights.
6. Compute covariance from `E[XY]-E[X]E[Y]` and interpret the sign.
7. Convert covariance to correlation and explain what normalization changes.
8. Apply Markov to a simple nonnegative-variable event.
9. Apply Chebyshev to a `kσ` interval/tail event and convert between tail and inside-interval forms.
10. Ask when the bounds are useful despite being loose.

## Rebuild sequence if cold recall is weak

```text
outcomes → two random variables
→ joint PMF
→ marginals
→ expectation of sums
→ indicators
→ variance as expectation
→ covariance → correlation
→ mean-only bound (Markov)
→ mean+variance bound (Chebyshev)
```

## Mastery signal

The learner can construct/interpret a small joint distribution, marginalize it, use linearity of expectation correctly, explain variance as a weighted expectation, distinguish covariance/correlation and apply/interpret simple Markov and Chebyshev bounds.

## Bridge forward

```text
expectation + variance + dependence
→ averages of many observations
→ sampling distributions
→ CLT / standard error
→ inference and hypothesis testing
```
