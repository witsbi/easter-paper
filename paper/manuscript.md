<!--
  Working manuscript for the EASTER+DRC paper.
  Converted from paper/source/DRC_EASTER_initial_paper_draft.docx
  (Draft 0.2, dated 25 September 2026). The .docx is preserved as the
  conversion source; this Markdown file is the working manuscript.
  Manuscript format: Markdown (LaTeX later when targeting a venue).
-->

# Distinction, Relation, Constraint and EASTER

**Separating Functional Meaning from Consequential Continuity in Agent Systems**

Initial working paper — Draft 0.2

**Co-created by Nathan Woolen and ChatGPT (OpenAI)**

25 September 2026

|  |
| --- |
| Authorship and AI-use statement. This manuscript was developed through sustained human–AI co-creation. Nathan Woolen originated and directed the research program, selected and accepted the research claims, performed or directed the underlying EASTER experiments and reverse reviews, and retains human responsibility for submission and factual verification. ChatGPT (OpenAI) participated as a co-creative research partner in conceptual reduction, adversarial questioning, synthesis, source gathering, and drafting. Because publication venues may not recognize an AI system as an accountable legal/scientific author, the final submission should adapt the byline to the venue’s authorship policy while preserving this contribution disclosure. |

# Abstract

Agent systems are commonly discussed in terms of memory, context, persistence, and orchestration, but these terms conflate at least two architectural problems: whether a system can represent enough structure for work to remain functionally meaningful, and whether consequential work can remain inspectable and recoverable across changes in session, model, agent, runtime, or machine. This paper introduces two independently derived lenses. DRC — Distinction, Relation, and Constraint — is proposed as a deliberately minimal cross-domain vocabulary for describing meaning-bearing structure in AI-agent userland. EASTER — Evidence, Authority, State, Transition, Exception, and Receipt — is a six-primitive model and reference kernel for consequential continuity. We apply both lenses to a frozen, pre-disclosure corpus of six materially different agent architectures: Hermes Agent, OpenClaw, LangGraph, Anthropic Claude Agent SDK, OpenAI Agents SDK, and Google Antigravity. Across the corpus, DRC coverage is invariant (3/3 covered), while previously conducted EASTER reviews varied across the same corpus (see §8; aggregates are descriptive summaries with unequal archival resolution, not equivalent measurements). This pattern does not establish universality, statistical independence, or discriminative power: no DRC-negative system was observed, and necessity, sufficiency, and universality are not established. Within the examined corpus, DRC coverage did not entail EASTER coverage. The reverse direction (EASTER-covered without DRC-covered) is predicted by the model but was not observed in the present corpus. We further argue that EASTER can operate as an external, vendor-neutral continuity layer, provided userland exposes enough consequential structure for projection. The paper contributes a bounded vocabulary, an adversarial reverse-review method, a comparative architectural result, and an open implementation path for studying semantic work-state portability.

Keywords: agent systems; continuity; memory; state; provenance; authority; durable execution; semantic portability; DRC; EASTER

# 1. Introduction

Modern agent systems increasingly preserve conversations, tool calls, checkpoints, memories, workflow state, and execution traces. Yet a system may appear to “remember” while still losing the facts required to continue consequential work correctly. Conversely, a system may preserve extensive durable history while failing to preserve the distinctions, relations, or constraints needed to interpret that history. We therefore separate two questions that are often collapsed.

Functional meaning: can the system represent what things are, how they relate, and what configurations are admissible?

Consequential continuity: can the system preserve what happened, under whose authority, from which state, with what evidence and outcome?

The first question led to DRC: Distinction, Relation, Constraint. The second led independently to EASTER: Evidence, Authority, State, Transition, Exception, Receipt. EASTER predates DRC in this research program. Its primitives were developed through implementation, subtraction, adversarial testing, recovery experiments, and whole-kernel review. DRC emerged later from attempts to reduce the structures needed for functional meaning. This chronology matters because the two lenses were not jointly designed to fit the comparative corpus. We position DRC as a deliberately minimal cross-domain vocabulary for describing meaning-bearing structure in AI-agent userland — a working representational floor, not a claim about the novelty of its primitives against prior representational traditions (see §4.4, §10).

Our central hypothesis is deliberately bounded: functional meaning and consequential continuity are separable architectural properties. We do not claim to solve philosophical meaning, consciousness, intrinsic intentionality, or model understanding. DRC is restricted to functional/structural meaning: the information a system must be able to differentiate, relate, and constrain for work to be interpreted and continued. EASTER is restricted to consequential continuity: the durable record needed to inspect and continue work without silently converting guesses into authoritative history.

# 2. Definitions and terminology

The terms below are used in a deliberately architectural sense. Several have broader meanings in operating systems, philosophy, formal logic, and AI practice; these definitions specify the scope intended in this paper.

| **Term** | **Definition used in this paper** |
| --- | --- |
| Agent system | A software system in which one or more model-driven agents interpret context, select or invoke capabilities, and produce actions or outputs over one or more execution steps. |
| Userland | The semantic/application layer outside the EASTER kernel where users, agents, frameworks, prompts, tools, policies, memories, domain models, and application logic determine what work means. “Userland” does not imply a particular operating-system privilege level; it marks the side of the EASTER boundary that owns meaning. |
| Runtime / harness | The execution environment that supplies an agent loop and its surrounding machinery, such as context assembly, tool dispatch, sessions, delegation, persistence, approvals, and model invocation. A runtime may contain userland mechanisms but is not synonymous with userland. |
| System boundary | The explicitly chosen scope within which a review claim is made. A GAP means the inspected system boundary did not demonstrate the required property; it does not imply that no external component could provide it. |
| Functional / structural meaning | The operationally usable structure that allows a system to keep relevant distinctions separate, relate them, and restrict admissible interpretations or actions. The term excludes claims about consciousness, phenomenal experience, or intrinsic intentionality. |
| DRC | The candidate functional-meaning lens: Distinction, Relation, and Constraint. D asks what can remain meaningfully separate; R asks how those distinguishables stand with respect to one another; C asks which alternative relations or successor configurations are admissible. |
| Consequential representation | The subset or projection of userland meaning treated as important enough to affect future work and therefore worth preserving across a continuity boundary. |
| Projection | A mapping from richer userland structure into the continuity representation. Projection need not preserve every detail; it must preserve the structure claimed to be consequential for later recovery. |
| Continuity boundary | The architectural point at which consequential userland structure is handed to a persistence/continuity mechanism. Loss before this boundary is a userland/DRC problem; loss after it is a continuity problem within the chosen system boundary. |
| Consequential continuity | The ability to preserve enough authoritative history, provenance, state, failure information, and outcomes for later work to be inspected and continued without silently replacing missing history with inference. |
| EASTER | The six-primitive continuity model: Evidence, Authority, State, Transition, Exception, and Receipt. EASTER is meaning-agnostic about payload contents while preserving the structural record required by its continuity contract. |
| Kernel | The small authoritative EASTER component that owns admission of consequential writes and enforces the continuity semantics assigned to the six primitives. It is intentionally narrower than the agent runtime or userland. |
| Observability / exportability | The degree to which a runtime exposes enough consequential structure for an external continuity mechanism to capture it. A hidden internal fact cannot be preserved externally if no supported boundary makes it observable or exportable. |
| Semantic work-state portability | The ability for a different agent/runtime to continue consequential work from an external representation without depending on the originating runtime’s private conversation, checkpoint format, model identity, or hidden implementation state. |
| COVERED / OPEN / GAP / CHALLENGED | Reverse-review statuses. COVERED: the property is demonstrated. OPEN: evidence is insufficient. GAP: the inspected system boundary does not demonstrate the required property. CHALLENGED: evidence calls the primitive or lens itself into question rather than merely finding a system deficiency. |
| Pre-disclosure corpus | The frozen set of architecture reviews completed before public disclosure of the combined DRC/EASTER framework. It is preserved because disclosure can change future system designs and therefore alter the independence of later observations. |

These definitions preserve the paper’s central separation: userland owns functional meaning; EASTER owns a bounded continuity contract for the consequential projection supplied across its boundary.

# 3. Contributions

- A deliberately minimal cross-domain vocabulary for describing meaning-bearing structure in AI-agent userland: Distinction (D), Relation (R), and Constraint (C).
- A six-primitive continuity model and implemented reference kernel: Evidence, Authority, State, Transition, Exception, and Receipt (EASTER).
- A methodological separation between representational meaning in userland and durable consequential continuity at the kernel boundary.
- A pre-disclosure comparative reverse review of six independently developed agent architectures using both lenses.
- An observed asymmetry: all six systems cover DRC, while EASTER findings vary across the same corpus.
- A vendor-neutral interpretation of EASTER as an external continuity layer, with observability/exportability identified as a boundary condition rather than a seventh primitive.

# 4. DRC: a candidate substrate for functional meaning

## 4.1 Distinction

Distinction is the ability to preserve that one consequential thing is not another. Agent systems instantiate distinction through typed messages, roles, agents, tools, memories, sessions, tasks, files, identities, checkpoints, branches, and other separable objects. Without distinction, independently consequential entities collapse into an undifferentiated representation.

## 4.2 Relation

Relation captures how distinguishable entities stand with respect to one another: parent/child, tool-call/tool-result, agent/session, checkpoint/ancestor, evidence/claim, task/dependency, user/instruction, or arbitrary domain relationships. DRC does not require every relation to be represented as a typed graph edge; natural language may encode relations when that representation is adequate for the work.

## 4.3 Constraint

Constraint describes how distinguishable and related entities may admissibly stand otherwise. Constraints may be semantic (instructions and policies), structural (schemas and graph rules), operational (tool allowlists and permissions), temporal, security-related, or user-defined. Mutable constraints, meta-constraints, and constraints on constraint changes remain instances of C rather than requiring a fourth primitive, so long as the system can represent the relevant admissibility conditions.

DRC = {Distinction, Relation, Constraint}

The claim is not that every meaningful representation literally stores three fields named D, R, and C. The claim is that these three categories form a compact candidate lens for asking whether a userland representation retains enough functional structure to be interpreted. The present paper treats minimality as a research hypothesis, not a proof.

We therefore position DRC as a deliberately minimal cross-domain vocabulary for describing meaning-bearing structure in AI-agent userland — a working representational floor, not a novelty claim about its primitives. The observed 3/3 saturation across the six-system corpus is a frozen empirical observation; it does not establish discriminative power, and no DRC-negative system was observed in this program. Necessity, sufficiency, and universality are not established. DRC's lineage with entity/relation/constraint traditions in ER modeling, description logic, conceptual graphs, property graphs, and related representational traditions must be addressed in Draft 2 Related Work rather than implied as primitive novelty here.

## 4.4 Negative classification, falsification, and the unobserved negative case

No DRC-negative case has been observed in this research program to date: every reviewed architecture covered D, R, and C. That absence reflects corpus selection — the corpus contains mature agent architectures selected toward rich representations — not a proven universal. We retain the limitation, and we distinguish two different things a future specimen could do.

A **negative classification** is a system that lacks D, R, or C under the frozen definitions. Predicted examples, retained as out-of-sample replication targets (see §7.3): an undifferentiated stream preserving consequential work, in which instructions, observations, tool results, and other consequential entities cannot later be reliably distinguished from one another (predicted D-negative); a bag of typed objects with no parent/child structure, call/result linkage, lineage, or dependency (predicted R-negative); a substrate with no allowlists, schemas, policies, or validity rules, where every arrangement of distinguishables is admissible (predicted C-negative). Such a finding would break the currently observed DRC saturation, but would not by itself challenge the necessity claim of the lens.

**Falsification** — a genuine CHALLENGED-class result against the primitive itself — would require more: a system demonstrating adequate functional/structural meaning (work remains interpretable and continuable across the demands the lens describes) while *lacking* the allegedly necessary primitive under the frozen definitions. A DRC-negative specimen shows the primitive absent; only a meaningful-without-the-primitive specimen shows the primitive unnecessary. No such case has been observed, and the present corpus was not designed to seek one.

# 5. EASTER: a six-primitive model for consequential continuity

EASTER is an append-oriented continuity model implemented as a reference kernel. The kernel owns authoritative writes, validates authority before committing transitions, preserves append-only semantics, atomically links accepted state changes with their transition and receipt, and records failure outcomes without mutating authoritative state. The current implementation deliberately leaves semantic truth to userland. [1]

| **Primitive** | **Role in the continuity model** | **What it does not imply** |
| --- | --- | --- |
| Evidence | Durable material cited in support of consequential work. | Truth merely because it was recorded. |
| Authority | Who/what is permitted to admit consequential change, including grants and revocation. | That authorized content is semantically correct. |
| State | Immutable admitted work-state payloads from which continuation may branch. | A kernel-selected current, canonical, or preferred state. |
| Transition | An admitted change from an existing state to a new state under validated authority. | That all possible changes must be linear. |
| Exception | Durable diagnostic/failure material for operations that do not become accepted state. | An accepted transition. |
| Receipt | Kernel-authored immutable outcome record for accepted, rejected, or failed operations. | A semantic endorsement of the payload. |

A key design choice is that EASTER does not select a single current branch and does not decide semantic truth. The reference implementation supports branching and treats payload meaning as opaque to the kernel. Earlier adversarial review showed why this boundary matters: direct database writes can create structurally problematic states, while the supported kernel boundary pairs accepted state creation with transition provenance and receipts. [1][2]

# 6. Relationship between DRC and EASTER

Meaning / userland  →  DRC  →  consequential projection  →  EASTER  →  continuity

DRC and EASTER operate at different layers. DRC asks whether userland has enough representational structure for functional meaning. EASTER asks whether consequential work crossing a continuity boundary is durably admitted with provenance and outcome. Within the examined corpus, DRC coverage did not entail EASTER coverage. The converse — an EASTER-complete persistence mechanism preserving opaque payloads whose userland representation is inadequate for functional interpretation — is predicted by the model but was not observed; it remains an open empirical direction, not an established finding.

Demonstrated: DRC-covered ⇏ EASTER-covered

Predicted, not observed: EASTER-covered ⇏ DRC-covered

This separation also explains why DRC is not proposed as a lower-dimensional EASTER kernel. Meaning remains a userland concern. EASTER receives a consequential projection of that meaning. If userland collapses distinctions, relations, or constraints before projection, EASTER can faithfully preserve the loss; it cannot recreate information it never received.

# 7. Methodology

## 7.1 Reverse-review classifications

Each lens was applied through source-oriented reverse review. Findings use four labels: COVERED, OPEN, GAP, and CHALLENGED. COVERED means the required property was demonstrated by inspectable architecture or behavior. OPEN means evidence is insufficient and the question remained unresolved. GAP means the property was not demonstrated within the inspected system boundary. CHALLENGED is reserved for evidence that attacks the primitive or lens itself rather than merely showing that a system lacks it.

## 7.2 Independence and chronology

The corpus is pre-disclosure: the examined systems were not designed in response to the combined DRC/EASTER framework. EASTER and several EASTER reverse reviews preceded DRC. DRC was later frozen and applied without changing its definitions to fit the target architectures. Wherever practical, DRC classifications were frozen before overlay with prior EASTER findings. This does not eliminate researcher interpretation, but it reduces one obvious path for retrospective fitting.

## 7.3 Stopping rule

The mature-system survey stopped at six systems. We record honestly that the stopping rationale — repeated DRC saturation implying that additional mature frameworks would add sample count rather than conceptual diversity — was reconstructed after stopping, not preregistered as a frozen rule before the survey closed. It should therefore be read as a limitation on the corpus, not as methodology. (If a dated artifact recording the stopping decision before closure is produced, this paragraph will be replaced with that record.) Untested systems are retained for later out-of-sample replication rather than consumed during initial theory formation.

## 7.4 Source boundary

The reviews rely on inspectable public documentation/source where available and on the EASTER reference implementation and archived research artifacts for EASTER-specific claims. Before formal submission, the reproducibility appendix should pin exact repository commits/tags for every system and attach the primitive-by-primitive review receipts. The present document is an initial paper draft, not the final archival evidence package.

# 8. Comparative architectural results

The table below keeps five layers separate: the DRC frozen overlay, primitive-level findings, whole-system composition, final aggregate disposition, and archival completeness. The recovery artifact (`paper/archive/recovered-review-state-2026-09-29.md`) is the source of truth; nothing below is inferred from aggregate gap counts.

| **System** | **DRC (frozen overlay)** | **Primitive-level findings** | **Whole-system composition** | **Final aggregate** | **Archival completeness** |
| --- | --- | --- | --- | --- | --- |
| Hermes Agent | D/R/C COVERED | Ev, Au, St, Ex COVERED. Tr, Re COVERED + OPEN H-OPEN-1. | H-OPEN-1 (unrecoverable external-effect window) survives composition; explicitly not promoted to GAP. | 0 GAP, 0 CHALLENGED. | Strong. DRC primitive receipts and exact commit pin not yet recovered. |
| OpenClaw | D/R/C COVERED | Ev, Au, Ex COVERED. St, Tr COVERED + OC-OPEN-1. Re COVERED + OC-OPEN-1 + OC-OPEN-2. Initial sweep: 30 COVERED / 11 OPEN / 0 GAP. | OC-OPEN-1 (unrecoverable external-effect window) spans State, Transition, Receipt. OC-OPEN-2 (delivery bypass) spans Receipt. | 0 GAP, 0 CHALLENGED. | Strong. Only the abbreviated prefix `2ef3b4a0…` recovered; full SHA pin still incomplete. Individual DRC receipts not yet recovered. |
| LangGraph | D/R/C COVERED | Ev COVERED + OPEN (UntrackedValue boundary). Tr 7 COVERED / 4 OPEN. Ex 7 COVERED / 4 OPEN. Re 5 COVERED / 5 OPEN. Au, St reviewed; finding matrices not recovered. | Composition closed many primitive-level OPENs (checkpoint, task, pending-write, metadata, authorization/control, fault-tolerance mechanisms). | 0 GAP, 0 CHALLENGED. | Substantial. Au/St matrices and exact source SHA not yet recovered. |
| Anthropic Claude Agent SDK | D/R/C COVERED | Unknown — aggregate result only. | Not recovered. | 0 GAP; no demonstrated GAP. | Aggregate only. Primitive decomposition unknown; must remain unknown until a primitive-level artifact is recovered. |
| OpenAI Agents SDK | D/R/C COVERED | Unknown — which primitive owned the GAP was not recovered. (An unverified recollection of an Evidence OPEN is quarantined, not used.) | Not recovered. | Exactly 1 GAP (real, recorded). | Aggregate + GAP existence. Primitive mapping unknown. |
| Google Antigravity | D/R/C COVERED | Ev: 2 GAP (MCP annotations lost before policy evaluation; exception fidelity lost) + 2 OPEN. Au: 4 GAPs (incl. retrospective authorization provenance). St: 1 GAP (compaction change metadata) + 2 OPEN. Tr: partial (T-3, T-4). Ex: 1 GAP (structured exception fidelity) + 3 OPEN. Re: not sufficiently recovered. | Six conceptual families recovered: evidence metadata loss; retrospective authorization provenance; effective-state / compaction reconstruction; tool-call transformation provenance; structured failure fidelity; normalized terminal outcomes. Exact mapping from families to the final 3 GAPs not recovered. | 3 GAPs; no demonstrated CHALLENGE. | Substantial sweeps. Receipt freeze, 3-GAP mapping, and exact runtime version not yet recovered; launch-blog citation insufficient alone. |

Notes. DRC 3/3 COVERED is the frozen comparative overlay result; individual D/R/C primitive receipts are not yet recovered for most systems. Final aggregates are previously recorded frozen results — descriptive summaries only, not additive, not ordinal, not scores, not rankings. Primitive-level cells show only what the recovery artifact establishes; "unknown" is preserved explicitly and never filled from aggregate counts or recollection.

The recovered record corrects a natural misreading: 0 GAP did not mean six uncomplicated COVERED primitives. Hermes, OpenClaw, and LangGraph each retained surviving OPEN findings at the primitive level while whole-system composition produced no demonstrated GAP — primitive sweeps and whole-system composition are distinct layers of the method. Preservation quality is uneven across the corpus (strong for Hermes, OpenClaw, LangGraph, and Antigravity's sweeps; aggregate-only for Anthropic and OpenAI's decomposition), and the manuscript distinguishes recovered primitive evidence from aggregate frozen results throughout.

This is comparative architectural evidence, not a statistical sample. The six systems are mature agent architectures and are therefore selected toward rich representations. Nevertheless, the observed asymmetry is informative. Within the examined corpus, DRC coverage did not entail EASTER coverage. OpenAI Agents SDK and Google Antigravity are observed cases under the frozen review method in which DRC was COVERED while one or more EASTER properties were GAP within the inspected boundary.

# 9. Interpretation

## 9.1 Why “memory” is too coarse

The public vocabulary of agent memory often mixes conversation history, curated facts, semantic retrieval, checkpoints, durable execution, provenance, and authorization. OpenClaw, for example, separates workspace files, MEMORY.md, dated notes, session transcripts, and search behavior; Hermes separates bounded curated memory from full searchable session history and procedural skills. [3][5][6] LangGraph’s checkpoint model separately preserves graph state, metadata, lineage, and pending writes. [7][8] These mechanisms solve different parts of the continuity problem. DRC/EASTER provides a way to ask which part failed rather than labeling every failure “memory.”

## 9.2 EASTER as an external continuity layer

EASTER need not be natively implemented by every vendor. Its reference architecture can sit outside an agent harness:

Runtime A  →  EASTER_external  →  Runtime B

The critical precondition is observability/exportability. If userland exposes the consequential distinctions, relations, constraints, evidence, authority facts, states, transitions, failures and outcomes needed for projection, an external kernel can preserve them. If a managed runtime exposes only input and final output, an external continuity layer cannot reconstruct hidden consequential structure. We treat this as a boundary condition on projection, not as a seventh EASTER primitive.

A further boundary condition is projection fidelity: EASTER preserves what crosses the boundary, but it cannot establish the completeness or semantic fidelity of the userland projection. A lossy or distorted projection is preserved as faithfully as a sound one; the kernel attests to what it admitted, not to what it should have received.

## 9.3 Deliberate omissions are not automatically defects

An EASTER GAP is not synonymous with a bad system. Privacy, deletion guarantees, security boundaries, cost, simplicity, and product design can justify intentionally omitting recoverability. OpenAI’s tracing documentation, for example, notes that tracing can be disabled and is unavailable for organizations using Zero Data Retention. [11] The framework therefore identifies a continuity tradeoff; it does not prescribe that every system maximize persistence.

## 9.4 Candidate integration observation (bounded)

Independent prior-art comparison (Hyperledger Fabric [16][20], R3 Corda [17][21], Holochain [18][21], Ethereum [19]) identified a candidate conjunction that no examined system was found to combine:

- revocable authority validation inside the consequential admission path;
- uniform durable ACCEPTED / REJECTED / FAILED outcome recording;
- durable Exception/failure records excluded from accepted State;
- no substrate-designated canonical current State.

In the systems and literature examined to date, we did not identify any architecture combining all four. These four properties are independently documented EASTER commitments predating the comparison (see the pre-prior-art provenance record, `paper/archive/pre-prior-art-conjunction-provenance-2026-09-29.md`); they were not selected post-hoc to fit the comparison. One methodological limitation remains: the properties predate the comparison, but the decision to foreground exactly these four as a potentially distinguishing conjunction emerged through the subsequent comparative analysis. This observation is a candidate integration and boundary-discipline contribution, not an established architectural-novelty claim, and it remains open to future counterevidence. Full per-property, primary-source classifications (COVERED / PARTIAL / NOT COVERED / UNKNOWN, with quotations and citations) and the reconciliation of two independently-decomposed evaluations are archived at [20][21][22]; no single closest architecture is named here, and none should be inferred pending Draft 2 Related Work.

# 10. Threats to validity and limitations

- Selection bias. The corpus contains sophisticated agent systems; 6/6 DRC coverage cannot establish universality.
- Researcher interpretation. Primitive classification is a structured architectural judgment, not a mechanically computed metric.
- Version drift. Agent frameworks evolve quickly. Final publication must pin commits/tags and dates for every reviewed source.
- Unequal observability. Open-source frameworks expose more internals than managed products. GAP claims are bounded to the inspected source/system boundary.
- No proof of DRC minimality. DRC survived the research program’s reductions and adversarial attacks, but no formal proof establishes that no alternative or smaller basis exists.
- No proof of philosophical meaning. DRC concerns functional/structural meaning only; it makes no claim about consciousness or intrinsic intentionality.
- No statistical independence claim. The invariant DRC / varying EASTER pattern is descriptive comparative evidence, not an inferential statistical result.
- Observer effect after disclosure. Once the framework is public, vendors or open-source maintainers may change architectures in response; the present corpus should therefore be preserved as pre-disclosure evidence.
- Goodhart risk. If DRC/EASTER becomes a checklist, systems may adopt labels without preserving behavior. Coverage must remain behavior/source demonstrated rather than name-based.
- Projection fidelity. EASTER preserves what crosses the continuity boundary but cannot establish that the projection was complete or semantically faithful. A system can satisfy every EASTER primitive on a projection that omits consequential facts.
- Independent lineage is not independent evaluation. The six architectures were not designed in response to the framework, and DRC definitions were frozen before overlay — but the reviews themselves were conducted within a single research program with substantial human–AI collaboration. They were not blinded and not performed by independent research teams. Cross-agent agreement within the program (including AI collaborators sharing a human collaborator and overlapping research vocabulary) is evidence of response convergence within the research process, not independent replication.
- Shadow-review independence is response isolation, not historical independence. The adversarial review round for this draft was conducted by two reviewers with no direct contact, sharing only the manuscript via a human relay — but both reviewers share the same human collaborator and overlapping research vocabulary. Agreement between them demonstrates independent responses to the same text, not historically independent observation.
- Operator/reviewer entanglement. Hermes Agent and OpenClaw are operated and configured within Nathan Woolen's research environment. Independent system lineage — neither was designed in response to the framework — must not be confused with independent evaluation: the reviews were conducted inside a single research program. Their zero-GAP aggregate findings must not be framed as independent validation of those systems or of EASTER.
- Antigravity observability asymmetry. Google Antigravity has the weakest inspected boundary in the corpus while carrying the largest frozen EASTER GAP aggregate (3). Its evidence therefore carries greater uncertainty than the strongly archived systems, and the larger GAP count must not be read as establishing architectural inferiority.
- DRC lineage outstanding. DRC's relationship to ER modeling, description logic, conceptual graphs, property graphs, and related representational traditions is not addressed in this draft; it belongs to Draft 2 Related Work. No primitive-novelty claim is made here.
- Authority traditions outstanding. EASTER's Authority primitive should be situated against reference-monitor, capability, and delegation traditions in Draft 2 Related Work; the present draft does not establish its novelty against them.
- Confused deputy and principal binding. EASTER's structural authority guarantees do not by themselves solve confused-deputy or principal-binding/delegation problems; these are explicitly outside the kernel's claims.
- Maturity boundaries. Idempotency and exactly-once semantics, cryptographic tamper-evidence, snapshotting strategy, and compensation/Saga semantics are implementation and maturity boundaries. Their absence as EASTER primitives must not be mistaken for the absence of the corresponding operational risks.
- Integration, not primitive novelty. EASTER's candidate contribution is integration and boundary discipline across its six primitives, not the novelty of Evidence, Authority, State, Transition, Exception, or Receipt individually.

# 11. Publication and ecosystem effects

Disclosure changes the object of study. Before publication, zero-gap findings can be interpreted as independent convergence more readily than after publication. After disclosure, architecture changes may be treatment effects of the framework itself. This makes the frozen pre-disclosure corpus valuable and argues for preserving versions, source evidence, classifications, and dates.

The framework’s value does not depend on vendors adopting nine named primitives. Its more general contribution is a vocabulary for locating loss. Developers can ask whether a failure arose because functional meaning was collapsed before projection (D/R/C) or because consequential history was not preserved after projection (E/A/S/T/E/R). If systems improve continuity after disclosure, that is compatible with success of the idea even if the EASTER kernel itself is not adopted.

# 12. Implications for semantic work-state portability

The combined model suggests a future portability target. A runtime may project consequential userland work into EASTER, terminate or lose its private state, and allow a heterogeneous runtime to recover from the external continuity record. The research question is not whether two runtimes share internal checkpoints, but whether consequential semantic work-state can survive across heterogeneous intelligence runtimes.

DRC_A  →  EASTER  →  transport  →  EASTER′  →  DRC_B

The target is semantic work-state portability rather than checkpoint portability or context-window portability. This remains future work; it is not required for the claims of the present paper.

# 13. Conclusion

This paper proposes that two architectural problems commonly conflated under “memory” should be treated separately. DRC — Distinction, Relation, Constraint — provides a deliberately minimal cross-domain vocabulary for describing meaning-bearing structure in AI-agent userland. EASTER — Evidence, Authority, State, Transition, Exception, Receipt — provides a six-primitive model and reference kernel for consequential continuity. Across six pre-disclosure agent architectures, DRC coverage remained invariant while EASTER findings varied. Within the examined corpus, DRC coverage did not entail EASTER coverage. The reverse direction remains a model prediction, not an observed finding. The bounded contribution is not a universal theory of meaning and not a vendor leaderboard. It is a vocabulary, an implementation boundary, and a reverse-review method for making continuity loss more inspectable. The DRC vocabulary is positioned as a minimal working representational floor; its lineage against prior representational traditions, and any assessment of novelty, belong to Draft 2 Related Work.

# 14. Reproducibility status and next publication steps

This Draft 0.2 intentionally distinguishes paper-ready claims from archival work still required before submission. The research phase for the initial paper is frozen; the remaining work is preservation and documentation, not additional experiments.

- Pin exact commit SHA/tag and review date for all six system specimens.
- Attach or publish the primitive-level DRC and EASTER review receipts used to produce the comparison table.
- Publish the EASTER repository tag/release corresponding to the kernel described here and cite its immutable release URL/DOI if archived.
- Replace provisional source URLs with archival citations (commit permalinks, releases, documentation snapshots, or Zenodo/Software Heritage where practical).
- Add a chronology appendix showing that EASTER and relevant EASTER reviews preceded DRC, and that DRC definitions were frozen before overlay.
- Run an independent source audit of every GAP/COVERED claim before submission.
- Adapt the authorship/byline disclosure to the target venue’s AI authorship policy while preserving the co-creation record.
- Draft 2 Related Work placeholders (not written in this pass): situate DRC against ER modeling, description-logic, conceptual-graph, and property-graph traditions; situate EASTER Authority against reference-monitor, capability, and delegation traditions; address confused-deputy and principal-binding boundaries; treat idempotency, cryptographic tamper-evidence, snapshotting strategy, and compensation/Saga semantics as maturity boundaries.

# References

[1] Woolen, N. EASTER reference kernel source and research artifacts (2026). Internal/public repository materials; current kernel implementation documents authoritative SQLite writes, authority validation, append-only semantics, atomic state/transition/receipt commits, and failure receipts. Final submission should cite the immutable public release/commit.

[2] Woolen, N. EASTER State adversarial review / isolated red-team notes (20 Sep 2026). Archived research artifact. Final submission should publish or attach the review receipt and exact kernel commit.

[3] Nous Research. Hermes Agent — Persistent Memory. GitHub documentation, accessed 25 Sep 2026. https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/memory.md

[4] Nous Research. Hermes Agent — Sessions. GitHub documentation, accessed 25 Sep 2026. https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/sessions.md

[5] OpenClaw. Memory overview. GitHub documentation, accessed 25 Sep 2026. https://github.com/openclaw/openclaw/blob/main/docs/concepts/memory.md

[6] OpenClaw. Agent / workspace bootstrap documentation, accessed 25 Sep 2026. https://github.com/openclaw/openclaw/blob/main/docs/concepts/agent.md

[7] LangChain AI. LangGraph Checkpoint README. GitHub, accessed 25 Sep 2026. https://github.com/langchain-ai/libs/checkpoint/README.md

[8] LangChain AI. LangGraph checkpointers / persistence documentation. GitHub, accessed 25 Sep 2026. https://github.com/langchain-ai/docs/blob/main/src/oss/langgraph/checkpointers.mdx

[9] Anthropic. Claude Agent SDK for Python README. GitHub, accessed 25 Sep 2026. https://github.com/anthropics/claude-agent-sdk-python/blob/main/README.md

[10] OpenAI. OpenAI Agents SDK documentation, accessed 25 Sep 2026. https://openai.github.io/openai-agents-python/

[11] OpenAI. Agents SDK tracing documentation, accessed 25 Sep 2026. https://openai.github.io/openai-agents-python/tracing/

[12] OpenAI. Agents SDK sessions documentation, accessed 25 Sep 2026. https://openai.github.io/openai-agents-python/sessions/

[13] Google Antigravity Team. “Build with Google Antigravity, our new agentic development platform.” Google Developers Blog, 20 Nov 2025. https://developers.googleblog.com/build-with-google-antigravity-our-new-agentic-development-platform/

[14] OpenClaw. Main-session continuity documentation, accessed 25 Sep 2026. https://github.com/openclaw/openclaw/blob/main/docs/concepts/main-session.md

[15] Nous Research. Hermes Agent tools reference, accessed 25 Sep 2026. https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/tools-reference.md

[16] Androulaki, E. et al. "Hyperledger Fabric: A Distributed Operating System for Permissioned Blockchains." EuroSys 2018. arXiv:1801.10228. Also: Hyperledger Fabric documentation, accessed 30 Sep 2026. https://hyperledger-fabric.readthedocs.io/

[17] Hearn, M. and Brown, R.G. "Corda: A Distributed Ledger" (Technical Whitepaper), v1.0, 20 Aug 2019. https://docs.r3.com/en/pdf/corda-technical-whitepaper.pdf

[18] Harris-Braun, E., Brock, A., d'Aoust, P. "Holochain: Distributed Coordination by Scaled Consent, not Global Consensus," v2.0, 8 Nov 2024. https://www.holochain.org/documents/holochain-white-paper-2.0.pdf

[19] Nethereum documentation. "Transaction Receipt Status," accessed 30 Sep 2026. https://docs.nethereum.com/en/latest/nethereum-receipt-status/

[20] Woolen, N. / Clawde. "Hyperledger Fabric vs. EASTER's Architectural Properties — Adversarial Evaluation" (2026-09-30). Archived research artifact. `paper/archive/clawde-hyperledger-fabric-evaluation-2026-09-30.md`.

[21] Woolen, N. / Clawde. "Corda and Holochain vs. EASTER's Architectural Properties — Primary-Source Evaluation" (2026-09-30). Archived research artifact. `paper/archive/clawde-corda-holochain-evaluation-2026-09-30.md`.

[22] Woolen, N. / Pax / Clawde. "Pax/Clawde Closest-Architecture Reconciliation" (2026-09-30). Archived research artifact. `paper/archive/clawde-pax-closest-architecture-reconciliation-2026-09-30.md`. See also the pre-prior-art provenance record, `paper/archive/pre-prior-art-conjunction-provenance-2026-09-29.md`.

# Appendix A. Frozen comparative claim

Frozen initial-paper claim: Across a pre-disclosure corpus of six materially different agent architectures, the DRC functional-meaning lens found 3/3 coverage in all six, while previously conducted EASTER continuity reviews found 0, 0, 0, 0, 1, and 3 gaps. This supports continued investigation — within the examined corpus, DRC coverage did not entail EASTER coverage — without establishing universality, formal minimality, statistical independence, or the reverse direction.

# Appendix B. Co-creation provenance

The research program was developed iteratively through dialogue between Nathan Woolen and ChatGPT. Nathan exercised human authority over goals, acceptance, stopping decisions, system selection, experiment execution, and publication intent. ChatGPT contributed conceptual formulations, counterarguments, reduction attempts, architecture comparisons, synthesis, and manuscript drafting. The collaboration repeatedly used an evidence-over-agreement norm: claims were attacked, frozen only after review, and revised when source evidence contradicted earlier formulations. This appendix is included because the method of human–AI co-creation is itself relevant to provenance and reproducibility.
