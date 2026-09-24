# AIMS5702 Lecture 3 — live lecture

**Date:** 2026-09-24  
**Source boundary:** learner report plus screenshots from the live lecture mini-quiz.

## Lecture / quiz evidence

Lecture 3 was attended after the targeted pre-lecture bridge. The supplied quiz screenshots sampled cross-entropy, linear-layer parameter shapes, broadcasting, einsum, stride/storage offset, tensor view-vs-copy behavior, CPU/GPU tensor movement and Python coding style.

The learner reported **6/8 correct (75%)**.

Two misses shown in the screenshots:

- **Unequal-rank broadcasting:** for shapes `(4,1,3)` and `(2,3)`, the learner chose runtime error. Right-aligning dimensions gives an output shape of `(4,2,3)`.
- **PyTorch Linear storage convention:** for `nn.Linear(784,10)`, the learner chose weight `(784,10)`, bias `(10,)`. PyTorch stores the weight as `(out_features,in_features) = (10,784)`, with bias `(10,)`.

The second miss is a convention switch rather than evidence that the earlier linear-layer concept failed. The pre-lecture bridge deliberately used the lecturer's equation convention first:

```text
equation convention used in prep: W -> (in, out)
PyTorch nn.Linear.weight:          W -> (out, in)
bias:                              b -> (out,)
```

The other quiz items were reported correct. Treat this as sampled evidence only, not broad mastery.

## Upcoming cadence and plan

Learner-reported schedule:

```text
week after 24 Sep -> lecture break
following teaching week -> in-class graded lab
15 Oct -> CNN lecture
```

Use the lecture-break week first to consolidate Weeks 1–3 to graded-lab readiness, then begin a bounded CNN bridge. The lab is the nearer assessment target.

Consolidation targets:

- unequal-rank broadcasting by right-alignment;
- equation weight orientation vs PyTorch Linear storage;
- indexed/output-shape and dataset-objective notation;
- TensorDataset / DataLoader, batch-label shapes, zero_grad() and validation no_grad();
- stride/offset and view-vs-copy distinctions;
- one changed end-to-end PyTorch classification-pipeline reconstruction.

After that foundation is stable, build toward CNN through image tensor shapes -> locality -> weight sharing -> kernels/filters -> channels -> stride/padding -> output-shape reasoning -> a small Conv2d model.

## Evidence boundary

The 75% mini-quiz is useful sampled evidence, not a course mastery score. The two errors are narrow representation/API-convention gaps and should become targeted retrieval items during the lecture break.
