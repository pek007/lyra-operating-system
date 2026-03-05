# COORDINATION_EVENT_WORKBOARD_SPEC_V1

## 1) Decision

Adopt a **coordination event stream + projected workboard** pattern.

- Canonical state for cross-session WIP coordination: append-only coordination events
- Human-readable surface: generated `WORKBOARD.md`
- `WORKBOARD.md` is a **projection**, never a source of truth

This is intended to reduce duplicate work and cross-job blind spots without collapsing session/context isolation.

## 2) Scope

In scope:
- Cross-job/session status signaling (`status`, `blocker`, `request`, `handoff`, `impact_notice`)
- Lightweight machine-usable metadata for filtering and retrieval
- TTL and compaction rules for bounded size

Out of scope:
- Replacing job-local state (`jobs/<JOB-ID>/STATE.md`, task artifacts, decisions)
- Sensitive detail sharing in common artifacts
- Shared prompt/context windows

## 3) Canonical Event Contract (v0)

Event type: `coord_status`

Required fields:
- `event_id` (string; unique)
- `at` (RFC3339 timestamp)
- `job_id` (string; use `shared` only when no single job owner)
- `session_key` (string)
- `actor` (object)
  - `agent_id` (string)
  - `subagent_id` (string, optional)
- `kind` (enum)
  - `status` | `blocker` | `request` | `handoff` | `impact_notice`
- `summary` (string; max 400 chars)
- `refs` (array of strings; optional task IDs/decision IDs/file paths)
- `ttl_days` (int; default 7)
- `safety` (object)
  - `non_sensitive` (bool; must be `true` for shared visibility)

Optional fields:
- `supersedes_event_id` (string)
- `idempotency_key` (string; required for periodic/tick writers)

## 4) Write Rules

1. Append-only: no in-place edits or deletes.
2. State-transition writes only:
   - start/intent change
   - blocked/unblocked
   - explicit request to another job
   - handoff/completion
3. Idempotency:
   - periodic writers MUST set `idempotency_key`
   - repeated writes with same key are no-ops
4. Sensitivity gate:
   - shared events require `safety.non_sensitive=true`
   - sensitive details remain in job-local artifacts; coordination event carries redacted summary + reference

## 5) Projection Contract (`WORKBOARD.md`)

Generated artifact path: `governance/WORKBOARD.md`

Generation mode:
- deterministic from current coordination events
- regenerate on schedule or after qualifying events

Projection sections:
1. **Current Active Intents (by job)**
   - latest non-expired `status`/`handoff` summary
2. **Open Blockers**
   - latest unresolved `blocker` events
3. **Open Cross-Job Requests**
   - `request` events not superseded/closed
4. **Recent Notable Events**
   - bounded list of latest blocker/request/impact_notice

Projection limits:
- max items/section (default 20)
- drop expired events (`at + ttl_days`)
- never include sensitive payloads

## 6) Activation Path

`WORKBOARD.md` classification: **retrieval module** (not kernel injection).

Activation rules:
- Control Tower heartbeat checks only blocker/request sections.
- Job tick writers emit coordination events after meaningful state transitions.
- Retrieval is on-demand via memory search/indexing; avoid unconditional loading.

## 7) Storage and Concurrency

Preferred backend: SQLite event store (WAL mode) aligned with existing TDE state store patterns.

Requirements:
- transactional append
- idempotency ledger support
- stable ordering (`at`, insertion order)

Fallback (temporary): JSONL append log + file lock + periodic compaction.

## 8) Governance and Guardrails

- `WORKBOARD.md` is non-authoritative by policy.
- Authoritative artifacts remain:
  - job `STATE.md`
  - task/decision records
  - approved governance/process documents
- Any policy/principle change discovered through board events still requires normal governance decision flow.

## 9) Metrics (v0)

Track weekly:
- Duplicate-work rate
- Cross-job blocker acknowledgment latency
- Workboard staleness (% jobs with no fresh status > threshold)
- Coordination noise ratio (events per completed unit)

Success condition: lower duplicate work and blocker latency without increased leakage/noise.

## 10) Rollout Plan

Phase A (low-risk):
1. Define event schema + writer helper.
2. Emit events from one or two jobs only.
3. Generate `governance/WORKBOARD.md`.

Phase B:
4. Add idempotency enforcement for periodic writers.
5. Add retrieval/index path.
6. Add weekly metric review and tuning.

Phase C:
7. Extend to all active jobs after 2 clean review cycles.

## 11) Explicit Non-Goals

- No free-form “everyone edits one board” workflow.
- No broad shared memory bypassing session isolation.
- No sensitive information centralization in coordination artifacts.
