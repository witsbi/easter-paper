# 7. Userland and the Continuity Boundary

EASTER does not determine what consequential work means. It receives a projection of work whose functional structure has already been established outside the kernel.

This creates a boundary question:

**What structure must exist in userland for consequential work to remain functionally interpretable before EASTER is asked to preserve its continuity?**

During the research program, this question produced a candidate three-part vocabulary: **Distinction, Relation, and Constraint (DRC)**.

DRC and EASTER address different problems.

**DRC concerns functional representational structure in userland.**

**EASTER concerns durable continuity of consequential work crossing the kernel boundary.**

The distinction can be summarized as:

**userland meaning → consequential projection → EASTER → continuity**

DRC provides a vocabulary for reasoning about the structure on the userland side of that boundary. It is not proposed here as a replacement for EASTER, a lower-dimensional EASTER kernel, or a proven universal theory of meaning.

## 7.1 Distinction

**Distinction** is the ability to preserve that one consequential thing is not another.

Agent systems instantiate distinctions through such objects as messages, roles, agents, tools, memories, sessions, tasks, files, identities, checkpoints, branches, and application-specific entities.

Without adequate distinction, independently consequential entities collapse into an undifferentiated representation.

Distinction does not require one particular data model. Typed objects, identifiers, structured records, natural-language representations, or other mechanisms may preserve distinctions when they are adequate for the work being performed.

## 7.2 Relation

**Relation** captures how distinguishable entities stand with respect to one another.

Examples include parent/child, tool-call/tool-result, agent/session, checkpoint/ancestor, Evidence/claim, task/dependency, user/instruction, and arbitrary domain relationships.

DRC does not require every Relation to be represented as an explicit typed graph edge. A natural-language representation may preserve a Relation when that representation is adequate for the consequential work.

The relevant question is whether the relationship necessary for functional interpretation remains representable, not whether a particular storage structure is used.

## 7.3 Constraint

**Constraint** describes how distinguishable and related entities may admissibly stand or evolve.

Constraints may be semantic, structural, operational, temporal, security-related, or application-defined. Examples include instructions, schemas, graph rules, tool permissions, temporal conditions, authorization requirements, and domain-specific admissibility rules.

Mutable constraints and constraints governing other constraints do not necessarily require additional DRC categories. They remain instances of Constraint so long as the representation can distinguish the relevant entities and relations and express the admissibility conditions governing their change.

In an earlier formalization, Constraint was expressed as a set of admissible successor structures:

\[
C(G) = \{G' \mid G' \text{ is an admissible successor of } G\}
\]

This notation is useful for expressing constrained evolution, but Draft 2 does not require all userland systems to instantiate a formal graph or explicitly compute such a set.

## 7.4 DRC as a candidate vocabulary

The claim made here is deliberately limited.

DRC proposes that **Distinction, Relation, and Constraint form a compact candidate vocabulary for asking whether a userland representation retains functional structure relevant to consequential work.**

It does not claim that every meaningful representation literally stores three fields named D, R, and C.

Nor does the present study establish that these categories are mathematically minimal, universally necessary, or sufficient for all forms of meaning.

No formal minimality proof excludes a smaller or alternative basis.

No DRC-negative architecture was observed in the initial corpus.

No ablation study established that removing one of the three categories necessarily destroys functional meaning.

The three-part reduction should therefore be treated as a research hypothesis and analytical vocabulary rather than a proven ontology.

## 7.5 Observed DRC coverage

The frozen DRC overlay classified all three categories as COVERED for each of the six architectures examined:

| System | Distinction | Relation | Constraint |
| --- | --- | --- | --- |
| Hermes Agent | COVERED | COVERED | COVERED |
| OpenClaw | COVERED | COVERED | COVERED |
| LangGraph | COVERED | COVERED | COVERED |
| Anthropic Claude Agent SDK | COVERED | COVERED | COVERED |
| OpenAI Agents SDK | COVERED | COVERED | COVERED |
| Google Antigravity | COVERED | COVERED | COVERED |

Thus the observed corpus produced:

**DRC = {3/3 × 6}**

This result is descriptive.

The systems were mature architectures selected toward comparatively rich agent functionality. Six positive cases do not establish universality, necessity, sufficiency, or strong discriminative power.

The absence of a DRC-negative specimen is consequently both an observation and a limitation.

## 7.6 DRC coverage did not entail EASTER coverage

The same six-system corpus produced a different pattern under EASTER.

The frozen aggregate EASTER GAP vector was:

**{0, 0, 0, 0, 1, 3}**

OpenAI Agents SDK and Google Antigravity therefore received D/R/C COVERED dispositions while retaining one or more EASTER GAPs within their inspected boundaries.

Within this corpus:

**DRC-covered ⇏ EASTER-covered**

This is the strongest empirical reason to keep the two lenses separate.

A system may preserve enough Distinction, Relation, and Constraint for functional interpretation while failing to durably preserve some consequential Evidence, Authority, State, Transition, Exception, or Receipt property across a continuity boundary.

DRC coverage therefore does not establish consequential continuity.

## 7.7 The converse remains unobserved

The conceptual separation also permits the opposite possibility.

An EASTER-compatible continuity mechanism could faithfully preserve opaque consequential payloads whose userland representation is inadequate for functional interpretation.

For example, if userland collapses a distinction, loses a necessary relation, or omits a consequential constraint before projection, EASTER can preserve the resulting payload and its provenance without reconstructing the information that never crossed its boundary.

Conceptually:

**EASTER-covered ⇏ DRC-covered**

However, this converse was **not observed in the present six-system corpus**.

It therefore remains a prediction of the architectural separation rather than an empirical result of this study.

## 7.8 Projection fidelity

The boundary between userland and EASTER introduces a limitation that neither framework eliminates: **projection fidelity**.

EASTER can preserve only the consequential representation supplied to it.

If userland projects a complete and appropriately structured representation, EASTER can preserve that projection according to its continuity contract.

If userland omits consequential information, collapses distinctions, strips relations, removes constraints, or otherwise distorts the representation before admission, the kernel may faithfully preserve an incomplete artifact.

EASTER therefore provides continuity of the admitted projection, not a guarantee that the projection captures everything required for semantic reconstruction.

This is why semantic truth and application meaning remain outside the kernel.

## 7.9 Boundary result

The combined DRC/EASTER analysis supports a narrower result than either a universal theory of meaning or a universal continuity theorem.

Within the examined corpus, **functional representational structure and consequential continuity behaved as separable architectural properties**.

DRC provides a compact vocabulary for examining the first.

EASTER provides a six-primitive model for examining and implementing the second.

The relationship is therefore not one of reduction but of projection:

**functional structure in userland → consequential projection → continuity boundary**

This separation allows EASTER to remain semantically narrow while still preserving consequential work whose meaning is owned elsewhere.
