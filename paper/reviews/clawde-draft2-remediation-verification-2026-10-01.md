# Clawde/Sonnet — targeted verification of Draft 2 post-adversarial remediation (findings #1–#4)

> **First-party deposit by Clawde/Sonnet — 2026-10-01.**
>
> Status: **TARGETED VERIFICATION, NOT A FULL RE-REVIEW**
>
> Commissioned directly by Nathan: verify the remediation in PR #15
> (`witsbi/easter-paper`, merge commit `0e6e06eb595f79cf121d1dfe561d619a03ce899a`)
> against findings #1–#4 of the frozen adversarial review
> (`paper/reviews/clawde-draft2-adversarial-review-2026-10-01.md`, PR #14)
> only. Findings #5–#6 (implementation/model correspondence; primitive
> minimality/DRC/corpus-methodology/conclusions) were explicitly out of scope
> and were not reopened, since none of the four remediations examined here
> created a contradiction touching that ground.
>
> Verified by diffing the reviewed commit (`6386f9927c6111205ca0b188c10c0c32353f5b50`)
> against the PR #15 merge commit directly — `git diff 6386f992..0e6e06e` — not
> by reading the PR description or commit messages alone.

---

**1. Corda Reference [3] / Appendix B — CLOSED**

Reference [3] now reads: *"M. Hearn and R. G. Brown, 'Corda: A distributed ledger,' technical whitepaper, version 1.0, 20 Aug. 2019... https://docs.r3.com/en/pdf/corda-technical-whitepaper.pdf"* — matches exactly what I confirmed by downloading and `pdftotext`-ing that PDF in the original review (title page: *Mike Hearn, Richard Gendal Brown, August 20, 2019, Version 1.0*). Appendix B.4's bullet is also corrected: it no longer frames this as a "mirror substitution" (which was the logical error — a different document, not a mirror) and now correctly states [3] "identifies the same Corda v1.0 whitepaper cited and quoted in the preserved closest-prior evaluation." Both the citation and the rule explaining it are now internally consistent with the archive.

**2. Two-identity gateway-authentication disclosure — CLOSED**

Section 8.6 now discloses that `identity:clawde` hit the same failure, cites a new first-party archive file (`pax-gateway-outage-operational-account-2026-10-01.md`), and both Section 8.6 and 10.10 report a root cause corroborated by actual logs rather than the "approximately three missed rotations" guess I'd repeated in my own finding. Worth noting on the merits, separate from closing the finding: the remediation's own paper trail (three sequential commits in the archive file) shows that guess was checked against real logs and found **wrong** — the broker minted every token successfully; `git push` of the distribution repo was silently failing in the cron context, so consumers kept presenting a token that expired `2026-09-30T20:16:14Z`, corroborated by actual gateway `403`/`200` log timestamps. The correction is append-only (old hypothesis preserved, not deleted), consistent with the paper's own provenance rules. This resolves the finding with stronger evidence than the finding itself had.

**3. Manifest finalization — CLOSED**

`PUBLIC-ARTIFACT-MANIFEST.md` Section C now reads: *"Immutable commit: `6386f9927c6111205ca0b188c10c0c32353f5b50`... merge commit for PR #13, containing the completed Draft 2 publication package used as the frozen Clawde/Sonnet adversarial-review target."* The self-referential staleness (manifest describing its own containing commit as "pending") is gone; it now names the exact commit I reviewed as the exact commit it describes.

**4. §11.6 portability-oracle independence safeguard — CLOSED**

A new paragraph was inserted directly after the oracle's seven-point spec: criteria and adjudication must be frozen before the trial, *"the person or system defining those criteria and the evaluator judging trial success should be independent of the EASTER development team or blinded to treatment condition. If that independence is unavailable, the resulting limitation should be reported explicitly rather than treating contributor agreement as independent validation."* This directly carries forward the §10.5 non-independence caution into the future-experiment design, which was exactly the gap — not that the oracle was undesigned, but that it didn't inherit a safeguard the paper applies everywhere else.

## Summary

| # | Target | Status |
|---|---|---|
| 1 | Corda Reference [3] / Appendix B | **CLOSED** |
| 2 | Two-identity gateway-authentication disclosure | **CLOSED** |
| 3 | Manifest finalization of reviewed commit | **CLOSED** |
| 4 | §11.6 portability-oracle independence safeguard | **CLOSED** |

All four CLOSED. No new contradiction surfaced that would warrant reopening findings #5–#6.

— Clawde
