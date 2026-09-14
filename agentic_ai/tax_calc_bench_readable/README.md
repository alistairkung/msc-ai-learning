# Readable TaxCalcBench walkthrough

This folder rewrites the **FTEC5660 Tutorial 1 TaxCalcBench example** in a deliberately boring, readable style.

The goal is not to learn US tax law. The goal is to make the lecturer's architecture obvious enough to inspect line by line:

```text
raw taxpayer JSON
    ↓
LLM: inventory source facts
    ↓
Python: validate inventory
    ↓
LLM: place each fact on a Form 1040 line
    ↓
Python: validate placements
    ↓
LLM: externalise tax rules as Python code
    ↓
Python: validate/load the generated rules
    ↓
Python: compute the return deterministically
    ↓
format for TaxCalcBench
    ↓
benchmark evaluator
```

The lecturer's notebook uses the TaxCalcBench case:

```text
single-w2-unemployment-1099g
```

The known key outputs shown in the tutorial are reproduced in the local fixture:

```text
Line 1a     145,000
Line 9      157,345
Line 11     157,345
Line 12      14,600
Line 15     142,745
Line 16      27,301
Line 25d     13,235
Line 37      14,066
```

## Files

### `lecturer_case.py`

A compact fixture containing the **inventory and placement artifacts printed by the lecturer's notebook** for the chosen benchmark case. This lets the manual Python path run without an LLM or external benchmark checkout.

### `manual_tax_rules.py`

The 2024 single-filer standard deduction and tax-bracket calculation written explicitly in Python.

This is intentionally more verbose than the lecturer's generated function. It exposes the contribution from each bracket so the arithmetic can be read/debugged instead of hidden in a loop.

### `manual_return.py`

A readable version of the lecturer's `compute_return(...)` function. It implements the Form 1040 subtotal arithmetic with named intermediate calculations and comments.

This is the deterministic heart of the example.

### `checks.py`

Readable versions of the notebook's inventory/placement validation ideas.

### `readable_workflow.py`

Two views of the same architecture:

1. `run_imperative_workflow(...)` — ordinary Python with explicit variables after every stage;
2. `build_lcel_workflow(...)` — the equivalent LCEL pipeline, but with named stage functions instead of nested lambdas.

Read the imperative version first.

### `benchmark_adapter.py`

Optional integration with an actual local checkout of `column-tax/tax-calc-bench`. It loads the same benchmark case, derives the form lines, renders the calculated return in benchmark format, and calls the official evaluator.

The core tests do **not** require cloning TaxCalcBench.

## Suggested reading order

```text
lecturer_case.py
    ↓
manual_tax_rules.py
    ↓
manual_return.py
    ↓
checks.py
    ↓
readable_workflow.py: run_imperative_workflow
    ↓
readable_workflow.py: build_lcel_workflow
    ↓
benchmark_adapter.py
```

## Run the self-contained tests

```bash
pytest agentic_ai/tax_calc_bench_readable -q
```

The tests verify the manual tax brackets and the exact key Form 1040 outputs printed in the lecturer's example.

## Optional: run against the real TaxCalcBench evaluator

Clone the benchmark beside the learning repo (or anywhere you prefer):

```bash
git clone https://github.com/column-tax/tax-calc-bench
pip install lxml
```

Then use `benchmark_adapter.load_benchmark_context(...)` with that checkout path. The adapter intentionally keeps the external benchmark dependency out of normal unit tests.

## Important safety boundary

The lecturer demonstrates `exec(...)` on LLM-generated Python to teach the pattern **generate artifact → validate artifact → execute artifact**.

`readable_workflow.py` includes a matching educational loader so the example mirrors the lecture. **Do not execute untrusted generated code this way in a real application.** Python `exec` is not a sandbox.

The learning point is the trust boundary, not that `exec` is a production deployment technique.
