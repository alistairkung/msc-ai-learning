# Historical probability/statistics 01 — counting, conditional probability and Bayes

**Status:** Historical reconstruction with strong recoverable tutoring evidence  
**Period:** Early November 2025  
**Format at the time:** Interactive chat + Coursera study + pen-and-paper/notebook work

## Learning objective

Build probability from sample spaces and counting into conditional probability, independence, the law of total probability and Bayes' theorem.

## Reconstructed progression

### 1. Counting and sample spaces

The sequence began with counting/combinatorics as a way to enumerate possible outcomes before assigning probabilities.

Useful structures included combinations and reasoning about equally likely sample-space outcomes.

This later mattered when physical objects could be distinct even if their labels/colours matched: counting outcomes correctly requires deciding what the elementary outcomes actually are.

### 2. Probability axioms

The Kolmogorov-style foundation was introduced conceptually:

- probabilities are non-negative;
- the entire sample space has probability 1;
- disjoint event probabilities add.

These axioms were used as the base layer beneath later formulas rather than as proof-heavy formalism.

### 3. Conditional probability

```text
P(A | B) = P(A ∩ B) / P(B)
```

The key conceptual question is:

> Once we know B happened, what fraction of the remaining B-world also satisfies A?

Conditional probability changes the effective sample space.

### 4. Independence

Independent events satisfy:

```text
P(A ∩ B) = P(A)P(B)
```

or equivalently (when conditioning is defined):

```text
P(A | B) = P(A)
```

The important distinction was that **disjoint** and **independent** are not synonyms. Mutually exclusive non-impossible events are generally not independent because learning one occurred tells us the other did not.

### 5. Law of total probability

When outcomes can arise through several mutually exclusive cases, probability can be assembled across those routes:

```text
P(B) = Σ P(B | Ai)P(Ai)
```

This became the denominator-building tool that made Bayes' theorem intuitive rather than magical.

### 6. Bayes' theorem

```text
P(A | B) = P(B | A)P(A) / P(B)
```

A particularly useful historical example was a medical test with low disease prevalence.

The learner correctly calculated the joint true-positive probability:

```text
P(D ∩ +) = P(D)P(+ | D)
```

but initially treated this as though it were already the posterior `P(D | +)`.

The key repair was:

> The numerator is the positive tests coming from people with the disease. The denominator must include **all positive tests**, including false positives.

This made base-rate effects concrete: a highly sensitive test can still have a surprisingly low posterior probability when the condition is rare and false positives are not negligible.

## What was understood well

The learner became comfortable building probability problems from events and conditioning rather than reaching immediately for memorised formulas.

Bayes became much clearer once the denominator was constructed using total probability and interpreted as “all ways the observed evidence could have happened.”

## Known fragile points

1. **Joint vs conditional/posterior probability** — `P(A ∩ B)` is not `P(A | B)`.
2. **Bayes denominator** — include every route that produces the observed evidence.
3. **Base rates** — do not ignore the prior prevalence/probability.
4. **Independence vs disjointness** — conceptually different relationships.
5. **Counting elementary outcomes** — define what counts as distinct before applying combinations/permutations.

## Cold-retrieval blueprint

1. Give a small finite sample-space/counting problem and ask how many elementary outcomes exist.
2. Ask for `P(A | B)` from a simple table or set of counts.
3. Ask whether two events are independent, requiring justification via probabilities.
4. Give a two-source total-probability problem.
5. Give a low-prevalence diagnostic-test Bayes problem with changed numbers.
6. Pause after the learner computes the numerator and ask: “What exactly have you calculated?”
7. Ask why the posterior can be much lower than the sensitivity.

## Rebuild sequence if cold recall is weak

```text
sample space + counting
→ event probability
→ intersection
→ conditioning shrinks the reference set
→ independence
→ total probability across cases
→ Bayes reverses the conditioning direction
```

## Mastery signal

The learner can distinguish joint and conditional probabilities, test independence, construct a total-probability denominator and solve/explain a Bayes problem in plain English without relying on formula recognition alone.

## Bridge forward

```text
events + conditioning
→ random variables
→ distributions
→ expectation / variance
→ joint distributions
→ Bayesian networks / inference later in the MSc
```
