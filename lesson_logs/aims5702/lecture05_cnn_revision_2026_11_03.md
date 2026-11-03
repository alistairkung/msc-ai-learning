# AIMS5702 — Lecture 5 CNN revision and cold recall — 3 November 2026

## Source and scope
Reviewed the uploaded 111-page AIMS5702 Lecture 5 CNN PDF and prior 15 October guided pre-lecture conversation. The present session is review of taught material, not new CNN code or live lecture attendance. The lecturer's reported clarification was that the output-size equation on slide 62 should retain `K_half`, and stride-aware receptive-field tracing would not be required in the quiz. The PDF alone does not establish quiz scope.

## What was demonstrated today
- Rebuilt one-window convolution elementwise multiplication/sum correctly without further repair. For a 3×3 input and sliding 2×2 kernel, three of four output positions were calculated correctly; bottom-left selected the wrong value (5 instead of 8), an indexing rather than algorithm error.
- Initially confused sign and spatial input size in the output-size formula, then correctly solved 9×9/K3/S2 → 4×4 and 8×8/K3/P1/S1 → 8×8.
- Needed explicit B/C/H/W re-teaching; initially mixed batch, spatial extent and filter weight shape. Subsequently **independently** solved `(8,3,64,64)` through `Conv2d(3,16,K5,P2)`: output `(8,16,64,64)`, weights `(16,3,5,5)`, 1216 trainable parameters.
- MaxPool(2,stride2) output spatial size 32 from a 64-wide map was computed correctly after clarification that one 2×2 window becomes **one maximum**, not four repeated values.
- Reconstructed 5 layers of 3×3 stride-1 convolution → 11×11 receptive field, then the context/stride-2-pooling rationale and independently calculated the further RF expansion 10 → 14 with the supplied formula. Do not infer delayed recall of a general RF recurrence or expect it from lecture scope.
- U-Net: independently explained why downsampling loses spatial precision, why upsampling alone cannot restore it, and why earlier feature maps are passed through skip connections; computed channel concatenation `(8,96,64,64)` correctly.
- ResNet: explained `x+F(x)` as adding block input to learned residual, providing a direct gradient path and making deeper models easier to optimise.
- Follow-up cold recall (six questions): Q1 convolution dimensions/count correct but full output batch/channel shape omitted; Q2 output-size formula set up correctly but rounded `floor(14.5)+1` to 16 instead of 15; Q3 pooled 16×16 right but omitted B/C; Q4 RF 9×9 and overlap rationale correct; Q5 U-Net and Q6 ResNet rationale correct without prompts. **Same-session reconstructed recall**, not delayed independent mastery.
- End-of-session skim: high/low pass filters, translation stability (including limits on shear/scale), architectural timeline and GPU/cache/SoC recap; not yet cold-tested.

## Fragile boundaries
- Off-by-one/floor arithmetic, full activation tensor shape vs weight tensor, identifying H/W rather than B in spatial formulas, and local-window indexing.
- Residual/skip conceptual explanations were independently given after same-session guided rebuilding; long-term retention still needs changed-example cold check.
- Convolution backward (especially batched 4D slicing and overlapping gradient accumulation) was *not* independently reconstructed or tested this session. Historical Assignment 3 passing tests remain guided code evidence only.
- No evidence here about independent CNN training or final assignment submission status.

## Next study action
Before 5 November assessed lab, do one brief mixed, unfamiliar MCQ/shape check if time remains; prioritise 4 November Transformers and 5 November inference revision rather than repeating the whole CNN lecture. Ahead of 12 November quiz: changed no-hint `Conv2d` shape/parameter problem with nonintegral quotient, pooling translation-stability conceptual check and filter/architecture recognition. Park full batched convolution backward reconstruction unless the assessed scope warrants it.

## Revision page
See [CNN Revision Summary](lecture05_cnn_revision_summary_2026_11_03.md).
