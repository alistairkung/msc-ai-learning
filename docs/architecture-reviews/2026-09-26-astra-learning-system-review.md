# Architectural Review: `msc-ai-learning`

**Review date:** 2026-09-26  
**Repository snapshot reviewed:** around commit `e0297c5`  
**Status:** Historical architecture-review snapshot; recommendations are not automatically current architecture.

> Preserved copy of Astra's read-only architectural review. No repository changes were made as part of the analysis.

## Executive conclusion

**Keep GitHub, Markdown and YAML as the foundation. Don't deploy a vector database yet. Do make the system easier to query—and harder to misinterpret.**

The recommended direction is:

> **Clearer ownership of current state → smaller, purpose-built context → more explicit learning evidence → benchmarked retrieval.**

A vector layer could eventually help recover old explanations, recurring mistakes and cross-topic connections. The concrete problems today, however, are conflicting temporal state and maintenance overhead rather than insufficient storage or semantic search.

A semantic-retrieval prototype could still be educational before it becomes operationally necessary. The working tutor should not depend on it until it proves useful.

## Current architecture

The repository is already a hybrid learning system rather than a collection of notes:

```text
Live MSc work
    ↓
course demand / roadmap / deadlines
    ↓
study session
    ↓
exercises + tests + lesson logs
    ↓
LEARNING_STATE.md
    ↓
reviewed learning_progress.yaml
    ↓
Learning Atlas

ARCHITECTURE.md + SESSION_WORKFLOW.md govern the process.
Git/PR/CI provide provenance and mechanical validation.
```

The intended separation is strong:

- focused logs and artifacts = learning evidence;
- `LEARNING_STATE.md` = current operational handover;
- syllabus map = near-term course demand;
- roadmap = longer-term strategy;
- `learning_progress.yaml` = reviewed structured projection;
- `deadlines.yaml` = delivery constraints, deliberately separate from mastery;
- Learning Atlas = presentation, not authority.

Git should remain both the persistence mechanism and the history of how the learning system itself evolves.

## What is working especially well

### Evidence boundaries

The system distinguishes independent performance, guided work, historical learning, same-session transfer, exposure and future material. It avoids collapsing these into a single mastery percentage.

That is one of the most valuable properties of the architecture and should survive any future database or retrieval migration.

### Diagnostic learning records

Logs often preserve *why* an error occurred. For example, a PyTorch weight-storage orientation error is distinguished from misunderstanding linear layers. Algebra slips are distinguished from calculus misunderstanding.

That lets a future tutor repair the actual weakness rather than reteaching an entire topic.

### Productive struggle

The tutoring protocol favours cold recall, changed examples, incremental hints and learner-owned implementation. Supplied solutions do not automatically become evidence of independent mastery.

### Transfer evidence

The Receipts work records architecture and system-design decisions separately from repetitive code delegated to AI. It also records when real data disproved an assumed invariant. This is useful evidence of engineering transfer rather than simply “project completed.”

## Problems visible today

### Current and superseded instructions coexist

Historical plans sometimes remain beside newer operational instructions. A model can often infer which is current, but it should not have to reconstruct temporal authority repeatedly.

Explicitly distinguish:

- current instruction;
- historical evidence;
- superseded plan.

### Discovery is beginning to drift

The manually maintained lesson index is older than several substantive later logs. This is an early sign that navigation should become more deterministic.

Generate inventories/manifests where possible before adding semantic search.

### Synchronisation is becoming real work

Recent history already contains reconciliation of divergent learning-state changes. Automate mechanical work such as source hashes, reference checks, affected-file discovery and rendering before automating pedagogical judgment.

### Fresh source does not mean correct interpretation

A source hash proves which version was reviewed. It does not prove that a learning claim is semantically justified by the evidence.

A vector database would not solve this.

### CI/dashboard dependency gap

The dashboard consumes `deadlines.yaml`, but the reviewed dashboard workflow did not list it among its path triggers. Review all dashboard inputs against CI/deployment triggers.

### Tests mix invariants and changing facts

Separate permanent rules about valid learning state from assertions about today's particular deadlines, submissions and topic statuses. Use fixtures for generic rendering/schema tests while retaining deliberate evidence regressions.

## Target direction

Do not replace the storage foundation. Move gradually toward:

```text
Git-backed canonical sources
        ↓
narrative evidence + structured observations
        ↓
reviewed judgments/current decisions
        ↓
deterministic validation
        ↓
small current-context views
+ structured queries
+ optional search indexes
        ↓
AI tutor
```

The important boundary is **observation vs judgment**, not Markdown vs database.

For meaningful assessment moments, consider structured observations containing:

- stable event ID;
- topic;
- event date and record date;
- task reference;
- retrieval/guided/recognition/transfer mode;
- support received;
- result/error;
- provenance;
- correction or supersedes relationship.

Do not automatically turn these into numeric mastery scores.

Also separate event time, record time, latest assessment and latest retrieval. Historical backfills particularly need this.

## Knowledge graph

You already have a graph through topic IDs and `depends_on`.

Extend that rather than creating a graph database.

Useful tutor behaviours include:

- checking relevant tensor prerequisites before CNN work;
- finding a weak prerequisite that unlocks several upcoming topics;
- identifying a misconception recurring in another domain.

Keep strict prerequisites separate from softer “related to” relationships, and do not turn prerequisites into gates that prevent useful new learning.

## Vector database assessment

### Embeddings and a vector DB are separate decisions

Test semantic retrieval locally before choosing database infrastructure.

The first question is:

> **Does semantic retrieval find better evidence for real tutoring questions?**

Only after that ask how to persist and serve the index.

### Use different retrieval mechanisms for different questions

| Query | Best first mechanism |
|---|---|
| What should I study next? | Explicit current state |
| Is an assignment submitted? | Structured deadline state |
| What depends on gradients? | Prerequisite graph |
| Last three broadcasting attempts? | Structured events/date query |
| Where did I make a similar conceptual mistake? | Lexical + semantic retrieval |
| Find a related engineering analogy | Semantic retrieval |
| What does this function do? | Code search/direct source |

Vector similarity should never determine which version of a fact is current.

### Retrieval options

| Option | Recommendation |
|---|---|
| Direct file/section loading | Keep |
| Text search + generated manifest | Improve now |
| YAML/JSON filtering | Use more |
| SQLite/FTS | Add when repeated structured/text queries justify it |
| Existing prerequisite graph | Reuse |
| Local embedding search | Good experiment |
| Hybrid lexical + semantic | Benchmark |
| Managed vector DB | Wait for demonstrated operational need |

### What to embed

Start with selected semantic sections of lesson logs: attempts, misconceptions, useful explanations, evidence boundaries and reflections.

Do not indiscriminately embed every roadmap/state summary; that creates duplicated facts with different temporal meanings.

Attach metadata including topic, course, event date, provenance, source path/hash, repository revision and whether the chunk is evidence, policy, current decision or superseded instruction.

### Never vector-only

Keep current priorities, deadlines, learner identity, teaching constraints, reviewed assessment state and provenance canonical and directly inspectable.

## Context/token/credit economics

Reducing context is useful, but the economic effect depends on product surface.

- In ordinary Chat, allowances may be message/model based rather than a simple token bucket. Smaller context can still improve latency, relevance and useful work per interaction.
- In Work/Codex/agentic workflows, context, model, reasoning, tools and caching can affect consumption more directly.
- A custom API tutor introduces separate API billing; moving the tutor there can increase direct monetary cost even if it is token-efficient.

Illustrative repository bootstrap sizes from the review:

| Material loaded fully | Source bytes | Rough token heuristic |
|---|---:|---:|
| Workflow + handover | 45,066 | ~11.3k |
| + architecture | 62,937 | ~15.7k |
| Eight root Markdown docs | 136,188 | ~34k |

These are rough bytes/4 illustrations, not tokenizer measurements, and the architecture already recommends lazy loading.

The important point is:

> **Storing structured state is cheap. Repeatedly feeding irrelevant structured state to the model is the problem.**

Retrieval itself also costs embedding, search/tool calls, model processing, maintenance and study time. Measure three budgets separately:

1. product allowance;
2. money;
3. study time.

## Make retrieval improve learning

The ideal retrieval layer should help the tutor choose a better *new question*, not reveal the learner's old answer.

```text
retrieve old misconception
    ↓
check latest evidence
    ↓
construct changed problem
    ↓
ask learner
```

Useful additions to test:

- record assistance level, not only correctness;
- use delayed transfer checks;
- occasionally ask the learner to predict an outcome and confidence before evaluation.

None requires a vector DB.

A semantic-retrieval prototype can itself be an MSc learning project:

```text
lexical baseline
→ embedding similarity
→ retrieval evaluation
→ metadata filtering
→ stale/contradictory evidence tests
→ decide whether complexity earns its place
```

This teaches vectors, similarity, ranking, evaluation, provenance and deterministic-vs-probabilistic boundaries. Keep it experimental and ensure the normal tutor works without it.

## Scaling warning signs

| Horizon | Pressure to watch |
|---|---|
| Next 6 months | Repeatedly correcting tutor about what is current |
| ~1 year | Historical questions require scanning many narratives |
| MSc completion | Hard to compare performance because tasks/scaffolding changed |
| Multiple learners/agents | Concurrent updates overwrite or contaminate state |

The first likely failures are about authority and data modelling, not raw storage.

## Staged roadmap

### DO NOW

- Make current state unambiguous and mark superseded plans.
- Keep routine bootstrap/context smaller.
- Generate discovery/inventory information where possible.
- Fix dashboard dependency triggers.
- Separate permanent test invariants from mutable learner facts.
- Measure what context sessions actually use.

### WAIT FOR A TRIGGER

| Change | Trigger |
|---|---|
| Structured observations | Attempt-level history becomes hard to recover from prose |
| Context builder | Context selection repeatedly wastes time/tokens |
| SQLite/FTS | Repeated filtering/date/text queries emerge |
| Embeddings | Lexical/metadata retrieval misses useful semantic evidence |
| Retrieval tool | Manual context transfer becomes the bottleneck |
| Managed vector DB | Local approach fails measured access/concurrency needs |
| Generic tutor framework | A second learner actually uses the system |

### PROBABLY UNNECESSARY NOW

- graph database;
- production multi-agent tutor;
- embedding every Git revision;
- automatic mastery percentages;
- moving ordinary tutoring wholesale to a custom API application.

## Five experiments

### 1. Clean-room resumption

Give a fresh tutor a compact context and ask it to identify the correct current lane and first question. Compare with the existing bootstrap.

### 2. Retrieval benchmark

Create ~20 representative questions with manually identified relevant and misleading evidence. Compare direct lookup, lexical search and embeddings using the same context budget.

### 3. Structured-observation pilot

For a few topics, record meaningful attempts and support received for several weeks. See whether this improves subsequent teaching decisions enough to justify the bookkeeping.

### 4. Synchronisation regression

Simulate two sessions updating different topics from the same starting state. Test preservation, duplicate handling and invalid transitions.

### 5. Economics + learning comparison

Compare similar sessions using broad vs targeted context. Measure available usage data, latency, tool/read count, corrective turns and maintenance time, then perform a later unaided learning check.

Success means lower friction/cost **without worse retention, transfer or independence**.

## Reusability

A reusable tutor framework remains plausible, but extraction should follow real use.

Most reusable:

- teaching protocol;
- evidence model;
- validation;
- context selection.

Learner-specific:

- curriculum choices;
- active priorities;
- learning history.

Do not prematurely generalise until a second learner exposes which abstractions are genuinely reusable.

## Remaining uncertainty

The review did not directly measure routine token usage, cache-hit rates, exact account allowances, retrieval accuracy or maintenance time. It reviewed representative code rather than every exercise. Some historical records are reconstructed or learner-reported.

Those uncertainties are why benchmarking should precede infrastructure changes.

## Final decision

**Keep the current tutor working. Make current state cleaner. Give it a small deterministic way to retrieve the right records. Then test semantic search on the questions the simpler mechanisms handle badly.**

The most important success measure is not how much the tutor remembers about the learner. It is whether that memory helps the learner become more capable **without the tutor**.

A particularly good next project is:

> **Prove that the tutor can receive less context while preserving—or improving—the quality of its next teaching decision.**
