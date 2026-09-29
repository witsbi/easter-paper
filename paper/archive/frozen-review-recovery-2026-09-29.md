# Frozen review recovery — 2026-09-29

**Provenance.** Recovered by Ori from the frozen EASTER/DRC review history for the six-system corpus; archived by Pax on `draft1-shadow-r1` without reclassification.

**Rule.** This is an archival reconstruction artifact, not a new review. Do not reclassify systems. Do not infer primitive statuses from aggregate gap counts. Preserve uncertainty explicitly.

---

## 1. Hermes Agent

### Recovered

- Whole-system freeze dated Sep 24, 2026.
- Evidence: COVERED.
- Authority: COVERED.
- State: COVERED.
- Transition: COVERED with surviving OPEN H-OPEN-1.
- Exception: COVERED.
- Receipt: COVERED with same surviving OPEN H-OPEN-1.
- Whole-system: 0 demonstrated GAP, 0 CHALLENGED.
- H-OPEN-1: unrecoverable external-effect window: effect occurs → Hermes durable record lost → no independent external receipt → later recovery cannot establish whether effect occurred.
- Explicitly not promoted to GAP.
- DRC frozen overlay: D/R/C all COVERED.

### Not yet recovered

- Exact primitive DRC review receipts.
- Exact repo commit/version pin.

### Disposition

- Primitive-level EASTER evidence recoverable.
- Final archival source package incomplete.

---

## 2. OpenClaw

### Recovered

- Frozen review Sep 24–25, 2026.
- Source commit: `2ef3b4a0…`.
- Initial primitive sweep: 30 COVERED / 11 OPEN / 0 GAP / 0 CHALLENGED.
- Whole-system:
  - Evidence COVERED
  - Authority COVERED
  - State COVERED + OC-OPEN-1
  - Transition COVERED + OC-OPEN-1
  - Exception COVERED
  - Receipt COVERED + OC-OPEN-1 + OC-OPEN-2
- Whole-system: 0 demonstrated GAP, 0 CHALLENGED.
- OC-OPEN-1: unrecoverable external-effect window.
- OC-OPEN-2: delivery bypass / no authoritative later proof of delivery.
- DRC frozen overlay: D/R/C all COVERED.

### Not yet recovered

- Individual D/R/C primitive receipts.

### Disposition

- Strong primitive-level recovery.
- Exact source commit recovered.

---

## 3. LangGraph

### Recovered

- Frozen review Sep 24, 2026.
- Whole-system: 0 demonstrated GAP / 0 CHALLENGED.
- Evidence: COVERED + OPEN; specific preserved findings include checkpoint state/bookkeeping, pending writes, provenance, parent lineage, metadata source distinctions, and UntrackedValue boundary as OPEN.
- Transition: 7 COVERED / 4 OPEN / 0 CHALLENGED.
- Exception: 7 COVERED / 4 OPEN / 0 CHALLENGED.
- Receipt: 5 COVERED / 5 OPEN / 0 CHALLENGED.
- Authority/State were reviewed/frozen but exact finding matrices were not recovered in this pass.
- Whole-system composition closed many primitive-level OPENs.
- LANGGRAPH INVARIANT-0: Invariant considered as possible seventh primitive and rejected; useful for equivalence/correctness, not required for reconstructing the execution that actually occurred.
- DRC frozen overlay: D/R/C all COVERED.

### Not yet recovered

- Exact Authority/State finding counts.
- Exact source SHA/version pin.

### Disposition

- Substantial primitive-level recovery.
- Demonstrates importance of whole-system composition.

---

## 4. Anthropic Claude Agent SDK

### Recovered

- DRC frozen overlay: D/R/C all COVERED.
- Frozen EASTER aggregate: 0 GAP.
- Whole-system disposition: no demonstrated GAP in the frozen comparison.

### Not recovered

- Primitive-level EASTER classifications.
- Surviving OPEN findings.
- Detailed whole-system composition.
- Exact reviewed source SHA/version.

### Public source family

- Anthropic Claude Agent SDK Python / tool-permission surface.

### Disposition

- Aggregate result recoverable only.
- EASTER primitive cells must remain unknown unless original artifact is recovered.

---

## 5. OpenAI Agents SDK

### Recovered

- DRC frozen overlay: D/R/C all COVERED.
- Frozen EASTER aggregate: exactly 1 GAP.
- The existence of a real recorded GAP is preserved.
- Public source family includes Agents SDK docs, tracing, sessions; manuscript notes tracing can be disabled/unavailable under ZDR.

### Not recovered

- Which EASTER primitive owned the GAP.
- Primitive-level COVERED/OPEN findings.
- Exact reviewed source SHA/version.

### Important correction

- Ori previously recalled an Evidence OPEN; that recollection is unverified and must not be used unless the actual freeze is recovered.

### Disposition

- Aggregate + existence of a real GAP recovered.
- Primitive mapping remains unknown.

---

## 6. Google Antigravity

### Recovered EASTER primitive findings

**Evidence:**

- GAP E-1: MCP annotations lost before policy evaluation.
- GAP E-2: exception fidelity lost.
- COVERED: call/result/step correlation.
- OPEN: truncation behavior.
- OPEN: HookContext / ToolContext fragmentation.
- CHALLENGED: none.

**Authority:**

- GAPs: retrospective authorization provenance; Boolean human approval; dynamic delegation provenance; silent ineffective sandbox behavior.
- COVERED: capability/authorization separation; required authorization boundary.
- CHALLENGED: none.

**State:**

- COVERED: recovery; trajectory/workspace separation; concurrency protection.
- GAP: compaction change metadata.
- OPEN: exact effective context; cross-domain provenance.
- CHALLENGED: none.

**Transition:**

- T-3: compaction lacks reconstructable transition metadata.
- T-4: chained argument transformations lack exposed provenance.
- Full finding counts not recovered.

**Exception:**

- GAP: structured exception fidelity.
- COVERED: correlated failures; terminal propagation; appropriate suppression; fail-closed predicates.
- OPEN: predicate diagnostics; retry history; durable diagnostic history.
- CHALLENGED: none.

**Receipt:**

- Not sufficiently recovered.

### Whole-system composition

- Conceptual families recovered:
  1. Evidence metadata loss
  2. retrospective authorization provenance
  3. effective-state / compaction reconstruction
  4. tool-call transformation provenance
  5. structured failure fidelity
  6. normalized terminal outcomes
- No demonstrated CHALLENGE to EASTER.
- Frozen final aggregate: 3 GAPs.
- Exact mapping from the six conceptual families to the final three GAPs not recovered.

### DRC

- Sep 25 frozen result: D/R/C all COVERED.
- OPEN none, GAP none, CHALLENGED none.
- Observability limitation: public SDK wraps a compiled runtime.

### Not recovered

- Exact runtime version/commit.
- Full Receipt primitive freeze.
- Exact final 3-GAP mapping.

---

## Final archival conclusions

**A.** Aggregate gap counts are not sufficient to reconstruct primitive state.

**B.** 0 GAP did not mean six uncomplicated COVERED primitives; Hermes, OpenClaw, and LangGraph retained OPEN findings.

**C.** Preservation quality is uneven across systems and does not appear to track review chronology cleanly.

**D.** FREEZE preserved substantial consequential research state, but not a complete scholarly evidence package.

**E.** Missing source/version pins and primitive-level receipts are publication work, not grounds for retrospective reclassification.

**F.** The manuscript must distinguish recovered primitive evidence from aggregate frozen results whose primitive decomposition is presently unknown.

**G.** Do not infer any missing primitive status from remembered summaries.
