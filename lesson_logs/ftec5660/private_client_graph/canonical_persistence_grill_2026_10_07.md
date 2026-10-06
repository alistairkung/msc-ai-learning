# Private Client Graph — canonical persistence architecture boundary

_Status: proposed architecture boundary from the 6–7 Oct 2026 design grill. No implementation or migration is authorised by this learning record._

## Purpose and scope

Replace serialized graph authority with relational canonical facts protected by database-enforced integrity, for both Matter Proposals and accepted Matters. Provenance integrity and aggregate isolation are domain requirements independent of stochastic extraction performance. `CanonicalGraph` remains a deterministically reconstructed domain/presentation representation with no separately persisted identity or lifecycle.

The deterministic substrate must support multiple explicitly identified Sources. Prove this with controlled fixtures supplying Entity identity; do not introduce multi-document practitioner intake, extraction orchestration, or entity resolution. Preserve existing single-source practitioner journeys. Establish Case 01 equivalence and the controlled multi-source persistence baseline before subsequent extraction experiments.

## Canonical facts and cardinality

Each Matter owns its Sources, Entities, Relationships, and their provenance. Each Matter Proposal owns a separate proposed set with the same structural guarantees.

- **Source:** explicit identity within its owner; stores finalized text and title. Matching titles/text do not imply identity or corroboration.
- **Entity:** Matter/Proposal-local identity independent of name; retains type and exact name. Duplicate names are valid.
- **Evidence:** belongs to exactly one Source; identity for this slice is Source + exact quote text, not occurrence/span. One Evidence item may support multiple Relationships.
- **Relationship:** connects two existing Entities under the same owner; semantic identity is endpoint identities + supported relationship type. Symmetric types ignore endpoint order; directed types preserve it. Every persisted Relationship has one or more Evidence associations.
- **Support association:** connects one Relationship to one Evidence item under the same owner, once per pair.

Persist enough facts/reference metadata to reconstruct the reviewed graph exactly. Preserve Source text/titles even for an empty graph. Graph-local IDs need not be DB primary keys. Source attribution resolves through identity, not display title.

## Deferred — entity-resolution/extraction design

Exact-name grouping is not a permanent semantic identity rule. A later Case 03-driven review must evaluate entity resolution in both directions:

- different surface forms referring to one real-world entity should merge correctly;
- identical names referring to different real-world entities should remain distinct.

Persistence must support both outcomes. The controlled multi-source persistence fixture supplies explicit Entity identities and does not test entity resolution. Benchmark correctness of model-proposed identity and practitioner confirmation of proposed identity are separate future questions.

## Reviewed graph preservation

Persistence round trips and confirmation preserve the reviewed graph's observable Entity/Evidence IDs, list ordering, values and associations. Internal DB keys may differ, but reconstruction must not renumber observable references, regroup Entities by name, or reorder the reviewed graph.

## Canonical integrity requirements

Canonical persistence must protect structural and referential invariants through PostgreSQL constraints wherever they naturally express the rule; application validation complements rather than replaces those guarantees. The same structural guarantees apply to durable Matter Proposals and accepted Matters.

- **Provenance integrity:** every Evidence item resolves to its Source, and every Relationship–Evidence association resolves at both ends without duplicate associations.
- **Aggregate isolation:** related Sources, Evidence, Entities and Relationships belong to the same Matter or the same Matter Proposal.
- **Provenance completeness:** every committed Relationship has at least one supporting Evidence association. Empty graphs remain valid.
- **Verbatim provenance:** each Evidence quote occurs exactly in its referenced Source's finalized text. Whether it semantically supports a Relationship remains outside this guarantee.

Database rejection tests must cover dangling references, duplicate support associations, cross-aggregate references, zero-support Relationships, removal of final support while retaining a Relationship, non-verbatim Evidence, provenance-field mutation, duplicate canonical edges and reversed symmetric duplicates.

## Ownership and Proposal/Matter boundary

Repeat aggregate ownership scope where necessary for ordinary composite FKs to enforce isolation. Repeated scope values are constrained to agree rather than independently asserting ownership.

Use separate proposal-owned and Matter-owned persistence structures with equivalent structural guarantees and real FKs to their aggregate roots. Structural similarity does not collapse their distinct semantics: Proposal is machine-proposed durable review state; Matter is professionally accepted canonical state.

Proposal creation atomically persists its complete proposed facts and external-reference claim. Whole-proposal discard removes its owned facts/claim atomically.

Confirmation locks/reloads the Proposal, validates reviewed state, allocates Matter identity, copies all reviewed facts and associations unchanged into Matter-owned records, transfers the external-reference claim, and consumes the Proposal/children in one transaction. No extraction, name-based reconstruction or new identity resolution occurs during confirmation. Rollback leaves Proposal intact and no partial Matter.

## Provenance immutability and deletion boundary

Persisted Source finalized text and Evidence Source/quote are immutable in this slice. Validate verbatim quote occurrence on Evidence creation. Whole-aggregate deletion remains possible.

No individual Source/Evidence deletion product operation is introduced. Future design must decide what removing final support means. Candidate future semantics include rejecting deletion, atomically removing now-unsubstantiated Relationships, or introducing a separately modelled practitioner-asserted/unsubstantiated relationship concept.

**Future hypothesis:** an unsubstantiated/practitioner-asserted relationship, if earned, should be semantically explicit rather than represented by weakening the current invariant and accidentally allowing ordinary Relationships to have zero Evidence.

For now: persisted Relationship -> at least one Evidence.

## Migration boundary

A brief maintenance window and coordinated cutover are acceptable. Pause access/writes, validate and decompose persisted Matters and pending Proposals, verify exact reconstruction, activate the new application, and remove legacy authoritative graph storage without permanent dual writes.

Migration uses persisted state rather than regenerated fixtures and aborts on invalid state rather than silently repairing it. Use new Alembic migrations; never rewrite applied history.

## Regression and acceptance

- Case 01 follows its existing deterministic construction policy, then new persistence/reconstruction, and remains observationally equivalent including full evaluation output.
- Controlled multi-source fixture uses explicit Entity identities: one semantic Relationship supported by two Sources reconstructs once with both provenance items.
- Identical quotes in different Sources remain distinct; repeated identical quotes in one Source share Evidence; shared Evidence may support multiple Relationships.
- Distinct same-name Entities remain distinct; explicitly shared Entity references remain shared.
- Direct invalid DB writes are rejected for both Proposal and Matter storage families.
- Exercise successful/failed proposal creation, unchanged confirmation, discard, concurrent terminal actions, rollback, empty graphs and Evergreen idempotence.
- Test relevant concurrent bypassing writes and migration exact reconstruction.
- Existing practitioner API/browser journeys remain protected.

## Non-goals

No new extraction/evaluation contracts; alias/homonym resolution; individual Source/Evidence deletion workflow; relationship editing/partial confirmation; practitioner-asserted relationships; temporal state; contradictions; supersession; confidence; audit/history; graph versions; graph databases; organisation Entities; document integrations; queues; event sourcing; CQRS; or permanent JSONB/relational dual authority.

## Reasoning evidence

The final design was reached through an adversarial architecture grill rather than by asking an agent to justify a preferred schema.

The learner entered with a preference for relational canonical persistence. The grill challenged the initial justification: PostgreSQL JSONB can itself be authoritative, Case 02 does not require relational persistence, and the current Case 04 fixture does not actually evaluate source-qualified provenance.

The learner then articulated the stronger requirement behind the preference from prior production experience: a canonical datastore should not merely hold authoritative bytes; it should protect structural/referential invariants naturally expressible by the datastore so persisted state remains trustworthy even if an application path, migration or operational write bypasses normal validation.

That requirement was repeatedly challenged and refined into concrete domain invariants:

- provenance integrity and provenance completeness;
- Matter/Proposal aggregate isolation;
- Entity identity separate from name;
- Source-aware Evidence identity;
- Proposal and Matter as distinct domain states with equivalent integrity guarantees rather than one abstraction chosen to eliminate structural duplication;
- `CanonicalGraph` as a deterministic representation rather than independently persisted truth.

The learner explicitly remained willing to abandon relationalisation if the stronger requirement could not justify it. The value of the grill was therefore not agreement with the initial preference, but forcing an engineering intuition to reveal testable requirements and survive adversarial review.

## Evidence boundary

This is strong learner-led architecture/data-modelling judgement with AI acting as an adversarial reasoning partner. It is not independent SQL/PostgreSQL implementation evidence. Enforcement mechanisms, migrations and code remain unimplemented and should not be recorded as mastered implementation skills.
