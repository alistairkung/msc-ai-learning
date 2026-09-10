# AIMS5702 Lecture 1/2 — pre-lecture bridge and Lecture 1 reflection

_Date: 2026-09-10_
_Status: Lecture 1 attended; Lecture 2 systems material below remains pre-read preview unless explicitly noted_

## Evidence boundary

Only the **introductory / Lecture 1 material** was actually covered in class on 10 Sep. The dtype, memory, stride, view/contiguity and `einsum` work later in this note came from pre-reading the supplied later deck and a guided pre-lecture session. Do **not** record those systems topics as already taught in class.

## Lecture 1 reflection — representation translation is the important gap

The lecturer used mathematical index notation such as `i`, `j`, etc. heavily when reasoning about tensor operations. This makes the later appearance of Einstein summation feel more coherent: `einsum` is close to executable index/contraction notation.

The learner's strongest existing representation remains **tensor shapes**. Preserve that as the primary reasoning anchor rather than replacing it with index notation.

New course-facing objective:

> Become bilingual between diagram/network notation, tensor-shape notation, mathematical index notation, and PyTorch code.

A useful translation pattern is:

```text
index notation          shape reasoning                 semantic meaning
X_ij                    X.shape = (i,j)                 i=samples/batch, j=input features
W_jk                    W.shape = (j,k)                 j=input features, k=output features
Σ_j X_ij W_jk           (i,j) @ (j,k)                  contract/sum over j
Y_ik                    Y.shape = (i,k)                 samples preserved, new feature width
```

For implementation, simple matrix multiplication should still normally be read/written naturally as `X @ W`; `einsum` is a useful general tensor-contraction language and a bridge to the lecturer's mathematical notation, not a replacement for ordinary shape reasoning.

### Diagram / MLP translation

Lecture 1 also used multilayer-perceptron diagrams and parameter counting in a flowchart/network style. The learner found the underlying idea harder to process in that representation than in the tensor-shape representation already practised in Lessons 29–31.

Treat this as a **representation-translation gap, not evidence of a parameter-counting conceptual gap**. Lesson 30 already contains parameter counting for a `10 -> 6 -> 1` MLP.

Future AIMS5702 retrieval should deliberately practise:

```text
network diagram
    ↕
tensor shapes
    ↕
index notation
    ↕
PyTorch modules / operations
    ↕
parameter count
```

Example translation template:

```text
diagram: 5 inputs -> 3 hidden -> 2 outputs

shapes:
(B,5) -> (B,3) -> (B,2)

weights/biases:
Linear(5,3): 5*3 + 3
Linear(3,2): 3*2 + 2

index view:
X_bi W_ih -> H_bh
H_bh V_ho -> Y_bo
```

The goal is not to force index notation to become the learner's primary mental model. The goal is fast translation **into and out of shapes**, so mathematical notation and lecturer diagrams stop imposing an extra cognitive cost.

## Existing preparation retrieved successfully before class

The pre-lecture session cold-recalled:

- tabular shape `(samples, features)`;
- reduction semantics: the selected axis disappears;
- `(n,d) - (d,)` broadcasting across samples;
- matrix multiplication shape `(batch,in) @ (in,out) -> (batch,out)`;
- tensor reductions after transformations.

This aligns with Lessons 10, 11 and 27. Shape/axis reasoning remains worth occasional retrieval. An initial image-layout question was deliberately discarded because image/channel conventions had not been part of prior preparation.

## Pre-read preview — not yet taught in the 10 Sep lecture

### Dtypes and memory estimation

Core model introduced during the guided pre-read:

```text
8 bits = 1 byte
float32 = 4 bytes/value
float16 = 2 bytes/value
int8 = 1 byte/value

number of elements = product(shape)
memory bytes = number of elements * bytes per element
```

Successful changed examples included:
- `(100,8)` float32 -> 800 elements -> 3200 bytes;
- 1B float32 parameters -> roughly 4 GB decimal storage;
- 3B float16 parameters -> roughly 6 GB decimal storage;
- `(64,512)` float16 -> 32768 elements -> 65536 bytes.

The learner initially carried the correct `4 billion bytes` arithmetic into the wrong output unit (`4 billion GB`), then corrected the bytes-to-GB conversion and subsequent examples were correct.

### Floating-point intuition

Introduced only at pre-read depth:

```text
more exponent bits -> wider magnitude/range
more mantissa/significand bits -> greater precision
```

Exact IEEE encoding remains new/not established.

### Flat storage, shape, stride and offset

New guided mental model:

```text
tensor view = logical shape + strides + offset over underlying flat storage
```

For normal contiguous tensors:

```text
shape (2,3)   -> stride (3,1)
shape (2,3,4) -> stride (12,4,1)
```

Important fresh fragile point: the learner initially recomputed strides from a sliced view's new shape, e.g. predicting `(8,4,1)` for a `(2,2,4)` view. The correction was that basic slicing does not repack storage; a view may retain `(12,4,1)`.

Durable rule:

> Shape alone does not determine the stride of a view. For a view, reason about how it walks the underlying storage.

### Views, copies and contiguity

Experimentally inspected in PyTorch during the pre-read:

- `x.T` changed `(2,3)/(3,1)/contiguous=True` to `(3,2)/(1,3)/contiguous=False`;
- mutation through the transpose view changed the original tensor, confirming shared storage;
- basic slicing such as `x[:,1:]` shares storage;
- explicit index-list selection such as `x[:,[0,2]]` produced independent storage in the exercised case;
- step slicing `x[:,::2]` was reasoned as representable by changed strides;
- shared storage and contiguity were distinguished as separate properties.

### Einstein summation

Introduced in the pre-read because it appears in the later supplied deck. Durable reading rule:

```text
indices on the output survive
contracted/omitted indices are summed over
```

Examples discussed:

```text
ij->i      row sums
ij->j      column sums
ij,j->i    matrix-vector product
ik,kj->ij  matrix multiplication as an einsum expression
```

A small numerical example expanded `ij,j->i` into elementwise products followed by a sum over `j`. The learner correctly identified surviving/summed indices and output shapes after explanation. This remains **guided pre-read evidence**, not independent mastery or lecture-covered material.

## Coding evidence from pre-read

Interactive scratch/REPL work inspected:

- `.shape`;
- `.stride()`;
- `.is_contiguous()`;
- transpose behaviour;
- mutation through shared views;
- mutation after explicit index-list selection.

No numbered lesson was created because this was course preparation rather than the next sequential foundation lesson.

## Next AIMS5702 study block

Prioritise **representation translation** before adding more content:

1. Take actual MLP/network diagrams from Lecture 1 and translate diagram -> shapes -> parameter count.
2. Add index notation to the same examples: shapes -> indices and indices -> shapes.
3. Keep `@`/shape reasoning as the implementation anchor; use simple `einsum` examples to make index contraction readable.
4. When Lecture 2 is actually taught, cold-check dtype memory and stride/view concepts rather than replaying the full pre-read.
5. Record what Lecture 2 actually emphasizes before expanding the systems track.
