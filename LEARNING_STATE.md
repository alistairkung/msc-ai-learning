# Learning State — Current Handover

_Last maintained: 2026-10-07. Learning evidence through 2026-10-07. Delivery/recall plan reviewed 2026-10-05._

Read `SESSION_WORKFLOW.md` for tutoring rules. `learning_progress.yaml` is the structured learning-evidence projection; `deadlines.yaml` is the separate delivery-planning record used for explicit workload constraints. Focused lesson/course notes remain the detailed evidence source. Do not infer mastery from code presence or deadline urgency.

## Three parallel commitments

| Lane | Next useful work | Why / boundary |
|---|---|---|
| Continue | **AIMS5701 HW1 (Search): independent attempt → receipt-recorded targeted scaffolding by 14 Oct** | The 6 Oct generic cold-recall block repaired state-space counting and admissibility/consistency on changed examples, and confirmed the UCS goal-popped distinction. Manual A* work is conceptually sounder when the graph/frontier are externalised on paper; one real `g`/`f` bookkeeping slip occurred. On 7 Oct, consistency ⇒ nondecreasing `f` was repaired and then reconstructed cold with a conceptual algebra script: adding `g(A)` means adding cost already paid, converting remaining-cost reasoning into estimated-total-solution-cost reasoning. The A* optimality blocking argument was also consolidated as `f(n) <= C* < f(G)` for an optimal-path frontier node versus a suboptimal goal. Next: attempt HW1 independently; if blocked, use a separate transcript-recorded window with structurally equivalent but concretely different scaffolds. |
| Parallel | **AIMS5702 lab readiness: epoch/eval orchestration → CNN bridge** | The 1 Oct delayed sweep confirmed broad Lecture 1–3 retention and repaired unequal-rank broadcasting plus stepped-slice stride/offset reasoning. The remaining practical gap is epoch/evaluation orchestration and metric accumulation; close that with one changed pipeline, then move into CNN shapes/mechanics ahead of 15 Oct. |
| Protect | **FTEC5660 Private Client Graph: build deterministic evaluator** | Case 01 now runs through live structured extraction and deterministic graph construction. The first live extraction recovered all six intended edges with no extras. Evaluation semantics are now frozen: semantic edge comparison, symmetric normalization, precision/recall/F1, and approved-evidence provenance scored only on true-positive edges. Next implement the evaluator behind this contract before adding harder cases or retries. |

These lanes coexist; they are not one sequential queue. Delivery dates can temporarily resize them, but a deadline is not itself learning evidence.

## Delivery constraints — separate from learning evidence

Canonical structured copy: `deadlines.yaml`. **AIMS5701 Homework 1 — Search Algorithms is due 14 Oct and remains the nearest delivery priority**, followed by the FTEC5660 solo hackathon on 19 Oct and **FTEC5660 Homework 2 — CV verification agent and adversarial CV on 20 Oct**. Protect the 5701 cold-recall/independent-attempt boundary first, then treat 19–20 Oct as a compressed FTEC delivery cluster rather than two unrelated queues. For HW2, course use of GenAI is learner-reported as permitted; preserve learner ownership of agent/verification architecture, deterministic-versus-stochastic boundaries, evaluation and adversarial reasoning while allowing routine implementation to be delegated where useful. Preserve full AI transcripts used for AIMS5701 assignment-related concept support to satisfy that homework's acknowledgement requirement. Keep delivery planning distinct from `learning_progress.yaml`.

## AIMS5701 — Search delayed proof confirmation, 7 Oct

Detailed source: `lesson_logs/aims5701/hw1_search_cold_recall_2026_10_06.md` (7 Oct continuation appended).

The delayed confirmation strengthened the previously fragile proof-level Search material. After an initial goal-node contamination, the learner independently reconstructed consistency => nondecreasing `f`: `h(A) <= c(A,B)+h(B)` becomes `f(A) <= f(B)` by adding `g(A)`, understood conceptually as adding the cost already paid so a remaining-cost comparison becomes an estimated-total-solution-cost comparison. A visual inconsistent-heuristic example also made the reopening mechanism concrete.

The A* blocking optimality proof was consolidated using the same semantic anchor: for frontier node `n` on an optimal path, admissibility gives `f(n) <= C*`; a suboptimal goal has `h(G)=0`, hence `f(G)=g(G)>C*`; therefore the optimal-path node must be popped first. Preserve the exam-ready conceptual scripts in the detailed log. Search has reached today's stop condition; move to Markov-chain diagnostic and HMM/particle-filtering JIT.

## AIMS5701 — HW1-targeted Search cold recall + calibrated survey, 6 Oct

Detailed source: `lesson_logs/aims5701/hw1_search_cold_recall_2026_10_06.md`.
Assignment-related transcript receipt: `lesson_logs/aims5701/assignments/hw1_search/ai_transcripts/AIMS5701_HW1_AI_Conversation_Transcript_2026-10-06.md`.

Two Search blocks were completed on 6 Oct. The first was a generic cold-recall diagnostic without the problem sheet. The second loaded HW1 only to calibrate concept coverage, reasoning pattern and difficulty; every practice task remained a concretely fresh analogue and the actual assessed questions were not solved.

The strongest newly exposed conceptual gap was **minimal state formulation**: distinguishing dynamic world state from fixed map/problem information, then retaining only dynamic variables that can affect legal future behaviour or goal-relevant outcomes. Repeated changed examples repaired this within-session, including future-relevant Boolean flags and inclusive symbolic ranges such as `0..Rmax -> Rmax+1`. Treat this as repaired same-session evidence and check once with a delayed changed example before calling it durable.

BFS mechanics are broadly intact, but the learner initially conflated expansion order with returned path; explicit parent tracing repaired this. State-space counting still shows occasional small off-by-one or omitted-factor slips.

Admissibility reasoning is conceptually available. A changed example exposed one inequality-direction slip, then the learner correctly articulated that heuristic distance and true action cost may be in different units, so a distance heuristic can overestimate when one action covers multiple cells. Admissibility versus consistency is now stronger: the learner independently distinguished the global lower-bound condition from the local edge condition and gave an admissible-but-inconsistent edge inequality.

A* remains primarily a **bookkeeping-under-load** risk rather than a missing algorithmic model. One fresh trace used an incorrect initial `f=g+h` arithmetic result, changing expansion order, but cheaper-path update and parent logic were understood after correction. Continue to externalise `g/h/f`, frontier and parents on paper.

Next AIMS5701 confirmation pass on 7 Oct should stay bounded: one cold UCS trace; one clean A* trace; one heuristic-design/admissibility probe; one small admissible-but-inconsistent closed-set trace; and a brief cold reconstruction of consistency => admissibility / nondecreasing `f`. Do not turn this into another long Search session if those return cleanly.

## AIMS5702 — lecture-break consolidation + lab readiness, 1 Oct

Detailed source: `lesson_logs/aims5702/lecture_break_consolidation_lab_readiness_2026_10_01.md`.

A broad delayed retrieval sweep across Lectures 1–3 was productive. Tensor-axis/reduction semantics, right-aligned broadcasting, singleton insertion, pairwise dot products/einsum, reshape/flatten/transpose distinctions, cross-entropy intuition, Dataset/DataLoader roles, train/validation/test roles and the core batch-training dependency chain all returned with either independent answers or quick repair.

The most substantial repair was stepped-slice storage reasoning. The learner already understood stride/offset/contiguity conceptually, but repeatedly mixed slice stop, selected-count/shape and step when calculating a view's stride. After ~30 minutes of changed examples the durable mapping stabilised as **start -> base offset, step -> new stride, count -> new shape**, and the final changed example was solved cleanly end to end. Keep this as same-session repaired evidence rather than delayed-independent mastery.

Other narrow weak edges remain: integer index versus length-one slice, PyTorch `Linear.weight` storage orientation, and formal objective notation. These all responded to semantic grounding rather than requiring conceptual reteaching.

The changed multiclass lab-style pipeline reached a useful boundary. Data/split shapes, `TensorDataset`, loader intent, `nn.Sequential(6 -> 12 -> ReLU -> 3)`, CrossEntropyLoss, SGD intent and the core `zero_grad -> forward -> loss -> backward -> step` sequence were reconstructed. API names needed small corrections (`model(X)`, `loss.backward()`), and validation/evaluation orchestration remained hazy: epoch wrapping, `model.train()/eval()`, `torch.no_grad()`, using current validation batches, `argmax` predictions and epoch-level loss/accuracy accumulation were not independently reconstructed.

Next AIMS5702 block: do **not** repeat the broad sweep. Use a nearly complete changed script and fill only the epoch/eval/metric pieces, then reconstruct the whole small pipeline once with minimal prompting. If stable, begin the bounded CNN bridge.

## FTEC5660 — Private Client Graph canonical persistence architecture grill, 7 Oct

Detailed source: `lesson_logs/ftec5660/private_client_graph/canonical_persistence_grill_2026_10_07.md`.

A ~1 hour adversarial architecture grill materially strengthened the 6 Oct data-modelling reflection. The learner entered with a preference for relational canonical persistence, but accepted the challenge that PostgreSQL JSONB can itself be authoritative and that neither Case 02 nor the current Case 04 fixture proves relationalisation necessary. Rather than defending the preferred implementation directly, the learner articulated the production lesson behind the preference: canonical persisted state should remain internally trustworthy, with PostgreSQL enforcing structural/referential invariants it can naturally express rather than relying solely on application validation.

The resulting proposed boundary makes provenance integrity, provenance completeness and Matter/Proposal aggregate isolation explicit domain requirements. Evidence belongs to one explicit Source; Relationships connect Matter-local Entity identities rather than names and must retain at least one Evidence association; Proposal and Matter remain distinct lifecycle states with equivalent structural guarantees; and `CanonicalGraph` remains a deterministic reconstructed representation rather than separately persisted truth.

Important deferred boundary: entity resolution is part of the future stochastic/evaluation problem, not name normalisation in persistence. A Case 03-driven review must evaluate both under-merging (different surface forms for one real entity) and over-merging (identical names for different entities). Persistence must represent both outcomes. A future practitioner-asserted/unsubstantiated Relationship is also recorded only as a hypothesis; today's accepted Relationships continue to require documentary Evidence.

The architecture is proposed, not implemented. This is strong architecture/data-modelling judgement with AI used adversarially, not SQL/PostgreSQL implementation mastery. Next engineering step is to ticket the agreed persistence slice, then establish Case 01 equivalence plus a controlled model-free multi-source provenance baseline before resuming stochastic Cases 02–04 experiments.

## FTEC5660 — Private Client Graph canonical persistence reflection, 6 Oct

Detailed source: `lesson_logs/ftec5660/private_client_graph/data_modelling_case04_2026_10_06.md`.

Cases 02–04 have begun to pressure-test the Case 01 architecture rather than merely enlarge the benchmark. The most important 6 Oct modelling discussion came from Case 04: multiple source documents can support the same semantic relationship, so relationship identity must remain distinct from individual Evidence/assertion instances. The emerging model is Matter -> Sources -> Evidence alongside canonical Entities/Relationships, with Relationship <-> Evidence many-to-many and each Evidence item belonging to one Source.

The learner challenged an initially attractive hybrid persistence option in which Source/Evidence became relational but canonical graph facts remained authoritative inside JSONB. The resulting principle is stronger: PostgreSQL should persist enough canonical Matter facts and relationships to reconstruct the current Matter state deterministically; `CanonicalGraph` is currently a derived domain/presentation representation of that state rather than necessarily a separately persisted entity. Independent graph identity should be earned only by future lifecycle/history semantics such as graph versioning or supersession.

This is meaningful architecture/data-modelling judgement and a useful future interview example, not independent SQL implementation evidence. No relational migration was implemented in this record. Next PCG architecture work should let Case 04 specify the smallest schema evolution consistent with canonical relational state, while continuing to resist table-per-noun normalisation.

## FTEC5660 — Private Client Graph evaluation design + first end-to-end slice, 2 Oct

Detailed decision record:
- `lesson_logs/ftec5660/private_client_graph/decisions/evaluation-design-case-01-2026-10-02.md`

The first live Case 01 structured extraction succeeded against the frozen relationship-only contract: all six intended relationships were recovered, no unsupported extras appeared, directions were correct, and the shared parent sentence was reused for both parent edges. This is useful evidence that the minimal semantic extraction contract is sufficient for Case 01; it does not justify retries, verifier agents or additional LLM stages.

Deterministic graph construction is now treated as a separate bounded context from extraction. It owns candidate validation, entity derivation and type inference, entity/evidence IDs, evidence deduplication, symmetric-edge canonicalisation and relationship deduplication. The implementation is deliberately separated from `extract.py`, and each deterministic behaviour was required to have focused unit tests. This is architecture/test-design evidence rather than cold implementation mastery because coding-agent assistance was intentionally used behind learner-owned contracts.

Evaluation semantics were then designed before implementation. Predicted and ground-truth relationships will be compared as normalized semantic triples rather than by generated IDs. `spouse_of` and `sibling_of` are canonicalised symmetrically; directed relationships retain direction. Relationship quality uses TP/FP/FN plus precision, recall and F1, with diagnostic edge sets returned for failure analysis.

Provenance ground truth will store a list of `approved_evidence` spans alongside each relationship. Provenance is scored only for true-positive edges, and an edge passes when at least one attached predicted evidence span matches at least one approved span. V1 provenance accuracy is therefore the proportion of correctly recovered edges with at least one approved evidence span. This remains distinct from deterministic grounding validation, which only proves that an extracted quote occurs verbatim in the source.

Next step: implement the smallest deterministic evaluator against this frozen contract, then use its diagnostics to decide what Case 02 should make harder.

## FTEC5660 — Private Client Graph extraction contract + delegation boundary, 2 Oct

Detailed decision records:
- `lesson_logs/ftec5660/private_client_graph/decisions/extraction-contract-case-01-2026-10-02.md`
- `lesson_logs/ftec5660/private_client_graph/decisions/ai-implementation-delegation-2026-10-02.md`

Case 01's first-stage contract is now substantially simpler than the 29 Sep proposal. The LLM should emit only semantic relationship candidates containing `source_name`, `relationship_type`, `target_name` and exact `supporting_text`. It does not emit entity/evidence IDs, a separate entity list, or entity types. Deterministic code will derive unique endpoint entities, infer person/trust type from relationship semantics, detect conflicts, assign internal IDs, deduplicate evidence and build the normalised graph.

The learner actively challenged the initial idea of separate LLM entity extraction and pushed to maximise deterministic work. A neutral third-agent review was used to break the tie and independently recommended relationship-only extraction for Case 01. The future trigger for a separate entity-extraction path is now explicit: entity information must become useful even when no supported relationship edge can be asserted.

Runtime normalisation is expected to use a name-keyed entity lookup for Case 01, with the clear boundary that raw names cease to be sufficient once aliases/entity resolution enter scope. Final normalised objects remain deliberately lean: Entity = id/type/name; Relationship = source/type/target/evidence_ids; Evidence = id/document/supporting_text. Literal generated ID values are implementation handles rather than semantic evaluation targets.

The learner also intentionally loosened implementation guardrails. LangChain/API syntax is not itself the assessment target, so bounded coding-agent assistance is now acceptable once semantics have been designed. The learner retains ownership of contracts, deterministic-vs-probabilistic boundaries, evaluation and failure interpretation; framework plumbing/repetitive implementation may be delegated. The immediate delegated task is only source → structured `RelationshipCandidate[]`, with validation/normalisation/retries/UI explicitly excluded until the first real model output is inspected.

Do not over-promote this as framework mastery: no model call has yet been run in the project. The learning evidence is stronger architecture/delegation judgment and contract refinement. Next step is the first actual Case 01 structured extraction and then failure-driven iteration.

## FTEC5660 — Private Client Graph Case 01 design, 29 Sep

Detailed source: `lesson_logs/ftec5660/private_client_graph_case01_design_2026_09_29.md`. Rich personal decision records are preserved under `lesson_logs/ftec5660/private_client_graph/decisions/` rather than the shared hackathon repository.

A focused ~90-minute hackathon session deliberately stopped before LangChain implementation and transferred the receipts design discipline into a new relationship-extraction problem. Case 01 now has a six-edge graph answer key across Alice Chen, David Chen, Bob Chen, Carol Wong and the Evergreen Family Trust; the initial primitives are `parent_of`, `sibling_of`, `spouse_of`, `settlor_of`, `trustee_of` and `beneficiary_of`.

The strongest learning evidence is architectural boundary-setting rather than framework syntax. The learner reasoned that inverse/symmetric graph views should be derived deterministically rather than redundantly extracted, trust roles belong on edges, relationships should attach to stable entity identities, and provenance should be first-class evidence referenced by relationships. The learner also caught that treating ground truth as merely "facts we care about" would distort precision/recall; it is now framed as the complete answer key for the graph task, while graph-neutral meeting facts may remain outside it.

Source-fixture realism improved after domain feedback. A too-short synthetic note was replaced by a roughly 2–3 page-style one-hour fact-finding attendance note whose extra prose comes from scope, questioning, clarification, recap and next steps rather than extra graph facts. The source was checked against the six-edge answer key. One sufficient exact source passage per relationship is enough for provenance; exhaustive repeated-mention detection is not required.

Do not over-promote this session. Trust-domain vocabulary and several benchmark-design distinctions were guided/new, and no extraction pipeline has yet been implemented or tested. The draft `expected_extraction.json` in the hackathon repository is intentionally unresolved. Next session: review its field/ID/evidence choices, freeze the smallest Case 01 contract, then run the first structured extraction before considering retries, routing, reflection or other agentic complexity.

## AIMS5701 — Search retrieval + Bayes Nets I pre-lecture bridge, 30 Sep

Detailed source: `lesson_logs/aims5701/lecture03_prelecture_retrieval_2026_09_30.md`.

The first deliberate cumulative midterm-retention pass on Search produced meaningful delayed evidence. BFS/DFS/UCS/Greedy/A* frontier policies, `g/h/f`, admissibility and the intuition for consistency returned cold. UCS optimality was initially misrecalled as non-optimal and Greedy as complete; both were repaired by reasoning from frontier order and infinite-branch counterexamples. The A* blocking proof was reconstructed in depth. Its overall structure now transfers, but the admissibility inequality was flipped once after the break and `h*(n)` (remaining cost) was twice confused with the bound on `f(n)` (whole estimated path). Final changed-proof performance was independent apart from a notation typo. Keep the proof in spaced retrieval rather than promoting theorem mastery.

The 28 Sep Bayesian-network bridge also received its first delayed retrieval. Joint/conditional notation, conditional-independence meaning, DAG parent reading, local factorisation and the definition of marginalisation returned cold. Applying marginalisation to an unseen hidden-variable inference initially failed: the learner misidentified the hidden variable. Population-flow scaffolding repaired the operation, and a changed Study -> Prepared -> Pass problem then had evidence/hidden/query roles and both branches constructed independently, with only an arithmetic addition slip.

New pre-lecture work covered forward sampling, rejection sampling and likelihood weighting through a population/dot model. The key likelihood-weighting idea became operational: force observed evidence for every sample, sample unobserved nodes normally, multiply a running weight by each evidence likelihood from the CPT, then estimate a posterior as weighted query mass divided by total weighted mass. A two-evidence changed example produced `w=0.16` independently, and the indicator-function estimator notation became readable. This is same-session guided transfer, not delayed mastery.

Independence work progressed through chain, fork/common-cause and collider/common-effect structures, explaining away, observed descendants of colliders and multi-path d-separation. Concrete reasoning was strong, but the first abstract table reversed the observed chain/fork cases and the first d-separation exercise repeated the fork reversal; both were repaired immediately, after which changed multi-path examples were solved correctly. Treat d-separation as newly demonstrated/guided.

The newly released **Lecture 3: Bayes Nets I** deck materially narrows tonight's confirmed scope to **representation** and **independence**. It reviews joint/marginal/conditional probability and Bayes, defines Bayes-net semantics as a directed acyclic graph plus local conditional probabilities/CPTs, develops joint factorisation, then covers conditional independence, chain/common-cause/common-effect triples and d-separation. Sampling and variable elimination do not appear in this deck. Keep today's sampling/inference work as useful future runway; do not infer where that material moved until newer live teaching resolves it.

Next: attend Lecture 3 without more pre-study. In the next retrieval block, reconcile live emphasis and cold-check DAG/CPT semantics, factorisation, the local Markov property (“a node is conditionally independent of its non-descendants given its parents”), chain/fork/collider and one changed d-separation graph. Then diagnose Markov-chain recall before HMM / particle-filtering JIT.

## AIMS5701 — live 2026 course map confirmed, 29 Sep

Source basis: the learner supplied the current Lecture 1 intro deck. Its live tentative schedule now supersedes the older public-description ordering for AIMS5701 planning.

The course is explicitly structured around selected pre-deep-learning AI (Search -> Bayesian Networks -> HMMs/Particle Filtering), then a Week 5 deep-learning bridge (models, loss, optimisation, backpropagation, NN training), then CNNs, RNN/Transformers, RL/recommendation, latent-variable/GAN/diffusion models, meta/multimodal learning and agentic/embodied AI. Decision trees, random forests, KNN, K-means, SVM and gradient boosting do not appear anywhere in the live 12-week schedule. Remove them from the active AIMS5701 JIT roadmap unless later live material explicitly brings them back; do not interpret this scope decision as a judgment about their general relevance.

The live deck also confirms a 40% written midterm. The learner reports that it focuses on the first five weeks. This materially changes the study strategy: retain JIT for acquisition, but add systematic cumulative cold retrieval across W1-W5. Search retrieval on 30 Sep should therefore count as the first deliberate spaced midterm-retention pass rather than mere maintenance.

Current live sequence through the midterm window is: W1 introduction/intelligence-from-computation-vs-data; W2 Search; W3 Bayesian Networks; W4 HMMs + Particle Filtering; W5 models/loss/optimisation/backprop/NN training. This is a much more coherent exam target than the stale classical-ML survey map and should drive planning until contradicted by newer live material.

## AIMS5701 — Bayesian-networks JIT bridge, 28 Sep

Detailed source: `lesson_logs/aims5701/bayesian_networks_jit_2026_09_28.md`. Durable notation/reference sheet: `foundations/probability_statistics/bayesian_network_probability_bridge.md`.

The live course sequence was corrected from the stale map: the next Fundamentals lecture is **Bayesian networks: representation, independence, inference and sampling**, not decision trees.

Probability retrieval was stronger than expected. Conditional and joint probability were intact once notation was translated. Bayes' formula was not cold, but the learner derived it from the shared joint event viewed from opposite conditioning directions. Independence was initially conflated with mutual exclusivity; conditional independence intuition returned quickly.

New same-session Bayesian-network work covered DAGs/parents, CPTs, binary assignment growth, local joint factorisation, marginalisation, simple exact inference and forward/prior-sampling intuition. The strongest changed-example evidence was independently identifying a hidden middle variable and computing `P(Focus=T | Exercise=T) = (0.7*0.8)+(0.3*0.2)=0.62` by marginalising over it.

Do not over-promote this material. On the final cold check one DAG edge was misread during factorisation, marginalisation still needed wording tightened, and sampling had one threshold slip before correction. No delayed retrieval has happened yet; variable elimination, chain/fork/collider graphical independence, rejection sampling, likelihood weighting and Gibbs/MCMC were not taught.

Wednesday plan: ~1h delayed Search retrieval, ~1h delayed retrieval of this BN bridge without the summary sheet, then use the remaining 2–3h for likely lecture-facing expansion. Prioritise chain/fork/collider structure and explaining-away intuition, exact inference/variable-elimination intuition, then rejection sampling/sampling with evidence. Treat those as predicted coverage until the actual lecture deck/live teaching confirms scope.

## AIMS5701 — Search guarantees + adversarial-search bridge, 23 Sep

Detailed source: `lesson_logs/aims5701/search_guarantees_reactivation_2026_09_23.md`.

The afternoon block completed the planned search-theory bridge without repeating BFS/DFS implementation. UCS goal-popped termination and admissibility returned cold. Consistency is improving and is now connected to nondecreasing `f=g+h`, but still had one changed-example label inversion. Completeness vs optimality is understood conceptually. Branching-factor complexity was introduced: BFS `O(b^d)` time/space and DFS `O(b^m)` time, `O(bm)` space are understood intuitively, although `d` vs `m` slipped on immediate recap.

Adversarial search was introduced as pre-lecture preparation. The useful translation key is `MAX = one agent / MAX's turn`, `MIN = opposing agent / MIN's turn`, with terminal utility measured from MAX's perspective. Turn ownership initially caused repeated inversions; after a deliberate reset the learner correctly solved changed minimax trees. Alpha-beta was then derived from player-choice irrelevance before attaching alpha/beta notation. Changed pruning examples were handled with some correction, including one whole-subtree cutoff where MIN's control of the choice was initially forgotten.

Do not promote minimax/alpha-beta to established or independent mastery yet: this is same-session introductory evidence and no implementation has been attempted. The actual Lecture 2 deck did **not** cover minimax/alpha-beta, so park implementation unless a later live-course requirement brings adversarial search back.

Implementation-maintenance decision: do not immediately rebuild BFS/DFS/UCS/A* merely for completeness. Prior implementation evidence already exists; use later changed-problem blank-file reconstruction as an operational spot check when useful.

The 24 Sep reconciliation is now complete. Smaller lecture gaps were swept: state abstraction, graph-vs-tree search, iterative deepening, greedy best-first, relaxed-problem heuristics/dominance and graph-search duplicate handling. Iterative deepening needed one reteach of the actual repeated depth-limited DFS mechanism, after which the learner correctly reasoned why repeated shallow work is cheap relative to deeper exponential growth.

The difficult A* guarantee material materially improved. Consistency is now grounded in the local-edge intuition “heuristic drop cannot exceed step cost”; changed examples were classified correctly. The learner reconstructed consistency ⇒ admissibility on a changed path, reconstructed the A* blocking proof to `f(n) <= f(A) < f(B)` with scaffolding at the first inequality, and connected consistency ⇒ nondecreasing `f` ⇒ safe permanent closing. Admissibility’s exact role in the optimality proof needed one correction, so this is **guided proof reconstruction**, not delayed cold proof mastery.

Search now moves to spaced maintenance. Next AIMS5701 JIT: brief linear/logistic retrieval, then decision-tree split/impurity/information-gain intuition and random forests — but only after the receipts homework is complete.

## Immediate execution plan — 24 to 28 Sep

This short-horizon sequence is intentionally serial to reduce context switching:

```text
24 Sep
AIMS5701 reconciliation — COMPLETE
-> AIMS5702 targeted pre-lecture study — COMPLETE
-> AIMS5702 Lecture 3 — COMPLETE

25 Sep
FTEC5660 receipts only

28 Sep
receipts contingency until complete
-> then AIMS5701 decision-tree bridge
```

Detailed AIMS5702 preparation source: `lesson_logs/aims5702/lecture03_deep_learning_basics_prelecture_bridge_2026_09_24.md`.

The supplied Lecture 3 deck overlaps strongly with existing PyTorch/MLP training evidence. Do not re-teach train/validation/test, overfitting, DataLoader basics or generic training-loop mechanics from zero. Highest-value pre-lecture targets are:

- translate `y_j = Σ_i w_ij x_i + b_j` into index meaning, shapes and code semantics;
- unpack one-hot/cross-entropy and dataset-level objective notation;
- map formal gradient-descent/SGD notation onto the already-known PyTorch loop;
- explain why stacked linear maps need nonlinearity;
- preview locality + weight sharing as the motivation for CNNs.

Friday/Monday receipts work retains the existing constrained architecture and scope rule. Trees begin only once receipts is closed.

## AIMS5702 — Lecture 3 pre-lecture evidence, 24 Sep

Detailed source: `lesson_logs/aims5702/lecture03_prelecture_session_2026_09_24.md`.

The session confirmed that the underlying ML concepts are stronger than the lecturer-style indexed notation.

### Stronger / comfortable

- gradient sign, learning-rate update and basic GD/SGD mechanics;
- mapping `loss.backward()` to gradient computation and `optimizer.step()` to parameter update;
- batch/epoch intuition;
- train/validation/test roles and inference-vs-training distinction;
- why multiple linear layers collapse to one linear transform without nonlinearity;
- high-level MLP intuition;
- CNN motivation through local connectivity + shared weights.

### Fresh / fragile

- `y_j = sum_i w_ij x_i + b_j` initially blocked cold; the learner can now interpret `i`, `j`, `w_ij` and derive `W:(N,M)`, but output-side `b/y` shapes slipped once later and recovered immediately after the cue "bias belongs to the output";
- one-hot cross-entropy intuition is now usable, but true-class indexing slipped once before transferring correctly;
- dataset-objective notation required explicit translation: example index vs feature index, prediction vs loss, and `min_theta` as choosing parameters that minimise loss rather than choosing small parameters;
- `TensorDataset` was rusty and needed reteaching as an indexing/pairing wrapper over already-created tensors;
- `y_batch` shape, `optimizer.zero_grad()` and validation `torch.no_grad()` were not cold and needed correction/prompting.

Do not promote this to independent deep-learning mastery. Most evidence is same-session guided or delayed retrieval with correction.

Softmax was mentioned only as contextual outside-deck ML knowledge after a sigmoid/softmax role confusion. Do not treat it as lecturer-taught Lecture 3 evidence unless the live lecture covers it.

Lecture 3 is now complete. Detailed live evidence is in `lesson_logs/aims5702/lecture03_live_2026_09_24.md`. Next AIMS5702 work is delayed consolidation during the lecture break, followed by a bounded CNN bridge.

## AIMS5702 — Assignment 1 preparation and lecture calibration, 17 Sep

Sources: `lesson_logs/aims5702/lecture01_02_prelecture_bridge.md`, `lesson_logs/aims5702/tensor_cold_review_2026_09_11.md`, `lesson_logs/aims5702/assignment01_tensor_vectorisation_plan_2026_09_17.md`, `lesson_logs/aims5702/lecture_reflection_2026_09_17.md`, and `practice/aims5702_assignment01/`.

### Pre-lecture retrieval / refresh

The learner began with changed tensor examples before the 17 Sep maths lecture.

Evidence observed:

- reduction output shapes were retrieved correctly immediately, though the first semantic description mixed up the reduced time axis with the feature axis;
- integer indexing vs one-element slicing was rusty on first retrieval (`x[:, 1]` was initially predicted to retain a singleton dimension), then corrected and immediately transferred to `1:2` slice examples;
- broadcasting output shapes were generally retrieved correctly; semantic descriptions became reliable once values were attached to axes;
- singleton-axis meaning was understood as “reuse/broadcast along this axis”; sample/time/feature roles were successfully traced on changed examples;
- `unsqueeze` was not initially retrieved by name (`reshape` was proposed), but after introduction the learner correctly chose `unsqueeze(0)` / `unsqueeze(1)` on changed examples.

Do not promote slicing/`unsqueeze` API syntax to cold-independent based on immediate corrected retrieval.

### Pairwise dot products — concept and implementations

The learner built the operation from first principles:

```text
x: (m, k)
y: (n, k)

for each x row and y row:
    multiply matching k features
    sum over k

result: (m, n)
```

Durable mathematical model:

```text
z[m,n] = sum_k x[m,k] * y[n,k]
```

Equivalent linear-algebra description: the pairwise dot-product matrix is `X Y^T`, though the practice deliberately avoids matrix-multiplication shortcuts.

#### Single dot product

The learner implemented independently after the test contract was isolated:

```python
return (x * y).sum()
```

Key understanding: dot product = elementwise multiplication followed by reduction over the feature dimension.

#### Two-loop representation

The learner independently proposed the core construction:

```text
for each row m of x:
    for each row n of y:
        result[m,n] = dot_product(x[m], y[n])
```

Python/API support was needed for:

- `range(len(x))` rather than iterating over `len(x)` directly;
- allocating the result buffer with `torch.zeros((len(x), len(y)))` rather than the initially recalled `arange`-like idea.

Final implementation uses exactly two Python loops; the feature axis is handled inside `dot_product`, not by a third Python loop.

#### Broadcasting representation

The learner first derived the shape plan interactively, including one correction for the `y` singleton placement, then transferred it correctly to changed dimensions:

```text
(m, k) -> (m, 1, k)
(n, k) -> (1, n, k)

multiply -> (m, n, k)
sum k   -> (m, n)
```

During initial expression writing, the learner needed reminders that `unsqueeze` returns a tensor rather than mutating the original and that `.sum()` without a dimension would reduce everything. After that correction, the learner wrote the complete changed-example expression independently:

```python
(x.unsqueeze(1) * y.unsqueeze(0)).sum(axis=2)
```

and later implemented the practice function directly from recall.

Current conceptual heuristic:

> Broadcasting replaces the two outer Python loops by representing the x-row and y-row pairings as tensor axes; reduction consumes the feature axis.

#### Einsum representation

`einsum` moved from guided pre-read into guided implementation with successful immediate transfer.

The learner correctly reasoned that:

- output indices survive;
- an input index omitted from the output is reduced/summed;
- `ij->i` reduces `j`, `ij->j` reduces `i`, and `ij->ji` transposes;
- pairwise row dot products can be described as `mk,nk->mn` (or equivalent letters).

The learner transferred this to a changed customer/product example (`ik,jk->ij`) and then implemented:

```python
return torch.einsum("mk,nk -> mn", x, y)
```

### Post-lecture calibration

The lecture changed the priority of several low-level representation topics. The lecturer appears willing to probe dtype/storage/indexing mechanics explicitly, so these should no longer be treated as incidental API details.

#### Dtype representation

The lecturer asked how `int8` handles negative values; the learner did not follow the explanation confidently. Floating-point terminology around mantissa/significand and exponent also moved too quickly to feel understood or retrievable.

Keep two evidence categories separate:

```text
storage-size reasoning
    vs
bit-level value representation
```

Positive live evidence: the learner correctly calculated VRAM/storage for a `float32` example during the lecture.

Not established: signed `int8` representation and floating-point sign/exponent/mantissa intuition.

#### Strides, contiguity and slicing

Strides/contiguity remain active weaknesses and should receive more deliberate drilling. Future review should connect:

```text
shape
→ flat storage
→ stride
→ indexing/slicing
→ view
→ contiguity
```

The lecturer also used a specific slicing/indexing "trick" or formula that the learner expects may be quiz-relevant. The exact formula was not retained confidently, so recover the lecturer's exact notation from course material before drilling it rather than inventing a substitute.

#### Singleton-axis insertion

The lecturer demonstrated a manual indexing-based way to insert a singleton dimension rather than teaching `unsqueeze()` directly. The learner remembers syntax approximately like `[:, new_dim, :]`, but this is not exact evidence. Recover the actual lecture example first, then connect its semantics to singleton-axis insertion and, only secondarily, to convenience APIs such as `unsqueeze()`.

#### Interpolation sequencing

Do not move directly into interpolation yet. The learner wants a deeper cold review first:

```text
cold tensor/dtype review
    ↓
dtype representation
    ↓
stride / contiguity / slicing
    ↓
singleton-axis insertion / indexing
    ↓
then interpolation
```

### Evidence boundary for 17 Sep

The pairwise implementations are strong **same-session guided-to-independent implementation evidence**, not delayed cold mastery.

Strong current evidence:

- understands a single dot product as elementwise multiply + sum;
- understands pairwise dot products as every x-row paired with every y-row;
- can explain why output shape is `(m,n)` and why `k` disappears;
- can relate the two-loop, broadcasting and einsum versions as three representations of the same computation;
- successfully transferred broadcasting shapes and einsum index notation to changed dimensions/examples during the session;
- correctly performed a `float32` VRAM/storage calculation in live lecture context.

Still fragile / needs delayed retrieval:

- Python allocation/iteration syntax (`range(len(...))`, tensor allocation) was not cold;
- slicing integer-index vs slice dimension preservation recovered quickly but was initially rusty;
- `unsqueeze` API name/axis manipulation was initially guided;
- broadcasting expression construction initially needed reminders about returned tensors and specifying the reduction dimension;
- einsum is newly learned and only has same-session transfer evidence;
- signed integer representation and floating-point sign/exponent/mantissa intuition are not established;
- strides/contiguity and lecturer-specific slicing/indexing mechanics need deeper drilling;
- no evidence yet for vectorised advanced indexing or bilinear interpolation;
- the actual Assignment 1 functions have not been independently attempted and must not be marked complete from the practice code.

### AIMS5702 next step / 18 Sep plan

Tomorrow's substantive study session should focus on **AIMS5702 Assignment 1** rather than splitting the block across courses.

Before breaking down interpolation, begin with a bounded cold review/drill of dtype representation, strides/contiguity, slicing/indexing and singleton-axis insertion, using the lecturer's exact notation where course material is available. Then continue into the assignment scaffold and independent attempt.

FTEC5660 receipts homework is intentionally deferred to the next substantial block planned for Monday; this is workload sequencing, not a change in its evidence state or importance.

## AIMS5702 — 18 Sep representation checkpoint + interpolation bridge

Detailed source: `lesson_logs/aims5702/assignment01_interpolation_bridge_2026_09_18.md`.

The planned prerequisite checkpoint was completed before attempting interpolation implementation.

### Representation evidence

- Storage-size reasoning was retrieved with an initial bits/bytes unit slip; a changed float16 example was then correct.
- Signed `int8` / two's-complement representation was genuinely new at the start of the session. The learner derived the `-128..127` range after teaching and decoded a changed signed bit pattern successfully. This is immediate-transfer evidence only.
- Floating-point sign/exponent/significand roles were clarified. Exponent-range vs significand-precision was initially reversed, then transferred correctly to a changed hypothetical format.
- Stride/contiguity received substantial changed-example drilling. The learner now explains contiguity through logical traversal vs compact underlying storage rather than merely memorising API outcomes.
- The lecturer's storage-index and base-offset formulas were supplied from memory and applied to changed examples.
- A useful fragility was exposed: slice start affects base offset, while slice step affects the view stride. This distinction recovered after correction.
- `start:stop:step` syntax was not initially retrievable when all three fields appeared, then recovered on immediate changed examples.
- `np.newaxis` / `None` singleton insertion was connected to PyTorch `unsqueeze`; changed shape examples were correct.

Do not promote any of this same-session corrected/guided representation work to delayed cold mastery yet.

### Bilinear interpolation

Bilinear interpolation moved from **planned/no evidence** to **conceptually demonstrated with guided derivation and successful manual changed-example execution**.

Current mental model:

```text
normalised query coordinate
    ↓
scale to grid coordinate
    ↓
lower/upper row + column indices
    ↓
row/column fractions
    ↓
gather four neighbouring grid values
    ↓
linear interpolation across top and bottom
    ↓
linear interpolation between those results
```

The learner manually completed a changed bilinear example to the correct final value and understood that the same scalar interpolation expression can operate elementwise over `(N,)` tensors.

Advanced paired indexing `grid[rows, cols]` was introduced as the mechanism for gathering one value per query point without a Python loop. Pairing semantics were understood, although reading values from the toy grid produced a couple of lookup slips.

The supplied Assignment 1 Test 1 harness was also understood: SciPy `RegularGridInterpolator` is the trusted oracle; `x_ref/y_ref` are normalised `[0,1)` query coordinates; `h-1/w-1` scale them into grid space; the student loop/no-loop implementations are compared with the reference within tolerance.

### Current Assignment 1 boundary

Established today:

- conceptual 1D interpolation;
- conceptual bilinear interpolation;
- lower/upper neighbour selection and fractional position;
- conceptual vectorisation path through paired indexing + elementwise arithmetic;
- understanding of the first interpolation test harness.

Not established:

- independent `interp2d_forloop` implementation;
- independent `interp2d_nofor` implementation;
- boundary/edge handling;
- passing interpolation tests;
- delayed cold retrieval of today's new representation/interpolation material.

### AIMS5702 next step

Do not replay today's full lesson.

Next focused block (~2–3 hours expected):

1. brief changed-example retrieval of the fragile pieces;
2. map the supplied loop implementation/context onto lower/upper indices, four neighbours and fractions;
3. learner implements/reconstructs the loop version;
4. lift scalar-per-point variables into `(N,)` tensors;
5. learner implements the no-loop version with advanced indexing and elementwise interpolation;
6. run supplied tests and diagnose boundary/indexing failures.

## AIMS5702 — Assignment 1 implementation complete, 21 Sep

Detailed source: `lesson_logs/aims5702/assignment01_completion_2026_09_21.md`. The learner also supplied the completed notebook as the authoritative Assignment 1 artifact for this session.

Verified notebook evidence:

- all three pairwise-dot-product implementations are present: two-loop, no-loop singleton-axis/vectorised, and einsum;
- supplied pairwise tests are green across changed dimensions, a larger float32 case and invalid-shape cases;
- `interp2d_nofor` is complete;
- supplied interpolation tests are green against SciPy `RegularGridInterpolator`, exact corner/centre cases and invalid-input cases.

### Interpolation implementation evidence

After the weekend, lower/upper neighbour selection and fractions retrieved cold, while the scalar interpolation formula itself needed the cue `start + fraction * (end - start)` before transferring correctly.

The lecturer's matrix bilinear notation was then translated into the geometric model:

```text
x1/x2 -> lower/upper x
y1/y2 -> lower/upper y
Qij   -> corner location
f(Qij)-> value at that corner
```

The learner understood that the four-corner weighted sum is the algebraically expanded version of horizontal top/bottom interpolation followed by vertical interpolation.

For the no-loop implementation, the learner derived the central vectorisation move: promote each per-query scalar into an `(N,)` tensor and process all query points together. Paired advanced indexing gathers the four `(N,)` corner-value tensors, followed by elementwise weighted arithmetic to produce the `(N,)` result.

Targeted support/debugging was needed for `.long()` after `floor`, `torch.clamp(..., max=...)`, device/dtype conversion, corner-gather insertion and ordinary typos. Paired advanced indexing was not initially retrieved after the weekend. `dtype`, `device` and `.to(...)` were newly taught rather than assumed.

### Evidence boundary

Assignment 1 is **implemented, submitted, and supplied tests are green**, but do not mark the interpolation/vectorisation skill as delayed cold-independent mastery. The implementation was guided/debugged and no later blank-file reconstruction has occurred.

The transferable target to maintain is notation/scalar algorithm → tensor shapes → vectorised indexing/arithmetic, not memorisation of the bilinear formula.

AIMS5702 Assignment 1 can leave the active implementation queue unless submission/admin work remains.

## FTEC5660 / LangChain — receipts HW1 complete

Detailed sources:
- `lesson_logs/ftec5660/hw1_receipt_chain_session_2026_09_21.md`
- `lesson_logs/ftec5660/hw1_receipt_chain_session_2026_09_22.md`
- `lesson_logs/ftec5660/hw1_receipt_chain_completion_2026_09_25.md`

The receipts homework is complete and submitted. The final public path passed 27/27 deterministic tests, processed all seven public receipts, and produced both correct aggregate answers.

The completed architecture separates probabilistic vision extraction from deterministic validation/calculation. `ReceiptValidator` normalises money to Decimal and reconciles item/discount/subtotal/rounding invariants. Real batch evaluation exposed legitimate zero-value marker lines and stochastic model errors including quantity unit-price vs extended-total confusion; the validator and prompt rules were corrected from that evidence.

The learner pushed the per-receipt path into a composed LCEL runnable:

```text
prompt | llm | JsonOutputParser | RunnableLambda(validate)
                              -> semantic retry on ValueError
```

This is meaningful changed-domain transfer of LCEL composition. The broader Runnable API and `RunnableBranch` remain outside cold-independent evidence.

The final grader policy also introduced a deliberate availability trade-off: validated/retrying extraction is preferred, but after bounded retries a raw extraction fallback prevents one stubborn receipt from crashing the entire batch and suppressing `results.csv`.

The lecturer's single-file submission requirement forced the clean modular implementation into `hw1.py` for submission. After submission, the learner froze that repository and created a separate attributed `receipt-agent` project to restore modular extractor/validator/calculator boundaries and add a cleaner standalone pipeline/CLI. Treat this as post-submission engineering reflection, not additional course mastery.

Receipts should now leave the active build queue. Next FTEC5660 delivery pressure is the 19 Oct solo hackathon; next JIT learning priority remains the AIMS5701 regression -> decision trees -> random forests bridge.

## AIMS5701 / search and trees

Detailed source: `lesson_logs/aims5701/search_guarantees_reactivation_2026_09_23.md`.

The 23 Sep morning block provided delayed search evidence without replaying implementations:

- BFS mechanics, parents-as-seen/predecessor, FIFO and shortest-by-edges reasoning retrieved strongly.
- DFS LIFO/depth-first behaviour and lack of shortest-path guarantee retrieved strongly.
- UCS initially picked up A*'s heuristic by mistake, then recovered lowest-`g(n)` selection and the cheaper-route update rule.
- UCS termination needed a substantive correction: optimality is guaranteed when the goal is **popped as the minimum-cost frontier item**, not when it is first discovered.
- A* core `g/h/f` definitions, lowest-`f` selection and `h=0 -> UCS` were retrieved correctly after the UCS/A* contamination was corrected.

Guarantee analysis then moved forward. Admissibility was initially inverted, then transferred correctly on changed examples: `h(n) <= h*(n)`. Consistency was the main new/fragile concept and required repeated examples. The current useful model is:

```text
h(B)          = estimated cost still remaining
h(A) - h(B)   = estimated progress
c(A,B)        = actual cost paid

consistent when:
h(A) - h(B) <= c(A,B)
```

After this distinction landed, the learner correctly classified changed consistency examples, including equality, separated admissibility from consistency on an admissible-but-inconsistent example, and connected inconsistency with decreasing `f=g+h` along an edge.

Do not promote guarantee analysis to independent mastery: admissibility was initially inverted and consistency stabilised only after several same-session examples. Completeness/time/space complexity and the stronger consistency→admissibility relationship remain open.

Next search block: briefly cold-check UCS goal-popped, admissibility direction and consistency intuition, then continue with A* assumptions/optimality and completeness/time/memory complexity. Do not replay BFS/DFS. After Week-2 search pressure, shift JIT preparation toward Week-3 regression + decision trees/random forests; trees remain new material.

## Established foundations / remaining uncertainty

- **Python / NumPy / PyTorch:** Assignment 1 now has verified green implementations for pairwise vectorisation and no-loop bilinear interpolation. This is guided implementation evidence rather than delayed cold mastery; paired advanced indexing was reactivated on 21 Sep, while dtype/device/.to handling was newly taught.
- **Linear algebra:** historical JHU foundation established; retrieve selectively.
- **Probability/statistics:** strong historical evidence across major foundations; Markov chains/Poisson remain diagnostic-needed.
- **Calculus:** historical derivative/gradient/chain-rule/backprop foundation established.
- **Practical ML:** linear/logistic regression and train/validation/test workflow implemented; changed-task transfer still useful.
- **Agentic/LCEL:** stateful composition/gates have guided implementation evidence; routing conceptually retrieved; `RunnableBranch` implementation and later Tutorial 2 parts remain open.
- **January extensions:** likelihood/MLE, exponential families, formal generalisation/concentration, convergence assumptions and proof-style derivations remain new work.

## Handover discipline

After the next substantive assessed-work block, update the relevant focused log and this handover. Assignment 1 is submitted; do not reopen it merely to manufacture mastery evidence. Update `learning_progress.yaml` only when the structured learning-evidence state materially changes. Update `deadlines.yaml` whenever assessed-work dates/statuses change. Do not promote same-session corrected/guided tensor work to delayed cold mastery, and do not treat practice implementations as evidence that the actual assignment has been independently completed.
