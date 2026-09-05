# Probability and statistics foundations — historical JHU sequence

This directory records the probability/statistics foundation learned through Johns Hopkins Coursera study in late 2025, before the repository's numbered lesson workflow existed.

The historical record is split by **evidence strength** so that later retrieval stays honest:

- **Demonstrated / recoverable** — worked examples, questions, mistakes and explanations are recoverable from prior tutoring context.
- **Course-completed / weak chat evidence** — the learner remembers studying the topic and/or it belonged to completed coursework, but the worked trail is not recoverable enough to reconstruct confidently.
- **Future MSc extension** — material should be treated as new or needing deliberate reactivation regardless of historical course coverage.

The purpose is not to prove every line of the original JHU syllabus was mastered. The purpose is to preserve enough of the real learning path that familiarity can be rebuilt quickly and gaps can be tested rather than guessed.

## Durable retrieval records

1. `lesson_logs/historical_probability_statistics_01_counting_conditional_bayes.md`
   - counting/combinatorics, probability axioms, conditional probability, independence, total probability and Bayes;
2. `lesson_logs/historical_probability_statistics_02_random_variables_distributions.md`
   - discrete/continuous random variables, geometric distribution, PDF/CDF, expectation/variance and common distributions;
3. `lesson_logs/historical_probability_statistics_03_joint_expectation_variance_inequalities.md`
   - joint/marginal distributions, linearity of expectation, indicators, variance, covariance/correlation, Markov and Chebyshev inequalities;
4. `lesson_logs/historical_probability_statistics_04_clt_hypothesis_testing_and_evidence_boundary.md`
   - CLT, sampling distributions, standard error, Z-style hypothesis testing/p-values, plus explicit weak-evidence notes for Markov chains, Poisson and other late-course topics.

## Reconstructed demonstrated arc

```text
counting / sample spaces
→ probability axioms
→ conditional probability
→ independence
→ total probability / Bayes
→ discrete random variables
→ expectation / variance
→ continuous random variables
→ PDF / CDF
→ Uniform / Exponential / Normal
→ joint + marginal distributions
→ linearity of expectation / indicators
→ covariance / correlation
→ Markov + Chebyshev inequalities
→ CLT / sampling distribution of the mean
→ standard error / standardisation
→ hypothesis testing / p-values
```

## Known weaker-evidence historical coverage

The learner distinctly remembers studying **Markov chains** and **Poisson** material during the JHU sequence. Earlier historical notes also place these ideas in the advanced probability tail. However, the currently recoverable chat evidence is not detailed enough to reconstruct worked proficiency honestly.

Therefore these topics are recorded as:

```text
historically studied / likely course coverage
≠ demonstrated from recoverable tutoring evidence
```

A future cold retrieval should test them from first principles. If strong recall appears, the evidence state can be upgraded. If not, treat them as a short rebuild rather than assuming mastery.

## Why this matters for the MSc

This foundation is directly relevant to:

- AIMS5701 Bayesian networks, inference, sampling, HMMs and particle filtering;
- regression/classification uncertainty and evaluation;
- AIMS5704 probability prerequisites;
- expectation/variance/covariance notation;
- likelihood/MLE and exponential-family models;
- concentration/generalisation ideas;
- bandits and Bayesian reasoning;
- stochastic/generative topics later in ML Theory.

Probability/statistics remains a **higher-priority Term-1 retrieval lane** than linear algebra because it has had less recent practical use and is directly needed in AIMS5701 Weeks 4–5 and AIMS5704.

## Retrieval policy

Use cold retrieval before rereading.

1. Choose the smallest relevant historical log.
2. Ask one question at a time with changed numbers/examples.
3. Probe recorded misconceptions rather than generic textbook trivia.
4. Distinguish calculation slips from conceptual gaps.
5. For weak-evidence topics such as Markov chains/Poisson, explicitly treat the first session as a diagnostic rather than claiming prior mastery.
6. Stop once retention is clear; ordinary maintenance should be about 10–15 minutes.

## Evidence boundary

This is a conservative reconstruction from recoverable tutoring context and the learner's explicit recollection of completed JHU study. It is **not a transcript**, and it does not infer mastery from course enrollment/completion alone.

No historical exercise/test pair is fabricated because the original work was primarily conversational, handwritten and notebook-based. Later MSc-facing probability/statistics work should create new durable evidence as it happens.
