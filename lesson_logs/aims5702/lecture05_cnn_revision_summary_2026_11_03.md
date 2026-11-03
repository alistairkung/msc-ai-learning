# AIMS5702 Lecture 5 — CNN Revision Summary

_3 November 2026 · Source: Lecture 5 “Convolutional Neural Network”, slides 10–110. This is a revision summary, not evidence of independent implementation mastery._

## Essential formulas

| Task | Formula / PyTorch convention | Conditions |
|---|---|---|
| Convolution output height or width | `O = floor((I + 2P - K) / S) + 1` | Standard convolution; symmetric padding, dilation 1 |
| Padding to preserve spatial size | `P = (K - 1) / 2` | Odd kernel, stride 1 |
| Conv weights | `Kh * Kw * Cin * Cout` | Standard Conv2d, excluding bias |
| Conv parameters | `Kh * Kw * Cin * Cout + Cout` | Bias enabled, one bias per output channel |
| PyTorch input/output | `(B, Cin, H, W) -> (B, Cout, Hout, Wout)` | Batch remains unchanged |
| PyTorch weight shape | `(Cout, Cin, Kh, Kw)` | Do not confuse with activation shape |
| Receptive field, L stacked 3×3 convolutions | `R = 1 + 2L` | All stride 1, dilation 1, measured away from image boundaries |

**Lecturer notation:** Slide 62's printed striding expression was clarified in class: retain `K_half = (K - 1) / 2` in `(I - 2K_half - 1 + 2P) / S + 1`. The standard expression above is algebraically equivalent before floor rounding. The lecturer reportedly excluded stride-dependent receptive-field tracing from the quiz; treat this as reported assessment guidance, not an explicit statement in the PDF.

**Worked shape example:** `Conv2d(3, 16, kernel_size=3, padding=1)` on `(8,3,32,32)` produces `(8,16,32,32)`; weight tensor `(16,3,3,3)`; 432 weights + 16 biases = **448 parameters**.

## Convolution, pooling and receptive fields

**Convolution:** A learned kernel computes elementwise products and sums over a local patch (in the deep-learning convention of the lecture, no kernel flip). Local connectivity and spatial weight sharing make convolution more parameter-efficient than a fully connected layer. Each standard output filter spans every input channel and produces one output feature map.

**Pooling:** Max pooling picks the largest value in each local window; average pooling takes the mean. `MaxPool2d(2, stride=2)` turns each non-overlapping 2×2 region into **one** value and halves height and width (for even dimensions). It does *not* replace four pixels with four copies of the maximum.

| Pooling benefits | Limits / trade-offs |
|---|---|
| Reduces spatial positions and later computational cost | Discards activations and precise locations |
| Keeps strong local feature responses (max pooling) | Weak responses or fine boundaries can disappear |
| Relative stability to small translations/local deformations | Does not guarantee invariance to arbitrary shifts, scale or shear |
| Stride-2 downsampling lets later convolutions expand receptive fields faster | Resolution declines, complicating pixel-accurate segmentation |

A 3×3 stride-1 convolution expands receptive field sizes **3 → 5 → 7 → 9** across four layers. With `Conv3 → Conv3 → Pool2(stride 2) → Conv3`, the illustrative sequence is **3 → 5 → 6 → 10**, because adjacent pooled activations are spaced two original-image pixels apart. The aim is broader context: a tiny cow-fur patch might look like a cowhide rug; a larger field can capture the animal's head, legs and shape.

## ResNet (slide 108)

`y = x + F(x)` — a residual block adds its **block input** to its learned transformation.

**Benefits:** easier optimisation of deep networks, a direct gradient pathway, and the ability to learn small residual corrections (`F(x) ≈ 0` preserves the input).

**Constraints:** direct addition needs compatible shapes (a projection shortcut may be required). Residuals do not automatically reduce computation or solve all training difficulties.

## U-Net (slides 87–97)

**Purpose:** segmentation requires both broad image context (*what object?*) and precise high-resolution details (*which pixels?*).

1. **Downsampling** via pooling increases context / receptive-field growth, but sacrifices spatial precision.
2. **Upsampling** restores the feature-map dimensions, not necessarily the lost information.
3. **Skip connections** pass earlier high-resolution **activations/feature maps, not learned weights** to the decoder, usually concatenating along the channel axis to help locate boundaries.

For example, `(8,32,64,64)` concatenated with `(8,64,64,64)` along `dim=1` gives **`(8,96,64,64)`**; height, width and batch must align.

| | ResNet | U-Net |
|---|---|---|
| Typical shortcut operation | Elementwise addition | Channel concatenation |
| Motivation | Easier training of deep networks | Combine high-resolution detail with broader context |
| Information carried | Residual block input | Earlier encoder feature maps |

## Other lecture distinctions

- **High-pass / Laplacian filters (slides 69–71):** emphasise spatial changes and edges; **low-pass** averaging filters smooth and reduce noise.
- **VGG (65–66):** repeats convolution + ReLU blocks and pooling; convolution has learned weights, ReLU and standard pooling are fixed operations.
- **CNN history (99–110):** LeNet (early CNN), AlexNet (large-scale breakthrough), VGG (stacked blocks), Inception (deeper CNN), ResNet (residual depth).
- **GPU recap (3–8):** data movement/bus bottleneck, caches to reduce access costs, SoC integration vs chip-area and manufacturing trade-offs.

## Exam technique

For a `Conv2d` tensor question: **(1)** write output `(B,Cout,?,?)`; **(2)** use input **H/W** in the spatial formula, not batch or channels; **(3)** write weights `(Cout,Cin,Kh,Kw)`; **(4)** multiply these and add `Cout` biases only if enabled; **(5)** floor the quotient before adding 1. In pooling, preserve batch and channel dimensions.

**Memory anchors:** Convolution = learned local features. Pooling = preserve strong responses while reducing resolution. ResNet = add block input for easier deep optimisation. U-Net = reconnect high-resolution encoder features for segmentation.
