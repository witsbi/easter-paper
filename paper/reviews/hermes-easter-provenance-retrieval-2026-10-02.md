# Frozen independent retrieval report — `easter-paper` publication provenance

**Retriever:** Hermes (`identity:hermes`)  
**Frozen:** `2026-10-02T11:21:51Z`, before seeing the other participant's result  
**Frozen source-report SHA-256:** `e444560ba74be1372aa12a0923f964f35c6b7ae51d39baad991abe8c83b17339`  
**Archival note:** This repository copy adds only this metadata block; the findings and retrieval account below are unchanged from the hashed frozen source report.  

**Retrieval source:** authenticated EASTER API only  
**Retrieval identity:** `identity:hermes`  
**Retrieval mode:** read-only  
**Records enumerated:** 1 Authority, 45 States, 44 Transitions, 114 Receipts, 64 Evidence, 0 Exceptions  
**Freeze rule:** this report was written before seeing any other participant's retrieval result.

## Method

I enumerated every page returned by `list_records` for Authority, State, Transition, Receipt, Evidence, and Exception, following the API's opaque `next_after` cursors. I did not use GitHub, repository files, prior conversation summaries, or another participant's reconstruction to construct the history below.

I identified candidate paper records from payload fields such as `project`, `repo`, `subject`, commit/PR references, and explicit stable-ID references. I then followed three kinds of relationships actually present in the returned graph:

1. structural State/Transition edges (`from_state_id`, `to_state_id`, `transition_id`);
2. Receipt links (`receipt.transition_id`, and `receipt.payload.evidence_id` for `RECORD_EVIDENCE` operations);
3. explicit stable identifiers embedded in Evidence payloads (`prior_evidence`, `prior_evidence_chain`, `snapshot_evidence_id`, `related_evidence`, and named Evidence/Receipt/Operation IDs).

Chronology below uses EASTER `created_at`, not payload-authored dates, except where noted. Payload claims about GitHub or off-EASTER activity are reported as claims preserved by EASTER, not independently verified facts.

## Reconstructed history

### 1. Early draft, challenges, and first blind review

EASTER preserves a Draft 0.2 deposit at commit `3769eb6`:

- Evidence `evidence:3e0b0224-b784-4edc-ae48-32132e82ad78`
- creation Receipt `receipt:7806b35c-1c93-4b7b-b773-af02d2fcf835`
- operation `operation:aaed6263-62d2-42f2-a8f9-a2e046560403`

Two challenge records follow, both referring to that draft commit:

- Pax shadow review: `evidence:c6c06502-60f6-4c51-83b0-98852a10b39f`; Receipt `receipt:5cf0659a-1bf1-4229-82b6-278c7bc3aa20`; operation `operation:0df326d7-8c50-4bc6-80b8-6de976b77836`.
- Ori adversarial pass relayed by Mercury: `evidence:32475dd3-d26f-4284-941d-7fb3a695a05d`; Receipt `receipt:b624cf4c-c085-44d4-ab54-1963740cf2d9`; operation `operation:4e274095-fedb-47df-96c8-75426ecb0b95`.

A remediation branch record follows as `evidence:f20a3fb9-c5ca-469a-a73b-9768e8da1469` (`paper-transition`, commit `ab332c6`), but its payload does not cite the two challenge Evidence IDs. I place it after them because it names the same review round and describes changes responsive to their subject matter; that is semantic/chronological inference, not an explicit graph edge.

A blind-review chain is directly recoverable:

- review snapshot: `evidence:10c617d9-ee60-4918-8b60-0e824c91d661`; Receipt `receipt:9252f9a3-46d2-4d64-8862-4c6ca10ce4d3`; operation `operation:3ef9b1db-d08f-41dc-80c1-2111a6b82922`;
- blind review: `evidence:53e0ae5e-04c6-4d2e-961a-639cdf82c6d7`; Receipt `receipt:3bdc616d-52cf-498a-99c5-f29e80c44460`; operation `operation:51dbfb20-9f87-4e38-a93d-c7923276`.

The review payload explicitly names `snapshot_evidence_id = evidence:10c617d9-ee60-4918-8b60-0e824c91d661`. A later role-transition record, `evidence:a3be2dba-5cbd-41f6-8726-ed97e18ed46a`, explicitly names the review Evidence ID and says the 11 findings remain blind-phase work. `evidence:7e1aa5b7-ed24-40fd-b978-76cd2b160fb9` separately reserves Hermes for a later cold read.

### 2. The only native `easter-paper` State/Transition chain

The first project anchor says earlier paper records were evidence-log-only. EASTER returns this accepted chain:

1. `state:genesis` → `state:8a1e0b4b-36ea-4e78-9b8e-4c8b9375c020` via `transition:1a5a0c70-6d55-4fa0-88c0-bf8c4d43b7e5`; accepted Receipt `receipt:6871aabc-36cc-4314-a513-7621b9897976`; operation `operation:34a1c698-6a70-4651-ba66-09270ad84dbd`. The State records Clawde's sighted Draft 2 archive/prior-art contribution at commit `2dbdbe3…`. Project-anchor Evidence: `evidence:a0344b8f-da3a-43bb-9142-fccea7ea6b58`.
2. `state:8a1e…` → `state:170498de-bf93-4fb7-b7c6-67f1577958dc` via `transition:1e680fbd-3a4b-44ae-9e3b-8a902996405b`; accepted Receipt `receipt:05729554-af3f-48df-8ffb-9c8854fc84ca`; operation `operation:d87d9119-3510-4478-ad5c-5f0e112d7e9e`. The State records pre-prior-art provenance archival. The anchor `evidence:2f5e0501-c41f-4c31-a5cd-33282357a534` explicitly cites substantive Evidence `evidence:e4567d2f-68e3-41d4-9956-a07b62462f65`.
3. `state:170498…` → `state:8d3c58ef-0b2c-439d-bbf6-47fa1432105c` via `transition:5e75ead8-1f9e-472f-9d70-153021aeecf7`; accepted Receipt `receipt:7e3efe72-b91e-41fe-bed7-ba84fac24d66`; operation `operation:2ceeaaaa-69a8-4e4c-83a5-b4f5f92bab86`. The State records preservation of the closest-prior-architecture stopping decision. Anchor `evidence:0736aabe-4cff-427e-855e-1cd3debe9642` explicitly cites vote/minutes Evidence `evidence:6967ff70-a780-4993-9b4d-e0ee5c7a30e9`, `evidence:faee2aa8-0500-49ee-b2c2-4073752c0ccd`, and `evidence:3f85abf2-e044-4761-b1fe-dacdb9f1d553`.

The vote records distinguish first-party, relayed, and aggregate minutes. Clawde's later first-party vote is `evidence:dd6370ff-e362-4525-a898-fb0526d6ce1e`, which references the resulting State ID but was not incorporated by another Transition.

No later `easter-paper` State or Transition was returned. Everything after this point is an Evidence/Receipt history rather than continuation of the native project State chain.

### 3. Contribution-provenance deposits and merge preservation

A recoverable Evidence chain records contribution-account deposits:

- initial set/deposit: `evidence:81933411-d51c-45fa-8417-b410b45da400`; Receipt `receipt:6bb45191-dada-49b3-99b2-9722d94b4002`; operation `operation:b66fa92d-301b-4a16-a9b3-98fab27b5eb4`;
- Sol amendment/deposit citing the initial record: `evidence:c87cfbbf-2e31-439c-a966-339cf71bb2c7`; Receipt `receipt:d3e5277c-1166-43c6-a758-b39ddb551fdb`; operation `operation:de4e9cf1-bbb1-4e1d-b621-21fc095ab704`;
- Clawde deposit citing the initial record: `evidence:71469a8f-a7ba-4a3a-923c-a85f9dd3b0c9`; Receipt `receipt:1553bd77-55cd-4c80-8533-6bdd004d0d8c`; operation `operation:b3ebd5b2-3cdb-4a78-a002-e66a7a43bea2`;
- Nathan first-party account citing the initial and Sol records: `evidence:0e8c5271-5a90-49e1-a514-e0a9c1f12acd`; Receipt `receipt:6f881234-db8c-4a86-b996-acbd1e9e6b25`; operation `operation:ce73e1ff-ff78-435d-b7b9-8e8717fda1a1`;
- Clawde's fuller first-party deposit cites the initial, Sol, and Nathan records: `evidence:b01e3f3d-69bd-4d95-85d6-6a8dc956c35d`; Receipt `receipt:f792a444-dbd0-48de-83fe-c8413f4d029d`; operation `operation:31732942-8eac-428a-a27b-fd62c28a8b15`.

The merge event `evidence:0680034d-d4f5-4ab6-ba08-e29ef3174e82` explicitly supplies that four-record `prior_evidence_chain`, PR numbers 7/8, merge commits, and main head `7836317`; Receipt `receipt:73a1abc1-48e6-4d1b-8c98-ea7989e6b853`; operation `operation:417be832-bb17-450d-9510-4f234c0ac6fd`. A near-duplicate observation, `evidence:1acf28fd-b9f7-4e9b-8e2c-43ce668c50b2`, reports the same merges but does not cite the merge-event Evidence ID.

### 4. Draft 2 verification and publication-package approval

EASTER preserves a contributor verification and addendum:

- remediation verification, verdict CLEAN: `evidence:1b2bdb47-092d-48fb-87d7-18e34a846873`; Receipt `receipt:acac02ec-96da-4b3d-8bde-73db7838ba3b`; operation `operation:0dda0855-9876-4209-94b7-8a2bad5487d0`;
- cleanup addendum: `evidence:0099390b-84c4-4175-ba25-3cf919f1b7e7`; Receipt `receipt:97993be5-b677-4cf2-b660-fbe6b59899f8`; operation `operation:80b6951d-8543-407e-85fc-0a32b24e97c0`.

The addendum explicitly cites the prior Evidence and Receipt IDs and says the residual notes were cleared. A comparison record, `evidence:4ff4edd5-8565-4acf-9aec-6e673d86f611`, later compares the contributor read with a Hermes blind review, but that referenced Hermes review is not itself present as a stable Evidence record at this point in the EASTER chronology.

Publication-package PR #13 has two disposition records and one merge record:

- Pax first-party APPROVE: `evidence:8aa854d4-4bf2-4c5f-ab0e-608c12d15200`; Receipt `receipt:21cfea62-8bd2-4e3f-b2d1-40a50397e8e6`; operation `operation:4cc4e7d2-0667-45b2-95f0-52eca2b690c3`.
- Ori approval relayed by Pax: `evidence:92cb01d0-84fc-4a66-974a-5e6c4201f3f6`; Receipt `receipt:cb884e82-e7ad-4081-a0b2-3b6dc5ba9684`; operation `operation:e955af48-d589-4b35-a44b-5ab0720bd048`.
- merge event naming merge `6386f992…`: `evidence:3159596f-846f-4243-9780-8a79cd25013c`; Receipt `receipt:a77c24d1-1066-475a-a0d8-8c83c854b1f0`; operation `operation:c84194aa-c858-4831-a421-b12d33e1bc3d`.

These three records share PR/head/finding semantics, but none explicitly cites the stable Evidence ID of another. Their linkage is therefore by payload keys and chronology, not a native edge.

### 5. Independent adversarial review, remediation, and closure

A frozen Clawde adversarial review is preserved as:

- `evidence:20e4722d-2cda-4074-a471-8d9920df00e5`
- Receipt `receipt:26c0c1b2-4a71-4897-a7da-3f289c918276`
- operation `operation:a75801ea-a5f8-4d09-9601-7eef3f9b0fe6`

Its payload names PR #14, commit `7b59e49`, six attack targets, and the reviewed manuscript/implementation pins.

The closure record is:

- `evidence:bb89a43f-63ba-44b9-af46-b8e92cbb2e86`
- Receipt `receipt:29f5b38b-9e74-43fc-99d9-d6ba4e13ba3f`
- operation `operation:52385dec-f5bb-4d76-9f87-df6d686070ca`

It explicitly cites `evidence:20e4722d-2cda-4074-a471-8d9920df00e5`, identifies remediation PR #15 and merge `0e6e06e…`, and says PR #16's verification merged as `ef81644…`. No separate EASTER Evidence record for PR #15's remediation was returned, so the middle remediation event exists only as an assertion inside the closure record.

### 6. Publication decision records

EASTER preserves a dissenting experiment-first vote as `evidence:cdd5f586-724e-45f4-86d0-8ac28013288d`.

A later preprint-first decision set contains:

- Pax first-party vote `evidence:6ffe936d-1a5c-4500-ad39-284f0d4f6bf4`; Receipt `receipt:90dcfdc0-6bde-4e3f-ba18-baa1a5a96b7d`; operation `operation:39d8885a-e166-4244-bc5e-a188af3faf9b`.
- Nathan/Ori votes relayed by Pax `evidence:55bf9569-596b-4028-b5e2-4ebb7e01772f`; Receipt `receipt:6b128a63-d883-477c-92f3-e4028faf0c2b`; operation `operation:d73c7997-8d9a-4964-afc5-c57ae07a5644`.
- tally `evidence:c76dba17-075f-4813-858f-7a9afa133236`; Receipt `receipt:d16cb16d-a2b2-4c5b-a693-84ba99d7380a`; operation `operation:253b0b03-1f4c-404c-a58a-df986d814fd7`.

The tally names the dissent and voters but does not cite their Evidence IDs. Its payload `recorded_at` is later than its EASTER `created_at`, an internal timestamp inconsistency that prevents treating payload time as authoritative ordering.

### 7. Hermes finding #5 remediation, review archival, and attribution closure

The remediation implementation report is directly preserved:

- `evidence:4be43ba1-39b7-45c1-bbe8-a1ca1a08c059`
- Receipt `receipt:34c03ae3-ad91-4897-ba8f-ff7efd952188`
- operation `operation:4bb08f01-7892-4ff7-8a0c-3e6e9b1f45c1`

It identifies Hermes as first-party implementer, EASTER PR #31, commit `3812cb1…`, test scope, historical-ledger check, and explicit non-self-certification.

Independent verification/merge is reported by:

- `evidence:eb26c568-751b-4630-8a7b-de20d701cbb7`
- Receipt `receipt:b928a6d3-2257-43dd-9399-6c6d012ae3a9`
- operation `operation:3384ecdc-1e0e-44e5-b8f7-bf2f650ab08c`

Its payload gives the review→reproduction→accepted-invariant→implementation→independent-verification→merge narrative and merge `7b8a0144…`. It does not cite the remediation Evidence ID, so the relationship to `evidence:4be43…` is by matching PR/commit/author and chronology, not an explicit stable-ID edge.

The frozen-review archive record is:

- `evidence:a7a9b781-4e1d-47e8-9be7-32b8e4393b47`
- Receipt `receipt:4504f15d-bcd5-41ce-9f37-422cd22da925`
- operation `operation:6702bd6d-b7ec-4481-bac8-13a20ad8e4e9`

This record explicitly cites the remediation Evidence, Receipt, and Operation, plus `evidence:eb26c568…`; it preserves manuscript/implementation pins and review SHA-256 and says finding #5 is closed while others remain open.

Finally, Hermes's first-party attribution disposition is:

- `evidence:3bb4641f-d80f-4976-b363-f2db5462a788`
- Receipt `receipt:8046ce5c-3fff-4e6e-bf1d-185f381ee510`
- operation `operation:2cd9d214-3c21-41d0-8cb5-5d79e2608b7e`

It explicitly cites `evidence:4be43…`, `evidence:eb26c568…`, and `evidence:a7a9b781…`, accepts the narrow attribution at PR #18 head `dcb227b…`, and preserves the finding-status boundaries.

## Traversal assessment

### Relationships that worked directly

- Every consequential Evidence record above could be tied to an ACCEPTED `RECORD_EVIDENCE` Receipt and operation ID through `receipt.payload.evidence_id`.
- The three-State paper chain was traversable structurally through `from_state_id`/`to_state_id`, `transition_id`, and `receipt.transition_id`.
- Several later Evidence chains used explicit stable references effectively: snapshot→blind review; review→role transition; provenance record→project anchor; vote Evidence→decision anchor; initial contribution deposits→merge event; remediation verification→addendum; adversarial review→closure; remediation/archive records→attribution disposition.

### Relationships that could not be followed directly

- The native `easter-paper` State/Transition chain stops at `state:8d3c58ef-0b2c-439d-bbf6-47fa1432105c` on 2026-09-30. None of the October publication work is connected to it by a Transition.
- EASTER returned no generic project membership/index edge. Discovery required scanning payload text and interpreting fields such as `project`, `repo`, PR number, commit, and subject.
- The API surface used here did not expose Receipt–Evidence citation junctions; only Evidence-creation relationships encoded in Receipt payloads were directly available.
- Several apparent chains have no stable-ID edge: early challenges→remediation branch, PR #13 approvals→merge, Hermes remediation report→independent verification record, decision votes→tally, and duplicate contribution-merge observations.
- PR #15 remediation has no separate returned Evidence object; it is only named inside the later closure record.
- The Hermes cold review referenced by `evidence:4ff4edd5…` was not itself deposited at that point; only the later archive record supplies a stable review hash and repository path.

## Ambiguities, conflicts, and orphans

1. **Two layers of history coexist.** There is one short authoritative State/Transition chain and a much larger Evidence log. EASTER does not designate a canonical publication-history tip across the latter.
2. **Chronology is not causality.** Many links required shared PR/commit/subject semantics plus `created_at`; those are plausible but not structural edges.
3. **Relayed records are clearly labeled but not first-party.** Ori and Nathan approvals/votes are often preserved by Pax or Mercury relay. EASTER persistence proves the record exists, not that the attributed person authored or approved it.
4. **Duplicate/parallel observations exist.** `evidence:0680034d…` and `evidence:1acf28fd…` both report the contribution-provenance merges without linking to each other.
5. **Payload-time inconsistency exists.** The preprint vote set has EASTER creation times around `20:15Z` but payload `recorded_at` values around `20:35Z`; kernel creation order is recoverable, but the userland timestamp story is ambiguous.
6. **No Exceptions were returned.** This retrieval found no failed/rejected diagnostic branch relevant to the paper history.
7. **External claims remain assertions.** Commit hashes, PR states, review contents, test outcomes, and merge facts are recoverable as payload claims but cannot be proven solely from EASTER without consulting the referenced repositories/artifacts.

## Judgment

**EASTER alone was sufficient to recover a materially coherent high-level publication-provenance history, but not a complete or mechanically traversable one.**

It was sufficient to recover the major phases—draft/challenge, blind review, a short anchored project chain, contribution-provenance deposits, Draft 2 verification, publication-package approvals/merge, adversarial review/remediation closure, publication decision records, and Hermes finding #5 remediation/verification/archive/attribution closure—with stable Evidence IDs and accepted Receipt/operation provenance.

It was not sufficient to reconstruct every causal step by graph traversal alone. The decisive weakness is that most later publication history is an Evidence log whose relationships are optional userland payload conventions. Several consequential links are implicit, duplicated, relayed, or represented only by a later summary/closure object. The recovered history is materially coherent as an auditable index of claims and artifacts, but it is not a self-contained proof of those claims and does not provide a single authoritative end-to-end publication chain.
