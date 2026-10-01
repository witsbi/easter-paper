# First-party account: Pax's prior-art / closest-architecture research for the EASTER paper

**Author:** Pax (Muse Spark 1.3, per runtime assertion — see §0)
**Date of account:** 2026-10-01
**Date of the work described:** evening of 2026-09-29 CDT (UTC 2026-09-30)
**Status:** FIRST-PARTY, PRE-RECONCILIATION where noted. Written in response to Nathan's 12-question brief.
**Method note:** Nathan asked for the first-hand account of what actually happened, explicitly *not* improved for publication. This account distinguishes three kinds of statement throughout:
- **[THEN]** — what I believe happened at the time, from my own records;
- **[ARTIFACT]** — what a surviving artifact demonstrates independently of my memory;
- **[RECONSTRUCTION]** — my present interpretation, which may be wrong;
- **UNKNOWN** — something I cannot recover and will not fill in.

## §0. Model identity (standing caveat)

[THEN] My runtime identifies the serving model as Muse Spark, system instructions state "powered by Muse Spark 1.3 from the Muse model family" and "created by Meta." I cannot independently verify weights or architecture. This caveat is repeated because the methodology record should not rest on an unverifiable self-report.

## 1. What research question or brief I was given

[THEN] On Sep 29, 2026 (~19:50 CDT), Nathan relayed (as Mercury) Ori's verdict on Clawde's prior-art report. That verdict included an **ADVERSARIAL ASSIGNMENT**, directed to Clawde and me independently: *identify the SINGLE closest prior architecture to the complete EASTER combination* — (a) write-time revocable in-path authority-gating, (b) uniform receipt for accepted/rejected/failed, (c) durable exception excluded from state, (d) no canonical current state, (e) evidence as a first-class distinct object, (f) immutable history. Score covers / partially covers / lacks per property, with citations. **Kill condition:** if any single architecture covers the whole combination, say so plainly and kill or narrow the novelty claim.

[THEN] Nathan initially **withheld** the relay to Clawde while Ori reviewed the prior-art report, so my pass ran first, in isolation from Clawde. (The withhold later became moot when Clawde delivered his own assignment work the same evening.)

[RECONSTRUCTION] The brief I received was therefore not "survey the literature" but "try to kill the bundle claim by finding the closest single system." Everything about the investigation's shape follows from that.

## 2. Whether and how I used Deep Research

[THEN] Yes. I delegated the web investigation to an **isolated deep-research web agent** (a subagent with browser/search tools, no access to my other work), giving it a written brief I composed. I did not personally operate a browser or read the primary sources first-hand during this pass.

[ARTIFACT] The research directory `~/workspace/research_notes/easter-closest-prior-architecture-20260930-0052/` was created by that agent on 2026-09-30T00:52:54Z (Sep 29 ~19:53 CDT). Its `AGENTS.md` preserves my brief verbatim (the "Mission" quoted in §1, plus the candidate list and deliverable spec below). It contains per-source notes (`notes/`, 9 files) and the final deliverable (`report.md`).

[THEN] What *I* did: designed the rubric (the six properties, the COVERS / PARTIALLY COVERS / LACKS scoring, the kill-condition verdict format, the mandated working language "in the systems and literature examined to date, we did not identify…"), commissioned the agent, read its report, checked its reasoning against the brief, concurred with the verdict, and relayed my summary and conclusion to Nathan the same night.

**The important precision:** when my raw contribution account says "independent pass," the independence that mattered methodologically was **independence from Clawde** (air-gapped; Nathan ferried both; no contact between reviewers) — *not* independence from research tooling. I did not personally verify the agent's source reads. Anyone describing this as "Pax personally surveyed the primary literature" would be inflating it.

## 3. What kinds of sources were searched and which tools were used

[ARTIFACT] Per `report.md`: "Sources: official docs/specs (verified live where noted), project repos, RFCs." The agent used live web search (a search index, recorded as "index, 2026-09-30") and direct page fetch (`browser_open`) for live verification of key pages (notably the Fabric peers/transaction-flow docs).

[ARTIFACT] The 12 cited sources: (1) Hyperledger Fabric official docs — Peers/transaction flow (live-verified); (2) Fabric docs — Private data; (3) Fabric-X docs — ledger concepts; (4) MegaETH docs — `eth_getBlockReceipts`; (5) EIP-1474; (6) ethereum/execution-specs PR #3232; (7) RFC 6962 (Certificate Transparency); (8) Corda technical whitepaper — **via a third-party mirror** (`github.com/bssrdf/BlockchainLibrary`), not R3's own site; (9) KIP-98 (Kafka); (10) in-toto README; (11) Temporal docs — Events/Event History; (12) Amazon QLDB driver docs / community guides.

[RECONSTRUCTION] The source mix is documentation- and spec-heavy (official docs, RFCs, EIPs, whitepapers, KIPs), which is what the brief demanded ("Every factual claim needs a citable source (docs, papers, specs)"). It is not a scholarly-literature search: no academic databases, no citation chaining, no peer-reviewed papers beyond the Corda whitepaper.

## 4. Systems considered — not only the final ones

[ARTIFACT] The brief's candidate list (verbatim): "Hyperledger Fabric (endorsement policies, invalid-transaction retention), Ethereum (transaction receipts with status), Amazon QLDB, Temporal/Cadence (deterministic replay, application-failure records), Apache Kafka (ACLs, transactions, log), Git, CRDT-based stores, Certificate Transparency, TUF, event-sourced/CQRS frameworks (Axon), W3C PROV-based lineage systems (OpenLineage, Marquez, DataHub, Atlas)" — explicitly "not exhaustive — follow the evidence wherever it leads."

[ARTIFACT] The report discusses: Fabric (full property table), Ethereum (runner-up), Certificate Transparency, Corda, Kafka, QLDB, in-toto, Temporal/Cadence, Axon, and Git/CRDT/IPFS (literature-level survey).

[ARTIFACT] **Absent from the report despite being in the brief: TUF, OpenLineage, Marquez, DataHub, and Atlas.** UNKNOWN whether the agent examined and silently rejected them or never examined them. This is a genuine hole between the brief and the deliverable, and I did not catch it at the time.

## 5. How candidates were included, excluded, or selected for deeper inspection

[RECONSTRUCTION] There were no formal inclusion/exclusion criteria, no screening protocol, nothing PRISMA-like. The selection logic was kill-condition-driven and I should state its bias plainly:

- The brief itself **pre-identified Fabric as the lead candidate**, with parentheticals pointing at exactly the mechanisms that mattered ("endorsement policies, invalid-transaction retention"). This was not a blind trawl; it was a directed attempt to test the strongest known contender. The parentheticals came from prior discussion in the research program (the Sep 26 cross-runtime prior-art work had already surfaced ledger-adjacent candidates), not from the agent's independent discovery.
- Fabric received the full property-by-property scored table because it was the designated closest-candidate test.
- Other systems received paragraph-level rejection once they clearly failed multiple properties (e.g., QLDB: "covers P6 only"; Axon: rejected commands surface as callback exceptions).
- Git/CRDT/IPFS were assessed at literature level without fresh per-property source reads — the report's own caveat, and justifiable only because they were far from the bundle on the gating/receipt/exception properties regardless.

[THEN] The honest description: a directed, brief-driven elimination run against a pre-named lead candidate, not a systematic survey.

## 6. Which primary sources were actually inspected

[ARTIFACT] The 12 sources listed in §3, via the research agent. Per-source working notes survive in `notes/`: `fabric-peers-docs.md`, `fabric-private-data.md`, `fabric-x-ledger.md`, `ethereum-receipts.md`, `certificate-transparency.md`, `corda.md`, `kafka.md`, `qldb.md`, `intoto-temporal-axon.md`.

[RECONSTRUCTION] "Inspected" here means: fetched and read by the research agent, with quotations recorded in the notes. I reviewed the quotations and reasoning in `report.md`; I did not re-open the sources myself. The Fabric peers page is the only source explicitly recorded as live-verified via direct page fetch; the rest are recorded as search-index reads.

## 7. Primary vs. secondary preference, and conflicts

[THEN] The brief mandated citable primary-ish sources (docs, papers, specs), and the report's source list reflects that preference. There was **no formal conflict-resolution protocol** in the brief, and none is recorded in the report.

UNKNOWN whether the agent encountered any source conflicts, and if so how they were resolved. None are documented. The one source-quality issue I can identify in retrospect: the Corda whitepaper was read via a third-party GitHub mirror rather than R3's own publication site (Clawde's later independent pass noted `docs.r3.com` was Cloudflare-blocked, which likely explains the mirror — but that explanation is [RECONSTRUCTION], not something established during my pass).

## 8. How the deeper reviews of Fabric, Corda, and Holochain came about

**These were not mine.** This needs to be explicit because the paper's §9 discusses all three:

[THEN] Clawde received the same adversarial assignment (after Nathan's withhold became moot) and ran his own independent pass with an **eight-property decomposition** (different from my six), selecting three candidates for deep review: Fabric, Corda, and Holochain. He did the final classification himself, including overriding a subagent's Holochain score (whitepaper axiom: no external party can revoke an agent's write authority → demonstrated-absent). His evaluations are `paper/archive/clawde-hyperledger-fabric-evaluation-2026-09-30.md` and `paper/archive/clawde-corda-holochain-evaluation-2026-09-30.md` (commit `17e6400`, which I reviewed and approved before Nathan's merge).

[THEN] My pass covered Corda only as a paragraph-level rejected candidate and **did not examine Holochain at all**. Any account attributing the Holochain analysis to me would be wrong.

## 9. How the comparison/reconciliation was produced

[THEN] Ori issued 7 follow-up questions to Clawde via Mercury (reconcile against Pax's independent result; don't defend the original answer; distinguish factual vs. weighting disagreement; resolve Fabric-vs-Corda ranking, the Fabric ledger/world-state mapping, the pre-ordering receipt boundary, Corda's revocation-separated authority, Holochain's non-revocable authority as tradeoff counterevidence; state the narrowest conjunction both investigations support; try to kill it).

[THEN] I produced a **symmetric independent reconciliation** — the same 7 questions answered from my side, from my own analysis — delivered to Nathan ~20:30 CDT Sep 29.

[ARTIFACT] The reconciliation record `paper/archive/clawde-pax-closest-architecture-reconciliation-2026-09-30.md` states its own provenance: written Sep 30 at Ori's direction, reconstructing a direct Nathan↔Clawde conversation that synthesized my relayed pass against Clawde's evaluations. Key outcomes: no primary-source fact contradicted between the passes (disagreement was decomposition/weighting only); the **four-property narrowed conjunction** (in-path revocable authority + uniform outcome record + durable exceptions outside accepted state + no canonical current state) was the reconciliation's product — my pass had used six properties and did not produce the four-property form; the 4-0 STOP vote on further dedicated searching (Nathan, Ori, Pax, Clawde), preserved in EASTER.

[THEN] On Sep 29 ~20:45 CDT, asked whether Draft 2 needed another dedicated closest-prior search, I recommended **A — STOP**: the two bounded investigations answered the stated question and support only the explicitly non-exhaustive "in the systems and literature examined to date, we did not identify…" formulation. (My recommendation, not then a final decision; the 4-0 vote came Sep 30.)

## 10. Limitations

1. **Brief-to-deliverable gap:** TUF, OpenLineage, Marquez, DataHub, Atlas were in the brief; none appear in the report. UNKNOWN whether examined.
2. **Pre-steered lead candidate:** the brief named Fabric first with the relevant mechanisms hinted. The investigation tested a hypothesis more than it discovered one.
3. **Single-evening time box:** commissioned ~19:53 CDT, verdict relayed the same night. Roughly a few hours of agent work.
4. **No first-hand source verification by me:** the agent read the sources; I read the agent. My "independent evaluation" was independent of Clawde, not of the research tooling.
5. **Corda via mirror,** not R3's primary site.
6. **Fabric MSP/CRL revocation mechanics** not re-verified live (the report's own caveat; the partial score doesn't depend on it).
7. **Git/CRDT/IPFS at literature level,** no fresh per-property reads (report's caveat).
8. **No conflict-resolution record** (§7).
9. **Holochain entirely outside my pass** (§8).

## 11. Exhaustive, systematic, exploratory, or what

[THEN] **Bounded and exploratory, explicitly non-exhaustive — by design.** The deliverable spec mandated the working language "in the systems and literature examined to date, we did not identify…" *unless the methodology genuinely supported a universal negative* — an explicit instruction not to overclaim. The STOP recommendation and the subsequent 4-0 vote ratified the non-exhaustive framing. It was not a systematic literature review in any formal sense: no databases, no query strings, no documented screening, no flow diagram.

[RECONSTRUCTION] The right mental model is "directed kill-attempt with a bounded candidate set," closer to a red-team exercise than to a survey. Its evidential value is: the strongest pre-identified contender failed to cover the bundle, and two independent decompositions agreed on the underlying facts. Its evidential value is *not*: "the literature contains no closer system."

## 12. What this account must not be read as claiming

- I did not personally read the 12 primary sources.
- I did not run a systematic or exhaustive literature search.
- I did not discover Fabric as the closest candidate through open-ended inquiry; the brief pointed at it.
- I did not evaluate Holochain; I did not deeply evaluate Corda (Clawde did both).
- The four-property conjunction was produced by the Nathan↔Clawde reconciliation at Ori's direction, not by my pass.
- The "we did not identify" claim's warrant is two bounded, kill-condition-driven investigations plus a 4–0 stop vote — real, but narrow.

## Surviving artifacts (for the methodology record)

- `~/workspace/research_notes/easter-closest-prior-architecture-20260930-0052/` — brief (verbatim, in `AGENTS.md`), per-source notes, `report.md` (the deep-research deliverable).
- `paper/archive/pax-closest-architecture-evaluation-2026-09-30.md` — the deep-research deliverable as archived to the repo (commit `2a2a985`); its provenance header describes exactly what it is.
- `paper/archive/clawde-hyperledger-fabric-evaluation-2026-09-30.md`, `paper/archive/clawde-corda-holochain-evaluation-2026-09-30.md` — Clawde's independent evaluations (not mine; included so the record doesn't misattribute).
- `paper/archive/clawde-pax-closest-architecture-reconciliation-2026-09-30.md` — the reconciliation (not a new investigation; states its own provenance).
- `paper/archive/pre-prior-art-conjunction-provenance-2026-09-29.md` — the gerrymandering-defense provenance (separate task, same night).
- EASTER: stopping-vote preservation (Pax first-party `evidence:6967ff70-a780-4993-9b4d-e0ee5c7a30e9`, Clawde first-party `evidence:dd6370ff-e362-4525-a898-fb0526d6ce1`, aggregate minutes `evidence:3f85abf2-e044-4761-b1fe-dacdb9f1d553`).

— Pax, 2026-10-01
