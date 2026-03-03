# Internal Job Market Model v1

## Purpose
Manage responsibilities as **jobs** that can be assigned to the best execution surface over time. Jobs are not bound 1:1 to agents.

## Model
- One runtime can hold multiple jobs.
- One job can move between runtimes as needs change.
- Job requirements drive agent lifecycle decisions.

## Job Record Schema
- Job ID
- Job Name
- Domain (OS / PX / Shared)
- Mission and outcomes
- Decision rights
- Required execution profile:
  - quality/reasoning level
  - tools and side effects allowed
  - memory scope
  - trust boundary
  - latency/cost target
- Preferred runtime default
- Escalation triggers
- KPI/acceptance signals
- Current assignee (session/sub-agent/persistent agent/gateway)
- Review cadence

## Assignment Rules
1. Start with existing runtime + session split.
2. Use sub-agent for parallel or independent bounded runs.
3. Promote to persistent agent only for durable boundary differences.
4. Use separate gateway/host when trust boundary is materially different.

## Job Change Process
1. Propose change (new job / changed requirement / retired job)
2. Re-score execution profile
3. Re-assign runtime if needed
4. Update job record + dependencies + KPI target

Standard artifact template: `JOB_CHANGE_WORKFLOW_TEMPLATE_V1.md` (captures proposal + re-score + reassignment + dependency/KPI impact).

## Initial Job Catalog

### JOB-SEC-001 — Head of Security
- Domain: OS/PX Shared
- Mission: security posture monitoring, risk detection, hardening proposals
- Execution profile: high tool discipline, high trust sensitivity, audit trail mandatory
- Preferred runtime: main agent + isolated sub-agent runs; persistent specialist only if boundary divergence becomes durable

### JOB-ENG-001 — Software Developer
- Domain: OS/PX Shared
- Mission: implement approved work orders with verification evidence
- Execution profile: code tools, tests, bounded execution contracts, high throughput
- Preferred runtime: supplier sub-agents and/or coding workbench

### JOB-AUD-001 — Auditor
- Domain: OS/PX Shared
- Mission: independent review of decisions/changes/controls
- Execution profile: read-heavy, critique-oriented, limited side effects
- Preferred runtime: separate session or sub-agent with independent prompt profile

### JOB-ARC-001 — Chief Architect (Job, not agent)
- Domain: OS/PX Shared
- Mission: architecture constraints, boundary governance, ADR quality, sign-off recommendations
- Execution profile: high reasoning, low direct side effects, strict evidence requirements
- Preferred runtime: main agent ownership + dedicated architecture review sessions/sub-agents

### JOB-CT-001 — Head of Control Tower
- Domain: OS/PX Shared
- Mission and outcomes:
  - Keep the operating system execution loop coherent (Now/Next/Watch) and bottleneck-focused.
  - Ensure plans/tasks/decisions stay synchronized across artifacts and cadence rituals.
  - Drive throughput by selecting highest-priority executable work each cycle and capturing auditable progress.
- Decision rights:
  - Prioritize and sequence internal execution steps within approved strategy/guardrails.
  - Update operational artifacts (`TASKS.md`, process docs, evidence indexes) to maintain board integrity.
  - Trigger escalation when execution requires irreversible external action, policy change, or unresolved blocker.
- Required execution profile:
  - Quality/reasoning level: medium-high; strong synthesis across governance + delivery artifacts.
  - Tools and side effects allowed: repo-local read/write/edit, test/validation commands, evidence publication; no external comms without explicit user request.
  - Memory scope: daily continuity logs + long-term governance memory for trend tracking and carry-forward context.
  - Trust boundary: same as main runtime; heightened discipline on cross-artifact consistency.
  - Latency/cost target: frequent lightweight cycles (high cadence, low overhead per loop).
- Preferred runtime default: main session ownership with optional bounded sub-agent support for parallel evidence prep.
- Escalation triggers:
  - Competing top-priority items needing strategic trade-off.
  - Blockers requiring access/permissions beyond current runtime.
  - Any change with external/legal/financial impact.
- KPI/acceptance signals:
  - Priority-step completion rate per sprint loop.
  - % loops with auditable artifact/task-index updates.
  - Reduction in stale/duplicate task noise and board-state drift.
  - Time-to-escalation for true blockers.
- Current assignee: Main runtime (`agent=main`)
- Review cadence: weekly assignment-health review; monthly profile-fit rescore.

### JOB-CI-001 — Continuous Improvement Lead
- Domain: OS/PX Shared
- Mission and outcomes:
  - Continuously improve the operating system through small, compounding changes with evidence.
  - Systematically scan the workspace library (governance/process/docs/tools) for newly relevant gaps, drift, and missed opportunities.
  - Ensure improvement backlog execution discipline by checking open improvement tasks and nudging flow from idea to done.
- Decision rights:
  - Auto-implement low-risk, reversible improvements inside workspace guardrails.
  - Create/update improvement backlog entries in `TASKS.md` (canonical `IMP-AUTO-*` IDs) with owner, impact, and next action.
  - Escalate high-impact, controversial, or boundary-changing improvements for explicit decision.
- Required execution profile:
  - Quality/reasoning level: medium-high; synthesis across docs, tooling, and execution evidence.
  - Tools and side effects allowed: read/write/edit local artifacts, run validation scripts/tests, maintain evidence files.
  - Memory scope: recent daily notes + process/task history for trend and recurrence detection.
  - Trust boundary: same as main runtime; no automatic changes to security boundaries/credentials/external integrations/runtime permissions.
  - Latency/cost target: daily lightweight sweep with bounded implementation scope.
- Preferred runtime default: isolated daily cron sweep with reporting to Lyra Operations + main-session oversight.
- Escalation triggers:
  - Proposed change could alter security posture, access model, or external behavior.
  - Improvement requires cross-job prioritization decision due to capacity conflict.
  - Repeated backlog aging indicates structural execution bottleneck.
- KPI/acceptance signals:
  - % sweeps that produce either implemented low-risk improvements or clear backlog additions.
  - Improvement backlog execution rate (open→done cycle time for `IMP-AUTO-*`).
  - Library coverage check completion rate (docs/process/tooling reviewed on cadence).
  - Reduction in repeated drift findings over month.
- Current assignee: Daily cron job `continuous-improvement:sweep` + main runtime oversight (`agent=main`).
- Review cadence: weekly backlog execution review; monthly role-effectiveness and scope-fit review.

## Governance Cadence
- Weekly: open jobs and assignment health
- Monthly: profile fit review + consolidation opportunities
- Quarterly: job catalog refactoring and retirement

### Cadence artifacts (baseline)
- Job-to-runtime fit matrix baseline: `governance/job-runtime-fit-matrix-2026-03-03.md`
- Monthly lifecycle KPI snapshot baseline: `governance/job-lifecycle-kpi-snapshot-2026-03.md`
- Job lifecycle change artifact template: `JOB_CHANGE_WORKFLOW_TEMPLATE_V1.md`
- Evidence log for initial publish: `knowledge/evidence/2026-03-03__ops-2026-039-job-runtime-fit-matrix-initial-publish.md`

## Version
- v1.3
- Date: 2026-03-03
- Owner: Peter/Lyra
