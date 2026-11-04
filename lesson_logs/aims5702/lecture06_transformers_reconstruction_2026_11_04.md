# AIMS5702 — Lecture 6 Transformer reconstruction — 4 November 2026

## Source and assessment
Guided 4 Nov session using Lecture 6 slides, the uploaded lecturer transcript and AIMS_week6.ipynb. The student preferred a fresh introduction, not initial cold-testing. AIMS5702 assessed lab/random question is 5 Nov (8%+2%); cumulative, calculator-free coding quiz is 12 Nov. Lecturer stated the majority stays close to slides and workbooks, with ~5–6 challenging marks.

## Demonstrated learning
- Rebuilt token IDs vs embeddings vs contextual hidden states and the whole tokenizer → embedding → Q/K/V → attention → layer-output pipeline.
- Articulated the roles of Q/K/V and corrected own misconception about which V is multiplied: each token's query scores other keys, and those weights combine the **contributing tokens'** value vectors.
- Correctly recognised that each layer's output becomes the next layer's input and generates fresh projections; identified tokenizer and pretrained BERT as separate components.
- Worked through a complete fully displayed two-token worked example. Attempted the unseen problem and identified `A @ V` as the final operation. First softmax row was correct but second row was copied incorrectly (did not sum to 1); after correction requested the final numeric answer. **Full independent QKV end-to-end competence not demonstrated.** Tutor's earlier marking briefly reused worked-example values; revised final calculation did not establish mastery.
- Restated desiderata of positional encoding independently and understood raw position numbers, sinusoidal vectors, RoPE rotation at a **high conceptual** level. Detailed sine/RoPE math not cold-tested.
- Independently answered three layers containing four heads each, rather than twelve sequential layers. Recognised width/head dimensionality in a 768/8 example.
- Understood N² comparisons: initially offered 20² instead of factor of increase 20→40; subsequently correctly formulated 60²/20² for the triple-length case.
- Reviewed Week 6 autograd, `nn.TransformerEncoderLayer`, `AutoTokenizer`, `AutoModel`, `model(**inputs)`, `last_hidden_state` and BERT contextual vectors. No code independently implemented this session.
- FFN/residual/layer-norm pipeline covered in summary rather than independently reconstructed.

## Evidence boundaries / follow-up
Same-session conceptual reconstruction with targeted explanations and repairs, **not delayed mastery or independent full numerical attention computation**. Preserve remaining uncertainties about row-wise softmax, end-to-end matrix orientation/calculation, full architecture, RoPE details and independent code recognition.

**Next:** 5 Nov inference/quantisation and short mixed CNN/Transformer/inference MCQs before 8% lab/2% random question; from 7 Nov cumulative slides/workbooks with selective code practice/HW3. Protect AIMS5701 HW4 before 9 Nov and 18 Nov written midterm as well as FTEC deadlines. Do not assume submissions or other project statuses changed.

## Revision reference
[Lecture 6 Transformer Revision Summary](lecture06_transformers_revision_summary_2026_11_04.md)
