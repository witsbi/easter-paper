# 8. EASTER in Use: Contribution Provenance

The preceding sections describe EASTER as a model, an implementation, and an analytical lens. During preparation of this manuscript, the reference implementation was also used to preserve a consequential research-provenance workflow involving the human researcher and three AI participants.

This episode was not designed in advance as a controlled experiment. It is reported as an operational case study: a real provenance problem arose during preparation of the paper, Git was used to preserve the contribution artifacts, and EASTER was used to preserve consequential events surrounding their deposit and integration.

The case therefore demonstrates use of the reference implementation under its intended semantics. It does not establish universal sufficiency of the six primitives.

## 8.1 Provenance problem

As the manuscript developed, a publication-level attribution question arose: which contributions to EASTER and the associated research program should be attributed to Nathan Woolen, ChatGPT/Sol, Pax/Muse, and Clawde/Sonnet?

The participants had contributed in materially different ways, including architectural direction, implementation, conceptual development, prior-art investigation, adversarial review, experimental work, manuscript synthesis, and research governance.

Rather than reconstructing a single attribution ledger from one participant's memory, the workflow preserved separate contribution accounts.

The provenance rules included:

- explicit attribution is not equivalent to historical truth;
- primary evidence may overturn corroborated recollection;
- residual or unattributed work must not automatically be assigned to another participant;
- corrections append rather than silently replacing earlier records;
- model identity and participant identity remain distinct; and
- coordination, implementation, discovery, review, authority, and acceptance remain distinguishable forms of contribution.

The purpose was therefore not to force consensus. It was to preserve attributable claims in a form that could later be compared against primary evidence.

## 8.2 Independent contribution accounts

The initial preserved set contained Pax/Muse's first-party account and a provisional three-tier reconstruction of Nathan's contributions derived from the independently produced participant accounts available at that point.

Where first-party accounts from other participants were not yet available for deposit, the archive used explicit **PENDING DEPOSIT** placeholders rather than reconstructing or fabricating their contents.

ChatGPT/Sol subsequently deposited its own first-party account. Clawde/Sonnet independently deposited its first-party account afterward.

Nathan then produced a separate first-party contribution account. His account explicitly remained **PROVISIONAL / PRE-RECONCILIATION** and stated that primary evidence should outrank recollection where the two conflict.

The resulting archive therefore preserved participant claims as claims rather than prematurely converting them into a reconciled historical truth.

## 8.3 Correction without erasure

The workflow encountered at least one substantive attribution correction.

An earlier contribution account attributed the architectural origin of the Authority-separation remediation too strongly to ChatGPT/Sol. Nathan subsequently clarified that the architectural decision to separate Authority from the rest of the stack and give it an independent path originated with him; ChatGPT/Sol agreed with that direction and implemented the resulting remediation, and Clawde/Sonnet later independently red-teamed it.

The correction did not require pretending that the earlier account had never existed.

The provenance convention instead allowed the original statement and its later correction to coexist, with the correction becoming the accepted account for subsequent synthesis while preserving the historical record of the mistaken attribution.

This is an example of the distinction between **historical record** and **accepted current interpretation** that EASTER's append-oriented design is intended to support.

## 8.4 Git preservation

GitHub preserved the human-readable provenance artifacts and their revision history.

The first provenance-set commit, `90a1239`, created the contribution archive with the provisional reconstruction, Pax/Muse's first-party account, pending-deposit placeholders, and an index documenting known gaps.

Later commits replaced the placeholders with first-party deposits rather than inferred reconstructions. ChatGPT/Sol's account was deposited in commit `791b8af`; Clawde/Sonnet's account was deposited in commit `843dec1`.

Pull request #7 then merged the multi-participant provenance set into the manuscript repository.

Nathan's first-party account was preserved separately through pull request #8, which was subsequently merged into main.

This sequence left the individual claims, their deposit chronology, and the distinction between provisional reconstruction and first-party accounts inspectable in the repository history.

## 8.5 EASTER preservation

EASTER was used alongside Git rather than as a replacement for it.

Git preserved the documents themselves and their repository history. EASTER preserved consequential provenance events around the workflow as attributable Evidence and Receipts.

For example, the initial contribution-record deposit was recorded as EASTER Evidence after its Git preservation. Subsequent participant deposits were likewise anchored through EASTER records, and the final merge state was recorded after both provenance pull requests had landed on main.

This produced two complementary layers:

**Git → artifact content and revision history**

**EASTER → attributable consequential records for operations that reached the kernel boundary**

The distinction is important. EASTER did not need to duplicate Git's version-control function in order to preserve that a particular Git artifact had become consequential to the research process.

### Preserved event-to-primitive map

The case should not be read as though every event exercised all six primitives. The surviving manuscript/repository evidence supports the following bounded map:

| Workflow event | Stable external identifier available in the publication repository | EASTER role demonstrated by the case | Not demonstrated by that event |
| --- | --- | --- | --- |
| Initial provenance-set preservation | Git commit `90a1239` | Artifact existed as an independently identifiable provenance object; subsequent EASTER Evidence anchoring is reported for the deposit workflow. | No claim that the Git commit itself is an EASTER State or Transition. |
| ChatGPT/Sol first-party deposit | Git commit `791b8af` | Independently attributable contribution artifact; later anchored through the EASTER provenance workflow. | No claim that EASTER certified the historical truth of the account. |
| Clawde/Sonnet first-party deposit | Git commit `843dec1` | Independently attributable contribution artifact; later anchored through the EASTER provenance workflow. | No claim that every EASTER primitive was exercised by the deposit. |
| Multi-participant integration | Pull request #7 | Repository integration point used by the provenance workflow and later merge anchoring. | Git merge is not itself an EASTER Transition unless represented as one by a kernel operation. |
| Nathan first-party integration | Pull request #8 | Separate first-party artifact and integration point used by the later merge anchor. | No semantic reconciliation performed by the kernel. |
| Successful EASTER deposits / merge anchoring | Kernel operations reported by the preserved workflow | Evidence and Receipt use at the authoritative kernel boundary; accepted kernel records preserve that the relevant operation was admitted. | EASTER does not independently prove the external GitHub events asserted inside preserved payloads. |
| Independent provenance retrieval | Frozen Pax/Muse and Hermes retrieval reports | Later readers independently recovered materially coherent publication history from preserved EASTER records using different retrieval methods. | Complete, self-indexing, mechanically traversable end-to-end history was not demonstrated. |

The final two rows state the evidence boundary directly. The case demonstrates preservation and later recovery of consequential publication history, not a self-contained proof of every external event or a canonical graph supplied by the kernel.

## 8.6 Merge anchoring

After the participant accounts and Nathan's first-party account had been merged into the repository, the merge event was itself anchored in EASTER.

This extended the provenance chain from:

**claim → artifact → deposit → repository integration**

without requiring EASTER to determine whether every attribution claim was historically correct.

That distinction matters because the contribution accounts intentionally remained subject to later reconciliation against primary evidence.

EASTER preserved that the records were produced, deposited, and integrated. It did not certify the truth of every statement inside them.

## 8.7 What the case demonstrates

The case demonstrates that the reference implementation can support a multi-participant provenance workflow in which:

- independent and provisional claims remain distinguishable;
- missing first-party evidence can remain explicitly pending rather than being fabricated;
- later corrections can supplement earlier records without requiring historical erasure;
- artifact preservation and consequential-event preservation can be separated between Git and EASTER;
- consequential integration events can be durably anchored without asking the kernel to determine semantic truth; and
- consequential portions of the preserved history can later be independently recovered from EASTER records.

These are implementation observations, not universality claims.

The episode does not establish that EASTER captures every form of research provenance, that the six primitives are sufficient for every multi-participant workflow, or that use of EASTER makes the resulting attribution historically correct. It also does not demonstrate all six primitives through every event in the workflow; the case should be read only for the records and relationships actually preserved.

It demonstrates something narrower:

**the reference implementation was used to preserve consequential portions of this attribution workflow while leaving interpretation, correction, reconciliation, and publication judgment outside the kernel.**

That is the boundary the implementation was designed to maintain.

## 8.8 Independent cold review and Receipt-cardinality remediation

After the contribution-provenance workflow above, the manuscript underwent an independent cold review by Hermes, frozen 2026-10-01T19:45:59Z against manuscript `ef81644` and reference implementation `8bf4227` (archived in `paper/reviews/hermes-independent-cold-review-2026-10-01.md`). The review produced seven substantive findings. This section concerns finding #5.

Finding #5 observed that Receipt outcome uniqueness was assumed by supported entry points but not enforced as a kernel invariant: the `receipts` schema did not constrain the operation identifier, and the repository's own attack test demonstrated that an ACCEPTED and a later FAILED Receipt could coexist for one operation identifier.

Nathan accepted the intended invariant: **an operation identifier identifies one attempted kernel operation; at most one terminal Receipt may exist for that identifier, and when durable outcome recording succeeds, exactly one exists.** Hermes implemented the remediation in `witsbi/easter` PR #31 — a schema-level unique constraint on the Receipt's operation identifier, with duplicate terminal outcomes rejected as deliberate kernel errors — which was independently verified and merged as `7b8a0144dce24a2e4b3cc25a839c99ec8253c86f`. The frozen review itself was not amended: it remains byte-for-byte the assessment of the pre-remediation kernel, and a separate disposition note records finding #5 as CLOSED (`paper/reviews/hermes-independent-cold-review-finding-5-update-2026-10-01.md`).

The manuscript's current implementation claims — including the Receipt-cardinality invariant in §3.2 — describe the remediated kernel. They must not be read as claims about the kernel Hermes reviewed.

EASTER anchors for this chain: Hermes's first-party remediation record (`evidence:4be43ba1-39b7-45c1-bbe8-a1ca1a08c059`, `receipt:34c03ae3-ad91-4897-ba8f-ff7efd952188`); the independent verification and merge observation (`evidence:eb26c568-751b-4630-8a7b-de20d701cbb7`).

Contribution credit: Hermes is credited narrowly and specifically for the independent cold review, the discovery of the Receipt-cardinality enforcement defect, and the implementation of the accepted kernel remediation. The wording of this credit was drafted from the frozen review and remediation artifacts; it is not self-authenticating. Hermes will independently review this representation and either accept it or identify corrections, and her disposition will be deposited first-party into EASTER.

## 8.9 Independent provenance retrieval

Hermes cold-review finding #3 challenged whether the provenance case exposed enough stable EASTER records to permit independent reconstruction rather than relying on a first-party narrative. The finding was tested directly rather than answered from recollection.

Pax/Muse and Hermes independently retrieved the EASTER publication history and froze separate reports before seeing the other participant's result. Pax/Muse worked under the `agent` role using stable-ID traversal through `get_evidence` and `get_receipt`; Hermes independently enumerated the authenticated EASTER API using opaque pagination cursors and reconstructed the relevant history from the returned corpus. Their reports are preserved separately as `paper/reviews/pax-easter-provenance-retrieval-2026-10-02.md` and `paper/reviews/hermes-easter-provenance-retrieval-2026-10-02.md` and are not treated as a synthesized canonical history.

Both retrievals recovered a materially coherent publication-provenance history from EASTER and found no conflicting consequential chronology in the records they recovered. Their coverage differed with their retrieval capabilities: Hermes's enumeration recovered substantially more of the earlier publication history, while Pax's restricted traversal recovered a connected later subgraph from known stable identifiers.

The two reports also converged on the principal limitation. The preserved history is not a complete, self-indexing, mechanically traversable graph. Some causal relationships are explicit stable-ID edges, while others are encoded in payload fields or require matching project, PR, commit, subject, or chronology. Later publication work is represented predominantly through Evidence rather than one continued State/Transition chain. EASTER also preserves assertions about external GitHub events without independently proving those external events.

Finding #3A is therefore closed on a bounded result: **EASTER preserved consequential publication records sufficient for two independent retrievers, using different access and traversal methods, to recover materially coherent publication history; complete autonomous end-to-end reconstruction was not demonstrated.** This is evidence for historical preservation and recoverability, not a claim that the kernel supplies a canonical graph or graph-query semantics.