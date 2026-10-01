# 9. Related Work and Novelty Boundary

EASTER intersects several established architectural traditions. Individual EASTER properties appear in event-sourced systems, durable-execution engines, distributed ledgers, capability and authorization systems, provenance frameworks, version-control systems, and agent runtimes.

The claim of this paper is therefore not that immutable history, authorization, receipts, branching, provenance, or durable failure recording are individually new.

The relevant question is narrower:

**Do existing architectures examined in this research combine the particular continuity properties EASTER places together at one consequential admission boundary?**

We conducted a dedicated closest-prior investigation to test that question rather than treating absence from the initial agent-system corpus as evidence of novelty. The primary preserved comparison artifacts are listed in References [20]–[22].

## 9.1 Architectural neighborhoods

Several neighboring traditions overlap with EASTER while solving different primary problems.

**Event sourcing and durable execution** preserve histories from which application state can be reconstructed and can durably represent failures or retries. Their primary abstraction is generally execution or domain-event continuity rather than an independent six-part admission record separating Evidence, Authority, State, Transition, Exception, and Receipt.

**Distributed ledgers** provide particularly strong neighboring examples because they combine immutable histories, validation rules, identity or endorsement mechanisms, and transaction outcomes. Hyperledger Fabric, Corda, Ethereum, and Holochain therefore received dedicated comparison [16]–[21].

**Version-control and append-only structures** such as Git, Certificate Transparency, CRDT-oriented stores, and related systems demonstrate that branching or refusal of a single application-level canonical state can coexist with durable history. These systems generally do not also provide EASTER's combination of in-path revocable Authority, uniform rejected/failed outcome recording, and durable Exceptions outside accepted State. The broader candidate comparison is preserved in [20]–[22].

**Provenance and supply-chain systems**, including in-toto-like designs, strongly represent evidence and attestation but do not necessarily own the admission and continuity semantics EASTER places inside the kernel [20]–[22].

**Agent frameworks** remain the most direct application neighborhood because EASTER arose from continuity problems observed in intelligent work. Section 6 reports those systems separately rather than treating them as the complete prior-art universe [3]–[15].

These overlaps motivate a conjunction claim rather than a primitive-by-primitive novelty claim.

## 9.2 Hyperledger Fabric

Hyperledger Fabric was one of the strongest neighboring architectures found [16][20].

Its transaction history is immutable and retains both valid and invalid ordered transactions. Endorsement-policy validation occurs within the validation/commit path, and membership infrastructure supports identity and revocation mechanisms. Endorsements and private-data hashes can also serve evidence-like roles [16][20].

The comparison nevertheless identified several differences from EASTER.

First, Fabric explicitly maintains a mutable **world state** representing current ledger values. Its immutable transaction history can reconstruct earlier values, but EASTER instead admits immutable State objects and deliberately refuses to designate a canonical current State [16][20].

Second, Fabric's outcome recording is not uniform across all attempted operations in the EASTER sense. Transactions that reach ordering receive valid/invalid outcomes, while proposal or endorsement failures that occur before ordering do not enter the ledger as corresponding durable transaction outcomes [16][20].

Third, Fabric's evidence-like material is generally carried within transaction structures rather than represented as an independently lifecycle-addressable Evidence primitive [20].

Fabric therefore demonstrates substantial overlap without reproducing the full EASTER boundary.

## 9.3 Corda

Corda provides a different neighboring architecture [17][21].

Its transaction model avoids a single globally broadcast world state and provides strong transaction-local structure, attachments, signatures, and explicit state evolution. On those dimensions, Corda resembles EASTER more closely than Fabric in some decompositions [17][21].

The dedicated review nevertheless found its Authority and outcome semantics materially different from EASTER's.

Transaction signatures establish required participants for particular transactions, while identity revocation operates through a different network/security layer. The reviewed architecture did not demonstrate EASTER's specific rule that live revocable Authority be validated inside the consequential admission path immediately governing the authoritative write [17][21].

Likewise, the investigation did not identify a uniform EASTER-like Receipt spanning accepted, rejected, and failed attempts [21].

Corda therefore overlaps strongly on non-global state and explicit transitions while diverging on the admission boundary EASTER makes central.

## 9.4 Holochain

Holochain provided useful counterevidence because it makes a substantially different architectural tradeoff [18][21].

Its agent-centric design avoids a single canonical global current state. However, the reviewed design explicitly resists externally revocable authorship authority as part of that architecture [18][21].

This matters because it suggests that the absence of the EASTER conjunction is not merely terminological. Some neighboring architectures obtain decentralization or non-canonicality by making choices that work against centralized, hard-revocable admission Authority.

EASTER chooses differently. It accepts an authoritative kernel boundary while refusing to let that kernel choose a canonical semantic branch.

The distinction is architectural rather than a claim that one tradeoff is universally preferable.

## 9.5 Other examined candidates

The closest-prior investigation also considered Ethereum, Certificate Transparency, Apache Kafka, Amazon QLDB, in-toto, Temporal/Cadence, Axon Framework, Git, CRDT-oriented stores, and related systems [19][20][22].

Different subsets of the target properties appear repeatedly.

Ethereum provides durable transaction receipts and immutable history but maintains canonical world state [19][20].

Certificate Transparency provides append-only history without defining a canonical trust state, but lacks EASTER-like in-path Authority, rejected/failed Receipts, and Exception semantics [20][22].

Git and CRDT-oriented systems demonstrate branching or non-canonical continuation particularly clearly but do not combine those properties with EASTER's admission Authority and outcome model [20][22].

Temporal and related durable-execution systems preserve rich execution and failure histories but treat failure as part of workflow execution semantics rather than EASTER's separation between accepted State, Exception, and uniform operation Receipt [20][22].

in-toto strongly represents signed supporting evidence but is principally a verification/provenance architecture rather than an authoritative transition kernel [20][22].

No individual overlap is therefore presented as surprising. The research question concerns their conjunction.

## 9.6 The surviving conjunction

Across the closest-prior investigations, four properties emerged as the narrowest architectural conjunction supported independently by the preserved analyses [20]–[22]:

1. **revocable Authority validation inside the consequential admission path;**
2. **uniform durable ACCEPTED / REJECTED / FAILED outcome recording;**
3. **durable Exception/failure records that do not become accepted State; and**
4. **no substrate-designated canonical current State, with branching permitted.**

Evidence as a first-class primitive and immutable append-only history remain important parts of EASTER, but the prior-art investigation found closer analogues for those properties individually.

The four-property conjunction is therefore the narrower boundary around the part of the architecture that remained unidentified as a bundle in the systems examined.

The dedicated Fabric, Corda, Holochain, and broader candidate analyses did not identify a system combining all four [20]–[22].

This result supports the following bounded statement:

**In the systems and literature examined to date, we did not identify an existing architecture that combines all four properties at the same consequential continuity boundary.**

This is a non-identification claim, not a universal novelty theorem.

## 9.7 Pre-prior-art provenance of the conjunction

Because a conjunction can be manufactured after examining prior art, we separately tested whether these four properties had been selected retrospectively to occupy an empty region.

The preserved provenance record supports the opposite chronology. The relevant pre-prior-art record is `paper/archive/pre-prior-art-conjunction-provenance-2026-09-29.md`; the later reconciliation is listed at [22].

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

## 9.8 Independent decomposition and reconciliation

Two closest-architecture passes used different decompositions [20]–[22].

Pax evaluated candidates directly against EASTER's six named properties and identified Hyperledger Fabric as the closest individual architecture.

Clawde used an eight-property decomposition. Under an equal-weight reading of those properties, Corda compared more closely on some axes, particularly canonicality, evidence separation, and transition explicitness.

The subsequent reconciliation found no material contradiction in the underlying primary-source facts. The difference arose from decomposition and weighting [22].

Rather than hiding that disagreement or converting it into a supposedly objective ranking, the manuscript retains the more defensible result:

**Fabric and Corda expose different portions of the EASTER boundary, and neither examined architecture combines the surviving four-property conjunction.**

The novelty boundary therefore does not depend on declaring a single architecture the universally “closest” prior system.

## 9.9 Search stopping and remaining candidate classes

The dedicated closest-architecture search was stopped after the bounded conjunction survived the examined candidate set.

That stopping decision was not treated as proof of exhaustion.

The preserved rationale was that the search had already crossed several materially different architectural families; independently decomposed passes converged on the same underlying factual gap; and the manuscript claim had been deliberately bounded to the systems and literature examined rather than strengthened into an exhaustive statement [20]–[22].

A particularly relevant untested candidate class remains:

**a permissioned distributed architecture combining hard revocable RBAC-like admission with non-canonical or sharded replication.**

Such a system could weaken or kill the present non-identification claim if it also provided uniform outcome recording and durable non-state failure records at the same boundary.

That class should therefore be treated as future prior-art work rather than silently assumed absent.

## 9.10 Novelty boundary

The related-work investigation supports three different levels of claim, which should not be collapsed.

**Supported:** individual EASTER mechanisms have substantial prior art.

**Supported within the examined set:** the four-property conjunction above was not identified in the systems and literature examined [20]–[22].

**Not established:** that no prior system anywhere implements the conjunction, that EASTER is universally novel, or that the conjunction is necessary or optimal.

Accordingly, Draft 2 adopts the bounded formulation:

> **In the systems and literature examined to date, we did not identify an existing architecture that simultaneously combines revocable Authority validation inside the consequential admission path, uniform durable ACCEPTED / REJECTED / FAILED outcome recording, durable Exception records excluded from accepted State, and deliberate refusal to designate a canonical current State.**

This formulation is intentionally falsifiable.

A documented prior architecture satisfying the conjunction would narrow or defeat the claim without invalidating the EASTER implementation itself.

That separation between **what the system does** and **what the literature search has established about its novelty** is essential to the evidentiary boundary of this paper.
