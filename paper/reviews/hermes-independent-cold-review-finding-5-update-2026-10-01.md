# Post-freeze provenance and disposition note — Hermes cold-review finding #5

## Scope

This note is separate from, and does not amend, the frozen independent cold review in [`hermes-independent-cold-review-2026-10-01.md`](hermes-independent-cold-review-2026-10-01.md). The archived review remains byte-for-byte the review produced against:

- manuscript: `witsbi/easter-paper@ef81644f655294ecb7d863a9c6ce527f7fef214f`
- implementation: `witsbi/easter@8bf422747836c96233f8dc11d4b11d1a61c832c1`
- frozen: `2026-10-01T19:45:59Z`
- SHA-256: `585d5931b41dbce4696cde6a93631c47d282ccdb54676dc394f99ae4246c0b02`

Finding #5 in that review must be read as a finding about those frozen targets. It has not been rewritten to reflect later implementation changes.

## Subsequent provenance

After the review froze:

1. Finding #5—the lack of schema enforcement for one terminal Receipt per `operation_id`—was independently reproduced against the pinned implementation.
2. Nathan accepted the intended invariant: **An operation identifier identifies one attempted kernel operation. At most one terminal Receipt may exist for that identifier; when durable outcome recording succeeds, exactly one exists.**
3. Hermes implemented the remediation in [`witsbi/easter` PR #31](https://github.com/witsbi/easter/pull/31), commit `3812cb144a38a1446fd053aa34df2feba7148478`.
4. The remediation was independently verified, including the original counterexample and additional concurrency/error-classification checks, and then merged as `7b8a0144dce24a2e4b3cc25a839c99ec8253c86f`.
5. Hermes's first-party remediation record was accepted into EASTER with these stable identifiers:
   - Evidence: `evidence:4be43ba1-39b7-45c1-bbe8-a1ca1a08c059`
   - Receipt: `receipt:34c03ae3-ad91-4897-ba8f-ff7efd952188`
   - Operation: `operation:4bb08f01-7892-4ff7-8a0c-3e6e9b1f45c1`

The separate EASTER observation recording the independent verification and merge is `evidence:eb26c568-751b-4630-8a7b-de20d701cbb7`.

## Disposition

**Finding #5: CLOSED by subsequent implementation remediation and independent verification.**

This disposition does not retrospectively change the frozen review or its assessment of the pinned implementation. All other findings in the cold review remain **OPEN / UNADJUDICATED**. This note makes no change to the manuscript's substantive text, claims, conclusions, or contribution statement.
