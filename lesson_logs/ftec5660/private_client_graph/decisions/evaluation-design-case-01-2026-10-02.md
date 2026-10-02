# Private Client Graph — Case 01 evaluation-design decisions, 2 Oct 2026

## Context

Case 01 has now crossed the first real end-to-end implementation boundary:

```text
source.txt
    ↓
LLM semantic extraction
    ↓
RelationshipCandidate[]
    ↓
deterministic validation / graph construction
    ↓
CanonicalGraph
```

A live extraction recovered the intended six Case 01 relationships with no unsupported extras. The deterministic graph-construction boundary was then designed and implemented separately from extraction. This session focused on defining the benchmark semantics before delegating the evaluation implementation.

## Decision 1 — evaluation is a separate concern

Evaluation should consume a predicted canonical graph and ground truth. It should not know which model produced the prediction or how extraction was implemented.

```text
predicted CanonicalGraph + ground_truth.json
                    ↓
                evaluator
                    ↓
          relationship + provenance metrics
```

This keeps model behaviour, deterministic graph construction and benchmark scoring independently testable.

## Decision 2 — compare semantic relationships, never generated IDs

Entity and evidence IDs are graph-local implementation handles. Their literal values are not part of semantic correctness.

Relationship scoring therefore compares semantic edge keys:

```text
(source_name, relationship_type, target_name)
```

rather than internal IDs.

## Decision 3 — normalize representation trivia before scoring

Symmetric relationship types are canonicalised before comparison:

- `spouse_of`
- `sibling_of`

Their endpoint names are sorted into deterministic order. Directed relationships such as `parent_of`, `settlor_of`, `trustee_of` and `beneficiary_of` retain direction.

Both predicted and ground-truth edges should pass through the same semantic normalisation before set comparison.

## Decision 4 — relationship quality uses exact set comparison

Let predicted and ground-truth semantic edge sets be (P) and (G).

```text
TP = P ∩ G
FP = P - G
FN = G - P
```

Report:

- true positives;
- false positives;
- false negatives;
- precision;
- recall;
- F1.

The evaluator should also return the actual diagnostic edge sets, because they are more useful for failure analysis than headline metrics alone.

## Decision 5 — provenance ground truth stores approved evidence per relationship

A single expected quote is too brittle because a realistic source may repeat the same fact in multiple valid passages.

Each ground-truth relationship should therefore carry:

```text
approved_evidence: [exact source span, ...]
```

Example:

```json
{
  "source": "Alice Chen",
  "type": "parent_of",
  "target": "Bob Chen",
  "approved_evidence": [
    "Alice Chen confirmed that Alice Chen and David Chen are the parents of Bob Chen."
  ]
}
```

This keeps provenance scoring deterministic while allowing multiple valid source spans.

`expected_extraction.json` and `ground_truth.json` have different roles:

- `expected_extraction.json` is one ideal raw semantic LLM output;
- `ground_truth.json` is the benchmark answer key, including all approved evidence alternatives.

## Decision 6 — provenance is scored only on correctly recovered edges

A missed relationship is already penalised by relationship recall. It should not be penalised again as a provenance failure.

For each true-positive edge:

1. resolve every predicted `evidence_id`;
2. collect the attached `supporting_text` values;
3. compare them with that edge's `approved_evidence`;
4. provenance passes if the intersection is non-empty.

In other words:

> At least one attached evidence item must match at least one approved evidence span.

If a correctly predicted edge has several evidence IDs and one is approved, the edge passes provenance in v1.

## Decision 7 — first provenance metric stays deliberately simple

For v1:

```text
provenance_accuracy =
    true-positive edges with >=1 approved evidence span
    /
    all true-positive edges
```

Also return the concrete provenance passes and failures.

A stricter future diagnostic such as valid attached evidence / all attached evidence may later measure provenance precision, but it is deliberately excluded from the first evaluator.

## Decision 8 — deterministic grounding validation remains distinct from provenance scoring

Graph construction already checks that every `supporting_text` occurs verbatim in the source.

That answers:

> Is this evidence grounded in the document?

Evaluation answers a different question:

> Is this one of the approved source spans supporting this particular correct edge?

Do not collapse these into one metric.

## Evidence boundary

Strong learner-owned reasoning in this session included:

- challenging a mechanical transfer of the receipts validation/normalisation architecture;
- identifying entity/graph construction as its own bounded deterministic context;
- preserving extraction and graph construction as separate responsibilities;
- insisting that every deterministic behaviour have focused unit tests;
- recognising that evaluation must ignore generated IDs;
- rejecting exact-one-span provenance scoring as too brittle for realistic repeated evidence;
- selecting approved-evidence lists per relationship;
- choosing at-least-one provenance matching for edges with multiple evidence references;
- choosing symmetric semantic normalisation before evaluation.

Implementation of the extraction and graph-construction plumbing was deliberately delegated after the contracts were designed. This should not be treated as cold framework implementation mastery.

## Next step

Delegate the smallest deterministic evaluator behind this frozen benchmark contract:

```text
CanonicalGraph + ground_truth.json
    ↓
semantic edge normalisation
    ↓
TP / FP / FN + precision / recall / F1
    ↓
true-positive provenance match against approved_evidence
    ↓
diagnostic EvaluationResult
```

Every deterministic scoring behaviour should receive focused unit-test coverage before adding additional benchmark complexity.
