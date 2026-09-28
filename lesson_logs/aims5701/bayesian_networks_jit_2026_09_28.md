# AIMS5701 Bayesian-networks JIT bridge — 28 Sep 2026

## Session purpose

First pre-lecture bridge for the upcoming live topic: **Bayesian networks — representation, independence, inference and sampling**. The session began with delayed probability retrieval and then introduced Bayesian-network concepts. It intentionally stopped at first-rung sampling rather than racing into specific approximate-inference algorithms.

## Probability retrieval

Cold/basic retrieval was stronger than expected:

- `P(A)`, complements, conditional probability and joint-probability meaning were intact once notation was translated.
- The product rule was reconstructed from a 100-case population model.
- Bayes' formula itself was not cold. The learner first inverted terms, then derived the rule from the fact that `P(A)P(B|A)` and `P(B)P(A|B)` describe the same joint intersection.
- Independence intuition was present but was initially conflated with mutual exclusivity. The distinction was corrected.
- Conditional independence came quickly. For common-cause and simple-chain examples, the learner correctly reasoned that once the mediating/common variable is known, another variable can provide no additional signal.

A durable notation/mental-model summary was requested and created at `foundations/probability_statistics/bayesian_network_probability_bridge.md`.

## Bayesian-network representation

Introduced:

- DAG/node/parent language;
- CPT/local conditional distributions;
- binary parent configurations;
- full-joint size intuition (`n` binary variables -> `2^n` assignments);
- local factorisation `P(X1,...,Xn)=product_i P(X_i | Parents(X_i))`;
- why conditional independence turns the ordinary chain-rule expansion into parent-local factors.

The learner correctly identified parents and factorised changed DAGs during guided work. On the end-of-session cold check, one edge was misread: for a graph where A parents B and C, the learner wrote `P(C|B)` instead of `P(C|A)`. Keep DAG parent-reading/factorisation as retrieval work, not established mastery.

## Marginalisation and inference

Marginalisation required conceptual reconciliation. The durable mental model became:

> Keep the variables/values I care about fixed; if I do not care which value a hidden variable takes, sum over all of its possible values so it disappears from the result.

The learner distinguished this from conditioning after initially feeling that a conditional-probability table exercise was doing the opposite. They then performed simple exact inference through a hidden variable.

Strongest changed-example evidence:

```text
Exercise -> Energy -> Focus

P(Energy=T | Exercise=T) = 0.7
P(Energy=F | Exercise=T) = 0.3
P(Focus=T | Energy=T) = 0.8
P(Focus=T | Energy=F) = 0.2

P(Focus=T | Exercise=T)
  = (0.7 * 0.8) + (0.3 * 0.2)
  = 0.62
```

The learner independently identified Energy as the variable to marginalise and constructed the two-branch sum. This is same-session changed-problem evidence, not delayed mastery.

## Sampling

Introduced only forward/prior-sampling intuition:

- sample root variables from their priors;
- then sample children from the CPT row selected by sampled parent values;
- continue in parent-before-child/topological order;
- repeated worlds can approximate marginal probabilities by frequency.

One threshold interpretation slipped once (a random draw 0.73 under probability 0.9 was initially classified False), then corrected. The learner cold-reconstructed the parent -> child sampling order at session end.

Rejection sampling, likelihood weighting, Gibbs/MCMC and variable elimination were **not** taught.

## End-of-session cold check

Returned correctly:
- `P(A|B)` vs `P(A,B)`;
- independence vs conditional independence in words;
- sampling order.

Needed correction/refinement:
- one DAG edge when factorising;
- marginalisation definition needed the “keep cared-about variables fixed; sum over all values of the eliminated variable” precision.

## Next session — Wednesday pre-lecture

Planned 4–5 hour block:

1. ~1h delayed cold review of Lecture 2 search: BFS/DFS/UCS/Greedy/A*, frontier ordering, guarantees/complexity, admissibility/consistency, plus actual-slide gaps such as graph-vs-tree search and safe closing.
2. ~1h delayed cold review of this Bayesian-network bridge without the summary sheet first.
3. Remaining time: expand likely lecture-facing coverage, prioritising chain/fork/collider independence structure (including collider/explaining-away intuition), exact inference beyond one hidden node / variable-elimination intuition, and sampling with evidence such as rejection sampling. Add likelihood weighting or Gibbs only if time/course evidence warrants it.
4. Prefer one changed integrated DAG problem over breadth if time becomes tight.

The exact live lecture deck is not yet available, so these extensions are predictions from the advertised headings rather than confirmed course coverage.
