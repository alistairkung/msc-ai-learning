# FTEC5660 — Agentic AI in Finance / FinTech — Course Context

_Last updated: 2026-09-08_

## Purpose

This is the durable course-level context for FTEC5660. It exists so a future tutor/model can recover not only **what the course is teaching**, but also **how I am interpreting it through prior software-engineering and cross-border-payments experience**.

Use this file together with the individual FTEC5660 lecture logs. Do not treat personal synthesis below as lecturer-authored course content.

---

## Source boundaries

### Directly supported by Lecture 1 slides

The course frames agentic AI as systems that can pursue goals, perceive context, reason/plan, act through tools, and learn/escalate with limited supervision. The lecture emphasises reusable agentic design patterns because multi-step agent behaviour introduces state, tool choice, error recovery and coordination problems.

Lecture 1 showed a catalogue of **21 named agentic design patterns as an introductory overview of what the course will cover later**:

1. Prompt chaining
2. Routing
3. Parallelization
4. Planning
5. Goal Setting and Monitoring
6. Tool Use (Function Calling)
7. Model Context Protocol
8. Memory Management
9. Knowledge Retrieval
10. Multi-Agent Collaboration
11. Inter-Agent Communication
12. Reflection
13. Learning and Adaptation
14. Reasoning
15. Exploration and Discovery
16. Exception Handling and Recovery
17. Human in the Loop
18. Resource Aware Optimization
19. Guardrails
20. Evaluation and Monitoring
21. Prioritization

The lecture groups these broadly into:

- orchestration patterns;
- enterprise knowledge and system-access patterns;
- multi-agent collaboration patterns;
- decision-intelligence patterns;
- governance, safety and operational-control patterns.

### Retrieval rule for the catalogue

The list above is a **course map/reference**, not a list the learner is expected to memorise from Lecture 1.

Do not ask for all patterns by name or number. Individual patterns become fair retrieval targets only after the course later teaches, discusses or applies them substantively. Retrieval should focus on explanation, recognition, distinction and application rather than catalogue enumeration.

Prompt Chaining is now the first exception to the overview-only state: it has been substantively taught and has its own focused retrieval/tutorial log at `lesson_logs/ftec5660/pattern01_prompt_chaining.md`. The course-level rule remains unchanged for the other patterns.

### Lecturer comments / learner recollection to verify

- The module has **two major project-style assessments**, described in class as a **hackathon** and a **final project**.
- I recall these accounting for **roughly 80% of the grade combined**, but the exact weighting should be verified against the official assessment specification before being treated as authoritative.

These are important planning constraints even while the exact percentage remains unverified.

---

## Personal learning lens

For each agentic pattern or workflow **once it is actually taught**, deliberately ask:

1. **What does the lecturer mean by the pattern?**
2. **What is the closest conventional software-engineering analogue, if any?**
3. **How would this appear in cross-border payments, KYC/onboarding or AML?**
4. **What genuinely becomes better by making this part agentic rather than deterministic?**
5. **What new failure mode, governance problem or verification burden does agenticity introduce?**

This is intended to make the course additive to existing engineering knowledge rather than a disconnected vocabulary exercise.

---

# Personal synthesis threads

These are **working hypotheses developed after Lecture 1**, not settled course conclusions. Revisit them as later lectures on tool use, planning, multi-agent systems, evaluation, safety and alignment provide stronger evidence.

## 1. Agentic patterns sit alongside traditional software-engineering patterns

Traditional patterns such as Factory, Strategy, Adapter, Observer and Command mainly structure software components and collaboration. The course's agentic patterns mainly structure **behaviour, decision-making and multi-step control flow**.

The useful question is not "which old pattern did agents replace?" but:

> What existing engineering concept is this related to, and what is genuinely new because an LLM can choose actions dynamically?

The underlying production software still has ordinary concerns such as state, idempotency, contracts, retries, consistency, observability and failure handling.

## 2. Agent autonomy should be expressed as decision rights

"Give the agent autonomy" should not mean "the agent may change anything it wants".

Useful distinction:

```text
reason / discover
    -> propose
    -> use approved capabilities autonomously
    -> escalate when a decision exceeds authority
```

Example: an engineering agent may independently decide that canarying, shadow traffic or blue/green deployment is appropriate, while introducing a new production dependency such as Istio may still require architecture/platform approval.

The important design question is:

> Where is the decision-rights boundary between human/organisation and agent?

Likely factors include reversibility, blast radius and verifiability.

## 3. Human specifications are not automatically complete

A human may specify "reliable asynchronous communication" while omitting an important domain requirement such as replayability, auditability, reconciliation or disaster-recovery recovery.

Therefore:

```text
human prompt != complete ground truth
```

A robust agentic environment should expose authoritative organisational/domain constraints independently of the immediate task prompt: policies, regulations, ADRs, platform standards, recovery requirements and risk controls.

A requirements/planning agent can help challenge assumptions, but simply adding more agents does **not** create independent evidence if all agents share the same incomplete context.

## 4. Verification becomes more important as implementation gets cheaper

The valuable part of TDD/BDD may increasingly be the **durable executable specification and regression asset**, rather than forcing an autonomous coding agent through the exact human red-green-refactor ritual.

Working hypothesis:

```text
specification
    -> generation
    -> independent verification
    -> controlled release
```

Existing regression tests, acceptance tests, integration tests, contracts, CI gates and production evidence can act as constraints on agent autonomy.

A coding agent's objective must not simply be "make CI green". Existing tests are evidence and institutional knowledge; the agent should not silently delete, skip or weaken them to make its own change pass. A genuine specification conflict should be escalated.

## 5. Cheap implementation changes architecture economics, but complexity remains real

Historical technology adoption cost bundled together:

- learning a new tool;
- implementing it;
- integrating it into local/dev/CI environments;
- operating it in production;
- supporting upgrades/incidents;
- adding another concept to the organisation.

Agents may dramatically compress the first three. They reduce, but do not eliminate, the latter costs.

Useful rule developed from the historical Flink example:

> **Experiment freely; adopt conservatively.**

When prototypes are cheap, an agent can build/benchmark alternatives quickly. Production adoption should still be justified by the capability gained relative to the lasting operational/conceptual complexity introduced.

An additional risk is that agents make **overengineering cheap**: implementation effort no longer acts as a natural brake on unnecessary architectural complexity.

## 6. Agenticity should be selective

Not every financial-software decision benefits from LLM autonomy.

Likely deterministic candidates:

- IBAN/checksum validation;
- ledger posting mechanics;
- idempotency guarantees;
- hard policy/permission boundaries;
- other crisp rules where deterministic software is simpler and safer.

Stronger agentic candidates:

- ambiguous investigations;
- evidence gathering;
- dynamic planning;
- policy/knowledge retrieval;
- exception classification;
- remediation recommendations;
- workflows that historically required humans to navigate many systems and incomplete information.

The recurring question should be:

> **What genuinely improves because this decision becomes agentic?**

---

# Domain anchors from prior engineering experience

## Cross-border payments

Re-examine traditional payment workflows from an agentic perspective:

- payment failure investigation;
- evidence gathering across payment state, beneficiary data and downstream responses;
- routing/remediation recommendations;
- human escalation for high-risk or irreversible actions;
- retaining deterministic boundaries for actual money movement, ledger integrity and hard controls.

## KYC / onboarding / AML

Traditional implementation often combines deterministic validation, rules engines, external KYC/sanctions/fraud checks and manual exception handling.

Agentic opportunity:

```text
case / goal
  -> decide what evidence is missing
  -> invoke approved tools
  -> retrieve relevant policy
  -> reconcile ambiguous/conflicting evidence
  -> request additional evidence where permitted
  -> recommend action or escalate
```

This provides a concrete domain for studying planning, routing, tool use, retrieval, memory, reflection, guardrails, evaluation and human-in-the-loop **as those topics are introduced in depth later**.

## SWIFT reference-data ingestion / outbox / replay

Historical engineering example:

- daily SWIFT reference information had to be ingested and propagated;
- the organisation strongly valued durable event publication/recovery, often expressed as "what happens in disaster recovery; how do we replay?";
- a Flink-based implementation incurred a long adoption spike.

Agentic reinterpretation:

- encode the **underlying invariant** (durability, recoverability, replay, reconciliation, auditability) rather than fossilising a particular implementation such as "always use Flink/Kafka/outbox";
- let an agent reason from those constraints to implementation options;
- exploit cheap prototyping while still pricing long-term operational ownership.

---

# Term-1 planning implications

FTEC5660 is not just another low-cost lecture stream. The two project-heavy assessments are likely to create **large, uneven workload spikes** during Term 1.

Planning therefore needs to balance:

```text
live FTEC5660 lectures + project work
        |
        +-- immediate AIMS5701 / AIMS5702 preparation
        |
        +-- protected January maths lane for AIMS5704
```

The maths lane should not disappear merely because an agentic project becomes interesting. During heavy project weeks, reduce the maths block if necessary but preserve continuity through short retrieval/application sessions where possible.

Conversely, do not pre-study or memorise the pattern catalogue simply because it was shown in Lecture 1. Let live FTEC5660 teaching/projects determine which individual patterns deserve depth while the roadmap protects prerequisites for the more mathematically demanding ML Theory module.

---

# Open questions to revisit later

- How should organisations encode decision rights and escalation boundaries for agents?
- How much of a human-provided specification should an agent challenge before acting?
- How should authoritative regulation/policy be separated from model-generated reasoning?
- How should verification artifacts be protected from the agent that generated the implementation?
- When is a second verifier agent useful, and when is it merely correlated AI checking AI?
- How should agents discover useful tools that are not currently available in the organisation?
- When should an agent be allowed to introduce a new dependency versus only propose it?
- Does cheap retooling materially change YAGNI/architecture trade-offs in practice?
- Which banking/KYC/AML workflows are truly improved by dynamic agent planning rather than deterministic orchestration?

---

## Future-update rule

After each substantive FTEC5660 lecture/project session:

1. update the relevant lecture/project log;
2. add only durable cross-lecture synthesis here;
3. convert particularly valuable personal reflections into **personal-synthesis cold-recall prompts**;
4. add specific agentic patterns to recall only after they have been substantively taught/applied;
5. revise working hypotheses when later course evidence contradicts them;
6. update the global roadmap/state only when FTEC5660 materially changes term priorities or workload.
