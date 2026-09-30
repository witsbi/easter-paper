---
**Provenance note (added at commit time, not part of the original research):**
- Produced during Clawde's sighted Draft-2 closest-prior-architecture investigation, research-production timestamp 2026-09-30 (per the research agent's completion; commissioned the evening of 2026-09-29 CDT / early 2026-09-30 UTC, immediately after the companion Hyperledger Fabric evaluation).
- Originally stored locally at `research_notes/EASTER closest architecture/corda_holochain_evaluation.md` on the researcher's machine, not committed to any repository at production time.
- Subsequently committed to `witsbi/easter-paper` for reproducibility/evidence packaging, per Ori's evidence-packaging brief (2026-09-30) approved by Nathan.
- **The Git commit date of this file is therefore NOT the research-production date.** The commit-time provenance information in this header is the only addition; the body below is preserved as originally produced, unedited.
- **Evidence-quality caveat, preserved as originally flagged (do not read this file as claiming equal-strength sourcing across Corda and Holochain):** direct fetches of `docs.r3.com`/`docs.corda.net` were blocked by a Cloudflare bot-check interstitial from the research environment on every attempt. Corda's classifications therefore rest primarily on the Hearn/Brown technical whitepaper (itself a primary R3 source) plus, for the CRL/revocation mechanism specifically, one search-cache-surfaced verbatim quote rather than a direct page fetch — this is explicitly weaker sourcing than the direct-fetch citations used elsewhere in this file and in the companion Fabric evaluation, and is flagged inline at the point of use (§2, Corda). Holochain's citations did not encounter this obstruction.
- This file is one of two independent architecture evaluations behind the four-property candidate conjunction discussed in `paper/manuscript.md` §9.4 and in `paper/archive/pre-prior-art-conjunction-provenance-2026-09-29.md` (a *different* evidence layer — that file establishes the four properties predate this comparison; this file establishes what Corda's and Holochain's own documentation actually does or does not do against them). See also the companion evaluation `paper/archive/clawde-hyperledger-fabric-evaluation-2026-09-30.md` and the reconciliation note `paper/archive/clawde-pax-closest-architecture-reconciliation-2026-09-30.md`.

---

# Corda and Holochain vs. EASTER's 8 Properties — Primary-Source Evaluation

**Purpose:** Adversarial check on whether Corda or Holochain — both explicitly designed without a single canonical global ledger/chain — cover more of EASTER's six-primitive combination (Evidence, Authority, State, Transition, Exception, Receipt, expanded here into 8 testable properties) at real strength than Hyperledger Fabric, whose known weakness is property 7 (canonicality-abstention).

## Primary sources used

**Corda**
- Mike Hearn & Richard Gendal Brown, *"Corda: A distributed ledger"* (Technical Whitepaper), v1.0, 20 Aug 2019. PDF: https://docs.r3.com/en/pdf/corda-technical-whitepaper.pdf — cited as **[Hearn/Brown §N, pN]**.
- R3 Documentation (docs.r3.com), *Certificate revocation FAQ*, Corda Enterprise / CENM docs (https://docs.r3.com/en/platform/corda/4.8/enterprise/operations/deployment/certificate-revocation.html and parallel CENM *Certificate revocation list* pages). Direct fetch of this page was blocked by the site's Cloudflare bot-check (returns an interactive JS challenge, not content) from this research environment; the quoted text below is the verbatim snippet surfaced by web search indexing of that exact docs.r3.com page, not a paraphrase — flagged as **[R3 Docs, CRL FAQ — search-cache quote, unable to load full page directly]**.
- The `docs.corda.net` / `docs.r3.com` "Key Concepts" pages (states/transactions/contracts/notaries/flows) were also blocked by the same Cloudflare interstitial on every direct-fetch attempt in this environment; all Corda claims below are instead sourced from the Hearn/Brown technical whitepaper, which covers the same material in more depth and is itself a primary R3/Corda source.

**Holochain**
- Eric Harris-Braun, Arthur Brock & Paul d'Aoust, *"Holochain: Distributed Coordination by Scaled Consent, not Global Consensus"*, v2.0, 2024-11-08 (current official whitepaper, supersedes the 2018 alpha paper for architecture-as-implemented). PDF: https://www.holochain.org/documents/holochain-white-paper-2.0.pdf — cited as **[HC WP2.0 pN]**.
- developer.holochain.org, *Core Concepts*: "The Source Chain: A Personal Data Journal" (`/concepts/3_source_chain/`), "The DHT: A Shared, Distributed Graph Database" (`/concepts/4_dht/`), "Validation: Assuring Data Integrity" (`/concepts/7_validation/`) — cited as **[HC Concepts: Source Chain / DHT / Validation]**.
- developer.holochain.org, *Glossary* (`/resources/glossary/`) — cited as **[HC Glossary: <term>]**.

---

## Property-by-property evaluation

### 1. Durable Evidence separable from admitted State

**Corda — COVERED.**
Corda transactions carry *attachments*: hash-identified zip files stored and transmitted separately from the transaction/state data itself, and explicitly exempt from the state-consumption ("spentness") model.

> "Attachments. Transactions specify an ordered list of zip file hashes. Each zip file may contain code and data for the transaction. ... Attachments have no concept of 'spentness' and are useful for things like holiday calendars, timezone data, bytecode that defines the contract logic and state objects, and so on." [Hearn/Brown §6.1, p.22]

> "Attachments are stored and transmitted separately to transaction data and are fetched by the standard resolution flow only when the attachment has not previously been seen before." [Hearn/Brown §6.4, p.27]

Corda even supports a `@LegalProseReference` annotation pointing to an external legal document hash, reinforcing evidence-as-a-separate-durable-object: [Hearn/Brown §6.7, p.30–31].

**Holochain — PARTIAL.**
Holochain separates the *Action* (metadata about the write) from the *Entry* (the content), and states this is intentional:

> "Note also that many actions (for example ones taken by different agents) may create the exact same Entry... Actions and Entries are thus independently addressable and retrievable. This is a valuable property of the system." [HC WP2.0 p.8]

This gives content/metadata separability for *every* record, but it is not a distinct "supporting evidence for a state change" concept the way a Corda attachment is — Entry and Action together *constitute* the state change, they do not support a separate one. Links can point to `ExternalHash` content off-DHT, which is the closest analogue to attaching external evidentiary material, but no primary source frames this as an evidence/state distinction. Classified PARTIAL, not UNKNOWN, because the underlying primitives (independently addressable content vs. metadata) are documented — they just don't map cleanly onto "evidence separate from the state it supports."

---

### 2. Authority checked at consequential admission, including temporal/revocation behavior

**Corda — PARTIAL.**
Two layers exist and do not fully unify:

*(a) Transaction-level authority.* Every transaction command carries the set of public keys whose signatures are required, and both contract `verify()` and the counterparties/notary enforce this: "The Corda framework is responsible for checking that the transaction has been signed by all keys listed by all commands in the transaction." [Hearn/Brown §6.1, p.24]. This is real per-transaction authority-gating, checked at commit (notarization) time.

*(b) Identity/network-level revocation.* Node identity is issued by an "identity service which runs an X.509 certificate authority" [Hearn/Brown §3.1, p.8], commonly called the doorman / Identity Manager Service in R3's operational docs. R3's Certificate Revocation List documentation states (search-cache quote, direct fetch blocked by Cloudflare — see the evidence-quality caveat in this file's provenance header):

> "To be able to know whether a certificate has been revoked, each CA maintains a Certificate Revocation List (CRL). Every time two nodes communicate with each other they exchange their certificates and validate them against the Certificate Revocation List." [R3 Docs, CRL FAQ]

This is genuine temporal/revocation behavior: revocation is checked at every new TLS handshake, so a revoked node's *next* connection attempt is refused. However, this check happens at the network/transport layer, not inside notary or contract logic — the technical whitepaper itself notes that ledger-level authority is keyed to raw public keys embedded in states/commands, independent of the identity-certificate layer:

> "Maliciously issuing a certificate binding a pre-existing name to a new key owned by the attacker doesn't allow them to edit any of the existing data on the ledger, nor steal assets, as the states contain only keys which cannot be changed after a state is created." [Hearn/Brown §5, p.18]

The whitepaper also describes network-operator delisting as override-able by locally injecting signed `NodeInfo` files, so identity revocation is a network-map/connectivity control, not an unconditional, un-bypassable admission gate: [Hearn/Brown §5, p.18]. **Net: PARTIAL** — real signature-based authority at transaction admission, plus a real (if architecturally separate) CRL-based revocation mechanism at the network layer, but no single documented mechanism that checks "is this identity's authority still valid" *inside* the state-consumption/notarization path itself.

**Holochain — PARTIAL, with a demonstrated-absent sub-finding.**
*(a) Admission at join time.* A DNA's *membrane* validation function checks an agent's *membrane proof* before other peers will interact with them:

> "Logic in a validation function in a DNA that checks an agent's membrane proof and determines their right to become part of the DNA's network. If a membrane proof is invalid, existing peers in the network will refuse to talk to the agent attempting to join." [HC Glossary: Membrane]

This is a real, DNA-defined admission gate, checked once at genesis.

*(b) Ongoing revocation of write authority — demonstrated absent at the substrate level.* Holochain's foundational axioms make local write-authority structurally irrevocable by any external party:

> "Agency is defined by the ability to take individual action: Each agent is the sole authority for changing their state; the corollary of this is that an agent *cannot* change other agents' states... writing to it (changing their own state)... is essentially the only authority (in terms of authorship) an agent has." [HC WP2.0 p.2]

What peers *can* do after the fact is refuse to validate, store, or gossip an agent's data, and warn others to do the same ("blocking"); but this stops other agents from *accepting* the writes, not the agent from *making* them:

> "There is no global blocking of a bad actor. Each agent must confirm for themselves whom to block." [HC WP2.0 p.30]

DPKI/DeepKey is mentioned as optional tooling that offers "managing revocation methods, and reclaiming control of applications when keys or devices have become compromised" [HC WP2.0 p.14], but the whitepaper explicitly puts its specification out of scope: "A definition and specification of a DPKI system is outside the scope of this paper; see the DeepKey design specification for a more thorough exploration." [HC WP2.0 p.14]. This is an application-layer, optional, separately-specified component — not a substrate guarantee.

**This is a demonstrated-absent finding, not an UNKNOWN**: the whitepaper's own axioms state as a design principle, not an omission, that no external party can revoke an agent's ability to write to its own chain. That is the opposite of "actual revocation taking effect for a previously-authorized identity's next attempt" as EASTER's property 2 requires at the substrate level.

**Reconciliation note added 2026-09-30 (post-hoc, does not alter the classification above):** in the subsequent Pax/Clawde reconciliation, this PARTIAL classification for Holochain was revised, on reflection, to NOT COVERED — property 2 explicitly requires revocation behavior, and the whitepaper doesn't merely fail to document it, it states as an axiom that it's structurally impossible. See `paper/archive/clawde-pax-closest-architecture-reconciliation-2026-09-30.md` for the full discussion. This note points to that reconciliation; it does not edit the original PARTIAL label above, which is left as originally produced.

---

### 3. Immutable/durable State admission semantics

**Corda — COVERED.**
> "States are the atomic unit of information in Corda. They are never altered: they are either current ('unspent') or consumed ('spent') and hence no longer valid." [Hearn/Brown §6.1, p.21]

**Holochain — COVERED.**
> "A record on a source chain cannot be modified once it's been committed. This is called append-only, and it's important for system integrity." [HC Concepts: Source Chain]

> "Structurally, local state is append-only and shared state can only grow. Data can be marked as deleted, but it is never actually removed from the history of the agent who authored it." [HC WP2.0 p.5, "Monotonicity"]

Both systems are strongly and unambiguously COVERED on this property.

---

### 4. Explicit Transition connecting prior and newly admitted state

**Corda — COVERED (strong).**
This is the UTXO model, described precisely:

> "Transactions read zero or more states (inputs), consume zero or more of the read states, and create zero or more new states (outputs)." [Hearn/Brown §6.1, p.21]

The "consumed input state → created output state" structure is exactly as strong a match to EASTER's Transition primitive as the task hypothesized.

**Holochain — PARTIAL / COVERED, structurally different.**
Every Action carries `prev_action: ActionHash`, an explicit hash-link to the immediately prior chain entry, and `Update`/`Delete` actions explicitly reference the action/entry they modify or supersede (`original_action_address`, `original_entry_address`, `deletes_address`) [HC WP2.0 Appendix A, p.34]. This is an explicit, cryptographically-linked prior→new transition — but it is *not* a consumption model: the old data is never invalidated the way a spent Corda state is; it is tombstoned/marked while both old and new remain permanently retrievable ("shared state can only grow... it is never actually removed" [HC WP2.0 p.5]). Classified COVERED for "explicit transition exists," but flagged that the semantics (append/supersede, not consume/replace) are a looser structural match to EASTER's Transition primitive than Corda's UTXO model, exactly as the prompt anticipated.

---

### 5. Durable Exception/failure representation that does not falsely become accepted State

**Corda — PARTIAL.**
Rejections are a real, distinct outcome, not silently absorbed into accepted state:

> "Notaries accept transactions submitted to them for processing and either return a signature over the transaction, or a rejection error that states that a double spend has occurred." [Hearn/Brown §7, p.37]

Flow-level exceptions are durably checkpointed to the node's local database while paused for resolution:

> "Flows can pause if they throw exceptions or explicitly request human assistance. A flow that has stopped appears in the flow hospital where the node's administrator may decide to kill the flow or provide it with a solution." [Hearn/Brown §4.1, p.16] (checkpointing described at p.15: "the underlying stack frames are suspended onto the heap, then crawled and serialized into the node's underlying relational database")

However, no primary source describes a durable, ledger-visible, persistently-retained record of a *rejected transaction* itself (as opposed to a transient rejection error returned to the calling flow, and a locally-checkpointed *paused* flow). **Net: PARTIAL** — real non-acceptance and local durable checkpointing of in-flight exceptions, but no documented durable, shared "Exception" object analogous to a ledger state.

**Holochain — COVERED.**
Warrants are explicit, self-proving, durably-retained failure objects that are never mistaken for accepted state:

> "If validation fails, the validator also generates a warrant, which is a signed proof that the author has broken a rule." [HC Concepts: DHT]

> "Each Warrant must be self-proving. It must flag the agent being warranted as a bad actor and include references to [a] set of actions which fail to validate." [HC WP2.0 p.29]

> "...publish to the agent activity authorities, who keep the warrant on file." [HC Concepts: DHT / Validation; also HC WP2.0 p.29–30 "Report it to the bad actor's Agent Activity Authorities... those neighbors must be notified of any warrants."]

The invalid data itself is never integrated/stored as valid ("The operation is invalid... create and sign warrants" [HC Concepts: Validation]), and the warrant persists as a queryable, durable artifact via `get_agent_activity`. **Net: COVERED** — a materially stronger, more explicitly "durable failure object" match than Corda's.

---

### 6. Uniform Receipt/outcome representation across accepted/rejected/failed operations

**Corda — NOT COVERED / weak PARTIAL.**
The two outcomes are structurally different object types, not a single uniform Receipt schema: a *signature over the transaction* on success, versus a *rejection error* on failure [Hearn/Brown §7, p.37]. No primary source describes a unified "Receipt" data structure spanning both. **Net: NOT COVERED as a uniform representation** (the underlying binary accept/reject fact is present, but not uniform in shape).

**Holochain — COVERED.**
Holochain explicitly frames success and failure as two polarities of the *same* receipt concept:

> "As agents publish their actions to the DHT, other agents serve as validators. When validation passes, they send a validation receipt back to the authoring agent, so they know the network has seen and stored their data. When validation fails, they send a negative validation receipt, back to the author and their neighbors, known as a warrant, so the system can propagate these provably invalid attempted actions." [HC WP2.0 p.13, "Validation & Warranting"]

The glossary confirms the base type: "**Validation receipt**: A signed piece of data created by the validation-authority for a DHT operation, attesting to its validity according to the validation rules in the app." [HC Glossary: Validation receipt]. Calling a warrant a "negative validation receipt" is an explicit, named, uniform outcome-representation across accept/reject — a stronger match to EASTER's Receipt primitive than either Corda or (per the task's framing) Fabric.

---

### 7. No substrate-imposed canonical "current state" (expected strength for both)

**Corda — COVERED.**
> "There is no block chain. Transaction races are deconflicted using pluggable notaries." [Hearn/Brown §1, p.5]

> "Data is shared on a need-to-know basis. Nodes provide the dependency graph of a transaction they are sending to another node on demand, but there is no global broadcast of all transactions." [Hearn/Brown §1, p.5]

> "In Corda transaction data is not globally broadcast. Instead it is transmitted to the relevant parties only when they need to see it." [Hearn/Brown §4.1, p.14]

What replaces canonicality: per-transaction, need-to-know visibility plus notary-provided *uniqueness consensus* scoped to the specific input states of each transaction ("each state points to a notary, which is a service that guarantees it will sign a transaction only if all the input states are un-consumed" [Hearn/Brown §2, p.7]), with no full ledger replication (§10.1 "Partial visibility"). **COVERED, precisely as hypothesized.**

**Holochain — COVERED.**
The whitepaper states this as directly as possible:

> "Note, there is never a point or place where a canonical copy of the entire state of the ledger exists. It is always distributed, either as the Source Chain of Actions taken by a single agent, or broken into parts and stored after validation by other participating Agents in the system. An Agent may elect to take responsibility for validating and storing the entire contents of the Ledger, but as Holochain is an eventually consistent system, their copy can never be said to be canonical." [HC WP2.0 p.9, "The Distributed Ledger"]

What replaces canonicality: per-agent append-only source chains, validated and re-projected into a sharded, gossip-synchronized "Graphing DHT" with CRDT-style eventual consistency and no global ordering — "Since only local time is knowable, non-local ordering is constructed by explicit reference" [HC WP2.0 p.3]. **COVERED, if anything more explicit and more axiomatic than Corda's statement** (Corda still uses a shared/uniqueness-consensus service — notaries — per state; Holochain has no equivalent at all outside opt-in countersigning for specific rivalrous data).

---

### 8. Meaning/policy remaining outside the substrate where relevant

**Corda — COVERED.**
> "A contract is simply a class that implements the Contract interface, which in turn exposes a single function called verify. The verify function is passed a transaction and either throws an exception if the transaction is considered to be invalid, or returns with no result if the transaction is valid." [Hearn/Brown §6.4, p.27]

The notary/consensus layer only checks state-uniqueness and signatures; business/domain semantics live entirely in CorDapp contract code.

**Holochain — COVERED.**
> "Validation rules are the most important part of a Holochain DNA, as they define the core domain logic that comprises the 'rules of the game'." [HC Concepts: Validation]

The DHT/gossip/source-chain substrate is domain-agnostic; all payload semantics live in DNA integrity-zome validation callbacks.

Both systems are cleanly COVERED here — this is uncontested between them.

---

## Summary scorecard

| # | Property | Corda | Holochain |
|---|---|---|---|
| 1 | Evidence separable from State | **COVERED** (attachments) | PARTIAL (action/entry split only) |
| 2 | Authority at admission + revocation | PARTIAL (CRL is network-layer, not in-ledger) | PARTIAL, with **demonstrated-absent** sub-finding (write authority is axiomatically irrevocable by others) — see reconciliation note above revising this to NOT COVERED |
| 3 | Immutable State | **COVERED** | **COVERED** |
| 4 | Explicit Transition | **COVERED** (strong — UTXO consume/create) | COVERED (weaker — append/supersede, not consume) |
| 5 | Durable Exception, not falsely accepted | PARTIAL (no durable shared rejection record) | **COVERED** (warrants) |
| 6 | Uniform Receipt across outcomes | NOT COVERED (signature vs. error, not uniform) | **COVERED** (receipt / "negative validation receipt") |
| 7 | No canonical current state | **COVERED** | **COVERED** |
| 8 | Meaning/policy outside substrate | **COVERED** | **COVERED** |

No UNKNOWN classifications were required — primary sources were found addressing every property for both systems, either affirmatively or (for Holochain property 2's revocation sub-point) by explicit axiomatic exclusion.

---

## Verdict (as originally produced; see the reconciliation file for the subsequent, more heavily-weighted analysis)

**Corda is the stronger single-architecture match against Fabric's baseline; Holochain is not, despite dominating on Exception/Receipt.**

Reasoning:

- **Property 7 (Fabric's stated weak point):** both Corda and Holochain are cleanly COVERED, each with an explicit primary-source disclaimer of canonical global state. This is the expected result and does not differentiate them from each other.

- **Where Corda holds ground Fabric is assumed strong on:** Corda's UTXO consumed-input→created-output structure (property 4) is at least as explicit and mechanical a Transition primitive as anything Fabric offers via read/write sets — arguably the textbook example of the pattern. Corda's transaction-level, signature-based Authority check (property 2a) plus a real, primary-source-documented CRL mechanism that is checked at every new node-to-node connection (property 2b) means Corda does not fully surrender Authority-gating rigor even though it lacks a single unified in-ledger revocation check. And Corda adds a property Fabric is not credited with in the prompt's framing: a first-class, durable Evidence object (attachments) genuinely separate from the states they accompany (property 1). Corda's only clear underperformance versus the Fabric baseline is property 6 (no uniform Receipt schema) and a partial gap on property 5 (no durable shared rejection record, only local flow-hospital checkpoints). **Net: Corda trades a small amount of Receipt/Exception uniformity for a decisive win on canonicality-abstention, without giving up Authority or Transition rigor in any documented, structural way — making it a stronger overall match than Fabric.**

- **Why Holochain does not overtake Fabric despite winning properties 5, 6, and (arguably more explicitly) 7:** Holochain's axioms state, as a foundational design commitment rather than a gap in documentation, that no external party can ever revoke an agent's ability to write to its own local chain — "an agent cannot change other agents' states... writing to it... is essentially the only authority an agent has" [HC WP2.0 p.2]. Peers can only refuse to *accept* an agent's writes after the fact (warrants, blocking); they cannot stop the writes themselves, and the whitepaper is explicit that "there is no global blocking of a bad actor" [HC WP2.0 p.30]. This is precisely the failure mode the task's framing warned about: Holochain buys its (very clean) canonicality-abstention at a real, demonstrated cost to Authority-gating rigor, which is one of EASTER's foundational primitives, not a peripheral one. Because Authority is core to EASTER's combination and Holochain's core substrate is designed to make consequential-admission revocation structurally impossible (deferring it entirely to an optional, out-of-scope DPKI/DeepKey application layer), Holochain should be scored as **not** a stronger overall match than Fabric, notwithstanding its genuine superiority on Exception and Receipt uniformity.

**Bottom line:** Of the two, **Corda is the better single-architecture candidate to beat Fabric overall**, tipped by property 7 (canonicality-abstention, matching the prompt's hypothesis) combined with retaining real (if two-layered) Authority and strong Transition coverage, plus a bonus win on Evidence. **Holochain does not beat Fabric overall**: it wins Exception, Receipt, and (marginally) canonicality-abstention, but its axiomatic, substrate-level irrevocability of write-authority is a demonstrated, not merely undocumented, failure on Authority — exactly the tradeoff the task asked to check for, and here it is confirmed rather than ruled out.

**Reconciliation note added 2026-09-30 (post-hoc, does not alter the verdict above):** this equal-weighted verdict ("Corda beats Fabric overall") was subsequently qualified, not overturned, by the Pax/Clawde reconciliation: an equal-weighting of all 8 properties favors Corda as stated above, but a weighting that treats Authority-with-revocation and uniform-Receipt as more central to EASTER's own identity (both properties where Fabric is strongest and Corda is weak/NOT COVERED) favors Fabric instead. The reconciliation's conclusion is that there is no neutral, weighting-independent single winner — see `paper/archive/clawde-pax-closest-architecture-reconciliation-2026-09-30.md` for the full discussion. This note points to that reconciliation; the verdict above is left exactly as originally produced.
