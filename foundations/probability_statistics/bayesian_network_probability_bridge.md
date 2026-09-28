# Probability notation and Bayesian-network bridge

_Last updated: 28 Sep 2026._

This is a compact translation sheet for notation that came up while preparing for the AIMS5701 Bayesian-networks lecture. It records concepts actually retrieved or derived in-session rather than trying to be a complete probability reference.

## Read the notation in words

| Notation | Read it as | Meaning |
|---|---|---|
| `P(A)` | probability of A | Chance that A occurs |
| `P(¬A)` | probability of not A | Complement of A; the learner has also seen `P'(A)` |
| `P(A,B)` or `P(A ∩ B)` | probability of A and B | Joint probability that both occur |
| `P(A | B)` | probability of A given B | Restrict attention to the B cases, then ask what proportion are also A |
| `A ⟂ B` | A is independent of B | Knowing B gives no additional information about A |
| `A ⟂ B | C` | A is independent of B given C | Once C is known, B gives no additional signal about A |
| `Σ_B` | sum over B | Add across all possible values of B |
| `∏_i` | product over i | Multiply the terms for all values/nodes indexed by i |

## Complement

```text
P(¬A) = 1 - P(A)
```

For a binary event, A and not-A exhaust the possibilities.

## Conditional and joint probability

```text
P(A | B) = P(A,B) / P(B)
```

Mental model: **the population being inspected is whatever comes after the conditioning bar**.

The product rule is:

```text
P(A,B) = P(A) P(B | A)
```

Population interpretation: first reach the A cases, then take the fraction of those cases in which B also occurs.

## Why Bayes' rule is true

The same A-and-B overlap can be reached from either direction:

```text
P(A,B) = P(A) P(B | A)
P(A,B) = P(B) P(A | B)
```

Therefore:

```text
P(A) P(B | A) = P(B) P(A | B)
```

and dividing by `P(B)` gives:

```text
P(A | B) = P(B | A) P(A) / P(B)
```

Mental model: **Bayes reverses the conditioning direction by using the shared joint/intersection as the bridge.**

## Independence is not mutual exclusivity

If A and B are independent:

```text
P(A | B) = P(A)
P(A,B) = P(A)P(B)
```

Knowing one occurred does not change the probability of the other. Independent events can occur together.

Mutually exclusive events cannot occur together. For non-zero-probability events, learning A occurred therefore tells us B did not occur, so mutual exclusivity is not independence.

## Conditional independence

```text
A ⟂ B | C
```

means: **once C is known, learning B gives no additional information about A.**

For a simple chain:

```text
A -> B -> C
```

a useful first intuition is that once B is known, the relevant information flowing from A toward C is already represented by B:

```text
A ⟂ C | B
```

This is an introductory scaffold; later graphical-independence work should refine it beyond simple chains.

## Marginalisation

To **marginalise out B**:

> Keep the variables/values you care about fixed, and sum across every possible value of B because you no longer care which B occurred.

For binary B:

```text
P(A=True)
  = P(A=True, B=True)
  + P(A=True, B=False)
```

Compactly:

```text
P(A) = Σ_B P(A,B)
```

Marginalisation **eliminates B from the result**. It is distinct from conditioning, although marginalisation is often used to construct the denominator needed for a conditional probability.

## Bayesian-network factorisation

A Bayesian network is represented by a directed acyclic graph plus local conditional probability distributions/tables. Each node is conditioned on its parents.

For:

```text
    A
   / \
  B   C
   \ /
    D
```

the parents are:

```text
A: none
B: A
C: A
D: B,C
```

so the joint factorises as:

```text
P(A,B,C,D)
  = P(A)
    P(B | A)
    P(C | A)
    P(D | B,C)
```

General shorthand:

```text
P(X1,...,Xn) = ∏_i P(X_i | Parents(X_i))
```

Read the product symbol as: **for every node, take its probability given its parents and multiply all those terms together**.

The ordinary chain rule can condition later variables on all preceding variables; the Bayesian network's conditional-independence assumptions remove unnecessary conditions, yielding the local parent-based factorisation.

## Exact inference: current mental model

- **Factorisation:** multiply local probabilities to obtain joint probabilities for configurations.
- **Marginalisation:** sum over hidden/unwanted variable values to eliminate them.
- **Conditioning:** restrict to observed evidence and calculate proportions within that evidence population.
- **Prior:** belief before observing evidence.
- **Posterior:** updated belief after observing evidence.

A changed three-node exercise was solved independently in-session:

```text
Exercise -> Energy -> Focus

P(Energy=T | Exercise=T) = 0.7
P(Energy=F | Exercise=T) = 0.3
P(Focus=T | Energy=T) = 0.8
P(Focus=T | Energy=F) = 0.2
```

Marginalising hidden Energy:

```text
P(Focus=T | Exercise=T)
  = (0.7 * 0.8) + (0.3 * 0.2)
  = 0.62
```

## Sampling: first rung

Generate one complete world in parent-to-child order:

```text
sample A from P(A)
sample B from P(B | sampled A)
sample C from P(C | sampled B)
...
```

Repeated samples approximate probabilities by empirical frequency. This session covered only forward/prior-sampling intuition; rejection sampling, likelihood weighting, Gibbs/MCMC and other sampling algorithms were not taught.

## Current fragile edges

- Bayes' formula was not cold, although its derivation from the shared joint event was understood.
- Independence was initially confused with mutual exclusivity.
- DAG parent-reading had one cold-check slip (`C` was incorrectly conditioned on `B` rather than its actual parent `A`).
- Marginalisation needed wording tightened from “sum probabilities involving B” to “keep what I care about fixed and sum over all B values.”
- Symbols `⊥`, `Σ` and `∏` benefit from explicit spoken translations.
