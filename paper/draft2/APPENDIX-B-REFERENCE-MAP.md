# Appendix B. Publication Reference Map

This appendix maps the manuscript's externally grounded architectural claims to the verified bibliography in §13. It is intentionally separate from the historical-source record: Appendix A and the archived review artifacts describe what the original research pass preserved, while this appendix identifies authoritative publication references a reader can use to inspect the claims now.

## B.1 Comparative corpus navigation

| Manuscript target | Publication reference | Boundary |
| --- | --- | --- |
| Hermes Agent | [20] | Current official documentation for navigation; not an invented historical version pin. |
| OpenClaw | [21] | Current official session/memory documentation for navigation; historical review evidence remains Appendix A. |
| LangGraph | [22] | Current official documentation for navigation; historical review evidence remains Appendix A. |
| Anthropic Claude Agent SDK | [23] | Current official Anthropic agent-runtime documentation for navigation; historical aggregate remains unrecovered below system level. |
| OpenAI Agents SDK | [24] | Current official SDK documentation for navigation; historical owning primitive for the one-GAP aggregate remains unrecovered. |
| Google Antigravity | [25] | Current official documentation for navigation; historical six-family-to-three-GAP mapping remains unrecovered. |

## B.2 Related-work claim map

| §9 claim family | Primary / authoritative references |
| --- | --- |
| Hyperledger Fabric is a permissioned blockchain architecture with endorsement/validation, immutable transaction history, and a maintained world state | [1], [2] |
| Corda uses transaction-local state evolution, signatures/participants, attachments, and avoids a single globally broadcast ledger state | [3] |
| Holochain uses agent source chains, DHT validation, distributed authority, and non-global state; its design explicitly resists externally revocable authorship authority | [4] |
| W3C PROV provides an interoperable provenance model centered on entities, activities, agents, and their relations | [5], [6] |
| OAuth 2.0 provides delegated authorization rather than EASTER's continuity semantics | [7] |
| Capability systems are a mature prior architectural tradition for authority and protected object access | [8], [9] |
| Temporal represents durable execution through persisted workflow/event history and recovery | [10] |
| Kafka provides durable partitioned logs / ordered append-oriented record history | [11] |
| Axon provides event-store/event-sourcing infrastructure and transactional event publication | [12] |
| EventStoreDB is an event-sourcing database / event-store architecture | [13] |
| Git provides durable commit history and explicit branching without itself supplying the EASTER admission/outcome conjunction | [14] |
| CRDT literature provides non-centralized replicated-state convergence mechanisms and is relevant to the non-canonical-state neighborhood | [15] |
| Certificate Transparency provides append-only auditable logging | [16] |
| in-toto provides signed supply-chain provenance/attestation and verification | [17] |
| Ethereum provides durable transaction history/receipts together with protocol state; the Yellow Paper is retained as a historical architecture reference | [18] |
| Amazon QLDB provided immutable journal/ledger architecture and is retained as historical prior art despite end of service | [19] |

## B.3 EASTER implementation and evidence map

| Manuscript claim family | Immutable publication evidence |
| --- | --- |
| Reference kernel behavior, schema, transaction semantics, Authority behavior, tests | [26]; see `PUBLIC-ARTIFACT-MANIFEST.md` for pinned entry points. |
| Accepted remediated Draft 2 baseline and preserved research archive | [27] |
| Recovered six-system comparative state and explicit unknowns | [28], Appendix A |
| Pax/Muse prior-art methodology reconstruction | [29] |
| Clawde/Sonnet prior-art methodology reconstruction | [30] |
| Reconciliation that produced the four-property behavioral conjunction | [31] |
| Evidence that the conjunction's coarse properties predated the dedicated closest-prior investigation | [32] |

## B.4 Historical-versus-publication rule

A publication reference answers **where a reader can inspect an authoritative source now**. It does not answer **which exact source/version the historical reviewer inspected** unless the archive independently preserves that fact.

Accordingly:

- [20]–[25] must not be used to fill unrecovered historical version cells in Appendix A;
- [3] identifies the same Corda v1.0 whitepaper cited and quoted in the preserved closest-prior evaluation; using the authoritative R3-hosted copy for publication does not change the manuscript's statement about the historical access path used by Pax/Muse;
- [16] retains RFC 6962 because that specification family belongs to the historical search record even though RFC 9162 supersedes it; and
- [18] and [19] are explicitly historical architectural references whose current maintenance/service status is disclosed rather than hidden.

This map is intended to make Draft 2 adversarially reviewable before a target venue is selected. Venue conversion may replace bracket numbering/style mechanically, but it must preserve these evidence boundaries.