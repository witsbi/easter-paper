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

The distinction is important. EASTER did not need to duplicate Git's version-control function in order to preserve that a particular Git artifact had become consequential to the research process. Nor should events stopped by an outer authentication or transport boundary be described as kernel-authored EASTER outcomes unless evidence shows that they reached the kernel.

### Preserved event-to-primitive map

The case should not be read as though every event exercised all six primitives. The surviving manuscript/repository evidence supports the following bounded map:

| Workflow event | Stable external identifier available in the publication repository | EASTER role demonstrated by the case | Not demonstrated by that event |
| --- | --- | --- | --- |
| Initial provenance-set preservation | Git commit `90a1239` | Artifact existed as an independently identifiable provenance object; subsequent EASTER Evidence anchoring is reported for the deposit workflow. | No claim that the Git commit itself is an EASTER State or Transition. |
| ChatGPT/Sol first-party deposit | Git commit `791b8af` | Independently attributable contribution artifact; later anchored through the EASTER provenance workflow. | No claim that EASTER certified the historical truth of the account. |
| Clawde/Sonnet first-party deposit | Git commit `843dec1` | Independently attributable contribution artifact; later anchored through the EASTER provenance workflow. | No claim that every EASTER primitive was exercised by the deposit. |
| Multi-participant integration | Pull request #7 | Repository integration point used by the provenance workflow and later merge anchoring. | Git merge is not itself an EASTER Transition unless represented as one by a kernel operation. |
| Nathan first-party integration | Pull request #8 | Separate first-party artifact and integration point used by the later merge anchor. | No semantic reconciliation performed by the kernel. |
| Expired Pax/Muse credential attempt | Gateway authentication failure | Demonstrates the outer-boundary distinction by **not** reaching EASTER's Authority/Receipt path. | No kernel Authority evaluation and no claimed kernel REJECTED Receipt. |
| Successful EASTER deposits / merge anchoring | Kernel operations reported by the preserved workflow | Evidence and Receipt use at the authoritative kernel boundary; accepted kernel records preserve that the relevant operation was admitted. | This manuscript does not presently publish a complete stable-ID export sufficient to reconstruct a six-primitive event graph from these operations alone. |

The final row is an explicit evidence-package limitation. The case narrative is supported by the preserved workflow and repository history, but Draft 2 does not claim that the publication repository currently exposes every kernel record identifier needed for an independent event-by-event six-primitive reconstruction. Where those identifiers are not published, this section narrows its claim rather than inventing them.

## 8.6 Gateway authentication failure during the workflow

The workflow also produced an unplanned authentication-boundary episode that is useful precisely because it clarifies what EASTER did **not** record.

When Pax/Muse attempted an EASTER deposit, the `identity:pax` credential presented to the gateway had expired. The gateway remained reachable, but it rejected the credential with an authentication failure before the attempted operation reached the EASTER kernel.

Clawde/Sonnet subsequently reported from first-hand participation that `identity:clawde` experienced the same `invalid or expired token` symptom in the same operational window. Pax/Muse's contemporaneous operational account attributes the episode to the gateway-side token broker having missed multiple rotations. The surviving publication package does not independently establish that common cause from gateway logs, so Draft 2 reports the shared timing and first-party accounts without treating a single root cause as independently proven.

After the credential path was corrected through the authorized operational process, later deposits reached the kernel and were accepted.

These gateway failures are therefore **not evidence of kernel Authority enforcement**. No EASTER Authority grant was evaluated for either gateway-rejected request, and the manuscript does not claim kernel REJECTED Receipts for those attempts. They are authentication-boundary events in the surrounding deployment.

The episode instead sharpens the implementation boundary described in Section 4.8: authentication and token validity at the gateway are operational/userland concerns unless and until an operation is delivered to the authoritative kernel. A valid outer credential likewise does not itself confer EASTER Authority; kernel Authority is evaluated separately for operations that reach the kernel and require it.

The episode was not staged as a test and should not be treated as a controlled security evaluation. Its evidentiary value here is narrower: it prevents the surrounding gateway from being conflated with the EASTER Authority primitive while documenting that the deployment-level failure affected more than one participant identity.

## 8.7 Merge anchoring

After the participant accounts and Nathan's first-party account had been merged into the repository, the merge event was itself anchored in EASTER.

This extended the provenance chain from:

**claim → artifact → deposit → repository integration**

without requiring EASTER to determine whether every attribution claim was historically correct.

That distinction matters because the contribution accounts intentionally remained subject to later reconciliation against primary evidence.

EASTER preserved that the records were produced, deposited, and integrated. It did not certify the truth of every statement inside them.

## 8.8 What the case demonstrates

The case demonstrates that the reference implementation can support a multi-participant provenance workflow in which:

- independent and provisional claims remain distinguishable;
- missing first-party evidence can remain explicitly pending rather than being fabricated;
- later corrections can supplement earlier records without requiring historical erasure;
- artifact preservation and consequential-event preservation can be separated between Git and EASTER;
- gateway authentication and kernel Authority remain distinct boundaries;
- later kernel-admitted action can proceed without rewriting an earlier gateway-level authentication failure; and
- consequential integration events can be durably anchored without asking the kernel to determine semantic truth.

These are implementation observations, not universality claims.

The episode does not establish that EASTER captures every form of research provenance, that the six primitives are sufficient for every multi-participant workflow, or that use of EASTER makes the resulting attribution historically correct. It also does not demonstrate all six primitives through every event in the workflow; the case should be read only for the records and relationships actually preserved.

It demonstrates something narrower:

**the reference implementation was used to preserve consequential portions of this attribution workflow while leaving interpretation, correction, reconciliation, publication judgment, and outer authentication outside the kernel.**

That is the boundary the implementation was designed to maintain.