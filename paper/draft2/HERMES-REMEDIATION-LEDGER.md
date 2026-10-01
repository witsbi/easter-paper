# Hermes Draft 2 Remediation Ledger

**Baseline:** frozen Draft 2 blind-review copy assembled from `70cf31a`  
**Blind reviewer:** Hermes  
**Adjudication:** Nathan + Sol, followed by Pax evidentiary comparison  
**Rule:** missing historical evidence remains missing. Remediation may expose surviving evidence, clarify method, correct claims, or narrow conclusions; it must not reconstruct unrecovered historical classifications as if they had been preserved.

| Finding | Status | Change | Evidence / rationale |
| --- | --- | --- | --- |
| #1 Comparative result reproducibility | OPEN | Evidence/method pass required. Publish surviving derivations and mark irrecoverable mappings explicitly; do not fabricate missing primitive classifications. | Frozen adjudication; §6 already identifies aggregate-only and unrecovered material. |
| #2 “primitive GAP vector” label | OPEN | Replace with per-system aggregate GAP-count sequence/tuple in corpus order everywhere it occurs. | Coordinates correspond to six systems, not six primitives. |
| #3 Gateway authentication vs. kernel Authority | REMEDIATED | Rewrote §8.5–8.8. Expired `identity:pax` credential is now identified as a gateway authentication rejection before kernel delivery, not EASTER Authority enforcement. No kernel REJECTED Receipt is claimed for that attempt. | Pax first-party operational confirmation; consistent with §4.8 interface/kernel boundary. Commit `9342a7f`. |
| #4 Scope of uniform durable outcome recording | OPEN | Bound Receipt guarantee to operations that reach the kernel's receipt-capable admission path; explicitly exclude pre-kernel and catastrophic persistence failures. | Blind-review adjudication accepted quantifier defect. |
| #5 FAILED atomicity/durability | EVIDENCE CHECK | Document the actual implementation failure path only after verifying kernel code. Do not adopt a hypothetical savepoint or recovery-transaction design. | Frozen adjudication. |
| #6 Reverse-review operationalization | OPEN | Add coding/aggregation account and worked examples while distinguishing reconstructed publication method from procedures actually preserved in the historical reviews. | No retroactive procedural reconstruction. |
| #7 Public/immutable implementation evidence | OPEN | Publication packaging pass required. | Submission-readiness issue. |
| #8 Related-work primary literature/search protocol | OPEN | Expand primary-source bibliography and document search protocol. | Submission-readiness issue. |
| #9 Provenance primitive mapping | PARTIAL | §8 now explicitly limits the case to records actually preserved and no longer implies all six primitives are demonstrated by every event. A stable-ID event table remains to be built from surviving records. | Commit `9342a7f`; further evidence extraction required. |
| #10 DRC/EASTER separation wording | OPEN | State empirical result as one-way non-entailment/non-equivalence under applied classifications in this corpus; reserve separability for interpretation/hypothesis. | Frozen adjudication. |
| #11 “survived/challenged” inference | OPEN | Replace affirmative-survival language with archival statement: no preserved review artifact records a CHALLENGED disposition. | Absence of preserved CHALLENGED is not proof of exhaustive stress testing. |
| #12 Consequentiality boundary | OPEN | Distinguish domain consequentiality selected by userland from an operation submitted to EASTER's admission boundary. | Frozen adjudication. |
| #13 Authority/grant scope | OPEN | State precisely what current grants authorize; avoid implying kernel interpretation of application policy. | Frozen adjudication. |
| #14 Behavioral novelty conjunction | OPEN | Define conjunction behaviorally rather than requiring EASTER-named record types. | Frozen adjudication. |
| #15 Portability oracle | OPEN-STRENGTHEN | Define future experiment oracle, acceptable successors, constraints, baselines, and failure metrics. | Future-work strengthening. |
| #16 DRC falsifiability | OPEN-STRENGTHEN | Add negative/borderline specimen direction. | Future-work strengthening. |
| #17 “accountability machine” | OPEN-STRENGTHEN | Qualify immediately: mechanical inspectability/attribution, not moral/legal accountability, identity assurance, legitimacy, enforcement, or due process. | Reader-overreach risk. |
| #18 Machine-checkable contract | OPEN-STRENGTHEN | Add compact pre/postconditions or identify as conformance-suite work. | Strengthening, not architecture contradiction. |
| #19 Freeze wrapper | OPEN | Remove from future external/blind review copies. | Submission hygiene. |
| #20 Participant aliases | OPEN | Define aliases once and use consistently. | Submission hygiene. |
| #21 DRC notation | OPEN | Replace shorthand with prose: all three DRC categories were COVERED in all six systems. | Clarity. |
| #22 “source of truth” terminology | OPEN | Prefer authoritative reporting/record terminology where appropriate. | Aligns with truth boundary. |
| #23 Primitive capitalization | OPEN | Normalize convention. | Editorial. |
| #24 References submission readiness | OPEN | Immutable revisions, primary sources, public artifact locations, complete metadata. | Submission-readiness issue. |
| #25 Defensive repetition | OPEN | Consolidate repeated caveats without weakening claim boundaries. | Editorial pass. |

## Remediation discipline

1. Correct factual errors first.
2. Verify implementation claims against primary code before rewriting them.
3. Never infer a missing historical primitive classification from an aggregate count.
4. Distinguish historical review procedure from procedures introduced for publication reproducibility.
5. Keep the six-primitive architecture and frozen historical results closed unless surviving evidence directly contradicts them.
6. Every closed finding receives a concrete manuscript change and evidence/rationale in this ledger.
