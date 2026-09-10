# FTEC5660 Pattern 1 — Prompt Chaining

_Date: 2026-09-08_
_Status: **Concept taught; tutorial partial — class stopped after successful JSON parsing**

## Why this log exists

This is the focused retrieval blueprint for **Pattern 1: Prompt Chaining**.

It separates three things deliberately:

1. **slide-deck concepts** that belong to the taught pattern;
2. **tutorial code actually reached in class**;
3. **syntax fluency to build later this week** through an independent reconstruction session.

Do not treat later cells in the supplied tutorial notebook as completed class material merely because they exist in the notebook.

---

# 1. Course concept — what prompt chaining is

The slide deck defines prompt chaining as:

> solving complex tasks with LLMs by breaking work into sequential, focused steps.

Core pattern:

```text
complex task
    -> focused step 1
    -> focused step 2
    -> focused step 3
    -> final result
```

Each stage has a narrower objective than a single large prompt, and the output of one stage becomes input to the next.

## Why one large prompt can fail

The deck highlights several reasons:

- competing objectives can cause parts of a long instruction to be ignored;
- the model can lose track of the original goal;
- early errors can propagate downstream;
- later stages may require validated structured outputs;
- context-window pressure grows with task size;
- greater task complexity increases hallucination risk.

Prompt chaining responds by **decomposing** the work and giving each stage a clearer interface.

## Pattern overview

The lecture's intended design shape is:

```text
sub-task 1
   |
   | output
   v
sub-task 2
   |
   | output
   v
sub-task 3
```

Important properties:

- break the complex task into smaller sub-tasks;
- design one prompt per sub-task;
- optimise/debug steps independently;
- pass step outputs forward;
- use modularity to improve interpretability, debugging and robustness.

---

# 2. Reliability comes from the boundaries between steps

A particularly important part of the lecture is that a prompt chain is **not just several LLM calls in a row**.

The deck explicitly recommends:

- narrow objectives per stage;
- deterministic processing between stages, such as validation/normalisation;
- conditional repair prompts for malformed or missing output;
- distinct roles when useful;
- structured handoffs such as JSON/XML.

This makes the **interface between stages** an engineering object in its own right.

Useful mental model:

```text
LLM step
   -> structured output
   -> deterministic check / normalisation
   -> next step
```

That strongly connects with prior SWE instincts around contracts, validation and pipeline boundaries.

---

# 3. Generic chain shape from the slides

The deck's generic template is roughly:

```text
Generate
  -> Validate
       -> pass -> Final output
       -> fail -> Repair prompt -> Re-validate
```

with explicit retry/stop conditions and a safe failure path when retries are exhausted.

The lecture's rule of thumb is to use chaining when the task decomposes into **stable, checkable stages** with explicit interfaces and acceptance criteria.

## When chaining is a good fit

- stages are predictable and have clear boundaries;
- intermediate outputs can be checked;
- stages need different contexts or tools;
- a failed stage can be repaired without rerunning the whole task.

## When it is not the right pattern

The deck says not to default to chaining when:

- one call already meets the quality target;
- latency is critical;
- reasoning must stay tightly integrated across all information;
- subtasks are independently parallel → use parallelisation;
- path depends on input → routing;
- repeated generate/critique loops → evaluator/optimizer;
- the model itself must choose steps/tools → agent.

---

# 4. Context engineering connection

Prompt chaining is also a context-engineering problem.

Each stage should receive the **minimum sufficient, relevant and trusted context** needed for its job.

The lecture explicitly broadens context beyond the prompt text itself to include things such as:

- system instructions;
- retrieved documents;
- tool outputs;
- state/history;
- structured outputs.

Poor handoffs can lose information; excessive decomposition can also reduce end-to-end coherence.

---

# 5. Risks / trade-offs to retrieve

Prompt chaining buys control but adds moving parts.

The lecture highlights:

- upstream errors can propagate;
- more LLM calls increase latency and cost;
- more components add failure and maintenance points;
- badly designed handoffs can lose relevant context;
- over-decomposition can damage overall coherence.

Evaluation should therefore consider not only correctness but also:

- end-to-end quality;
- latency;
- cost;
- retry rate;
- failure rate.

---

# 6. Tutorial boundary — what was actually reached in class

The supplied notebook goes much farther than the class reached. **Current learning evidence stops at the first successful structured parse of the expense ledger into JSON.**

Do not treat later notebook sections — Python computation, `RunnablePassthrough.assign`, full chain wiring, TaxCalcBench, generated Python rules, gates, etc. — as taught/completed yet.

## Environment / model setup reached

The tutorial introduced:

```python
from langchain_deepseek import ChatDeepSeek
```

and construction of an `llm` object with:

- a DeepSeek model name;
- API key;
- low temperature for extraction-style work;
- thinking disabled for the tutorial's simple one-pass comparison.

The model was then called with:

```text
llm.invoke(...)
```

and the returned message exposes `.content` plus usage metadata.

### Current syntax-learning boundary

Do not make DeepSeek-specific configuration details the main memorisation target. The durable target is:

```text
construct model wrapper
    -> invoke model
    -> inspect output
```

---

# 7. First LCEL chain reached

The tutorial introduced **LangChain Expression Language (LCEL)** and the use of `|` to compose steps.

Important imports encountered:

```text
ChatPromptTemplate
StrOutputParser
JsonOutputParser
RunnableLambda
RunnablePassthrough
```

However, at the current class stopping point only the first three are substantively in scope. `RunnableLambda` / `RunnablePassthrough` appear in the import block but the class had not yet reached the notebook sections that actually teach/use them.

## Prompt templates

The tutorial used:

```text
ChatPromptTemplate.from_template(...)
```

with placeholders such as:

```text
{text_input}
{specifications}
{ledger}
```

A prompt template therefore acts like a parameterised prompt whose values are supplied later when the chain is invoked.

## String parser

The first small two-stage example used:

```text
prompt -> llm -> StrOutputParser()
```

`StrOutputParser()` converts the model response object into an ordinary string suitable for passing onward.

## Chaining a sub-chain into the next prompt

The notebook then used a mapping shape where the first extraction chain provides the value for a later prompt variable:

```text
{"specifications": extraction_chain}
    -> next prompt
    -> llm
    -> parser
```

This syntax is important enough to learn by reconstruction rather than merely recognise.

---

# 8. Expense-ledger example reached

The tutorial constructs a synthetic finance ledger with:

- 120 rows;
- several categories;
- inconsistent money formatting;
- refunded rows that must be excluded;
- known deterministic ground truth generated in Python.

The purpose is to create a task where **parsing each row is easy but doing long aggregation in one generation is unreliable**.

## Single-prompt failure

A single prompt asks the LLM to:

```text
parse
+ identify refunds
+ normalise money formats
+ aggregate categories
+ compute grand total
+ produce JSON
```

The result is well-formed and plausible-looking but numerically wrong; repeated runs produce different totals.

Important lesson:

> **Well-formed structured output is not the same as correct output.**

The tutorial deliberately has a deterministic `score()` function so the result can be checked against known truth.

---

# 9. Decomposition introduced in class

The notebook proposes this division of labour:

```text
1. Parse      -> LLM
2. Compute    -> Python
3. Explain    -> LLM
```

This is a very useful anchor because it shows that prompt chaining does **not** mean forcing the LLM to do every stage.

The class reached **Step 1: Parse**.

The parse prompt asks the model to convert every ledger row into a JSON list with a fixed schema containing:

```text
id
category
amount
refunded
```

It explicitly says:

- do not filter;
- do not sum;
- normalise amount into a plain number;
- convert refund status into a boolean;
- output JSON only.

The chain shape is:

```text
prompt_parse
    | llm
    | JsonOutputParser()
```

and it is invoked with a dictionary containing the ledger input.

The supplied execution successfully parsed **120 rows** and returned Python-accessible structured data.

**Class stopping point:** around this successful JSON parse. The notebook then proceeds into checking the parse, deterministic Python computation, and wiring the complete chain, but those later sections should remain **future material** until actually studied.

---

# 10. Syntax debt to close this week

The conceptual idea is ahead of the current ability to reproduce LangChain syntax unaided.

Goal for a dedicated practice session this week:

> **Be able to reconstruct the small LangChain/LCEL patterns used up to the JSON-parse boundary from memory, not merely recognise them in the notebook.**

This should be learned the same way NumPy syntax was learned: small pieces, repeated retrieval, changed examples, then composition.

## Syntax inventory to make retrievable

### A. Model wrapper

Be able to reconstruct the role/skeleton of:

```text
ChatDeepSeek(...)
llm.invoke(...)
result.content
```

Do not over-focus on every DeepSeek configuration field.

### B. Prompt templates

Retrieve:

```text
ChatPromptTemplate.from_template(...)
```

and understand how `{variable}` placeholders are supplied by invocation dictionaries.

Also notice that literal JSON braces inside a Python/LangChain template may need doubled braces:

```text
{{ ... }}
```

so they are not mistaken for template variables.

### C. LCEL composition

Retrieve the core visual grammar:

```text
prompt | llm | parser
```

and be able to explain what value is flowing through each boundary.

### D. Output parsers

Know the conceptual difference:

```text
StrOutputParser
    -> plain string

JsonOutputParser
    -> parsed structured Python value
```

### E. Invocation

Retrieve:

```text
chain.invoke({"input_variable": value})
```

and be able to map the dictionary key to the prompt placeholder.

### F. Sub-chain mapping

Be able to reconstruct/explain this kind of shape:

```text
{"some_variable": earlier_chain}
    | next_prompt
    | llm
    | parser
```

The target is not cargo-cult syntax; explain **why the mapping key matches the next prompt's placeholder**.

---

# 11. Planned syntax-learning session

Do **not** start by copying the notebook.

Use an incremental reconstruction loop.

## Stage 1 — role recall

Without code in front of you, explain what each of these does:

- `ChatDeepSeek`
- `ChatPromptTemplate`
- `StrOutputParser`
- `JsonOutputParser`
- `|`
- `.invoke()`

Stop and repair any conceptual confusion before typing.

## Stage 2 — one-step chain

From a blank file/notebook, reconstruct a tiny task of the form:

```text
input
  -> prompt template
  -> model
  -> plain string
```

Use a **new domain/example**, not the laptop text verbatim.

## Stage 3 — structured output

Change the task so the model returns JSON and reconstruct the chain using the JSON parser.

Verify the result is actually a Python structure rather than a string that merely looks like JSON.

## Stage 4 — two-step chain

Build:

```text
extract
  -> feed extracted result into second prompt
  -> transform
```

Reconstruct the mapping/sub-chain syntax from memory.

## Stage 5 — finance-domain transfer

Use a small payments/KYC/AML-flavoured example so the syntax is attached to a familiar domain rather than only the tutorial's laptop/ledger examples.

Possible shape:

```text
unstructured payment exception text
   -> extract fields as JSON
   -> second prompt writes a concise investigation summary
```

Keep the example small enough that LangChain syntax remains the learning target.

## Stage 6 — cold reconstruction later

Leave a small skipped/retrieval test or blank exercise that can be revisited later without storing the complete answer beside it, following the same principle used for BFS and NumPy retrieval.

---

# 12. What is NOT yet a fair syntax-recall target

Until the later tutorial section is actually studied, do not quiz or judge mastery of:

- `RunnablePassthrough.assign(...)`;
- `RunnableLambda(...)` composition in the full ledger pipeline;
- full parse -> compute -> explain wiring;
- gates / repair loops implemented in LangChain;
- TaxCalcBench workflow;
- generated Python tax-rule code;
- batch calls or later notebook abstractions.

Those can become retrieval targets after instruction/practice crosses that boundary.

---

# 13. Cold recall — concept

Ask one question at a time.

1. What problem is prompt chaining trying to solve?
2. Why can a single complex prompt fail even when the output looks plausible?
3. What does "pass the output of one step as input to the next" buy us besides decomposition?
4. Why are structured intermediate outputs useful?
5. Where can deterministic validation/normalisation sit inside a prompt chain?
6. Give a case where chaining is appropriate and one where routing/parallelisation/agent planning is a better fit.
7. What are the main latency/cost/maintenance trade-offs of adding more stages?
8. Why is context engineering relevant to each stage in the chain?
9. Explain the expense-ledger decomposition: why LLM -> Python -> LLM rather than LLM -> LLM -> LLM?
10. Why is well-formed JSON not evidence that the underlying finance result is correct?

---

# 14. Cold recall — LangChain syntax boundary

These are fair **after the dedicated syntax practice session**, not necessarily before it.

1. Which object creates a parameterised chat prompt from a template string?
2. What does `|` mean in the LCEL examples?
3. What is the difference between `StrOutputParser()` and `JsonOutputParser()`?
4. How do values get supplied to `{ledger}` or `{text_input}` in a prompt?
5. Reconstruct the minimal shape `prompt -> llm -> JSON parser` from memory.
6. Why might literal JSON examples inside a template require doubled braces?
7. In a two-stage chain, how can the output of the first chain populate a named variable for the next prompt?
8. If the next prompt contains `{specifications}`, what must the mapping key be and why?
9. How can you tell whether the final result is a Python dict/list versus a string containing JSON text?
10. Rebuild a tiny two-stage chain on a changed domain without looking at the tutorial.

---

# 15. Bridge to the next session

This week, schedule one focused **LangChain syntax reconstruction** session.

Success criterion:

> Starting from a blank file/notebook, independently construct a prompt template, compose it with the model and the appropriate parser, invoke it with a dictionary, then build a two-step chain that passes one stage's output into the next.

Do not continue into the later tutorial abstractions until this small syntax grammar feels understandable and reproducible.

Once that is demonstrated, create a numbered implementation/retrieval lesson in the normal repository style rather than prematurely marking the notebook code as mastered.