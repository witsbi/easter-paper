# Recovered Review State — 2026-09-29

This artifact is an archival reconstruction of previously frozen research state recovered from retained conversation/research context on 2026-09-29.

It intentionally preserves:
- primitive-level findings where recovered;
- whole-system composition findings where recovered;
- aggregate frozen results where only summaries survived;
- surviving OPEN findings;
- partial or incomplete recoveries;
- missing source/version pins;
- explicit corrections where recollection could not be verified.

No missing status should be inferred from aggregate counts.

## 1. Hermes Agent

Recovered whole-system freeze:
September 24, 2026.

Recovered EASTER disposition:

- Evidence — COVERED.
- Authority — COVERED.
- State — COVERED.
- Transition — COVERED with surviving OPEN H-OPEN-1.
- Exception — COVERED.
- Receipt — COVERED with the same surviving OPEN H-OPEN-1.

Whole-system result:
- 0 demonstrated GAP.
- 0 CHALLENGED.

Recovered surviving OPEN:

H-OPEN-1 — unrecoverable external-effect window.

Shape:
external effect occurs
→ Hermes durable record is lost
→ no independent external receipt exists
→ later Hermes recovery cannot establish whether the effect actually occurred.

Important:
This OPEN was explicitly not promoted to GAP without evidence.

DRC recovery:
- D = COVERED.
- R = COVERED.
- C = COVERED.

This 3/3 result is recovered from the frozen comparative overlay.

Not yet recovered:
- individual Hermes D/R/C primitive review receipts;
- exact reviewed repository commit/version;
- complete source citations attached to each primitive finding.

Recovery disposition:
- primitive-level EASTER evidence is recoverable;
- final archival source package remains incomplete;
- the result was not inferred from the aggregate `0 GAP`.

---

## 2. OpenClaw

Recovered review date:
September 24–25, 2026.

Recovered source commit:
`2ef3b4a0…`

Recovered initial primitive sweep:
- 30 COVERED
- 11 OPEN
- 0 GAP
- 0 CHALLENGED

Recovered whole-system EASTER disposition:

- Evidence — COVERED.
- Authority — COVERED.
- State — COVERED + OC-OPEN-1.
- Transition — COVERED + OC-OPEN-1.
- Exception — COVERED.
- Receipt — COVERED + OC-OPEN-1 + OC-OPEN-2.

Whole-system result:
- 0 demonstrated GAP.
- 0 CHALLENGED.

Recovered surviving OPENs:

OC-OPEN-1 — unrecoverable external-effect window.

Shape:
non-idempotent external effect occurs
→ local durable record is lost
→ no independent external receipt exists
→ later recovery cannot establish whether the effect actually occurred.

Affected composition:
- State
- Transition
- Receipt

OC-OPEN-2 — delivery bypass.

Shape:
plugin/direct-send delivery can bypass the shared durable lifecycle
→ no authoritative later proof of delivery may exist.

Affected composition:
- Receipt

Recovered priority:
OC-OPEN-2 was prioritized first, then OC-OPEN-1.

Recovered source/architecture basis included:
- transcript DB;
- approvals;
- gateway/node execution;
- native-harness adapters;
- recovery machinery;
- delivery queue;
- audit/receipt surfaces.

DRC recovery:
- D = COVERED.
- R = COVERED.
- C = COVERED.

This 3/3 result is recovered from the frozen comparative overlay.

Not yet recovered:
- individual OpenClaw D/R/C primitive review receipts.

Recovery disposition:
- strong primitive-level recovery;
- exact source commit recovered;
- result not inferred from aggregate `0 GAP`.

---

## 3. LangGraph

Recovered review date:
September 24, 2026.

Whole-system result:
- 0 demonstrated GAP.
- 0 CHALLENGED.

Recovered Evidence findings include:

- committed checkpoints preserve channel values plus execution bookkeeping such as `channel_versions`, `versions_seen`, metadata, and graph-position information;
- successful node writes from failed/incomplete supersteps can survive as pending writes without falsely implying full next-state commit;
- pending-write provenance connects durable writes to originating task;
- `parent_config` and ancestor-chain reconstruction preserve actual branch lineage;
- checkpoint metadata distinguishes sources such as input, loop, update, and fork;
- pre-commit execution evidence and replay identity/provenance were examined.

Recovered Evidence OPEN:
UntrackedValue boundary.

Concern:
whether values deliberately excluded from checkpoint persistence can nevertheless influence a consequential durable outcome without enough corresponding durable evidence.

This remained OPEN, not GAP.

Recovered primitive finding counts:

Transition:
- 7 COVERED
- 4 OPEN
- 0 CHALLENGED

Exception:
- 7 COVERED
- 4 OPEN
- 0 CHALLENGED

Receipt:
- 5 COVERED
- 5 OPEN
- 0 CHALLENGED

Authority:
- reviewed/frozen;
- exact finding matrix not recovered in this pass.

State:
- reviewed/frozen;
- exact finding matrix not recovered in this pass.

Whole-system composition:
many primitive-level OPEN findings were closed by composition among checkpoint, task, pending-write, metadata, authorization/control, and fault-tolerance mechanisms.

Recovered whole-system conclusion:
within the EASTER six-primitive lens, LangGraph showed:
- no demonstrated GAP;
- no CHALLENGE.

Important:
this was not an equivalence claim that LangGraph "is EASTER."

Separate recovered finding:

LANGGRAPH INVARIANT-0.

Invariant was considered as a possible seventh EASTER primitive and rejected.

Reason:
Invariant was useful for reasoning about equivalence/correctness across possible executions, but was not necessary for representing/reconstructing the execution that actually occurred.

This is evidence of primitive-set subtraction/testing, but it is not being reclassified as a CHALLENGED finding against one of the six EASTER primitives.

DRC recovery:
- D = COVERED.
- R = COVERED.
- C = COVERED.

This result is recovered from the frozen comparative overlay.

Not yet recovered:
- exact Authority finding matrix;
- exact State finding matrix;
- individual D/R/C primitive receipts;
- exact source SHA/version pin.

Recovery disposition:
- substantial primitive-level recovery;
- demonstrates why whole-system composition mattered;
- result not inferred from aggregate `0 GAP`.

---

## 4. Anthropic Claude Agent SDK

Recovered:

DRC frozen overlay:
- D = COVERED.
- R = COVERED.
- C = COVERED.

Frozen EASTER aggregate:
- 0 GAP.

Whole-system disposition:
- no demonstrated GAP in the frozen comparative result.

Public source family:
- Anthropic Claude Agent SDK for Python;
- tool-permission / agent-option surface.

Not recovered:
- primitive-level EASTER classifications;
- surviving OPEN findings;
- detailed whole-system composition review;
- exact reviewed source SHA/version.

Recovery disposition:
- aggregate result recoverable only;
- EASTER primitive decomposition is currently unknown;
- do not infer six COVERED primitives from aggregate `0 GAP`;
- publication matrix cells should remain unknown until an actual primitive-level artifact is recovered.

---

## 5. OpenAI Agents SDK

Recovered:

DRC frozen overlay:
- D = COVERED.
- R = COVERED.
- C = COVERED.

Frozen EASTER aggregate:
- exactly 1 GAP.

Recovered fact:
the existence of one actual recorded EASTER GAP is preserved in the frozen comparative result.

Public source family:
- OpenAI Agents SDK documentation;
- tracing documentation;
- sessions documentation.

The manuscript also records that tracing can be disabled and may be unavailable under Zero Data Retention.

Not recovered:
- which EASTER primitive owned the GAP;
- primitive-level COVERED/OPEN findings;
- exact reviewed source SHA/version.

Important correction:
Ori previously recalled an OpenAI Evidence review with `0 GAP / 1 OPEN`, but no preserved artifact was recovered to support that recollection.

Therefore:
- do not use that recollection as evidence;
- do not place OPEN or GAP into a specific primitive cell based on memory or current-doc re-analysis.

Recovery disposition:
- frozen aggregate + existence of one real GAP recovered;
- primitive mapping remains unknown;
- do not infer the missing primitive decomposition from the aggregate `1 GAP`.

---

## 6. Google Antigravity

Recovered EASTER primitive findings:

### Evidence

Recovered:

GAP E-1:
- MCP annotations lost before policy evaluation.

GAP E-2:
- exception fidelity lost.

COVERED:
- call/result/step correlation.

OPEN:
- truncation behavior.

OPEN:
- `HookContext` / `ToolContext` fragmentation.

CHALLENGED:
- none.

### Authority

Recovered GAPs:
- retrospective authorization provenance;
- Boolean human approval;
- dynamic delegation provenance;
- silent ineffective sandbox behavior.

Recovered COVERED:
- capability/authorization separation;
- required authorization boundary.

CHALLENGED:
- none.

### State

Recovered COVERED:
- recovery;
- trajectory/workspace separation;
- concurrency protection.

Recovered GAP:
- compaction change metadata.

Recovered OPEN:
- exact effective context;
- cross-domain provenance.

CHALLENGED:
- none.

### Transition

Recovered partial findings:

T-3:
- compaction lacks reconstructable transition metadata.

T-4:
- chained argument transformations lack exposed provenance.

Full Transition finding counts were not recovered.

### Exception

Recovered GAP:
- structured exception fidelity.

Recovered COVERED:
- correlated failures;
- terminal propagation;
- appropriate suppression;
- fail-closed predicates.

Recovered OPEN:
- predicate diagnostics;
- retry history;
- durable diagnostic history.

CHALLENGED:
- none.

### Receipt

Not sufficiently recovered.

Do not infer Receipt classification from aggregate result.

### Whole-system composition

Recovered conceptual families:

1. Evidence metadata loss
2. retrospective authorization provenance
3. effective-state / compaction reconstruction
4. tool-call transformation provenance
5. structured failure fidelity
6. normalized terminal outcomes

Recovered whole-system conclusion:
- no demonstrated CHALLENGE to EASTER;
- the six primitives remained sufficient under the review.

Frozen final aggregate:
- 3 GAPs.

Not recovered:
- exact mapping from the six conceptual families to the final three GAPs.

Do not reverse-engineer the final three GAPs from the six families.

### DRC

Recovered review date:
September 25, 2026.

Recovered result:
- D = COVERED
- R = COVERED
- C = COVERED
- OPEN = none
- GAP = none
- CHALLENGED = none

Whole-system:
- 3/3 COVERED.

Recovered observability limitation:
the public Google Antigravity SDK wraps a compiled runtime, restricting inspection of some internals.

Not recovered:
- exact runtime version/commit;
- full Receipt primitive freeze;
- exact whole-system mapping from primitive findings to final 3 GAPs.

Recovery disposition:
- primitive sweeps are substantially recoverable;
- final composition mapping is incomplete;
- current paper's launch-blog citation is insufficient by itself to support the recovered primitive findings;
- stronger source packaging is required before submission.

---

# Cross-system archival conclusions

A. Aggregate gap counts are insufficient to reconstruct primitive-level review state.

B. `0 GAP` did not mean six uncomplicated COVERED primitives.

Recovered examples:
- Hermes retained H-OPEN-1.
- OpenClaw retained OC-OPEN-1 and OC-OPEN-2.
- LangGraph retained multiple primitive-level OPEN findings despite 0 whole-system GAPs.

C. Primitive sweeps and whole-system composition are distinct layers of the methodology.

Primitive-level uncertainty could remain OPEN while composition still produced no demonstrated whole-system GAP.

D. Preservation quality is uneven across systems.

Strong recovery:
- Hermes
- OpenClaw
- LangGraph
- Antigravity primitive sweeps

Weak/aggregate recovery:
- Anthropic
- OpenAI primitive decomposition

E. Preservation quality does not appear to track chronology cleanly.

Antigravity was reviewed early but retains substantial primitive detail.
Anthropic was reviewed later but currently survives mainly as an aggregate result.

F. FREEZE preserved substantial consequential research state but did not produce a complete scholarly evidence package.

Missing items include:
- source/version pins;
- some primitive-level receipts;
- whole-system mapping detail;
- direct publication-ready evidence links.

G. Missing archival evidence is publication work, not permission to retrospectively reclassify.

Do not fill missing classifications from:
- aggregate counts;
- present-day memory;
- current source re-analysis presented as if it were the frozen result.

H. The manuscript should distinguish:
- recovered primitive-level evidence;
- frozen aggregate result;
- partial recovered composition;
- currently unrecovered status.

I. The six-system status matrix should not imply that all `0 GAP` systems were six clean COVERED primitives.

J. Current recovery artifacts should be preserved before further normalization or manuscript editing.

K. This recovery artifact is itself NOT the original freeze.

It records what was successfully recovered on 2026-09-29 from previously preserved research state and explicitly preserves the gaps in that recovery.
