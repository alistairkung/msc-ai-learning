# FTEC5660 — Private Client Graph benchmark design session, 29 Sep 2026

## Session purpose

A focused ~90-minute hackathon build/learning session for **Private Client Graph**. The session deliberately stopped before LangChain implementation and instead defined the smallest credible happy-path benchmark case.

The working spike remains:

> Can GenAI reconstruct a synthetic family/trust relationship graph from source documents while preserving provenance and uncertainty, and can the reconstruction be evaluated against hidden ground truth?

The architecture remains a hypothesis. Complexity should be earned by observed failures.

## Transfer from receipts homework

The session explicitly reused the design discipline learned from the completed receipts homework:

```text
probabilistic interpretation
    ↓
structured contract
    ↓
deterministic validation / normalisation
    ↓
deterministic processing
    ↓
evaluation
```

The learner repeatedly applied the same boundary in a new domain:

- avoid asking an LLM to emit redundant information that deterministic code can derive;
- define canonical structured handoffs before implementation;
- separate hidden truth from source evidence and justified extraction;
- require provenance rather than trusting structurally valid output;
- defer aliases, uncertainty machinery and agentic stages until a case exposes the need;
- build one narrow vertical slice before implementing the pipeline.

This is meaningful changed-domain design transfer, but it is still same-session guided design work rather than delayed independent reconstruction of the whole architecture.

## Relationship model

The learner reasoned toward a canonical edge model:

```text
source entity -- relationship type --> target entity
```

Case 01 freezes six initial primitives:

### Family

- `parent_of` — directed;
- `sibling_of` — symmetric;
- `spouse_of` — symmetric.

### Trust

- `settlor_of`;
- `trustee_of`;
- `beneficiary_of`.

Important decisions:

- store `parent_of`, not a redundant inverse `child_of`;
- store symmetric relationships once and let deterministic evaluation/normalisation ignore endpoint ordering where appropriate;
- do not invent `aunt_of`, `niece_of`, `cousin_of`, etc. merely to mirror every kinship word;
- do not manufacture unknown intermediate people/edges to explain a stated kinship label;
- keep the relationship representation extensible so later domain evidence can justify new primitives without redesigning what an edge is.

A useful boundary emerged: a primitive may still be worth storing when a source can state it directly without enough structure to derive it. This is why `sibling_of` remains useful even though siblings can sometimes be derived from shared parents.

## Entity and identity model

Case 01 uses two entity types:

- `person`;
- `trust`.

Minimum entity information:

- stable ID;
- type;
- canonical name.

Relationships attach to stable identities rather than literal mention strings. Alias/entity resolution is deliberately deferred; Case 01 makes identity trivial with consistent names.

Ground-truth IDs and extracted IDs are independent. Hidden IDs must not leak into the extraction pipeline.

The session also distinguished:

> mentioned in a document ≠ necessarily belongs in the relationship graph

Incidental named people are deferred from Case 01 rather than introducing relevance filtering immediately.

## Provenance model

Provenance is part of the benchmark hypothesis, not incidental metadata.

Decisions:

- every extracted edge requires provenance;
- provenance uses exact supporting source text, not an LLM-generated justification;
- evidence is a first-class object with stable identity;
- relationships reference evidence IDs;
- evidence does not duplicate reverse relationship references;
- one evidence item may support multiple relationships;
- one relationship may later have multiple evidence items;
- a perfect extraction needs at least one sufficient supporting passage per relationship, not every repeated mention.

This creates a deterministic validation opportunity later: verify that claimed supporting text actually occurs in the source.

## Ground truth / evidence boundary

The session refined the meaning of the three benchmark artifacts:

```text
ground_truth.json
    = answer key for the graph task

source.txt
    = documentary evidence presented to the extractor

expected_extraction.json
    = what a perfect extractor is justified in returning
```

Ground truth is not an exhaustive database of every true proposition in the fictional meeting. It must be complete for the graph task being evaluated.

This matters for precision/recall: any true relationship within the supported Case 01 relationship types must appear in the answer key, while graph-neutral facts such as meeting duration or process can appear in the source without becoming graph truth.

## Case 01 fictional graph

Entities:

- Alice Chen;
- David Chen;
- Bob Chen;
- Carol Wong;
- Evergreen Family Trust.

Answer-key relationships:

1. Alice Chen `settlor_of` Evergreen Family Trust.
2. Alice Chen `spouse_of` David Chen.
3. Alice Chen `parent_of` Bob Chen.
4. David Chen `parent_of` Bob Chen.
5. Bob Chen `beneficiary_of` Evergreen Family Trust.
6. Carol Wong `beneficiary_of` Evergreen Family Trust.

No family relationship is asserted for Carol Wong.

## Synthetic source design

An initial generated attendance note was rejected as unrealistically short after external lawyer feedback that a substantive one-hour meeting note could plausibly run several pages.

A domain-consultation pass then established a safer source-authoring pattern:

- use an approximately one-hour initial fact-finding/review meeting;
- create realistic bulk through purpose, scope, questioning, clarification, explanation, recap and next steps;
- avoid creating length through extra family members, trust roles, assets, distributions, tax facts or ownership/control;
- audit every durable fact for whether it accidentally changes the graph answer key.

The revised attendance note is roughly a 2–3 page style document with the six graph relationships embedded in graph-neutral professional prose. It was manually checked for answer-key integrity and evidence coverage.

## Artifacts produced in the hackathon repository

The separate `private-client-graph` repository now contains/has proposed:

- Case 01 `ground_truth.json`;
- reviewed Case 01 attendance-note `source.txt`;
- a draft proposal for `expected_extraction.json`;
- design notes covering relationship primitives, identity/provenance and the answer-key boundary;
- a reusable synthetic-case authoring workflow.

The expected-extraction PR is intentionally a proposal for the next session rather than a settled schema.

## Evidence boundary

### Strong same-session evidence

The learner independently or with light challenge:

- identified that one canonical `parent_of` edge is sufficient rather than storing `child_of` too;
- preferred one symmetric spouse edge and deterministic handling of reversed endpoints;
- recognised that trust roles belong on edges rather than as person attributes;
- argued for stable entity identities rather than name strings;
- proposed evidence as a first-class object that can be shared by multiple edges;
- preferred relationship -> evidence references to duplicated bidirectional state;
- noticed that defining ground truth as only target graph facts affects evaluation semantics;
- repeatedly pushed for extensibility without pre-building the full domain model.

### Guided/new material

Domain vocabulary such as settlor/trustee/beneficiary required explanation. The distinction between structural primitives and unsupported kinship labels, benchmark source-generation safeguards, and the precise evaluation boundary were developed interactively with tutor/domain-agent guidance.

Do not treat this as trust-law expertise or as independent mastery of a private-client ontology.

## Deferred

Case 01 still explicitly defers:

- entity resolution / aliases;
- contradictory documents;
- uncertain or historical relationships;
- multiple-document merging;
- sophisticated trust-law edge cases;
- RAG;
- routing/reflection/verifier agents;
- Neo4j;
- production infrastructure;
- polished UI.

No confidence/status field is added merely because uncertainty will matter later.

## Next useful step

Start the next hackathon session by reviewing the draft `expected_extraction.json` proposal.

Resolve only the contract questions needed for Case 01, especially:

- exact field naming;
- evidence span convention;
- whether relationships need IDs;
- which IDs/references the LLM should emit versus deterministic code assigning them.

Then freeze the three Case 01 fixtures and implement the smallest structured extraction attempt. Do not add LangChain stages beyond what the first observed extraction failures justify.
