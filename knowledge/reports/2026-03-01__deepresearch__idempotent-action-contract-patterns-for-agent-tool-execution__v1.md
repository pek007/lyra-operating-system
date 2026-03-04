---
title: "Idempotent Action Contract Patterns for Agent Tool Execution"
date: 2026-03-01
source: deepresearch
ingest_from: "telegram attachment file_95"
tags: [external-analysis, deepresearch, idempotency, task-decision-engine]
decision_relevance: "execution safety and retry contract design"
confidence: tbd
status: archived-source
---

# Idempotent Action Contract Patterns for Agent Tool Execution

## System context and failure model

Lyra TDE is being designed as a governance layer **on top of** OpenClaw’s execution substrate, so the contract has to work with OpenClaw’s existing delivery and session mechanics rather than assuming a bespoke “exactly-once executor.” OpenClaw’s Gateway cron scheduler persists jobs on disk so schedules survive restarts, and it supports two execution styles: a **main-session** style that enqueues a system event (processed via heartbeat) and an **isolated** style that runs a dedicated agent turn in a `cron:<jobId>` session with configurable delivery (announce/webhook/none). citeturn4search0turn4search1 In isolated mode, announce delivery is explicitly *best-effort* and OpenClaw even includes a duplicate-avoidance behavior for delivery (if the run already sent a message to the same target, announce delivery is skipped). citeturn5search2

On the agent-side, your internal operating rules already imply that **execution is frequently delegated, scoped, and timeboxed**: defaulting to spawned subagents unless persistent context ownership is required, requiring a spawn contract (objective/scope/allowed tools/output format/timebox), and requiring a completion contract (outcome/artifacts changed/risks/next actions). fileciteturn6file0L1-L1 This matters because retries are far more likely when work is split across sessions, agents, and execution lanes.

Finally, your governance model explicitly includes least-privilege boundaries by role (read/write/tool scopes, approval requirements). That becomes an input to the action contract (actor identity + envelope + approval state), not an afterthought. fileciteturn9file0L1-L1

### The four failure modes your contract must deterministically handle

**Duplicate delivery** and **retries after worker crash** are the “default reality” in reliable distributed systems: if the executor crashes after performing work but before recording completion/acknowledging upstream, the same message/action can be delivered again. entity["organization","RabbitMQ","messaging broker"] documents this pattern directly: with acknowledgements you get at-least-once delivery semantics, which implies redelivery after failures and a requirement for idempotent consumers. citeturn3search3

“**Action succeeded but acknowledgement failed**” is the most important edge case for agent tool calls because tool execution and control-plane recording are not atomic across process boundaries. entity["company","Temporal","durable workflow orchestration"] community guidance highlights the same core reality: an activity can complete successfully from the worker’s perspective, but if the completion cannot be recorded (network issues, timeouts, worker crash at the wrong moment), the system can retry it—so idempotency is still required even for “atomic” business logic. citeturn0search8turn2search17

**Concurrent mutations** (two actions targeting the same logical object) must be handled as a first-class conflict mode. Practically, this requires **optimistic concurrency checks** (expected version) and/or serializable transactions with client-side retry. entity["organization","PostgreSQL","open source database"] explicitly requires applications using stricter isolation levels to be prepared to retry whole transactions on serialization failures (SQLSTATE `40001`). citeturn0search0turn0search1

These observations jointly force an architecture stance: **treat tool execution as at-least-once**, then add a governance contract and storage discipline that makes retries safe and deterministic.

## Action contract v1 specification

This section defines a practical v1 contract that you can implement in 1–2 sprints, while leaving room for v2 extensions (cross-resource sagas, richer policy evaluation, etc.).

### Contract objects: command vs event

**Command**: an intent to cause side effects (“do X”), submitted by an actor (agent/human/system) against a target. Commands must be idempotent and retry-safe.

**Event**: an immutable fact emitted by the system (“X was accepted”, “attempt 2 started”, “succeeded”, “failed with reason Y”). Events are not “re-run”; they are appended and used for audit/rebuild/diagnostics.

This distinction aligns with your internal boundary doctrine: operational state belongs in the task/decision engine rather than chat transcripts, so commands/events should be durable records rather than conversational artifacts. fileciteturn12file0L1-L1

### ActionCommand v1 (required fields)

Below is a v1 command envelope deliberately shaped to solve your deterministic requirements without requiring a heavyweight workflow engine.

**Identity and retry control**

- `action_id` (required): globally unique immutable identifier for this *logical* action (UUID/ULID).  
  *Rule:* constant across retries and duplicates.
- `idempotency_key` (required): caller-provided stable key identifying the *business operation* (not the delivery attempt).  
  *Rule:* duplicates with the same idempotency key must not create additional side effects.
- `ttl_ms` or `expires_at` (required): how long the system will attempt/replay this action before it becomes terminally expired.  
  *Rule:* used for dedupe retention and for garbage collection of in-flight state.

**Actor and governance context**

- `actor` (required object):
  - `actor_id` (required): stable ID for human/role/agent-runtime.
  - `actor_kind` (required): `human | role | agent_runtime | system`.
  - `agent_id` (optional but strongly recommended): OpenClaw agent runtime identifier when actor is an agent.
  - `session_key` (optional but strongly recommended): OpenClaw session key if the action originates in a session context (e.g., `main`, `cron:<jobId>`). OpenClaw’s session model makes session keys a stable correlation primitive across tools and delivery routes. citeturn4search3turn4search6
- `permission_envelope` (required for agent actors): name/version of the envelope that governs tool scope and approval requirements. Your repo already defines envelope expectations by role, so the action record should preserve which envelope was in effect at decision time. fileciteturn9file0L1-L1
- `approval` (optional object, but required when policy says “human gate”):
  - `required` (bool)
  - `approval_id` (string, nullable)
  - `status` (`not_required | pending | approved | rejected | expired`)
  - `expires_at` (timestamp)
  - `resume_token` (string, nullable) for resumable workflows (e.g., OpenClaw Lobster resume tokens). OpenClaw’s workflow tooling is explicitly built around “needs approval” states and resume tokens. citeturn5search0

**Target and concurrency**

- `target` (required object):
  - `target_type` (required): e.g., `task`, `decision`, `evidence_record`, `change_record`, `external_system`.
  - `target_id` (required): stable identifier.
  - `target_partition` (optional): shard key / tenant / workspace identity.
- `expected_version` (required for mutable targets): integer (or ETag) representing the version the actor believes it is modifying.  
  *Rule:* if current_version ≠ expected_version, the action must resolve deterministically as `CONFLICT` (or require an explicit conflict policy).

**Intent**

- `intent` (required object):
  - `action_type` (required): canonical action name, e.g. `task.transition`, `decision.approve`, `tool.exec`, `message.send`.
  - `params` (required): structured parameters.
  - `intent_hash` (required): hash of canonicalized `{action_type, params, target}` (computed by the engine, stored, and returned).
  - `side_effect_profile` (required enum in v1): `none | internal_only | external_idempotent | external_non_idempotent`.  
    This drives mandatory safeguards (approval requirement, reconciliation rules, etc.).

**Retry policy**

- `retry` (required object):
  - `max_attempts` (required)
  - `backoff` (required): `none | fixed | exponential_jitter`
  - `initial_delay_ms`, `max_delay_ms` (optional, based on backoff mode)

This aligns with the “cron vs heartbeat” and “workflow runtime for multi-step side effects” doctrine you already documented: heartbeat for batching awareness, cron for precise isolated runs, workflows for multi-step side effects with pause/resume. fileciteturn12file18L1-L1 citeturn4search0

### ActionEvent v1 (minimum)

You can implement v1 with a single “actions” table plus an optional event log, but it is still useful to standardize event shape from day one:

- `event_id` (ULID/UUID)
- `action_id`
- `event_type`: `accepted | duplicate_detected | attempt_started | heartbeat | waiting_approval | succeeded | failed_retryable | failed_terminal | expired | cancelled | compensated`
- `attempt`: integer (monotonic per action)
- `at`: timestamp
- `details`: structured payload (error codes, tool receipts, external ids, etc.)

### State transition rules and failure semantics

A practical v1 state machine that directly addresses your deterministic requirements:

**Core states**

- `NEW` → `ACCEPTED`  
  Created when the command is first accepted and inserted into the dedupe store (atomic).
- `ACCEPTED` → `RUNNING`  
  A worker obtains a lease and begins execution attempt *n*.
- `RUNNING` → `SUCCEEDED`  
  Tool receipts and domain updates are persisted; the action is complete.
- `RUNNING` → `WAITING_APPROVAL`  
  A human gate was triggered (e.g., OpenClaw exec approvals returns `approval-pending` + approval id; or workflow returns `needs_approval` + resume token). citeturn5search1turn5search4turn5search0
- `RUNNING` → `FAILED_RETRYABLE` → `RUNNING`  
  Transient failure; next attempt scheduled.
- `RUNNING` → `FAILED_TERMINAL`  
  Non-retryable failure (policy violation, validation error, explicit rejection).
- Any non-terminal → `EXPIRED`  
  TTL exceeded before success.

**Lease rule (prevents concurrent execution of the same action)**  
When transitioning into `RUNNING`, the worker must atomically set:

- `lease_owner` (worker id)
- `lease_expires_at`
- `attempt = attempt + 1`
- `last_heartbeat_at = now`

Only the lease owner may report completion for that attempt. Another worker may take over **only** if `lease_expires_at < now` (crash/restart scenario).

**Duplicate semantics (deterministic)**  
When a command arrives with an `idempotency_key` that already exists:

- If `intent_hash` matches the stored command: return the stored response snapshot (or an “in progress” status) without re-running side effects.
- If `intent_hash` differs: return a deterministic error (e.g., `409 IDEMPOTENCY_KEY_REUSED_WITH_DIFFERENT_INTENT`), mirroring the widely-used “idempotency key → cached response” strategy in payment-style APIs. entity["company","Stripe","payments platform"] describes exactly this approach: clients retry with the same key; the server replays the prior result; and mismatched keys imply client misuse. citeturn2search7turn0search6

**Indeterminate outcome semantics**  
If a worker crashes or network fails after the tool side effect but before completion is recorded, the engine must treat the action as `RUNNING` with an expired lease and re-attempt it. This only becomes safe if the tool call is either:
- internally idempotent (domain UPSERT / inbox ledger),
- or externally idempotent (downstream supports idempotency key),
- or protected by an explicit human gate/rollback plan.

This is the same “completed but not recorded” edge case emphasized in durable workflow systems. citeturn0search8turn2search17

## Idempotency patterns for agent tool execution

This section focuses on *engineering patterns that actually ship* under at-least-once delivery, and how they map to TDE + OpenClaw.

### Idempotency key strategies

**Caller-generated, business-stable keys (preferred for external side effects)**  
For actions like “send message”, “create ticket”, “charge card”, the most robust strategy is: caller chooses a key that represents the business operation (e.g., `task:<id>:notify:<channel>:<template>:v1`). The system stores key → response, so duplicates return the same result. citeturn2search7turn0search6

**Engine-generated keys with deterministic derivation (good for internal mutations)**  
When the action is purely internal (e.g., task state transition), you can derive idempotency from natural keys and version checks:
- unique constraint on `(target_id, action_type, expected_version)`; or
- a monotonic “transition id” per target.

This yields “idempotent by construction” behavior and reduces key-management burden.

**Composable keys for workflow/runtime integration**  
Workflow engines often compose keys from a stable workflow run id + activity/step id so retries re-use the same idempotency token. Temporal training material recommends composing an idempotency key from identifiers that are stable across retries. citeturn2search44

### Dedup storage design

In practice, you need two related but distinct stores:

**Action ledger (system of record)**  
Stores the canonical action row (command + current state + outcome). This is the authoritative answer to “did we do this?”

**Dedup index (uniqueness boundary)**  
Implemented as a unique index in the action ledger itself (simplest) or a separate table if you want different retention TTLs. The dedup key should be scoped so that it matches business meaning, not transport meaning.

A pragmatic v1 uniqueness design:

- `UNIQUE (actor_id, action_type, target_type, target_id, idempotency_key)`

This mirrors the “composite scope” approach you already identified in internal architecture work as a precedent for idempotency discipline (actor/action/subject/idempotency). fileciteturn15file1L1-L1

### Replay behavior and response caching

A robust retry-safe system returns deterministic answers when duplicates occur:

- If first attempt succeeded: replay the stored success response.
- If first attempt is still running: return `202 IN_PROGRESS` + retry-after.
- If first attempt failed terminally: replay the stored terminal failure.
- If first attempt failed retryably: return the current retry schedule (including `next_retry_at`) so callers don’t spam retries.

This is explicitly the pattern described in idempotency-key API guidance: store the response (optionally with a request hash) for a TTL (often ~24h) and replay it on duplicates. citeturn0search6turn2search7

### Exactly-once vs at-least-once tradeoffs

“Exactly-once” is typically achievable only **within a tightly controlled boundary** (single system, single region, coordinated acknowledgement semantics). Even systems that advertise “exactly-once delivery” include important caveats: Google Cloud Pub/Sub’s exactly-once delivery prevents redelivery after successful acknowledgement, but still notes that publish-side duplicates can exist in certain retry scenarios or service behaviors. citeturn1search0turn1search2

For OpenClaw + TDE, the implementable stance is:

- **Assume at-least-once delivery** for action execution and tool invocation.
- Add *effectively-once outcomes* via idempotency keys, dedupe ledgers, and version checks.
- Reserve “exactly-once” language for narrowly-defined internal sequences (e.g., “one successful state transition per target version”).

You can still borrow “exactly-once semantics” ideas from Kafka ecosystems: idempotent producers and transactional coordination are used to reduce duplicates and align state commits with message offsets, but it’s still a carefully-scoped guarantee. entity["company","Confluent","kafka platform vendor"] documentation frames exactly-once as requiring specific producer/consumer transactional configuration and highlights that consumer crashes before saving position imply possible reprocessing—hence the continued need for idempotent processing. citeturn1search6

## Reference architecture for retry-safe action execution

### Overview: where the transactional boundary must sit

You have a classic “dual write” problem: update governance state + perform external side effects. The industry-standard fix is to make the **durable write** (action + intended effects) atomic, then perform external delivery asynchronously from a durable outbox.

entity["company","Amazon Web Services","cloud provider"] prescriptive guidance describes the transactional outbox pattern as a solution to inconsistent state when a database write succeeds but an event/message send fails (or vice versa): write business state and outbox entry in the same transaction, then publish from the outbox. citeturn0search12 entity["company","Microsoft","technology company"] provides the same pattern description: store events in an outbox table first, then publish from a separate worker that marks entries processed. citeturn0search14turn0search9

### Core components

**Action API (governance entrypoint)**  
Validates policy, detects duplicates, writes the action row, and returns a deterministic response.

**Action store (ACID database)**  
Minimum schema:

- `actions` table: command fields + state + outcome + response snapshot
- `action_attempts` table (optional in v1): per-attempt receipts/errors/heartbeats
- `outbox` table (optional but strongly recommended for v1 if you have any side-effect dispatch beyond the local DB)

**Action executor(s)**  
Workers that:
- claim actions via lease,
- execute the tool call(s) (through OpenClaw tools),
- record receipts,
- transition to succeeded/failed/waiting_approval,
- schedule retries.

### Transactional boundary options (what to implement first)

**Option A: “Action row + domain state + outbox” in one DB transaction (recommended v1)**  
Inside one DB transaction:

1. Insert (or dedupe-check) `actions` row.
2. Validate `expected_version`.
3. Apply domain mutation (e.g., task transition).
4. Insert outbox record describing the required side effect(s): tool call plan, message dispatch, evidence write, etc.
5. Commit.

Then an executor reads the outbox record and performs the tool call with the action’s `idempotency_key`, recording outcome back onto the action row.

This gives deterministic handling of “state updated but message/tool execution failed” and is the cleanest fix for your “succeeded but acknowledgement failed” class inside your own boundaries. citeturn0search12turn0search14

**Option B: “Action row only” + synchronous tool execution by the caller (acceptable if you need speed)**  
This is simpler but riskier: you still write an action row first (dedupe + lease), but you let the agent perform the tool call immediately and then call back to complete the action.

You must then harden reconciliation (see below), because crash-after-side-effect-before-recording is guaranteed to happen eventually.

**Option C: “Inbox + outbox” when consuming external events (v2 or when you add brokers)**  
If actions are triggered by message/event ingestion, add an inbox (processed-message ledger) so you can dedupe at the ingestion boundary, then apply Option A internally. This is the standard “idempotent consumer” pairing with outbox. citeturn3search3turn2search10

### Optimistic concurrency and conflict handling

Use `expected_version` for all first-class mutable targets (tasks, decisions, approvals). On `apply_action`:

- Load current version of target.
- If mismatch: return `409 CONFLICT` with `{current_version, conflict_hint}`.
- Do not attempt automatic merges for high-risk actions unless the action type is explicitly commutative and policy allows.

For database-level enforcement:

- If you use serializable isolation, you **must** retry whole transactions on serialization failures; the DB cannot do it correctly for you because it cannot re-run your application logic. citeturn0search0turn0search1  
- Even with weaker isolation, unique constraints will still surface “races” in dedupe and version updates; treat them as expected and map them deterministically to either “duplicate” or “conflict.”

### Conflict resolution strategy (practical v1)

A minimal strategy that is both safe and implementable:

1. **Default: fail closed** on version mismatch (`409 CONFLICT`).  
2. If the action is a pure “write model projection” (e.g., refresh materialized summary), allow a policy-controlled “last writer wins” mode because the operation is reversible and non-destructive.
3. If the action is external and irreversible (send, publish, charge), require one of:
   - prior approval, or
   - downstream idempotency support, or
   - a compensating action plan in the action metadata (v2-friendly but can be stubbed in v1).

This complements your internal “approval card” doctrine: irreversible actions should obligate a rollback plan and explicit allowed decisions. fileciteturn12file18L1-L1 citeturn5search0turn5search1

## Pseudocode reference

The pseudocode below assumes a single database with an `actions` table that enforces uniqueness on `(actor_id, action_type, target_type, target_id, idempotency_key)` and stores a `request_hash` plus a cached `response_snapshot`.

```pseudo
function canonical_hash(command):
    // Stable JSON canonicalization then SHA-256
    return sha256(canonical_json({
        action_type: command.intent.action_type,
        params: command.intent.params,
        target: command.target,
        actor_id: command.actor.actor_id,
    }))

function detect_duplicate(tx, command):
    key = {
      actor_id: command.actor.actor_id,
      action_type: command.intent.action_type,
      target_type: command.target.target_type,
      target_id: command.target.target_id,
      idempotency_key: command.idempotency_key
    }

    row = tx.query_one("
      SELECT action_id, state, request_hash, response_snapshot, lease_expires_at
      FROM actions
      WHERE actor_id=? AND action_type=? AND target_type=? AND target_id=? AND idempotency_key=?",
      key...)

    if row is null:
        return { is_duplicate: false }

    if row.request_hash != canonical_hash(command):
        return {
          is_duplicate: true,
          kind: "IDEMPOTENCY_MISMATCH",
          error: "idempotency key reused with different intent",
          existing_action_id: row.action_id
        }

    // Same command as before
    if row.state in ["SUCCEEDED", "FAILED_TERMINAL", "CANCELLED", "EXPIRED"]:
        return {
          is_duplicate: true,
          kind: "REPLAY_FINAL",
          response: row.response_snapshot
        }

    // Still running or retryable
    return {
      is_duplicate: true,
      kind: "IN_PROGRESS",
      action_id: row.action_id,
      state: row.state,
      lease_expires_at: row.lease_expires_at
    }

function apply_action(command):
    now = clock.now()
    request_hash = canonical_hash(command)

    return db.transaction(tx =>:
        dup = detect_duplicate(tx, command)
        if dup.is_duplicate:
            return dup

        // Validate TTL
        if command.expires_at <= now:
            return { error: "EXPIRED_BEFORE_ACCEPT", status: 410 }

        // Load target for optimistic concurrency (if applicable)
        if command.expected_version != null:
            target = tx.query_one("SELECT version FROM targets WHERE id=?", command.target.target_id)
            if target.version != command.expected_version:
                return {
                  error: "CONFLICT",
                  status: 409,
                  current_version: target.version
                }

        // Insert action row (dedupe uniqueness constraint enforces race safety)
        action_id = command.action_id
        tx.execute("
          INSERT INTO actions(
            action_id, actor_id, action_type, target_type, target_id,
            idempotency_key, request_hash, state,
            attempt, lease_owner, lease_expires_at,
            created_at, updated_at, expires_at,
            command_json, response_snapshot
          ) VALUES (?, ?, ?, ?, ?, ?, ?, 'ACCEPTED', 0, NULL, NULL, ?, ?, ?, ?, NULL)",
          ...)

        // Optionally: write an outbox record for asynchronous execution
        tx.execute("
          INSERT INTO outbox(outbox_id, action_id, kind, payload_json, status, created_at)
          VALUES(?, ?, 'ACTION_EXECUTE', ?, 'PENDING', ?)",
          new_ulid(), action_id, build_execution_payload(command), now)

        return { accepted: true, action_id: action_id, state: "ACCEPTED" }
    )

function retry_action(action_id):
    now = clock.now()
    return db.transaction(tx =>:
        row = tx.query_one("SELECT state, attempt, lease_expires_at, expires_at FROM actions WHERE action_id=? FOR UPDATE", action_id)

        if row is null:
            return { error: "NOT_FOUND" }

        if row.state in ["SUCCEEDED", "FAILED_TERMINAL", "CANCELLED", "EXPIRED"]:
            return { ok: true, state: row.state } // nothing to do

        if row.expires_at <= now:
            tx.execute("UPDATE actions SET state='EXPIRED', updated_at=? WHERE action_id=?", now, action_id)
            return { ok: true, state: "EXPIRED" }

        if row.lease_expires_at != null and row.lease_expires_at > now:
            return { ok: true, state: row.state, note: "LEASE_HELD" }

        // Acquire lease + increment attempt atomically under row lock
        new_attempt = row.attempt + 1
        lease_seconds = 60
        tx.execute("
          UPDATE actions
          SET state='RUNNING',
              attempt=?,
              lease_owner=?,
              lease_expires_at=?,
              updated_at=?
          WHERE action_id=?",
          new_attempt, worker_id(), now + lease_seconds, now, action_id)

        return { ok: true, state: "RUNNING", attempt: new_attempt }
    )

function reconcile_partial_success(action_id):
    // Called when prior attempt outcome is indeterminate
    // Strategy: prefer external idempotency evidence if available, else retry under same idempotency key
    row = db.query_one("SELECT command_json, idempotency_key, external_receipt FROM actions WHERE action_id=?", action_id)

    cmd = parse(row.command_json)

    if cmd.intent.side_effect_profile == "external_idempotent":
        // Ask downstream for operation by idempotency key OR attempt same call (safe)
        result = tool_call(cmd, idempotency_key=cmd.idempotency_key)
        return record_completion(action_id, result)
    else:
        // No safe external dedupe guarantee
        // Either:
        //  - require approval before retry, or
        //  - run a compensating check, or
        //  - fail closed and escalate
        return { error: "INDETERMINATE_REQUIRES_HUMAN", status: 409 }
```

Key properties of this design:

- **Duplicate delivery** returns deterministic responses from stored snapshots.
- **Worker crash** is handled by lease expiry and retry acquisition.
- **Success-but-ack-failed** becomes safe only when side effects are either internally idempotent (DB constraint) or externally idempotent (downstream accepts the idempotency key)—otherwise you must fail closed and escalate.

## Testing and verification strategy

A v1 implementation should be testable primarily through **fault injection** and **invariants**, not just unit tests.

### Chaos and failure-case tests

Design explicit tests around the four required failure modes:

- **Crash after side effect, before completion recorded**: simulate by killing the worker between “tool call returned success” and “DB update to SUCCEEDED.” On restart, the system must either reconcile safely via idempotency key (external idempotent) or fail closed (external non-idempotent). This is the core edge case highlighted in durable workflow systems: completion recording is not atomic with external work. citeturn2search17turn0search8
- **Lost acknowledgement / timeout**: simulate network timeouts where the client does not receive the response and retries; verify the action ledger replays the prior response snapshot (success or failure) for the same idempotency key. citeturn2search7turn0search6
- **Duplicate concurrent execution attempt**: simulate two workers racing to claim the same action; verify lease acquisition prevents both from executing tool calls (or, if both execute due to a bug, dedupe prevents additional state mutation).
- **Concurrent mutation conflict**: issue two actions against the same target with the same expected_version; one must succeed, the other must deterministically return conflict. If using serializable transactions, verify your retry loop handles `40001` correctly by retrying the *entire* transaction, including decision logic. citeturn0search0turn0search1

### Property-based tests (high leverage)

Property-based tests are a good fit because idempotency is fundamentally about invariants under arbitrary retry schedules.

Core properties:

- **Idempotency property**: for any command `C`, applying `C` N times with the same idempotency key produces exactly one logical side effect and yields the same response snapshot each time.
- **Monotonicity property**: action state must move only forward in the allowed transition graph (no “SUCCEEDED → RUNNING”).
- **Lease safety property**: at most one lease holder at a time for a given action.
- **Conflict determinism property**: when expected_version mismatches, the result is always conflict (never partial apply).

### Concurrency race tests

Implement a stress harness that runs:

- multiple threads calling `apply_action` with identical commands simultaneously;
- multiple threads calling `retry_action` simultaneously;
- simulated clock skew for lease expiry edges.

The acceptance criterion is not “no errors,” but “errors are deterministic and safe” (duplicates become no-ops; conflicts are surfaced; serialization failures are retried).

## Recommendation for Lyra TDE v1 and what to defer to v2

### Minimum viable contract for Lyra TDE v1

To fit in 1–2 sprints, implement the smallest system that guarantees retry safety for internal mutations and provides a safe bridge for external side effects when idempotency is available.

**Implement in v1**

- **Action ledger + dedupe uniqueness constraint** keyed by `(actor_id, action_type, target_type, target_id, idempotency_key)`, storing `request_hash` and a cached `response_snapshot`. citeturn2search7turn0search6
- **Lease-based execution claiming** with `lease_owner` + `lease_expires_at` to prevent concurrent attempts from running side effects.
- **Optimistic concurrency** via `expected_version` on all mutable governance objects.
- **Explicit “WAITING_APPROVAL” state** with storage for:
  - OpenClaw exec approval id when host-side commands require approval (exec tool returns `approval-pending` + id). citeturn5search4turn5search1
  - workflow resume token when using resumable pipelines (OpenClaw Lobster’s `needs_approval` + `resumeToken`). citeturn5search0
- **Outbox table + dispatcher** (strongly recommended if you do *any* external “send”) so your DB commit and “intent to execute” are atomic. citeturn0search12turn0search14
- **Retry scheduler integration via OpenClaw cron**: store `next_retry_at` per action, and use one isolated cron job (or heartbeat batch) to scan and dispatch due retries. OpenClaw cron is designed for durable retries and isolated execution styles. citeturn4search0turn4search1

### What to defer to v2

Defer anything that multiplies scope across many systems or requires heavyweight coordination:

- **Cross-resource transactional sagas** (multi-target, multi-system workflows) with compensating transactions as a formal model.
- **General event sourcing** (full replayable event log as the primary store) if you can ship v1 with a materialized state table + audit events; you can always add event sourcing later.
- **Guaranteed “exactly-once” semantics across external tools**. Treat at-least-once plus idempotency keys as the baseline; reserve more complex exactly-once claims for very narrow, provable boundaries. citeturn1search0turn1search6
- **Automatic conflict resolution** beyond explicitly commutative operations.
- **Multi-region execution guarantees** (even systems that support exactly-once note regional scoping and publish-side duplicates). citeturn1search0turn1search1

The net recommendation is simple but strict: **design for at-least-once tool execution, then enforce effectively-once results via an action ledger, idempotency keys, leases, and version checks**—and treat any action that lacks idempotency guarantees as requiring either (a) approval gates or (b) explicit reconciliation/escalation. This matches both OpenClaw’s explicit separation of scheduling/execution styles and your own governance posture that high-risk side effects should be explicit, auditable, and approval-gated. citeturn4search0turn5search1 fileciteturn12file18L1-L1