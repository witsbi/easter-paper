# 1. Introduction

Intelligent systems increasingly perform work that outlives the computational context in which it was created. An agent may begin a task under one model and continue under another. A process may cross session boundaries, move between machines, survive a service restart, pass from one agent to another, or require human intervention before resuming. Long-running work may therefore persist while the model, context window, conversation history, orchestration framework, process, or runtime that produced it does not.

This creates a continuity problem.

Existing systems preserve many forms of information that help address that problem: messages, checkpoints, application state, event histories, workflow graphs, memories, databases, traces, and serialized execution context. These mechanisms are valuable, but they answer different questions. A conversation history records communication. A checkpoint may preserve execution state. A workflow graph describes possible control flow. A memory system makes selected information available later. An event log records things that occurred.

None of those categories alone specifies what must survive for **consequential work** to remain inspectable and continuable after the intelligence or runtime that produced it changes.

The distinction matters because retaining information is not the same as preserving the structure of a consequential decision.

Suppose an agent proposes a change, another participant supplies evidence, an authorized actor accepts the proposal, and a later runtime must continue from the result. Preserving only the resulting payload loses how it became admissible. Preserving only the conversation requires a later system to reconstruct the decision from narrative history. Preserving only successful operations loses rejected attempts and failures that may matter to subsequent reasoning. Treating every diagnostic event as accepted state confuses what happened during computation with what was admitted as consequential state.

A continuity substrate therefore faces several distinct questions. What supports a consequential claim or action? Who or what was permitted to act? What state was actually admitted? What change connected one admitted state to another? What failure or diagnostic condition occurred without becoming accepted state? What durable outcome records the attempted operation?

EASTER names these questions **Evidence, Authority, State, Transition, Exception, and Receipt**.

The central design move is to treat these as separate primitives rather than properties of a model, agent, conversation, workflow, or application. EASTER does not attempt to preserve the private cognitive or computational state of an intelligent system. It instead preserves a small external structure around consequential work.

This leads to a deliberately narrow architectural boundary.

EASTER does not decide what a payload means. It does not determine whether evidence is true. It does not authenticate users, choose goals, orchestrate agents, resolve semantic disagreement, rank branches, or decide which state should be treated as the current truth. Those responsibilities remain outside the kernel. The continuity layer is concerned with whether consequential structures and their outcomes can be durably represented and validated without requiring the originating intelligence to remain present.

This separation is important for heterogeneous systems. Internal representations differ across model providers, agent frameworks, orchestration systems, applications, and runtimes. A continuity mechanism coupled to those representations inherits their boundaries. A substrate defined in terms of external consequential structure may instead permit work to cross those boundaries without requiring reconstruction of the originating system itself.

This paper investigates that possibility through a concrete architecture rather than assuming it as a property of the six primitives.

We specify EASTER as a six-primitive model and implement a reference kernel in Python and SQLite. We examine its structural behavior and use the model as a reverse-review lens across six mature agent architectures. We separately examine representational structure through a Distinction–Relation–Constraint (DRC) overlay, use the reference implementation to preserve contribution provenance during preparation of this manuscript, and investigate the closest architectural traditions against which EASTER's combination of properties should be compared.

The evidence supports a bounded claim: EASTER is implementable as a small continuity substrate, its primitives expose meaningful distinctions when applied to existing systems, and the resulting architecture can preserve consequential provenance without owning semantic interpretation or canonical truth.

It does **not** establish that six primitives are minimal, that they are universally sufficient, or that work represented through EASTER can necessarily survive arbitrary computational change.

The stronger proposition remains a hypothesis:

**Evidence, Authority, State, Transition, Exception, and Receipt may be sufficient macroscopic variables for preserving consequential intelligent work across microscopic computational change.**

That proposition is useful precisely because it can fail. If a heterogeneous runtime cannot correctly continue consequential work represented through EASTER after access to the originating runtime's private state has been removed, the failure may reveal missing primitives, inadequate projection fidelity, or continuity structure not captured by the model.

The objective is therefore not to reconstruct an intelligence.

It is to determine how little durable structure must survive for consequential work to continue without it.
