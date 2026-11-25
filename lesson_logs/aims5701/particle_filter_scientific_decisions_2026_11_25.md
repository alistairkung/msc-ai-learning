# AIMS5701 — Scientific decisions behind the particle-filter deployment gate

**Date:** 25 November 2026  
**Type:** Guided conceptual consolidation and research-design defence  
**Project:** [particle-filter-deployment-gate](https://github.com/alistairkung/particle-filter-deployment-gate)  
**Evidence boundary:** The SimPy feasibility pilot reported **GO** and the five-second outbox telemetry-sufficiency study reported **READY** under a synthetic workload. The particle filter and deployment gate are **proposed**, not yet implemented or evaluated. This note documents the reasoning behind decisions, not independent unaided mastery or proof of production validity.

## Research question and separation of roles

Can a particle filter use time-causal transactional-outbox telemetry to estimate hidden shared-database conditions and improve predictions of write-SLO breach risk when increasing Java's traffic share in a Ruby-to-Java strangler migration?

- **Physical simulator:** Generates application writes, background queries, database work, event publication, and true hidden state.
- **Observation boundary:** Exposes only permitted outbox history as of the decision time.
- **Prospective estimator:** Updates beliefs about unobserved conditions. This is not yet implemented.
- **Risk forecaster / gate:** Predicts hold and promote outcomes using those beliefs and a model of future work. This is not yet implemented.
- **Evaluator:** Has privileged access to simulated physical states and matched future outcomes for scoring, never as model inputs.

The historical motivation is a beneficiary-service migration with validation-only Istio mirroring followed by live weighted routing. Ruby used Active Record; Java used custom SQL, Hibernate and JPQL. Historical publishers varied across services. The one shared logical publisher below is an **experimental control**, not a claim about a specific production architecture.

## 1. Why one non-preemptive FIFO database bottleneck?

**Decision.** Model a single shared server accepting database work from Ruby, Java, background queries and outbox-publisher claim/mark visits, processed first-come-first-served.

**Reason.** It is the smallest transparent mechanism in which a long independent query can delay a short application write and an outbox relay. For example, a 12 ms Ruby operation starting at 0 ms, followed by a 40 ms query and then a 16 ms Java operation, makes the Java operation wait until 52 ms even if it arrived at 5 ms: its arrival-to-completion latency is 63 ms, not 16 ms. This illustrates *head-of-line blocking*. Shared waiting can also harm Ruby writes that did not change implementation.

**Control/evidence.** Isolated M/M/1 and M/D/1 analytical queue checks test the scheduling path; the equal-work routing placebo checks that a route label alone does not change physical timings. The feasibility work passed those controls and exhibited routing-dependent pooled write-SLO effects.

**Boundary.** One exclusive FIFO resource is **not** a model of Aurora's actual CPU scheduler, optimiser, row locks, concurrency or connection pools. It establishes a synthetic shared-resource interference mechanism, not production latency forecasts.

## 2. Why Ruby and Java have different synchronous database demands?

**Decision.** Both implementations produce equivalent business effects and one equivalent outbox event per eligible write, but their route-specific synchronous DB service demand is configurable. The migration condition uses a **12 ms mean Ruby visit versus a 16 ms mean Java visit**, each including the same 1 ms atomic insert. The shared relay adds the same eventual claim/mark DB work to either route.

**Reason.** Functional contract equivalence does not imply operational equivalence: Active Record, JPQL, Hibernate and custom SQL can express the same beneficiary behaviour with different query plans, N+1 access, result sizes and transaction boundaries. Neither language is inherently slower. The selected values are synthetic intervention parameters, not measurements from the historical rewrite.

With total write rate (lambda), Java share (r), mean synchronous costs (d_R,d_J), common relay work (d_P) and background offered work (b):

[
ho(r)=b+lambda[(1-r)d_R+rd_J+d_P].
]

Hence, holding total offered traffic constant, changing share from (r_0) to (r_1) changes expected work by

[
Deltaho=lambda(r_1-r_0)(d_J-d_R).
]

At 40 writes/s, raising Java from 25% to 60% adds **0.056 work-seconds per elapsed second**, i.e. 5.6 percentage points of normalised capacity. This is *offered work*, not observed utilisation or a linear prediction of latency.

**Control/evidence.** In the equal-work placebo, identical visit patterns and service draws must yield identical route-blind physical traces across routing weights. The migration comparison then isolates the work difference under common publisher behaviour. The pilot reported paired breach-risk increases of **+39.00 pp** at reference demand and **+17.25 pp** with increased post-decision background demand.

**Boundary.** Other workload profiles and a Java-more-efficient scenario remain legitimate future tests. The baseline experiment does not claim a universal Java cost disadvantage.

## 3. Why outbox delay is an ambiguous observation

**Decision.** Treat outbox count, oldest pending age, publication throughput and completed commit-to-mark delay as **indirect, dependent measurements from one source**, rather than direct DB-pressure readings or four independent sensors.

**Reason.** Pending events may age because database contention delays claim/mark operations **or** because the publisher waits on slow off-DB sink acknowledgements. These mechanisms have different implications for synchronous application writes. Also, an empty outbox does not prove the DB is idle: writes can still be blocked *before* committing the outbox row. A completed-delay metric ignores unfinished rows unless pending/censoring semantics are preserved.

**Control/evidence.** C5 deliberately increases off-DB acknowledgement time while leaving database-work costs common; it demonstrated large outbox ageing without material application-write deterioration under its quiet-background configuration. The telemetry-sufficiency study added passive time-causal five-second lifecycle aggregates. Its protected analysis found measurable pooled information about background demand and incremental risk, but much of that signal came from distinguishing operating conditions.

**Boundary.** A particle filter cannot distinguish physically aliased causes if permitted observations contain no distinguishing information. Do not claim that outbox telemetry universally leads conventional monitoring; that is a future comparison.

## 4. Why matched hold/promote continuations are necessary

**Decision.** For each independently generated *root* (pre-decision simulation history), deterministically replay the same physical prefix and fork into **hold 25% Java** versus **promote 60% Java**. Pair future exogenous arrivals, routing uniforms and underlying service draws by stable identity. Preserve queued work, residual service, pending events and in-flight acknowledgements at the cut.

**Reason.** Two unrelated future simulations could differ because of random background jobs rather than the intervention. Matched continuations reduce that noise and isolate the effect of changing the share within the defined stochastic coupling.

For each root, (Y_{	ext{hold}}) and (Y_{	ext{promote}}) are binary future write-SLO breach outcomes. The signed paired result is

[
D=Y_{	ext{promote}}-Y_{	ext{hold}}in{-1,0,+1}.
]

A promote-only breach contributes +1; hold-only contributes -1; both-breach and neither-breach contribute zero. Averaging (D) estimates the **population incremental risk**. It is not valid to interpret one future pair as the exact conditional risk for that root.

**Control/evidence.** Physical-prefix equality, deterministic replay, conservation and identical pre-decision controller histories were tested. The telemetry study's 1,200 protected ordinary pairs included **835 promotion breaches**, with **370 promote-only breaches** avoidable by holding under the matched future coupling.

**Boundary.** The precise identity of an individual promote-only future depends on coupling assumptions; marginal action risks and their difference are the primary decision quantities.

## 5. What the hidden state represents

**Decision and distinction.** The telemetry-sufficiency study's primary *physical estimation target* is realised exogenous background DB work offered per second **over the last 30 seconds before the decision**:

[
X_t^{(30)}=rac{sum_{	ext{background arrivals in final 30 s}}	ext{requested DB service seconds}}{30	ext{ s}}.
]

For example, 6 seconds of requested query work in 30 seconds yields 0.20 work-seconds per second.

Keep separate:
- **Configured background-query intensity:** The arrival-rate parameter generating queries.
- **Realised background demand:** Random total work requested over an interval.
- **Unfinished DB work:** Residual active service plus queued work at the cut, across workloads.
- **Publisher condition:** Nominal versus slow acknowledgement, an independent cause of outbox ageing.
- **Total contention and waits:** Consequences of all workloads interacting with resource capacity and queue memory.

**Why.** An explicit numerical target allows state-estimation accuracy to be evaluated against privileged simulator truth. But a scalar demand summary is **not** the full Markov state of the FIFO system: queue order, residual service, event ages and publisher phase carry memory. The future particle-filter state and transition model still require independent specification; they must not silently initialise from privileged simulator state.

**Evidence/boundary.** Outbox-history diagnostics improved pooled estimates of realised background demand, but performance within a fixed operating condition was weak. That result supports studying partial observability; it does not show an estimator has recovered the complete hidden queue state.

## 6. Why better state estimation may not improve deployment decisions

**Decision.** Evaluate physical-state estimation, absolute future breach risk and incremental promotion risk as **different claims**.

For a permitted history (H):

[
R_{mathrm{hold}}(H)=P(Y_{mathrm{hold}}=1mid H),qquad
R_{mathrm{promote}}(H)=P(Y_{mathrm{promote}}=1mid H)
]

[
Delta R(H)=R_{mathrm{promote}}(H)-R_{mathrm{hold}}(H).
]

**Reason.** If both choices are almost certainly unsafe because the DB is already overloaded, an accurate estimate of high contention may predict a breach but say little about whether holding *helps*. Conversely, a moderately loaded system near the capacity knee may be safe at 25% and unsafe at 60%. Accurate state estimation is useful only insofar as it supports a discriminating forecast of the action contrast.

**Evidence.** Outbox history improved pooled action-risk forecasts and had a detectable gain over a constant incremental-risk forecast. Yet its incremental-risk improvement versus the complete current outbox snapshot was only **+0.00146 MSE**, with a descriptive 95% interval **[-0.00076, +0.00362]**. The added temporal benefit for the decision remains unresolved. The pooled gains mostly reflected **between-condition** information; within-condition constant predictors could outperform the selected model. The privileged evaluator did better, but is not an admissible gate.

**Boundary.** Neither predictive-score improvement nor state estimation alone proves that a deployment policy saves incidents or improves operational decisions. Decision costs, false holds and unsafe promotions need separate evaluation.

## 7. How a particle filter would update beliefs and produce forecasts

**Status: proposed algorithm, not yet an empirical result.** A bootstrap particle filter represents uncertainty over a chosen hidden operational state using weighted particles ({x_t^{(i)},w_t^{(i)}}_{i=1}^N). The transition and likelihood must be specified and calibrated without reading the evaluator's true queue or future outcomes.

1. **Predict:** Sample a new candidate hidden state from the assumed transition model for each particle; include sufficient queue/publisher memory or an explicitly stated surrogate.
2. **Weight:** Compare each particle's predicted observation with the newly *available* joint outbox measurement, using a likelihood (p(y_tmid x_t^{(i)},	ext{history})). Count, age, throughput and delay share event histories, so blindly multiplying independent marginal likelihoods is not justified.
3. **Normalise:** Set weights to sum to one.
4. **Diagnose degeneracy:** Calculate effective sample size, (mathrm{ESS}=1/sum_i(w_t^{(i)})^2).
5. **Resample if needed:** Use a predeclared rule such as systematic resampling below an ESS threshold. Resampling concentrates computation on plausible states; it does not create new observational information.
6. **Forecast both actions:** For each weighted plausible state, use a specified *future workload and queue forecast model*, with fresh future randomness, to estimate breach risk under 25% and 60% Java. Average risks across particles, then subtract the two action risks.

Formally, for candidate action (a):

[
widehat R(a)approxsum_{i=1}^N w_t^{(i)}widehat P(Y_a=1mid x_t^{(i)},a,M).
]

(M) includes capacity, known service assumptions and the future-workload law. The particle filter updates beliefs; **it does not by itself supply a valid breach-risk forecaster**. A future independent abrupt shock cannot be predicted from identical pre-decision histories beyond its assumed hazard.

**Required comparisons.** Prior/current outbox/history diagnostics, a queue-based prediction baseline, and an appropriate same-model finite-state or grid check for filtering correctness if practical. Use fresh independent protected roots: previously inspected telemetry-sufficiency protected data are historical evidence, not an untouched test set for the PF.

## Evidence status and next learning checks

| Claim | Status as of this review |
|---|---|
| Shared FIFO simulator and route placebo valid under frozen assumptions | Supported by prior pilot tests/reproduction |
| Route intervention produces synthetic SLO harm | Supported by pilot GO |
| Five-second outbox history has some pooled predictive information | Supported by telemetry READY |
| Temporal history improves incremental-risk forecasts beyond full current snapshot | **Inconclusive** |
| Particle filter estimates hidden state accurately | **Not yet tested** |
| Particle filter improves hold/promote predictions or decisions | **Not yet tested** |
| Production Aurora applicability | **Not established** |

**Learning evidence:** The learner articulated the outbox-as-sensor premise and challenged the earlier Java-only publication-cost assumption. The discussion worked through the causal mechanism, matched branches, hidden targets and the predict–weight–normalise–ESS–resample sequence with guided explanations. This is *guided conceptual consolidation*; independent recall and derivation remain to be checked.

**Next useful self-test:** Explain without notes (i) why the equal-work placebo is necessary, (ii) why a slow publisher can impersonate DB contention, (iii) the difference between realised background demand and unfinished queue work, and (iv) why smaller latent-state RMSE may coexist with unchanged incremental-risk MSE. Then work one simple weighted-particle update and two-action forecast by hand.

## Source-of-truth pointers

- [Frozen research plan](projects/particle_filter_rollout_risk_plan.md)
- [Original independent feasibility review](projects/particle_filter_feasibility_review.md)
- [Feasibility pilot report](https://github.com/alistairkung/particle-filter-deployment-gate/blob/main/feasibility_pilot/FEASIBILITY_REPORT.md)
- [Telemetry sufficiency readiness report](https://github.com/alistairkung/particle-filter-deployment-gate/blob/main/telemetry_sufficiency/results/v1/Experimental_Readiness_Report.md)

The external repository owns implementation and full scientific evidence. This learning note is a conceptual and methodological explanation, not a replacement for its reports.
