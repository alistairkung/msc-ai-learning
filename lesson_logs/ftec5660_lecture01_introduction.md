# FTEC5660 Lecture 01 — Introduction to Agentic AI

_Date: 2026-09-08_
_Status: **Lecture completed; first-pass synthesis recorded**

## Why this log exists

This is a retrieval blueprint for the first FTEC5660 lecture. It deliberately separates:

1. **course material** from the uploaded Lecture 1 slide deck;
2. **personal synthesis** developed afterwards through discussion;
3. **future cold recall** for both the taught material and my own reasoning.

Do not treat the personal synthesis as if it came from the lecturer.

### Important retrieval boundary

The long list of agentic design patterns in Lecture 1 was presented as an **introductory overview of what the course will cover**, not as 21 items taught in depth during this lecture.

Therefore:

> **Do not ask the learner to name, enumerate or reconstruct the full pattern list from memory.**

The list is a course map/reference. A pattern becomes a fair cold-recall target only after it has been substantively taught, discussed or applied. Future retrieval should favour explanation, recognition, comparison and application over catalogue memorisation.

---

# 1. Course material

## Why agentic systems now

The lecture frames a shift from isolated models toward **systems that reason, plan and act**. LLMs may provide the cognitive engine, but structure is required for reliability. Design patterns provide reusable solutions and a shared vocabulary for building robust, scalable and safe agentic applications.

## Working definition of agentic AI

Agentic AI can pursue a goal, decide next steps, use tools and adapt with limited supervision.

The lecture's high-level loop:

```text
1. Perceive context
   documents / transactions / emails / policies / events
        ↓
2. Reason and plan
   break work into steps; choose tools/evidence
        ↓
3. Act through tools
   APIs / queries / workflow updates / decisions
        ↓
4. Learn and escalate
   feedback / logs / evals / human approvals
```

Key traits highlighted:

- autonomy;
- proactiveness;
- reactiveness;
- goal orientation.

## Why agentic design patterns

Agent behaviour introduces **state + multi-step control flow**. The lecture highlights difficult recurring problems including:

- tool choice;
- error recovery;
- coordination.

Patterns are intended to improve structure, maintainability and reliability and to avoid reinventing recurring solutions.

## Introductory overview of patterns to be covered

Lecture 1 showed the course's broader pattern catalogue, including prompt chaining, routing, parallelisation, planning, goal setting/monitoring, tool use, MCP, memory, knowledge retrieval, multi-agent collaboration/communication, reflection, learning/adaptation, reasoning, exploration/discovery, exception handling/recovery, human-in-the-loop, resource-aware optimisation, guardrails, evaluation/monitoring and prioritisation.

At this point the useful takeaway is **the shape of the course**, not memorising the names. The slides group the pattern space around:

- orchestration;
- enterprise knowledge and system access;
- multi-agent collaboration;
- decision intelligence;
- governance, safety and operational control.

As later lectures teach individual patterns in depth, add those patterns to retrieval based on what was actually taught.

## Evolution from LLM workflow to agentic AI

The lecture describes a rough progression:

```text
LLM workflow
prompt + rules-based triggers
        ↓
RAG
external grounding
        ↓
AI agent
planning + tools + memory + reasoning
        ↓
agentic AI
specialised/collaborating agents, often with HITL
```

## Spectrum of agent complexity

- **Level 0:** reasoning core; no tools/memory.
- **Level 1:** connected problem-solver; search/RAG/tools.
- **Level 2:** strategic agent; planning + context engineering.
- **Level 3:** collaborative multi-agent system; specialised team.

## Multi-agent systems

Multiple agents can interact in a shared environment. Coordination enables division of labour; communication and shared context become important for coherence.

## Operational/course framing

The lecturer explicitly presented the area as fast-moving, with many unknowns, and asked students to expect bugs/typos, manage expectations, adapt and use the TAs/feedback loop.

The lecture also framed AI use for learning as beneficial when it supports thinking rather than replacing cognitive effort. For this repository, the operational implication is unchanged: use AI as tutor/scaffold and preserve cold retrieval and learner-owned reasoning.

---

# 2. Personal synthesis — conventional SWE beside agentic AI

The first jarring observation was that the lecture's "design patterns" did not call back to traditional software-engineering patterns such as Factory, Strategy, Observer, Adapter or Command.

Working interpretation:

```text
Traditional SWE patterns
    -> structure collaborating software components

Agentic patterns
    -> structure behaviour, decision-making and multi-step control flow
```

They are different abstraction layers rather than obvious replacements for one another.

Useful recurring question for later lectures:

> **What existing software-engineering concept is this pattern related to, and what is genuinely new because the decision-maker can be an LLM?**

This matters because agentic applications still run on ordinary software with ordinary concerns: state, contracts, retries, idempotency, consistency, observability, security and failure handling.

---

# 3. Personal synthesis — finance-domain reinterpretation

The course is being taught through the lens of automating finance/fintech/business workflows rather than specifically through autonomous software engineering.

My useful parallel is to re-examine financial workflows I have already seen built conventionally.

## KYC / onboarding / AML

Traditional shape:

```text
application
  -> validation
  -> deterministic rules
  -> external KYC / sanctions / fraud checks
  -> rules engine
  -> accept / reject / manual review
```

Potentially agentic shape:

```text
case / objective
  -> decide what evidence is needed
  -> choose approved checks/tools
  -> retrieve policy
  -> reason across evidence
  -> request more information if needed
  -> recommend action or escalate
```

This provides concrete hooks for planning, routing, tool use, knowledge retrieval, reflection, HITL, guardrails and evaluation **when those patterns are taught later**.

## Cross-border payments

Potential agentic opportunities appear strongest around historically ambiguous/manual work:

- payment failure investigation;
- gathering evidence across multiple systems;
- explaining downstream responses;
- remediation planning;
- selecting the next permitted diagnostic action;
- escalating irreversible or high-risk decisions.

Likely deterministic boundaries should remain around things such as ledger integrity, hard validation rules, idempotency and tightly controlled release of funds.

The goal is not "LLM all the things". The question is whether dynamic reasoning genuinely improves a particular workflow.

---

# 4. Personal synthesis — autonomy is a decision-rights problem

Discussion moved from coding agents into a more general agent-design question:

> **If the agent is genuinely autonomous, which engineering/business decisions should it be allowed to make?**

Examples considered:

- choose RabbitMQ vs Kafka from stated requirements;
- propose blue/green vs canary vs shadow traffic;
- recognise that live-data mirroring would provide stronger evidence;
- discover that Istio could provide a missing capability;
- decide when a task cannot safely proceed under current tools/constraints.

Important distinction:

```text
autonomy to reason
    != autonomy to install/use anything
```

A useful hierarchy is:

```text
reason/discover
    -> propose
    -> use approved capability
    -> request/receive additional capability
    -> escalate high-blast-radius organisational decisions
```

Introducing a new production technology may have consequences beyond the current task, so the agent can be free to **recommend** it without automatically being free to deploy it.

---

# 5. Personal synthesis — underspecification and institutional constraints

A dangerous simplification would be:

```text
human specifies
    -> agent implements
```

because the human specification may omit something important.

Example considered:

> "We need reliable asynchronous communication."

A human may fail to mention that the financial domain requires replay, reconciliation, audit history or disaster-recovery reconstruction.

An agent optimising only against the prompt could produce a locally sensible queue solution that satisfies all visible acceptance tests while missing the real organisational requirement.

Therefore important constraints should not live only in the immediate task prompt. They may need to come from authoritative sources such as:

- regulation;
- internal policy;
- architecture decisions;
- recovery/RPO/RTO standards;
- security controls;
- operational/platform constraints;
- historical institutional knowledge.

A second "review agent" can help discover omissions, but adding agents does not automatically create independent assurance if they share the same incomplete premises.

---

# 6. Personal synthesis — testing, BDD and confidence to release

The discussion started from TDD/BDD against an agentic coding backdrop.

Working distinction:

```text
TDD as human development ritual
    versus
specifications/tests as durable verification assets
```

Even if an autonomous coding agent does not benefit from strict red-green-refactor in the same way a human does, executable specifications remain valuable because they can:

- guide implementation;
- encode expected behaviour;
- preserve historical regression knowledge;
- feed CI/CD release gates;
- constrain autonomous change.

Acceptance/BDD-style specifications may be particularly useful when they sit outside the builder agent's control.

Important failure mode:

> If the coding agent's objective is merely "make CI green", deleting a failing test, weakening an assertion, over-mocking or skipping a case may be instrumentally rational.

Desired behaviour when an existing test fails:

```text
existing test fails
    -> investigate why
       -> regression introduced: fix implementation
       -> intended behaviour genuinely conflicts: escalate/seek approval
```

Do not silently modify the evidence until the task appears successful.

As implementation becomes cheaper, verification/evaluation and confidence-to-release may become more important, not less.

---

# 7. Personal synthesis — architecture when implementation cost collapses

Historical example: a daily SWIFT reference-data ingestion/propagation task led to an Apache Flink spike that consumed roughly four weeks learning the framework, making it work in the development environment and implementing the solution.

Agentic implication:

- learning unfamiliar APIs may become dramatically cheaper;
- prototyping alternative implementations may become dramatically cheaper;
- environment/configuration work may become cheaper;
- long-term production complexity, operational ownership and real-world migration risk remain real.

Useful principle:

> **Experiment freely; adopt conservatively.**

Cheap implementation may make it easier to compare a boring batch/outbox solution against Flink/Kafka/etc. using real prototypes rather than architecture-by-opinion.

Counter-risk:

> **Overengineering becomes cheap too.**

Historically, large implementation effort acted as a natural brake on unnecessary architectural complexity. An agent capable of producing an elaborate system quickly removes that brake while leaving the production system with all of its moving parts.

## SWIFT / outbox / replay nuance

Historical organisational principle appeared to be less "always use technology X" and more:

> important state changes should be durably represented so downstream state can be reconciled/recovered/replayed after failure or disaster recovery.

That underlying invariant is more valuable to preserve than a blanket implementation rule such as "use Flink" or even "use Kafka".

---

# 8. Cold recall — course material

Do these **without looking above first**.

1. In your own words, what makes a system agentic rather than just an LLM call?
2. Reconstruct the four-stage loop from context perception through escalation.
3. Why do the lecture slides argue that agentic systems need design patterns?
4. What kinds of hard problems arise when agent behaviour becomes stateful and multi-step?
5. Explain the difference between Level 0, Level 1, Level 2 and Level 3 agent complexity.
6. What changes as the lecture moves from a simple LLM workflow to RAG to an AI agent to collaborative agentic AI?
7. Why are communication/shared context important in multi-agent systems?

### Explicit non-question

Do **not** ask "name all the patterns", "how many patterns were there?", or any equivalent enumeration question. Lecture 1 only used the catalogue as an overview of later course content.

---

# 9. Cold recall — personal synthesis

These prompts intentionally test **my own post-lecture reasoning**, not only lecturer material. Sample 2–3 at a time rather than replaying the whole list.

1. Why did the phrase "agentic design patterns" initially feel jarring from a traditional SWE background? Reconstruct the distinction you eventually made.
2. Reconstruct your argument that agent autonomy is better thought of as **decision rights** than "AI can do anything".
3. You considered an agent deciding RabbitMQ/Kafka/Istio/rollout strategy. Where did you place the boundary between reasoning, proposing, using approved tools and introducing new organisational capabilities?
4. Why is "human specifies, agent implements" insufficient when the human may forget replayability, DR or regulatory requirements?
5. Why does adding a second agent not automatically solve underspecification or verification?
6. Reconstruct your argument for why BDD/acceptance tests and regression suites may remain valuable even if strict TDD red-green-refactor becomes less central for coding agents.
7. If an agent encounters an existing failing regression test during its own PR, what behaviour did you want instead of simply changing/deleting the test?
8. What distinction did you make between **cheap adoption/implementation** of a new tool and **long-term operational ownership**?
9. Reconstruct the rule "experiment freely; adopt conservatively" from the historical Flink example.
10. Why might cheaper implementation perversely make overengineering easier?
11. Give one payments/KYC/AML activity that seems like a good agentic candidate and one that should probably stay deterministic. Explain why.
12. What was the deeper architectural principle behind the historical "what happens in DR; how do we replay?" outbox/event discussion?

---

# 10. Open / unresolved

- Exact assessment weighting for the hackathon + final project should be verified from official module material; current memory is roughly 80% combined.
- The pattern catalogue is established as a Lecture-1 **overview of future course coverage**; add individual patterns to retrieval only when later material teaches/applies them substantively.
- Later lectures should test/refine the working hypotheses around bounded autonomy, verification provenance, tool discovery and agent-vs-deterministic boundaries.

---

## Bridge to next FTEC5660 session

Before or after the next lecture:

1. run a short cold recall from the **course-material** prompts;
2. pick only 2–3 **personal-synthesis** prompts;
3. connect newly taught pattern(s) to one familiar payments/KYC/AML workflow;
4. add those specific patterns to retrieval only once they have actually been taught/applied;
5. update `ftec5660_course_context.md` only when the new lecture materially changes a cross-cutting synthesis thread.