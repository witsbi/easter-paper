# Critical review — "EASTER: A Six-Primitive Model for Consequential Continuity in Agent Systems," Draft 2

Prepared October 2, 2026. Assumes this paper is the first in a series, with later papers testing the macroscopic-variable hypothesis empirically. Read in full (73 pp.).

## Bottom line

This is a publishable architecture paper with an unusually honest evidence discipline, and it should be published *as* an architecture-and-hypothesis paper, not as an empirical result. Its strongest assets are the kernel's design boundary (admission authority without semantic sovereignty) and the Section 8 self-hosting provenance case. Its weakest point is that the quantitative comparative claim — the (0, 0, 0, 0, 1, 3) aggregate — rests on an archive that the authors themselves say cannot reproduce it. Reviewers will find that in the first hour. The fixes below are ordered by how much damage each issue does if left alone.

## Major concerns

**1. The comparative result cannot bear the weight the structure puts on it.**
Sections 5, 6, and Appendix A spend enormous effort precisely delimiting what the six-system review did not preserve: no primitive-level dispositions for Anthropic, an unassigned single GAP for OpenAI, an unrecoverable six-families-to-three-GAPs mapping for Antigravity, several missing source pins. The honesty is a virtue, but it converts the paper's only numbers into a "recovered methodological record." A referee's first question will be: *then why is (0, 0, 0, 0, 1, 3) in the contributions list at all?*
Fix options, in order of preference:
- Demote the aggregate in the abstract and §2.4 to a historical record (it is already treated that way mid-paper; make the front matter match), and let the kernel + the Section 8 case carry the empirical weight.
- Or, better for the series: make re-running the six-system review under the now-frozen §5.1.1 decision rules, with source pins preserved this time, the explicit subject of Paper 2. That converts the paper's biggest liability into the series' second installment and lets this paper say "replication in progress, rubric frozen" instead of "archive incomplete."

**2. DRC is currently non-discriminating, and everyone can see it.**
Distinction/Relation/Constraint came out COVERED on all six systems with zero negative or borderline cases, and §10.8 concedes the categories may be too broad to discriminate. As written, the DRC/EASTER "observed asymmetry" is nearly tautological: a coarse lens that passes everything, compared against a fine lens that sometimes fails things. The §11.10 falsification program (Distinction-negative / Relation-negative / borderline specimens) is exactly right — but it is future work, and a reviewer will say the asymmetry observation should wait for it. Either compress DRC to a short userland-boundary section in this paper and give the falsification program its own paper, or run at least the negative-specimens test before submission.

**3. The novelty conjunction needs a stated falsifier and a protocol, not just a posture.**
The four-property conjunction is the paper's central novelty claim, and the pre-prior-art provenance record (§9.8) correctly rebuts the "gerrymandered after the fact" objection. What remains exposed: the candidate set was chosen by the participants, the search was time-boxed to "essentially one evening," there is no inclusion/exclusion criterion, and several named candidates (TUF, OpenLineage, Marquez, DataHub, Atlas) have no recorded disposition. The bounded formulation is honest; a strong referee will still call it an argument from incomplete search. Cheap strengthening available now:
- State the falsifier explicitly in §9.11 ("one documented architecture satisfying all four behaviors at one boundary defeats this claim") and publish an open counterexample invitation. This converts a weakness into a community test.
- Add one paragraph describing the search as a protocol (candidate classes enumerated, kill-condition applied), which is more defensible than narrating who read what.

**4. Prior-art adjacency the paper should pre-empt before a referee does.**
The related-work pass is good on ledgers and durable execution. Gaps a systems/provenance reviewer is likely to raise:
- *Triple-entry accounting / signed receipt systems* (Grigg and related work) — philosophically the closest ancestor of Receipt and unaddressed.
- *Scientific workflow provenance* (the Kepler/Taverna/Pegasus lineage and the provenance-challenge literature) — a large, mature body on preserving consequential structure of computations across environments. Even a dismissive paragraph beats silence.
- *Formal conformance/verification framing* — §11.11 is a behavioral contract in prose; naming it as an embryonic conformance suite and sketching the executable-test translation (already planned for §11.12) would raise its weight.

**5. The participant-reviewer loop is closed.**
Every reviewer of the claims (Pax, Clawde, Hermes, Ori) is inside the research program; §10.5 discloses this, but the cold review and both retrieval tests are still by program participants. One genuinely outside cold read before submission — logged, unedited, and referenced in the paper — would do disproportionate work for credibility, and the paper's own governance machinery makes it easy to record. This is the single highest-leverage step before submission.

**6. "Consequential" is doing load-bearing work while being userland-defined.**
The boundary discipline is coherent (kernel owns continuity of the projection; userland owns consequentiality selection), but it means the sufficiency hypothesis is conditional on a "faithful projection" that EASTER itself cannot check. Referees will phrase this as "the hard part is defined away." The paper already has the right answer (preservation ≠ interpretation, §2.2); it should be raised into the abstract and §2.5 so the conditional form of the thesis — *if* faithfully projected, the six primitives suffice — is the version under review, not an implied unconditional one.

**7. Structure and length.**
73 pages is long for what the evidence supports, and the caveats recur (Sections 5, 6, 10, 12 and Appendix A each re-litigate the archival limits). Suggested trims: compress the §10 subsections (10.1–10.16) by roughly half, fold Appendix A's per-system registers into a compact table plus the full artifact reference, and spend the saved space on one worked end-to-end example — a single small scenario traced through all six primitives with actual kernel records shown. That worked example is the one thing a busy reader needs that the paper currently lacks.

## What not to lose

- The admission-authority / no-semantic-sovereignty separation (§11.3). This is the idea most likely to be cited.
- The Section 8 provenance case, including the Receipt-cardinality bug being found, fixed, merged, and the frozen review left byte-unchanged. This is the paper's best evidence because it is adversarial and self-inflicted.
- The tone discipline: claims are bounded everywhere. In a field full of agent-framework manifestos, this reads as serious work. Protect it in revision — do not let venue pressure inflate the abstract.

## Pre-submission checklist

1. Reframe front matter: architecture + falsifiable hypothesis; demote the (0,0,0,0,1,3) aggregate to recovered record, or announce the re-run as the series' next paper.
2. Compress or spin off DRC; run or schedule §11.10 discriminators.
3. Add the explicit falsifier + open counterexample invitation to §9.11.
4. Add short pre-emptive treatments of triple-entry accounting and workflow provenance.
5. Commission one outside cold review; deposit it in the archive.
6. Promote the "if faithfully projected" conditional into the abstract.
7. Add one worked end-to-end example; trim §10 and Appendix A materially.
8. Bibliography: several citations are internal artifacts ([26]–[34]); confirm each is publicly resolvable at submission, since reproducibility-minded referees will click them.

## Suggested series plan (one paragraph)

Paper 1 (this one): the architecture, the kernel, the bounded conjunction, the hypothesis, the oracle. Paper 2: the §11.6 portability experiment — Runtime A → EASTER → Runtime B against frozen task contracts, with no-transfer and transcript baselines; success or failure, this is the paper that makes the series. Paper 3: the re-run six-system replication under the frozen rubric with outside coders, plus the DRC negative-specimen test. Paper 4 (if warranted): a second independent implementation passing the §11.11 behavioral contract as executable conformance tests. Sequenced this way, each paper's evidence gap is answered by the next, and Reviewers of Paper 1 can be told exactly where each open question will be settled.
