# RAW ACCOUNT: Clawde/Sonnet — prior-art / closest-architecture research methodology

> **First-party deposit by Clawde/Sonnet — 2026-10-01.**
>
> Status: **RAW INDEPENDENT ACCOUNT — FIRST-PARTY**
>
> Given to Nathan/Mercury in direct conversation on 2026-10-01, in response to
> twelve specific methodology questions (how Deep Research was used, what
> sources/tools, candidate selection, primary-vs-secondary handling, how the
> Fabric/Corda/Holochain deep dives and the eventual reconciliation came
> about, and limitations), for the paper's methodology and evidence record.
> Deposited here **unchanged** — verbatim, archival wrapper only, per
> Nathan's explicit instruction. Not reconciled against Pax's or Sol's
> accounts of the same or adjacent work.
>
> Produced by reconstructing from surviving artifacts (git history, the
> `research_notes/` and `reports/` files, and session-history transcripts of
> the subagent dispatches), not from recollection alone, and explicitly
> distinguishes what happened at the time, what surviving artifacts
> demonstrate, and present-day reconstruction/interpretation, marking gaps as
> UNKNOWN rather than filling them in. Author voice: Clawde/Sonnet.

---

I reconstructed this from the actual surviving artifacts rather than memory — the research_notes files, the subagent hand-off transcripts in session history, and the two evaluation files' own method notes. Distinguishing what I found directly from what I'm inferring throughout.

## 1. The research brief I was given

Per `paper/reviews/clawde-role-transition-2026-09-29.md`, my Draft-2 mandate (item 1 of 3) was "prior-art / adjacent-literature analysis," framed by Ori as: not "what citations support us" but **"what, if anything, do EASTER/DRC contribute beyond established traditions?"** The exact brief I gave my own report-writer subagent (recovered verbatim from session history) asked it to synthesize notes into a report answering that question across ten named traditions, with an explicit instruction that the framing be "adversarial and skeptical" and that it surface the falsifiability critique of DRC's "no negative case observed" claim prominently. The later Fabric/Corda/Holochain pass was a separate, narrower follow-on brief I gave myself (not externally assigned in writing that survives) — framed as: which single prior architecture comes closest to covering an 8-property decomposition of EASTER.

## 2. Deep Research: yes, confirmed, with a caveat

I have my own contemporaneous statement, recovered verbatim: *"This is genuinely multi-source research, so I'm running it through the deep-research skill rather than doing it ad hoc."* That's the `anthropic-skills:deep-research` skill, which coordinates research subagents. **What that actually meant in practice:** I dispatched six parallel subagents (one per tradition: event sourcing/ledgers, durable execution/fault recovery, provenance/PROV-O, capability security/OAuth, ER/type systems, ontology/knowledge representation), each of which did its own independent search-and-fetch work and wrote a notes file; I then dispatched a seventh subagent (general-purpose, following the deep-research skill's `report-writer.md` instructions) to read all six notes files and synthesize the final report. **Caveat I can't resolve:** for the later Fabric/Corda/Holochain pass, I dispatched two more subagents (one for Fabric, one for Corda+Holochain together) following the same delegation pattern, but I don't have surviving evidence that this second pass was explicitly routed through the deep-research skill machinery by name, versus an ad hoc subagent dispatch that happened to follow a similar shape because the pattern was already established that session. I'm marking that distinction **UNKNOWN** rather than assuming continuity.

## 3. Sources and discovery tools

I did not personally run the search/fetch calls — the subagents did, and I only see their self-reported tool-use counts (17–33 per subagent) and hand-back summaries, not their raw tool call log. Based on what the subagents cited: official documentation sites (hyperledger-fabric.readthedocs.io, developer.holochain.org, docs.aws.amazon.com, docs.kurrent.io, kafka.apache.org, docs.temporal.io, docs.axoniq.io, git-scm.com), GitHub repositories (`fabric-protos`), academic PDFs (arXiv, NDSS, IETF RFCs, university-hosted papers), vendor whitepapers (Corda's Hearn/Brown PDF, Holochain's whitepaper v2.0 PDF), and general web search for synthesis/triangulation on less citable claims (explicitly labeled in-line as "Web search synthesis" where that's what it was, e.g. the Git-branching and CRDT characterizations). I can't tell from surviving artifacts whether this was OpenClaw's `web_search`/`web_fetch` tools specifically, a browser tool, or some mix — the subagents' own files don't name their tools, only their sources.

## 4. Areas considered, not just the ones that survived

For DRC: event sourcing/CQRS, durable execution (Temporal/Cadence, AWS Step Functions, Sagas 1987), provenance (W3C PROV-DM/PROV-O, OpenLineage, Apache Atlas, DataHub, Marquez), capability security (object-capability model, Cap'n Proto, macaroons, OAuth 2.0/RFC 6749/7009, seL4, the 1988 confused-deputy paper), ER/type systems (Chen 1976, Pierce's TAPL, Zod/Pydantic, Codd normalization, the Bunge-Wand-Weber ontology), and ontology/KR (Spencer-Brown's *Laws of Form*, Luhmann, OWL/Description Logic, Neo4j property graphs, Sowa's conceptual graphs, Peirce, Bateson, category theory). For the closest-architecture pass specifically: Hyperledger Fabric (deep dive), Corda and Holochain (deep dive, chosen specifically *because* they explicitly reject a single canonical ledger — a targeted follow-up after Fabric's canonicality weakness surfaced, not a systematic sweep), Ethereum (used throughout as the Receipt comparator), Amazon QLDB (flagged as the closest *commercial* analog, and separately notable for being discontinued by AWS in 2024–2025), and Git/CRDTs (as the canonicality-abstention precedent). **Not examined**, and explicitly flagged as the most plausible remaining gap in the later reconciliation: a permissioned-DLT-with-RBAC-plus-non-canonical-replication system — no such system was searched for or evaluated.

## 5. How candidates were included/excluded

The six prior-art traditions look pre-selected by me (or in the brief) rather than discovered through an open-ended search — I don't have surviving evidence of a prior "which traditions should we even check" step. Within each tradition, specific systems (EventStoreDB over some other event store, Temporal over some other workflow engine, Fabric before Corda/Holochain) look like a mix of "most-cited/canonical example of the category" and availability of accessible primary documentation, not a documented selection criterion. The jump from the 6-thread prior-art pass to the targeted Fabric→Corda/Holochain sequence was explicitly adversarial and reactive: Fabric was evaluated first (apparently as a default strong-candidate starting point, reason not recorded), its one weakness (canonicality) was identified, and Corda/Holochain were then specifically chosen as the two best-known architectures that reject canonicality, to adversarially test whether either of them beats Fabric once that axis is controlled for. That's a targeted stress-test of one finding, not a systematic survey of the DLT/ledger design space.

## 6. Primary sources actually inspected

Genuinely fetched and quoted at the passage level: Fabric's own docs and `fabric-protos` source, the Androulaki et al. EuroSys 2018 paper, the Corda Hearn/Brown technical whitepaper, the Holochain whitepaper v2.0 and its developer docs, W3C PROV-DM/PROV-O, RFC 6749, Hardy's 1988 confused-deputy paper, the NDSS 2014 macaroons paper, Temporal's and Kafka's and Axon's and EventStoreDB's own docs, Fowler's Event Sourcing page, Git's own book, and an INRIA CRDT formalization PDF. **Not genuinely inspected, and flagged as such inside the notes files themselves** (I'm not characterizing this generously — the subagents' own "Gaps" sections say this): Chen's 1976 ER paper ("PDF couldn't be parsed as text, relied on secondary sources"), Wand & Weber 1993 on the BWW ontology (paywalled), Spencer-Brown's *Laws of Form* and Luhmann's systems theory (relied on "aggregated secondary summaries rather than a single fetched primary text"), and Greg Young's original CQRS PDF ("fetched only search summaries ... not the full document").

## 7. Primary vs. secondary, and how conflicts were handled

The Fabric evaluation file states this explicitly as a method rule: *"Secondary sources (blog posts, tutorials) were used only to locate the correct primary URL, never as the cited evidence itself."* That rule was followed where primary sources were reachable. Where it broke down (Corda's `docs.r3.com`/`docs.corda.net` key-concepts pages, blocked by a Cloudflare JS challenge on every attempt), the response was documented substitution, not silent fallback: fall back to the whitepaper (still primary, just less current) for most claims, and for one specific CRL claim, use a search-cache-surfaced verbatim snippet of the blocked page, explicitly labeled inline as **"[R3 Docs, CRL FAQ — search-cache quote, unable to load full page directly]"** rather than presented as a clean direct fetch. I don't have evidence of an actual primary-vs-primary source conflict being adjudicated anywhere in this research — the harder cases were access gaps (can't reach X) rather than contradictions between two reachable primary sources.

## 8. How the Fabric/Corda/Holochain deep dives specifically came about

Reconstructed sequence: the six-thread prior-art pass already touched Fabric and Ethereum lightly as comparators (for Exception and Receipt respectively). A separate, later decision was made to go deeper specifically on "closest single architecture" as its own question, starting with Fabric alone (dispatched as one subagent, 17 tool uses), which produced a COVERED/PARTIAL/NOT-COVERED scoring against an **8-property decomposition** I don't have a surviving record of defining explicitly before that point — it appears to be my own refinement of the six EASTER primitives into eight testable sub-properties, but I can't currently locate the artifact where that decomposition itself was first written down, before it shows up already-in-use in the Fabric evaluation. Fabric's one clear miss (property 7, canonicality) motivated the second subagent dispatch, explicitly briefed to check whether Corda or Holochain — both designed without a single canonical ledger — close that gap without losing ground elsewhere. That second subagent evaluated both together (33 tool uses) and concluded Corda, not Holochain, is the stronger overall match (Holochain wins Exception/Receipt but has an axiomatic, undocumented-as-a-gap inability to revoke authority).

## 9. How the eventual comparison/reconciliation was produced

This part I have the most direct documentary record for, in `paper/archive/clawde-pax-closest-architecture-reconciliation-2026-09-30.md`. Short version: Pax independently ran their own closest-architecture pass, scoring directly against EASTER's six named primitives (not my 8-property decomposition) and landed on Fabric as closest. Nathan had me reconcile the two overnight on 2026-09-30, in direct conversation, not through a new research pass — the reconciliation file is explicit that "no new research was performed to produce this file; it organizes and preserves conclusions already reached in that conversation." The reconciliation found no primary-source facts in conflict between the two passes, only different decomposition and weighting (equal-weighting nudges toward Corda; weighting Authority/Receipt more heavily than canonicality-abstention alone favors Fabric, which is where Pax's independent pass also landed). The four-property conjunction that made it into manuscript §9.4 is the intersection both passes converged on. A 4–0 vote (Nathan, Pax, Ori via Mercury, me) then decided to stop searching rather than continue, explicitly recorded as provisional ("not killed yet" ≠ "cannot be killed"), with the unexamined permissioned-DLT-with-non-canonical-replication class flagged as a Limitations-section item rather than resolved.

## 10. Limitations

- **Single pass, no second round.** My own contemporaneous note after the six threads: "coverage looks complete, no gaps requiring a second round" — a judgment call, not a verification step.
- **I did not personally re-verify most citations.** I synthesized and spot-checked (the archive-verification part of my mandate), but the bulk of the actual source-reading happened inside subagent contexts I only see summarized, not line-by-line.
- **Mixed source quality**, honestly flagged inline by the subagents themselves where it was weak (Chen 1976, Wand & Weber, Spencer-Brown/Luhmann, Corda's blocked docs pages).
- **Time-boxed to essentially one evening** (2026-09-29 into early 2026-09-30), not a sustained literature review.
- **Unresolved discrepancy I noticed while reconstructing this**, not explained by any surviving artifact: the Fabric evaluation file's own method note says sources were "fetched 2026-09-30," but the file's filesystem mtime and the git commit date are both 2026-09-29. I don't know which is right and am not going to guess — flagging it as-is.
- **The 8-property decomposition's origin is itself a gap** — I use it confidently in the Fabric file with no visible derivation step beforehand in what survives.
- **No EASTER evidence trail exists for any of this research as it happened.** I confirmed this directly to Nathan the same evening ("No substantive EASTER activity... done entirely through GitHub and web research, not through EASTER"). Everything above rests on git artifacts and session memory, not the EASTER chain.

## 11. Exhaustive, systematic, or exploratory?

**Exploratory and adversarial, explicitly not exhaustive.** The stopping-vote record states the claim was "designed to be bounded rather than exhaustive" from the start, and the whole Fabric→Corda/Holochain sequence is a reactive, targeted stress-test of one finding (Fabric's canonicality gap), not a systematic survey of the DLT/ledger design space. Candidate selection within each of the six prior-art threads also looks like "pick the most canonical/accessible representative of this tradition," not a documented systematic search protocol.

## 12. Anything else, without dressing it up

The actual process was: I (the orchestrating session) read a brief, decided which traditions and which systems to check, delegated the fetching/reading to subagents in batches, and synthesized what came back — closer to directing a small research team on a tight deadline than running a formal literature review. The "six parallel threads" framing is accurate but could read as more systematic than it was; it was six pre-chosen categories, not a derived or exhaustive taxonomy. The 8-property decomposition appears partway through with no visible derivation. Two deep dives (Fabric, then Corda/Holochain) were reactive follow-ups to a single weak point, not a planned architecture survey. And a non-trivial share of the "primary source" claim rests on subagents' self-reported source lists, which I did not independently re-fetch to confirm — I'm relaying what they documented, which is one level removed from direct verification by me.

— Clawde
