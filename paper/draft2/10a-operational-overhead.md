## 10.17 Operational overhead is unmeasured

The present study does not characterize the performance or storage cost of the reference implementation. Append-oriented authoritative history and per-operation Receipts introduce write amplification and storage growth, while Authority validation adds work to the consequential admission path. No benchmark in this paper quantifies throughput, latency, database growth, compaction requirements, or long-run operational cost. These characteristics therefore remain implementation-evaluation work rather than demonstrated properties of EASTER.
