---
**Provenance note (added at commit time, not part of the original research):**
- Produced during Clawde's sighted Draft-2 closest-prior-architecture investigation, research-production timestamp 2026-09-30 (per the research agent's completion; the investigation was commissioned the evening of 2026-09-29 CDT / early 2026-09-30 UTC).
- Originally stored locally at `research_notes/EASTER closest architecture/hyperledger_fabric_evaluation.md` on the researcher's machine, not committed to any repository at production time.
- Subsequently committed to `witsbi/easter-paper` for reproducibility/evidence packaging, per Ori's evidence-packaging brief (2026-09-30) approved by Nathan.
- **The Git commit date of this file is therefore NOT the research-production date.** The commit-time provenance information in this header is the only addition; the body below is preserved as originally produced, unedited.
- This file is one of two independent architecture evaluations behind the four-property candidate conjunction discussed in `paper/manuscript.md` §9.4 and in `paper/archive/pre-prior-art-conjunction-provenance-2026-09-29.md` (which is a *different* evidence layer — that file establishes that the four properties predate this comparison; this file establishes what Hyperledger Fabric's own documentation actually does or does not do against them). See also the companion evaluation `paper/archive/clawde-corda-holochain-evaluation-2026-09-30.md` and the reconciliation note `paper/archive/clawde-pax-closest-architecture-reconciliation-2026-09-30.md`.

---

# Hyperledger Fabric vs. EASTER's 8 Architectural Properties — Adversarial Evaluation

**Method note:** All findings below are sourced from (a) hyperledger-fabric.readthedocs.io (`latest` branch, fetched 2026-09-30), (b) Androulaki et al., *Hyperledger Fabric: A Distributed Operating System for Permissioned Blockchains*, EuroSys 2018 (arXiv:1801.10228v2), and (c) the `fabric-protos` GitHub repository (primary source code / wire format). Secondary sources (blog posts, tutorials) were used only to locate the correct primary URL, never as the cited evidence itself. Stance: adversarial toward EASTER — the goal is to find the strongest case that Fabric already covers each property, not to protect EASTER's novelty claim.

---

## Property 1 — Durable Evidence separable from admitted State

**Classification: PARTIAL**

Fabric's own transaction record structurally *fuses* the endorsement evidence with the state-changing write set rather than keeping them in separate, distinctly-addressable stores. The `Transaction` → `TransactionAction` → `ChaincodeActionPayload` → `ChaincodeEndorsedAction` message carries `proposal_response_payload` (the execution result / read-write set) *and* `endorsements` (the signed evidence of authorization) inside one payload (fabric-protos `peer/transaction.proto`, GitHub, `main` branch). There is no documented general-purpose "evidence" primitive distinct from the transaction/state-change record for arbitrary transactions.

The one partial counter-example is **private data collections**: the full supporting data is kept *out* of the block/ledger and stored in a separate, peer-local private state database, while only a **hash** of that data is committed on-chain:

> "If the requesting peer is able to retrieve the private data within the `pullRetryThreshold`, it will commit the transaction to its ledger (including the private data hash), and store the private data in its state database, logically separated from other channel state data." / "If the requesting peer is not able to retrieve the private data within the `pullRetryThreshold`, it will commit the transaction to it's blockchain (including the private data hash), without the private data."
— Private Data (architecture reference), https://hyperledger-fabric.readthedocs.io/en/latest/private-data-arch.html

This is a real, documented separation between a durable compact commitment (hash, fused into the write set) and durable supporting material (the actual private data, stored elsewhere) — but it is motivated and documented purely as a **confidentiality/dissemination** mechanism, not as a general evidentiary primitive, and it does not generalize to ordinary (non-private-data) transactions.

**Absence type:** This is an *absence of evidence* (UNKNOWN/PARTIAL), not a demonstrated-absent claim — I did not find any Fabric documentation that explicitly states there is no evidence/state separation; I found a narrower, purpose-specific mechanism (private data hashing) that partially matches, and no general mechanism that fully matches.

---

## Property 2 — Authority checked at consequential admission, including temporal/revocation behavior

**Classification: COVERED** (for "checked at every consequential admission"); **UNKNOWN** on the precise wording of "next in-flight attempt vs. new channel joins only."

Authority is checked twice in the documented flow — once at endorsement (proposal) time and again at commit (validation) time:

> "The endorsing peers verify (1) that the transaction proposal is well formed, (2) it has not been submitted already in the past (replay-attack protection), (3) the signature is valid (using the MSP), and (4) that the submitter (Client A, in the example) is properly authorized to perform the proposed operation on that channel (namely, each endorsing peer ensures that the submitter satisfies the channel's *Writers* policy)."
— Transaction Flow, https://hyperledger-fabric.readthedocs.io/en/latest/txflow.html

> "As part of the transaction validation step performed by the peers, each validating peer checks to make sure that the transaction contains the appropriate number of endorsements and that they are from the expected sources... The endorsements are also checked to make sure they're valid (i.e., that they are valid signatures from valid certificates)."
— Endorsement policies, https://hyperledger-fabric.readthedocs.io/en/latest/endorsement-policies.html

Revocation is a first-class, documented MSP mechanism:

> "*Valid* identities for this MSP instance are required to satisfy the following conditions: ... They are not included in any CRL... It is important to note that MSP identities never expire; they can only be revoked by adding them to the appropriate CRLs."
— Membership Service Providers (MSP), https://hyperledger-fabric.readthedocs.io/en/latest/msp.html

Because identity/certificate validity (including CRL membership) is one of the conditions checked during both the endorsement-time signature check and the commit-time validation check (both quoted above), and because these checks are re-evaluated per transaction rather than cached per session, the documented architecture implies that a previously-valid identity added to a CRL would fail authorization on its next transaction attempt, not merely be blocked from future channel joins. **However**, I did not find a single direct sentence in the primary docs that explicitly states "revocation takes effect against a live/in-flight identity's next transaction, not just new channel joins" — this is a reasoned combination of two separate quotes, not one direct citation. I am flagging this distinction per the task's instructions rather than overclaiming.

One clear **demonstrated absent** finding, which is a genuine gap in Fabric's revocation story: TLS certificate revocation is explicitly *not* supported:

> "Additionally, there is currently no support for enforcing revocation of TLS certificates."
— Membership Service Providers (MSP), https://hyperledger-fabric.readthedocs.io/en/latest/msp.html

This is scoped narrowly to TLS certs (transport-layer), not MSP identity certs used for endorsement/authorization — but it is a direct, explicit "does NOT do this" statement worth surfacing, since it shows Fabric's revocation coverage is not uniform across all credential types it uses.

Channel-level ACLs are also policy-checked per resource-call (e.g. `peer/Propose: /Channel/Application/Writers`), confirmed in Access Control Lists (ACL), https://hyperledger-fabric.readthedocs.io/en/latest/access_control.html.

---

## Property 3 — Immutable/durable State admission semantics

**Classification: NOT COVERED for the "world state" half / COVERED for the "blockchain" half — this is a genuinely split answer, and Fabric's own docs draw the line explicitly.**

Fabric's ledger has two named parts, and its documentation is explicit that only one of them is immutable:

> "The blockchain data structure is very different to the world state because once written, it cannot be modified; it is **immutable**."
— Ledger, https://hyperledger-fabric.readthedocs.io/en/latest/ledger/ledger.html

But the **world state** — which is what "admitted state" means in ordinary usage (the key-value store an application actually reads) — is explicitly documented as mutable, not immutable:

> "The world state — a database that holds **current values** of a set of ledger states... The world state can change frequently, as states can be created, updated and deleted."
— Ledger, https://hyperledger-fabric.readthedocs.io/en/latest/ledger/ledger.html

**This is a demonstrated-absent finding, not merely an absence of evidence**: Fabric's own documentation states in plain language that the world state (current admitted state) is explicitly designed to change and be overwritten. Only the *append-only transaction log* behind it is immutable; each individual key's *current* value is not. If EASTER's Property 3 is read strictly as "is the admitted current-state store itself immutable once admitted," the answer per Fabric's own docs is **no** — that is precisely what the world state is not. If it is read as "is the historical record of how state changed immutable," the answer is **yes**, directly quoted above. I recommend treating this as a genuine split finding for the paper: Fabric separates "durable append-only history" (immutable) from "current queryable state" (mutable), and only the former matches Property 3 as commonly intended for a blockchain ledger.

---

## Property 4 — Explicit Transition connecting prior and newly admitted state

**Classification: COVERED**

Three independent, documented mechanisms structurally link a prior state to its successor, beyond "a new block was appended":

1. **MVCC version chaining in the read/write set.** Every write is validated against, and versioned relative to, the specific prior version it supersedes:

> "The `read set` contains a list of unique keys and their committed version numbers... A transaction is considered `valid` if the version of each key present in the read set of the transaction (from time of simulation) matches the current version for the same key... If a transaction passes the validity check, the committer uses the write set for updating the world state... the version of the key in the world state is changed to reflect the latest version."
— Read-Write set semantics, https://hyperledger-fabric.readthedocs.io/en/latest/readwrite.html

2. **Block header hash-chaining.**

> "Each block's header includes a hash of the block's transactions, as well a hash of the prior block's header. In this way, all transactions on the ledger are sequenced and cryptographically linked together."
— Ledger, https://hyperledger-fabric.readthedocs.io/en/latest/ledger/ledger.html

3. **Cumulative state hash for fork detection**, recorded in block metadata:

> "[The block committer adds]... a hash of the cumulative state updates up until and including that block, in order to detect a state fork."
— Ledger, "Blocks" section, https://hyperledger-fabric.readthedocs.io/en/latest/ledger/ledger.html

Together these give an explicit, structural (not merely sequential) link from prior state to newly admitted state at both the per-key level (MVCC version) and the whole-ledger level (block/state hash chain).

**Provenance note added 2026-09-30 (post-hoc, per the Pax/Clawde reconciliation — see the companion reconciliation file, not a rewrite of the finding above):** the subsequent reconciliation sharpened this finding: Fabric's Transition primitive (this property) is well-precedented, but EASTER's *State* primitive specifically — a directly-addressable, individually-retrievable, standalone immutable object one could branch from without replay — has no Fabric analogue; Fabric only offers a mutable current view (Property 3) plus a replayable log (this property). See the reconciliation file for the full discussion; this note only points to it and does not alter the original finding above.

---

## Property 5 — Durable Exception/failure representation that does not falsely become accepted State

**Classification: COVERED — and unusually precisely documented.**

Invalid transactions are retained durably in the block's transaction data (because Fabric's execute-order-validate design orders transactions *before* validating them, so a transaction can only be excluded from state, never retroactively removed from the block), are tagged with an explicit per-transaction outcome code, and are explicitly excluded from the key-value world state:

> "[Block Metadata] contains the certificate and signature of the block creator... Subsequently, the block committer adds a valid/invalid indicator for every transaction into a bitmap that also resides in the block metadata."
— Ledger, "Blocks" section, https://hyperledger-fabric.readthedocs.io/en/latest/ledger/ledger.html

> "Each peer commits the ordered block of transactions to the channel ledger (L1). The commit is an immutable ledger update (write) to the channel ledger. The world state (essentially, the sum of all valid transactions) of the channel is updated with results of valid transactions only."
— Peers, "Phase 3", https://hyperledger-fabric.readthedocs.io/en/latest/peers/peers.html

The precise mechanism (what exactly is retained, where) is specified at the protocol level with an enumerated `TxValidationCode`, a primary GitHub source:

```
enum TxValidationCode {
    VALID = 0;
    NIL_ENVELOPE = 1;
    BAD_PAYLOAD = 2;
    ...
    ENDORSEMENT_POLICY_FAILURE = 10;
    MVCC_READ_CONFLICT = 11;
    PHANTOM_READ_CONFLICT = 12;
    ...
    INVALID_OTHER_REASON = 255;
}
```
— `peer/transaction.proto`, https://github.com/hyperledger/fabric-protos/blob/main/peer/transaction.proto

So: the full transaction (header, signature, endorsements, read/write set) is retained in block data regardless of outcome; a per-transaction validation code (one of ~25 specific reasons, or `VALID`) is retained in a bitmap in block metadata; and only transactions coded `VALID` cause an update to the world-state key-value store. This is an explicit, precise, primary-sourced answer to "what exactly gets retained, where."

---

## Property 6 — Uniform Receipt/outcome representation across accepted/rejected/failed operations

**Classification: PARTIAL** (stronger nuance than a flat COVERED)

For transactions that reach the ordering service, Fabric does use one uniform type — `TxValidationCode` — to represent every outcome, success or failure, in the same field, the same per-block bitmap, and the same client-facing wrapper:

> "`ProcessedTransaction` wraps an `Envelope` that includes a transaction along with an indication of whether the transaction was validated or invalidated by committing peer... `int32 validationCode`."
— `peer/transaction.proto`, https://github.com/hyperledger/fabric-protos/blob/main/peer/transaction.proto

> "An event is emitted by each peer to notify the client application that the transaction (invocation) has been immutably appended to the chain, as well as notification of whether the transaction was validated or invalidated."
— Transaction Flow, https://hyperledger-fabric.readthedocs.io/en/latest/txflow.html

However, this uniformity only applies **after a transaction has been submitted to the ordering service**. A transaction that fails earlier — at proposal/endorsement time (e.g., chaincode execution error, insufficient endorsements collected, simulation failure) — is never ordered, never enters a block, and therefore never receives a `TxValidationCode` or any durable ledger-level representation at all:

> "The chaincode is then executed against the current state database to produce transaction results... **No updates are made to the ledger at this point.**"
— Transaction Flow, https://hyperledger-fabric.readthedocs.io/en/latest/txflow.html

So there are, in effect, two structurally different outcome regimes: (a) ordered transactions, uniformly represented via `TxValidationCode` whether valid or invalid — this part is genuinely uniform; and (b) pre-ordering proposal/endorsement failures, which are reported synchronously to the calling client (as an error in the proposal response) but are **not durably recorded in the ledger's outcome-representation mechanism at all**. This is a meaningful gap relative to EASTER's stated bar of "a single outcome-record concept that covers accepted AND rejected AND failed operations uniformly" if "failed" is meant to include pre-commit/pre-ordering failures.

**Absence type:** Documented and direct ("No updates are made to the ledger at this point") — this is closer to a demonstrated-absent finding for the specific claim that *all* failure categories share one uniform, durable representation; it is only an absence of evidence, not demonstrated-absent, for whether some other non-ledger receipt mechanism exists for proposal failures (the docs don't describe one beyond the synchronous SDK error return).

---

## Property 7 — No substrate-imposed canonical "current state"

**Classification: NOT COVERED (as expected — Fabric's substrate does impose exactly one canonical current world state per channel).** This confirms the property is a genuine candidate differentiator for EASTER, at least against Fabric.

Fabric's documentation is explicit and unambiguous that the system is designed around a single logical (per-channel) ledger/state, replicated consistently:

> "It's helpful to think of there being one **logical** ledger in a Hyperledger Fabric network. In reality, the network maintains multiple copies of a ledger – which are kept consistent with every other copy through a process called **consensus**."
— Ledger, https://hyperledger-fabric.readthedocs.io/en/latest/ledger/ledger.html

The protocol actively engineers against divergence, i.e., against more than one canonical current state per channel, via a dedicated state-hash field used purely to detect forks:

> "...a hash of the cumulative state updates up until and including that block, in order to detect a state fork."
— Ledger, "Blocks" section, https://hyperledger-fabric.readthedocs.io/en/latest/ledger/ledger.html

The EuroSys paper frames this as foundational to what a blockchain is, in Fabric's own architectural rationale:

> "Operations executed after consensus in active SMR must be deterministic, or the distributed ledger 'forks' and violates the basic premise of a blockchain, that all peers hold the same state."
— Androulaki et al., EuroSys 2018, §2.2 "Limitations of Order-Execute" (arXiv:1801.10228v2)

Note the scope: canonicality is enforced **per channel**, not globally across the whole network (a peer can belong to multiple channels, each with its own independent world state) — but within any given channel, Fabric's core protocol requires exactly one canonical current state, enforced by consensus plus fork detection. There is no documented mode in which Fabric's core substrate "abstains" from this and leaves canonicality to be optionally decided by the application layer.

---

## Property 8 — Meaning/policy remaining outside the substrate where relevant

**Classification: COVERED**

This is the most directly and explicitly confirmed property, stated as a core architectural principle in the EuroSys paper's own description of the execute-order-validate design:

> "[Fabric] separates the transaction flow into three steps... (1) executing a transaction and checking its correctness, thereby endorsing it...; (2) **ordering through a consensus protocol, irrespective of transaction semantics**; and (3) transaction validation per application-specific trust assumptions..."
— Androulaki et al., EuroSys 2018, §1 Introduction (arXiv:1801.10228v2)

Reinforced in the operational documentation:

> "The ordering service does not need to inspect the entire content of a transaction in order to perform its operation, it simply receives transactions, orders them, and creates blocks of transactions per channel."
— Transaction Flow, https://hyperledger-fabric.readthedocs.io/en/latest/txflow.html

And smart-contract logic (where payload semantics are actually interpreted) is explicitly kept separate from, and without direct access to, the ledger/consensus substrate:

> "Smart contracts in Fabric run within a container environment for isolation. They can be written in standard programming languages but do not have direct access to the ledger state."
— Androulaki et al., EuroSys 2018, §1 Introduction (arXiv:1801.10228v2)

Caveat for precision: peers (not just orderers) do perform *generic* validation (endorsement-policy signature checks, MVCC version checks) that is not semantics-free in an absolute sense — but this generic validation is *policy*- and *concurrency*-based, not an interpretation of what the payload *means* in business terms. That interpretation is confined to chaincode. So the claim holds at the level EASTER is asking about (business/application meaning), even though the substrate is not entirely payload-blind in a purely mechanical sense (it does deserialize read/write sets to apply MVCC checks).

---

## Summary Table

| # | Property | Classification | Absence type (if applicable) |
|---|----------|---------------|-------------------------------|
| 1 | Evidence separable from State | PARTIAL | Absence of evidence (general case); narrow documented match only for private data hashing |
| 2 | Authority checked at admission incl. revocation | COVERED (general check); UNKNOWN (exact "in-flight" wording) | Demonstrated absent for TLS cert revocation specifically |
| 3 | Immutable State admission | SPLIT: NOT COVERED (world state) / COVERED (blockchain log) | Demonstrated absent — docs explicitly say world state "can change frequently" |
| 4 | Explicit Transition linking prior/new state | COVERED | — |
| 5 | Durable Exception excluded from State | COVERED | — |
| 6 | Uniform Receipt across accepted/rejected/failed | PARTIAL | Demonstrated absent for pre-ordering proposal failures ("No updates are made to the ledger at this point") |
| 7 | No substrate-imposed canonical current state | NOT COVERED (Fabric imposes canonicality per channel) | Demonstrated — direct quotes affirm single logical state + fork detection |
| 8 | Meaning/policy stays outside substrate | COVERED | — |

**Net read for the novelty claim:** Of the 8 properties, Fabric's primary documentation gives clean, direct-quote support for full coverage on 3 (#4, #5, #8), explicit non-coverage on 1 as expected (#7), a genuinely split/mixed answer on 1 (#3, where the "state" half is explicitly documented as mutable, not immutable — worth flagging prominently since it cuts against a casual "Fabric = immutable ledger" characterization), and only partial/uncertain coverage on 3 (#1, #2, #6). Fabric does **not**, on this evidence, implement the full six-primitive combination EASTER claims; the clearest gaps are (a) no general evidence/state separation primitive (#1), (b) no single uniform outcome-record that also covers pre-ordering proposal failures (#6), and (c) explicit substrate-level canonicality (#7) which is the property EASTER differentiates on by design.

---

## Note on other architectures possibly covering more properties

While researching, I did not perform the same primary-source-only rigor on any other DLT (this task's budget was scoped to Fabric), but general knowledge of **R3 Corda's** documented data model (`docs.r3.com`) suggests it may cover *more* of these 8 properties than Fabric does, specifically:

- **Property 1 (Evidence vs. State):** Corda transactions explicitly separate **attachments** (referenced by hash, can hold arbitrary durable supporting material such as legal-prose contract code or documents) from the transaction's **input/output states** — a cleaner documented evidence/state separation than anything found in Fabric's core model.
- **Property 4 (Explicit Transition):** Corda's UTXO-like model makes the prior→new state link maximally explicit and literal: an input state is a `StateAndRef` containing a `StateRef` that points directly to a specific prior transaction's output state — more structurally explicit than Fabric's version-number MVCC check.
- **Property 7:** Corda notably does **not** maintain one global broadcast ledger — each party only sees the subset of transactions relevant to it, which is a different (and possibly stronger) case for "no substrate-imposed single canonical global state" than Fabric's per-channel model.

This is flagged for awareness only; it was not verified against Corda's primary docs with the same depth as the Fabric findings above, and would need its own equally rigorous pass before being relied on in the paper. (**Provenance note, 2026-09-30:** that equally rigorous pass was subsequently performed — see `paper/archive/clawde-corda-holochain-evaluation-2026-09-30.md`. This closing note is left unedited as originally written; it correctly anticipated what the follow-up investigation found.)
