# Quiz 2 — revised syllabus coverage and priority map (lecturer update, 26 November)

**The complete audited inventory remains 45 competency families + 23 CP pattern families (699 source-level entries pre-deduplication).** The tables below retain their identifiers as a coverage ledger, **not** a claim that each atom will be separately tested or mastered. For the assessment format and source hierarchy, see [README.md](README.md), [TECHNICAL_ATTENDANCE_BANK.md](TECHNICAL_ATTENDANCE_BANK.md) and [ETHICS_EXAM_SCOPE.md](ETHICS_EXAM_SCOPE.md).

## Required end-to-end mathematical checkpoints

**Checkpoint FC — 28 November:**
1. For **each** `nn.Linear(d_in,d_out)`, learner gives input/output activation shape, **lecture input-first** weight view `(d_in,d_out)`, **PyTorch stored** `(d_out,d_in)`, bias `(d_out,)`, trainable count `d_in*d_out+d_out` (when bias enabled).
2. Independently work through a *multi-layer* network, including nonparametric activations. **Two unseen networks**, not a repeated taught example. No MCQ recognition counts as passing.
3. Count correct class-logit output dimensions and keep the true-class target distinct from the prediction.

**Checkpoint CNN — 29 November:**
1. For **each** ordinary ungrouped `nn.Conv2d(Cin,Cout,(Kh,Kw),bias=True)`, weight `(Cout,Cin,Kh,Kw)`, bias `(Cout,)`, trainable parameters `Cout*(Cin*Kh*Kw+1)`. Spatial image dimensions do **not** enter convolution weight count.
2. Propagate `(B,C,H,W)` through **Conv2d → ReLU → Pool2d → Flatten → Linear** and sum parameters. For standard conv output, `floor((H+2P-D*(K-1)-1)/S+1)` on each axis. Lecturer says *convolution stride calculations not on Quiz 2*, so practice **stride-one** kernel/padding/output calculations rather than lengthy non-unit-stride problems.
3. Contrast max versus average pooling: both summarize a region without learned kernel weights; max selects the largest value, average uses the mean. Pooling changes shape, not trainable parameters.
4. **Two complete unfamiliar network problems**, each with a table of input/output shape, weight shape, bias shape, and per-layer/total parameter count. Independent cold completion and at least one delayed changed check on 30 Nov or mock.

**Other signalled targets:** LSTM uses **tanh** activation in its cell/update transformations (record this at lecture depth); attention/ViT/causal; ONNX exported graph and output check; PyCUDA/C++ kernel string and global index; Triton decorator, offsets, masks/load/store, host grid/block arithmetic.

## Competency-family allocation

| Family | Audited family name | New primary date | Evidence rule |
|---|---|---|---|
| F01 | Learning problem/dataset scale | 27 Nov tensor cold review; 28 Nov FC | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| F02 | Image/labels representation | 27 Nov tensor cold review; 28 Nov FC | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| F03 | Numeric formats and precision | 27 Nov tensor cold review; 28 Nov FC | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| F04 | Tensor/model memory accounting | 27 Nov tensor cold review; 28 Nov FC | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| F05 | Tensor creation/shape/arithmetic | 27 Nov tensor cold review; 28 Nov FC | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| F06 | Broadcasting/singletons | 27 Nov tensor cold review; 28 Nov FC | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| F07 | Basic/advanced indexing | 27 Nov tensor cold review; 28 Nov FC | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| F08 | Storage/strides/views/contiguity | 27 Nov tensor cold review; 28 Nov FC | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| F09 | Reshape/transpose/concat | 27 Nov tensor cold review; 28 Nov FC | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| F10 | Reductions/einsum | 27 Nov tensor cold review; 28 Nov FC | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| F11 | Bilinear interpolation | 27 Nov tensor cold review; 28 Nov FC | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| F12 | Code conventions/testing/reproducibility | 27 Nov tensor cold review; 28 Nov FC | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| F13 | Host/device operations | 27 Nov tensor cold review; 28 Nov FC | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| T01 | Dataset transforms/batching | 28 Nov DL basics/MLP | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| T02 | Linear models/MLP | 28 Nov DL basics/MLP | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| T03 | Activations/norm/dropout | 28 Nov DL basics/MLP | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| T04 | Softmax/cross-entropy/stability | 28 Nov DL basics/MLP | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| T05 | Optimization/training/evaluation | 28 Nov DL basics/MLP | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| C01 | Convolution params | 29 Nov CNN/backprop | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| C02 | CNN padding/stride/output shape | 29 Nov CNN/backprop | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| C03 | Pooling | 29 Nov CNN/backprop | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| C04 | Receptive field/U-Net/segmentation | 29 Nov CNN/backprop | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| C05 | ResNet/architecture design | 29 Nov CNN/backprop | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| G01 | Autograd/elemental backward | 29 Nov CNN/backprop | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| G02 | Manual linear gradients | 29 Nov CNN/backprop | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| G03 | Manual convolution gradients | 29 Nov CNN/backprop | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| R01 | QKV/attention | 30 Nov Transformer | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| R02 | Multi-head shapes/modules | 30 Nov Transformer | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| R03 | Positional encodings/RoPE | 30 Nov Transformer | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| R04 | Patch/CLS/text application | 30 Nov Transformer | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| R05 | Causal masks/decoding | 30 Nov Transformer | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| I01 | Inference/training differences | 30 Nov inference/ONNX | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| I02 | Quantization/fusion | 30 Nov inference/ONNX | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| I03 | ONNX/IR | 30 Nov inference/ONNX | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| I04 | Annotation/augmentation | 30 Nov inference/ONNX | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| E01 | AI governance frameworks | 27 Nov ethics teaching; daily 8-MCQ recall | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| E02 | Synthetic content/copyright/provenance | 27 Nov ethics teaching; daily 8-MCQ recall | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| E03 | Human-centred ethics/dependency | 27 Nov ethics teaching; daily 8-MCQ recall | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| U01 | GPU foundations/SIMD-SIMT | 1 Dec CUDA; 2 Dec mock | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| U02 | GPU warp/grid/block/SM launch | 1 Dec CUDA; 2 Dec mock | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| U03 | CUDA indexing/PyCUDA | 1 Dec CUDA; 2 Dec mock | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| U04 | GPU traffic/fusion | 1 Dec CUDA; 2 Dec mock | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| U05 | Triton elementwise/tile | 1 Dec Triton; 2 Dec conceptual/mock | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| U06 | Triton GEMM/reduction tiling | 1 Dec Triton; 2 Dec conceptual/mock | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |
| U07 | FlashAttention/online softmax | 1 Dec Triton; 2 Dec conceptual/mock | Unassessed atoms stay eligible; lecturer-led question weighting controls practice |

## Coding/reasoning pattern allocation

| CP | Audited pattern | New primary date | Target depth |
|---|---|---|---|
| CP01 | Tensor shape/dtype/size/device | 27 Nov; CP04 B component | A: cold+transfer |
| CP02 | Broadcast/reshape/storage | 27 Nov; CP04 B component | A: cold+transfer |
| CP03 | Reductions/einsum | 27 Nov; CP04 B component | A: reductions; einsum omitted by lecturer |
| CP04 | Bilinear interpolation | 27 Nov; CP04 B component | B: component cold/transfer |
| CP05 | Naive/stable softmax | 28 Nov | A: cold+transfer |
| CP06 | DataLoader/transforms | 28 Nov | B: component cold |
| CP07 | MLP train/eval | 28 Nov | A: cold+transfer |
| CP08 | Conv shapes/params/pool/RF | 29 Nov | A: full CNN-to-FC shapes/weights/parameters |
| CP09 | Elemental/linear backprop | 29 Nov | A: cold+transfer |
| CP10 | Conv backward | 29 Nov | B: critical gradient expressions |
| CP11 | Residual projection | 29 Nov | B: component cold |
| CP12 | Scaled attention/multihead | 30 Nov | A: cold+transfer |
| CP13 | Sinusoidal/RoPE | 30 Nov | A: key expressions cold |
| CP14 | ViT patches/CLS | 30 Nov | B: component cold |
| CP15 | Causal masks/LayerNorm/dropout | 30 Nov | B/C: blanks and interpretation |
| CP16 | Quantization/fusion/ONNX | 30 Nov | B/C: calculation and scaffold reading |
| CP17 | CUDA 1D/PyCUDA launch | 1 Dec; 2 Dec mock | A: kernel + wrapper cold |
| CP18 | CUDA 2D flattened | 1 Dec; 2 Dec mock | A: kernel + wrapper cold |
| CP19 | Triton offsets/masked tiles | 1 Dec; 2 Dec mock | A: kernel cold+transfer |
| CP20 | Triton GEMM/tl.sum | 1 Dec; 2 Dec mock | B: essential tile/reduction blanks, not full GEMM |
| CP21 | GPU fusion/memory hierarchy | 1–2 Dec conceptual/numerical | C: numerical/explanation |
| CP22 | Online softmax/FlashAttention | 1–2 Dec conceptual/numerical | C: tiled softmax/IO only |
| CP23 | Ethics case distinctions (non-code) | 27 Nov teaching; 28 Nov–3 Dec retrieval | MCQ case reasoning |

## Explicit lecturer-driven priority changes

| Instruction reported from revision lecture | Practical allocation |
|---|---|
| 8 of 16 MCQs on AI ethics | 27 Nov taught-risk-table session; 8 lecture-faithful risk/example questions daily thereafter |
| 8 technical MCQs, ≥6 attendance-quiz variations retaining options | Use the 18-distinct-question/20-image bank; six new stems with **identical A–D options** and an unambiguous answer, plus two additional technical questions |
| CNN and fully connected weight sizes, CNN output dimensions | **Mandatory full cold whole-network checkpoints** on 28–29 Nov, repeat in 2 Dec mock |
| Q3 ONNX / Q4 PyCUDA / Q5 Triton cited by lecturer | Dedicated cold code/comment/numerical blanks on 30 Nov, 1 Dec, 2 Dec mock |
| CUDA global indexing, grid/block, Triton decorator/offsets/masks | **Must produce exact syntax without cues**, plus unseen changed dimensions and bounds |
| No `einsum` and no SIMD | No dedicated exam practice; retain historical evidence but don't spend scarce time mastering these now |
| Conv stride not assessed, output size likely | Train straightforward **stride-one** CNN spatial shapes; preserve conceptual stride recognition only if incidental |
| FlashAttention unlikely in depth | MCQ/tiled-IO/online-softmax intuition, no production implementation |
| Tanh in LSTM | Recognition and small conceptual blanks, not an LSTM from scratch |

## Boundary and omissions

- **Depth A:** learner independently completes essential code/calculation with unseen changed input. **B:** independently fills meaningful missing components in supplied scaffold. **C:** can interpret or calculate a key principle. Do not upgrade B/C to A.
- Preserve L02/L03 concept MCQ record: 24 cold / 15 correct; nine reviewed; **eight open questions unattempted**. Preserve separate 24 Nov 60-minute coding evidence: CP01/CP03 partial, CP02 tested subset plus transfer, CP04 unattempted.
- **Exam scope remains broad** beyond explicit exclusions. Lower *practice priority* does not imply blanket exclusion of unsupported skills. Record untested atoms rather than claiming full 699-item mastery.
- AIMS5701 poster 2 Dec and PCG presentation 8 Dec are delivery commitments; keep 2 Dec mock bounded and PCG work separate.
