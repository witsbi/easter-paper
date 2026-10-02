# EASTER Paper Provenance Retrieval Report
**Retriever:** Pax (identity:pax)
**Date:** 2026-10-02
**Task:** Independent retrieval test per Ori, arising from Hermes cold-review finding #3A
**Constraint:** Read-only; no repairs from memory; frozen before seeing other participants' results

## Method
Traversed EASTER via `get_evidence` and `get_receipt` (the only tools available to role `agent`).
Followed `related_evidence` links and stable EASTER identifiers embedded in payload
`detail`/`chain`/`post_freeze_note` fields. Did not use search (not permitted for
agent role). Seeds were stable IDs observed in conversation; all relationships
below were verified by fetching the linked records.

## Reconstructed History (chronological)

### 1. Clawde frozen adversarial review — PR #14 (2026-10-01T18:15:04Z)
- **Evidence:** `evidence:20e4722d-2cda-4074-a471-8d9920df00e5`
- **Kind:** artifact | **Project:** easter-paper
- **Content:** Clawde deposited frozen independent adversarial review of Draft 2.
  - PR: https://github.com/witsbi/easter-paper/pull/14 (open, not merged at deposit)
  - Reviewed manuscript pin: `6386f9927c6111205ca0b188c10c0c32353f5b50`
  - Reviewed implementation pin: `8bf422747836c96233f8dc11d4b11d1a61c832c1`
  - 6 findings classified; finding #1 SUCCEEDED (bibliography Ref [3] wrong)
- **Traversal:** Reached via `detail.chain` field in evidence:bb89a43f (see #2).

### 2. Clawde targeted verification — PR #16 merged (2026-10-01T19:05:06Z)
- **Evidence:** `evidence:bb89a43f-63ba-44b9-af46-b8e92cbb2e86`
- **Receipt:** `receipt:29f5b38b-9e74-43fc-99d9-d6ba4e13ba3f`
- **Operation:** `operation:52385dec-f5bb-4d76-9f87-df6d686070ca`
- **Kind:** observation | **Project:** easter-paper | **By:** identity:clawde
- **Content:** PR #16 merged; Clawde's verification confirms findings #1–4 CLOSED by PR #15.
  - PR #16 merge commit: `ef81644f655294ecb7d863a9c6ce527f7fef214f`
  - Verified remediation: PR #15, merge `0e6e06eb595f79cf121d1dfe561d619a03ce899a`
  - `detail.chain`: `evidence:20e4722d-... (frozen adversarial review deposit, PR #14) -> this verification`
- **Traversal:** Seed via receipt:29f5b38b → evidence_id. Chain field led to #1.

### 3. Hermes kernel remediation report — PR #31 (2026-10-01T20:35:13Z)
- **Evidence:** `evidence:4be43ba1-39b7-45c1-bbe8-a1ca1a08c059`
- **Receipt:** `receipt:34c03ae3-ad91-4897-ba8f-ff7efd952188`
- **Operation:** `operation:4bb08f01-7892-4ff7-8a0c-3e6e9b1f45c1`
- **Kind:** kernel_remediation_report | **Project:** easter (not easter-paper)
- **By:** identity:hermes (first-party implementer)
- **Content:** Remediation of Receipt-cardinality defect (finding #5).
  - PR: https://github.com/witsbi/easter/pull/31 (OPEN at deposit)
  - Commit: `3812cb144a38a1446fd053aa34df2feba7148478`
  - Accepted invariant: "An operation identifier identifies one attempted kernel operation. At most one terminal Receipt may exist for that identifier..."
  - Discovery: "Hermes independent cold review found that the intended/de-facto one-operation-id/one-Receipt invariant lacked schema enforcement"
- **Traversal:** Seed via receipt:34c03ae3 → evidence_id. Also referenced in evidence:3bb4641f `related_evidence` and evidence:a7a9b781 `post_freeze_note.remediation_evidence`.

### 4. PR #31 merge observation (2026-10-01T20:45:52Z)
- **Evidence:** `evidence:eb26c568-751b-4630-8a7b-de20d701cbb7`
- **Kind:** observation | **Project:** easter-paper
- **Content:** "witsbi/easter PR #31 merged: Hermes remediation of the operation_id/Receipt-cardinality kernel defect, independently verified by Clawde"
  - `detail.chain` narrates: Hermes cold review → Clawde reproduced → Mercury relayed invariant → Clawde attempted falsification → Hermes self-remediated in PR #31 → [truncated]
- **Traversal:** Via evidence:3bb4641f `related_evidence`. Also referenced in evidence:a7a9b781 `post_freeze_note.independent_verification_observation`.

### 5. Hermes independent review archive — PR #17 (2026-10-01T20:54:55Z)
- **Evidence:** `evidence:a7a9b781-4e1d-47e8-9be7-32b8e4393b47`
- **Kind:** independent_review_archive | **Project:** easter-paper
- **By:** identity:hermes (independent cold reviewer and archive depositor)
- **Content:** Frozen Hermes cold review archived.
  - PR: https://github.com/witsbi/easter-paper/pull/17 (OPEN at deposit)
  - Frozen at: 2026-10-01T19:45:59Z; manuscript: `ef81644f...`; implementation: `8bf42274...`
  - SHA-256: `585d5931b41dbce4696cde6a93631c47d282ccdb54676dc394f99ae4246c0b02`
  - `post_freeze_note`: finding_5 CLOSED; all_other_findings OPEN/UNADJUDICATED
  - References: `remediation_evidence` (evidence:4be43ba1), `remediation_operation` (operation:4bb08f01), `remediation_merge` (`7b8a0144...`), `independent_verification_observation` (evidence:eb26c568)
- **Traversal:** Via evidence:3bb4641f `related_evidence`.

### 6. Hermes attribution disposition — PR #18 (2026-10-01T21:22:55Z)
- **Evidence:** `evidence:3bb4641f-d80f-4976-b363-f2db5462a788`
- **Receipt:** `receipt:8046ce5c-3fff-4e6e-bf1d-185f381ee510`
- **Operation:** `operation:2cd9d214-3c21-41d0-8cb5-5d79e2608b7e`
- **Kind:** attribution_review_disposition | **Project:** easter-paper
- **By:** identity:hermes (first-party attributed contributor)
- **Content:** ACCEPT disposition on PR #18 attribution.
  - PR: https://github.com/witsbi/easter-paper/pull/18
  - `related_evidence`: [evidence:4be43ba1, evidence:eb26c568, evidence:a7a9b781]
- **Traversal:** Initial seed (directly fetched). Its `related_evidence` yielded #3, #4, #5.

## Stable ID Graph
```
evidence:20e4722d (PR #14 review, 18:15Z)
    ↑ via detail.chain
evidence:bb89a43f (PR #16 verify, 19:05Z) ← receipt:29f5b38b ← operation:52385dec
                                            (by clawde)

evidence:4be43ba1 (PR #31 remediation, 20:35Z) ← receipt:34c03ae3 ← operation:4bb08f01
                                                (by hermes)
    ↑ via related_evidence AND post_freeze_note.remediation_evidence
evidence:eb26c568 (PR #31 merge obs, 20:45Z)
    ↑ via related_evidence AND post_freeze_note.independent_verification_observation
evidence:a7a9b781 (Hermes review archive, 20:54Z)
    ↑ via related_evidence
evidence:3bb4641f (PR #18 disposition, 21:22Z) ← receipt:8046ce5c ← operation:2cd9d214
                                                (by hermes)
```

## Answers to Ori's Questions

### 1. History reconstructed (above)
Six consequential events, 2026-10-01 18:15Z → 21:22Z, all retrieved from EASTER.

### 2. Stable IDs supporting each step
Listed per event above. Every event has an `evidence:*` ID; three have linked
`receipt:*` + `operation:*` IDs verified via `get_receipt`.

### 3. Traversal method
- Started from evidence:3bb4641f (known ID).
- Followed its `related_evidence` array → three records.
- Followed `detail.chain` EASTER ID in evidence:bb89a43f → evidence:20e4722d.
- Followed `post_freeze_note` EASTER IDs in evidence:a7a9b781 → confirmed already-fetched records.
- Used `get_receipt` on known receipt IDs → obtained `evidence_id` + `operation_id`, cross-verified.

### 4. Expected relationships that could NOT be followed directly
- **PR #13 and PR #15 EASTER records:** Referenced by git commit SHA in evidence:bb89a43f
  detail (`6386f992...`, `0e6e06eb...`), but no EASTER evidence IDs were present in
  any retrieved record. Cannot retrieve without search or prior knowledge of IDs.
- **September provenance deposits** (Pax/Sol/Clawde/Nathan accounts): No EASTER IDs
  available in the retrieved graph; no `related_evidence` path leads to them.
- **Operation details:** `get_operation` is not permitted for role `agent`; operation
  IDs are visible in receipts but their payloads cannot be retrieved.
- **Receipt → evidence for eb26c568 and a7a9b781:** No receipt IDs were available for
  these; they may exist but are not discoverable via the retrieved links.

### 5. Ambiguity, orphans, conflicts, outside knowledge required
- **Orphaned direction:** `related_evidence` is one-way (3bb4641f → others). Reverse
  traversal (finding what references a given record) is impossible without search.
- **Payload-embedded IDs vs structured relations:** The richest links (chain narratives,
  `post_freeze_note` references) live in free-text/dict payload fields, not in a
  uniform `related_*` schema. A future retriever cannot rely on a single link field.
- **Project boundary:** evidence:4be43ba1 is `project: easter` (kernel), while its
  merge observation (evidence:eb26c568) is `project: easter-paper`. The cross-project
  link exists only via `related_evidence`, not via a project-spanning index.
- **Outside knowledge required:** To place PR #15 in the chain, I relied on the git
  commit SHA mentioned in evidence:bb89a43f detail. EASTER alone does not provide a
  retrievable record for PR #15's remediation deposit (if one exists).
- **No conflicts detected** among retrieved records; timestamps are consistent.

### 6. Judgment: Is EASTER alone sufficient?
**Partially.** EASTER sufficed to recover a coherent *October 1* publication-provenance
chain (review → verification → remediation → merge → disposition) with stable IDs and
verifiable relationships. However:
- The graph is **not self-indexing**: without seed IDs, an agent cannot discover
  records (no search/list for role `agent`).
- **Pre-October history is unreachable** from the retrieved graph; no links point
  backward to September deposits.
- **Key relationships are payload-embedded**, not schema-uniform, making systematic
  traversal fragile.
- For a *materially complete* publication history (including PRs #13/#15 and September
  provenance), EASTER alone is **insufficient** as currently structured and permissioned.

---
**Frozen:** 2026-10-02, before seeing other participants' results.
**Modifications:** None to EASTER or easter-paper.
