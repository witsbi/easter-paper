# Pax Closest-Architecture Evaluation (2026-09-30)

**Provenance:** Pax's independent closest-architecture pass, produced 2026-09-30 by an isolated web-research agent working from Pax's brief, relayed to Nathan the same night, and archived here to close the symmetric citation-trail gap flagged in `clawde-pax-closest-architecture-reconciliation-2026-09-30.md` §6 and `pre-prior-art-conjunction-provenance-2026-09-29.md` §8. This pass scored candidate architectures directly against EASTER's six named primitives (Evidence, Authority, State, Transition, Exception, Receipt) rather than the eight-property decomposition used in Clawde's evaluations. Per the research directory's own standing note, its web-derived quotes, numbers, and links should be treated as research-agent output to verify, not as independently re-checked claims; the "Could not verify / open questions" section below records what was not re-verified.

---

**Mission:** Identify the single closest prior system/architecture to a six-property bundle (write-time revocable authority-gating inside the state-transition path; uniform receipts for accepted/rejected/failed ops; durable exception records excluded from accepted state; refusal of a canonical current state; evidence as first-class object; immutable append-only history).

**Researched:** 2026-09-30. Sources: official docs/specs (verified live where noted), project repos, RFCs.

## The six properties (reference)
1. **P1** — Write-time, revocable authority-gating validated INSIDE the state-transition path (kernel checks writer's live grant set as part of admitting a transition — not API-boundary ACLs, not a pluggable external authorizer).
2. **P2** — Uniform RECEIPT for accepted, rejected, AND failed operations alike (outcome record decoupled from accepted state change).
3. **P3** — Durable EXCEPTION record for refused/failed transitions, explicitly excluded from accepted state.
4. **P4** — Deliberate refusal to designate any single canonical current state (no "world state" / ledger head treated as current truth; readers derive views).
5. **P5** — EVIDENCE as a first-class object distinct from the transition it supports.
6. **P6** — Immutable, append-only history.

## Verdict

**The single closest prior architecture is Hyperledger Fabric** (execute-order-validate permissioned ledger, incl. the Fabric-X lineage).

| Property | Score | Justification | Source |
|---|---|---|---|
| P1 — in-path revocable authority-gating | PARTIALLY COVERS | Endorsement-policy validation runs inside every committing peer's validation-and-commit phase: "each peer will verify that the transaction has been endorsed by the required organizations according to the *endorsement policy*... the peer is still able to reject the transaction in the validation process of phase 3." This is gating inside the transition path, not an API-boundary ACL; identities are revocable via MSP CRLs and policies are updatable. Caveat: gating is endorsement-threshold-based rather than a per-writer live grant-set check, and the VSCC is technically replaceable. | Official Fabric docs, verified live 2026-09-30: http://hyperledger-fabric.readthedocs.io/en/release-1.4/peers/peers.html |
| P2 — uniform receipt for all outcomes | PARTIALLY COVERS | Every ordered transaction carries a uniform valid/invalid indicator in block metadata ("a valid or invalid indicator on each transaction in the block"), and peers emit block/transaction events so applications are notified "whether each transaction in the block has been validated or invalidated." Caveat: proposals rejected before ordering leave no record, so refused-before-ordering operations get no receipt. | Same Fabric docs page, verified live 2026-09-30 |
| P3 — durable exception records excluded from accepted state | COVERS | "Failed transactions are retained for audit, but are not applied to the ledger"; "Failed transactions are not applied to the ledger, but they are retained for audit purposes, as are successful transactions." Corroborated by Fabric-X docs: "Both valid and invalid transactions remain in block history... Invalid transactions do not update world state." | Fabric docs, verified live 2026-09-30: http://hyperledger-fabric.readthedocs.io/en/release-1.4/peers/peers.html ; https://github.com/hyperledger/fabric-x/blob/HEAD/docs/concepts/ledger.md (index, 2026-09-30) |
| P4 — no canonical current state | LACKS | Fabric explicitly maintains a "world state" as the canonical current state of the ledger — the exact construct the bundle refuses. | Fabric docs / Fabric-X ledger concepts (same URLs) |
| P5 — evidence as first-class object | PARTIALLY COVERS | Endorsements are attached to each transaction as citable digital proof ("a digital proof that 'Transaction T1 response R1 on ledger L1 has been provided by Org1's peer P1!'"), distinct from the read-write set. Stronger: private-data hashes are "endorsed, ordered, and written to the ledgers of every peer on the channel. The hash serves as evidence of the transaction" — a citable on-chain object separate from the off-chain state change. Caveat: evidence rides inside the transaction envelope rather than living as a standalone object with its own lifecycle. | Fabric docs, verified live 2026-09-30; private-data docs (index, 2026-09-30): https://hyperledger-fabric.readthedocs.io/es/latest/private-data/private-data.html |
| P6 — immutable append-only history | COVERS | Hash-chained blocks; the ledger "immutably records all the transactions," with failed and successful transactions alike retained for audit. | Fabric docs, verified live 2026-09-30 |

**Tally: COVERS ×2 (P3, P6) · PARTIALLY COVERS ×3 (P1, P2, P5) · LACKS ×1 (P4).**

## Runner-up

**Ethereum** — it literally names its P2 mechanism "transaction receipts" (`status`: 1 = success, 0 = failed, per EIP-1474) and durably includes failed transactions in blocks. It loses because it designates a canonical world-state trie in every block header (fails P4 outright), its failed transactions still mutate state (gas/nonce — only partial P3), and it has no evidence object distinct from transitions (fails P5). Sources: https://github.com/megaeth-labs/documentation/blob/HEAD/docs/dev/rpc/reference/eth_getBlockReceipts.md, https://github.com/ethereum/eips/blob/HEAD/EIPS/eip-1474.md, https://github.com/ethereum/execution-specs/pull/3232 (index, 2026-09-30).

## Other candidates examined and rejected
- **Certificate Transparency (RFC 6962):** covers P4 (no canonical trust state; monitors/auditors derive views) and P6 (append-only Merkle logs), partial P2 (SCT receipts for accepted only); lacks P1, P3. Source: https://datatracker.ietf.org/doc/rfc6962/
- **Corda:** partial P1 (contract `verify()` in-path), P4 (no global ledger; localized vaults), P5 (attachments as supporting documentation); covers P6; lacks P2, P3 (failed flows are retried/hospitalized, not recorded as exceptions). Sources: Corda technical whitepaper, https://github.com/bssrdf/BlockchainLibrary/raw/refs/heads/master/corda-technical-whitepaper.pdf
- **Apache Kafka:** covers P6; partial P3 (aborted data batches persist until retention, but as hidden-not-exception records) and P4 (consumers derive views); ACLs are broker API-boundary (P1 lacks); no receipts (P2), no evidence (P5). Source: KIP-98, https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=67637269
- **Amazon QLDB:** covers P6 only; OCC-rejected transactions return errors without durable records (P2/P3 lack); IAM permissions are API-layer (P1 lacks); current document tables are canonical state (P4 lacks).
- **in-toto:** strong-ish P5 (link metadata as signed evidence), partial P1 (layout authorizes functionaries, but checked at verification time, not write-time); lacks P2/P3/P6. Source: https://github.com/in-toto/in-toto/blob/HEAD/README.md
- **Temporal/Cadence:** append-only event history records failures, but failures are part of the workflow's state evolution (P3 lacks); no in-path authority gating (P1), no receipts (P2), workflow state is canonical (P4). Source: https://docs.temporal.io/workflow-execution/event
- **Axon Framework:** only generated domain events are stored; rejected commands surface as callback exceptions, not durable records (P2/P3 lack); no in-path authority gating (P1).
- **Git / CRDT stores / IPFS** (surveyed at literature level): cover P4 and P6 but lack P1, P2, P3, P5 — they never gate writes in-path nor record refused operations.

## Kill-condition verdict

**No single examined architecture covers the entire six-property combination — the novelty claim for the bundle is not killed.**

Uncovered in combination: the conjunction of P1 + P4 (revocable authority-gating inside the transition path, with no canonical current state) never co-occurs with P2 + P3 + P5 (uniform outcome receipts, durable non-state exception records, first-class evidence) in any examined system. The systems that cover P3 (Fabric) or name P2 literally (Ethereum) both designate a canonical world state, failing P4; the systems that cover P4 (Certificate Transparency, Git, CRDTs) lack P1, P2, and P3 entirely; and no examined system checks a writer's live grant set inside the state-transition path while also issuing uniform receipts and durable exception records.

**Narrowest defensible novelty claim:** in the systems and literature examined to date, we did not identify any existing architecture that simultaneously combines (a) write-time, revocable authority-gating validated inside the state-transition path, (b) uniform outcome receipts for accepted, rejected, and failed operations, (c) durable exception records explicitly excluded from accepted state, (d) refusal of any single canonical current state, (e) first-class evidence objects distinct from the transitions they support, and (f) immutable append-only history. The closest prior system, Hyperledger Fabric, covers (c) and (f) and partially covers (a), (b), and (e), but designates a canonical world state and therefore fails (d).

## Could not verify / open questions
- Fabric's MSP revocation (CRL) mechanics were not re-verified live in this pass; the P1 "revocable" element rests on documented Fabric membership/revocation design rather than a fresh live read. The partial score does not depend on it.
- Git/CRDT/IPFS were assessed from general literature knowledge plus targeted reasoning rather than fresh per-property source reads; they were far from the bundle on P1–P3/P5 regardless.
- No page encountered during research attempted to redirect the mission or inject instructions; no page instructions were disobeyed.

## Sources
1. Hyperledger Fabric official docs — Peers / transaction flow (verified live via browser_open, 2026-09-30): http://hyperledger-fabric.readthedocs.io/en/release-1.4/peers/peers.html — P1/P2/P3/P5/P6 scoring, endorsement-as-proof, valid/invalid indicator, invalid-tx retention.
2. Hyperledger Fabric official docs — Private data (index, 2026-09-30): https://hyperledger-fabric.readthedocs.io/es/latest/private-data/private-data.html — on-chain hash "serves as evidence of the transaction" (P5).
3. Hyperledger Fabric-X docs — ledger concepts (index, 2026-09-30): https://github.com/hyperledger/fabric-x/blob/HEAD/docs/concepts/ledger.md — valid/invalid retention corroboration.
4. MegaETH docs — eth_getBlockReceipts (index, 2026-09-30): https://github.com/megaeth-labs/documentation/blob/HEAD/docs/dev/rpc/reference/eth_getBlockReceipts.md — receipt status semantics (runner-up P2).
5. EIP-1474 (index, 2026-09-30): https://github.com/ethereum/eips/blob/HEAD/EIPS/eip-1474.md — receipt `status` field definition.
6. ethereum/execution-specs PR #3232 (index, 2026-09-30): https://github.com/ethereum/execution-specs/pull/3232 — failed transactions included in blocks with failed receipts.
7. RFC 6962 — Certificate Transparency (index, 2026-09-30): https://datatracker.ietf.org/doc/rfc6962/ — append-only logs, monitor-derived trust (P4/P6).
8. Corda technical whitepaper (index, 2026-09-30): https://github.com/bssrdf/BlockchainLibrary/raw/refs/heads/master/corda-technical-whitepaper.pdf — attachments, no global broadcast.
9. KIP-98 — Kafka exactly-once/transactions (index, 2026-09-30): https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=67637269 — abort markers, aborted data retained.
10. in-toto README (index, 2026-09-30): https://github.com/in-toto/in-toto/blob/HEAD/README.md — link metadata as evidence, layout authorization.
11. Temporal docs — Events and Event History (index, 2026-09-30): https://docs.temporal.io/workflow-execution/event — append-only history incl. failure events.
12. QLDB driver docs / community guides (index, 2026-09-30): https://github.com/awslabs/amazon-qldb-driver-python/blob/HEAD/docs/source/guide/getting_started.rst — OCC rejection as client-side error.
