# Independent cold review — EASTER manuscript

**Frozen target:** `witsbi/easter-paper` commit `ef81644f655294ecb7d863a9c6ce527f7fef214f`  
**Reference implementation inspected:** `witsbi/easter` commit `8bf422747836c96233f8dc11d4b11d1a61c832c1`  
**Review frozen:** 2026-10-01T19:45:59Z  
**Recommendation:** **Major revision / not publication-ready as an empirical systems paper.**

## Overall assessment

The manuscript presents a coherent small kernel and, unusually, states many of its boundaries precisely. The strongest part is the implementation-level architectural claim: the pinned Python/SQLite kernel does implement append-oriented records, immutable State through supported interfaces and triggers, explicit branching Transitions, Authority validation inside serialized write transactions, separate diagnostic Exceptions, and accepted/rejected/failed Receipts subject to the stated persistence boundary. I found no material contradiction in those central implementation claims.

The submission is not publication-ready because its principal comparative evidence is not independently reproducible from the submitted package and, for several systems, is not independently auditable even at the level needed to support the reported aggregate. The package preserves a later reconstruction of outcomes, not the original study materials. The DRC/EASTER non-entailment result inherits that evidentiary weakness. The operational provenance case likewise lacks the kernel record export and underlying logs necessary to verify its material event claims. The related-work claim is carefully bounded as non-identification, but the search is knowingly incomplete in candidate classes most likely to defeat it. These are substantive evidence and methodology defects, not formatting defects.

## Substantive findings

### 1. The six-system comparative result is a report of a recovered assertion, not a reproducible architectural result — major

The headline sequence `(0, 0, 0, 0, 1, 3)` appears in the abstract and conclusions, but the submission explicitly concedes that the complete original review dataset was not preserved (`paper/draft2/05-evaluation-methodology.md:128-147`). The decisive recovery artifact describes itself as an “archival reconstruction,” not the original freeze (`paper/archive/frozen-review-recovery-2026-09-29.md:1-5`).

The evidentiary deficits are not peripheral:

- Anthropic has only a zero-GAP aggregate; no primitive classifications, OPEN findings, composition reasoning, or exact reviewed version survive (`APPENDIX-A-COMPARATIVE-EVIDENCE-REGISTER.md:98-113`).
- OpenAI has only the assertion that exactly one GAP existed; its primitive, source version, and supporting analysis are missing (`APPENDIX-A-COMPARATIVE-EVIDENCE-REGISTER.md:115-129`).
- Antigravity has six recovered issue families but no recovered rule mapping them to the reported three-GAP aggregate, no Receipt freeze, and no exact runtime version (`APPENDIX-A-COMPARATIVE-EVIDENCE-REGISTER.md:131-175`).
- Hermes and LangGraph lack exact source pins; much of the DRC primitive evidence is missing (`APPENDIX-A-COMPARATIVE-EVIDENCE-REGISTER.md:19-26`).

The manuscript is commendably candid about this, but candor does not restore evidentiary support. A reader can reproduce that the manuscript accurately transcribes the recovery artifact; a reader cannot reproduce or adequately challenge the historical classifications themselves. The aggregate should therefore not be presented as a substantive empirical finding in the abstract or conclusion. At most, it is a historical outcome reported by the research program with incomplete supporting records.

**Required remedy:** either (a) conduct and publish a new, prospectively specified review with exact source pins, complete primitive-level evidence, coder decisions, and composition rules, clearly replacing the historical aggregate as the empirical study; or (b) demote the entire six-system comparison to an explicitly anecdotal/method-development record and remove the numeric sequence from the abstract and principal conclusions.

### 2. The DRC/EASTER “bounded non-entailment” is logically conditional but not robustly established by the package — major

The inference depends on both D/R/C COVERED classifications and EASTER GAP classifications for OpenAI and Antigravity. Yet individual DRC receipts are absent across much of the corpus, OpenAI’s EASTER GAP cannot be assigned to a primitive, and Antigravity’s composition is unrecovered (`paper/draft2/06-comparative-architectural-results.md:100-120`; Appendix A above).

Further, DRC has no negative specimen, no ablation, and categories broad enough that the manuscript itself recognizes possible non-discriminability (`paper/draft2/07-userland-continuity-boundary.md:59-75`; `10-limitations-threats-to-validity.md:98-112`). Thus the formal-looking `DRC-covered ⇏ EASTER-covered` statement is true only relative to classifications that cannot be independently reconstructed. It should not be described as “establishing” even a bounded empirical relationship without a reproducible classification package.

**Required remedy:** execute the negative/borderline program already proposed in §11.10 and re-run the relevant system classifications under frozen rules and independent adjudication. Until then, characterize the asymmetry as an observation in the authors’ recovered coding record, not an established result.

### 3. The operational provenance case is not independently verifiable at the claimed kernel-event level — major

The manuscript admits that it does not publish a stable-ID export sufficient to reconstruct the six-primitive event graph (`paper/draft2/08-easter-in-use-contribution-provenance.md:82-96`). That omission prevents verification of the most EASTER-specific part of the case: which operations reached the kernel, which Evidence and Receipts were created, and how they relate.

The gateway narrative is also supported only by a first-party operational account that quotes or summarizes logs; the logs themselves are not in the package. The account’s own chronology contains an initial diagnosis, an addendum saying the root cause was not established, and a later correction claiming it was established from a different broker log (`paper/archive/pax-gateway-outage-operational-account-2026-10-01.md:9-38`). The final story may be correct, but the submission package supplies the narrator’s report of the logs, not primary log evidence. Section 8.6 states precise expiry and request times as log-corroborated facts (`08-easter-in-use-contribution-provenance.md:98-112`) that an external reviewer cannot verify from the package.

**Required remedy:** publish a redacted, immutable export of the relevant EASTER records with stable identifiers and hashes, plus minimally sufficient redacted gateway/broker log excerpts or machine-verifiable summaries whose derivation is supplied. Otherwise narrow the case to the Git-visible contribution artifacts and label the kernel/gateway account as first-party testimony.

### 4. The reference implementation is coherent, but the submitted reproducibility path is incomplete and the test corpus is not a runnable suite — major for artifact evaluation, moderate for the architecture claim

At the pinned implementation commit, installation succeeded under Python 3.14 using `requirements-mcp.txt`, and 28 scripts passed when run individually against fresh initialized databases. Core adversarial scripts confirmed transaction serialization, branching, revocation behavior, rollback, Exception/Receipt separation, and immutable records.

However, the repository supplies no test runner, no declared Python version range, and no fixture/orchestration instructions for the script collection. A naive run of all `tests/*.py` is invalid: some files are explicitly retired historical scripts (`tests/authority_0b_0f.py:1-26`), some require a pre-populated development database with hard-coded record IDs, some assume corpus size from that development database, and `initialize_test.py` fails when executed by path because it does not add the repository root to `sys.path` (`tests/initialize_test.py:12-16`). The checked-out repository does not include the `data/kernel.db` expected by many scripts. Running each script against a fresh initialized database produced eight failures caused mainly by hidden fixture/sequencing assumptions; attempting the documented-looking historical sequence still failed because `authority_0b_0f.py` hard-codes a prior generated state ID.

This does not refute the implementation invariants I directly exercised, but it means the paper’s “regression evidence” is not packaged as a reproducible verification procedure.

**Required remedy:** provide one documented command that builds all fixtures and runs only current tests from a clean clone; separate historical experiments from executable tests; declare supported Python/SQLite versions; ensure every current test is hermetic or explicitly orchestrated; publish expected pass counts.

### 5. Receipt outcome uniqueness is assumed by supported entry points, not enforced as a kernel invariant — moderate

The `receipts` schema does not make `operation_id` unique (`schema.sql:327-351`). `Kernel.record_failure()` accepts a caller-supplied operation ID and does not reject an ID that already has an ACCEPTED Receipt (`kernel.py:587-812`). The repository’s own `exception_1_attacks.py` demonstrates that an ACCEPTED and a later FAILED Receipt can coexist for the same operation ID (“EXC-6c FINDING”).

Ordinary supported operations generate fresh UUID operation IDs, so this does not break the normal entry points I tested. But it weakens the manuscript’s singular phrasing that a Receipt records “the outcome” of an attempted operation and leaves the authoritative meaning of conflicting Receipts underspecified. If `record_failure()` is internal-only, that boundary should be mechanically enforced rather than conventional.

**Required remedy:** make failure recording private/unreachable from supported interfaces and document operation-ID uniqueness as an entry-point invariant, or enforce one terminal Receipt per operation in schema/kernel behavior and add a conformance test.

### 6. The novelty claim is defensibly worded but not yet a strong publication contribution — major for a novelty-based venue

The manuscript properly disclaims novelty of individual mechanisms and limits the claim to non-identification within examined material (`paper/draft2/09-related-work-novelty-boundary.md:199-217`). It also preserves evidence that the four-property conjunction predates the closest-prior search; repository history confirms the relevant implementation/paper commits preceded the closest-architecture commit.

But the search is intentionally non-systematic, time-boxed, directed toward preselected families, and acknowledges unexamined candidates including permissioned non-canonical/sharded architectures and named systems whose screening status is unknown (`09-related-work-novelty-boundary.md:13-41,181-197`). Most search work was delegated to AI research agents, and some orchestrators did not reopen the cited sources. The bibliography is dominated by product documentation and broad architectural references, with limited engagement with academic work on event sourcing, audit logs, workflow provenance, authorization, and distributed histories.

The resulting statement—“we did not identify”—is supportable as a report of that bounded search. It is not enough to establish architectural novelty at the level normally expected for a research contribution. The paper’s value must therefore rest primarily on the artifact and problem formulation unless the prior-art study is strengthened.

**Required remedy:** conduct a documented systematic search with databases, queries, dates, inclusion/exclusion rules, citation chaining, candidate disposition table, and focused coverage of the acknowledged high-risk classes. Have a reviewer not involved in EASTER adjudicate behavioral equivalence against the conjunction.

### 7. The central portability/sufficiency hypothesis is not evaluated — appropriately disclosed, but it limits the paper’s present contribution

The motivating claim is that six macroscopic variables may suffice for continuation across heterogeneous runtime change. No heterogeneous-runtime continuation experiment is presented. The six-system review tests classification fit, not continuation; the provenance case tests record use, not semantic portability. The manuscript states this correctly (`paper/draft2/11-discussion-research-implications.md:114-176`).

Accordingly, the paper currently demonstrates an implementable record model and proposes a future experiment; it does not demonstrate the title-level implication “continuity in agent systems” beyond preservation/inspectability of projected records. Venue positioning should reflect this: architecture/proposal paper, not validated continuity result.

## Important challenges attempted and adequately supported

1. **Authority/revocation race safety.** I checked whether grant validation occurred before acquiring the write lock. It occurs on the same connection after `BEGIN IMMEDIATE`, and the concurrency probe showed revocation and transition serialize coherently (`kernel.py:91-105,344-444`; `tests/whole_kernel_concurrency.py`). This claim is supported within SQLite’s single-writer model.

2. **Authority independence from State and wall-clock ordering.** Grants and revocations share `authority_seq`; revocation validity does not derive from State, Receipt payloads, or timestamps (`kernel.py:236-338`; `schema.sql:77-170`). The relevant manuscript description is accurate.

3. **Accepted atomicity and failed-operation separation.** Accepted Transition writes and Receipts occur in one transaction; failed requested writes unwind before a separate failure-recording transaction persists a Receipt/Exception. Adversarial scripts exercised integrity failures, unexpected exceptions, and fallback-persistence failure without partial authoritative State. The manuscript’s persistence caveat is correctly bounded.

4. **Branching and absence of canonical current State.** The schema permits multiple outgoing Transitions, enforces one incoming Transition per non-genesis successor via unique `to_state_id`, and contains no head/current-state field or operation (`schema.sql:172-257`). Concurrent branch creation succeeded. This design claim is supported.

5. **Bootstrap exceptionalism.** Initialization refuses an existing destination and atomically publishes a fresh database; the one Genesis State and bootstrap Receipt are created outside ordinary live-kernel admission (`initialize.py:23-139`). The manuscript does not disguise bootstrap as an ordinary authorized operation.

6. **Conjunction chronology.** The relevant EASTER implementation commits (`435e3199`, `a5341487`, `0031fd20`) and the earlier paper commit `9d23bc0` precede the closest-architecture commit `2dbdbe3`. This supports the narrow anti-gerrymandering claim. It does not prove novelty, and the manuscript correctly says so.

7. **Boundary discipline.** The manuscript repeatedly and correctly excludes authentication, truth, semantic interpretation, external exactly-once effects, canonical branch selection, projection completeness, and storage compromise. I did not find those exclusions silently reversed in the implementation description.

## Editorial and presentation issues

These are secondary to the evidence defects above:

- `README.md:17-20` still says “Early drafting” and “Nothing here is submission-ready,” inconsistent with a frozen publication package.
- `PUBLIC-ARTIFACT-MANIFEST.md` does not identify the actual reviewed commit `ef81644`; its latest named package is `6386f99`, so the manifest is stale for this submission.
- The submission is fragmented across section files and does not provide a built paper/PDF or a deterministic build command.
- Section 9 relies on Appendix B’s claim map rather than conventional inline citations at many consequential claims, making source-to-sentence auditing unnecessarily difficult.
- “Six mature agent architectures” is insufficiently defended for a heterogeneous set that includes managed/partially observable products and a comparatively new Antigravity target.
- The abstract foregrounds the numeric aggregate despite the manuscript’s later admission that it is not fully reproducible; this misallocates emphasis even though caveats are included.
- Several sections repeat the same boundaries at length. The manuscript could be shortened substantially after the empirical record is repaired.

## Publication-readiness decision

**Not ready for publication in its present form; major revision required.**

The kernel artifact and its architecture are credible enough to support a focused systems/design paper. The present manuscript, however, asks the comparative reconstruction, DRC overlay, provenance case, and bounded novelty search to carry more evidentiary weight than the frozen package can independently support. The defects are repairable, but not editorially: they require a new reproducible comparative study, publication of primary case-study records, a clean artifact test harness, and a stronger prior-art search.

A publishable revision should narrow its demonstrated contribution to what the artifact proves, or produce new evidence for the broader empirical claims. The current conclusions are generally careful in wording, but the abstract and repeated headline sequence still make the package appear to establish more than an external reviewer can reproduce.