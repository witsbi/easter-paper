# Appendix A — Comparative Evidence Register

This appendix records the surviving evidentiary basis for the six-system comparative result reported in Section 6. It is a **recovery register**, not a reconstructed original dataset.

The governing rule is:

> Missing historical evidence remains missing. This appendix does not infer primitive classifications from aggregate counts, present-day recollection, or later re-review.

The principal recovered artifact is `paper/archive/frozen-review-recovery-2026-09-29.md`, an archival reconstruction created from previously preserved EASTER/DRC research state. That artifact explicitly distinguishes recovered findings from material that was not recovered.

## A.1 Derivation status of the aggregate result

The manuscript reports the frozen per-system aggregate GAP-count sequence, in corpus order:

`(0, 0, 0, 0, 1, 3)`

The surviving evidence supports that sequence at different resolutions by system. It does **not** support reconstructing a complete primitive-by-system matrix.

| System | Frozen aggregate GAP count | Surviving derivation evidence | Irrecoverable / unknown |
| --- | ---: | --- | --- |
| Hermes Agent | 0 | Primitive-level EASTER dispositions survive for all six primitives; H-OPEN-1 survives for Transition/Receipt; whole-system freeze records 0 demonstrated GAP. | Exact source commit/version and individual DRC receipts not recovered. |
| OpenClaw | 0 | Initial sweep `30 COVERED / 11 OPEN / 0 GAP / 0 CHALLENGED`; whole-system primitive dispositions survive; OC-OPEN-1/2 survive; source commit abbreviated as `2ef3b4a0…`. | Individual DRC primitive receipts not recovered. |
| LangGraph | 0 | Substantial Evidence findings; Transition `7 COVERED / 4 OPEN`; Exception `7 COVERED / 4 OPEN`; Receipt `5 COVERED / 5 OPEN`; whole-system freeze records 0 demonstrated GAP. | Exact Authority/State matrices and source SHA/version not recovered. |
| Anthropic Claude Agent SDK | 0 | Frozen aggregate `0 GAP` and DRC D/R/C COVERED survive. | Primitive-level EASTER classifications, OPEN findings, composition reasoning, and exact reviewed version not recovered. |
| OpenAI Agents SDK | 1 | Frozen aggregate records exactly one real GAP; DRC D/R/C COVERED survives. | Owning EASTER primitive, primitive-level COVERED/OPEN findings, and exact reviewed version not recovered. A later recollection about Evidence is excluded. |
| Google Antigravity | 3 | Substantial Evidence/Authority/State/Transition/Exception findings survive; six conceptual issue families survive; frozen final aggregate records 3 GAPs; DRC D/R/C COVERED survives. | Receipt freeze, exact runtime version, and exact mapping from six issue families to final three GAPs not recovered. |

This table establishes what can and cannot be derived from the surviving archive. In particular:

- Anthropic's zero cannot be expanded into six COVERED primitive cells.
- OpenAI's one cannot be assigned to a primitive.
- Antigravity's three cannot be reverse-engineered from the six recovered issue families.

## A.2 Recovered system-level evidence

### Hermes Agent

Recovered:

- whole-system freeze dated September 24, 2026;
- Evidence COVERED;
- Authority COVERED;
- State COVERED;
- Transition COVERED with H-OPEN-1;
- Exception COVERED;
- Receipt COVERED with H-OPEN-1;
- whole-system 0 demonstrated GAP;
- H-OPEN-1: external effect may occur, local durable record may be lost, no independent external receipt may exist, leaving later recovery unable to establish whether the effect occurred;
- DRC D/R/C COVERED.

Not recovered:

- exact primitive DRC review receipts;
- exact repository commit/version pin.

### OpenClaw

Recovered:

- frozen review dated September 24–25, 2026;
- source commit recorded as `2ef3b4a0…`;
- initial primitive sweep: 30 COVERED / 11 OPEN / 0 GAP / 0 CHALLENGED;
- whole-system Evidence COVERED;
- Authority COVERED;
- State COVERED + OC-OPEN-1;
- Transition COVERED + OC-OPEN-1;
- Exception COVERED;
- Receipt COVERED + OC-OPEN-1 + OC-OPEN-2;
- whole-system 0 demonstrated GAP;
- OC-OPEN-1: unrecoverable external-effect window;
- OC-OPEN-2: delivery bypass may leave no authoritative later proof of delivery;
- DRC D/R/C COVERED.

Not recovered:

- individual DRC primitive receipts.

### LangGraph

Recovered:

- frozen review dated September 24, 2026;
- whole-system 0 demonstrated GAP;
- Evidence includes COVERED and OPEN findings, including the `UntrackedValue` boundary as OPEN;
- Transition: 7 COVERED / 4 OPEN;
- Exception: 7 COVERED / 4 OPEN;
- Receipt: 5 COVERED / 5 OPEN;
- Authority and State were reviewed/frozen, but exact matrices are not preserved;
- whole-system composition closed multiple primitive-level OPEN findings;
- `LANGGRAPH INVARIANT-0`: Invariant was considered as a possible seventh primitive and rejected as unnecessary for reconstructing the execution that actually occurred;
- DRC D/R/C COVERED.

Not recovered:

- exact Authority/State finding counts;
- exact source SHA/version pin.

### Anthropic Claude Agent SDK

Recovered:

- frozen EASTER aggregate: 0 GAP;
- whole-system disposition: no demonstrated GAP in the frozen comparison;
- DRC D/R/C COVERED.

Not recovered:

- primitive-level EASTER classifications;
- surviving OPEN findings;
- detailed whole-system composition;
- exact reviewed source SHA/version.

No primitive cells are inferred from the zero aggregate.

### OpenAI Agents SDK

Recovered:

- frozen EASTER aggregate: exactly 1 GAP;
- existence of a real recorded GAP;
- DRC D/R/C COVERED.

Not recovered:

- which EASTER primitive owned the GAP;
- primitive-level COVERED/OPEN findings;
- exact reviewed source SHA/version.

A later recollection suggested a particular Evidence disposition, but no preserved artifact substantiates it. That recollection is excluded.

### Google Antigravity

Recovered primitive material includes:

**Evidence**
- GAP: MCP annotations lost before policy evaluation;
- GAP: exception fidelity lost;
- COVERED: call/result/step correlation;
- OPEN: truncation behavior;
- OPEN: HookContext / ToolContext fragmentation.

**Authority**
- GAP families involving retrospective authorization provenance, Boolean human approval, dynamic delegation provenance, and silent ineffective sandbox behavior;
- COVERED: capability/authorization separation and required authorization boundary.

**State**
- COVERED: recovery, trajectory/workspace separation, concurrency protection;
- GAP: compaction change metadata;
- OPEN: exact effective context and cross-domain provenance.

**Transition**
- compaction lacks reconstructable transition metadata;
- chained argument transformations lack exposed provenance;
- full finding counts not recovered.

**Exception**
- GAP: structured exception fidelity;
- COVERED: correlated failures, terminal propagation, appropriate suppression, fail-closed predicates;
- OPEN: predicate diagnostics, retry history, durable diagnostic history.

**Receipt**
- not sufficiently recovered.

Recovered whole-system issue families:

1. Evidence metadata loss;
2. retrospective authorization provenance;
3. effective-state / compaction reconstruction;
4. tool-call transformation provenance;
5. structured failure fidelity; and
6. normalized terminal outcomes.

Frozen final aggregate: 3 GAPs.

The exact mapping from the six issue families to the final three GAPs was not recovered and is intentionally not reconstructed.

## A.3 Reproducibility boundary

This register makes the surviving derivation inspectable, but it does not make the historical study fully reproducible.

A reader can verify that Section 6 accurately reports the recovered artifact and its explicit unknowns. A reader cannot reproduce every original primitive classification for Anthropic or OpenAI, the exact Antigravity six-to-three composition decision, or several missing source/version pins from the surviving package alone.

Re-running the reverse review against current or pinned system sources would be valuable future work, but it would create a new replication dataset. It would not recover the missing historical evidence and should not be substituted for it.

## A.4 Preservation rule

The evidence register is intentionally asymmetric: some rows are detailed and others are sparse. That asymmetry is itself part of the research record.

The paper therefore prefers an explicit unknown over a retrospectively completed matrix.