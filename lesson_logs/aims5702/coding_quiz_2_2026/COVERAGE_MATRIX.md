# AIMS5702 Quiz 2 — front-loaded coverage ledger, 27 Nov update

This is a prioritisation and tracking grid, **not automatic mastery**. The audited study inventory remains **45 conceptual competency families + 23 coding/reasoning patterns** grouped from the 699-entry syllabus audit. For new preselected atomic IDs use the original master audit where available.

## Dates and evidence gates

- **27 Nov:** CP01–03 tensor consolidation *reported* in user handover (mixed transfer 4/5 cold; final `argmax` repair guided); CP04 interpolation deprioritised. Teach ethics EU/HK/China and begin altered-attendance daily drills.
- **28 Nov:** **CP16 ONNX + CP17/18 PyCUDA**; cold new scaffold and 1D CUDA kernel/launch.
- **29 Nov:** **CP19 Triton**, CP20 key blank components; fresh **cold ONNX + PyCUDA + Triton triad** by Sunday evening.
- **30 Nov:** **CP05–11 foundational layers**; mandatory **2 independent unfamiliar FC network worksheets + 2 independent CNN→pool→flatten→FC network worksheets**, with per-layer shapes/weight/bias/parameter counts; stable softmax, cross-entropy, training loop (time permitting).
- **1 Dec:** **CP12–15 attention/Transformer**, inference CP16 review; core backprop/training repair; cold retrieval on weekend triad and FC/CNN, as capacity.
- **2 Dec:** full 60-min exam-shaped mock; 3 Dec light recall/assessment.

## Mandatory weight and output checkpoints (retained, moved to Monday)

| Layer | Input/output shapes | Stored weight shape | Bias shape | Parameter count |
|---|---|---|---|---|
| `nn.Linear(I,O)` | `(B,I)` → `(B,O)` | `(O,I)` (lecture input-first view sometimes `(I,O)`) | `(O,)` | `I*O+O` |
| `nn.Conv2d(Cin,Cout,Kh×Kw)` ungrouped, bias | `(B,Cin,H,W)` → `(B,Cout,Hout,Wout)` | `(Cout,Cin,Kh,Kw)` | `(Cout,)` | `Cout*(Cin*Kh*Kw+1)` |
| `ReLU` / pooling / flatten | Shapes change according to layer; no learned weights | None | None | 0 |

Practice simple stride-one conv output calculation with padding/kernel and mean versus max pooling. A pool and flatten change features supplied to a following linear layer (which **does** change its parameter count). Complete all four unseen networks cold and then an altered delayed check. No automatic promotion based on MCQ recognition.

## Technical attendance and ethics MCQ coverage

- **16 MCQs in 60-min final quiz overall** = **8 ethics + 8 technical** (24 marks). Lecturer reportedly said **≥6 of the eight technical** are modified attendance questions **with unchanged options A–D**. Drill **all eight** as attendance variants daily for practice but retain two out-of-bank technical questions in at least the mock so the drill doesn't assume a guarantee.
- Rotate **18 distinct themes from 20 images**, preserve question IDs, new scenario, original answer choices and unique-answer validation (AQ01 broadcast two valid answers; AQ09 BatchNorm caveat). [TECHNICAL_ATTENDANCE_BANK](TECHNICAL_ATTENDANCE_BANK.md).
- Ethics target is lecturer's L07 slides/transcript and original EU risk-level examples/consequences, HK Government framework and mainland China approach. Not a broader AI-law syllabus. [ETHICS_EXAM_SCOPE](ETHICS_EXAM_SCOPE.md).

## Conceptual-family ledger (all 45 retained)

| Family | Audited family | Scheduled contact | Mastery boundary |
|---|---|---|---|
| F01 | Learning problem/dataset scale | 27 Nov: tensor evidence / 30 Nov: DL basics as relevant | Cold versus guided evidence only; unassessed atoms remain untested |
| F02 | Image/labels representation | 27 Nov: tensor evidence / 30 Nov: DL basics as relevant | Cold versus guided evidence only; unassessed atoms remain untested |
| F03 | Numeric formats and precision | 27 Nov: tensor evidence / 30 Nov: DL basics as relevant | Cold versus guided evidence only; unassessed atoms remain untested |
| F04 | Tensor/model memory accounting | 27 Nov: tensor evidence / 30 Nov: DL basics as relevant | Cold versus guided evidence only; unassessed atoms remain untested |
| F05 | Tensor creation/shape/arithmetic | 27 Nov: tensor evidence / 30 Nov: DL basics as relevant | Cold versus guided evidence only; unassessed atoms remain untested |
| F06 | Broadcasting/singletons | 27 Nov: tensor evidence / 30 Nov: DL basics as relevant | Cold versus guided evidence only; unassessed atoms remain untested |
| F07 | Basic/advanced indexing | 27 Nov: tensor evidence / 30 Nov: DL basics as relevant | Cold versus guided evidence only; unassessed atoms remain untested |
| F08 | Storage/strides/views/contiguity | 27 Nov: tensor evidence / 30 Nov: DL basics as relevant | Cold versus guided evidence only; unassessed atoms remain untested |
| F09 | Reshape/transpose/concat | 27 Nov: tensor evidence / 30 Nov: DL basics as relevant | Cold versus guided evidence only; unassessed atoms remain untested |
| F10 | Reductions/einsum | 27 Nov: tensor evidence / 30 Nov: DL basics as relevant | Cold versus guided evidence only; unassessed atoms remain untested |
| F11 | Bilinear interpolation | 27 Nov: tensor evidence / 30 Nov: DL basics as relevant | Cold versus guided evidence only; unassessed atoms remain untested |
| F12 | Code conventions/testing/reproducibility | 27 Nov: tensor evidence / 30 Nov: DL basics as relevant | Cold versus guided evidence only; unassessed atoms remain untested |
| F13 | Host/device operations | 27 Nov: tensor evidence / 30 Nov: DL basics as relevant | Cold versus guided evidence only; unassessed atoms remain untested |
| T01 | Dataset transforms/batching | 30 Nov: DL basics; 1 Dec: delayed recall | Cold versus guided evidence only; unassessed atoms remain untested |
| T02 | Linear models/MLP | 30 Nov: DL basics; 1 Dec: delayed recall | Cold versus guided evidence only; unassessed atoms remain untested |
| T03 | Activations/norm/dropout | 30 Nov: DL basics; 1 Dec: delayed recall | Cold versus guided evidence only; unassessed atoms remain untested |
| T04 | Softmax/cross-entropy/stability | 30 Nov: DL basics; 1 Dec: delayed recall | Cold versus guided evidence only; unassessed atoms remain untested |
| T05 | Optimization/training/evaluation | 30 Nov: DL basics; 1 Dec: delayed recall | Cold versus guided evidence only; unassessed atoms remain untested |
| C01 | Convolution params | 30 Nov: FC/CNN; 1 Dec: delayed recall | Cold versus guided evidence only; unassessed atoms remain untested |
| C02 | CNN padding/stride/output shape | 30 Nov: FC/CNN; 1 Dec: delayed recall | Cold versus guided evidence only; unassessed atoms remain untested |
| C03 | Pooling | 30 Nov: FC/CNN; 1 Dec: delayed recall | Cold versus guided evidence only; unassessed atoms remain untested |
| C04 | Receptive field/U-Net/segmentation | 30 Nov: FC/CNN; 1 Dec: delayed recall | Cold versus guided evidence only; unassessed atoms remain untested |
| C05 | ResNet/architecture design | 30 Nov: FC/CNN; 1 Dec: delayed recall | Cold versus guided evidence only; unassessed atoms remain untested |
| G01 | Autograd/elemental backward | 30 Nov: FC/CNN; 1 Dec: delayed recall | Cold versus guided evidence only; unassessed atoms remain untested |
| G02 | Manual linear gradients | 30 Nov: FC/CNN; 1 Dec: delayed recall | Cold versus guided evidence only; unassessed atoms remain untested |
| G03 | Manual convolution gradients | 30 Nov: FC/CNN; 1 Dec: delayed recall | Cold versus guided evidence only; unassessed atoms remain untested |
| R01 | QKV/attention | 1 Dec: Transformer / attention | Cold versus guided evidence only; unassessed atoms remain untested |
| R02 | Multi-head shapes/modules | 1 Dec: Transformer / attention | Cold versus guided evidence only; unassessed atoms remain untested |
| R03 | Positional encodings/RoPE | 1 Dec: Transformer / attention | Cold versus guided evidence only; unassessed atoms remain untested |
| R04 | Patch/CLS/text application | 1 Dec: Transformer / attention | Cold versus guided evidence only; unassessed atoms remain untested |
| R05 | Causal masks/decoding | 1 Dec: Transformer / attention | Cold versus guided evidence only; unassessed atoms remain untested |
| I01 | Inference/training differences | 28 Nov: ONNX; 1 Dec: inference | Cold versus guided evidence only; unassessed atoms remain untested |
| I02 | Quantization/fusion | 28 Nov: ONNX; 1 Dec: inference | Cold versus guided evidence only; unassessed atoms remain untested |
| I03 | ONNX/IR | 28 Nov: ONNX; 1 Dec: inference | Cold versus guided evidence only; unassessed atoms remain untested |
| I04 | Annotation/augmentation | 28 Nov: ONNX; 1 Dec: inference | Cold versus guided evidence only; unassessed atoms remain untested |
| E01 | AI governance frameworks | 27 Nov: ethics teaching; 28 Nov–3 Dec daily retrieval | Cold versus guided evidence only; unassessed atoms remain untested |
| E02 | Synthetic content/copyright/provenance | 27 Nov: ethics teaching; 28 Nov–3 Dec daily retrieval | Cold versus guided evidence only; unassessed atoms remain untested |
| E03 | Human-centred ethics/dependency | 27 Nov: ethics teaching; 28 Nov–3 Dec daily retrieval | Cold versus guided evidence only; unassessed atoms remain untested |
| U01 | GPU foundations/SIMD-SIMT | 28 Nov: PyCUDA; 29 Nov: cold triad; 1 Dec: recall | Cold versus guided evidence only; unassessed atoms remain untested |
| U02 | GPU warp/grid/block/SM launch | 28 Nov: PyCUDA; 29 Nov: cold triad; 1 Dec: recall | Cold versus guided evidence only; unassessed atoms remain untested |
| U03 | CUDA indexing/PyCUDA | 28 Nov: PyCUDA; 29 Nov: cold triad; 1 Dec: recall | Cold versus guided evidence only; unassessed atoms remain untested |
| U04 | GPU traffic/fusion | 28 Nov: PyCUDA; 29 Nov: cold triad; 1 Dec: recall | Cold versus guided evidence only; unassessed atoms remain untested |
| U05 | Triton elementwise/tile | 29 Nov: Triton / GPU concepts; 1 Dec: recall | Cold versus guided evidence only; unassessed atoms remain untested |
| U06 | Triton GEMM/reduction tiling | 29 Nov: Triton / GPU concepts; 1 Dec: recall | Cold versus guided evidence only; unassessed atoms remain untested |
| U07 | FlashAttention/online softmax | 29 Nov: Triton / GPU concepts; 1 Dec: recall | Cold versus guided evidence only; unassessed atoms remain untested |

## Coding/reasoning-pattern ledger (all 23 retained)

| Pattern | Audited pattern | Scheduled contact | Target depth |
|---|---|---|---|
| CP01 | Tensor shape/dtype/size/device | 27 Nov evidenced; 1 Dec quick recall | A: cold+transfer |
| CP02 | Broadcast/reshape/storage | 27 Nov evidenced; 1 Dec quick recall | A: cold+transfer |
| CP03 | Reductions/einsum | 27 Nov evidenced; 1 Dec quick recall | A: reductions; einsum omitted by lecturer |
| CP04 | Bilinear interpolation | Deprioritised; only if time | B (deprioritised) |
| CP05 | Naive/stable softmax | 30 Nov; 1 Dec recap | A: cold+transfer |
| CP06 | DataLoader/transforms | 30 Nov; 1 Dec recap | B: component cold |
| CP07 | MLP train/eval | 30 Nov; 1 Dec recap | A: cold+transfer |
| CP08 | Conv shapes/params/pool/RF | 30 Nov; 1 Dec recap | A: full CNN-to-FC shapes/weights/parameters |
| CP09 | Elemental/linear backprop | 30 Nov; 1 Dec recap | A: cold+transfer |
| CP10 | Conv backward | 30 Nov; 1 Dec recap | B: critical gradient expressions |
| CP11 | Residual projection | 30 Nov; 1 Dec recap | B: component cold |
| CP12 | Scaled attention/multihead | 1 Dec | A: cold+transfer |
| CP13 | Sinusoidal/RoPE | 1 Dec | A: key expressions cold |
| CP14 | ViT patches/CLS | 1 Dec | B: component cold |
| CP15 | Causal masks/LayerNorm/dropout | 1 Dec | B/C: blanks and interpretation |
| CP16 | Quantization/fusion/ONNX | 28 Nov ONNX; 29 Nov triad; 1 Dec recall | B/A: export and verification scaffold cold |
| CP17 | CUDA 1D/PyCUDA launch | 28 Nov PyCUDA; 29 Nov triad; 1 Dec recall | A: kernel + wrapper cold |
| CP18 | CUDA 2D flattened | 28 Nov PyCUDA; 29 Nov triad; 1 Dec recall | A: kernel + wrapper cold |
| CP19 | Triton offsets/masked tiles | 29 Nov Triton; 1 Dec recall | A: kernel cold+transfer |
| CP20 | Triton GEMM/tl.sum | 29 Nov Triton; 1 Dec recall | B: essential tile/reduction blanks, not full GEMM |
| CP21 | GPU fusion/memory hierarchy | 29 Nov concepts; 2 Dec mock | C: numerical/explanation |
| CP22 | Online softmax/FlashAttention | 29 Nov concepts; 2 Dec mock | C: tiled softmax/IO only |
| CP23 | Ethics case distinctions (non-code) | 27 Nov teaching; daily ethics MCQs | MCQ case reasoning |

## Source/effort boundaries

- Lecturer said: `einsum` and SIMD not on exam, no convolution-stride calculations; full FlashAttention kernel unlikely. Bilinear interpolation is user-deprioritised **not confirmed excluded**.
- Mark each family **taught**, **cold checked**, **guided**, or **untested** by actual evidence; the date column indicates targeted contact, not completion. Long-tail audited atoms not individually tested remain untested.
- Weekend milestone is **ONNX/PyCUDA/Triton cold reproduction**, *not* an excuse to drop FC/CNN layer mathematics.
