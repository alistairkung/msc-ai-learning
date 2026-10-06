# FTEC5660 — Private Client Graph data-modelling reflection, 6 Oct 2026

## Why this record exists

This records a design discussion prompted by the benchmark growing from single-document Case 01 into Cases 02–04. It is preserved as evidence of how the learner approached a data-modelling problem: starting from concrete benchmark pressure, identifying the domain relationships that had emerged, comparing persistence options, and extracting a durable architectural principle rather than jumping directly to a schema rewrite.

This is architecture/reasoning evidence, not evidence of independent SQL implementation mastery.

## Trigger: Case 04 changed the shape of provenance

Case 04 introduced two source documents that can assert the same semantic relationship. That exposed a distinction which was mostly invisible in Case 01:

```text
relationship
    !=
individual assertion / evidence for that relationship
```

For example, two separate attendance notes may both support:

```text
Andrew Chan --beneficiary_of--> Hillcrest Family Trust
```

The canonical Matter state should contain one relationship, while retaining each supporting passage and its source provenance.

The emerging domain relationships were therefore reasoned about as:

```text
Matter 1 ---- * Source
Source 1 ---- * Evidence

Canonical Matter state
    ---- * Entity
    ---- * Relationship

Relationship * ---- * Evidence
```

Evidence belongs to one Source: the same words appearing in two documents are two distinct pieces of provenance. A Relationship may have many Evidence items, and one Evidence passage may support multiple Relationships.

## Existing simplifying assumption

The current practitioner persistence model stores one complete Matter per row, including one Authoritative Source and a serialized `current_graph` JSONB value.

The deterministic graph builder already does useful canonical work:

- derives entities from relationship endpoints;
- deduplicates semantic edges by source/type/target;
- accumulates multiple evidence IDs onto one relationship;
- returns a `CanonicalGraph` domain object.

This was an appropriate Case 01 simplification. Case 04 puts pressure on the single-source boundary and makes Source/Evidence identity and referential integrity more important.

## Options considered

### Continue with a richer JSONB representation

The existing serialized graph could be expanded to contain multiple Sources and source-aware Evidence. This remains simple and is adequate if the application always treats the graph as one opaque aggregate.

### Relationalise only Source/Evidence

A hybrid could make Sources and Evidence first-class relational records while leaving Entities/Relationships inside the JSONB graph. This improves provenance handling but leaves part of the canonical Matter state authoritative only inside the serialized representation.

### Persist canonical domain facts relationally

The stronger option is for PostgreSQL to persist the canonical facts and their relationships directly: Matters, Sources, Evidence, Entities, Relationships, and the Relationship/Evidence association.

This allows database constraints to participate in protecting invariants such as:

- Evidence references an existing Source;
- relationship endpoints reference existing Entities;
- relationship/evidence links reference existing records;
- one semantic relationship is not duplicated merely because several Sources support it.

The exact physical schema remains deliberately unresolved. The discussion did not conclude that every domain noun deserves a table or that `CanonicalGraph` needs its own persisted identity.

## Key modelling distinction: CanonicalGraph is a representation

The most useful conclusion was:

> PostgreSQL should contain enough canonical Matter state to reconstruct how the Matter stands. `CanonicalGraph` is the deterministic representation currently used to present that state, not necessarily an independently persisted source of truth.

Conceptually:

```text
canonical persisted Matter facts
            |
            v
deterministic construction
            |
            v
CanonicalGraph
            |
            v
review / presentation
```

This keeps the database capable of serving as the canonical source of truth without confusing a useful domain representation with independent persisted identity.

A future requirement could still earn first-class graph identity, for example graph versioning, historical accepted graphs, promotion/supersession semantics, or an independent graph lifecycle. None is required merely because the application has a `CanonicalGraph` class.

## Reasoning pattern worth retaining

The discussion followed a useful sequence:

1. Start from a concrete benchmark case rather than a speculative future architecture.
2. Identify what new invariant the case exposes.
3. Separate domain facts from representations of those facts.
4. Compare the smallest persistence options rather than assuming full normalisation.
5. Ask which facts the database itself should be able to protect and reconstruct.
6. Give independent persistence identity only when lifecycle/invariants earn it.
7. Record the principle before implementing the schema change.

This also corrected an initially attractive hybrid design. The learner challenged whether leaving the canonical graph facts authoritative only inside JSONB was consistent with the database being the canonical source of truth. That challenge shifted the preferred direction toward relational canonical facts while still resisting a premature table-per-noun design.

## Interview-ready example

A concise future interview framing:

> A benchmark case introduced multiple documents supporting the same semantic relationship. I used that concrete failure pressure to revisit a deliberately simple JSONB persistence model. We separated Source, Evidence, Entity and Relationship as canonical facts, recognised that one relationship can have evidence from multiple sources, and then asked whether the rendered CanonicalGraph was itself state or just a projection. I argued that PostgreSQL should contain enough canonical facts to deterministically reconstruct the Matter, with the graph treated as a presentation/domain projection unless it later earns its own lifecycle. That let us strengthen referential integrity without prematurely creating a graph-version entity or normalising every noun.

Useful follow-up discussion points:

- why the Case 01 JSONB design was reasonable at the time;
- why Case 04 changed the trade-off;
- relationship identity versus evidence/assertion identity;
- many-to-many Relationship/Evidence support;
- why Evidence belongs to exactly one Source;
- database-enforced referential integrity versus application-only validation;
- domain concept versus persisted entity;
- architecture being earned by benchmark failures.

## Evidence boundary

This was a learner-led architecture discussion with AI used as a reasoning partner and critic. The strongest evidence is in identifying ownership, canonical-state and persistence boundaries and challenging an initially proposed hybrid. It should not be represented as independent implementation evidence: no relational migration or repository implementation was completed in this learning record.

The corresponding Private Client Graph repository records the architectural guardrail separately: PostgreSQL owns canonical Matter facts, while derived representations such as `CanonicalGraph` must not contain authoritative facts that exist nowhere else in canonical persistence.
