# Draft 2 Public Artifact Manifest

**Purpose.** This manifest closes the publication-side reproducibility boundary for Draft 2 by naming immutable public Git objects for the implementation and preserved evidence package. Branch names are intentionally not used as the authoritative identifiers because branches can move.

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

## B. Accepted Draft 2 and research-archive pin

**Repository:** `witsbi/easter-paper`  
**Immutable commit:** `18ffc91e6550a6df7b41f335dd1879ec0002d111`  
**Commit date:** 2026-10-01  
**Meaning:** merge commit for PR #12, the accepted post-Hermes-remediation Draft 2 baseline.  
**Pinned tree:** https://github.com/witsbi/easter-paper/tree/18ffc91e6550a6df7b41f335dd1879ec0002d111

This pin contains the accepted Draft 2 manuscript source plus the preserved archive used to bound the comparative review, prior-art reconstruction, and contribution-provenance claims.

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

## C. Interpretation rule

These pins make the surviving publication evidence inspectable and immutable at the Git-object level. They do **not** convert unrecovered historical material into recovered evidence. In particular:

- an exact historical source/version pin that Appendix A marks unrecovered remains unrecovered;
- the Antigravity six-family-to-three-GAP primitive mapping remains unrecovered;
- a current official documentation link used for publication navigation does not retroactively become the source inspected in the historical review; and
- later research must be labeled as later research rather than recovery of the frozen procedure.

The manifest therefore closes the public-location problem without weakening the manuscript's missing-remains-missing rule.