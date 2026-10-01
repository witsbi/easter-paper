# 5. Evaluation Methodology

We evaluated EASTER through source-oriented architectural reverse review rather than through benchmark scoring. The purpose of the review was not to rank agent systems or determine whether a system was well designed. It was to ask a narrower question: within an inspectable system boundary, where are the continuity properties represented by EASTER demonstrably preserved, unresolved, absent, or challenged?

The method evolved during the research program. Draft 2 therefore distinguishes procedures that were actually used and preserved from methodological rationales reconstructed afterward. No retrospective rationale is presented as preregistered methodology.

## 5.1 Reverse review

For each inspected architecture, EASTER's primitives were used as lenses against source code, public technical documentation, and other inspectable system evidence available within the review boundary.

Findings use four dispositions:

- **COVERED** — the required property is demonstrated by inspectable architecture or behavior within the reviewed boundary.
- **OPEN** — available evidence is insufficient to resolve whether the property is covered.
- **GAP** — the property is not demonstrated within the inspected system boundary.
- **CHALLENGED** — evidence attacks the adequacy of the primitive or review lens itself rather than merely showing that the inspected system does not provide it.

These labels are architectural dispositions, not scores. They are not additive measures of system quality, maturity, safety, or capability.

A GAP can represent an intentional product or architectural tradeoff. Privacy requirements, deletion guarantees, security boundaries, simplicity, cost, or limited observability may all justify not preserving a property that EASTER would preserve. Conversely, COVERED does not establish that an implementation is complete, correct, secure, or optimal.

### Operational decision rule

The surviving research record supports a common decision rule even though the original reviews were not conducted from a single preregistered coding manual.

For each primitive-level question, the reviewer identifies the continuity property being tested, the inspectable boundary, and the strongest source or behavior available inside that boundary. The disposition is then assigned as follows:

1. **COVERED** only when the inspected evidence demonstrates the property within the stated boundary.
2. **OPEN** when the evidence does not establish either coverage or absence—for example because the relevant behavior is hidden behind a managed or compiled boundary, documentation is ambiguous, or an external-effect window cannot be resolved.
3. **GAP** when the inspected architecture exposes enough of the relevant boundary to show that the property is not provided there. Absence of public evidence alone is not sufficient for GAP when the underlying mechanism is unobservable; that case remains OPEN.
4. **CHALLENGED** when the evidence indicates that the EASTER primitive or lens itself is inadequate to describe the continuity problem, rather than merely showing a missing mechanism in the inspected system.

A disposition is therefore a claim about **evidence within a bounded architecture**, not a claim about an entire vendor or product beyond what was inspected.

This operational statement is a reconstruction of the method evidenced by the surviving reviews and their dispositions. It is included to make the interpretation of the labels reproducible. It must not be read as a claim that every historical review was executed from this exact written checklist; no such preregistered coding manual was preserved.

## 5.2 Primitive review and whole-system composition

The review method separates two analytical layers.

**Primitive review** asks whether individual EASTER properties are demonstrated at specific points in the inspected architecture.

**Whole-system composition** asks whether mechanisms distributed across the architecture collectively resolve, preserve, or leave open the continuity question raised at the primitive level.

This distinction became important in the recovered corpus. Hermes, OpenClaw, and LangGraph each retained OPEN findings during primitive-level review while producing no demonstrated aggregate GAP after whole-system composition. A primitive-level OPEN therefore cannot be mechanically promoted into a system-level GAP, nor can an aggregate zero-GAP result be interpreted as uncomplicated primitive-by-primitive coverage.

The method consequently preserves primitive findings and composition findings separately.

Whole-system composition is not an arithmetic reduction. A reviewer must identify the primitive-level concern and the additional mechanism or interaction that resolves it, leaves it OPEN, or demonstrates a GAP at the composed boundary. Where that reasoning was not preserved, Draft 2 does not reconstruct it from the final aggregate.

This limitation is particularly important for Google Antigravity. Six conceptual issue families survive archival recovery, while the frozen whole-system result contains three GAPs. The rule or case-by-case reasoning that reduced those six families to the final three was not recovered. Draft 2 therefore reports both facts and explicitly leaves the mapping unknown.

Aggregate dispositions are descriptive summaries of the frozen review outcome. They are not calculated scores and must not be reverse-engineered to invent missing primitive classifications.

## 5.3 Evidence discipline and unknowns

The review uses the strongest recoverable evidence available for each finding. Where source-level or primitive-level evidence has not been recovered, the classification remains unknown rather than being reconstructed from aggregate counts or researcher recollection.

This rule matters because archival completeness is uneven across the six-system corpus. Some systems retain substantial primitive-level review artifacts, while others currently retain only aggregate findings. Draft 2 therefore treats archival completeness as a separate dimension from architectural disposition.

An aggregate finding may establish that a review reached a particular disposition without establishing which primitive produced it. In such cases, the aggregate result may be reported, but the missing primitive mapping remains explicitly unknown.

Unverified recollections are not used to fill those gaps.

The September 29 recovered-review artifact is itself an archival reconstruction from previously preserved research state. It records both recovered findings and explicit non-recovery. It is evidence for what the research program successfully preserved; it is not represented as the original primitive-by-primitive review package.

## 5.4 Review boundary

Every disposition is bounded by what could actually be inspected.

For open-source systems, this may include source code and repository documentation. For managed systems, the observable boundary may be limited to public documentation, exposed interfaces, or behavior visible to the research program.

A GAP therefore means that the property was not demonstrated within the inspected boundary **where that boundary was sufficiently observable to support an absence finding**. If available evidence cannot distinguish absence from an unobservable private mechanism, the appropriate disposition is OPEN rather than GAP.

This observability asymmetry is particularly important when comparing open and managed systems and is one reason the review is not a vendor ranking.

## 5.5 Corpus and chronology

The initial corpus contains six mature agent architectures:

- Hermes Agent
- OpenClaw
- LangGraph
- Anthropic Claude Agent SDK
- OpenAI Agents SDK
- Google Antigravity

The corpus is **pre-disclosure** with respect to the combined EASTER/DRC framework: these systems were not designed in response to the framework as presented in this paper.

EASTER and several EASTER reverse reviews preceded the later DRC formulation. DRC was subsequently frozen and applied to the corpus without changing its definitions to fit individual targets. Where practical, DRC classifications were frozen before overlay with prior EASTER findings.

This chronology reduces one route for retrospective fitting, but it does not create independent evaluation. The reviews were conducted within one research program involving substantial human–AI collaboration.

Accordingly, Draft 2 describes these results as **pre-disclosure architectural observations**, not independent validation or independent replication.

## 5.6 Corpus selection and stopping limitation

The six systems do not constitute a statistical sample.

They are mature agent architectures selected in a research program concerned with continuity, representation, memory, and agent-system behavior. The corpus is therefore biased toward systems likely to contain comparatively rich mechanisms.

The survey stopped after six systems. The rationale that repeated DRC saturation suggested additional mature frameworks would add sample count more readily than conceptual diversity was reconstructed after the stopping point rather than frozen as a preregistered stopping rule.

We therefore treat the stopping decision as a limitation, not as evidence of methodological saturation.

Untested systems remain available for later out-of-sample or independent replication rather than being retroactively incorporated into the initial corpus.

## 5.7 Response isolation and adversarial review

Parts of the broader research program used multiple AI collaborators for adversarial review and reconstruction.

Where reviewers were intentionally isolated, the isolation prevented direct reviewer-to-reviewer anchoring during that review round. It did not make the reviewers historically independent: they shared the same human research program and overlapping project vocabulary.

Agreement between isolated reviewers is therefore treated as convergence of independently produced responses to the same frozen material, not as independent scientific replication.

Disagreement is preserved rather than resolved by vote. Where competing interpretations affect a consequential claim, the intended resolution mechanism is evidence: inspect the underlying source or artifact, preserve the competing claims, and revise the manuscript only to the degree supported by the evidence.

## 5.8 Projection and interpretation limits

EASTER reverse review evaluates continuity structure, not semantic truth.

A system may preserve every reviewed continuity property while receiving an incomplete or distorted projection from userland. Conversely, a system may intentionally avoid durable preservation while maintaining rich semantic structure internally.

The method therefore does not infer semantic adequacy from EASTER coverage.

Likewise, the later DRC overlay and EASTER review operate at different layers. DRC concerns functional representational structure in userland; EASTER concerns the continuity of consequential work after projection. Their findings must not be collapsed into a single score or maturity measure.

## 5.9 Reproducibility status

The present corpus has uneven archival completeness. The comparative result is therefore **partially reproducible from the preserved package, not fully reproducible at primitive level for all six systems**.

For Hermes Agent, OpenClaw, and LangGraph, substantial primitive-level findings survive. For Anthropic Claude Agent SDK, only the zero-GAP aggregate survives. For OpenAI Agents SDK, the one-GAP aggregate survives but its owning primitive does not. For Google Antigravity, substantial primitive findings and six issue families survive, but the exact composition mapping to the frozen three-GAP aggregate and the Receipt freeze do not.

The publication package should preserve, where available:

- exact source commit, tag, version, or review date;
- primitive-level findings;
- whole-system composition findings;
- final frozen disposition;
- source evidence supporting consequential classifications; and
- explicit unknowns where those materials were not recovered.

The September 29 recovered-review artifact is the **authoritative reporting artifact for the recovered comparative state** used by the manuscript. It is not the original review package, and its explicit unknowns are part of the result.

Accordingly, a reader can reproduce the derivation of the manuscript's comparative table only to the resolution preserved by that artifact. The paper does **not** claim that a reader can independently derive every historical primitive classification or the aggregate sequence `(0, 0, 0, 0, 1, 3)` from a complete original review dataset, because that dataset was not preserved.

A future replication may re-review the same systems under the now-explicit decision rules, but its results would constitute a **new replication**, not a reconstruction of the missing historical cells. Such a study may confirm, narrow, or disagree with the frozen historical aggregate without changing what the original record preserved.

Missing evidence is not silently regenerated from the manuscript.

This methodology therefore supports a bounded claim: the paper reports what the preserved review process demonstrated within its inspected boundaries and identifies where that demonstration is no longer independently reproducible from the surviving archive. It does not claim exhaustive architectural knowledge, statistical representativeness, complete historical reproducibility, or independent replication.