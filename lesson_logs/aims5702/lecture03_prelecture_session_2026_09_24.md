# AIMS5702 Lecture 3 — pre-lecture study evidence

**Date:** 2026-09-24
**Source boundary:** guided by the supplied Lecture 3 deck; this is same-session preparation evidence, not lecture-completion evidence.

## Linear-layer notation

The first cold check exposed a genuine notation gap around `y_j = sum_i w_ij x_i + b_j`. The session rebuilt the notation from a scalar linear model.

Current same-session model:

```text
i -> input-feature index
j -> output-feature index
w_ij -> weight connecting input i to output j
N inputs -> M outputs
x:(N,)  W:(N,M)  b:(M,)  y:(M,)
```

Changed examples such as 8->4, 6->3 and 784->10 were then answered correctly. Later, a 100->5 check temporarily assigned the input dimension to `b` and `y`; the cue `bias belongs to the output` transferred immediately to a 32->7 example.

## Cross-entropy and objective notation

The learner understood that a one-hot target reduces multiclass cross entropy to the negative log probability assigned to the true class. One early changed example selected the wrong class probability; a later changed example was correct.

The dataset objective `min_theta sum_i CEL(f_theta(I_i), y_i)` needed explicit decompression:

```text
i -> training-example index
I_i -> whole i-th input example
y_i -> true label
f_theta(I_i) -> model prediction
CEL(...) -> scalar loss for that example
sum_i -> dataset loss
min_theta -> choose trainable parameters that minimise the loss
```

Initial slips included treating `i` as a feature index, `I_i` as part of an image, `f_theta(I_i)` as the loss, and `min_theta` as choosing small weights. Changed examples later separated prediction from loss correctly.

## Gradient descent / SGD

This material retrieved strongly. The learner correctly used derivative sign to choose update direction, computed changed scalar updates, interpreted a gradient vector, and mapped:

```text
loss.backward() -> compute parameter gradients
optimizer.step() -> apply the optimiser update
```

Mini-batch arithmetic and epoch meaning also returned cleanly.

## Nonlinearity / MLP

The learner remembered the high-level idea that real relationships can be nonlinear, but the algebraic reason for activations needed unpacking. A scalar example established that stacked linear maps collapse: `W2(W1 x) = (W2 W1)x`. `Equivalent` was clarified to mean the stack can be represented by one new linear map, not that later layers have no effect.

ReLU was initially described as helping magnitude grow. A changed example then established the correct role: nonlinearity prevents the whole stack collapsing to one fixed linear transformation. The learner connected this back to prior Imperial ML intuition about nonlinear decision relationships.

## CNN motivation

The learner correctly reasoned from huge fully-connected parameter counts to:

```text
local connectivity -> only nearby inputs matter
weight sharing -> reuse the same local weights at different positions
```

No convolution arithmetic, channel/kernel shape work, padding/stride, implementation or CNN training was attempted.

## Delayed PyTorch-pipeline reconstruction

After a break, the learner reported that the core training loop felt familiar but `TensorDataset` / `DataLoader` orchestration felt fuzzy.

Retrieved correctly:
- 60/20/20 train/validation/test roles;
- test set held out until development is complete;
- DataLoader provides mini-batches;
- full batch shape is `(batch, features)` and the final partial batch is smaller;
- epoch -> batches -> forward -> loss -> backward -> update;
- validation keeps forward/loss but removes backward and parameter updates;
- shuffling makes sense for training.

Fragile/re-taught:
- `TensorDataset` was initially misremembered as converting data into tensors; it was re-taught as pairing already-created tensors so `dataset[i] -> (X[i], y[i])`;
- `y_batch` initially took the feature dimension rather than the batch dimension;
- `optimizer.zero_grad()` was omitted twice and needed reintroduction;
- `torch.no_grad()` for validation was recalled only after prompting.

## Evidence boundary

Strong now: gradient-update mechanics, batch/epoch intuition, train-vs-validation-vs-test roles, why linear stacks need nonlinearity, and high-level locality/weight-sharing motivation.

Fresh/fragile: indexed `w_ij` notation, output-side `b/y` shapes, multiclass true-class indexing, dataset-objective notation, `TensorDataset`, batch-label shape, `zero_grad()` / `no_grad()` orchestration.

Softmax was mentioned as contextual outside-deck ML knowledge after the learner guessed sigmoid for multiclass probability conversion; do not treat that as lecturer-taught Lecture 3 evidence unless the live lecture covers it.

**Immediate next step:** attend Lecture 3. Listen hardest for indexed notation, multiclass loss/objective framing, the formal-SGD-to-PyTorch bridge, and the transition from linear layers to MLP/CNN. Do not add more pre-lecture study today.