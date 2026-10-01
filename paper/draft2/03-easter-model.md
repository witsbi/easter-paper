# 3. EASTER: A Model for Consequential Continuity

EASTER is a six-primitive model for preserving consequential work across changes in session, agent, model, runtime, or machine. The six primitives are **Evidence, Authority, State, Transition, Exception, and Receipt**.

The model separates the continuity of consequential work from the semantic interpretation of that work. Userland determines what a payload means, whether a claim is true, which branch should be preferred, which operations are consequential enough to project to the kernel, and what consequences should follow. EASTER does not independently discover consequentiality from domain semantics. Once userland submits an operation through the EASTER boundary, the kernel defines a bounded continuity contract for that admitted projection: records are admitted under explicit Authority, state changes retain lineage, unsuccessful operations remain distinguishable from accepted State, and kernel operation outcomes remain inspectable.

The reference implementation realizes this model as a small authoritative kernel. The model and the reference implementation are distinguished throughout this paper: properties required by the EASTER continuity contract are not necessarily properties of every possible implementation, and implementation choices such as storage engine, transport, authentication mechanism, or interface are not themselves EASTER primitives.

## 3.1 The six primitives

| Primitive | Role in EASTER | Boundary |
| --- | --- | --- |
| **Evidence** | Durable, independently identifiable material that may be cited in support of consequential work. | Recording Evidence does not establish that it is true, authentic, relevant, or sufficient. |
| **Authority** | The permission represented by the EASTER Authority mechanism under which an operation may be admitted, including the lifecycle of grants and revocation. | Authority does not establish semantic correctness, truth, desirability, or application-level policy sufficiency. The reference kernel's v0.1 grant scope is narrower than a general RBAC/capability policy system. |
| **State** | Immutable admitted work-state from which later continuation may proceed. | State is not a kernel-selected current, canonical, correct, or preferred representation of the work. |
| **Transition** | The admitted lineage relation from an existing State to a newly admitted State under valid Authority. | Transition does not require global linearity; legitimate branches may share a predecessor. |
| **Exception** | Durable diagnostic material describing an operation that failed rather than becoming accepted consequential State. | An Exception is not an accepted Transition and does not itself alter authoritative State. |
| **Receipt** | Immutable kernel-authored record of the outcome of an attempted operation that reached the kernel's receipt-capable admission path. | A Receipt records the kernel outcome; it does not cover requests rejected before that boundary, guarantee persistence through storage catastrophe, semantically endorse the payload, or establish external-world causality. |

These primitives are intentionally narrow. They do not attempt to reproduce an agent runtime, workflow engine, policy language, semantic model, or reasoning system inside the kernel.

### Evidence

Evidence allows consequential work to cite durable material without asking the kernel to determine what that material means. Evidence may support later transitions or decisions, but its admission establishes provenance rather than truth. A recorded observation may be mistaken; a document may be incomplete; two pieces of Evidence may conflict. Those questions remain outside the continuity contract.

This distinction allows EASTER to preserve disagreement without silently resolving it. Later work can cite the relevant Evidence while leaving interpretation to userland.

### Authority

Authority answers whether the EASTER Authority conditions for a submitted kernel operation are satisfied at admission time. Authority is maintained independently from State: historical State does not confer future permission, and replaying or branching from an earlier State cannot restore revoked Authority.

The reference kernel supports explicit grant and revocation operations. Authority validity is evaluated as part of the consequential admission operation so that a concurrent revocation and attempted transition resolve according to serialized kernel order rather than allowing stale permission to resurrect itself through State history.

In reference kernel v0.1, grant semantics are deliberately limited. Any currently valid non-root grant may authorize an ordinary State transition when exercised by the identity that holds it; root grants additionally authorize Authority administration such as definition, grant, and revocation. The kernel does not interpret arbitrary application roles, object-level permissions, or fine-grained domain capability scope from opaque payloads. Those richer policy decisions remain userland responsibilities unless represented by mechanically enforced Authority structure.

Authority therefore establishes permission under the kernel's represented Authority rules. It does not establish that the resulting payload is correct, wise, truthful, desirable, or permitted under every external application policy.

### State

State is an immutable admitted consequential payload. Once admitted, an existing State is not rewritten into a later condition. Change is represented by admitting another State and connecting the two through Transition.

The model permits branching. Multiple later States may legitimately descend from the same predecessor, and the kernel does not select a single branch as current, canonical, preferred, or true. Selecting which branch should guide future work remains a userland decision.

The reference kernel contains a Genesis State as the sole State permitted without an incoming Transition. Subsequent admitted States obtain lineage through Transition.

### Transition

Transition records consequential change as an explicit relationship from one admitted State to another newly admitted State. It provides lineage without requiring the history to form one global linear chain.

Transition does not itself create Authority. An operation must already possess valid Authority to be admitted. Nor does Transition imply that a successor State is semantically better than its predecessor; it establishes that the change was admitted under the kernel's structural and authority rules.

### Exception

Exception preserves diagnostic material when an operation fails rather than becoming accepted State. This separation prevents failure information from being silently confused with an admitted change to consequential work.

Exceptions are durable records when the failure-recording path itself commits successfully, but they do not become accepted State merely because they were recorded. Their role is diagnostic: they preserve what prevented an attempted operation from completing. A catastrophic failure that prevents the kernel from persisting its own failure record lies outside this durability claim.

### Receipt

Receipt is the kernel-authored record of an operation's outcome once an attempted operation reaches the reference kernel's receipt-capable admission path and the outcome record itself can be persisted. The reference kernel distinguishes three ordinary post-bootstrap outcomes:

- **ACCEPTED** — the operation and its requested authoritative effects were admitted atomically.
- **REJECTED** — the kernel refused admission under its rules and the requested authoritative effects were not committed.
- **FAILED** — an exception prevented completion; the attempted authoritative effects were unwound, and a separate failure-recording transaction preserves a FAILED Receipt and diagnostic Exception when that recording transaction succeeds.

Receipt therefore answers a narrower question than semantic correctness: **what durable outcome did the authoritative kernel boundary record for this attempted operation?**

This scope excludes requests refused by authentication, transport, parsing, or other components before the kernel's receipt-capable path. It also excludes the stronger claim that a Receipt must survive a storage failure that prevents the Receipt itself from being committed. If failure-record persistence itself fails, the reference implementation rolls that recording transaction back rather than leaving a partial or phantom failure record.

Receipt ordering does not replace State/Transition lineage, and an ACCEPTED Receipt does not establish that the admitted content is true or that an external-world effect occurred exactly once.

## 3.2 Kernel invariants

The six primitives obtain their architectural meaning from the relationships enforced among them. The reference kernel currently embodies the following invariants.

**Authority is checked on the consequential admission path.** Permission is not merely advisory metadata attached after a write. An operation that requires Authority must satisfy the relevant kernel-represented validity conditions before its requested authoritative effects are admitted.

**Accepted consequential change is atomic.** An accepted state-changing operation commits its associated State, Transition, and ACCEPTED Receipt as one authoritative outcome. A partially admitted transition is not a successful EASTER operation.

**Unsuccessful operations do not silently mutate authoritative State.** REJECTED and FAILED outcomes do not commit the requested State change. After the attempted operation's transaction has unwound, the reference implementation records the unsuccessful outcome through its failure-recording path; diagnostic Exception material may be preserved without promoting that material into accepted State.

**State is immutable.** EASTER represents change by additional State and Transition records rather than by rewriting prior consequential history.

**Lineage is explicit and branching is valid.** Transition records provide State lineage. Branching is not treated as corruption, and receipt sequence or insertion order does not define a preferred branch.

**The kernel does not designate current State.** EASTER preserves possible consequential histories but does not decide which admitted branch should be treated as current, canonical, preferred, or semantically correct.

**Authority is independent of historical State.** State and Transition history cannot manufacture, restore, or imply Authority. Revocation changes future permission without rewriting previously valid history.

**Evidence establishes provenance, not truth.** Evidence can be durably recorded and cited without becoming a kernel-certified fact.

**Exceptions remain diagnostically distinct from accepted State.** Recording why an operation failed does not convert the failed operation into a successful transition.

**Receipts describe kernel outcomes, not semantic endorsement.** ACCEPTED means that the kernel admitted the operation according to its contract. It does not mean that the payload is true, useful, desirable, or complete.

Together these invariants define the authoritative boundary more precisely than the six primitive names alone. EASTER is therefore not simply a taxonomy of records. It is a continuity model in which the primitive types have constrained relationships and distinct responsibilities.

## 3.3 Deliberate omissions and boundary discipline

EASTER is intentionally incomplete as an agent architecture.

The kernel does **not determine semantic truth**. It can preserve Evidence, State, lineage, Authority, failure information, and outcomes without deciding what those records mean.

The kernel does **not perform agent reasoning**. Planning, inference, model invocation, tool selection, memory retrieval, and other cognitive or orchestration functions belong outside the continuity kernel.

The kernel does **not interpret application policy**. Userland may define roles, identities, workflows, approval rules, capability structures, domain semantics, or other policy mechanisms. EASTER enforces only the authority and structural semantics mechanically represented at its boundary.

The kernel does **not decide what is consequential in the application domain**. Userland makes that semantic selection by deciding what operations and records to project through EASTER. The kernel can then preserve the continuity consequences of that projection; it cannot guarantee that userland projected every event that mattered.

The kernel does **not select a canonical branch or current State**. Branch choice is a semantic/application decision.

The model does **not claim exactly-once external execution**. A durable EASTER outcome cannot by itself prove whether an external side effect occurred once, multiple times, or outside the kernel's observable boundary.

The reference implementation does **not claim cryptographic tamper-evidence** merely because its authoritative records are append-oriented and immutable through the supported kernel interface. Storage-level or administrative compromise is a separate security concern.

EASTER also does **not guarantee projection completeness**. The kernel can preserve only what crosses its boundary. If userland omits, collapses, or distorts consequential information before projection, EASTER may faithfully preserve an incomplete representation.

These omissions are not proposed as missing primitives. They define the scope of the continuity contract. The central design boundary is therefore:

**userland owns meaning, consequentiality selection, and application policy; EASTER owns the admitted continuity record of the projection supplied to its kernel boundary.**

Whether this six-primitive boundary is sufficient across heterogeneous computational change is a broader research hypothesis considered later in this paper. The architecture described here establishes the object to be tested; it does not assume the hypothesis is already true.