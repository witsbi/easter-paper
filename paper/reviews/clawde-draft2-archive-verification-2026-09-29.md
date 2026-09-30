# Clawde archive verification (sighted, Draft 2)

- **Reviewer:** Clawde (Sonnet), direct conversation with Nathan
- **Date:** 2026-09-29
- **Status:** sighted (post role-transition, `paper/reviews/clawde-role-transition-2026-09-29.md`)
- **Mandate item:** archival evidence verification (per `clawde-integration-attack-r1.md` review point #2, and the onboarding brief's sighted-mandate item 2)
- **Basis:** `paper/archive/recovered-review-state-2026-09-29.md`, `paper/archive/frozen-review-recovery-2026-09-29.md`, both read in full at commit `c269ff4` (current `main`).

---

## Task

My R1 review (blind to GitHub/EASTER at the time) flagged, as review point #2, that "the comparative evidence table is largely unverifiable as submitted": missing commit SHAs for most systems, missing primitive-level receipts, aggregate-only results for the Anthropic and OpenAI Agents SDK rows, and one recollected finding (an OpenAI Evidence OPEN) that should be treated as unsupported. The sighted mandate asked me to check that claim against the actual recovery state in `paper/archive/` and correct or confirm it.

## Finding: confirmed, not corrected

Both archive files independently corroborate the R1 claim in more detail than the manuscript's §8 table alone shows:

- **Missing source/version pins**: confirmed for Hermes, LangGraph, Anthropic SDK, and OpenAI SDK (OpenClaw is the only system with an exact commit pin, `2ef3b4a0…`, and even that is abbreviated).
- **Aggregate-only rows**: Anthropic SDK's primitive decomposition is explicitly "currently unknown" per the recovery artifact — "EASTER primitive cells must remain unknown unless original artifact is recovered." OpenAI SDK's aggregate is "exactly 1 GAP" with primitive attribution unknown.
- **Quarantined recollection**: the recovery artifact explicitly states "Ori previously recalled an OpenAI Evidence review with 0 GAP / 1 OPEN, but no preserved artifact was recovered to support that recollection... do not use that recollection as evidence" — matching my R1 caution exactly.
- **0 GAP ≠ six clean primitives**: the recovery artifact makes this point explicitly and by name for Hermes (H-OPEN-1), OpenClaw (OC-OPEN-1, OC-OPEN-2), and LangGraph (multiple primitive-level OPENs) — a nuance the manuscript's §8 table now (as of the merged Draft 1) states directly, which is good, but the underlying archive shows the nuance runs deeper than the table's prose conveys.

No correction is needed to R1 point #2. The archive doesn't contradict the claim; it substantiates it with more specificity than was available to make the claim in the first place.

## Note on process

This verification was done by reading the two archive files directly via the GitHub API (`gh api repos/witsbi/easter-paper/contents/...`), not by re-deriving conclusions from memory or from the manuscript's own summary of itself, per the recovery artifact's own rule G: "do not infer any missing primitive status from remembered summaries."
