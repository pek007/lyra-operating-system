# METRICS_WEEKLY.md

## Purpose
Weekly operational snapshot for Lyra + Peter to monitor execution quality, reliability, and improvement velocity.

## How to Use
- Update once per week (suggested: end of week)
- Keep entries short and factual
- Focus on trend and decisions, not vanity metrics

---

## Metric Definitions

- **Throughput**: Number of tasks moved to Done during the week
- **Cycle Time (median)**: Median days from Active -> Done
- **WIP (end of week)**: Number of tasks in Active at week end
- **Overdue Tasks**: Count of tasks past due date
- **Incidents**: Operational/security incidents count
- **MTTR** (Mean Time to Recovery): Average time to recover from incidents
- **Automation Wins**: Count of workflow improvements implemented

---

## Weekly Template

### Week of: YYYY-MM-DD

#### 1) Core Flow Metrics
- Throughput:
- Cycle time (median):
- WIP (end of week):
- Overdue tasks:

#### 2) Reliability & Risk
- Incidents:
- MTTR:
- Notable risks observed:

#### 3) Improvement Metrics
- Automation wins implemented:
- Process improvements implemented:
- Open improvement items (count):

#### 4) Quality Snapshot
- % outputs needing major rewrite:
- Recurring bottlenecks:
- What improved this week:

#### 5) Decisions & Actions
- Keep doing:
- Start doing:
- Stop doing:
- Top 1 priority for next week:

---

## Baseline Entry

### Week of: 2026-02-23

#### 1) Core Flow Metrics
- Throughput: Baseline week (tracking starts now)
- Cycle time (median): Baseline week
- WIP (end of week): Baseline week
- Overdue tasks: Baseline week

#### 2) Reliability & Risk
- Incidents: Telegram channel outage resolved via token rotation + pairing approval
- MTTR: Not yet measured systematically
- Notable risks observed: Credential handling hygiene (rotate exposed tokens/codes)

#### 3) Improvement Metrics
- Automation wins implemented: 1 (daily 12:00 best-practice brief cron)
- Process improvements implemented: 4 (model routing policy, OS v1 plan, intake SOP, DoD standard)
- Open improvement items (count): Track from TASKS.md starting next weekly cycle

#### 4) Quality Snapshot
- % outputs needing major rewrite: Baseline week
- Recurring bottlenecks: Missing external web-search API key for broader research
- What improved this week: Core operating framework established

#### 5) Decisions & Actions
- Keep doing: Daily incremental operating-system build
- Start doing: Weekly metrics review cadence
- Stop doing: Ad-hoc process updates without documentation
- Top 1 priority for next week: Finalize systems-of-record decision and stabilize workflow instrumentation

## Version
- v1.0
- Date: 2026-02-23
