# 6. Comparative Architectural Results

We applied the reverse-review method to six mature agent architectures. The results below preserve three distinct evidentiary layers: recovered primitive-level findings, recovered whole-system composition, and previously frozen aggregate disposition.

These layers are not interchangeable.

The archival record is uneven. For some systems, substantial primitive-level findings were recovered; for others, only an aggregate result survived. Missing classifications remain unknown. We do not reconstruct them from aggregate counts, present-day recollection, or later re-analysis.

The recovered-review artifact used here is itself a reconstruction created on September 29, 2026 from previously preserved research state. It is not represented as the original freeze.

## 6.1 Comparative summary

| System | DRC frozen overlay | Recovered EASTER evidence | Whole-system composition | Frozen aggregate | Archival status |
| --- | --- | --- | --- | --- | --- |
| **Hermes Agent** | D/R/C COVERED | Evidence, Authority, State, Exception COVERED. Transition and Receipt COVERED with surviving H-OPEN-1. | H-OPEN-1, an unrecoverable external-effect window, survives composition and remains OPEN rather than GAP. | 0 demonstrated GAP; no preserved CHALLENGED disposition. | Strong primitive recovery; exact reviewed commit and individual DRC receipts not recovered. |
| **OpenClaw** | D/R/C COVERED | Evidence, Authority, Exception COVERED. State and Transition COVERED + OC-OPEN-1. Receipt COVERED + OC-OPEN-1 + OC-OPEN-2. Initial sweep: 30 COVERED / 11 OPEN / 0 GAP / 0 CHALLENGED. | OC-OPEN-1 concerns an unrecoverable external-effect window. OC-OPEN-2 concerns delivery paths that may bypass a shared durable lifecycle. | 0 demonstrated GAP; no preserved CHALLENGED disposition. | Strong primitive recovery; abbreviated source commit recovered; individual DRC receipts not recovered. |
| **LangGraph** | D/R/C COVERED | Evidence findings substantially recovered, including an UntrackedValue OPEN. Transition: 7 COVERED / 4 OPEN. Exception: 7 COVERED / 4 OPEN. Receipt: 5 COVERED / 5 OPEN. Authority and State were reviewed but their exact matrices were not recovered. | Composition among checkpoints, tasks, pending writes, metadata, authorization/control, and fault-tolerance mechanisms closed many primitive-level OPENs. | 0 demonstrated GAP; no preserved CHALLENGED disposition. | Substantial recovery; Authority/State matrices, individual DRC receipts, and exact source SHA not recovered. |
| **Anthropic Claude Agent SDK** | D/R/C COVERED | Primitive-level EASTER classifications not recovered. | Not recovered. | 0 demonstrated GAP. | Aggregate recovery only. Primitive decomposition remains unknown. |
| **OpenAI Agents SDK** | D/R/C COVERED | Primitive-level decomposition not recovered. | Not recovered. | Exactly 1 GAP. | Aggregate result and existence of one real GAP recovered; owning primitive remains unknown. |
| **Google Antigravity** | D/R/C COVERED | Substantial primitive sweeps recovered: Evidence, Authority, State, Transition, and Exception contain documented GAP/OPEN/COVERED findings; Receipt is not sufficiently recovered. | Six conceptual families survived recovery, but their exact mapping to the final three GAPs did not. | 3 GAPs; no preserved CHALLENGED disposition. | Substantial primitive recovery; final composition mapping, Receipt freeze, and exact runtime version remain incomplete. |

The table is descriptive, not ordinal. GAP counts are not system scores, and the aggregate column cannot be used to reconstruct missing primitive classifications.

In corpus order (Hermes Agent, OpenClaw, LangGraph, Anthropic Claude Agent SDK, OpenAI Agents SDK, Google Antigravity), the frozen **per-system aggregate GAP-count sequence** is **(0, 0, 0, 0, 1, 3)**. This is an ordered summary across systems, not a primitive-level vector. In particular, the surviving OpenAI aggregate does not identify which EASTER primitive owns its one GAP, and Antigravity's recovered primitive findings do not reconstruct the exact mapping from six conceptual families to its final three-GAP aggregate.

## 6.2 Zero aggregate GAP did not mean complete primitive coverage

Three systems—Hermes, OpenClaw, and LangGraph—illustrate why primitive review and whole-system composition must remain separate.

Hermes retained **H-OPEN-1**, an unrecoverable external-effect window:

external effect occurs  
→ local durable record is lost  
→ no independent external receipt exists  
→ later recovery cannot establish whether the effect occurred.

The finding affected Transition and Receipt but was explicitly retained as OPEN rather than promoted to GAP.

OpenClaw retained two whole-system OPEN findings.

**OC-OPEN-1** has the same general external-effect shape: a non-idempotent external effect may occur, the local durable record may be lost, and no independent external receipt may exist from which later recovery can establish the event.

**OC-OPEN-2** concerns delivery bypass: plugin or direct-send delivery can bypass a shared durable lifecycle, potentially leaving no authoritative later proof of delivery.

Despite these surviving OPEN findings, OpenClaw's frozen aggregate contained no demonstrated GAP.

LangGraph likewise retained primitive-level uncertainty. Its recovered Evidence review includes an OPEN around the `UntrackedValue` boundary: whether deliberately uncheckpointed values can influence a consequential durable outcome without enough corresponding durable Evidence. Recovered Transition, Exception, and Receipt matrices also contain multiple OPEN findings.

Whole-system composition nevertheless closed many primitive-level questions through the interaction of checkpoints, pending writes, task provenance, metadata, authorization/control mechanisms, and fault-tolerance behavior.

The resulting observation is methodological rather than competitive:

**zero aggregate GAP does not mean six uncomplicated COVERED primitives.**

## 6.3 Aggregate-only results remain aggregate-only

The Anthropic Claude Agent SDK and OpenAI Agents SDK demonstrate the opposite archival problem.

For the Anthropic review, the frozen aggregate result of **0 GAP** survived, but the primitive-level decomposition and detailed whole-system composition did not.

We therefore report the aggregate result without inferring that all six EASTER primitives were individually COVERED.

For the OpenAI Agents SDK, the frozen aggregate establishes **exactly one real EASTER GAP**. The archival record does not establish which primitive owned that GAP.

A later recollection suggested a particular Evidence disposition, but no preserved artifact was recovered to substantiate it. That recollection is excluded from the result.

The owning primitive therefore remains unknown.

This treatment intentionally sacrifices apparent completeness in favor of provenance fidelity.

## 6.4 Google Antigravity

Google Antigravity retains the most substantial recovered GAP set in the initial corpus.

Recovered Evidence findings include loss of MCP annotations before policy evaluation and loss of exception fidelity, alongside COVERED call/result/step correlation and OPEN questions involving truncation and context fragmentation.

Recovered Authority findings include GAPs involving retrospective authorization provenance, Boolean human approval, dynamic delegation provenance, and silent ineffective sandbox behavior, alongside COVERED capability/authorization separation and a required authorization boundary.

Recovered State findings include COVERED recovery, trajectory/workspace separation, and concurrency protection; a GAP in compaction change metadata; and OPEN questions around exact effective context and cross-domain provenance.

Recovered Transition material includes incomplete reconstructability of compaction transitions and missing exposed provenance for chained argument transformations.

Recovered Exception findings include a GAP in structured exception fidelity, several COVERED failure behaviors, and OPEN questions involving predicate diagnostics, retry history, and durable diagnostic history.

Receipt was not sufficiently recovered and is not inferred.

At whole-system level, six conceptual families survived archival recovery:

1. evidence metadata loss;
2. retrospective authorization provenance;
3. effective-state and compaction reconstruction;
4. tool-call transformation provenance;
5. structured failure fidelity; and
6. normalized terminal outcomes.

The exact mapping from these six families to the frozen final aggregate of **three GAPs** was not recovered. We therefore do not reverse-engineer that mapping.

No preserved Antigravity review artifact records a CHALLENGED disposition against an EASTER primitive. This is an archival statement, not evidence that every primitive was affirmatively challenged and survived.

## 6.5 DRC/EASTER asymmetry observed in the corpus

The frozen DRC overlay classified Distinction, Relation, and Constraint as COVERED for all six systems.

That result should be interpreted cautiously. The corpus consists of mature agent architectures selected toward rich representation, and individual DRC primitive receipts remain incomplete for much of the corpus.

Nevertheless, the combined results establish one bounded relationship within the examined set:

**under the applied classifications in this corpus, DRC coverage did not entail zero EASTER GAPs.**

The OpenAI Agents SDK and Google Antigravity both received D/R/C COVERED dispositions while retaining one or more frozen EASTER GAPs within their inspected boundaries.

The converse relationship was not observed. No system in the corpus demonstrated EASTER coverage while failing the DRC overlay. The corpus therefore establishes only this observed one-way non-entailment; it does not establish a general architectural separation theorem or determine whether EASTER-covered systems necessarily possess adequate DRC structure in userland.

## 6.6 No preserved primitive challenge in the recovered corpus

Across the recovered six-system record, **no preserved review artifact records a CHALLENGED disposition against one of EASTER's six primitives**.

That archival absence is not equivalent to showing that every primitive was affirmatively stress-tested in every system and survived challenge. Recovery is incomplete, and the manuscript does not infer missing primitive-level dispositions from aggregate results.

Within the preserved material, observed deficiencies could still be described using the existing EASTER lenses without a recovered disposition proposing a replacement or additional primitive. This does **not** establish that the six primitives are necessary, minimal, or universally sufficient.

One explicit subtraction test occurred during the LangGraph analysis. **Invariant** was considered as a possible seventh EASTER primitive and rejected. Invariant was useful for reasoning about equivalence or correctness across possible executions, but was not judged necessary for representing or reconstructing the execution that actually occurred.

This is evidence of one explicit primitive-set test, not proof of six-primitive minimality or evidence that every primitive underwent an equivalent test.

## 6.7 Archival result

The comparative study produced a second result about the research method itself: preserving a frozen aggregate conclusion is not equivalent to preserving a publication-ready evidence package.

Recovery quality varied substantially across systems. Some primitive findings, source pins, and composition mappings were recoverable; others were not.

The archival reconstruction therefore established a rule that Draft 2 adopts throughout:

**missing archival evidence is publication work, not permission to retrospectively reclassify.**

The comparative results should consequently be read as a bounded architectural record of what survived the frozen review process, including its OPEN findings and unknowns, rather than as a normalized benchmark dataset.