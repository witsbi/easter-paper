# 4. Reference Implementation

EASTER is accompanied by a reference implementation intended to make the six-primitive model executable and adversarially inspectable. The current implementation is a Python kernel over SQLite, with additional interfaces and deployment components layered outside the kernel. This section describes the implementation as evidence that the model can be instantiated; it does not treat every implementation choice as part of the EASTER model.

The implementation divides enforcement between Python and SQLite. Python owns operation semantics such as authority validation and admission behavior. SQLite supplies transactional serialization, foreign-key integrity, structural constraints, and immutability enforcement. Userland payload meaning remains opaque to both layers except where a property must be mechanically enforced by the kernel.

## 4.1 Authoritative storage

The reference schema contains durable records for identities, authority definitions, authority grants and revocations, States, Evidence, Transitions, Receipts, Receipt–Evidence associations, and Exceptions.

Authoritative records are append-oriented. Database triggers reject UPDATE and DELETE operations against authoritative tables. Corrections, revocations, recovery, and later interpretation therefore occur through additional records rather than rewriting earlier history.

Payloads are represented as JSON where userland meaning is required. Structural properties that the kernel must mechanically enforce are represented separately. For example, root Authority is represented by a kernel-enforced `is_root` property rather than inferred from an opaque JSON payload.

This split implements a general boundary rule of the reference kernel:

**mechanically enforced kernel properties are explicit structure; application meaning remains opaque payload.**

## 4.2 Transaction boundary

Authoritative writes execute inside SQLite `BEGIN IMMEDIATE` transactions. The kernel acquires the write transaction before performing authority validation for an operation that depends on that Authority.

This ordering is consequential. An earlier implementation allowed authority validity to be inspected before the authoritative write transaction acquired its lock. A concurrent revocation could therefore occur between validation and commit. The current implementation validates the grant using the same database connection and serialized transaction that performs the resulting write.

Accordingly, an accepted operation is evaluated against the Authority state visible at its position in the kernel's serialized write order.

For accepted state transitions, the requested State, Transition, associated Evidence links, and ACCEPTED Receipt are committed as one transaction. If an exception escapes that transaction, the transaction context rolls back its writes rather than leaving partial admission.

The supported operation then handles the failure outside that rolled-back transaction. `record_failure()` opens a new `BEGIN IMMEDIATE` transaction and writes the unsuccessful outcome as a Receipt plus linked Exception; for submitted Evidence identifiers that already exist, it may also preserve Receipt–Evidence associations. The failure-recording transaction creates no requested State or authoritative Transition. A successful failure-recording transaction therefore leaves the attempted authoritative change absent while preserving the fact and diagnostic classification of the unsuccessful attempt.

The schema additionally constrains each operation identifier to at most one terminal Receipt. A duplicate outcome record for an identifier that already has a terminal Receipt is rejected by the database itself, and the kernel surfaces the rejection as a deliberate error rather than recording a second outcome. The enforcement is therefore a schema property, not a caller-discipline convention.

This two-stage behavior is important: the FAILED Receipt and Exception are **not survivors of the transaction that failed**. The attempted operation transaction is unwound first; the failure record is a subsequent kernel transaction. If failure-record persistence itself cannot commit, that second transaction also rolls back. The implementation therefore does not claim that every catastrophic storage/process failure can produce a durable Receipt.

Regression evidence exercises this boundary directly. A genuine SQLite integrity failure and a generic unexpected exception both produce a FAILED Receipt linked to an Exception while leaving zero requested authoritative effects. Separate Exception red-team tests exercise all six supported write entry points and verify that unsuccessful operations leave no authoritative effect other than their Receipt/Exception failure record. Tests also distinguish a genuine persistence failure in `record_failure()` itself: if even the fallback failure record cannot be persisted, the transaction rolls back with no phantom Receipt.

The implementation therefore relies on SQLite transaction atomicity as an implementation mechanism for two separate guarantees: accepted authoritative effects commit together with their ACCEPTED Receipt, while unsuccessful attempted effects are rolled back before any durable failure record is written.

## 4.3 Authority implementation

Authority is implemented independently from State and Transition history.

Authority definitions and possession are separate records. An identity possesses Authority through an immutable grant. Grants may have validity intervals and may subsequently be invalidated through append-only revocation records rather than modification of the original grant.

The current implementation supports direct revocation of a grant and `REVOKE_ALL`, which invalidates grants held by an identity as of the revocation's position in Authority's ordered history.

Grant and revocation records share an Authority-owned monotonically ordered sequence. Authority validity is determined from this ledger rather than inferred from Receipt payloads or wall-clock ordering.

This separation was strengthened through adversarial remediation. A prior design derived revocation information from Receipts and used timestamps in ways that allowed clock-ordering anomalies. The current implementation makes Authority's own records the authoritative basis for Authority validity while leaving Receipts responsible for recording what the kernel did.

Root capabilities are likewise represented as mechanically enforced Authority properties. Root-authorized operations govern Authority definition, grant, and revocation, while ordinary state transition does not create or mutate Authority.

The v0.1 scope is deliberately limited. For ordinary State transitions, a currently valid non-root grant held by the requesting identity is sufficient under the kernel's Authority rules; `authority_id` is not a fine-grained RBAC or object-capability policy for State content. Root grants additionally authorize Authority administration. Application-specific roles, object permissions, and semantic approval rules remain userland concerns unless they are represented by mechanically enforced kernel structure.

The result is a deliberate separation:

**State history cannot manufacture Authority, and Receipt history does not determine Authority validity.**

An unauthorized attempt that reaches a supported kernel operation may produce a REJECTED Receipt documenting the kernel outcome, while producing no requested authoritative mutation. Receipt records the attempt's disposition; it does not confer or substitute for Authority. Authentication or transport refusal before the kernel is reached is outside this Receipt claim.

## 4.4 State and Transition implementation

State rows contain immutable JSON payloads and identifiers. State does not contain its own parent pointer. Lineage is represented exclusively through Transition records connecting `from_state_id` to `to_state_id`.

The reference database begins from a distinguished Genesis State. Genesis is the sole State without an incoming Transition. Later States are admitted through successful transitions.

The schema permits multiple Transitions from the same predecessor. Repeated or competing accepted operations therefore produce separate branches rather than overwriting one another.

No schema field or kernel operation designates a canonical head or current State. Branch selection and continuation remain explicit userland choices.

Each Transition records the specific Authority grant exercised for its admission. A Transition therefore records not only lineage between States but the concrete grant under which that change entered authoritative history.

## 4.5 Evidence implementation

Evidence is stored as immutable, independently identifiable material.

Evidence can be associated with Receipts through a many-to-many relation. The same Evidence object may therefore support multiple operations without duplication.

The implementation deliberately distinguishes between Evidence cited in support of an operation and the Receipt created when an Evidence object itself is recorded. This prevents the provenance relation from becoming self-referential: the Receipt may establish that the kernel recorded the Evidence, but the Evidence does not thereby become support for its own creation Receipt.

Neither SQLite nor the Python kernel interprets whether Evidence is substantively true. Admission establishes that the material was durably recorded and can subsequently be cited.

## 4.6 Receipts and Exceptions

Receipts provide a uniform record **within the reference kernel's receipt-capable operation boundary**. The schema currently recognizes bootstrap, accepted, rejected, and failed outcomes.

An ACCEPTED Receipt may refer to an admitted Transition, but Receipt is not structurally dependent on Transition. Authority operations can succeed without producing a State Transition and still produce Receipts.

This decoupling allows Receipt to describe supported kernel operation outcomes without treating every consequential operation as a State change. It does not imply that requests refused before reaching the kernel—for example by gateway authentication—or catastrophic failures that prevent receipt persistence themselves must have kernel Receipts.

REJECTED and FAILED operations do not produce requested authoritative Transitions. The supported entry points catch kernel-rule rejection and unexpected failure after the attempted operation transaction has unwound, then call the separate failure-recording path. `record_failure()` atomically inserts the REJECTED or FAILED Receipt and its linked Exception in a new transaction. FAILED Receipts carry a minimal kernel-authored failure classification; the Exception owns the detailed diagnostics.

The failure-recording path is itself transactional. If it cannot persist a valid failure record, it rolls back rather than leaving only part of the Receipt/Exception pair. This bounds the durability claim to outcomes the kernel is able to commit; EASTER does not manufacture a durable record through an unavailable or failed persistence substrate.

The implementation therefore preserves recoverable failure without promoting failed work into authoritative State.

Receipt is also deliberately excluded from determining Authority validity. It records that the kernel performed an Authority operation; the resulting Authority records themselves determine later validity.

## 4.7 Genesis and bootstrap

A fresh reference database is initialized with a distinguished Genesis State and bootstrap records required to establish the initial Authority boundary.

Bootstrap is exceptional by necessity: before any Authority exists, ordinary Authority-mediated admission cannot yet authorize its own creation. The implementation therefore handles genesis explicitly rather than disguising bootstrap as an ordinary transition.

After bootstrap, consequential writes proceed through the ordinary kernel admission rules.

Genesis should therefore be understood as an implementation bootstrap boundary, not as evidence that EASTER requires one particular application-level starting state.

## 4.8 Interfaces are not the kernel

The repository now contains multiple components surrounding the kernel, including MCP and HTTP interfaces, consoles, a gateway, deployment configuration, and observability/read-model facilities.

These components are useful operationally, but they are not additional EASTER primitives.

The architectural requirement is that supported write interfaces project operations onto the same authoritative kernel semantics rather than independently reimplementing them. Authentication, transport security, network exposure, user interface, token distribution, and deployment policy remain boundary/userland concerns unless they affect the six-primitive continuity contract itself.

This distinction is especially important for evaluating EASTER as a model. A defect in a particular transport adapter is not automatically a defect in the six-primitive model; conversely, an interface that bypasses the authoritative kernel can violate EASTER's continuity guarantees even if the underlying database schema remains present.

## 4.9 Implementation scope

Several properties of the reference implementation should not be generalized into theoretical requirements without further evidence.

SQLite is an implementation choice, not an EASTER primitive.

Python is an implementation choice.

JSON is the current opaque payload representation, not a claim that consequential State must universally be encoded as JSON.

`BEGIN IMMEDIATE` is the mechanism used by this implementation to obtain serialized write behavior; the model requires the relevant admission invariants, not this specific database instruction.

The current root-capability model is a concrete Authority design. Other implementations may represent Authority differently provided they preserve the EASTER boundary being claimed.

Likewise, MCP, HTTP, console, gateway, and deployment mechanisms demonstrate possible access surfaces rather than defining the model.

The reference implementation therefore serves two purposes: it demonstrates that the six-primitive model can be instantiated as a working continuity kernel, and it provides a concrete artifact against which the model's claimed invariants can be tested.

It does not establish that this implementation is the only, optimal, or universally sufficient realization of EASTER.