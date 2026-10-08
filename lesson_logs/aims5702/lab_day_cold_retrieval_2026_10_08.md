# AIMS5702 — Lab-day cold retrieval (8 Oct 2026)

**Source boundary:** conversational cold retrieval and changed-example repairs using the actual Lecture 1–3 decks; no assessed notebook used. This is learning evidence, not a grade or independent practical execution.

## Independently retrieved
- Training versus inference, minibatch learning on datasets exceeding GPU memory, generalisation/overfitting, validation versus test roles, hyperparameters versus learned parameters.
- Diagram to tensor shape and parameter counting: 5 → 4 → 2 network, 34 parameters; affine layer composition/no nonlinearity limitation.
- Right-aligned unequal-rank broadcasting: (4,1,5) + (3,5) → (4,3,5); matrix product shapes and einsum contraction; DataLoader 1000/128 → eight batches with final size 104.
- float16 versus float32 memory/performance trade-offs, bfloat16 range/precision trade-off; bit-to-byte slip repaired in-session.
- Chain-rule/backprop conceptual role; gradient accumulation and core zero_grad → forward → loss → backward → step sequence.
- Model-selection reasoning and generalisation gap; sample-weighted batch accuracy arithmetic.

## Incorrect cold or incomplete, then guided repair
- Image/video height-width order and audio as continuous 1D waveform; represented video as flattened tensor before prompt.
- Reductions: initially preserved reduced axis for mean; later recovered sum output shape but required scaffold for entry-wise summands.
- Integer indexing vs length-one slice: initial slice-length error, corrected on new example.
- Stepped slice: (5,6) original and [1:5:2,1:6:2] → shape (2,3) cold; incorrect stride (12,1) and offset 9. Reconstructed stride (12,2), offset 7, position y[1,1]=21 using recalled template. NOT delayed-independent.
- Transpose: initially believed non-contiguous means copy. After correction identified shared view and y[0,1] ↔ x[1,0].
- Cross-entropy: logits vs probabilities cold correct, but initially described one-hot as predicted argmax; repaired target semantics and -log(p_true) with changed probability example. Delayed independent check due.
- Gradient descent update: incorrectly inserted old-weight multiplication; corrected formula on changed numerical problem.
- model.train/eval/no_grad: initially conflated mode switches with running backward/updates. Understood dropout/batchnorm switch after teaching, and gave eval + no_grad after scaffold.
- Validation: needed guidance for argmax(dim=1), element-wise equality, sum().item(), tensor batch count and epoch aggregation. Rebuilt components interactively but NOT a cold full loop. This remains highest notebook-readiness gap.
- Lecture 1 advantages of DL (flexibility and ecosystem) and learned features needed cues; coding-style rationale for global-state avoidance needed explanation.

## Required follow-up
1. Once permitted and without using the assessed notebook: reconstruct a fresh complete small training + validation epoch, sample-wise accuracy and losses without hints.
2. Cold-check stepped-slice starts/steps/counts; transpose view; indexing and reduction semantics on unseen examples.
3. Mixed oral Q&A without topic cues: one-hot/cross-entropy, gradient update, mode vs grad context, representations/dtypes and generalisation.
4. In-class notebook: verify specific AI-use permission before actual assessed-work assistance. Confirm saved upload, TA verification, running demonstration, recorded mark, and UReply attendance.

**End boundary:** 50 numbered questions were reached, but some involved follow-ups and repairs; the planned separate mixed oral simulation and final delayed gap-repair block were not completed. Do not promote coached performance into durable mastery.
