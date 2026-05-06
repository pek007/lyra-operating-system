# TDE Cockpit v0

Status: generated cockpit v0
Product: Task Management / TDE
Owner: Task Management Product Owner / Lyra
Refreshed at: manual refresh
Canonical state: `os/runtime/tde_state.sqlite`
Readable projection: `os/runtime/TASKS_from_db.md`

## 1. What needs attention now

1. **Intake acceptance gap:** 39 / 101 file intakes have exact DB intake/assignment matches; 6 historical intakes have explicit disposition; 56 remain unresolved/not exact accepted.
2. **Open task surface:** 2 DB rows are Active/Waiting/Blocked/Deferred/Escalated.
3. **Closure-required debt:** 0 meaningful `Done` rows lack structured closure/disposition evidence.
4. **Projection parity:** `match=true` for `os/runtime/TASKS_from_db.md`.

This cockpit is an operator surface, not a canonical state store.

## 2. DB task counts by status

| Value | Count |
| --- | ---: |
| `Inbox` | 14 |
| `Triage` | 0 |
| `Active` | 0 |
| `Waiting` | 2 |
| `Blocked` | 0 |
| `Deferred` | 0 |
| `Escalated` | 0 |
| `Done` | 137 |
| `done` | 0 |

## 3. Current open-status surface

| Task | Status | Updated | Note |
| --- | --- | --- | --- |
| `TDE-SELF-UI-READINESS-20260326-003` | `Waiting` | `2026-03-27T03:02:43.412299+00:00` | waiting/open task |
| `TDE-SELF-UI-READINESS-20260326-004` | `Waiting` | `2026-03-27T03:02:43.412408+00:00` | waiting/open task |

## 4. Intake acceptance surface

| Value | Count |
| --- | ---: |
| `db_accepted` | 39 |
| `assignment_accepted` | 0 |
| `dispositioned_historical` | 6 |
| `unaccepted_file_only` | 0 |
| `invalid_packet` | 52 |
| `legacy_object_not_packet` | 4 |
| `packet_unvalidated` | 0 |
| `unreadable` | 0 |

Duplicate IDs: **1**.
Exact DB intake/assignment matches: **39 / 101**.
Not exact runtime-accepted: **62 / 101**.
Explicitly dispositioned historical intakes: **6 / 101**.
Unresolved not exact accepted: **56 / 101**.

### Decision-object dispositions

Disposition source: `generated_index`.

| Value | Count |
| --- | ---: |
| `duplicate` | 0 |
| `superseded` | 3 |
| `recorded_no_action` | 3 |

### DB intake outcomes

| Value | Count |
| --- | ---: |
| `create_decision` | 7 |
| `create_work` | 36 |
| `update_existing` | 4 |

## 5. Assignment acceptance states

| Value | Count |
| --- | ---: |
| `accepted` | 3 |
| `rejected_invalid_assignment` | 1 |

## 6. Closure and evidence discipline

### Closure outcomes

| Value | Count |
| --- | ---: |
| `close_and_chain` | 4 |
| `close_and_improve` | 1 |
| `close_clean` | 30 |

### Closure-required debt

| Task | Status | Reasons |
| --- | --- | --- |
| — | — | No meaningful `Done` rows missing closure/disposition evidence. |

Lowercase `done` rows: **0**.
Tasks with closure metadata: **26**.

### Latest closure records

| Task | Outcome | State | Created |
| --- | --- | --- | --- |
| `SF-ISOLATION-20260504-001` | `close_and_chain` | `Done` | `2026-05-04T02:00:53Z` |
| `PROC-AUDIT-20260501-REVIEW-CADENCE-001` | `close_clean` | `Done` | `2026-05-03T18:17:06Z` |
| `PROC-AUDIT-20260501-EVIDENCE-LIFECYCLE-DECISION-001` | `close_and_chain` | `Done` | `2026-05-03T17:40:01Z` |
| `PROC-AUDIT-20260501-REGISTRY-INTEGRITY-001` | `close_clean` | `Done` | `2026-05-03T17:31:15Z` |
| `TDE-SELF-UI-READINESS-20260326-002` | `close_clean` | `Done` | `2026-04-29T03:01:03Z` |
| `TDE-ADOPT-STAGE2-CP-UI-RENDERING-001` | `close_clean` | `Done` | `2026-04-29T02:02:05Z` |
| `SF-ISOLATION-ATTRIBUTION-001` | `close_clean` | `Done` | `2026-04-29T00:08:00Z` |
| `TDE-ADOPT-STAGE2-CP-SURFACE-001` | `close_clean` | `Done` | `2026-04-28T03:03:49Z` |

## 7. Approval-gate and chaining signals

| Signal | Current value |
| --- | ---: |
| Tasks with `depends_on` | 5 |
| Tasks with `activation_rule` | 5 |
| Tasks with `requires_approval=true` | 0 |
| `task_activated` events | 2 |
| `job_tick_summary` events | 3 |
| `task_closed` events | 33 |

## 8. Stale/conflict warnings

| Warning | Severity | Owner action |
| --- | --- | --- |
| File-submitted ≠ runtime-accepted remains widespread. | High | Do not treat intake files as accepted TDE work unless DB state confirms it or a decision object explicitly dispositions historical state. |
| Many file packets may fail current schema. | High | Add producer adapters, explicitly disposition historical files, or intentionally evolve schema before bulk ingest. |
| `TASKS_from_db.md` is readable projection only. | Medium | Keep DB as canonical; cockpit and projection are operator surfaces. |
| Level 3 decision automation should remain envelope-bound. | Medium | Proceed only through named policy envelopes and visible approval/blocking signals. |

## 9. Current control objects

- `products/task-management/04-execution/TDE_TASK_ADOPTION_HARDENING_PLAN_2026-04-27.md`
- `products/task-management/04-execution/TDE_INTAKE_PARITY_REPORT_2026-04-27.md`
- `products/task-management/04-execution/TDE_ACTIVE_WAITING_RECONCILIATION_2026-04-27.md`
- `products/task-management/04-execution/TDE_OPEN_STATUS_DISPOSITION_BATCH_2026-04-27.md`
- `products/task-management/04-execution/TDE_APPROVAL_GATE_BEHAVIOR_VERIFICATION_2026-04-27.md`
- `products/task-management/04-execution/TDE_NEW_WORK_ADOPTION_RULE_2026-04-27.md`
- `products/task-management/04-execution/TDE_CLOSURE_DISCIPLINE_ENFORCEMENT_2026-04-27.md`
- `products/task-management/04-execution/TDE_COCKPIT_TOOLING_2026-04-27.md`
- `products/task-management/04-execution/TDE_ADOPTION_PLAN_2026-04-27.md`
- `products/task-management/04-execution/TDE_OPERATOR_ADOPTION_CHECKLIST_2026-04-27.md`
- `products/task-management/04-execution/TDE_ADOPTION_STAGE1_EXECUTION_LOG_2026-04-27.md`
- `products/task-management/04-execution/TDE_COCKPIT_V0.md`

## 10. Recommended next actions

1. Continue Stage 1 using `TDE_OPERATOR_ADOPTION_CHECKLIST_2026-04-27.md` and `TDE_ADOPTION_STAGE1_EXECUTION_LOG_2026-04-27.md` until three meaningful Lyra/TDE work cycles have clean outcomes.
2. Run this generator/check around meaningful TDE mutation batches.
3. Treat non-zero closure-required debt as a cleanup or release-readiness signal.
4. Decide the first externalized adoption path after Stage 1 evidence: Control Panel, Software Factory, or Vega/PXS.
5. Do not expand Level 3 decision automation beyond named policy-envelope pilots until intake acceptance and cockpit visibility are maintained by default.

## 11. Integrity notes

- This cockpit is generated from current DB queries and intake-file inspection.
- The authoritative state remains `os/runtime/tde_state.sqlite`; this file is a control surface for operators.
