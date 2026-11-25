# AIMS5701 final project — Frozen Experimental Design

**Working title:** Particle Filtering for Risk-Aware Progressive Rollouts Under Hidden Infrastructure Contention  
**Status:** Research question and experimental scope frozen 11 November 2026. Shared-outbox architecture clarified 25 November 2026. The causal mechanism awaits simulator validation.  
**Deadline:** 24 December 2026 (learner reported).  
**Course:** AIMS5701 Fundamentals in AI.

## Motivation and historical boundary

In the beneficiary-service migration that motivated this project, the Ruby on Rails implementation predominantly used Active Record. The Java rewrite used a mixture of custom SQL, Hibernate and Jakarta Persistence Query Language (JPQL). Both were intended to satisfy the same functional contracts. A contract can establish that a beneficiary operation returns the expected result and produces the expected effects. Establishing operational equivalence also requires evidence about the resources each implementation consumes.

For example, one implementation might load related records in a single indexed query while the other issues a query per record (an N+1 pattern). Query plans, transaction boundaries, pagination and result-set sizes can also affect DB work or connection occupancy. Either implementation could be more efficient. These are possible explanations for a demand difference. Their occurrence and cost in the historical migration are unknown.

Historical Istio mirroring validated and logged requests without writes or downstream side effects. Live weighted routing came later. In the experiment, an eligible live request on either route commits the same business change and creates an equivalent event for the same logical publisher. This shared-outbox assumption is specific to the experiment.

**Causal mechanism.** Changing the traffic split changes the mix of implementation-specific synchronous DB work. Independently, expensive large-account queries compete for the same DB capacity. The resulting waiting can affect both application writes and the shared relay. Outbox timings and backlog are therefore an indirect sensor of operating conditions. The proposed filter uses those observations to estimate hidden background demand, then forecasts pooled write-SLO risk under each candidate split. The sensor’s predictive value and lead time are empirical questions.

## Frozen research question

**Can a particle filter infer hidden shared-database contention from transactional-outbox telemetry and predict the risk of increasing a rewritten service's production traffic share before conventional health monitoring identifies the problem?**

The primary output is a risk curve across candidate Java routing weights. A promote/hold decision derives from a pre-specified decision rule; this is a proposed CI/CD rollout assurance mechanism, **not** an implemented production gate.

## Experimental architecture

Use one seeded SimPy model with one first-come-first-served processing bottleneck and three workloads. The smallest change to the November design is to put event creation in a common commit path, parameterise the application’s synchronous service demand by route, and feed the existing publisher design from that common path.

| Workload | Service and instrumentation |
|---|---|
| Application writes | Generate one external stream of equivalent beneficiary requests. Assign a stable request ID and event eligibility before drawing the route. Both routes enter the same DB queue. On successful commit, update the beneficiary and create exactly one timestamped row per eligible request atomically. Write latency runs from request arrival to commit. |
| Outbox publisher | One logical FIFO worker claims rows from either route, waits for a simulated sink acknowledgement with the DB released, then acquires the DB to mark the row processed. Record commit, claim, acknowledgement and mark separately. Pool events across origins for all outbox sensor arms. |
| Large-account queries | An adjacent workload independently submits expensive queries against the same beneficiaries DB resource. Vary the arrival rate and duration of actual competing jobs. Record background offered work, DB waiting and work in service for the evaluator. |

SimPy schedules events and resource waits. The experiment specifies demand, scheduling and publisher behaviour. The single server represents a simplified shared processing bottleneck. A long job can delay a short job until the server is released. Conclusions about Aurora CPU scheduling, PostgreSQL locks or deployment-specific service costs require other evidence. Real Istio, Kafka, PostgreSQL, Kubernetes, chaos tooling, production CI integration, the wider service graph and transformer training remain outside scope.

### Expected work per offered request

Normalise DB capacity to one work-second per second. Let $b$ be expected background DB work offered per second, $\lambda$ the total eligible request arrival rate, $r$ the Java routing share, and $d_R,d_J$ the expected synchronous DB work of each route, including the same atomic outbox insert once. Let $d_P$ be expected DB work for claiming and marking one event. Sink acknowledgement time can occupy the worker but consumes no DB work in this model. The eventual total DB demands per eligible request are $D_R=d_R+d_P$ and $D_J=d_J+d_P$. Under the same input mix and background demand,

$$
\rho(r)=b+\lambda[(1-r)D_R+rD_J]
       =b+\lambda[(1-r)d_R+rd_J+d_P],\qquad
\Delta\rho=\lambda(r_1-r_0)(d_J-d_R).
$$

The increment compares proposed share $r_1$ with current share $r_0$. Common publication work affects headroom at both shares and cancels in this difference. The equation counts expected work owed by an arrival cohort assuming eventual commit and publication. To measure breach risk, the simulator must draw service times from the configured distributions, schedule work, and carry unfinished jobs across observation windows. A slower commit can change when a relay visit joins the queue and how long another write waits.

Treat $d_R$ and $d_J$ as configurable means for the two implementations’ synchronous service demands. The pilot represents differences in database access patterns through those workload parameters. All three configurations use the same business operation, event eligibility, atomic insert cost and publication mechanism.

| Workload configuration | Synchronous demand | Use |
|---|---|---|
| Equal-work placebo | $d_R=d_J$ | Required in the four-hour pilot. Control 1 also matches service draws, visit order and scheduling so that changing a route label alone has no effect. |
| Less-efficient rewrite | $d_J>d_R$ | Required in the four-hour pilot. Control 2 specifies a moderate increase. Control 3 tests whether background queries amplify its effect on pooled write-SLO risk. |
| More-efficient rewrite | $d_J<d_R$ | Optional subsequent control, outside the four-hour pilot. Increasing Java share reduces expected offered work. Use the same paired hold/increase comparison to test whether breach risk also falls. |

For the pilot every offered request is eligible. If a mixed population is introduced, use the all-request rate and average synchronous work over request classes, including the insert only for eligible writes. Multiply the relay term by the eligibility probability. Match the same class and eligibility draws across forks. If routing targets different classes or eligibility depends on route, estimate class-specific contributions explicitly before attributing a difference to synchronous cost.

### Causal-mechanism pilot and five controls

For each independent history, fork or deterministically replay to the same decision time. Carry outstanding writes, residual query work, pending commit times and the worker’s in-flight phase into both continuations. Compare holding the current share with increasing it over the same horizon. Pair arrivals, eligibility, route uniforms, background jobs and service draws by stable job identity within each continuation pair. Draw independent futures across pairs. Route-specific service transforms may differ in the migration condition. Preserve tie-breaking and queue discipline across routes.

| Control | Single change or comparison | Evidence and interpretation |
|---|---|---|
| 1. Equal-work placebo | Make synchronous service draws, DB visit sequence, priority and tie-breaking identical for Ruby and Java. Run the real common publisher in both forks. | With common draws the pooled write timings, event lifecycle and SLO indicators should match path by path. Only route labels may differ. Also exercise 0% and 100% Java and verify one real row per eligible commit at each extreme. Any physical divergence requires diagnosis. |
| 2. Genuine migration effect | Apply a predeclared moderate increase to Java synchronous service demand. Hold background demand at its reference level. | Record absolute breach risk under hold and increase, the paired difference and its uncertainty. Confirm the extra work in the synchronous visits. Both branches can have low breach risk if there is ample headroom. |
| 3. Background interaction | Repeat control 2 with a higher independent background-query rate or workload. Cross the same two shares with both background settings. | On the breach-probability scale compute the difference of the two routing effects, $\Delta R_{\rm high}-\Delta R_{\rm reference}$, with paired uncertainty. A positive value supports amplification in this regime. A high joint risk alone does not. |
| 4. Background-only overload | Increase background demand until the all-Ruby system is overloaded, then compare hold and increase from the same state. Check offered work and queue growth over the horizon. | Show absolute risk at 0% Java and both branch risks. Near the risk ceiling both branches may breach and the increment may be small, even if extra Java work still increases waiting. Report the measured increment. |
| 5. Publisher-only slowdown | Under a healthy DB at a fixed share, add off-DB acknowledgement delay. Keep request and query streams, claim/mark work and relay scheduling policy matched. Disable retries and extra polling in this control. | Seek a rise in pending age/count or commit-to-mark delay with healthy pooled writes. Verify DB waiting and write outcomes against the nominal sink before interpreting the trace. Backpressure can move or reduce relay DB visits. If DB pressure rises materially, the run has failed to isolate a publisher-only disturbance. |

**Evaluator and endpoint.** Score one binary outcome per continuation: a pooled application write-latency SLO breach within horizon $H$. Use all offered eligible writes on both routes, recording late writes even if still unfinished. The review’s pilot contract uses four consecutive 30 s windows, a 250 ms deadline from arrival and a breach when over 5% of eligible writes with deadlines in any window miss that deadline. Count only post-decision arrivals with deadlines within the horizon. An empty window cannot trigger a rate breach. Record denominators and show per-route latency as a diagnostic. Outbox age and delay are sensor readings throughout.

Estimate each branch probability using its breach frequency. Estimate $\Delta R$ using the mean paired difference in breach indicators. Show uncertainty intervals resampling independent root histories with their forks together. For the interaction, vary background at the fork from a common prefix, or predeclare regime-specific warm-ups and label the contrast accordingly. Record both branch risks, DB demand by workload, DB waiting, and outbox age on aligned time axes.

**Proceed to inference only after the causal check.** First pass an isolated stationary queue check, deterministic replay and outbox conservation (pending at end equals pending at start plus eligible commits minus marks, including in-flight rows once). Check commit ≤ claim ≤ acknowledgement ≤ mark. Require the placebo to pass and at least one predeclared contended comparison with a practically meaningful positive routing increment supported by the paired uncertainty interval. Freeze the smallest relevant risk increase and precision rule before the runs. Record flat and inconclusive contrasts as such. Additional independent histories can resolve sampling uncertainty. Changing thresholds after seeing the results would require a new, explicitly labelled experiment. The pilot deliverable is the five-control table and a decision on whether to proceed.

## State, observations and counterfactual forecast

- **Hidden target.** Use $X_t$ for exogenous background work offered per second. Its evolution is independent of the assigned route in the simulator. Routing changes foreground work and hence total contention. Demand, busy time and waiting are distinct quantities.
- **System memory.** Carry DB work remaining, pending event timestamps and publisher phase in the generator. A scalar demand can model the source of pressure while the queues retain memory. A future estimator must reconstruct uncertain queue state from its allowed history.
- **Known inputs.** Supply each method the same as-of-time information about offered workload, route allocation and proposed share. Keep true background demand, residual DB work, future shocks and future outcomes evaluator-only.
- **Three sensor configurations.** Compare pooled outbox only, conventional pooled request/write latency only, and both together, at the same cadence. Retain per-route latency as a diagnostic with sample counts. For the outbox use pending count, oldest pending age and completed commit-to-mark delay. Distinguish an empty queue from an interval with no completions. Pending ages give lower bounds on processing delays. Treat correlated sensors jointly and repeat with each outbox metric omitted.
- **Zero-information check.** All-Ruby traffic supplies normal outbox observations. For an uninformative observation history, start with an empty queue and idle publisher, and supply no eligible arrivals or outstanding writes from either route throughout the history. These outbox observations should leave the background belief at its prior predictive distribution.

After the pilot passes, evaluate the planned bootstrap particle filter with propagation, likelihood weighting, normalisation, effective sample size and systematic resampling when indicated. Specify its transition and observation approximation independently of the event generator. For a candidate share $r$ fixed through the horizon, define

$$
R(r)=P(\text{pooled write-SLO breach within }H\mid\mathcal I_t,\operatorname{do}(r),M),
\qquad \Delta R=R(r_{\mathrm{proposed}})-R(r_{\mathrm{current}}).
$$

Here $\mathcal I_t$ is the input and sensor history available to that arm through decision time $t$, and $M$ comprises the model, capacity assumptions and future workload law. Propagate uncertainty in both the present state and future workloads. Give all methods the same candidate weights and workload assumptions. Reserve higher shares from fitting and tuning. A concrete E2 design observes 5%, 10% and 25%, then compares holding 25% with stepping to 35% and 60%. Report the nearby and distant forecasts separately. Low-load telemetry may say little about capacity or an unforeseen background shock.

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
- **Required queue-only baseline:** model forecast based on observed arrivals and queue dynamics, to test whether particle filtering adds real value.
- **Particle-filter gate:** posterior predictive breach probabilities at candidate shares.

Evaluate Brier score and calibration for risk forecasts, missed unsafe promotions, false holds, lead time and computational cost. Compare combined telemetry against latency alone at matched episode false-alarm rates or fixed decision costs. Report missed warnings as well as lead times among detected breaches. Time to full rollout requires a separate repeated-decision policy and is deferred under the review’s time budget.

## Scientific safeguards and open assumptions

Fix generator semantics before tuning a forecaster. Split development, calibration and sealed test data by independent root history, keep all forks from a history together, and hold out a generator regime. Preserve shared random inputs across candidate branches and fresh futures across replicates. Score observational forecasts across independent histories. Only the evaluator may access the true state at each fork. Preserve the fixed-capacity publisher control, abrupt mismatch test and individual sensor ablations. A late sensor, an unidentifiable cause or a simpler method that wins are all acceptable results.

| Assumptions still open | Decision needed and consequence |
|---|---|
| Capacity and service work | Choose normalised capacity and service-time distributions before testing. Predeclare the moderate synchronous demand increase for the less-efficient configuration. The sign and size of the historical implementations’ demand difference are unknown. |
| Workload and relay timing | Choose nominal eligible request rate and mix, query duration/tail and persistence, nominal relay service/acknowledgement distribution and warm-up. Hold common work and route-independent eligibility fixed. These choices determine headroom and whether the sensor responds. |
| Detectable harm and precision | Confirm the proposed SLO windows, horizon, candidate shares, smallest consequential increase in breach probability, replication budget and paired interval rule before viewing the pilot results. Poor precision may leave the mechanism unresolved. |
| Subsequent inference | If the pilot passes, freeze priors, forecast law, likelihood, sensor bands, thresholds and decision costs on development data. Measure sensor lead time and incremental decision value on held-out data. The presence of a shared outbox establishes neither. |

## Work plan

The next implementation milestone is the four-hour causal pilot in the feasibility review. Protect the 3 December assessment. Release the later filtering, E1–E4, report and video work only on the evidence specified above. The course deadline is 24 December 2026. Deliver reproducible code, quantitative tables, plots, focused ablation, report and short video for the end-to-end study. Particle animation is optional. If the pilot is inconclusive, document the cause and precision before committing the remaining budget.

## Revision record

The 25 November clarification supersedes the 11 November Java-specific event path and the independent review’s Java-only work example, all-Ruby zero-event assertion, Ruby dummy publisher visits and zero-Java uninformative-sensor example. A change in route share now changes synchronous work while event eligibility and eventual publication work per eligible request are common. The write-latency breach resolves the earlier choice between write and delivery SLOs. The latency-only arm now covers both routes so both primary sensor arms observe the same application population. The independent review remains the record of the original feasibility assessment. [Feasibility review](particle_filter_feasibility_review.md)

## Literature starting points (verify in final report)

- Lindon, Sanden & Shirikian, *Rapid Regression Detection in Software Deployments through Sequential Testing* (2022): https://arxiv.org/abs/2205.14762
- Google SRE Workbook, *Canarying Releases*: https://sre.google/workbook/canarying-releases/
- Richardson, *Transactional Outbox*: https://microservices.io/patterns/data/transactional-outbox.html
- Debezium, *Reliable Microservices Data Exchange With the Outbox Pattern*: https://debezium.io/blog/2019/02/19/reliable-microservices-data-exchange-with-the-outbox-pattern/
- SimPy documentation: https://simpy.readthedocs.io/

## Future work deliberately excluded

Transformer-based discovery of undocumented behavioural contracts and local Markov-blanket-based counterfactual service impact is a **separate future research idea**, preserved in `lesson_logs/aims5701/research_brainstorming_2026_11_09.md`.
