# AIMS5701 particle-filter project — initial development findings and investigation handover

**Recorded:** 25 November 2026  
**Status:** First particle-filter development implementation merged; method lock **withheld**. Likelihood correction for issue #15 approved for implementation, **not yet validated**. Protected evaluation **not generated or accessed**.  
**Internal completion target:** 15 December 2026; module deadline 24 December 2026.  
**Implementation:** [particle-filter-deployment-gate PR #14](https://github.com/alistairkung/particle-filter-deployment-gate/pull/14), merged; [tracking issue #12](https://github.com/alistairkung/particle-filter-deployment-gate/issues/12).  
**Primary evidence:** [Development report](https://github.com/alistairkung/particle-filter-deployment-gate/blob/2b492da/particle_filter/results/development/README.md), [teacher-forced diagnosis](https://github.com/alistairkung/particle-filter-deployment-gate/blob/2b492da/particle_filter/results/development/TEACHER_VALIDATION.md), [structural-refactor equivalence](https://github.com/alistairkung/particle-filter-deployment-gate/blob/bb15f9b/particle_filter/results/structure-refactor/README.md).

## Research question and current boundary

Can a bootstrap particle filter infer hidden shared-database conditions from time-causal transactional-outbox readings, then predict the risk of increasing Java traffic from 25% to 60% better than a simpler temporal-history predictor?

The frozen SimPy environment contains one non-preemptive FIFO DB bottleneck, equivalent functional writes with route-dependent synchronous work, independent expensive background queries, and a shared outbox relay. A, B and C represent normal operation, increased background DB query demand, and slow downstream publisher acknowledgement. The controller sees outbox readings `(M,N,A,D)` every five seconds (completed marks, pending rows, oldest pending age, median completed publication delay); it does **not** see the evaluator's physical queue, regime label or future workload.

At the cut, the compact approximate hidden state is `X=(Z,W)`: regime and unfinished DB work. Posterior draws feed paired stochastic 120-second hold/promote futures. An action breaches if **any** nonempty 30-second window contains strictly more than 5% of eligible application writes that miss their 250 ms deadline. The key forecast is the signed increment `R_promote − R_hold`.

The feasibility and telemetry-sufficiency studies were completed before this implementation. The present log concerns the **first PF development results**, not final protected evaluation.

## First development implementation and validation

PR #14 implemented the bootstrap PF, fitted counts-first joint likelihood, time-causal inference, matched posterior-predictive forecasts, four direct baselines, regime-conditional cut-work ablation, half-life sensitivities, tests and development evidence. It was reorganised for researcher navigation into `particle_filter/model/` (regimes, approximate FIFO physics, likelihood, distributions, support), `filter.py`, `forecast.py`, `experiment.py` and `evaluation.py`. The refactor reported exact scientific-content equivalence for 37 development artifacts, with expected changes only to path-dependent fingerprints and runtime/provenance. The implementation passed 211 repository tests in the reported run. **Passing software tests did not establish scientific validity.**

### Development validation findings

| Diagnostic | Observed result | Interpretation |
|---|---|---|
| Teacher-forced observation likelihood | 1,200 development roots, 14,400 five-second intervals, five root-disjoint folds. All observations had finite log mass; 17 repeated frequency/serial-residual flags. | Conditional observation probabilities remain inaccurate even when supplied with the simulator's true development hidden state; this cannot be fixed merely by increasing particles. |
| Slow-publisher backlog tail | In three flagged C folds, model predicted high-backlog frequency **15.0–16.0%** versus **8.3–9.0% observed**. | Dominant likelihood calibration discrepancy. |
| Sequential filter diagnostics | 36 held-out development roots; 21 frequency/serial-residual flags. PF cut-work RMSE **47.7 ms** versus **58.6 ms** for the diagnostic using the true regime's development mean. | Possible useful hidden-work information, but no established gain for rollout decisions. |
| Particle doubling | 128 to 256 particles failed stability criteria. Maximum RMS cut-regime probability change **0.438 in C** (allowed 0.03); cut mean-work RMS change **0.0149 s** (allowed 0.01 s). | Numerical convergence is unproven; cause still to investigate. |
| Publisher-phase diagnostic | On 13,967 supported intervals, revealing phase/acknowledgement residual changed absolute mark-count error by **−0.011 marks** (95% interval −0.029 to 0.006); 433 lacked compatible donors. | No clear benefit for this specific mark-count diagnostic; omitted phase cannot yet be ruled out generally. |

### Initial forecasting scores — development only

36 root-disjoint held-out histories, 128 particles, 64 matched forecast pairs per root:

| Predictor | Signed-increment MSE ↓ | Hold Brier ↓ | Promote Brier ↓ |
|---|---:|---:|---:|
| Full PF pipeline | 0.19915 | 0.17369 | 0.20299 |
| PF with regime-conditional cut work | 0.19906 | 0.17394 | 0.20283 |
| Temporal outbox history | **0.19106** | **0.14272** | **0.17788** |
| Complete current snapshot | 0.19571 | 0.18130 | 0.19274 |
| Oldest pending age | 0.19956 | 0.19236 | 0.19197 |
| Action-only prior | 0.21145 | 0.24324 | 0.20060 |

The predeclared primary **temporal-minus-full PF** gain in signed-increment MSE was **−0.00809**, paired development 95% interval **[−0.02729, +0.01153]**. The **ablated-minus-full** difference was **−0.00009**, interval **[−0.00220, +0.00204]**. Both cross zero: **neither PF superiority nor equivalence is established**. The nearly identical backlog-ablation scores also do not establish that accurate workload information is useless: the estimate could be inaccurate, the outcome could be insensitive, or precision inadequate.

## Three GitHub investigation issues

1. **[#15 — Observation-likelihood calibration](https://github.com/alistairkung/particle-filter-deployment-gate/issues/15)** (first, scientific blocker): reproduce the teacher-forced failures, isolate the incorrect conditional law, make the smallest scientifically justified correction, rerun root-disjoint development calibration and document residual failures.
2. **[#16 — Particle stability and convergence](https://github.com/alistairkung/particle-filter-deployment-gate/issues/16)** (second, numerical blocker): investigate ESS, concentration, resampling, regime extinction, seed effects and bounded particle-count convergence. Adding particles cannot repair systematic likelihood bias. Retain runtime and memory receipts.
3. **[#17 — Forecast performance and backlog contribution](https://github.com/alistairkung/particle-filter-deployment-gate/issues/17)** (third, interpretation): after the first two investigations, reassess the PF versus temporal-history primary comparison and the regime-preserving `W` ablation on development histories. A negative or inconclusive result is legitimate. A true-`W_0` oracle and comparison of early versus late 30-second windows are **optional explanatory diagnostics**, not additional required experiments.

The original [issue #12](https://github.com/alistairkung/particle-filter-deployment-gate/issues/12) remains the overarching implementation/method-lock tracker.

## Issue #15 — reproduction, deeper diagnosis, approved correction

A follow-up rerun of merged `main` at `2b492da` exactly reproduced the **14,400 interval records** and all **17 repeated teacher-forced flags** across the 1,200 development roots. This is evidence of a repeatable likelihood misspecification, not a one-off seed artifact.

**Dominant defect — positive pending excess under slow publishing:** with fresh prior count `N_start`, new commits `C_new`, and completed marks `M`,

```text
N_end = N_start + C_new − M
minimum feasible ending pending = max(0, N_start − M)
positive excess = N_end − minimum feasible ending pending
```

When inherited rows cover all the marks (`M <= N_start`), positive excess is **exactly `C_new`**. Under the last five C intervals, actual new commits averaged **200–201 per five seconds** with standard deviation **14–15**. The fitted excess mean drifted **193 to 253**, with predictive standard deviation **169 to 221**. The existing regression allowed accumulated pending backlog to drive the fitted positive-excess count; its dispersion was shared across regimes. Conditioning on actual marks and forcing the hurdle open barely changed the tail gap. This is direct evidence of **conditional count-law misspecification**. No replay/support/alignment defect explained it.

**Other unresolved likelihood defects:** in two C folds with oldest pending age in `(2,5]` seconds, **65.4%** of median completed delays fell in `(0.5,2]` seconds versus roughly **53% predicted**. Reference and elevated-background histories also exhibited conditional delay errors. Mark residuals had negative lag-one products in all A/B folds; pending residuals had positive lag-one products in all C folds and two B folds. Oldest pending age had no repeated teacher-forced flag. These timing and serial issues remain open even if the dominant count tail is repaired.

**Approved *proposed* correction (not yet implemented/validated at the time of this log):** change **only** the positive-excess component for a hypothetical **regime C particle with a fresh starting pending count**. Fit a regime-C-specific negative-binomial law for *implied new commits*, with its own dispersion, then map probabilities back to ending pending/excess through conservation and the existing hurdle/support constraints. For stale or missing starting counts, retain the existing law. Do not introduce a new latent state, intervention clock, estimator or altered simulator physics.

**Important edge case:** if `M > N_start`, some newly committed rows must have been marked within the interval. Then excess is **not** equal to the number of new commits; the mapping must handle the lower bound, truncation, zero excess and correct normalisation. Example: starting 10, new commits 200, marks 50 yields ending pending 160, not 200.

**Approved bounded validation:** deterministic conservation/truncation/normalisation tests; refit on the same five root-disjoint development folds; check conditional log score, observed-mark and mark-integrated tail error, penultimate and final C intervals separately; repeat teacher-forced and sequential diagnostics; check material regressions in A/B; report remaining delay and serial flags. **Select based on held-out likelihood validity, not whether the PF wins the forecasting comparison.** Obtain independent scientific verification before considering method lock.

### Intuition captured during discussion

- **A larger inherited backlog does not imply more incoming commits.** For example, 800 pending + 200 commits − 40 marks = 960 pending; 1,500 pending + the same 200 commits − 40 marks = 1,660 pending. New commits remain 200. The revised likelihood seeks to stop a large accumulated backlog from inflating the model's prediction of new incoming commits.
- **Pending events and slow marks don't uniquely identify DB contention.** Slow downstream acknowledgement can accumulate rows while the app DB remains healthy, and can reduce publisher claim/mark visits to the DB.
- **Particle noise versus model bias:** more particles can reduce Monte Carlo approximation error, not fix incorrect conditional observation probabilities.
- **State inference versus decision benefit:** a wrong cut backlog may shift both absolute hold/promote breach risks similarly and partly cancel in signed incremental risk. Better hidden-state RMSE does not automatically mean better deployment choices.
- **Short effects can determine long endpoints:** even if initial DB backlog dissipates quickly, it can trigger the first of four 30-second breach windows and hence the entire 120-second binary endpoint. Window-specific diagnostics can help explain, but must not change the frozen endpoint.

## Next actions and guardrails

Complete #15's bounded diagnostic correction and independently verify before treating likelihood calibration as resolved. Then address #16 numerical stability; use #17 to evaluate forecasting consequences, not to force a positive PF result. Preserve the frozen simulator, controller/evaluator information separation, paired future draws, root-disjoint training/development evaluation, four locked direct baselines, main queue-state ablation, named half-life sensitivity variants and source/evidence manifests.

**Method lock remains withheld. Protected evaluation remains closed.** The existing 300-root protected plan (100 each A/B/C) requires separate owner authorisation after validation and budget lock. If the PF is well validated but performs no better than temporal history, report that negative result honestly. If validation cannot pass within the MSc project budget, report the limitation rather than weaken the gates.
