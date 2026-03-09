# TDE chaining — real workflow wiring

Date: 2026-03-09
Status: Applied

## Purpose
Apply the bounded TDE chaining pilot capability to real non-demo product workflows in canonical DB state.

## Real workflows wired

### 1. Continuous Improvement chain
Workflow:
- `OPS-2026-045` — Shift Continuous Improvement leverage discovery cadence from monthly to weekly and formalize Deep Research handoff workflow
- `OPS-2026-046` — Implement Opportunity-to-Execution Engine v1 bootstrap from Deep Research report
- `OPS-2026-047` — Execute Drift Aftercare pilot (`OPP-2026-001`) and decide scale/rollback

Applied metadata:
- `OPS-2026-046`
  - depends on `OPS-2026-045`
  - `activation_rule=all_predecessors_done`
  - `stage_id=bootstrap`
  - pilot enabled (`family=pilot-a`)
- `OPS-2026-047`
  - depends on `OPS-2026-046`
  - `activation_rule=all_predecessors_done`
  - `stage_id=pilot-execution`
  - pilot enabled (`family=pilot-a`)

### 2. Security remediation / disposition chain
Workflow:
- `SEC-AUTO-20260309-02` — Restore deterministic non-elevated PF posture evidence / approved fallback proof path
- `SEC-AUTO-20260309-01` — Resolve or formally re-accept the recurring trust-model warning using updated evidence and reopen triggers

Applied metadata:
- `SEC-AUTO-20260309-01`
  - depends on `SEC-AUTO-20260309-02`
  - `activation_rule=all_predecessors_done`
  - `stage_id=risk-disposition`
  - pilot enabled (`family=pilot-a`)

## Operational meaning
These tasks are now wired so that once the predecessor is completed in canonical DB state, the successor becomes eligible for automatic promotion on the next scheduled TDE tick.

## Projection
Updated runtime projection:
- `os/runtime/TASKS_from_db.md`

## Note
This wiring does not force execution immediately. It prepares real product workflows to use the bounded chaining mechanism under the current pilot gate.
