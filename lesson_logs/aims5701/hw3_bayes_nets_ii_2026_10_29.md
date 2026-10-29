# AIMS5701 HW3 — Bayes Nets II: inference and sampling (27–29 Oct 2026)

## Delivery
Learner explicitly confirmed **HW3 submitted on 29 Oct 2026**. Six problems attempted and an eight-page write-up reviewed before submission. The provided assignment PDF displayed an outdated 19 Oct deadline; the learner described a later short window and a shared three-day extension allowance across five homeworks. **Do not infer an official revised due date or extension usage** from this session; submission is learner-reported.

## Session and assessment boundary
AI tutoring used different networks/contexts/numerical CPTs for worked demonstrations and independent analogous practice. The learner then worked on the assessed questions, requested targeted procedural and final-result checks, and produced their own write-up. Some assignment-specific results and corrections were supplied during checking. This is **assisted assessment work**, not pristine unseen evidence or delayed independent mastery. Original unedited AI transcript receipts are required by the assignment policy; this log is not a replacement.

## Learning evidence
- **Q1 variable elimination:** learned factor scopes (join=union; eliminate=remove summed variable), evidence instantiation as selecting rows, CPT complements, joins and two successive sum-outs, and final normalization. Completed an analogous one-hidden-variable problem and two-elimination example, with bookkeeping corrections. Actual Q1 factor tables and two-elimination arithmetic eventually reconciled; initial CPT lookup errors and a wrong eliminated variable exposed high risk from 0/1 row selection.
- **Q2 enumeration:** transferred fork-factorization, hidden-parent marginalization, numerator/denominator and conditioning. Changed practice completed after correction for complement lookup and division; assessed Q2 independently attempted and checked, with a temporarily omitted normalization.
- **Q3 prior/rejection sampling:** correctly explained topological prior draws, acceptance as matching evidence, accepted-count posterior as number qualifying / accepted total, without multiplying by evidence likelihood again. Produced eight-row marginalization over three binary variables; one calculator input, not CPT selection, caused discrepancy.
- **Q4 likelihood weighting/ESS:** understood evidence fixed rather than rejected, weights of evidence conditional on sampled parents, numerator=sum of query-qualifying weights, denominator=all weights, ESS=(sum weights)^2/sum squared weights. An analogous sample weight lookup was corrected; completed Q4 calculations with ESS rounded to two decimals.
- **Q5 Gibbs/Markov blanket:** identified parent/child/co-parent structure on changed graph, evaluated both candidate values with local factors and normalization, related Gibbs flip to normalized resampling probability. Distinguished local conditional (full current blanket) from target posterior conditional only on evidence. Recognized Q5(c) as common-parent enumeration after removing an unobserved leaf factor.
- **Q6 Markov transitions:** moved from graph outgoing arrows to transition matrix rows, identified unit starting vector, and propagated row-vector distributions via pi(t+1)=pi(t)P for one/two/three steps. Completed an unseen three-step analogous problem. Matrix notation/row-vs-column and arithmetic were clarified; repeated assistant numerical mischecks required corrections.

## Final write-up review
Eight-page PDF checked against problems. Final numerical values appeared consistent, but review identified notation/presentation issues: Q3(a) marginalization equality/summation direction, Q4(a) displayed estimator denominator (should be sum of all weights), Q1(c) heading misnumbered, Q2(b) conditional parentheses typo, and Q3 table typo/rounding. Learner discussed Q3(b) justification and **reported submission**, but did not upload a corrected final PDF after review; do not claim all fixes were confirmed applied or that declaration/transcript appendix was audited in the submitted artifact.

## Future cold-retrieval prompts (changed contexts, unseen values)
1. Given an abbreviated binary CPT and evidence, expand complementary rows and build factor scopes; join/sum out two variables with checks.
2. From a Bayes-net graph and conditional query, factorize, identify hidden variables, enumerate a small table and normalize without prompting.
3. Explain acceptance probability versus rejection-sampling estimate; compare to weighting estimator and ESS.
4. Derive local Gibbs two-value conditional from Markov blanket, then distinguish it from marginal posterior conditioned on evidence only.
5. Convert a three-state directed transition graph into a row-stochastic matrix and propagate distribution three steps with a check each vector sums to 1.

## Next work
Return to AIMS5702 CNN assignment and missed Transformers lecture, with upcoming 5702 quiz (12 Nov) and 5701 midterm (18 Nov) requiring **homework-shaped, delayed cold retrieval** across Search, Bayes nets, HMM and particle filtering. Avoid redoing HW3 immediately; schedule selective changed-problem retention checks.
