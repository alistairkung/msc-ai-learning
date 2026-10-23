# AIMS5702 — Assignment 3 backpropagation refresher and implementation — 23 October 2026

## Scope / source boundaries
Assignment 3 notebook: Part A manual gradients for multiplication, multiplication+ReLU, linear+ReLU and convolution; Part B progressively deeper CNNs and residual/projection shortcuts. Assignment due 29 Oct. This log reflects tutoring and learner-reported local notebook work, not a stored copy of the submitted notebook or independent verification of unreported tests.

## Observed progression
- Recovered derivative-as-local-sensitivity, the scalar chain rule and cumulative upstream gradients on changed examples. Initially omitted the loss-to-output factor when moving beyond a simple chain, then independently reconstructed complete forward/backward passes.
- Recovered branching rule: multiply derivatives **along** a computational path and add gradient contributions **across** paths. A sum-versus-product slip was corrected; a later changed scalar example including ReLU was solved without conceptual help.
- **A.1:** independently derived both input gradients for elementwise multiplication, coded the method with only a typo correction, and explicitly reported that the supplied test passed.
- **A.2:** independently derived multiplication+ReLU gradient expressions and produced a correct NumPy implementation, with a small missing-comma syntax repair. Supplied tests were **not reported as passed** in this conversation.
- **A.3 mathematics:** independently solved a scalar linear+ReLU example with input, weight and bias gradients, then a 2-input/2-output analogue on paper after initial derivation scaffolding. All forward values, local derivatives, weight/bias gradients and accumulated input gradients were ultimately correct. Connected those scalar computations to the matrix formulas under the notebook's row-batch convention.
- **A.3 matrix/batch translation:** memorised and retrieved `G W` for input gradients, `G^T X` for weight gradients and column-wise batch sum of `G` for bias. Still confused ReLU mask over input vs preactivation/output, `*` versus `@`, list extraction, weight transposition in the forward pass, and shape interpretation when coding. A.3 forward/backward not confirmed passing; parameters not yet implemented.
- **A.4** and **Part B** not started in this session.

## Reliable anchors
Forward (row-batch convention): `Z = X @ W.T + b`, `A = ReLU(Z)`.
Backward: `G = output_gradient * (A > 0)`, then input `G @ W`, weight `G.T @ X`, bias `G.sum(axis=0)`. These are *study reference formulas*, not evidence that the learner wrote or tested the complete implementation.

Shapes: `X(B,I)`, `W(O,I)`, `Z/G(B,O)`; expected gradients `dX(B,I)`, `dW(O,I)`, `db(O,)`. Use the shape contract to repair transpose mistakes. The learner can explain the scalar graph but finds the computational graph difficult to visualise after matrix notation compresses its paths.

## Tutoring calibration / next
- The learner explicitly prefers **one coherent fully worked example (ideally sliders) then one unseen complete attempt**. Fragmenting into a long sequence of tiny leading questions causes loss of the overall computation; giving successive code-line hints feels like being led to the answer.
- Do not repeat the full scalar derivation. Provide a compact anchor of the whole computation, then let the learner independently write the A.3 methods. Diagnose concrete shape/operator errors rather than repeatedly prompting one line at a time. Respect learner ownership of assessed implementations.
- First verify A.2's tests, then complete A.3's forward, input and parameter-gradient methods, and run supplied checks. Next begin A.4 with one small convolution gradient trace before coding. Part B needs GPU/training runs and remains untouched.
- Deadline planning: wedding 23–24 Oct local US, travel from San Francisco Sun 25 Oct arriving Hong Kong Tue 27 Oct, with patchy in-flight internet. Do not assume full travel days or turn wedding time into mandatory study. Original 8-hour completion target was revised upward because mathematical groundwork and CNN experiment runs take longer.

## 24 Oct follow-up — Part A passes; independent convolution reconstruction parked

Learner confirmed **all four A.1–A.4 notebook tests passed**. This supersedes the unverified A.2–A.4 implementation status in the earlier session log. It is learner-reported passing-test evidence, not proof of delayed independent reconstruction.

**A.4 difficulty and productive visualisation:** A.4 was experienced as extremely challenging and relied on considerable guidance. Three aligned, interactive tensors — input X, kernel K and output/upstream gradient G — were decisive: selecting a kernel placement and highlighting the corresponding input window, kernel position and upstream gradient made the local contribution and accumulation interpretable. There is now an operational understanding of kernel-gradient gathering (one fixed weight, all placements), input-gradient scatter/overlap (one fixed pixel, all placements covering it) and bias-gradient summation.

**Remaining gap:** Generalising one pictured convolution window to the full four-dimensional algorithm, identifying destination versus accumulation dimensions, handling multiple batch/channel indices, matching slices, broadcasting across the batch, and choosing sum versus indexed addition. Assembled, passing NumPy code followed sustained scaffolding. Do not score this as unassisted implementation fluency.

**Explicit post-deadline return (after 29 Oct, no immediate assessment pressure):**
1. Start with a side-by-side input X / kernel K / upstream gradient G slider and have the learner describe *which variable's gradient is being tracked*, which window/pair contributes and why.
2. Work a small changed unseen problem: one kernel weight, one corner input pixel, one centre pixel and one bias. Show each contributing path and running accumulation.
3. Before coding, specify result shape; indices identifying one result; axes that accumulate; and axes NumPy can process together.
4. Generalise stepwise to batch, input/output channels, padding, slices, broadcasting and reductions, then independently reconstruct a small convolution backward routine against changed-shape tests.
5. Retest after a delay, distinguishing cold unaided completion from guided repair.

**Immediate priority:** Part B architectures/training and assignment submission; do not revisit A.4 in depth until assessment pressure is over.
