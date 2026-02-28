# SOP: Agent Lifecycle Management (Jobs → Profiles → Runtime) v1

## Purpose
Define a controlled end-to-end process for evaluating, deciding, deploying, managing, and retiring agents in the Lyra OpenClaw environment.

## Core Principle
Do not start with personas. Start with:
1. **Job** (work to be done)
2. **Execution profile** (quality/tools/memory/trust/cost needs)
3. **Runtime placement** (session/sub-agent/persistent agent/separate gateway)

A new persistent agent is created only when a durable runtime boundary is required.

## Scope
Applies to all agent additions/changes/removals across OS and PX product domains.

## Lifecycle Stages

### Stage 1 — Intake & Job Trigger
Input can come from:
- new recurring responsibility
- sustained overload on existing setup
- new trust boundary / channel routing requirement
- repeated need for different tools/sandbox/model defaults

Required artifact:
- Job request in `JOB_MARKET_MODEL_V1.md` format

### Stage 2 — Evaluation
Evaluate whether need is best solved by:
- same session
- fresh session
- sub-agent
- persistent agent
- separate gateway/host

Decision criteria (score High/Medium/Low):
- durable memory/context isolation needed
- durable tool/sandbox policy differences needed
- routing/account/channel separation needed
- model default specialization needed
- trust boundary separation needed
- expected frequency and longevity
- operational overhead and cost impact

### Stage 3 — Decision
Decision outcomes:
- **Approve runtime without new persistent agent**
- **Approve new persistent agent**
- **Approve separate gateway/host** (for real trust boundary)
- **Reject/defer**

Governance:
- Peter approval required for new persistent agent and separate gateway/host
- Lyra may auto-approve session/sub-agent placement changes

### Stage 4 — Deployment
For approved persistent agents:
1. Create agent with explicit workspace/state/session boundaries
2. Configure model defaults and allowed tool/sandbox profile
3. Set routing/bindings (channel/thread/account/peer)
4. Add minimal bootstrap files (lean context)
5. Register in operational docs

Required artifacts:
- Agent profile record
- Boundary summary
- Rollback/decommission plan

### Stage 5 — Management
Monthly review per persistent agent:
- utilization and outcome quality
- cost/tokens and latency
- security posture and permission drift
- overlap/redundancy with other runtimes
- job fit vs actual assignment

### Stage 6 — Retirement
Retire when any is true:
- no longer tied to active jobs
- duplicate of existing runtime
- unnecessary cost/complexity
- security boundary no longer valid

Retirement steps:
1. unbind routing
2. migrate essential memory/artifacts
3. close active sessions safely
4. archive profile and rationale

## Guardrails
- Keep persistent agent count small by default.
- Use sub-agents for parallelism before adding persistent runtimes.
- Enforce boundaries through config (tool/sandbox/routing), not prose only.
- Long reports stay in reference docs, not auto-injected bootstrap files.

## KPI Set (monthly)
- Persistent agent count
- % jobs covered without new persistent agents
- Agent utilization rate
- Cost per agent profile
- Retirement/creation ratio
- Boundary-violation incidents

## Version
- v1.0
- Date: 2026-02-28
- Owner: Peter/Lyra
