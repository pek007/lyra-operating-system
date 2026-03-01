---
title: "Decision Memo — Task & Decision Engine Project Definition Gate v2"
date: 2026-03-01
source: deepresearch
ingest_from: "telegram attachment file_94"
tags: [external-analysis, deepresearch, decision-memo, task-decision-engine]
decision_relevance: "approval basis for project-definition phase"
confidence: tbd
status: archived-source
---

# Decision Memo — Task & Decision Engine Project Definition Gate v2

Status: Proposed for approval  
Date: 2026-03-01 (Europe/Stockholm)  
Decision Owner: Peter  
Prepared by: Lyra  

## Decision requested

Approve a **Project Definition Phase** to validate and specify a Task & Decision Engine (TDE) for the Lyra/OpenClaw system, with a tightly bounded scope and explicit deliverables.

This approval is **not** approval to start a full product build. The approval is to produce (a) an unambiguous product thesis and success definition, (b) architecture + information architecture foundations, and (c) a credible, integration-first implementation pathway to a build-phase go/no-go decision. fileciteturn0file1L3-L16

## Vision, objectives, and non-goals

### Vision

The TDE is an **OS-grade governance and state layer** that lets Lyra operate as a closed-loop control system: intake → clarify → commit → execute → review → adjust, while remaining auditable and resistant to drift. fileciteturn0file0L3-L13 fileciteturn0file2L3-L16 citeturn0search6

### Primary objectives

This project is explicitly in service of three outcomes:

Lyra should be able to run continuously without human micro-management, while still allowing Peter to steer using high-level goals and decision rights. This implies “non-terminating” control loops (reconciliation and anti-stall behavior), not a static dashboard. fileciteturn0file0L3-L13 citeturn0search6

The solution must be built **on top of** existing OpenClaw primitives rather than replacing them. In particular, scheduling and wakeups should leverage OpenClaw’s gateway scheduler (cron) and heartbeat mechanisms, plus session routing and tool governance, instead of re-implementing these concerns in the TDE. fileciteturn0file1L3-L16 citeturn11search1turn11search0turn4search5turn10search0

It must be feasible to retire entity["company","Trello","task management software"] as a day-to-day operational dependency by establishing the TDE as the canonical system of record for (at minimum) task state, decision state, and traceable action/evidence linking. This requires an explicit migration and cutover design, not a vague “we’ll later move off it.” fileciteturn0file0L3-L13

### Non-goals for this definition gate

The definition phase must not balloon into a disguised build. The following are non-goals unless explicitly approved later:

A UI-first control panel rebuild as the primary deliverable (the “decision-first artifact” approach is the default). fileciteturn0file2L3-L16

A full workflow-orchestration platform replacement (e.g., attempting to build “Temporal, but for us” without proving governance value first). fileciteturn0file1L3-L16

ML-driven autonomous prioritization as a foundational dependency (the engine must work deterministically with policy and traceability constraints first). fileciteturn0file2L3-L16

## Scope and deliverables for the definition phase

This phase exists to prevent the “solution-first drift” failure mode by forcing clarity in: (a) decision use-cases, (b) information architecture, and (c) system boundaries/ownership. fileciteturn0file2L3-L16

### Required deliverables

A Start Packet for the TDE initiative, containing: product goal, the top decision outcomes it improves, explicit non-goals, measurable success metrics, and kill criteria (so the build phase cannot improvise its way into scope creep). fileciteturn0file2L3-L16

A prioritized use-case set that is written as “decision and control problems” rather than “features.” The use cases must explicitly show how high-level objectives become governed work. This follows the “jobs vs agents” framing: jobs are durable continuity contracts; agents are replaceable executors. fileciteturn0file0L18-L23 citeturn4search5

A first-pass information architecture (canonical object model + IDs + relationships) that is stable enough to prevent schema drift. At minimum, it must define: Task, Decision, EvidenceRecord, ChangeRecord, Objective/Goal, Approval/Authority, and Action (auditable side-effect). fileciteturn0file2L3-L16 citeturn0search0

An architecture baseline expressed as a small set of diagrams and contracts (not “big design up front”), using a consistent diagramming approach such as the entity["organization","C4 model","software architecture diagrams"] to keep system boundaries legible and reviewable. citeturn1search3turn1search6

An OpenClaw integration map that states exactly which existing OpenClaw primitives are used for which needs (wakeups, scheduling, isolation, session routing, tool governance, delivery), and where the TDE begins and ends. This explicitly leverages cron and heartbeat behavior rather than reinventing scheduling. citeturn11search1turn11search0turn4search0turn4search5

A Trello retirement design: minimum compatibility layer requirements (import/sync strategy if needed), cutover mechanism, and “Trello-free” steady state definition. fileciteturn0file0L3-L13

### Thin vertical slice to specify (definition-only)

The definition must specify one thin, end-to-end slice that demonstrates the engine’s governing role, without being UI-led:

Wakeup trigger (cron/heartbeat or event hook) → state evaluation (tasks/decisions) → decision packet generation → governed action proposal → approval gate (if required) → idempotent execution → audit/evidence linkage. fileciteturn0file2L3-L16 citeturn11search1turn11search0turn0search6

## Architecture stance and key technical choices

### Architecture stance

The recommended stance is a **hybrid governance architecture**: centralized governance state and audit trail, with decentralized execution by agents/tools, and deterministic reconciliation loops that continuously drive actual state toward desired state. fileciteturn0file2L3-L16 citeturn0search6

This stance is deliberately aligned with two widely used patterns:

Event-sourced state: storing “what happened” as immutable events makes auditability and “why did this happen” explanations feasible, and allows rebuild/replay of derived state. citeturn0search0turn0search5

Controller-style reconciliation: a non-terminating loop that repeatedly evaluates state and applies corrective actions is a proven way to prevent drift and keep systems continuously converging. citeturn0search6turn0search2

### Integration-first with OpenClaw primitives

OpenClaw already provides the necessary infrastructure-level primitives to implement “continuous operation” without rebuilding the gateway:

Cron (gateway scheduler): persistent scheduled jobs, with execution styles (main session vs isolated) and delivery options. citeturn11search1turn11search3

Heartbeat: periodic main-session agent turns designed to surface “needs attention” items without constant human prompting. citeturn11search0

Session tooling and routing: stable session keys for cron/hook contexts and deterministic routing to the right agent runtime boundary. citeturn4search0turn4search5

Therefore, the TDE should be designed as an **additive capability**: it owns governance state and decision logic, while OpenClaw continues to own scheduling, session lifecycles, routing, and tool invocation boundaries. fileciteturn0file1L3-L16 citeturn11search1turn11search0turn4search5

### Non-negotiable engineering properties (to prevent “AI drift” failures)

Idempotent, retry-safe execution: when actions can be retried (because workers crash, networks fail, or acknowledgements are missed), side effects must be safely deduplicated. This is a core principle of durable execution systems; it applies directly to agent tool invocations. fileciteturn0file2L3-L16 citeturn1search49turn0search3

Policy-as-code separation: decision rights (“what is allowed”) should be evaluated by a policy decision point rather than being scattered across imperative logic, to keep governance auditable and changeable. citeturn1search4

Telemetry-first: a multi-agent system needs traceability for debugging and governance metrics; an industry-standard approach is to instrument traces/metrics/logs via entity["organization","OpenTelemetry","observability framework"]. citeturn1search2turn1search0

Capacity control (anti-stall): the TDE must enforce WIP (work-in-progress) and queue limits as hard constraints, because uncontrolled work queues systematically produce stall and drift. fileciteturn0file0L61-L74 citeturn9search1turn9search48

## Go/no-go criteria and risks

### Go criteria for entering build phase

Proceed to build only if the definition phase produces all of the following:

A stable, reviewable architecture baseline (diagrams + contracts) with unambiguous system boundaries, and no unresolved “who owns truth” disputes for critical entities. citeturn1search3turn1search6

A complete use-case set for the thin vertical slice, with explicit decision rights and approval gating. The slice must be defined in a way that is implementable using OpenClaw cron/heartbeat/session primitives (i.e., integration-first). citeturn11search1turn11search0turn4search0

A concrete Trello retirement pathway with cutover conditions and a definition of “done” that results in Trello no longer being required for operational continuity. fileciteturn0file0L3-L13

A “drift prevention” control model: WIP limits, reconciliation loops, and a blocker/approval contract that prevents stuck items from silently accumulating. fileciteturn0file0L61-L74 citeturn0search6turn9search1

### No-go (kill) criteria

Do not proceed to build if any of the following persists at the end of the definition phase:

Core entity drift (Task/Decision/Evidence/Action semantics repeatedly change without explicit versioning or compatibility strategy). citeturn0search0

Unresolved mutation authority (it remains ambiguous which component is allowed to change which state and under what approval). citeturn1search4

Inability to specify an idempotent execution contract for side-effecting actions (meaning the system is structurally unsafe under retries). citeturn1search49turn0search3

Trello retirement remains an aspiration rather than an engineered migration (no cutover logic, no steady-state definition). fileciteturn0file0L3-L13

### Primary risks and mitigations

Scope creep: mitigated by an explicit Start Packet plus a stable definition of the thin vertical slice that serves as the “kernel.” fileciteturn0file1L3-L16

Reliability hazards from retries and partial failures: mitigated by idempotency keys and an outbox-style approach (commit state + record intended external events/actions, then publish/execute via a worker). citeturn0search3turn1search49

Incentive drift toward UI work: mitigated by requiring decision-first artifacts as the validation surface before any UI expansion. fileciteturn0file2L3-L16

## Schedule and governance

### Time window and milestones

This phase uses absolute dates (not “days” or “weeks”) and is evaluated by deliverable completion.

Planned window: **2026-03-02 through 2026-03-20**.

Milestones (acceptance is binary: delivered / not delivered):

- **2026-03-04:** Start Packet approved (goal, top decision outcomes, non-goals, success metrics, kill criteria). fileciteturn0file2L3-L16  
- **2026-03-07:** Use-case set complete, with thin-slice use case fully specified. fileciteturn0file0L18-L23  
- **2026-03-12:** Information architecture complete (canonical object model + IDs + relationships + ownership boundaries). fileciteturn0file2L3-L16  
- **2026-03-16:** Architecture baseline complete (C4-style diagrams + API/data contracts + OpenClaw integration map). citeturn1search3turn11search1turn11search0  
- **2026-03-18:** Trello retirement design complete (migration plan + cutover conditions + steady state). fileciteturn0file0L3-L13  
- **2026-03-20:** Go/no-go recommendation, including budget and risk posture for the build phase.

### Governance mechanics

Decision discipline: classify any irreversible or expensive-to-reverse design choice as “one-way door,” and require an explicit rationale and review trigger before committing, following the common one-way/two-way decision heuristic popularized by entity["company","Amazon","ecommerce and cloud company"] leadership. citeturn9search3

Flow discipline: enforce WIP limits during the definition phase itself; if too many parallel threads open, definition quality degrades (and drift returns). citeturn9search1

Direction discipline: ensure every use case is traceably linked to a high-level objective, so work selection can be objective-driven rather than inbox-driven. fileciteturn0file0L3-L13

## Evidence base

Internal analyses provided for this decision gate include:  
Job-based orchestration and use-case framework. fileciteturn0file0L1-L15  
Feasibility study and scope boundary recommendations. fileciteturn0file1L3-L16  
Best practices synthesis and architectural stance recommendations. fileciteturn0file2L3-L16  
Prior draft decision memo (v1) for reference and supersession. fileciteturn0file3L8-L12  

Primary external best-practice references supporting the architecture and governance stance include event sourcing, control-loop controllers, idempotent/retry-safe execution patterns, policy decision point design, architecture diagramming practice, and OpenClaw’s scheduling/routing primitives. citeturn0search0turn0search6turn0search3turn1search4turn1search3turn11search1turn11search0turn4search5