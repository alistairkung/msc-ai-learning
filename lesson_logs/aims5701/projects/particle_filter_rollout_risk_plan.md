# AIMS5701 final-project plan — Particle Filtering for Counterfactual Rollout Risk

**Status:** Proposed, pre-implementation; no empirical results.  
**Deadline:** 24 December 2026 (learner reported).  
**Course:** AIMS5701 Fundamentals in AI.

## Motivation and architecture
Motivated by a real Ruby-to-Java beneficiary-service strangler migration: Istio mirrored requests to Java for **validation/logging without writes or downstream side effects**, then used **weighted percentage routing** for gradual live cutover. The experiment models an *illustrative* live-write Java service with a transactional outbox and finite-capacity publisher. Do not assert that the historical shadow implementation used an active outbox.

## Research question
Can sequential Monte Carlo estimate uncertain outbox publisher capacity from noisy observations during a partial rollout, then predict the risk of event-processing SLO breaches at untried higher Istio traffic percentages?

A risk curve R(r), not only a binary alarm, is the primary output; a decision gate can be derived from it.

## Hypotheses
- **H1:** A particle-filter risk forecast improves calibration and/or unsafe-promotion prevention against conventional reactive and trend-forecast baselines, compared at matched false-alarm or decision costs.
- **H2:** At low load, latent maximum capacity is poorly identifiable; risk estimates sharpen as informative load regimes are observed.
- **H3:** The model may be overconfident under abrupt saturation or misspecified state dynamics; robustness analysis should quantify this limit.

## Simulator: ground truth separate from the filter
Small discrete-event simulator with seeded arrivals, Istio routing share r, eligible write rate, atomic creation of pending outbox records, queue processing and publisher capacity μ. Distinguish shadow validation (no writes/outbox emission) and progressive live weighted-routing mode. Queue evolves through counted arrivals and completed publications. Inject gradual contention and optionally abrupt saturation. Record exact hidden capacity and full message lifecycle for evaluation only.

## Observations and model
At each interval, the estimator receives known request/arrival rate, completed-record processing delay (created_at to processed_at), pending count, oldest pending-record age and optional throughput. Pending records have no processed_at: treat them as censored/still waiting, never as healthy missing observations. Define a measurement likelihood and latent transition prior independently of simulator implementation; document assumptions and identifiability limitations. Avoid a made-up headroom score unless grounded in physical dynamics.

## Sequential Monte Carlo
Particles track candidate latent effective capacity (and any strictly necessary queue state). For each observation step: predict particles, calculate telemetry likelihood, normalise importance weights, compute ESS, resample systematically if below threshold. Forecast each posterior particle forward under candidate traffic weights r and a stated workload forecast over horizon H.

Estimate R(r) = P(outbox-processing SLO breach within H | data to time t, proposed do(r), simulator/model assumptions), with uncertainty and warnings for extrapolation. Particle filtering represents uncertainty conditional on assumptions; it does not prove causal effects of load outside modelled regimes.

## Baselines, evaluation and ablation
1. Reactive threshold on current delay/oldest pending age or backlog.
2. A fair trend-based predictive baseline with the same observable telemetry and horizon.
3. Particle-filter counterfactual forecast.

Evaluate risk calibration (Brier score and reliability plot), missed unsafe promotions, false holds, time to safe rollout, prediction lead time, and estimation error versus hidden capacity. Use held-out seeds and intervention regimes, compare thresholds at matched decision costs. Quantify numerical/runtime costs.

Ablate pending age, completed delay, backlog, particle count, and sequential updating. Repeat under model mismatch: abrupt capacity collapse not adequately represented in the filter. A negative or inconclusive result is valid if properly explained.

## Scope / acceptance
Required: deterministic simulator with reproducible tests, physically plausible queue dynamics, particle filter, two baselines, fixed evaluation protocol, risk curves, tables/plots, report and video pitch. Excluded: real Istio/Kafka/Kubernetes/database, production CI deployment, transformers, broad dependency learning, paid APIs. Scientific tests cover mass conservation, shadow no-side-effects, routing fraction, lifecycle timestamps, deterministic seeds, weight normalisation, ESS/resampling, ground-truth leakage.

## Delivery stages
- **Nov 9–18:** specification and literature positioning only while protecting 12 Nov AIMS5702 quiz and 18 Nov AIMS5701 midterm.
- **Nov 19–29:** simulator + tested baseline; feasibility checkpoint.
- **Nov 30–Dec 9:** PF and fixed experiments.
- **Dec 10–17:** ablations, error analysis, write-up.
- **Dec 18–24:** buffer, video, final verification and submission; accommodate unknown AIMS5702 final and PCG work.

If simulator fidelity or evaluation fails by the Nov 29 checkpoint, reduce to state estimation and a tightly controlled counterfactual demonstration rather than expanding infrastructure.

## Literature starting points (verify claims in report)
- Lindon, Sanden & Shirikian, *Rapid Regression Detection in Software Deployments through Sequential Testing* (2022), https://arxiv.org/abs/2205.14762
- Google SRE Workbook, *Canarying Releases*, https://sre.google/workbook/canarying-releases/
- Richardson, *Transactional Outbox*, https://microservices.io/patterns/data/transactional-outbox.html
- Debezium, *Reliable Microservices Data Exchange With the Outbox Pattern*, https://debezium.io/blog/2019/02/19/reliable-microservices-data-exchange-with-the-outbox-pattern/

## Related work intentionally parked
Transformer-based learned behavioural compatibility and local Markov-blanket/counterfactual dependency inference are separate future project ideas; see the 9 Nov brainstorming log.
