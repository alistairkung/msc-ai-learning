# AIMS5701 — Search retrieval + Bayes Nets I pre-lecture bridge — 2026-09-30

## Session purpose

Use the first deliberate cumulative midterm-retention pass on Search, then cold-retrieve the 28 Sep Bayesian-network bridge and build only enough new runway for the live Lecture 3 deck.

The session happened before the 30 Sep lecture. The newly released deck is titled **Bayes Nets I** and its stated scope is **Representation of Bayes Nets** plus **Independence in Bayes Nets**. Sampling and variable elimination were useful pre-reading extensions, not confirmed content of this deck.

## Search — delayed retrieval evidence

### Returned cold

- Frontier policy:
  - BFS -> FIFO
  - DFS -> LIFO
  - UCS -> lowest known cost-so-far `g(n)`
  - Greedy -> lowest heuristic `h(n)`
  - A* -> lowest `f(n)=g(n)+h(n)`
- Meaning of `g`, `h`, and `f`.
- Admissibility as `h(n) <= h*(n)`: the heuristic does not overestimate true remaining cost.
- Consistency intuition: across an edge, the heuristic cannot fall by more than the real step cost.
- Changed frontier ordering across UCS / Greedy / A*.

### Needed reconstruction / repair

- UCS was initially recalled as complete but not optimal. The learner reconstructed optimality from lowest-`g` popping plus non-negative costs: after a goal of cost C is popped, no cheaper frontier route can later emerge without a negative edge.
- Greedy completeness was initially recalled as complete. An infinite low-`h` branch exposed why Greedy can behave like badly guided DFS and is not generally complete.
- Consistency => admissibility was understood after scaffolding through local inequalities and a telescoping sum.
- A* blocking optimality was the main deep-retrieval target. The learner reconstructed the proof shape, but initially flipped the admissibility inequality after the break and twice mixed the bound on `h*(n)` (remaining cost) with the bound on `f(n)` (whole estimated path). On the final changed problem the proof was produced independently apart from a notation typo:
  - admissibility gives `h(n) <= h*(n)`;
  - add `g(n)`: `f(n) <= g(n)+h*(n)=C*` for a frontier node on an optimal path;
  - a suboptimal goal G has `h(G)=0`, hence `f(G)=g(G)>C*`;
  - therefore the optimal-path node blocks the suboptimal goal.

### Boundary

This is meaningful delayed Search retention, not theorem mastery. Core algorithm selection and heuristic definitions are strong. UCS/Greedy guarantees and the A* blocking proof are recoverable by reasoning, but the proof should be cold-retrieved again after spacing, especially the distinction `h*(n)=C*-g(n)` versus `f(n)<=C*`.

## Bayesian networks — delayed retrieval

### Returned cold

- `P(A,B)` as joint probability and `P(A|B)` as conditional probability.
- `A ⟂ B` and `A ⟂ B | C` notation; the latter was explained as “once C is known, B gives no additional signal about A.”
- Parent reading and local factorisation on a changed DAG:
  `P(A,B,C,D)=P(A)P(B|A)P(C|A)P(D|B,C)`.
- Why a node can omit non-parent ancestors from its local conditional: conditional independence.
- Marginalisation definition: if B is no longer of interest, keep A fixed and sum over all possible values of B.

### Fragile / repaired

- The definition of marginalisation survived, but recognising a hidden-variable inference pattern did not initially return. On `Cloudy -> Rain -> Traffic`, the learner first misidentified the evidence as the hidden variable.
- Population-flow scaffolding repaired the operation: hold evidence fixed, identify the hidden variable, compute probability mass through every hidden branch, then sum.
- On the changed `Study -> Prepared -> Pass` problem the learner independently identified evidence / hidden / query and constructed the two-branch marginalisation correctly; only the final arithmetic addition slipped (`0.675+0.05=0.725`).
- Forward sampling order returned as parent-before-child, while the explicit `P(A) -> P(B|A) -> P(C|B)` procedure needed a short restatement.

## Sampling extension

A population/dot model inspired by Chris Piech's conditional-probability visualisation became the durable mental model.

### Forward sampling

Generate complete worlds. Root variables are sampled from priors; each child is sampled from the conditional distribution selected by its sampled parent values. No population is discarded.

### Rejection sampling

Generate worlds normally, then discard samples inconsistent with observed evidence. This maps directly to restricting attention to the evidence population. Rare evidence wastes most samples.

### Likelihood weighting

The learner reached the key intuition:

- sample unobserved variables normally;
- for an evidence node, **force every sample to the observed value** instead of running that lottery;
- multiply the sample's running weight by the CPT probability of that evidence given the sampled parent values;
- with multiple evidence nodes, multiply all evidence likelihoods into the running weight;
- estimate a posterior by weighted counting:
  `sum(weights matching query) / sum(all weights)`.

The strongest changed example used `A -> B -> C -> D` with evidence `B=T, D=T`. For a world with `A=T, C=F`, the learner correctly obtained `w=0.8*0.2=0.16` and interpreted the weight as effective probability mass / voting power, not “16% chance the sample is correct.”

The notation
`P_hat(Q=q | E=e) = [sum_i w_i 1(Q_i=q)] / [sum_i w_i]`
became readable as “weighted mass matching the query / total weighted mass.”

### Boundary

Likelihood weighting was newly taught and immediately transferred across changed examples; it is not delayed evidence. The live **Bayes Nets I** deck does not include sampling, so keep this as future inference/sampling runway rather than claiming live-course coverage.

## Independence and d-separation extension

New work covered the three canonical triples:

- chain `A -> B -> C`: unobserved middle -> endpoints generally dependent; observe middle -> endpoints conditionally independent;
- fork/common cause `A <- B -> C`: unobserved middle -> dependent; observe middle -> conditionally independent;
- collider/common effect `A -> B <- C`: unobserved collider -> endpoints independent; observe collider -> endpoints become dependent (“explaining away”).

The learner also understood that observing a **descendant of a collider** can activate the collider because the descendant carries information about it.

On larger DAGs, the learner successfully applied the d-separation procedure: inspect all undirected paths; a single blocked segment blocks a path; conditional independence requires every path to be blocked; one active path is enough for dependence to remain possible.

### Boundary

Concrete reasoning was strong, but the first abstract chain/fork/collider table reversed the chain/fork observed cases, and the first multi-path d-separation question repeated the fork reversal. Both were immediately repaired, and the learner then solved changed multi-path examples correctly. Treat d-separation as newly demonstrated/guided, not durable mastery.

## Live Lecture 3 deck reconciliation

The released deck materially narrows the immediate live scope:

- title: **Lecture 3: Bayes Nets I**;
- stated outline: **Representation of Bayes Nets** and **Independence in Bayes Nets**;
- probability review: joint, marginal and conditional distributions; product, chain and Bayes rules;
- representation: DAG/topology + local conditional probabilities/CPTs; joint factorisation as the product of local conditionals;
- independence: ordinary and conditional independence, local conditional-independence assumptions, chain/common-cause/common-effect triples and d-separation;
- no forward/rejection/likelihood-weighting sampling or variable-elimination algorithm appears in this deck.

The deck's local Markov statement — a node is conditionally independent of its non-descendants given its parents — is understood conceptually through factorisation but has not yet been directly cold-retrieved in that exact formulation.

Do not infer where inference/sampling moved from this deck alone. The Lecture 1 term map remains tentative for later weeks until newer live material resolves the sequence.

## Next

1. Attend Lecture 3 without further pre-study.
2. Within the next retrieval block, reconcile live emphasis and cold-check:
   - DAG + CPT semantics and factorisation;
   - local Markov property wording;
   - chain / fork / collider;
   - explaining away and descendant-of-collider activation;
   - one multi-path d-separation query.
3. Keep likelihood weighting and variable-elimination intuition parked as useful future Bayes-net runway unless live teaching explicitly brings them in.
4. After Lecture 3 reconciliation, diagnose Markov-chain recall before the HMM / particle-filtering JIT.
