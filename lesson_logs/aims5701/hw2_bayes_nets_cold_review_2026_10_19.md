# AIMS5701 — HW2 Bayes Nets I cold review and Q5 preparation — 19 October 2026

## Scope and assessment boundary
A long tutoring session used **fresh analogue graphs and CPT values**, not answers to the assessed HW2. The provided HW2 sheet (due **21 Oct 2026**) was used to map the demands of Q1–Q6. Lecture 3 terminology was checked against the lecturer's deck: **causal chain**, **common cause**, **common effect (v-structure)**. Q5 and Q6 actual homework calculations/listing remain unattempted in this session. Retain original AI conversation/transcript for assignment disclosure; this log is a handover, **not** a substitute for the required original transcript.

## Observed evidence — distinguish independence from guided work

| HW2 area | What the learner demonstrated | Boundary / next check |
|---|---|---|
| Q1 probability | Reconstructed the 4-variable general chain rule on a fresh order after initial extra-factor/BN independence confusion; completed a diagnostic Bayes posterior with base-rate interpretation after repairing the neglected complement. | The **proof/derivation** of the 3-variable chain rule from the product rule has not been independently checked. |
| Q2 factorization and inference | Correctly read parents on a fresh branched graph. On a completely fresh 4-node ventilation problem, independently calculated the intermediate marginals and posterior on paper, confirmed from a photo. A chat transcription had a wrong conditional factor, but learner clarified correctly written notebook factorization. | The exercise scaffold gave intermediate queries in the same order as HW2 Q2. Planning a posterior without supplied intermediate queries was **partially guided**: root prior and denominator identified, but a two-edge likelihood needed help constructing. Intermediate sums should appear in assessed write-up. |
| Q3 parameter counting | Correctly reasoned 1 free parameter per binary CPT row, 4 for a child with 2 binary parents, and used 2^4+4 = 20 on a fresh 4-parent/root scenario. Correctly compared causal and reverse two-node structures for expert elicitation. | One slip used exponent = number of nodes rather than number of parents; repaired to 2^k for k binary parents. No need to overdrill, but double-check count. |
| Q4 d-separation | Repeatedly correctly classified causal chains, common causes and common effects; reasoned about collider-descendant evidence and multi-path activity. Final changed direct-edge graph correctly identified a blocked path and an unblocked direct path. One final mixed graph was fully correct on paper (learner report), despite mistyped chat conclusion. | Under load sometimes swapped fork/common cause with collider/common effect, changed the queried pair, or reversed active-path vs guaranteed-independence conclusion. Use a per-path middle-node table; keep target pair fixed. A later cold multi-path check would establish retention. |
| Q5 numerical inference | Completed *guided* chain marginalization through hidden states after losing connection between intermediate computations and the target. Followed and reproduced visual slider walkthroughs of (i) two independent causes -> common effect, 4 weighted rows, and (ii) common cause -> two observed effects -> posterior. Learner spontaneously recognized the double sum maps directly to table columns and rows. | **No independent unseen two-cause marginalization or two-evidence posterior yet; no five-node combined inference attempted.** Do not label as independent competence. |
| Q6 structural independence | Reviewed homework's requirement: local Markov rule and **exhaustive** list of pairwise d-separations over unordered pairs and conditioning subsets. Learner proposed systematic path enumeration and understands direct-edge shortcut. | No complete fresh four-node enumeration or local-Markov statement independently demonstrated today. |

## Tutoring and representation calibration — materially important
- Learner's successful shortcut from graph to a reduced marginal formula was valid; insistence on deriving a full four-variable joint was an unnecessary detour. Prefer **correct efficient calculation + sufficient working for marks**, not compulsory maximal algebra.
- Concrete, **fully visible CPT tables** are much easier to follow than abstract conditional notation or scrolling to old tables. Repeat all relevant CPTs with each independent task.
- Strong preferred method: **formula -> table (each factor = column, each hidden-variable assignment = row) -> multiply within rows -> sum rows -> posterior**.
- **Interactive slider walkthroughs** were a breakthrough: fixed target/query, color-highlighted CPT entries, one calculation per slider stage, and a persistent ledger tying all values to numerator/denominator. User followed and reproduced both 3-node worked examples. This supports comprehension, not yet cold transfer.
- Do **not** narrate each intermediate calculation as an unrelated prompt; show the entire target and outline the dependency plan once, then reveal steps. Avoid long strings of micro-questions. If an image/graph is rendered, ensure diagram is clear (diamond with distinct arrows when appropriate), mathematical notation compiles, and symbols match the actual query.
- Distinguish genuine handwritten reasoning from chat transcription slips; do not convert every typing mistake into a conceptual deficit. Correct path bookkeeping still matters. User reported fatigue late in session.

## Next session plan (20 Oct) — user-chosen
1. **Two common-cause (fork) exercises:** first with today's notes visible, then **fresh without notes**.
2. **Two common-effect (collider) exercises:** first with notes, then **fresh without notes**.
3. If the cold transfers work, one **integrated five-node cause/evidence graph** with a slider walkthrough; then a fresh independent planning-and-table attempt at approximately Q5 difficulty.
4. Bounded Q6 independent enumeration on a *different* four-node graph plus short Q1 chain-rule derivation check.
5. Only afterwards begin actual assessed HW2 as independently authored solutions, checking deadline **21 Oct** and preserving AI acknowledgement/unedited transcripts. Delivery urgency is **not** evidence of mastery. Leave Lecture 4 full variable elimination/sampling/HMM outside this HW2 review unless needed.

## Evidence labels
- Cold/independent: fresh 4-node Q2-style factorization and numerical results, many Q4 local-path answers; later same-session fresh Q4 multi-path checkpoint.
- Independent after repair: changed binary marginalizations, parameter counts, common-cause/common-effect rules.
- Guided: multi-edge hidden-variable posterior planning, chain propagation, and both slider examples.
- Not yet demonstrated: unguided integrated Q5, full Q6 enumeration, Q1(a) formal derivation, delayed retention of today's d-separation corrections.
