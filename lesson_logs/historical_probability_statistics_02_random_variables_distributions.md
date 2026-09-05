# Historical probability/statistics 02 — random variables and distributions

**Status:** Historical reconstruction with strong recoverable tutoring evidence  
**Period:** Mid November 2025  
**Format at the time:** Interactive chat + Coursera study + pen-and-paper/notebook work

## Learning objective

Move from probabilities of named events to **random variables** and probability distributions, then understand expectation/variance and the discrete-to-continuous transition through PMFs, PDFs and CDFs.

## Reconstructed progression

### 1. Random variables

A random variable was treated as a numerical mapping from outcomes to values rather than as “a variable that randomly changes.”

This shift allows a probability experiment to be summarized and analysed through the distribution of a numerical quantity of interest.

### 2. Discrete distributions and geometric waiting time

A representative discrete topic was the geometric distribution:

```text
P(X = n) = (1-p)^(n-1) p
```

A specific historical question was why the exponent is `n-1` rather than `n`.

The key reasoning:

> If the first success occurs on trial `n`, then there must be exactly `n-1` failures before the success on trial `n`.

This is a good retrieval point because it tests whether the formula can be reconstructed from the event structure rather than recalled mechanically.

### 3. Expectation

Expectation was learned as a probability-weighted average:

```text
E[X] = Σ x p(x)
```

for a discrete random variable, with the continuous analogue using integration.

The important intuition is **long-run/average value under the distribution**, not necessarily a value the random variable itself can actually take.

### 4. Variance

Variance measures expected squared deviation from the mean:

```text
Var(X) = E[(X - E[X])^2]
```

and equivalently:

```text
Var(X) = E[X^2] - E[X]^2
```

The probability weighting in the expectation remained an important recurring intuition later in the advanced course.

### 5. Continuous random variables

For continuous random variables, probability is associated with **area under a density curve**, not the height at one exact point.

For a continuous distribution:

```text
P(X = x) = 0
```

for any single exact point under the usual continuous model, while interval probabilities come from integration.

### 6. PDF vs CDF

A durable conceptual distinction was:

```text
PDF f(x) = local density / height
CDF F(x) = P(X ≤ x) = accumulated probability up to x
```

with:

```text
F(x) = ∫[-∞ to x] f(t) dt
f(x) = F'(x)
```

The learner explicitly worked through the difference between “density” and actual probability. A PDF value can exceed 1 as long as the total integrated area is 1; it is not itself the probability of the exact point.

### 7. Common distributions

Recoverable study included:

- **Uniform** — equal density across an interval;
- **Exponential** — continuous waiting-time distribution and memoryless intuition;
- **Normal** — bell-shaped distribution parameterised by mean and variance/standard deviation.

The goal was to recognise the modelling story and core parameters, not memorize every distribution identity.

## What was understood well

The learner developed a good bridge from event probability to distributional thinking and could interpret expectation and variance conceptually.

The PDF/CDF distinction became substantially clearer once expressed as **height/density versus accumulated area**.

## Known fragile points

1. **Geometric `n-1`** — reconstruct the preceding failures rather than memorising the exponent.
2. **Expectation weighting** — every possible value is weighted by its probability/density.
3. **PDF value vs probability** — density at a point is not point probability.
4. **CDF direction** — `F(x)` accumulates from the left up to `x`.
5. **Variance vs standard deviation** — variance is in squared units; standard deviation returns to the original units.
6. **Distribution recognition** — focus on the generative/waiting-time story rather than keyword matching.

## Cold-retrieval blueprint

1. Define a random variable for a simple experiment.
2. Given a geometric waiting-time question, derive the probability from the required failure/success sequence.
3. Compute expectation for a small discrete distribution.
4. Compute or interpret variance for a tiny distribution.
5. Ask what a PDF value means and whether it is itself a probability.
6. Convert a simple PDF into an interval probability conceptually using area.
7. Ask what the CDF represents before calculating one value.
8. Give short scenarios and choose among Uniform, Exponential and Normal with justification.

## Rebuild sequence if cold recall is weak

```text
outcomes/events
→ random variable maps outcomes to numbers
→ distribution assigns probability across values
→ expectation = weighted centre
→ variance = weighted squared spread
→ continuous values require density/area
→ PDF vs CDF
→ common distribution stories
```

## Mastery signal

The learner can define a random variable, reason through a geometric waiting-time probability, calculate/interpret expectation and variance, distinguish PDF from CDF and explain the basic modelling role of Uniform/Exponential/Normal distributions.

## Bridge forward

```text
single-variable distributions
→ joint distributions
→ marginals / dependence
→ covariance / correlation
→ sampling distributions / CLT
```
