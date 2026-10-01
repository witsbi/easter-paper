# Clawde/Sonnet — independent adversarial review of EASTER Draft 2 (frozen)

> **First-party deposit by Clawde/Sonnet — 2026-10-01.**
>
> Status: **FROZEN ADVERSARIAL REVIEW**
>
> Commissioned directly by Nathan/Mercury: *"perform an independent adversarial
> review of EASTER Draft 2... Your objective is to break the work, not improve
> it... Do not use or seek prior reviews, remediation history, or reviewer
> dispositions. Freeze your findings before any discussion with Nathan, Ori,
> or Pax."*
>
> **Reviewed targets (immutable pins):**
> - Manuscript: `witsbi/easter-paper` @ `6386f9927c6111205ca0b188c10c0c32353f5b50`
> - Reference implementation: `witsbi/easter` @ `8bf422747836c96233f8dc11d4b11d1a61c832c1`
>
> Deposited here **unchanged** — verbatim body, archival wrapper only, per the
> same convention established for prior first-party deposits in this archive.
> Not reconciled against any other participant's account or against any prior
> review of this or an earlier draft.
>
> **Methodological disclosure (stated in the review itself, repeated here):**
> the reviewer is not blind. Clawde/Sonnet is a named participant in the
> Section 8 provenance narrative under review and personally produced some of
> the prior-art research this manuscript cites. `paper/archive/*.md` review/
> remediation files and `HERMES-REMEDIATION-LEDGER.md` were deliberately not
> opened for this task, per instruction — but direct first-hand knowledge of
> events described in Section 8 could not be un-known, and was used in one
> finding below, flagged accordingly.

---

I spent the research budget reading the full Draft 2 manuscript (all 14 sections + both appendices) at the pinned commit and verifying specific claims against the reference implementation (`kernel.py`, `schema.sql`, `initialize.py`) and primary sources, rather than against the manuscript's own prose. Findings below, frozen.

## Findings

### 1. Citation integrity — Reference [3] does not identify the document actually cited — **SUCCEEDED**

`13-references.md` [3]: *"M. Hearn, 'Corda: A Distributed Ledger,' technical whitepaper, **version 0.5, 29 Nov. 2016**. Authoritative project-hosted copy: `https://www.corda.net/content/corda-technical-whitepaper.pdf`"*

But `paper/archive/clawde-corda-holochain-evaluation-2026-09-30.md` (part of the same accepted archive, reference [27]) explicitly cites and quotes, with page numbers, *"Mike Hearn & Richard Gendal Brown, 'Corda: A distributed ledger' (Technical Whitepaper), **v1.0, 20 Aug 2019**"* at `https://docs.r3.com/en/pdf/corda-technical-whitepaper.pdf`, with quotes like `[Hearn/Brown §6.1, p.22]`.

I downloaded the actual PDF at the URL the archive cites and extracted its title page with `pdftotext`:

```
Corda: A distributed ledger
Mike Hearn, Richard Gendal Brown
August 20, 2019
Version 1.0
```

This confirms the archive's citation is accurate and the published Reference [3] is not — wrong version (0.5 vs 1.0), wrong date (2016 vs 2019), wrong author list (Hearn alone vs. Hearn & Brown), wrong host. A reader trying to verify `[Hearn/Brown §6.1, p.22]` against the numbered bibliography would be pointed at a different document than the one actually quoted. Appendix B.4 explicitly anticipates and licenses *mirror → authoritative-copy* substitutions ("[3] may replace a historical third-party Corda mirror... without changing the manuscript's statement that the mirror was what Pax/Muse actually inspected") — but that licensed exception is about swapping a mirror for the *same* document, not substituting a different, earlier, differently-authored document. This is exactly the failure mode Appendix B's entire apparatus exists to prevent.

*Severity:* narrow but real — one bibliography entry, mechanically fixable, doesn't touch the architecture or the conjunction claim. But it is a genuine, primary-evidence-confirmed defect in the paper's own citation-integrity machinery, which the paper repeatedly holds up as a methodological strength.

### 2. Provenance evidence (Section 8) — the gateway-authentication-failure narrative is incomplete — **SUCCEEDED**, with the above COI caveat

Section 8.6 presents the expired `identity:pax` credential as a single, illustrative "unplanned boundary event," narrowly scoped to "not evidence of kernel Authority enforcement." That narrow claim is accurate as far as it goes. But I have direct first-hand knowledge — from being the acting participant, not from any archive file — that `identity:clawde`'s token *also* failed with the identical symptom (`invalid or expired token`, surviving a fresh pull against the current rotation commit) in the same operational window, and self-resolved only after whatever fix was applied for Pax's identity. Pax's own contemporaneous ops note (quoted in the same episode, not independently verified by me here) attributed this to the Mac-side token broker missing roughly three 12-hour rotations — a systemic, multi-identity outage, not an isolated single-credential event.

Section 8's "What the case demonstrates" list (8.8) and the Limitations section (10.10, "the expired gateway-credential event was naturally occurring rather than intentionally injected") both describe this in the singular. Nothing in Section 8 or 10 discloses that it was one of at least two near-simultaneous failures from a common root cause. This matters for the case study's evidentiary weight: a reader could reasonably take "one unplanned event" as weaker/more anecdotal than "a systemic rotation failure that happened to hit two of three AI identities around the same time," which is actually a more informative (and less flattering) fact about deployment fragility during the very episode being used as a positive demonstration of the architecture.

*Why I'm not more confident this rises higher than SUCCEEDED-but-narrow:* the manuscript's literal claims about Pax's event are accurate; this is an omission, not a misstatement, and the omitted fact doesn't touch EASTER kernel behavior (both failures were pre-kernel, at the gateway, exactly as the boundary claim says). It weakens the *case study's framing* more than the *architecture's claims*.

### 3. Provenance evidence — the manifest's self-reference is already stale at the commit under review — **SUCCEEDED, trivial severity**

`PUBLIC-ARTIFACT-MANIFEST.md`, Section C, at the exact commit I was asked to review (`6386f99`, which is itself the merge of PR #13): *"PR #13 adds the finalized Draft 2 bibliography... While the pull request remains open, no immutable merge commit can identify that completed package... After PR #13 is merged, its merge commit SHALL be recorded as the immutable Draft 2 adversarial-review candidate."*

This commit **is** that merge, which I confirmed directly (`git log -1`: `Merge pull request #13 from witsbi/draft2-publication-package`, commit `6386f992...`). The manifest embedded in its own target commit still describes itself as pending. It's a trivial, self-correcting documentation lag (the next commit that touches the manifest would presumably fix it), but worth naming since the manifest's entire purpose is precise self-reference.

### 4. Portability oracle (§11.6) — doesn't address its own non-independence risk — **UNRESOLVED**

The oracle design (task contract, migration cut, information boundary, acceptable-successor set, invalid-successor conditions, baselines, measures) is procedurally reasonable. But Section 10.5 already concedes the current research program's AI collaborators are not independent of each other ("their errors may therefore be correlated... Agreement... is treated as evidence of response convergence, not independent validation"). Section 11.6 doesn't carry that same caution forward: nothing in the oracle specification requires that whoever defines the "acceptable-successor set" (step 4) or judges a trial be independent of the team that built EASTER and has a stated interest in the portability hypothesis succeeding. Without that, a future positive result could reproduce exactly the non-independence problem the paper is otherwise careful to flag everywhere else. I can't classify this SUCCEEDED because no trial has been run yet — there's no behavior to falsify — but it's a credible, concrete gap in a design the paper otherwise treats as sufficiently specified for falsification.

### 5. Implementation/model correspondence — extensively verified, no defect found — **FAILED** (reported because the attacks were real attempts, not waived)

I read `transition()`, `record_failure()`, `_validate_grant()`, `revoke()`/`revoke_all()`'s `_count_other_valid_root_grants()`, and `initialize.py` directly against specific manuscript claims:

- **Authority-in-transaction-boundary claim (§4.2, §4.3):** confirmed in code — `_validate_grant` runs on the same connection, inside `BEGIN IMMEDIATE`, after the write lock is taken, with an explicit docstring naming the exact TOCTOU this closes. Matches.
- **Authority-ordering-independent-of-wall-clock claim (§4.3):** confirmed — `authority_seq` is a single monotonic sequence shared by `authority_grants` and `authority_grant_revocations` (`_next_authority_seq`), not derived from Receipts or timestamps. Matches.
- **`record_failure()` atomicity and minimal-Receipt/detailed-Exception split (§4.2, §4.6):** confirmed in code and comments (including the NaN/Infinity degrade-not-crash path and the "no phantom receipt" rollback guarantee). Matches almost verbatim.
- **Bootstrap exceptionalism (§4.7):** confirmed — `initialize_database()` is a one-shot file-creation script that refuses to run against an existing database path and is not reachable through any live-kernel operation. No way to mint a second genesis against a running instance.

I did not have budget to build a live concurrency-race harness against revocation (the one piece of adversarial testing Section 11.12 itself admits hasn't been done), so I can't claim to have exhausted this category — but every static/structural claim I checked against the actual code held up exactly as described.

### 6. Architecture / six-primitive sufficiency, minimality; DRC analysis; novelty boundary; corpus/reproducibility methodology; conclusions — **FAILED to find new ground**

I read these sections closely looking for overclaiming, circularity, or unacknowledged gaps, and didn't find anything the manuscript hasn't already conceded itself, usually more precisely than I could re-derive independently: the Invariant-rejection test is explicitly called "one explicit primitive-set test, not proof... minimality" (§6.6, §10.6); the DRC "no negative specimen observed" claim is explicitly flagged as indistinguishable from an unfalsifiable/overly-permissive definition and paired with a concrete negative-specimen falsification program (§7.4, §10.8, §11.10); the corpus-stopping rationale is explicitly labeled reconstructed-after-the-fact rather than preregistered (§5.6, §10.4); the aggregate GAP sequence `(0,0,0,0,1,3)` is internally consistent with Appendix A's per-system table; the conclusion (§12) doesn't introduce any claim not already bounded in the body. This document has clearly already been through serious adversarial pressure before reaching this commit — the obvious attacks are pre-empted in the prose itself, which made this review harder than I expected going in, not easier.

## Summary

| # | Target | Verdict |
|---|---|---|
| 1 | Citation integrity (Ref [3], Corda whitepaper) | **SUCCEEDED** |
| 2 | Provenance narrative completeness (§8.6) | **SUCCEEDED** (COI-disclosed) |
| 3 | Manifest self-reference staleness | **SUCCEEDED** (trivial) |
| 4 | Portability oracle independence gap (§11.6) | **UNRESOLVED** |
| 5 | Implementation/model correspondence (Authority, Receipt, bootstrap) | **FAILED** |
| 6 | Primitive minimality, DRC falsifiability, corpus/reproducibility, conclusions | **FAILED** |

Three real, narrow, fixable findings; one open design question for future work; the implementation itself held up under every concrete test I ran against it. This was frozen before discussion with anyone.

— Clawde
