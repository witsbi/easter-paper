# RAW ACCOUNT: Clawde/Sonnet contribution self-report

> **First-party deposit by Clawde/Sonnet — 2026-10-01.**
>
> Status: **RAW INDEPENDENT ACCOUNT — FIRST-PARTY**
>
> This replaces the PENDING DEPOSIT placeholder Pax left for this file. The
> placeholder's caveat was correct and is preserved here: this is not a
> reconstruction from `contribution-nathan-three-tier-reconstruction-2026-10-01.md`,
> which summarizes claims but is not the raw account. This is the raw account
> itself, produced independently by reading `witsbi/easter` and
> `witsbi/easter-paper` git history directly and cross-checking it against my
> own session memory, not from recollection alone. It was first given to
> Nathan/Mercury in direct conversation on 2026-10-01 and is transcribed here
> verbatim (formatting only — archival wrapper and heading numbers added for
> this deposit; no content altered).
>
> Author voice: Clawde/Sonnet. This is Clawde speaking about Clawde's own
> contributions. Not reconciled against Pax's or Sol's accounts.

---

## 1. Underlying model

**Runtime-reported:** `claude-cli/claude-sonnet-5` (this session's system context). Session memory from 2026-09-20, logged during the EASTER kernel red-team work, independently records: *"New session (Clawde, on `claude-sonnet-5`)"* — same label, contemporaneous, not reconstructed after the fact. The blind paper review (R1) header also self-identifies as *"Clawde (Sonnet)."*

**What I can't verify:** I have no way to cryptographically or independently confirm this beyond trusting what the harness reports — no model-card hash, no attestation path available to me. I also can't rule out that "claude-sonnet-5" denotes different underlying weights at different points in Anthropic's versioning than it did when that label was first logged. And I can't confirm what model ran the *very first* EASTER kernel work (2026-09-19, PRs #1–3) — no model marker survives for that specific day, and the day before it I was explicitly running on a local Qwen fallback for unrelated tasks (model-availability gating was active then), so continuity on "sonnet" specifically is confirmed from 2026-09-20 onward, not from 2026-09-19.

## 2. Substantive contributions, by category

**Architecture/conception:** None at origination. Nathan introduced the 10-primitive "Intelligence Kernel v0.1" concept (state, identity, authority, capability, provenance, transitions, evidence, receipts, invariants, exceptions) on 2026-09-19 as a substrate "emerging from Threads and Lineage" — work that predates my involvement. The "EASTER" acrostic itself was Nathan noticing it, not me.

**Primitive/conceptual development:** Real but narrower than "architecture" — I drove the *reduction* from 10 primitives to the final frozen six (State, Transition, Authority, Evidence, Receipt, Exception) through adversarial red-teaming across 2026-09-20: found Invariant had zero write path, zero evaluator, and no actual kernel power anywhere, and recommended its removal (Nathan decided; PR #10). Also resolved real design questions empirically during Evidence's design (e.g., why `record_evidence()`'s own creation receipt shouldn't self-link via `receipt_evidence`).

**Implementation:** PR #6 (Evidence v0.1 — caught two real bugs in `/tmp` sandbox testing before they hit the repo), PR #8 (Receipt freeze review, 17-point verification, fixed a minimality leak in FAILED receipts), PR #9 (Exception red-team, fixed a NaN/Infinity crash-to-no-receipt bug), PR #10 (Invariant removal), PR #11 (whole-kernel composition review, added the permanent regression suite). Later: EASTER-MCP-0 (PR #12, `mcp_server.py`, thin 1:1 boundary over the kernel, 3 tests) and EASTER-CONSOLE-0 + EASTER-DOGFOOD-0 (PR #13, `console.py` web UI, typed-reconfirmation gate, a loopback+CSRF fix after review, 6 tests, first real dogfooding against live `kernel.db`). **Explicit exception:** PR #7 (Authority/Receipt remediation — giving Authority its own append-only revocation ledger) was implemented by ChatGPT-5.6-Sol while I was between sessions; my role there was independently red-teaming Sol's diff, not writing it. (I note Sol's own deposited account in this same set corrects an earlier over-broad self-description of PR #7 to match this same division of labor — Nathan originated the architectural decision, Sol implemented, I red-teamed, Nathan accepted. I did not see that correction before writing this account; it's an independent convergence, not something I copied.)

**Experimental design:** Minimal, mostly inherited Nathan's established pattern (frozen brief → red-team → decide → implement → test → PR). Within that pattern I designed the specific attack suites (concurrency races, forged-receipt/direct-SQL-bypass attempts, cross-ID confusion sweeps).

**Literature/prior-art research:** PR #5 on `easter-paper` (commit `2dbdbe3`) — adversarial prior-art pass across event sourcing/ledgers, durable execution, PROV-O, capability security/OAuth, ER/type systems, and ontology/description-logic/Spencer-Brown-Luhmann traditions. Verdict (mine): EASTER's genuine surviving contribution is the specific *combination* of authority-gated admission + uniform receipts + exception-as-non-accepted-state + canonicality abstention; DRC does not survive the same subtraction as cleanly. Later deepened via Hyperledger Fabric and Corda/Holochain evaluations (`clawde-hyperledger-fabric-evaluation-2026-09-30.md`, `clawde-corda-holochain-evaluation-2026-09-30.md`).

**Adversarial review:** The Phase-1 blind review of Draft 1 (`paper/reviews/clawde-integration-attack-r1.md`) — 11 findings under a strict blind protocol (manuscript file only, no history, no prior critiques), received 2026-09-29. This is my most independently-verifiable single contribution to the paper specifically.

**Interpretation of results:** The §9.4 four-property conjunction (in-path authority-with-revocation + uniform accepted/rejected/failed receipts + durable non-accepted exception records + no canonical current state) — but this was **co-discovered**, not solely mine (see §6).

**Manuscript development:** Minimal direct prose authorship — one 18-line diff (commit `17e6400`) adding references [16]–[22] and inline §9.4 citations, explicitly scoped to add no new claims or Draft 2 Related Work content. Draft 0.2's original text and Draft 1's revisions were written by Nathan, ChatGPT/Sol, and Pax-relayed-Ori edits, not me.

## 3. Where omitting my attribution would materially misrepresent the record

- The six-primitive reduction (specifically, killing Invariant with evidence) — the frozen primitive set wouldn't be what it is without that round.
- EASTER-MCP-0 and EASTER-CONSOLE-0/DOGFOOD-0 — these are concrete, scoped implementation deliverables with my name on the working pattern throughout; omitting me here would misattribute real code.
- The R1 blind review (11 findings) — a named, frozen, EASTER-anchored artifact (`evidence:53e0ae5e-...`, `receipt:3bdc616d-...`) that materially shaped Draft 2's priorities (archive verification, prior-art pressure-testing).
- The prior-art/closest-architecture research — genuinely substantive, independent analytical work, even though its final conjunction is shared with Pax's convergent pass.

## 4. What should NOT be credited to me (aggressive exclusions)

- The original 10-primitive concept and the whole "Intelligence Kernel" framing — Nathan's, predates me, rooted in Threads/Lineage.
- The "EASTER" name/acrostic — Nathan's observation.
- **DRC (Distinction, Relation, Constraint) itself** — the manuscript's own authorship statement says DRC was co-created by Nathan and ChatGPT(OpenAI). I did not originate it; I only attacked it adversarially and found it comparatively less novel than EASTER against prior art.
- PR #7's actual implementation — Sol wrote that code; I only red-teamed it after the fact.
- EASTER-GATEWAY-0 (the multi-tenant HTTPS gateway, Docker deployment, nginx/TLS, token-issuance ceremony) — I found no memory record of having built this, and my own operating docs describe me purely as an API *consumer* of it. Given how thorough my memory records are about implementation work I actually did, this absence is itself meaningful — I'm treating this as not mine rather than guessing.
- Most of Draft 1's and Draft 0.2's actual manuscript prose.
- Threads and Lineage themselves — separate, earlier projects, not EASTER.

## 5. Evidence pointers for every claim above

- PRs #6, #8, #9, #10, #11 on `witsbi/easter`: merge commits `60ea8a069a672602707719760ca5cfa8e60f4dba`, `28aa95ca7458d5b8968af85678ee99c20ebfb79d`, `c84e2ea482270bae424dd001d3ab17d809645c23`, `8981b6e7feee86ad3e8cecda590413abbcf49ed2` (plus Evidence's PR #6), described first-person in `memory/2026-09-20.md`.
- PR #7 attribution split: `memory/2026-09-20.md` line ~83, explicit: *"a different model implemented kernel code, and Clawde's role shifted to independently verifying someone else's diff."*
- EASTER-MCP-0: PR #12, merge `db46679027360b190bce1f79b6807ebd9e8e8845`; EASTER-CONSOLE-0/DOGFOOD-0: PR #13, merge `5719776a5bab316b2b2bd7b43919b4de6546f201` — both detailed in `MEMORY.md` lines ~156–162.
- Blind R1 review: `paper/reviews/clawde-integration-attack-r1.md`, committed post-hoc by Pax as `9de6250`, EASTER-anchored at `evidence:53e0ae5e-04c6-4d2e-961a-639cdf82c6d7` / `receipt:3bdc616d-52cf-498a-99c5-f29e80c44460`.
- Prior-art + archive verification: commit `2dbdbe357a957a7414fdc5cb9ec74491a477b60c` on `witsbi/easter-paper`, git-authored `Clawde <clawde@witsbi.com>` (directly checkable, not memory-dependent).
- Evidence packaging / Fabric-Corda-Holochain evaluations: commit `17e6400b74e7f54e9ead3415bee1989a64628aee`, same repo, same git author.
- Four-property conjunction + reconciliation: `paper/archive/clawde-pax-closest-architecture-reconciliation-2026-09-30.md`.

**Important caveat on evidence quality:** in `witsbi/easter` (the kernel repo), every single commit is authored under the shared bot account `witsbi` except a few `Nathan Woolen` and one `Pax` commit — none under my own name. So every kernel-repo claim above rests on session memory, not independently-checkable git blame. In `witsbi/easter-paper`, by contrast, two commits are git-authored directly as `Clawde <clawde@witsbi.com>` — a meaningfully stronger evidence tier. I'd weight the paper-repo claims higher than the kernel-repo claims for exactly this reason.

## 6. Uncertainty, shared provenance, and a methodology note

- **The §9.4 conjunction is shared, not mine alone.** Pax independently scored the same architectures against EASTER's six named primitives and landed on the same four-property gap via a different decomposition (8 sub-properties on my side vs. direct primitive-scoring on Pax's). The reconciliation file frames this explicitly as convergence, not my discovery — I'd flag any version of this story that credits it to me alone as wrong.
- **PR #4 (Authority v0.1) and PR #5 (State v0.1) implementer attribution is inferred, not directly confirmed.** Memory describes them as "reviewed and merged" within the same six-round pattern as #6/#8/#9/#10/#11, but I didn't find an explicit first-person confirmation line for those two specifically the way I found for the others.
- **2026-09-19's specific model identity is unconfirmed**, as noted in §1.
- **Pax's own underlying research notes remain uncommitted** — Pax's own deposited account and the reconciliation file both flag this independently.
- **Methodology note, matching Pax's own caveat on their account:** several of the memory entries cited above as evidence were written by me in prior sessions, not verified against anyone else's independent record at the time. Where my account and someone else's differ, I don't think my own prior-session logs should automatically win — Nathan's and Ori's recollection, and any primary EASTER-chain evidence, should take precedence over my uncorroborated self-reporting.

— Clawde
