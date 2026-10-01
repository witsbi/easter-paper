# 10. Limitations and Threats to Validity

The results in this paper are bounded by the size and selection of the architectural corpus, uneven archival completeness, the observational nature of several findings, the absence of formal minimality proofs, and the scope of the prior-art investigation.

These limitations constrain the claims that can be made from the present work.

## 10.1 Small and non-random architectural corpus

The comparative study examined six mature agent architectures:

- Hermes Agent;
- OpenClaw;
- LangGraph;
- Anthropic Claude Agent SDK;
- OpenAI Agents SDK; and
- Google Antigravity.

These systems do not constitute a statistical sample of agent architectures.

They were selected within a research program already concerned with continuity, representation, memory, and agent-system behavior. The corpus is therefore biased toward comparatively mature systems likely to contain rich continuity mechanisms.

The observed EASTER and DRC results should not be generalized statistically to agent systems as a population.

The absence of a demonstrated EASTER GAP in four of the six systems likewise should not be interpreted as an estimate of the prevalence of EASTER-like properties in agent architectures generally.

## 10.2 Uneven observability

The inspected systems differed substantially in how much of their architecture was available for review.

Open-source systems permitted source-oriented inspection. Managed systems exposed a narrower boundary consisting primarily of public documentation, interfaces, and behavior visible to the research program.

A GAP therefore means that a property was not demonstrated within the inspected boundary. It does not establish that no corresponding internal mechanism exists.

Conversely, COVERED means that sufficient evidence was identified within the review boundary to support the particular disposition. It does not establish implementation-wide correctness, security, or completeness.

Comparisons across systems must therefore account for observability asymmetry.

## 10.3 Uneven archival completeness

The publication archive is incomplete at the primitive level for portions of the six-system review.

Some systems retain detailed primitive sweeps and whole-system composition findings. Others retain only aggregate results. Exact source commits, versions, individual DRC receipts, or primitive matrices are missing for portions of the corpus.

The paper does not reconstruct those missing classifications from aggregate counts or present-day recollection.

This preserves provenance fidelity but limits reproducibility.

The comparative table should consequently be understood as a report of the strongest preserved review state currently available, not as a normalized benchmark dataset with equal evidentiary depth for every system.

## 10.4 Review evolution and retrospective rationale

The reverse-review method evolved during the research program.

Not every methodological decision was preregistered or frozen before the corresponding review. In particular, the rationale for stopping the initial six-system corpus was reconstructed after the stopping point.

Draft 2 therefore distinguishes procedures preserved as actually performed from explanations developed retrospectively.

Retrospective explanation may help interpret the research process, but it cannot acquire the evidentiary status of a preregistered decision merely because it is plausible.

## 10.5 Human–AI research dependence

The work was produced through substantial collaboration among a human researcher and multiple AI systems.

AI collaborators participated in architectural analysis, implementation, adversarial review, literature investigation, experimental design, provenance reconstruction, and manuscript development.

Some review rounds intentionally isolated AI responses to reduce direct reviewer-to-reviewer anchoring. Such isolation does not create independent scientific replication.

The collaborators shared a research program, overlapping vocabulary, common artifacts, and human-mediated context. Their errors may therefore be correlated even when individual responses were produced separately.

Agreement among the collaborators is treated as evidence of response convergence, not independent validation.

Where disagreement mattered, the intended resolution mechanism was inspection of primary evidence rather than majority vote.

## 10.6 No proof of EASTER minimality

No preserved review artifact records a CHALLENGED disposition against an EASTER primitive in the recovered corpus.

That observation does not establish that the primitive set is minimal.

A seventh candidate, Invariant, was explicitly considered during the LangGraph analysis and rejected as unnecessary for representing the execution that actually occurred. This is evidence that at least one candidate extension was tested.

It is not a proof that no smaller basis or alternative decomposition can represent the same continuity properties.

The present paper therefore proposes EASTER as a compact six-primitive model supported by the examined evidence, not as a mathematically minimal basis.

## 10.7 No proof of universal sufficiency

No reviewed system demonstrated a need for an additional EASTER primitive under the applied lens.

This does not establish universal sufficiency.

The six-system corpus may simply fail to contain architectures or consequential workflows that expose a missing category.

Future systems may reveal continuity properties that cannot be adequately represented through Evidence, Authority, State, Transition, Exception, and Receipt.

A demonstrated case of that kind should be treated as evidence against the present primitive set rather than forced into an existing category.

## 10.8 DRC remains a candidate vocabulary

The DRC overlay classified Distinction, Relation, and Constraint as COVERED for all six architectures.

No DRC-negative specimen was observed.

No ablation experiment demonstrated that removing one of the three categories necessarily destroys functional interpretability.

No formal proof establishes that DRC is minimal, universally necessary, or sufficient for meaning.

The observed 3/3 coverage across six mature systems is therefore compatible with several interpretations: DRC may identify highly general representational structure, the categories may be too broad to discriminate strongly, the corpus may be biased toward systems rich enough to satisfy them, or some combination of these may be true.

The present paper cannot distinguish among those possibilities.

DRC should consequently be treated as a candidate analytical vocabulary supporting the userland/continuity boundary, not as an established universal ontology.

## 10.9 Projection fidelity

EASTER preserves the consequential representation admitted to the kernel.

It cannot recover information that userland failed to project.

A system may therefore satisfy EASTER's continuity requirements while preserving an incomplete, distorted, or semantically inadequate representation.

This limits what continuity alone can guarantee.

EASTER does not establish semantic truth, completeness of userland representation, correctness of a model's reasoning, or adequacy of the application's interpretation.

Projection fidelity remains an external responsibility.

## 10.10 Operational case-study limitation

The contribution-provenance workflow described in Section 8 occurred during real preparation of this manuscript.

It was not designed prospectively as a controlled experiment.

The expired gateway-credential event was naturally occurring rather than intentionally injected. The participants already understood the architecture. The workflow was performed by people and systems involved in EASTER's development.

The case therefore demonstrates that the reference implementation was used operationally under the described conditions.

It does not establish comparative superiority, security robustness, general usability, or universal sufficiency.

Independent users applying EASTER to consequential workflows they did not design would provide stronger evidence.

## 10.11 Reference-implementation dependence

Several demonstrated properties depend on the current Python/SQLite reference implementation.

SQLite transactions, schema constraints, triggers, explicit Authority ledgers, and particular kernel operations are implementation mechanisms used to realize EASTER's claimed invariants.

A different implementation could claim compatibility while implementing those mechanisms differently.

The present study does not provide a formal conformance suite establishing exactly which observable behaviors another implementation must satisfy to qualify as EASTER-compatible.

Without such a suite, some boundary remains between the conceptual model and implementation-specific behavior.

Developing implementation-independent conformance tests is therefore future work.

## 10.12 Prior-art search is bounded

The related-work investigation crossed multiple architectural families and included dedicated analysis of several strong neighboring systems.

It was not exhaustive.

The paper's novelty language is therefore intentionally limited to systems and literature examined to date.

A prior architecture satisfying the four-property conjunction identified in Section 9 would narrow or defeat the present non-identification claim.

In particular, the research has not exhausted the candidate class of permissioned distributed architectures combining hard revocable admission control with non-canonical or sharded replication.

The novelty claim should therefore remain falsifiable and updateable as additional prior art is found.

## 10.13 Conjunction provenance does not prove novelty

The preserved pre-prior-art record provides evidence that EASTER's four-property conjunction existed before the dedicated closest-prior investigation.

This addresses retrospective gerrymandering of the conjunction.

It does not prove that the conjunction had never previously appeared elsewhere.

Chronology establishes that the researchers did not construct the conjunction after discovering the examined prior-art gap; it does not establish historical priority over unknown work.

These are separate claims and should remain separate.

## 10.14 Lack of independent replication

The present findings have not been independently replicated by researchers outside the development and review process.

This limitation applies both to the six-system architectural analysis and to the reference implementation.

Independent replication could challenge primitive classifications, identify overlooked prior art, expose missing continuity categories, or demonstrate that some current OPEN findings should be resolved differently.

Such disagreement would be informative rather than anomalous.

The review framework is intended to preserve enough specificity that competing classifications can be compared against underlying evidence.

## 10.15 Threat model boundary

EASTER is not presented as a complete security architecture.

The model addresses continuity of consequential work across computational change. Authentication mechanisms, credential issuance, transport security, secret management, network security, identity proofing, application policy, and payload semantics remain outside the six primitives except insofar as their consequential outcomes cross the kernel boundary.

Authority records can preserve who was permitted to perform an operation under the implemented rules.

They do not prove that the external identity mechanism was uncompromised or that the policy granting that Authority was normatively correct.

Similarly, immutable provenance can preserve a malicious or mistaken event faithfully.

Continuity should therefore not be confused with trustworthiness, safety, or correctness.

## 10.16 Scope of the present evidence

Taken together, the present evidence supports a bounded conclusion.

It shows that:

- a six-primitive continuity model can be instantiated as a working reference kernel;
- the model can be applied as an architectural review lens;
- the examined corpus contains both substantial overlap with EASTER and bounded demonstrated gaps;
- DRC coverage did not entail zero EASTER GAPs under the applied classifications in that corpus;
- the reference implementation supported one real multi-participant provenance workflow; and
- the closest-prior investigation did not identify the surviving four-property conjunction in the systems and literature examined.

The evidence does not establish universal sufficiency, minimality, semantic correctness, statistical prevalence, exhaustive novelty, or independent replication.

Those boundaries are part of the result rather than qualifications to be removed from it.
