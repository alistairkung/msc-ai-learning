# AIMS5702 Lecture 3 — Deep Learning Basics pre-lecture bridge

**Planned for:** 2026-09-24  
**Source boundary:** user-supplied AIMS5702 Lecture 3 slide deck plus existing repository learning evidence. This file is a preparation plan, not evidence that the lecture material has been mastered.

## Actual Lecture 3 scope from supplied deck

The deck moves through:

1. image representation / flattening;
2. linear layers and bias;
3. linear classification / perceptron intuition;
4. one-hot targets, softmax-style class outputs and cross-entropy loss;
5. dataset-level training objective;
6. gradient descent and learning rate;
7. training / validation / testing and overfitting;
8. mini-batches, epochs and stochastic gradient descent;
9. nonlinear activations such as ReLU / sigmoid;
10. stacking layers into an MLP;
11. why nonlinearity is necessary;
12. motivation for CNNs from huge fully-connected parameter counts, locality and weight sharing.

The deck explicitly says detailed SGD equations are not the target; basic ideas are.

## Mapping to existing evidence

### Strong / mostly retrieval

Existing repository evidence already covers:

- PyTorch tensors and shape reasoning;
- linear-model mechanics;
- manual gradients / autograd;
- a standard `nn.Linear` + loss + SGD training loop;
- binary MLP classification with ReLU and logits;
- DataLoader mini-batches;
- train / validation / test separation;
- train-only preprocessing and leakage reasoning;
- per-epoch validation under `torch.no_grad()`;
- recognising overfitting from train/validation divergence.

These should be cold-retrieved, not retaught from zero.

### High-value bridge

The most useful pre-lecture work is to connect the lecturer's notation to the code/mechanics already known:

```text
y_j = sum_i w_ij x_i + b_j
-> identify input/output indices
-> derive W and b shapes
-> map the equation to a linear layer
```

Then connect:

```text
per-example prediction
-> one-hot / class target
-> cross-entropy
-> sum/average over dataset
-> objective to minimise
-> gradient
-> parameter update
-> batch iteration
-> epoch
```

This directly supports the learner's broader goal of reading mathematical expressions and translating them into shapes/computation rather than treating notation as a separate language.

### Genuinely newer / highest forward value

CNN motivation is the clearest new edge relative to current evidence:

```text
huge fully-connected parameter count
-> local connectivity
-> reuse/shared weights across locations
-> convolution
```

Do not attempt to master CNN implementation before the lecture; aim only to make locality and weight sharing intelligible enough that the lecture can extend the model.

## 2026-09-24 study plan

The day should minimise context switching.

### Block 1 — AIMS5701 reconciliation, <= 90 min

Finish the search lecture gap pass recorded in the AIMS5701 log. Hard stop at 90 minutes.

### Remaining pre-lecture time — AIMS5702 only

Use all remaining study time before the 5702 lecture on this deck.

Priority order:

1. **Linear-layer notation and shape derivation**
   - read `y_j = sum_i w_ij x_i + b_j`;
   - derive weight / bias shapes from N-dimensional input and M-dimensional output;
   - map notation to PyTorch semantics.

2. **Cross-entropy and objective notation**
   - interpret one-hot target and predicted class distribution;
   - explain why cross-entropy penalises low probability on the true class;
   - translate the dataset objective into English and then into training-loop stages.

3. **Gradient descent / SGD bridge**
   - retrieve derivative/gradient meaning;
   - explain the minus sign and learning-rate role;
   - connect the formal update to `loss.backward()` and optimizer steps;
   - reconnect batch, iteration and epoch terminology.

4. **Nonlinearity / MLP / CNN motivation**
   - explain why stacked linear maps collapse to another linear map;
   - retrieve ReLU/sigmoid roles;
   - preview locality + weight sharing as the motivation for convolution.

### Explicitly low priority before lecture

Do not spend substantial time re-teaching:

- image-as-matrix basics;
- train/validation/test workflow;
- overfitting;
- DataLoader basics;
- a generic PyTorch training-loop implementation.

These already have stronger repository evidence than the genuinely new CNN/locality material.

## Near-term sequencing after the lecture

The agreed short-horizon order is:

```text
24 Sep
AIMS5701 reconciliation
-> AIMS5702 targeted pre-lecture bridge
-> AIMS5702 lecture

25 Sep
receipts homework only

28 Sep
receipts contingency until complete
-> only then begin AIMS5701 decision-tree bridge

29 Sep
receipts deadline
```

Decision trees should not interrupt an unfinished receipts block. Once receipts is complete, the AIMS5701 JIT lead becomes:

```text
linear/logistic retrieval
-> split intuition
-> Gini / entropy / information gain
-> recursive tree construction
-> stopping / overfitting
-> random forests
```
