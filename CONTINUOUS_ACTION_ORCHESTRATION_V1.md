# CONTINUOUS_ACTION_ORCHESTRATION_V1.md

Status: Active draft v1  
Owner: Peter (governance), Lyra (orchestration), Engineering role (implementation)

## Objective
Ensure Lyra/OpenClaw maintains continuous useful execution even when individual tasks are blocked.

## Core principle
A blocker blocks a task, not the system.

---

## 1) Structured blocker contract (required)

Every task in `waiting` state must include:
- `blocked_on` — one of: `human_approval | external_reply | credential | upstream_task | runtime_error | other`
- `unblock_action` — the immediate next action once unblocked
- `next_check_at` — RFC3339 timestamp for next automated follow-up
- `escalate_at` — RFC3339 timestamp for escalation
- `owner` — accountable role/agent/human

Optional:
- `blocking_ref` — approval ID, resume token, message/thread ID, or external ticket
- `max_wait_hours` — explicit wait budget

### Validity rule
A task cannot remain in `waiting` without blocker metadata.

---

## 2) Operating doctrine (hard policy)

### Heartbeat = awareness + batching
Use heartbeat for:
- periodic situation awareness
- batching low-risk checks
- detecting stalled states and generating concise nudges

### Cron = precision + isolation
Use cron for:
- exact timing requirements
- isolated recurring jobs
- jobs requiring separate model/runtime settings

### Workflow runtime (Lobster/equivalent) = multi-step pause/resume
Use deterministic workflows for:
- multi-step operations with side effects
- explicit approval pauses
- durable resume tokens

Policy rule:
No complex side-effecting flow should rely on ad-hoc chat state alone.

---

## 3) Approval-card standard (universal human gate)

Any blocked-on-human step must produce an approval card with:
- `approval_id`
- `task_id`
- `what_changes`
- `why_now`
- `risk_level`
- `rollback_plan`
- `allowed_decisions` (`approve | edit | reject`)
- `expires_at`
- `resume_path` (command/token/link)

### Resolution rules
- Expired approvals default to `rejected` unless explicitly renewed.
- Any edit response creates a new approval card version.
- Every decision must be logged in audit artifacts.

---

## 4) Sub-agent pool policy

## Topology
- Depth 0: Control Tower
- Depth 1: optional orchestrator
- Depth 2: leaf workers

Default max depth: 2.

## Concurrency budgets
- Global `maxConcurrent` configured and monitored
- Per-orchestrator max children configured
- Per-worker run timeout required

## Tool boundaries
- Orchestrators: session-management tools allowed only if needed
- Leaf workers: no spawn-management tools by default
- High-risk tools require explicit approval policy mapping

## Completion contract (mandatory)
Each worker completion must include:
- outcome summary
- artifacts changed
- risks/assumptions
- next recommended actions

---

## 5) Scheduling and delivery standards

Every scheduled job must declare:
1. execution style (`main` or `isolated`)
2. delivery mode (`announce | webhook | none`)
3. failure policy (retry/backoff/escalation)

Optional but recommended:
- exact-timing override (otherwise allow deterministic stagger)
- retention policy for run logs

Invalid job definitions are rejected at review.

---

## 6) Anti-stall automation

## Trigger conditions
Trigger anti-stall check when any condition is true:
- `waiting_count` rising for 2+ cycles while `ready_count` is low
- cron job fails N consecutive runs
- sub-agent announce/completion retry backlog exceeds threshold
- approval queue aging beyond SLA

## Automated response
1. Generate compact stall report
2. Surface top unblock actions (smallest first)
3. Open/refresh escalation task if threshold exceeded
4. Notify owner/channel based on severity policy

---

## 7) Evidence schema alignment requirement

Known risk:
Evidence producer and control panel parser may use mismatched status/field semantics.

Policy:
- Define and enforce a canonical evidence schema
- Validate at write time (producer)
- Validate at read time (consumer)
- Reject/flag incompatible artifacts with clear error reason

No production promotion if evidence ingestion and dashboard parsing are out of contract.

---

## 8) KPIs and SLO-style controls

Track weekly:
- % waiting tasks with valid blocker contract (target 100%)
- median waiting age
- unblock success rate
- approval turnaround time (p50/p95)
- cron consecutive-failure incidents
- sub-agent timeout/expiration rate
- handoff acceptance rate
- stalled-system episodes (target downtrend)

Suggested SLO seeds:
- 95% of waiting tasks have next_check_at <= 24h
- 95% of approvals resolved within defined SLA window
- 99% of critical cron jobs complete successfully per 7-day window

---

## 9) Implementation plan (4 weeks)

Week 1:
- Add blocker contract fields and validation rules
- Add waiting-state lint checks
- Add approval-card template and ID convention

Week 2:
- Enforce scheduling declaration standard (style/delivery/failure policy)
- Define sub-agent pool defaults (depth/concurrency/timeouts)
- Add completion contract validator

Week 3:
- Implement anti-stall triggers and compact stall report
- Integrate escalation task creation path
- Add dashboard counters for waiting/ready/approval aging

Week 4:
- Resolve evidence schema mismatch and add contract tests
- Run 1-week shadow monitoring
- Tune thresholds and finalize rollout

---

## 10) Done definition (v1)

v1 is complete when:
1. Waiting tasks cannot exist without blocker metadata.
2. Approval cards are generated for all human-gated actions.
3. Sub-agent pooling limits are enforced and observable.
4. Anti-stall automation runs and produces actionable output.
5. Evidence schema alignment is validated in CI and runtime.
6. KPI baseline is captured and reviewed.
