# Pre-Prior-Art Provenance: The EASTER Conjunction Under Test

**Record compiled:** 2026-09-29 (Pax, at Ori's direction via Mercury relay)
**Status:** Provenance/corrobation record. This file is NOT an original research
artifact and must not be cited as one. It records (a) frozen conversational
evidence recovered by Ori and (b) the results of an independent check of that
evidence against inspectable repository history. The two provenance levels are
kept distinct throughout.

**Manuscript status:** No manuscript change is made or implied by this record.

---

## 1. The methodological question

Pax and Clawde independently converged on a candidate surviving EASTER
conjunction (see §2). The methodological question is whether this conjunction
was **independently motivated before** the closest-architecture investigation
(Fabric / Corda / Holochain, 2026-09-29), or whether it was **constructed
post-hoc** to occupy an empty region of the prior-art comparison — the
gerrymandering objection.

Ori recovered frozen research state predating the closest-architecture
investigation that bears directly on this question. This record preserves that
recovery and Pax's independent corroboration check.

---

## 2. The four-part conjunction under test

1. **Revocable authority validation inside the consequential admission path.**
2. **Uniform durable ACCEPTED / REJECTED / FAILED outcome recording.**
3. **Durable Exception/failure records that do not become accepted State.**
4. **No substrate-designated canonical current State, with branching permitted.**

---

## 3. Recovered pre-prior-art evidence (Ori's recovery)

The following is recovered frozen conversational/research state, as relayed by
Ori on 2026-09-29. It is **recovered evidence**, not repository-verified
evidence; §4 checks it against repositories independently.

### A. In-path authority + revocation

- Frozen September 21 EASTER v0.1 state records Authority validation inside the
  kernel transaction/admission path.
- The grant must exist and satisfy validity/revocation requirements before the
  consequential transition is admitted.
- Invalid/revoked authority results in rejection rather than admission, with a
  REJECTED Receipt.
- Earlier September 20 kernel red-team state also preserves the append-only
  Authority/State/Transition/Exception/Receipt structure and atomic failure
  behavior.

**Provenance-level precision (per Ori, preserved, not collapsed):** the
September 25 paper artifact directly preserves grants/revocation and
authority-before-transition semantics. The earlier September 21/24 frozen state
carries the *stronger* validity/expiry/revocation-in-transaction detail.

### B. Uniform ACCEPTED / REJECTED / FAILED receipts

Frozen September 21 v0.1 semantics already distinguish durable Receipts for
ACCEPTED, REJECTED, and FAILED. Recovered semantics include: ACCEPTED effects
commit atomically; rejected operations do not commit the requested state
change; unexpected failures produce FAILED Receipts. This predates the
Fabric/Corda/Holochain comparison.

### C. Exception durable but not accepted state

Frozen September 21 semantics explicitly preserve: "Exceptions are
diagnostics, not State." Unexpected failures produce durable/immutable
Exception diagnostic material plus the FAILED Receipt. The failed requested
effects do not become admitted State. This predates the prior-art comparison.

### D. No canonical current state + branching

Frozen September 21 v0.1 semantics explicitly preserve: "There is no
kernel-defined current State." and "Multiple States may descend from the same
State." Later frozen language, still predating the current
closest-architecture comparison, states: "The kernel chooses neither a
preferred branch nor a canonical head." This is direct pre-prior-art evidence
that canonicality abstention was an intentional EASTER semantic rather than a
property introduced after discovering Fabric's canonical world-state mismatch.

### E. September 25 paper artifact

The initial EASTER/DRC paper draft of September 25 independently preserves the
same architectural commitments before the closest-architecture investigation.
Recovered language includes: the kernel owns authoritative writes and
validates authority before committing transitions; Authority includes grants
and revocation; Receipt is the immutable outcome for accepted, rejected, or
failed operations; Exception is durable diagnostic/failure material for
operations that do not become accepted state; State is immutable admitted
work-state from which continuation may branch; State is not kernel-selected
current/canonical/preferred state. The document also records that the research
phase was frozen.

---

## 4. Independent repository corroboration (Pax, 2026-09-29)

Checked against inspectable history in `witsbi/easter` (public kernel
implementation repo) and `witsbi/easter-paper` (this repo). Classification
per commitment: **DIRECT** / **PARTIAL** / **NOT FOUND**. A NOT FOUND here
means "not found in repository history examined" — it is not evidence the
frozen conversational state did not exist.

### Commitment 1 — In-path authority + revocation: DIRECT

- `witsbi/easter`, tree at commit `0031fd20` (2026-09-21, "Merge pull request
  #14"), `kernel.py`, `transition()`: authority is validated **inside the
  write transaction**, after `BEGIN IMMEDIATE` has taken the write lock —
  "specifically so that a concurrent revoke cannot commit in a gap between
  reading this and writing the transition that depends on it."
- `_validate_grant` checks: grant exists; `valid_from` reached; `expires_at`
  not reached; not revoked; held by the requesting identity.
- `AuthorityError` → `record_failure(outcome="REJECTED")`; no authoritative
  write occurs (the write transaction does not commit).
- Earlier commits: `a5341487` (2026-09-19, "AUTHORITY-0B..0F: grant, exercise,
  exceed, revoke, post-revocation retry"); `435e3199` (2026-09-19, "Authority
  v0.1 redesign: State/Authority separation, root-only administration").
- Sep 25 paper artifact (this repo, `paper/manuscript.md` at `9d23bc0`):
  "The kernel owns authoritative writes, **validates authority before
  committing transitions**"; Authority row: "including **grants and
  revocation**."

### Commitment 2 — Uniform ACCEPTED / REJECTED / FAILED receipts: DIRECT

- `witsbi/easter`, `schema.sql` at `0031fd20` (2026-09-21), `receipts` table:
  `CHECK (outcome IN ('BOOTSTRAP','ACCEPTED','REJECTED','FAILED'))` and
  `CHECK (outcome = 'ACCEPTED' OR (outcome IN ('BOOTSTRAP','REJECTED','FAILED')
  AND transition_id IS NULL))` — REJECTED/FAILED receipts structurally carry
  no transition, enforced at the schema level.
- `kernel.py` `record_failure`: `KernelError` → REJECTED; `sqlite3.IntegrityError`
  → FAILED; unexpected exceptions → FAILED.
- Sep 25 paper artifact, Receipt row: "Kernel-authored **immutable outcome
  record for accepted, rejected, or failed operations**."

### Commitment 3 — Exception durable but not accepted state: DIRECT

- `witsbi/easter`, `schema.sql` at `0031fd20`: `exceptions` table keyed to
  `receipt_id` (not to states or transitions); schema header comment: "Failed
  operations leave immutable receipts/exceptions."
- The receipts-table CHECK above guarantees failed operations admit no state
  change.
- Sep 25 paper artifact, Exception row: "**Durable diagnostic/failure material
  for operations that do not become accepted state**"; body: "records failure
  outcomes **without mutating authoritative state**."

### Commitment 4 — No canonical current state + branching: DIRECT

- `witsbi/easter`, `schema.sql` at `0031fd20` (states-table comment): "The
  kernel has **no canonical-head/current-state concept and does not merge
  branches** — which branch to continue from is **entirely a userland choice,
  made per call, forever**." Also: "each accepted call commits its own
  distinct state and is a valid separate branch" from the same
  `from_state_id`; `states.parent_state_id` was deliberately removed.
- `kernel.py` `transition()` docstring at `0031fd20`: "neither is preferred,
  and the kernel does not merge them. There is **no canonical-head/
  current-state concept anywhere in this kernel**."
- The same comments are present in the 2026-09-24 (`b07c2e89`) and 2026-09-25
  (`2747fcba`) trees.
- Sep 25 paper artifact, State row: "**Immutable admitted work-state payloads
  from which continuation may branch**" — explicitly NOT "a kernel-selected
  current, canonical, or preferred state." Body: "A key design choice is that
  **EASTER does not select a single current branch** and does not decide
  semantic truth. The reference implementation supports branching..."

### Corroboration tally

| # | Commitment | Repository corroboration |
|---|-----------|--------------------------|
| 1 | In-path authority + revocation | **DIRECT** |
| 2 | Uniform ACCEPTED / REJECTED / FAILED receipts | **DIRECT** |
| 3 | Exception durable, not accepted state | **DIRECT** |
| 4 | No canonical current state + branching | **DIRECT** |

---

## 5. Discrepancies and precision notes

1. **Verbatim phrases.** The exact quoted phrases from Ori's recovery —
   "Exceptions are diagnostics, not State.", "There is no kernel-defined
   current State.", "Multiple States may descend from the same State.", "The
   kernel chooses neither a preferred branch nor a canonical head." — were
   **NOT FOUND verbatim** in repository history. The *semantics* are DIRECT
   in implementation and code-commentary language (see §4); the quoted
   phrasing is conversational-freeze language. Do not cite the phrases as
   repository strings.
2. **The September 18 freeze marker.** Commit `c94b0c2d` ("Freeze Intelligence
   Kernel v0.1", 2026-09-18) in `witsbi/easter` contains only `README.md`. It
   marks the freeze point but does not itself contain the recovered semantics;
   those live in the September 19–21 implementation and red-team commits. Do
   not cite the freeze commit for semantics it does not contain.
3. **The .docx embedded metadata.** `paper/source/DRC_EASTER_initial_paper_draft.docx`
   carries `python-docx`-generated placeholder metadata (2013 dates), which
   does **not** corroborate the September 25 date. The date rests on the
   manuscript's own header ("Draft 0.2, dated 25 September 2026"), the commit
   message of `9d23bc0` ("Add Draft 0.2 manuscript (DRC+EASTER, 25 Sep
   2026)"), and Nathan's records.
4. **Provenance levels preserved.** The September 25 paper artifact carries the
   *coarser* semantics (grants/revocation named; authority-before-transition).
   The September 21 kernel implementation carries the *stronger* detail
   (validity/expiry/revocation checked inside the write transaction, after the
   write lock). These levels are not collapsed in this record.
5. **Commit-timestamp ordering.** The manuscript commit `9d23bc0` is timestamped
   2026-09-29T14:54:11-05:00; Clawde's closest-architecture commit `2dbdbe3`
   is timestamped 2026-09-29T19:39:32-05:00 — roughly five hours later. The
   paper artifact therefore predates the investigation by commit timestamp as
   well as by its internal September 25 date.

---

## 6. Preliminary provenance conclusion

The recovered evidence supports this limited conclusion: **all four elements
of the conjunction independently identified by Pax and Clawde during the
Fabric/Corda/Holochain comparison were already present in frozen EASTER
descriptions (implementation, schema, comments, and the September 25 paper
draft) several days before that comparison.**

**Explicit non-claim:** this evidence addresses the post-hoc-selection
(gerrymandering) hypothesis only. It does **not** establish architectural
novelty, does not exhaust prior art, and does not warrant strengthening any
novelty claim. The working novelty language remains "in the systems and
literature examined to date, we did not identify…".

---

## 7. References

- `witsbi/easter` (public): kernel implementation history, commits
  `c94b0c2d` (2026-09-18) through `0031fd20` (2026-09-21), `b07c2e89`
  (2026-09-24), `2747fcba` (2026-09-25). Key files: `kernel.py`,
  `schema.sql`, `authority_0b_0f.py`.
- `witsbi/easter-paper` (private, this repo): `paper/source/DRC_EASTER_initial_paper_draft.docx`
  (Draft 0.2, dated 25 September 2026); `paper/manuscript.md` at `9d23bc0`.
- Closest-architecture investigation: branch `clawde-sighted-draft2-r1`,
  commit `2dbdbe3` (2026-09-29); Pax independent pass, research notes
  `workspace/research_notes/easter-closest-prior-architecture-20260930-0052/`;
  reconciliation 2026-09-29.
