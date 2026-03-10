# Control Panel — Decisions

## Decision CP-D1
- Context: Need a reusable, non-calendar-bound framework for product vision/goal/plan/continuous-improvement across Lyra OS portfolio.
- Decision: Adopt trigger-based `PRODUCT_WAY_OF_WORKING_PROCESS_V1.md` as mandatory structure standard.
- Trade-offs: Slight documentation overhead in exchange for clearer governance and comparability.
- Impacted artifacts/processes: Product management docs for all products; Control Panel product governance role.
- Reversal conditions: If framework adds friction without quality gains, revise required sections and simplify templates.

## Decision CP-D2
- Context: Product ownership now exists at the assembly level, while Lyra still currently operates broadly across the Lyra OS runtime. At the same time, memory spans agent, session, job, knowledge, and coordination layers and therefore needs explicit governance.
- Decision: Treat Memory as a formal horizontal process/capability owned through the Control Panel product assembly, while preserving distributed memory-content creation close to the work.
- Trade-offs: Adds explicit governance and maintenance overhead, but reduces drift, silent non-usage, continuity loss, and ambiguity about ownership.
- Impacted artifacts/processes: `MEMORY_PROCESS_V1.md`, `SITUATIONAL_AWARENESS.md`, Control Panel management artifacts, future retrieval/indexing policy, job memory standards, and memory-quality reviews.
- Reversal conditions: If product ownership and runtime ownership are later split more sharply, re-evaluate whether memory capability ownership should stay in Control Panel or move to a different platform governance product.

## Decision CP-D3
- Context: The current Lyra operating model relies too heavily on Telegram sessions/channels to hold product identity, which creates role drift, weak wake-up semantics, and manual cross-session coordination. Review of Vega / `pxs` showed stronger patterns around explicit runtime boundaries, structured handoffs, and shared-core governance.
- Decision: Adopt a hybrid runtime topology target: central Control Panel oversight runtime, selective persistent product/domain runtimes only where durable boundaries are justified, portable job memory as the continuity layer, and native cross-session communication as the default bridge.
- Trade-offs: Requires clearer runtime mapping and handoff discipline, but avoids both weak session-only identity and premature persistent-agent sprawl.
- Impacted artifacts/processes: runtime topology design, agent lifecycle decisions, heartbeat/cron execution design, job-memory portability implementation, and future cross-session coordination protocols.
- Reversal conditions: If the current session/channel model proves sufficient after stronger job memory and coordination mechanisms are implemented, or if a later architecture favors stricter per-product runtime isolation everywhere, revisit the topology choice.
