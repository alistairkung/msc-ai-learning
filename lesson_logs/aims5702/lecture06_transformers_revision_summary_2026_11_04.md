# AIMS5702 — Lecture 6: Transformers Revision Summary

_4 November 2026. Sources: Lecture 6 slides, lecturer transcript, AIMS_week6.ipynb and guided revision. This is a study summary, not independent mastery evidence._

## 1. Why Transformers?

| Architecture | Main characteristic |
|---|---|
| CNN | Local receptive fields; distant interactions need enough receptive-field growth |
| RNN | Sequential hidden-state processing limits parallelisation |
| Transformer | Self-attention permits direct distant-token interactions in one attention layer |

**Advantage:** short dependency paths, parallelisable processing. **Trade-off:** full attention makes quadratically many pairwise comparisons.

## 2. Tokenisation, embeddings and contextual states

**Text → tokenizer → token IDs → learned embeddings → position information → Transformer layers → contextual hidden states.**

- Tokens may be words, subwords, punctuation or special tokens.
- A **tokenizer** returns token IDs, *not* embeddings.
- An **embedding** is a learned numerical vector representing a token.
- A **contextual hidden state** incorporates information from other tokens. Completed layer outputs become the next layer's inputs.
- BERT-base has hidden representation width **768**.

## 3. Query, key and value (Q/K/V)

Each token input vector produces three distinct learned projections. With **rows as tokens** in matrix $X$:

$$
Q=XW_Q,\qquad K=XW_K,\qquad V=XW_V.
$$

| Vector | Meaning | Role |
|---|---|---|
| Query (Q) | What information am I looking for? | Compare against keys |
| Key (K) | What information might I be relevant to? | Query–key compatibility |
| Value (V) | What information do I contribute? | Information that gets combined |

**Scaled dot-product attention:**

$$
\operatorname{Attention}(Q,K,V)=
\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V.
$$

1. **$QK^T$** computes dot-product compatibility scores. Each row corresponds to the query of one token, each column to a key.
2. **Scaling** by $\sqrt{d_k}$ prevents large dot products from producing excessively sharp softmax distributions.
3. **Row-wise softmax** produces nonnegative attention weights that sum to **1 in each row**.
4. **Attention weights × values:** each output token receives a weighted sum of the **other tokens' value vectors**, including itself if allowed.

The lecturer's compressed notation:

$$
o_i=\sum_j\alpha_{ij}v_j
$$

means **for output token $i$, multiply each token $j$'s value vector by the weight assigned to it, and add those resulting vectors**. The scalar weight multiplies the *whole* vector, not a coordinate representing a particular target token.

### Mini-example

With weights $[0.2,\ 0.8]$ and value vectors $[1,3]$ and $[2,1]$:

$$
o_i=0.2[1,3]+0.8[2,1]=[1.8,1.4].
$$

This is an **attention output vector**, not a predicted word. The *full Transformer block* additionally includes residual, feed-forward and normalisation operations before its output enters the next layer.

**Masking distinction:** a causal language model excludes future tokens from attention, whereas BERT's bidirectional encoder can use both left and right context. The tokenizer's padding `attention_mask` is **not** the learned attention-weight matrix.

## 4. Multi-head attention

Each head has its own Q/K/V projections and computes attention in parallel; heads can learn distinct relationships. The outputs are **concatenated and linearly projected** into the model representation dimension.

- `d_model`: width of token representations, chosen by model designers.
- `nhead`: number of parallel attention heads within each layer.
- `num_layers`: number of sequential encoder layers.
- With `d_model=768` and `nhead=8`, the usual equal head width is $768/8=96$.
- **Three layers with four heads** means three sequential layers, each containing four heads.

## 5. Positional encoding

Plain attention has no inherent signal for token **order**. The lecturer identifies desirable properties: distinguishable positions, relative-distance relationships, generalisation across lengths, and determinism.

| Approach | Mechanism | Conceptual contrast |
|---|---|---|
| Raw position numbers | Associate indices 0,1,2,... with token vectors | Large unscaled values can dominate other features |
| Sinusoidal positional encoding | Add bounded sine/cosine vectors with different frequencies | Distinct deterministic patterns; supports relative relationships |
| RoPE | Rotate query/key vectors according to position | Relative position appears through differences in rotation in Q–K comparisons |

The **original Transformer** adds sinusoidal position vectors to the token embeddings. **RoPE** modifies Q/K through rotations instead.

The transcript demonstrates values such as $\sin(i/100)$ and explains rotary intuition; it does **not** show a full RoPE implementation. Detailed derivations are lower revision priority, not confirmed exclusions.

## 6. Complexity

For $N$ tokens, each query compares with $N$ keys:

$$
\text{pairwise comparisons}=N^2.
$$

With attention-vector dimension $D$, pairwise attention work is on the order of $O(N^2D)$. Including standard dense projections, one common approximation is $O(N^2D+ND^2)$, when model and projected widths are comparable.

- Double tokens → **4×** comparisons.
- Triple tokens → **9×** comparisons.
- Short dependency paths **do not** imply small total computation.

## 7. Complete Transformer encoder architecture

**Multi-head attention → residual connection / layer norm → per-token feed-forward network → residual connection / layer norm → completed layer output.**

- **Attention:** mixes information *between tokens*.
- **Feed-forward network (FFN):** transforms features *within each token*.
- **Residual connections:** make deep networks easier to optimise.
- **Layer normalisation:** helps stabilise hidden representations.
- Exact pre-norm vs post-norm ordering varies across architectures.

## 8. Week 6 workbook: PyTorch and Hugging Face

### Autograd (backprop / Assignment 3 background)

~~~python
x = torch.randn(3, 4, requires_grad=True)
y = torch.relu(x)
y.backward(torch.ones_like(y))
print(x.grad)
~~~

`requires_grad=True` tracks gradients; `backward(upstream)` propagates supplied gradients, and `.grad` contains accumulated gradients. `torch.no_grad()` disables recording during its context, unlike `model.eval()` which changes module evaluation behaviour.

### Transformer layer and stacked encoder

~~~python
encoder_layer = nn.TransformerEncoderLayer(
    d_model=768,
    nhead=8,
    dropout=0.1,
)
encoder = nn.TransformerEncoder(
    encoder_layer,
    num_layers=1,
)
~~~

Know `d_model`, `nhead`, `num_layers`, `dropout` and the 768/8 = 96 head-width calculation.

### Pretrained BERT

~~~python
from transformers import AutoTokenizer, AutoModel

model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

inputs = tokenizer(sentence, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)
last_hidden_states = outputs.last_hidden_state
~~~

| Call | Meaning |
|---|---|
| `AutoTokenizer.from_pretrained` | Load tokenizer matching BERT |
| `AutoModel.from_pretrained` | Load BERT base model and pretrained weights |
| `return_tensors="pt"` | Produce PyTorch tensors |
| `model(**inputs)` | Unpack tokenizer dictionary into named arguments; forward pass |
| `last_hidden_state` | Contextual representation for every input token |

BERT-base output tensor shape: **`(batch_size, sequence_length, 768)`**. These representations can feed downstream classifiers or other models; `AutoModel` is not a next-token text generator by itself.

### Positional code demonstration

~~~python
pairs = [(i, math.sin(i / 100)) for i in range(100)]
~~~

This is a simple teaching example, not full sinusoidal encoding or RoPE.

## 9. Recognition distinctions

| Know | Do not confuse with |
|---|---|
| Token IDs | Embedding vectors |
| Initial embeddings | Contextual hidden states |
| $QK^T$ scores | Softmax attention weights |
| Attention weights | Value vectors |
| `nhead` | `num_layers` |
| Sinusoidal addition | RoPE rotations |
| Short dependency path | Low total computational work |
| Tokenizer `attention_mask` | Learned Q/K attention matrix |
| `AutoTokenizer` | `AutoModel` |
| BERT hidden states | Generated text |

**Assessment priorities:** understand conceptual Q/K/V, score → softmax → weighted values, head/layer distinction, positional encoding, $N^2$ scaling, and workbook APIs. Calculator-heavy exponentials and RoPE complex-number proofs are lower priority given the lecturer's practical framing; they are not officially ruled out.

**Evidence caution:** 4 November's discussion demonstrated same-session conceptual understanding. A fully correct unassisted attention calculation and delayed retrieval are **not yet established**.
