# Draft 2 Public Artifact Manifest

**Purpose.** This manifest identifies immutable public Git objects for the Draft 2 reference implementation and the accepted post-remediation manuscript/research baseline. The completed publication package introduced by PR #13 must be pinned separately after merge, because its immutable merge commit does not exist while the pull request is still open. Branch names are intentionally not used as authoritative identifiers because branches can move.

## A. Reference implementation pin

**Repository:** `witsbi/easter`  
**Immutable commit:** `8bf422747836c96233f8dc11d4b11d1a61c832c1`  
**Commit date:** 2026-09-29  
**Pinned tree:** https://github.com/witsbi/easter/tree/8bf422747836c96233f8dc11d4b11d1a61c832c1

This commit is the publication pin for the reference implementation used by Draft 2. It includes `kernel.py`, schema/operation behavior, tests, MCP/API surfaces, and later transport/console work. Claims about the six-primitive kernel should be checked against the kernel and tests at this commit, not against a moving branch head.

Useful pinned entry points:

- Kernel: https://github.com/witsbi/easter/blob/8bf422747836c96233f8dc11d4b11d1a61c832c1/kernel.py
- Repository tests: https://github.com/witsbi/easter/tree/8bf422747836c96233f8dc11d4b11d1a61c832c1/tests
- MCP boundary: https://github.com/witsbi/easter/blob/8bf422747836c96233f8dc11d4b11d1a61c832c1/mcp_server.py
- HTTP API boundary: https://github.com/witsbi/easter/blob/8bf422747836c96233f8dc11d4b11d1a61c832c1/api_server.py

## B. Accepted Draft 2 manuscript and research-archive baseline

**Repository:** `witsbi/easter-paper`  
**Immutable commit:** `18ffc91e6550a6df7b41f335dd1879ec0002d111`  
**Commit date:** 2026-10-01  
**Meaning:** merge commit for PR #12, the accepted post-Hermes-remediation Draft 2 manuscript and research-archive baseline.  
**Pinned tree:** https://github.com/witsbi/easter-paper/tree/18ffc91e6550a6df7b41f335dd1879ec0002d111

This pin contains the accepted Draft 2 manuscript source plus the preserved archive used to bound the comparative review, prior-art reconstruction, and contribution-provenance claims. It intentionally predates the publication apparatus added by PR #13 and must not be described as the immutable identifier for that later package.

### Comparative-review recovery

- Frozen review recovery: https://github.com/witsbi/easter-paper/blob/18ffc91e6550a6df7b41f335dd1879ec0002d111/paper/archive/frozen-review-recovery-2026-09-29.md
- Recovered review state: https://github.com/witsbi/easter-paper/blob/18ffc91e6550a6df7b41f335dd1879ec0002d111/paper/archive/recovered-review-state-2026-09-29.md
- Appendix A comparative evidence register: https://github.com/witsbi/easter-paper/blob/18ffc91e6550a6df7b41f335dd1879ec0002d111/paper/draft2/APPENDIX-A-COMPARATIVE-EVIDENCE-REGISTER.md

### Closest-prior / novelty evidence

- Pax/Muse closest-architecture evaluation: https://github.com/witsbi/easter-paper/blob/18ffc91e6550a6df7b41f335dd1879ec0002d111/paper/archive/pax-closest-architecture-evaluation-2026-09-30.md
- Clawde/Sonnet Fabric evaluation: https://github.com/witsbi/easter-paper/blob/18ffc91e6550a6df7b41f335dd1879ec0002d111/paper/archive/clawde-hyperledger-fabric-evaluation-2026-09-30.md
- Clawde/Sonnet Corda/Holochain evaluation: https://github.com/witsbi/easter-paper/blob/18ffc91e6550a6df7b41f335dd1879ec0002d111/paper/archive/clawde-corda-holochain-evaluation-2026-09-30.md
- Pax/Muse + Clawde/Sonnet reconciliation: https://github.com/witsbi/easter-paper/blob/18ffc91e6550a6df7b41f335dd1879ec0002d111/paper/archive/clawde-pax-closest-architecture-reconciliation-2026-09-30.md
- Pre-prior-art conjunction provenance: https://github.com/witsbi/easter-paper/blob/18ffc91e6550a6df7b41f335dd1879ec0002d111/paper/archive/pre-prior-art-conjunction-provenance-2026-09-29.md
- Pax/Muse first-party methodology account: https://github.com/witsbi/easter-paper/blob/18ffc91e6550a6df7b41f335dd1879ec0002d111/paper/archive/pax-prior-art-first-party-account-2026-10-01.md
- Clawde/Sonnet first-party methodology account: https://github.com/witsbi/easter-paper/blob/18ffc91e6550a6df7b41f335dd1879ec0002d111/paper/archive/clawde-prior-art-methodology-account-2026-10-01.md

### Contribution-provenance evidence

- Contribution provenance index: https://github.com/witsbi/easter-paper/blob/18ffc91e6550a6df7b41f335dd1879ec0002d111/paper/archive/contribution-provenance-index-2026-10-01.md
- Nathan raw account: https://github.com/witsbi/easter-paper/blob/18ffc91e6550a6df7b41f335dd1879ec0002d111/paper/archive/contribution-nathan-raw-account-2026-10-01.md
- ChatGPT/Sol raw account: https://github.com/witsbi/easter-paper/blob/18ffc91e6550a6df7b41f335dd1879ec0002d111/paper/archive/contribution-sol-raw-account-2026-10-01.md
- Pax/Muse raw account: https://github.com/witsbi/easter-paper/blob/18ffc91e6550a6df7b41f335dd1879ec0002d111/paper/archive/contribution-pax-raw-account-2026-10-01.md
- Clawde/Sonnet raw account: https://github.com/witsbi/easter-paper/blob/18ffc91e6550a6df7b41f335dd1879ec0002d111/paper/archive/contribution-clawde-raw-account-2026-10-01.md
- Nathan three-tier reconstruction: https://github.com/witsbi/easter-paper/blob/18ffc91e6550a6df7b41f335dd1879ec0002d111/paper/archive/contribution-nathan-three-tier-reconstruction-2026-10-01.md

## C. Publication-package pin to be created after PR #13 merge

PR #13 adds the finalized Draft 2 bibliography, publication reference map, this manifest, and citation wiring needed for adversarial review. While the pull request remains open, no immutable merge commit can identify that completed package.

After PR #13 is merged, its merge commit SHALL be recorded as the immutable **Draft 2 adversarial-review candidate**. That post-merge identifier, together with the implementation pin in Section A and the accepted manuscript/research baseline in Section B, closes the publication-side location boundary without pretending that an earlier commit contains later packaging work.

No adversarial-review handoff should identify the moving branch head as the review target.

## D. Interpretation rule

The pins above make the surviving implementation, accepted manuscript baseline, and research evidence inspectable at immutable Git objects. The post-merge PR #13 identifier will additionally freeze the completed publication package. None of these identifiers converts unrecovered historical material into recovered evidence. In particular:

- an exact historical source/version pin that Appendix A marks unrecovered remains unrecovered;
- the Antigravity six-family-to-three-GAP primitive mapping remains unrecovered;
- a current official documentation link used for publication navigation does not retroactively become the source inspected in the historical review; and
- later research must be labeled as later research rather than recovery of the frozen procedure.

The manifest therefore preserves the missing-remains-missing rule while distinguishing the accepted research baseline from the later publication-package freeze.