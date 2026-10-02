# Private Client Graph — Case 01 extraction-contract decisions, 2 Oct 2026

## Context

This session resumed the FTEC5660 Private Client Graph spike after Case 01 ground truth, a realistic attendance-note source, and a proposed expected extraction had already been designed.

The objective was to freeze the smallest semantic handoff before implementing the first real LLM extraction.

The recurring design principle was inherited from the receipts homework:

> Ask the LLM to do semantic interpretation that deterministic code cannot reliably do; keep bookkeeping, consistency and mechanically checkable work deterministic.

## Decision 1 — raw LLM output is relationship candidates only

The first draft of `expected_extraction.json` mixed together:

- semantic extraction;
- entity construction;
- entity IDs;
- evidence IDs;
- graph references;
- evidence deduplication.

That was rejected as giving the probabilistic stage too much responsibility.

The Case 01 LLM output is now conceptually:

```text
RelationshipCandidate
- source_name
- relationship_type
- target_name
- supporting_text
```

Example:

```json
{
  "source_name": "Alice Chen",
  "relationship_type": "parent_of",
  "target_name": "Bob Chen",
  "supporting_text": "Alice Chen confirmed that Alice Chen and David Chen are the parents of Bob Chen."
}
```

The LLM is responsible for answering:

> Who is related to whom, how, and what exact source text supports that semantic claim?

It is not responsible for maintaining graph identity or references.

## Decision 2 — do not ask the LLM to create IDs

Entity IDs and evidence IDs are deterministic bookkeeping.

The LLM should not invent values such as:

```text
entity_001
evidence_003
```

because those identifiers carry no semantic information about what was extracted.

Deterministic code will assign non-null unique IDs after semantic extraction.

The literal ID value is not part of evaluation correctness. Evaluation should compare semantic graph content, while IDs are checked only for structural integrity such as:

- non-null;
- unique where required;
- relationship references resolve to existing entities/evidence.

Random UUIDs, sequential readable IDs, or another internal scheme remain implementation choices rather than benchmark semantics.

## Decision 3 — do not extract a separate entity list in Case 01

Two options were considered:

### Option A — LLM returns entities and relationships

Potential benefit:

- entity recognition becomes independently observable;
- a missed relationship can be distinguished from a missed entity.

Costs:

- duplicates information already present in relationship endpoints;
- creates another probabilistic structure that can disagree with the relationships;
- asks the model to perform work that is not directly part of the Case 01 research question.

### Option B — derive entities from relationship endpoints

The LLM returns only relationship candidates. Deterministic code collects the unique source/target names and constructs the entity set.

This was selected for Case 01.

Reason:

> The current benchmark evaluates relationship-graph reconstruction and provenance, not independent named-entity recall.

A third-agent architecture review independently reached the same conclusion.

### Future trigger for changing this decision

Add a separate `EntityCandidate[]` extraction path when information about an entity becomes useful **even when no supported relationship edge can currently be asserted**.

Possible future triggers include:

- unconnected but graph-relevant entities;
- aliases;
- entity attributes;
- entity-level provenance;
- cross-document identity resolution;
- partially known relationships.

The internal domain model can still treat entities as first-class objects from day one; only the LLM extraction contract is relationship-only for now.

## Decision 4 — evidence stays inline in raw LLM relationship candidates

The LLM is not responsible for deduplicating shared evidence or creating evidence references.

If the same sentence supports two edges, it may appear twice in the raw extraction.

Example:

```text
Alice Chen parent_of Bob Chen
evidence = same parent sentence

David Chen parent_of Bob Chen
evidence = same parent sentence
```

Deterministic normalisation can later detect the identical supporting text and create one first-class evidence object referenced by both relationships.

This deliberately chooses the easiest semantic contract for the LLM rather than forcing the raw LLM output to mirror the final graph representation.

## Decision 5 — deterministic entity typing follows relationship semantics

For Case 01, entity types can be inferred from the six supported relationship primitives:

```text
parent_of       person -> person
sibling_of      person -> person
spouse_of       person -> person

settlor_of      person -> trust
trustee_of      person -> trust
beneficiary_of  person -> trust
```

Therefore the LLM does not need to separately classify endpoint types.

This also creates a deterministic consistency check.

If the same name is implied to be both a person and a trust by different relationship candidates, validation can report an entity-type conflict.

## Decision 6 — Case 01 runtime entity lookup can be keyed by canonical name

During normalisation, a keyed lookup by canonical name is sufficient for Case 01:

```text
"Alice Chen" -> Entity(...)
"Bob Chen" -> Entity(...)
"Evergreen Family Trust" -> Entity(...)
```

This supports:

- quick "already seen?" checks;
- entity deduplication;
- accumulating inferred types;
- deterministic conflict detection.

Important boundary:

> A raw/canonical name is only a safe lookup key because aliases/entity resolution are explicitly deferred.

Later, `Alice Chen`, `Alice`, `Mrs Chen`, etc. may require resolution to one stable identity.

## Decision 7 — final normalised graph objects remain deliberately lean

### Entity

```text
- id
- type
- name
```

No aliases, DOB, status, confidence or richer attributes are added in Case 01.

### Relationship

```text
- source
- type
- target
- evidence_ids
```

`source` and `target` refer to entity IDs.

No relationship ID is required yet because nothing in Case 01 needs to address a relationship as an independent object.

### Evidence

```text
- id
- document
- supporting_text
```

Evidence remains first-class in the final graph representation even though it is inline in raw LLM output.

## Decision 8 — expected extraction represents the raw semantic LLM handoff

The earlier draft expected extraction was rewritten.

It no longer represents:

```text
Entity[] + Evidence[] + Relationship[]
```

Instead it represents the expected **raw semantic extraction**:

```text
RelationshipCandidate[]
```

This gives the project a clearer multi-stage contract:

```text
source.txt
    ↓
LLM semantic extraction
    ↓
RelationshipCandidate[]
    ↓
deterministic validation / normalisation
    ↓
Entity[] + Relationship[] + Evidence[]
    ↓
evaluation against ground_truth.json
```

## Deterministic work currently anticipated

After raw extraction, deterministic code is expected to own:

1. relationship-type validation;
2. checking that supporting text occurs in the source;
3. deriving unique endpoint entities;
4. inferring entity type from relationship semantics;
5. detecting type conflicts;
6. canonicalising symmetric relationships where required;
7. deduplicating relationships;
8. deduplicating identical evidence;
9. assigning stable internal IDs;
10. building the final graph representation.

This is a design target, not permission to pre-build every stage immediately. The first implementation should still be the smallest extraction slice, and additional validation/normalisation should be introduced incrementally.

## Open point discovered but not yet resolved

The expected extraction currently uses the source sentence:

> "She confirmed that she is the settlor of the Evergreen Family Trust."

That text is verbatim, but the pronoun requires the immediately preceding sentence to identify Alice Chen.

This raises a later evidence-span question:

> Is a minimal supporting quote allowed to rely on local surrounding context, or should every evidence span independently identify all relationship endpoints?

Do not expand scope to solve this before the first model run unless it blocks the contract.

## Evidence boundary

### Strong learner-owned reasoning

The learner:

- immediately rejected LLM-generated IDs as deterministic bookkeeping;
- repeatedly pushed to maximise deterministic work;
- challenged whether separate LLM entity extraction was justified;
- identified the receipts analogy: probabilistic extraction followed by deterministic validation;
- accepted relationship-only extraction after reasoning through the evaluation trade-off;
- correctly treated IDs as implementation handles rather than semantic evaluation targets;
- preferred a keyed entity lookup for deterministic normalisation.

### Guided / externally checked

The tutor initially moved between separate LLM entity extraction and deterministic entity derivation as the trade-off became clearer.

A deliberately neutral third-agent review was requested to break the tie. It independently recommended relationship-only extraction for Case 01 and supplied a useful future trigger: introduce entity extraction when entity information matters without a supported edge.

This is useful reflection evidence because the final decision was reached through challenge and comparison rather than accepting the tutor's first proposal.

## Next step

The semantic extraction contract is now sufficiently frozen to implement the first model call.

Start with:

```text
source.txt
    ↓
structured LLM extraction
    ↓
RelationshipCandidate[]
```

Do not add retries, routing, reflection, RAG or sophisticated normalisation before observing the first real extraction.
