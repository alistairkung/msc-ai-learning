# AIMS5702 — lecture-break consolidation + lab readiness

**Date:** 2026-10-01  
**Source boundary:** delayed cold retrieval and guided lab-style reconstruction from the learner's Lecture 1–3 material and prior repository evidence. No new live lecture occurred today.

## Session goal

Use the lecture break to test whether AIMS5702 Weeks 1–3 material is actually retrievable, repair observed weak edges, then attempt a changed multiclass PyTorch pipeline before moving into CNN preparation.

This was deliberately a broad retrieval-and-transfer session rather than a reread.

## Broad delayed retrieval

### Tensor axes, reductions and broadcasting

Strong/independent after prompting only for concrete values:

- `(samples,time,features)` axis semantics;
- reduction shape and meaning, including `mean(dim=1)` and `mean(dim=2)`;
- right-aligned broadcasting;
- unequal-rank broadcasting such as `(4,1,3) + (2,3) -> (4,2,3)`;
- singleton insertion via `unsqueeze(1)`;
- feature-wise versus sample-wise broadcast semantics.

The 24 Sep unequal-rank-broadcasting quiz miss repaired cleanly on changed examples.

### Basic slicing versus advanced indexing

The distinction is conceptually understood but one shape-preservation trap remains worth spaced retrieval:

```text
x[2]    -> basic integer indexing -> selected axis disappears
x[2:3]  -> basic slice            -> selected axis remains with length 1
x[[2]]  -> advanced indexing      -> new tensor/copy semantics
```

A quickfire quiz on basic slicing, list/tensor indexing, boolean masks and view/copy behavior was otherwise strong. The learner consistently recognises basic slices/transposes/views as shared-storage operations and list/tensor/mask selection as advanced indexing that typically materialises new storage.

### Stride, storage offset and contiguity

This became the deepest repair of the session.

Existing intuition was sound:
- contiguous row-major strides can be derived from how far each axis moves through flat storage;
- transpose swaps logical axes/strides and can produce a non-contiguous view;
- `.is_contiguous()` checks; `.contiguous()` materialises contiguous storage when required;
- storage positions are computed as base offset plus local-index movement by stride.

The unstable point was procedural role assignment inside stepped slices. Multiple changed examples exposed that the learner was sometimes multiplying old stride by the **new view shape/count** or even by the slice stop rather than by the **slice step**.

The durable rule finally stabilised as:

```text
slice START -> base storage offset
slice STEP  -> new view stride
selected COUNT -> new view shape
```

For ordinary positive-step basic slicing:

```text
new_stride[d] = old_stride[d] * slice_step[d]
```

The final independent changed example was correct end to end:

```python
x = torch.arange(48).reshape(6, 8)
y = x[1:6:2, 2:8:2]
```

Recovered:

```text
selected rows = [1,3,5]
selected cols = [2,4,6]
y.shape = (3,3)
y.storage_offset = 1*8 + 2*1 = 10
y.stride = (16,2)
position of y[2,1] = 10 + 2*16 + 1*2 = 44
```

This took substantial correction before stabilising. Treat it as **same-session repaired with one clean final transfer**, not delayed-independent mastery.

### Pairwise dot products / einsum

Recovered cleanly after one semantic correction:

```text
x: (m,k)
y: (n,k)
pairwise result: (m,n)
```

Each output entry `result[i,j]` is the dot product of row `x[i]` with row `y[j]`; feature index `k` is multiplied and summed away.

Equivalent forms were readable:

```python
x @ y.T
torch.einsum("ik,jk->ij", x, y)
```

The learner correctly identified `k` as the contracted index and transferred output-shape reasoning to changed examples.

### Reshape / flatten / transpose

Recovered after one initial misconception that `reshape(batch,-1)` swapped axes.

Current distinction:

```text
reshape / flatten -> merge/reinterpret dimensions
transpose         -> swap dimensions
```

Changed examples such as `(16,28,28) -> (16,784)` and `(8,3,32,32) -> (8,3072)` via flattening were then correct. `flatten(start_dim=1)` was new API syntax but its meaning was inferred correctly.

## Linear layers and multiclass notation

### Linear layer representation

The main fragility was translating between semantic layer meaning and PyTorch's stored parameter orientation.

The conceptual anchor that repaired the confusion:

> `nn.Linear(in_features, out_features)`: each output neuron has one weight for every input feature.

Therefore:

```text
weight -> (out_features, in_features)
bias   -> (out_features,)
output -> (batch, out_features)
```

Rapid abstract shape drills initially degraded performance, but grounding the layer as “N output neurons × M weights each” restored correct changed examples.

Treat the neuron semantics as stronger than cold API-orientation recall.

### Cross-entropy and objective notation

The learner correctly retrieved that multiclass cross-entropy cares about the probability/score associated with the true class.

Formal objective notation remained hazy initially:

```text
i             -> training-example index
I_i           -> input for example i
f_theta(I_i)  -> model prediction for that input
y_i           -> true label
min_theta     -> choose parameters that minimise total loss
```

After decomposition, changed examples were explained correctly. This remains a representation-translation target rather than a conceptual loss-function gap.

## Dataset / DataLoader / training workflow

### Dataset and batching

Recovered:

- `TensorDataset(X,y)` pairs corresponding items so `dataset[i] -> (X[i],y[i])`;
- `DataLoader` adds batching;
- a `batch_size=10` loader over `X:(50,6), y:(50,)` yields full batches `X_batch:(10,6), y_batch:(10,)`;
- training shuffles; validation need not.

One initial answer gave single-sample shapes for a DataLoader batch, then repaired immediately.

### Training loop

The learner independently reconstructed the correct conceptual dependency:

```text
zero_grad
-> forward
-> loss
-> backward
-> optimiser step
```

In lab-style code, the structure was correct but two API names were rusty:
- used `model.predict(X_batch)` instead of `model(X_batch)`;
- used `loss.backwards()` instead of `loss.backward()`.

### Epochs and validation/evaluation

This is the clearest remaining lab-readiness weakness.

Conceptually retrieved:
- an epoch is one complete pass over all training mini-batches;
- validation keeps forward pass, loss and metrics but removes backward/update;
- validation should run under `model.eval()` + `torch.no_grad()`;
- train/validation/test roles are understood;
- multiclass predictions come from `logits.argmax(dim=1)`.

However, orchestration was hazy:
- wrapping the batch loop in the epoch loop was not independently reconstructed;
- inside validation the learner first used whole `X_val/y_val` instead of current `X_batch/y_batch`;
- accuracy accumulation from predictions vs labels needed teaching;
- epoch-level loss/accuracy accumulation and normalisation were shown rather than independently produced.

The learner explicitly reported feeling comfortable through dataset/model/loss/optimiser setup and the core training batch loop, then mentally flagging around epochs and evaluation.

## Changed multiclass lab-style pipeline

A small synthetic task was built interactively:

```text
240 samples
6 input features
3 classes
192 train / 48 validation
model: 6 -> 12 -> ReLU -> 3
batch size: 32
loss: CrossEntropyLoss
optimiser: SGD(lr=0.01)
```

Independent/good:
- train/validation tensor shapes;
- `TensorDataset` construction;
- `DataLoader` intent (minor API spelling correction on training loader);
- validation loader without shuffle;
- `nn.Sequential(Linear(6,12), ReLU, Linear(12,3))`;
- CrossEntropyLoss selection;
- SGD parameter/learning-rate intent;
- training-loop order.

Guided/rusty:
- logits as per-sample raw class scores;
- model-call syntax;
- backward API spelling;
- validation-batch use;
- argmax-to-predictions;
- epoch/evaluation bookkeeping.

## Evidence boundary

Today materially strengthens confidence that the Lecture 1–3 conceptual base survives delayed retrieval. It does **not** establish a fully cold-independent PyTorch training/validation pipeline.

The most useful boundary is:

```text
comfortable:
data/shapes -> Dataset/DataLoader -> model -> loss/optimiser -> core batch training logic

fragile:
epoch orchestration -> eval/no_grad -> batch-vs-whole-validation tensors
-> prediction/accuracy accumulation -> epoch-level reporting
```

Stride/view reasoning is conceptually strong but the stepped-slice role mapping should be sampled again later because it required ~30 minutes of repair before one clean final transfer.

## Next AIMS5702 block

Do not replay the whole lecture sweep.

1. Begin with one short cold check of:
   - integer index vs length-one slice;
   - PyTorch `Linear.weight` orientation;
   - stepped-slice rule: start -> offset, step -> stride, count -> shape.
2. Give a nearly complete changed classification script and have the learner fill only:
   - epoch loop;
   - `model.train()` / `model.eval()`;
   - `torch.no_grad()`;
   - batch predictions;
   - loss/accuracy accumulation and final epoch metrics.
3. Then reconstruct the full small pipeline once with minimal prompting.
4. If that is stable, move into the bounded CNN bridge: image shapes -> locality/weight sharing -> kernels/channels -> stride/padding -> output shapes.

Do not infer readiness from the synthetic classifier's performance because the generated labels were random and independent of the inputs.
