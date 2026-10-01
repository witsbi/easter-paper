# 9. Related Work and Novelty Boundary

EASTER intersects several established architectural traditions. Individual EASTER properties appear in event-sourced systems, durable-execution engines, distributed ledgers, capability and authorization systems, provenance frameworks, version-control systems, and agent runtimes.

The claim of this paper is therefore not that immutable history, authorization, receipts, branching, provenance, or durable failure recording are individually new.

The relevant question is narrower:

**Do existing architectures examined in this research combine the particular continuity properties EASTER places together at one consequential admission boundary?**

We conducted a dedicated closest-prior investigation to test that question rather than treating absence from the initial agent-system corpus as evidence of novelty.

## 9.1 Search method and evidentiary warrant

The closest-prior work was a **bounded adversarial investigation, not a systematic or exhaustive literature review**. This characterization is supported by two independently deposited first-party methodology accounts and the contemporaneous research artifacts.

Two AI-assisted passes approached the question with different decompositions and different search shapes.

**Pax pass.** Pax designed a six-property rubric corresponding to the EASTER combination, an explicit kill condition, and a bounded research brief, then delegated web investigation to an isolated deep-research agent. The brief pre-identified Hyperledger Fabric as the lead candidate and named adjacent candidates including Ethereum, QLDB, Temporal/Cadence, Kafka, Git, CRDT stores, Certificate Transparency, TUF, Axon, and provenance/lineage systems. The research agent inspected documentation, specifications, repositories, RFCs, and related sources and returned a report that Pax reviewed. Pax did not personally re-open the twelve cited sources during that pass. The resulting investigation is therefore best described as a directed kill-attempt against a pre-named strong contender, not as an open-ended discovery survey.

**Clawde pass.** Clawde separately used a deep-research workflow for a broader prior-art investigation: six parallel research subagents examined pre-selected traditions including event sourcing/ledgers, durable execution/fault recovery, provenance, capability security, ER/type systems, and ontology/knowledge representation, followed by a synthesis agent. A later closest-architecture pass then examined Fabric and, reactively after Fabric's canonicality weakness became salient, Corda and Holochain. That later pass used an eight-property decomposition whose pre-use derivation artifact was not recovered. Whether the later Fabric/Corda/Holochain dispatch itself formally used the named deep-research skill is also unrecovered; its delegation pattern was similar, but the record does not justify treating that as confirmed.

The two passes were independent of one another in the relevant sense: their analyses were produced without either participant first harmonizing its result to the other's. They were **not independent of AI research tooling**, and most source reading occurred in delegated research contexts rather than being personally re-fetched by the orchestrating participant.

The passes were subsequently reconciled against their cited source claims. The preserved reconciliation records no material contradiction in the underlying primary-source facts; the principal difference was decomposition and weighting. The four-property behavioral conjunction reported below emerged from that reconciliation rather than from either pass alone.

This procedure supports a narrow warrant: strong pre-identified and adjacent candidate architectures were subjected to differently decomposed attempts to defeat the conjunction, and none of the examined systems did so. It does **not** support the claim that the literature contains no closer architecture or that the candidate space was exhausted.

### Source discipline

The investigations preferred primary technical sources where accessible: official project documentation and repositories, specifications and RFCs, project or vendor whitepapers, and academic papers. Preserved source records include, among others, Hyperledger Fabric documentation and source plus the EuroSys Fabric paper; the Corda technical whitepaper; the Holochain whitepaper and developer documentation; W3C PROV material; RFC 6749; primary capability-security literature; Temporal, Kafka, Axon, EventStoreDB, and Git documentation; and a formal CRDT treatment.

Primary-source access was not complete. The Pax pass used a third-party mirror for the Corda whitepaper. Clawde's pass records inaccessible or unparsed primary material in several areas and labels secondary or search-cache substitution rather than silently presenting it as direct primary inspection. Neither first-party account documents a primary-vs-primary factual conflict requiring adjudication.

The final submission bibliography should cite the authoritative original source for each manuscript claim where an equivalent accessible original can be verified. Replacing a historical mirror with an authoritative bibliographic citation improves the publication apparatus; it does not rewrite which source was actually inspected during the historical pass.

### Search limitations preserved rather than repaired retrospectively

The historical search has known holes. Pax's brief named TUF, OpenLineage, Marquez, DataHub, and Atlas, but the resulting report does not show whether those candidates were examined and rejected or never examined. Clawde's reconstruction identifies an unexamined class of permissioned distributed architectures combining hard revocable admission with non-canonical or sharded replication. Candidate selection was not governed by formal inclusion/exclusion criteria, database queries, citation chaining, or a PRISMA-like screening protocol. The work was time-boxed to essentially one evening.

These gaps are not filled retrospectively. A later search of them would constitute additional prior-art work, not recovery of the historical procedure.

## 9.2 Architectural neighborhoods

Several neighboring traditions overlap with EASTER while solving different primary problems.

**Event sourcing and durable execution** preserve histories from which application state can be reconstructed and can durably represent failures or retries. Their primary abstraction is generally execution or domain-event continuity rather than an independent six-part admission record separating Evidence, Authority, State, Transition, Exception, and Receipt.

**Distributed ledgers** provide particularly strong neighboring examples because they combine immutable histories, validation rules, identity or endorsement mechanisms, and transaction outcomes. Hyperledger Fabric, Corda, Ethereum, and Holochain therefore received dedicated comparison.

**Version-control and append-only structures** such as Git, Certificate Transparency, CRDT-oriented stores, and related systems demonstrate that branching or refusal of a single application-level canonical state can coexist with durable history. These systems generally do not also provide the behavioral combination examined below: revocable permission checked on the admission path, durable outcomes for accepted/rejected/failed attempts that reach that authoritative path, durable failure diagnostics excluded from accepted work-state, and no substrate-designated canonical current work-state.

**Provenance and supply-chain systems**, including in-toto-like designs, strongly represent evidence and attestation but do not necessarily own the admission and continuity semantics EASTER places inside the kernel.

**Agent frameworks** remain the most direct application neighborhood because EASTER arose from continuity problems observed in intelligent work. Section 6 reports those systems separately rather than treating them as the complete prior-art universe.

These overlaps motivate a conjunction claim rather than a primitive-by-primitive novelty claim.

## 9.3 Hyperledger Fabric

Hyperledger Fabric was one of the strongest neighboring architectures found.

Its transaction history is immutable and retains both valid and invalid ordered transactions. Endorsement-policy validation occurs within the validation/commit path, and membership infrastructure supports identity and revocation mechanisms. Endorsements and private-data hashes can also serve evidence-like roles.

The comparison nevertheless identified several differences from EASTER.

First, Fabric explicitly maintains a mutable **world state** representing current ledger values. Its immutable transaction history can reconstruct earlier values, but EASTER instead admits immutable State objects and deliberately refuses to designate a canonical current State.

Second, Fabric's outcome recording is not uniform across all attempted operations in the bounded sense used by the EASTER comparison. Transactions that reach ordering receive valid/invalid outcomes, while proposal or endorsement failures that occur before ordering do not enter the ledger as corresponding durable transaction outcomes.

Third, Fabric's evidence-like material is generally carried within transaction structures rather than represented as an independently lifecycle-addressable Evidence primitive.

Fabric therefore demonstrates substantial overlap without reproducing the full EASTER boundary.

## 9.4 Corda

Corda provides a different neighboring architecture.

Its transaction model avoids a single globally broadcast world state and provides strong transaction-local structure, attachments, signatures, and explicit state evolution. On those dimensions, Corda resembles EASTER more closely than Fabric in some decompositions.

The dedicated review nevertheless found its Authority and outcome semantics materially different from EASTER's.

Transaction signatures establish required participants for particular transactions, while identity revocation operates through a different network/security layer. The reviewed architecture did not demonstrate EASTER's specific rule that live revocable Authority be validated inside the consequential admission path immediately governing the authoritative write.

Likewise, the investigation did not identify a uniform EASTER-like durable outcome record spanning accepted, rejected, and failed attempts at the same authoritative operation boundary.

Corda therefore overlaps strongly on non-global state and explicit transitions while diverging on the admission boundary EASTER makes central.

## 9.5 Holochain

Holochain provided useful counterevidence because it makes a substantially different architectural tradeoff.

Its agent-centric design avoids a single canonical global current state. However, the reviewed design explicitly resists externally revocable authorship authority as part of that architecture.

This matters because it suggests that the absence of the EASTER conjunction is not merely terminological. Some neighboring architectures obtain decentralization or non-canonicality by making choices that work against centralized, hard-revocable admission Authority.

EASTER chooses differently. It accepts an authoritative kernel boundary while refusing to let that kernel choose a canonical semantic branch.

The distinction is architectural rather than a claim that one tradeoff is universally preferable.

## 9.6 Other examined candidates

The closest-prior investigation also considered Ethereum, Certificate Transparency, Apache Kafka, Amazon QLDB, in-toto, Temporal/Cadence, Axon Framework, Git, CRDT-oriented stores, and related systems.

Different subsets of the target properties appear repeatedly.

Ethereum provides durable transaction receipts and immutable history but maintains canonical world state.

Certificate Transparency provides append-only history without defining a canonical trust state, but lacks the examined combination of in-path revocable permission, rejected/failed outcome recording at the same boundary, and separate durable failure diagnostics.

Git and CRDT-oriented systems demonstrate branching or non-canonical continuation particularly clearly but do not combine those properties with the same admission-permission and outcome behavior.

Temporal and related durable-execution systems preserve rich execution and failure histories but treat failure as part of workflow execution semantics rather than EASTER's separation between accepted work-state, diagnostic failure record, and operation outcome.

in-toto strongly represents signed supporting evidence but is principally a verification/provenance architecture rather than an authoritative transition kernel.

No individual overlap is therefore presented as surprising. The research question concerns their conjunction.

## 9.7 The surviving behavioral conjunction

Across the closest-prior investigations, four behavioral properties emerged as the narrowest architectural conjunction supported independently by the preserved analyses. They are stated behaviorally here so a prior architecture need not use EASTER's names or data partitioning to satisfy them:

1. **live revocable permission is validated on the authoritative admission path governing the consequential write;**
2. **attempts that reach that authoritative operation boundary receive a durable outcome distinguishing accepted, rule-rejected, and execution-failed operations, provided the outcome record itself can be persisted;**
3. **execution failure can leave durable diagnostic information without promoting the failed requested work into accepted authoritative work-state; and**
4. **the authoritative substrate deliberately does not designate one admitted work-state as the canonical current semantic state, and permits branching continuation.**

These are behavioral comparison criteria, not requirements that a prior system expose tables or objects named Authority, Receipt, Exception, or State. A differently partitioned architecture that provides equivalent behavior at the same boundary counts as satisfying the corresponding property.

Evidence as a first-class primitive and immutable append-only history remain important parts of EASTER, but the prior-art investigation found closer analogues for those properties individually.

The four-property conjunction is therefore the narrower boundary around the part of the architecture that remained unidentified as a bundle in the systems examined.

The dedicated Fabric, Corda, Holochain, and broader candidate analyses did not identify a system combining all four.

This result supports the following bounded statement:

**In the systems and literature examined to date, we did not identify an existing architecture that combines all four behavioral properties at the same consequential continuity boundary.**

This is a non-identification claim, not a universal novelty theorem.

## 9.8 Pre-prior-art provenance of the conjunction

Because a conjunction can be manufactured after examining prior art, we separately tested whether these four properties had been selected retrospectively to occupy an empty region.

The preserved provenance record supports the opposite chronology.

All four properties were present in EASTER artifacts before the dedicated Fabric/Corda/Holochain closest-architecture investigation:

- in-path Authority and revocation behavior existed in the kernel implementation;
- ACCEPTED / REJECTED / FAILED Receipt semantics existed in the schema and implementation;
- durable Exceptions excluded from accepted State were already explicit;
- branching without a kernel-defined canonical current State was already part of the design.

Repository history independently corroborated each of these commitments in implementation or manuscript artifacts predating the closest-prior comparison.

The September 25 manuscript artifact also contained the same coarse architectural commitments before the September 29–30 dedicated prior-art investigation.

This evidence addresses a specific methodological objection:

**the four-property conjunction was not constructed after discovering which properties the closest examined architectures lacked.**

It does not establish that the conjunction is globally novel.

## 9.9 Independent decomposition and reconciliation

The two closest-architecture passes used different decompositions and should not be flattened into a single search procedure.

Pax's pass used the six-property EASTER combination and pre-identified Fabric as the lead candidate. It identified Fabric as the strongest candidate in that bounded evaluation. Clawde's later closest-architecture work used an eight-property decomposition and deliberately added Corda and Holochain after Fabric's canonicality weakness surfaced.

Under an equal-weight reading of Clawde's properties, Corda compared more closely on some axes, particularly canonicality, evidence separation, and transition explicitness. Pax's differently structured pass retained Fabric as the closest candidate.

The subsequent reconciliation found no material contradiction in the underlying primary-source facts. The difference arose from decomposition and weighting.

Rather than hiding that disagreement or converting it into a supposedly objective ranking, the manuscript retains the more defensible result:

**Fabric and Corda expose different portions of the EASTER boundary, and neither examined architecture combines the surviving four behavioral properties.**

The novelty boundary therefore does not depend on declaring a single architecture the universally “closest” prior system.

## 9.10 Search stopping and remaining candidate classes

The dedicated closest-architecture search was stopped after the bounded conjunction survived the examined candidate set.

That stopping decision was not treated as proof of exhaustion. A later 4–0 participant vote favored stopping additional dedicated search while preserving the claim as provisional and bounded. The vote records a research-governance decision, not evidence that no counterexample exists.

The preserved rationale was that the search had already crossed several materially different architectural families; differently decomposed passes converged on the same underlying factual gap; and the manuscript claim had been deliberately bounded to the systems and literature examined rather than strengthened into an exhaustive statement.

A particularly relevant untested candidate class remains:

**a permissioned distributed architecture combining hard revocable RBAC-like admission with non-canonical or sharded replication.**

Such a system could weaken or kill the present non-identification claim if it also provided the bounded outcome recording and durable non-state failure behavior described above at the same boundary.

Pax's historical brief also names TUF, OpenLineage, Marquez, DataHub, and Atlas, but its surviving report does not establish whether those candidates were actually examined. They therefore cannot be counted as negative findings from that pass.

These classes should be treated as future prior-art work rather than silently assumed absent.

## 9.11 Novelty boundary

The related-work investigation supports three different levels of claim, which should not be collapsed.

**Supported:** individual EASTER mechanisms have substantial prior art.

**Supported within the examined set:** the four-property behavioral conjunction above was not identified in the systems and literature actually evidenced as examined.

**Not established:** that no prior system anywhere implements the conjunction, that EASTER is universally novel, that every candidate named in a historical brief was actually screened, or that the conjunction is necessary or optimal.

Accordingly, Draft 2 adopts the bounded formulation:

> **In the systems and literature examined to date, we did not identify an existing architecture that simultaneously combines live revocable permission validation on the consequential admission path, durable accepted/rejected/failed outcome distinction for attempts reaching that authoritative boundary when persistence succeeds, durable failure diagnostics excluded from accepted work-state, and deliberate refusal by the substrate to designate a canonical current semantic work-state.**

This formulation is intentionally falsifiable.

A documented prior architecture satisfying the behavioral conjunction—even with different terminology or internal record types—would narrow or defeat the claim without invalidating the EASTER implementation itself.

That separation between **what the system does** and **what the bounded prior-art investigation has established about its novelty** is essential to the evidentiary boundary of this paper.