# 2. Problem and Contributions

## 2.1 The continuity problem

We consider a unit of intelligent work **consequential** when its acceptance, rejection, failure, or resulting state can affect subsequent work.

The continuity problem addressed by this paper is:

> **What durable structure must be preserved so that consequential intelligent work remains inspectable and potentially continuable when the computational system that produced it changes or disappears?**

A computational change may include replacement of a model, loss of conversational context, process restart, transfer between agents, movement between machines, replacement of an orchestration framework, or migration to a different runtime.

The problem is not equivalent to persistence.

A system can persist data while losing distinctions required to interpret the consequences of prior work. A stored payload may identify an outcome without recording who was authorized to produce it. An event history may record an attempted operation without distinguishing acceptance from failure. A checkpoint may preserve enough implementation state to restart one runtime while remaining unusable to another. A conversation may contain the evidence for a decision while requiring a later intelligence to reconstruct which statements became consequential.

For continuity across heterogeneous systems, the durable representation should therefore minimize dependence on the private implementation state of the originating runtime.

At the same time, reducing the representation too aggressively can destroy distinctions that later work requires.

EASTER investigates whether six externally representable categories provide a useful boundary between these pressures:

**Evidence, Authority, State, Transition, Exception, and Receipt.**

The question is not whether all computation can be represented by these primitives. Nor is it whether they reproduce the internal reasoning of the intelligence that performed the work.

The question is whether they can preserve enough of the **consequential structure** of that work for another computational context to inspect what happened and, where appropriate, continue from it.

## 2.2 Consequential continuity

We use **consequential continuity** to distinguish the target of EASTER from several adjacent forms of continuity.

Conversational continuity preserves prior communication or makes it recoverable. Execution continuity preserves sufficient runtime state to resume a process. Application continuity preserves domain-specific state. Memory systems preserve selected information for later retrieval. Workflow continuity preserves control structure or progress through a defined process.

These mechanisms may contribute to consequential continuity, but none is identical to it.

Consequential continuity concerns the durable relationship among what was supported, what was authorized, what became accepted state, how accepted states were connected, what consequential failures occurred outside accepted state, and what outcome was recorded for an attempted operation.

This definition deliberately does not require preservation of hidden reasoning, model activations, complete prompts, complete conversation history, or runtime-specific implementation state.

It also does not imply that a later system will interpret preserved work correctly. Preservation and interpretation are separate problems.

EASTER addresses the former.

## 2.3 Scope and boundary

EASTER is designed as a continuity substrate rather than an agent architecture.

The kernel therefore does not own:

- semantic interpretation of payloads;
- truth evaluation of Evidence;
- identity authentication;
- application authorization policy beyond validation of admitted Authority;
- task planning or orchestration;
- model selection or inference;
- conflict resolution among semantic claims;
- branch ranking or branch selection;
- designation of a canonical current State; or
- domain-specific rules for deciding what should happen next.

These functions belong to userland systems built around the kernel.

The distinction is intentional. If the continuity substrate must understand the semantics, policy, or private runtime representation of every system that uses it, then continuity remains coupled to those systems. EASTER instead attempts to preserve a narrower structural record that heterogeneous systems can project into and recover from.

This boundary also limits what can be inferred from successful implementation. Demonstrating that EASTER can preserve consequential structures does not demonstrate that a future agent can correctly understand them, that the original decision was correct, or that the six primitives are sufficient for every form of intelligent work.

## 2.4 Contributions

This paper makes five contributions.

1. **A six-primitive model of consequential continuity.**  
   We define Evidence, Authority, State, Transition, Exception, and Receipt as separate architectural primitives and specify the distinctions among them, including immutable admitted State, explicit State-to-State Transition, revocable Authority, Exceptions outside accepted State, and durable outcomes for consequential operations.

2. **A reference implementation with a deliberately narrow kernel boundary.**  
   We implement the model in Python and SQLite and demonstrate structural invariants while leaving semantic interpretation, authentication, application policy, orchestration, and model behavior outside the kernel. The implementation does not designate a canonical current State and permits branching rather than resolving semantic alternatives internally.

3. **A comparative reverse review across six agent architectures.**  
   We apply the EASTER primitives as a common architectural lens to six mature systems and classify recovered support as COVERED, OPEN, GAP, or CHALLENGED. In corpus order, the recovered per-system aggregate GAP-count sequence is **(0, 0, 0, 0, 1, 3)**. This is a system-level aggregate summary, not a primitive-level vector; no preserved review artifact records a CHALLENGED disposition against an EASTER primitive. We separately apply a Distinction–Relation–Constraint overlay to test whether representational coverage entails EASTER continuity coverage in the examined corpus.

4. **An operational provenance case using EASTER itself.**  
   During preparation of this manuscript, the reference implementation preserves contribution claims and corrections across multiple human and AI participants, including kernel-admitted operations and repository integration. The case also records an outer gateway authentication failure that did not reach the EASTER kernel, sharpening rather than blurring the boundary between deployment authentication and kernel Authority. This provides an in-use example of the kernel preserving consequential provenance while leaving semantic judgment and publication authority outside the kernel.

5. **A bounded architectural and experimental hypothesis.**  
   We compare EASTER with relevant prior architectural traditions and identify a behavioral conjunction for which we did not find a matching architecture in the examined systems and literature: live revocable permission validation on the consequential admission path; durable accepted/rejected/failed outcome distinction for attempts reaching that authoritative boundary when persistence succeeds; durable failure diagnostics excluded from accepted work-state; and deliberate refusal by the substrate to designate a canonical current semantic work-state. We do not claim novelty for the individual mechanisms or exhaustive historical novelty. Instead, the resulting architecture motivates a falsifiable hypothesis: that the six EASTER primitives may constitute sufficient macroscopic variables for preserving consequential intelligent work across microscopic computational change.

## 2.5 Claim boundary

The paper distinguishes what has been demonstrated from what remains hypothetical.

The reference implementation demonstrates that the six distinctions can coexist in a working kernel with the specified boundary. The comparative review demonstrates how the EASTER lens classifies the examined systems under the recovered methodology. The provenance case demonstrates one operational use of the architecture.

These results provide evidence that the model is coherent and experimentally useful.

They do not establish minimality.

They do not establish universal sufficiency.

They do not establish semantic work-state portability.

The strongest claim is therefore reserved for future experimental evaluation:

> **If consequential work is faithfully projected through EASTER, can a heterogeneous runtime produce an acceptable next consequential action after access to the originating runtime's private state, conversation, memory, and implementation machinery has been removed?**

Section 11.6 defines the prospective oracle needed to judge such continuation without requiring Runtime B to reproduce Runtime A's hypothetical next output. A positive result would provide evidence for semantic work-state portability. A negative result would be equally informative if it exposes a missing primitive, a projection failure, an underspecified oracle, or another continuity dependency.

The architecture is therefore presented not as a completed theory of intelligent continuity, but as a concrete substrate from which that theory can be tested.
