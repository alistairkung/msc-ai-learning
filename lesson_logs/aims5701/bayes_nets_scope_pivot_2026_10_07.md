# AIMS5701 — HMM introduction paused after Bayes Nets scope update — 2026-10-07

## Session purpose

Begin preparation for the next AIMS5701 lecture using the current handover. The
session initially followed the tentative Week 4 plan, but the learner reported
that the newly released lecture slides continue Bayes Nets. The HMM/particle
filter preparation was therefore paused before treating it as the live course
scope.

## Guided pre-study completed

The learner was introduced from first principles to:

- an HMM as a hidden state sequence plus visible observations;
- transition probabilities between hidden states;
- emission probabilities from hidden states to observations;
- exact filtering as prediction through the transition model followed by an
  observation update and normalisation;
- particle filtering as transition, observation weighting and resampling;
- the distinction between a particle's likelihood/compatibility weight and the
  resampled particle population;
- why more particles generally improve an approximation while increasing cost.

The weather/umbrella example was used to calculate two prediction/update cycles.
The learner independently calculated the prediction and Bayesian normalisation,
understood that no-umbrella evidence favours sun, and reconstructed the
transition → observe → weight → resample loop after correction.

## Evidence boundary

This is **same-session guided introductory evidence**, not delayed or
independent HMM mastery. The learner explicitly identified that filtering,
weighting and resampling were becoming fuzzy and benefited from diagrams and
small concrete examples. Decoding/Viterbi and other extensions were introduced
too early and were explicitly parked.

No live lecture coverage should be inferred from this session. The learner then
reported that the newly released slides still cover Bayes Nets, so the immediate
course-facing priority returns to reconciling the actual Bayes Nets material.

## Next step

Read/reconcile the new Bayes Nets slides, then use one small retrieval sequence:
DAG/CPT semantics, local factorisation, conditional-independence structures and
one changed d-separation example. Keep HMM/particle filtering as deferred
runway until the live teaching sequence actually reaches it.
