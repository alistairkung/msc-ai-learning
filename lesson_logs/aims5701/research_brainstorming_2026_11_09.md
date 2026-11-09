# AIMS5701 research brainstorming — 9 November 2026

## Status and evidence boundary
Learner-led conceptual synthesis, not a completed implementation, model result, or proof of independent particle-filter coding proficiency. AIMS5701 final project deadline reported as **24 December 2026**. Considering replacing the originally selected **XJ10 AIMS5701** idea; no formal replacement submission confirmed.

## Reasoning trajectory
- Experience with poorly understood legacy behaviour and cross-domain incidents during strangler migrations prompted interest in AI-assisted testing and CI/CD safety.
- Initial hypothesis: transformer embeddings and sequences of distributed network traffic might uncover undocumented dependencies and generate realistic regression tests.
- Learner independently connected AIMS5701's Markov blanket / conditional-independence ideas to reducing a vast service graph to relevant local neighbours. Clarified that immediate network neighbours are not necessarily a true Markov blanket; asynchronous messaging, hidden state, shared resources and feedback break naive independence.
- Refined question from next-message prediction to **counterfactual downstream response when a neighbour changes behaviour**. A transformer trained on observational sequences cannot automatically infer effects of unseen semantic interventions.
- Potential follow-on: learned local predictive state and behavioural compatibility for legacy rewrites, with static contracts, process mining, stateful differential tests and probabilistic baselines.

## Bounded particle-filter pivot
Grounded in the learner's actual Ruby-to-Java beneficiary-service migration:
- Istio **mirrored** traffic while Java validated and logged outcomes; **no writes or downstream side effects** occurred in shadow mode.
- Subsequent live cutover used Istio **weighted routing percentages**.
- A simulated *transactional outbox* is proposed as the observability target **during weighted live rollout**, not shadow mode. Do not claim the historical migration contained this precise outbox pipeline.
- Instead of a fixed 50%-headroom rollback alert, use sequential Monte Carlo to infer latent publisher processing capacity and forecast **SLO breach risk curves** at candidate higher traffic shares. Gate holds/promotes based on risk, with explicit workload and queue assumptions.

Scientific threats identified: arbitrary headroom formula, perfect agreement between generator and estimator, capacity unidentifiable under low load, censored pending-message delay, unfamiliar high-load saturation, unclear cutover SLO, model mismatch, and baseline comparison fairness.

Candidate research comparisons: reactive threshold, trend forecast and particle-filter risk model, with repeated controlled interventions, calibrated breach risk, unsafe promotions, unnecessary holds, rollout delay and observation/particle-count ablations.

## Course rubric and time constraints
Rubric weights: experimental rigor 30, novelty/analytic insight 20, completeness/complexity 20, report 15, video 10, proposal 5. Novel application or rigorous analytic comparison can qualify for high novelty; professional relevance alone does not establish literature novelty.
Protect AIMS5701 midterm **18 Nov**, AIMS5702 quiz **12 Nov** and its as-yet-unannounced final project, plus FTEC5660 PCG final iteration. Keep simulator bounded and separate from larger transformer ambition.

## Parked future project — transformer behavioural assurance
Use legacy interaction histories and cross-service traces to infer implicit semantic/temporal behaviours, compare a rewrite against legacy outcomes and explore local predictive state / approximate Markov blankets for counterfactual impact analysis. Research question: can sequence models flag undocumented compatibility risks missed by explicit contracts, without treating correlation/attention as causal proof? Candidate for next-term AI-in-software-testing industry work, not part of the particle-filter project.

## Next useful study step
Freeze a concise simulator/observation specification and falsifiable hypotheses; independently re-derive particle predict–weight–ESS–resample and the conditional risk calculation before implementation. **No new mastery promotion** from brainstorming alone.
