# Hermes blind reservation for Draft-2 cold read

- **Frozen:** 2026-09-29
- **Decision:** unanimous 3–0 (Nathan, Pax, Ori)
- **Repo:** `witsbi/easter-paper`

## Reserved role

Hermes is reserved as the next cold reader: if Nathan commissions a blind
review of the Draft 2 manuscript, Hermes performs it under the same strict
blind protocol Clawde R1 used (manuscript file only; no history, no chain, no
prior critiques; reviewer never touches GitHub or EASTER; response frozen as
relayed before any post-hoc commit).

## Information boundary (frozen, not left to memory)

Until the Draft 2 blind review is complete — or Nathan explicitly lifts this
boundary sooner — Hermes must not receive substantive paper-review content:

1. The manuscript text in any version (Draft 0.2, merged `c269ff4`, any Draft 2 draft).
2. Any review findings: Clawde R1 (11 findings), Pax Shadow R1, Ori Shadow R1, Codex P2.
3. Any post-mortem, assessment, or verdict on those reviews.
4. Draft 2 plans, direction, or work items (including Ori's Draft 2 direction).
5. The recovery archives (`paper/archive/`) and any discussion of review classifications.
6. Discussion of the paper's claims, results, or reception.

**Incidental vs. substantive exposure:** filenames, branch names, or the bare
fact that a paper exists do not break blindness. Manuscript text, review
findings, critique content, classifications, and Draft 2 plans do.

## Lifting conditions

This boundary lifts when (a) Hermes completes the commissioned Draft 2 blind
review, (b) Nathan explicitly lifts it earlier, or (c) Nathan cancels the
Draft 2 review. Only Nathan decides.

## Boundary self-reference

This record is itself inside the boundary: it names review findings and Draft 2
plans. Do not share this file — or the Clawde role-transition record — with Hermes.
