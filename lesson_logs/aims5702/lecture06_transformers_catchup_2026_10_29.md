# AIMS5702 — Lecture 6 Transformers catch-up — 29 October 2026

## Source and boundary
Source: uploaded CUHK AIMS5702 Lecture 6 Transformer PDF (99 pages). This was a guided catch-up for a missed lecture, **not** attendance at the live class or evidence of delayed exam mastery. Lecture 7 Model Inference slides were inspected for orientation only; the learner had not yet attended the evening lecture at this handover.

## Coverage
- Slides 12–25: translated chain rule/backprop notation into upstream gradient × local derivative; elementwise add, ReLU, multiplication, linear input/weight/bias gradients and batch summations. Learner correctly interpreted partial derivatives and explained input gradients sum across affected outputs, while shared parameter gradients sum across batch examples.
- Slides 26–31: convolution gradient indexing and weight sharing. Interactive original-image/kernel/output/upstream-gradient visualisations supported the distinction between input-gradient accumulation (output gradient × matching kernel weight) and kernel-gradient accumulation (output gradient × original input). Learner correctly explained summing spatial contributions and output channels, and independently stated partial-differentiation rule (hold other multiplicand constant). Formal summation notation required translation.
- Slides 32–35: ResNet degradation problem and both slide-35 motivations: identity shortcut provides an alternative gradient path; residual branch learns a correction and can approach zero. Learner articulated this after clarification.
- Slides 36–43: CNN receptive-field and large-kernel weight-cost limitation; RNN carries context but sequential dependencies limit parallelisation. Learner explained these independently.
- Slides 44–67: attention intuition, query/key/value roles, dot products, QK transpose, learned projections, softmax weighted values, self vs general/cross attention. Learner successfully constructed Q/K/V from a provided 2×2 X and three projection matrices with two individual arithmetic repairs, then S=QKᵀ with one repaired entry; recognised stable softmax subtraction trick; final AV weighted-vector arithmetic was corrected by tutor. This was an **unseen same-session changed numerical example**, not independent error-free whole-pipeline completion.
- Slides 68–81: complexity N² pair comparisons × D features, N D² projection work, shared parameter count O(D²) vs quadratic attention work; path length vs total work; multiple heads learn distinct relationships. Learner correctly explained N² and D and multi-head purpose.
- Slides 82–95: why positional information matters, added position vectors, desired encoding properties, sine/cosine pattern and richer feature mapping. Conceptual recognition demonstrated; detailed sinusoidal mathematics not independently tested.
- Slides 96–98 (RoPE, attention + FFN architecture, PyTorch layer): **not studied in detail**. Lecture 7 quantisation slides 28–36 received a short high-level pre-lecture orientation only (fewer-bit numbers, scale/round/clip, PTQ vs QAT, memory-speed/accuracy trade-off).

## Strongest evidence
- When operations were visualised or written numerically, learner could reason about their mechanics and explain architectural motivations in their own words.
- Learner explicitly spotted that an exercise starting from given Q/K omitted input projections and requested a whole-pipeline example from X.
- Recognised that identical attention-weight rows imply identical weighted outputs.
- Identified own central gap accurately: successful stepwise computation does not transfer automatically to reading compressed mathematical notation on slides. Specifically, o_i and sum_j alpha_ij v_j initially appeared illegible despite completing the same operation numerically.

## Fragilities / calibration
- **Notation-to-operation translation is the highest-priority gap**, more than conceptual inability: indices i/j, summation ranges, matrix orientations, and tracking multiple nested operations in one expression.
- Some arithmetic slips in 2×2 products and AV; tutor corrections were needed. Do not mark independent QKV mastery or cold retrieval.
- Conceptual grasp of positional encoding; sine/cosine/RoPE derivations not fluent.
- Significant cognitive fatigue after extended intensive study, with evening lecture still scheduled. Protect recovery; no immediate further math drilling.
- Effective format: complete persistent worked example with input X, WQ/WK/WV, Q/K/V, scores, softmax, values/output **all simultaneously visible**; clickable cell-level explanations; then an unseen whole example. Hiding prior steps forced constant backtracking and impaired comprehension. Prefer translation of lecturer notation into plain English and labelled concrete matrices before more numerical drills.

## Next useful session
1. Brief *cold* reading exercise: identify indices and translate o_i = sum_j alpha_ij v_j, QKᵀ and softmax(...)V into sentences; do not immediately recalculate a full pipeline.
2. One changed small QKV problem with persistent matrix panels, independent computation and minimal prompting; check shapes and softmax/AV carefully.
3. Close slides 96–98 (RoPE and attention + FFN), only when recovered.
4. After Lecture 7 attendance, assess actual inference/quantisation understanding rather than treating the orientation as completed learning.
5. Prepare for AIMS5702 MCQ-style quiz on 12 Nov with spaced recognition/translation and selected short calculations.
