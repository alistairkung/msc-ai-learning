# AIMS5701 final project — Frozen Experimental Design

**Working title:** Particle Filtering for Risk-Aware Progressive Rollouts Under Hidden Infrastructure Contention  
**Status:** Research question and experimental scope frozen 11 November 2026; model parameters, implementation and results **not** frozen or validated.  
**Deadline:** 24 December 2026 (learner reported).  
**Course:** AIMS5701 Fundamentals in AI.

## Motivation and historical boundary

Inspired by a Ruby-to-Java beneficiary-service migration using the Strangler pattern. Istio mirrored requests to Java for validation/logging **without writes or downstream side effects**; subsequently **weighted percentage routing** progressively shifted live traffic to Java. This project proposes an illustrative Java write path with a transactional outbox for the experimental environment; it **does not claim that the historical shadow migration had an outbox pipeline**.

The engineering risk is a rewritten service that behaves functionally correctly but becomes unhealthy as more traffic is directed to it because another team's feature, batch job or expensive query competes for shared infrastructure. The outbox is an **indirect sensor** for that broader degradation, not necessarily the component causing the failure.

## Frozen research question

**Can a particle filter infer hidden shared-database contention from transactional-outbox telemetry and predict the risk of increasing a rewritten service's production traffic share before conventional health monitoring identifies the problem?**

The primary output is a risk curve across candidate Java routing weights. A promote/hold decision derives from a pre-specified decision rule; this is a proposed CI/CD rollout assurance mechanism, **not** an implemented production gate.

## Frozen architecture and boundaries

A compact, seeded **SimPy discrete-event simulation** represents:

1. A time-varying incoming workload, with a tunable Istio-style Java routing percentage.
2. The Java service's eligible write transactions, atomically creating corresponding outbox records in the simplified model.
3. An outbox queue containing timestamped pending events, and a publisher that claims/processes/publishes events to a simulated sink.
4. **Shared database resources** contended for by Java writers, outbox publisher operations and an independent background workload from an adjacent service or feature.
5. Finite resource capacity and stochastic holding/service times that induce waiting and possibly degradation. SimPy handles waiting and scheduling; custom processes define the DB behaviour. **No claim of PostgreSQL-level lock fidelity.**
6. Event lifecycle and telemetry sampling, with simulator-only access to ground-truth background pressure and latent contention.

**Primary disturbance:** adjacent feature increases shared database demand (e.g., expensive reporting queries or a batch job). This can delay both Java write operations and outbox publisher operations without changing beneficiary business logic. It must be represented as actual shared resource competition, not simply an observation curve scripted to favour the particle filter.

**Control case:** fixed-capacity publisher bottleneck.  
**Robustness case:** abrupt regime shift / threshold contention not fully represented by the filter.

Explicitly **excluded:** real Istio, Kafka, PostgreSQL, Kubernetes, real chaos tooling, entire organisation service graph, transformer training and production CI integration.

## State-space formulation (to specify and calibrate)

- **Known inputs** `u_t`: Java routing weight, incoming request rate/workload summary, and documented rollout intervention. The model is not given future background workload as ground truth.
- **Latent state** `x_t`: persistent unobserved background resource pressure / contention regime (possibly one scalar or a small discrete regime plus continuous intensity). Its definition must be operationally grounded: for example, increased competing DB resource holding time/demand, not just a renamed measured queue length.
- **Primary observations** `y_t`: completed-event outbox processing delay, pending outbox count, and age of oldest pending event. Pending events have no `processed_at` timestamp and must not be silently discarded as healthy.
- **Comparison/optional observations**: Java write/request latency, possibly observed publication throughput.
- **Transition model** `p(x_{t+1}|x_t,u_t)`: persistence of hidden contention and uncertain evolution; known routing changes and unknown adjacent workload shifts influence the simulated world. The filter's approximation should be documented independently.
- **Observation model** `p(y_t|x_t,u_t,Q_t)`: estimated telemetry distribution conditional on contention, routed workload and current backlog/known queue state. Measurement noise and process variability must be distinguished; correlations among multiple telemetry metrics must not be treated as independent without justification.

The outbox's backlog itself may be directly observed, but the underlying shared resource demand is not. Data generated by SimPy establishes ground truth **only for evaluation**. It must not leak into the filter.

## Particle filter and counterfactual forecast

Run standard Sequential Monte Carlo: propagate particles, compute observation likelihoods, normalise weights, calculate ESS, and resample systematically when indicated. Each particle encodes a possible hidden contention state. Roll particles forward under each proposed Java routing share `r` and a stated forecast of external workload and background contention; simulate future write/outbox outcomes.

Primary quantity: `R(r) = P(write-latency or outbox-event-delivery SLO breach within H | observations through t, proposed routing share r, model assumptions)`.

The exact SLO thresholds, forecast horizon `H`, prior, transition and likelihood parameters must be fixed **before** testing. The filter cannot predict a completely unseen future adjacent deployment; forecasts are conditional on assumptions about background workload and hidden-state dynamics. Low-load telemetry may be insufficient to identify latent risk.

## Required experiments

| ID | Experiment | Main question |
| --- | --- | --- |
| E1 | Healthy vs. gradual adjacent-workload contention | Can the filter infer increasing hidden resource pressure before a breach? |
| E2 | Weighted-rollout counterfactuals (e.g., observed 5/10/25% then proposed higher weights) | Can it provide calibrated risk curves for untried routing shares? |
| E3 | Sensor comparisons/ablation (outbox only, request latency only, combined) | Does outbox telemetry add early warning beyond conventional request metrics? |
| E4 | Abrupt contention regime shift / model mismatch | When does the filter become inaccurate or overconfident? |

Ablate outbox delay, pending count and pending age; optionally particle count / history-update logic if time allows. Multiple independent seeds, held-out parameter regimes, and matched independent counterfactual continuations establish breach ground truth. Avoid fitting the generator to the estimator.

## Comparison methods and metrics

- **Reactive monitoring:** current SLO / backlog / latency thresholds.
- **Predictive trend baseline:** a simple extrapolation of permitted telemetry over the same horizon.
- **Optional queue-only baseline:** model forecast based on observed arrivals and queue dynamics, to test whether particle filtering adds real value.
- **Particle-filter gate:** posterior predictive breach probabilities at candidate shares.

Evaluate Brier score, reliability/calibration, missed unsafe promotions, false holds, lead time, time to full rollout and computational cost. Compare decisions at matched false-alarm rates or fixed decision costs; avoid unfair advantage from giving one method information unavailable to the others.

## Scientific safeguards / success criteria

- Simulator model is defined and tested **before** PF tuning; hidden resource competition produces observable outcomes without the filter.
- Distinguish contention in the **DB** from ordinary fixed-capacity outbox saturation.
- Verify outbox conservation, causally consistent timestamps, routing allocation, shadow no-writes mode (if represented), reproducible seeds and no ground-truth leakage.
- Specify model assumptions and report when capacity/pressure is unidentifiable, the observation is delayed, or extrapolation is unsafe.
- A useful **negative result is acceptable**: the project investigates whether and under what conditions filtering adds decision value, rather than guaranteeing an improvement.
- Deliver reproducible code, quantitative tables, key plots, focused ablation, written report and a short video. Particle animation from recorded Python runs is optional, not on the critical path.

## Work plan

- **Through 18 Nov:** freeze methods, metrics, simulator contracts and reference literature; protect AIMS5701 midterm and other deadlines.
- **19–29 Nov:** validate SimPy contention world, observation data and simple baselines; feasibility checkpoint.
- **30 Nov–9 Dec:** implement/calibrate particle filter, independent rollout continuations and risk curves.
- **10–17 Dec:** ablations, robustness, qualitative failure-case interpretation and report.
- **18–24 Dec:** video, final verification and buffer shared with AIMS5702 final work and FTEC5660 PCG iteration.

If the hidden-state model fails the feasibility checkpoint, narrow to one contention regime and carefully calibrated short-horizon forecasts; do not add infrastructure or new AI methods.

## Literature starting points (verify in final report)

- Lindon, Sanden & Shirikian, *Rapid Regression Detection in Software Deployments through Sequential Testing* (2022): https://arxiv.org/abs/2205.14762
- Google SRE Workbook, *Canarying Releases*: https://sre.google/workbook/canarying-releases/
- Richardson, *Transactional Outbox*: https://microservices.io/patterns/data/transactional-outbox.html
- Debezium, *Reliable Microservices Data Exchange With the Outbox Pattern*: https://debezium.io/blog/2019/02/19/reliable-microservices-data-exchange-with-the-outbox-pattern/
- SimPy documentation: https://simpy.readthedocs.io/

## Future work deliberately excluded

Transformer-based discovery of undocumented behavioural contracts and local Markov-blanket-based counterfactual service impact is a **separate future research idea**, preserved in `lesson_logs/aims5701/research_brainstorming_2026_11_09.md`.
