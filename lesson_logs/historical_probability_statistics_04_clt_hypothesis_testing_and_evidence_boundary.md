# Historical probability/statistics 04 — CLT, hypothesis testing and evidence boundary

**Status:** Historical reconstruction with strong evidence for CLT/testing; explicit weak-evidence section for some late-course topics  
**Period:** Late November 2025  
**Format at the time:** Interactive chat + Coursera study + pen-and-paper/notebook work

## Learning objective

Understand how repeated sampling creates a distribution of statistics, use the central limit theorem to standardize sample means, then connect that machinery to hypothesis testing and p-values.

## Reconstructed progression

### 1. Sampling distributions

A key conceptual move was distinguishing:

- the distribution of the **raw observations**;
- the distribution of a **statistic computed from repeated samples**, especially the sample mean.

This distinction was central to understanding the CLT.

### 2. Central limit theorem

For iid observations with finite variance, the sample mean becomes approximately Normal under broad conditions as sample size grows.

The key historical correction was:

> The CLT says the **sampling distribution of the sample mean** becomes approximately Normal; it does not say the original raw data itself becomes Normal.

The working approximation was:

```text
X_bar ≈ Normal(μ, σ²/n)
```

with standard error:

```text
SE(X_bar) = σ / sqrt(n)
```

### 3. Standardization

A sample mean can be expressed in standard-error units relative to a hypothesized/population mean:

```text
Z = (X_bar - μ) / (σ / sqrt(n))
```

The important interpretation is:

> How many standard errors away from the reference mean is the observed sample mean?

This connected the probability model to inference.

### 4. Hypothesis testing

The historical sequence rebuilt hypothesis testing underneath a procedure the learner had used before in SPSS.

Core structure:

```text
H0 / HA
→ choose significance level α
→ compute test statistic
→ obtain p-value under H0
→ reject or fail to reject H0
```

The learner had prior procedural familiarity with “compare p to 0.05”; the JHU work made the probability meaning underneath this workflow explicit.

### 5. p-values

The p-value was interpreted as the probability, **assuming the null hypothesis/model**, of observing a result at least as extreme in the relevant direction(s) as the one obtained.

Important safeguards:

- it is not `P(H0 is true)`;
- failing to reject is not proof that `H0` is true;
- one-sided/two-sided framing affects what counts as “at least as extreme”.

### 6. Recoverable worked example

A representative historical example used:

```text
μ0 = 100
n = 49
X_bar = 104
s = 21
```

The standard error was:

```text
SE = 21 / sqrt(49) = 3
```

and the standardized statistic:

```text
Z ≈ (104 - 100) / 3 ≈ 1.333
```

A one-tailed p-value was around `0.0918`, so at `α = 0.05` the result would not be statistically significant.

The exact numbers are not retrieval targets; the conceptual pipeline is.

## What was understood well

The learner developed a meaningful link between probability distributions and the statistical-testing workflow previously used procedurally.

The strongest conceptual anchor was that inference reasons about where an observed statistic lies inside a **sampling distribution under a reference model**.

## Known fragile points

1. **Raw distribution vs sampling distribution** — the CLT concerns the latter.
2. **Standard deviation vs standard error** — `σ` describes individual observations; `σ/sqrt(n)` describes variability of the sample mean.
3. **Meaning of a Z/test statistic** — distance from the null/reference value in standard-error units.
4. **Meaning of p-value** — probability of data/extremeness under `H0`, not probability the hypothesis is true.
5. **Reject vs fail to reject** — do not turn “insufficient evidence” into acceptance/proof.
6. **One-tailed vs two-tailed tests** — the alternative determines the relevant tail area.

## Cold-retrieval blueprint

1. Ask what distribution the CLT is talking about.
2. Given `μ`, `σ` and `n`, compute/interpret the standard error of the mean.
3. Give a sample mean and ask for its Z-score relative to a null mean.
4. Ask what a Z-score of `2` means in plain English.
5. State `H0`, `HA` and `α` for a small scenario.
6. Give a p-value and ask for the correct decision language.
7. Ask explicitly: “Does `p=0.03` mean there is a 3% chance H0 is true?”
8. Ask what changes between one-tailed and two-tailed testing.
9. Connect the workflow back to why repeated-sampling distributions matter.

## Rebuild sequence if cold recall is weak

```text
sample → statistic
→ imagine repeating the sample
→ sampling distribution
→ CLT for sample mean
→ standard error
→ standardize against H0
→ tail probability / p-value
→ evidence-based decision
```

## Evidence boundary for later JHU topics

### Markov chains — remembered study, weak recoverable worked evidence

The learner distinctly remembers studying Markov chains. Historical context also places Markov-chain ideas in the late advanced sequence, including state/transition-matrix intuition and the Markov property. However, the currently recoverable conversation evidence is not strong enough to document worked calculations such as multi-step transition probabilities or stationary distributions as demonstrated mastery.

Future treatment:

```text
historically studied
→ cold diagnostic from first principles
→ upgrade to established if retrieved successfully
→ otherwise short rebuild
```

### Poisson material — remembered study, weak recoverable worked evidence

The learner distinctly remembers studying Poisson material. The current recovered chat trail is not sufficient to establish which aspects were worked deeply (Poisson distribution, Poisson process, waiting/event-count relationships, etc.).

Do not infer detailed mastery from the course memory alone. Test it when relevant.

### Confidence intervals / additional inference

The reconstructed record is strong for CLT, standard error, standardized tests and p-values, but weaker for a detailed confidence-interval exercise trail. If later MSc work needs confidence intervals, begin with a cold diagnostic rather than assuming automatic retention.

### Course completion boundary

By late November/early December 2025, historical records describe two JHU probability modules as completed. That establishes **course exposure/completion**, not uniform demonstrated mastery of every syllabus topic.

This file intentionally records the distinction rather than filling missing chats with generic course content.

## Mastery signal

For the demonstrated portion, retrieval is strong when the learner can explain sampling distributions/CLT correctly, compute and interpret standard error, standardize a sample mean, explain a p-value and make a statistically correct reject/fail-to-reject statement.

Markov chains and Poisson remain **diagnostic-needed** until new evidence is created.

## Bridge forward

```text
CLT / inference
→ likelihood and MLE
→ Bayesian/frequentist modelling language
→ concentration / generalisation bounds

historically remembered Markov/Poisson
→ targeted diagnostic
→ HMM / particle filtering / stochastic models when MSc invokes them
```
