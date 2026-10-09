# AIMS5702 — Train revision sheet (8 Oct 2026)

**Quick read (10–15 minutes).** Prioritised from today's actual errors. Not assessed-notebook answers.

## 1. Train vs validate
```python
model.train()
for inputs, targets in train_loader:
    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    loss.backward()
    optimizer.step()

model.eval()
total_correct = 0
total_samples = 0
with torch.no_grad():
    for inputs, targets in val_loader:
        outputs = model(inputs)
        predictions = outputs.argmax(dim=1)
        total_correct += (predictions == targets).sum().item()
        total_samples += targets.shape[0]
accuracy = 100 * total_correct / total_samples
```
- `train()/eval()` switch layer behaviours such as Dropout/BatchNorm, **not** parameter updates or backprop.
- `no_grad()` prevents graph tracking; `optimizer.step()` updates parameters.
- Aggregate **correct counts and sample counts** across batches (don't average unweighted batch percentages).

## 2. Slice layout mnemonic
**START → offset; STEP → stride; COUNT → shape.**
```text
1 original shape/stride
2 enumerate selected row/column indices
3 new shape = counts
4 new stride = original stride × step
5 offset = sum(start × original stride)
6 storage position = offset + sum(local index × new stride)
```
Basic slice/transpose usually share storage; non-contiguous **does not mean copy**.
`x[2]` removes axis, `x[2:3]` retains length-one axis, `x[[2]]` advanced indexing usually copies.

## 3. CEL and optimisation
`L = -sum_i(y_i log p_i) = -log(p_true)` for one-hot ground truth.
One-hot is **true class**, not argmax prediction. `nn.CrossEntropyLoss()` normally takes raw logits and integer class targets.
`w_new = w_old - learning_rate * dL/dw`. **Never multiply the update by w_old again.**

## 4. Axis and shape traps
- grayscale image `(height,width)`; video `(frames,height,width)`; mono audio `(samples,)`.
- `mean(dim=1)` eliminates axis 1 unless `keepdim=True`; `sum(dim=2)` sums over the third axis.
- `transpose(1,2)` swaps axes (view); `reshape` may return view or copy.
- `nn.Linear(in,out).weight` stored as `(out,in)`, bias `(out,)`.

## 5. Representation and memory
- 8 bits = 1 byte; `float32` = 4 bytes, `float16` = 2 bytes.
- Storage bytes = element count × bytes/element. Training needs extra activation, gradient and optimiser memory.
- `bfloat16` exchanges precision for exponent range; half precision speedups depend on hardware.

## 6. Oral one-liners
- Deep learning: flexible learned representations; scalable minibatch training; mature libraries/tooling.
- Training parameters are fitted using loss/gradients; hyperparameters configure learning.
- Validation tunes models; test reserved for final evaluation. Don't call train/val gap statistical variance.
- Globals create hidden dependencies; docstrings state purpose, args and returns.
- No activation between affine layers → equivalent single affine transformation.

## Tonight's operational checklist
Course slides specify instructor approval before generative AI use in coursework (Approach 2): confirm lab-specific permission before using AI on the assessed notebook.
Upload notebook, have TA verify, demonstrate successful run, verify recorded mark; complete UReply attendance between 7–9 pm.
