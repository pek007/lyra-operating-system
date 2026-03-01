---
title: "Sprint 6 Review of Task Service Design for a Local‑First Control Panel"
date: 2026-03-01
source: deepresearch
ingest_from: "knowledge/inbox/external-analysis-dropzone/deep-research-report (21).md"
tags: [external-analysis, deepresearch]
decision_relevance: tbd
confidence: tbd
status: archived-source
---

# Sprint 6 Review of Task Service Design for a Local‑First Control Panel

## Executive recommendation

Proceed with the proposed direction—**a bounded Task Management service inside Control Panel (not a separate deployable microservice) with strict domain separation and projection-only cross-domain views**—and tighten it into an implementable “two-sprint” shape by making one architectural choice explicit:

**Preferred direction:** implement **three domain stores (`os`, `px`, optional `shared`) + one unified read model**, where **all escalation (schedule materialization + job/cron ingestion) writes only into the domain stores**, and **all cross-domain/Executive views are projections constrained to *read-only aggregation***. This directly matches the approved Sprint 6 decisions around bounded task service, template→instance recurrence, policy-gated job escalation, and strict at-rest separation. fileciteturn2file2 fileciteturn2file7

Why this is the right call for a 1–2 sprint horizon:

- It keeps the scope **“contract-first” and modular** (bounded service + clear endpoints) without the operational drag of microservices. That aligns with how DDD (domain-driven design) uses bounded contexts to avoid one giant inconsistent model. fileciteturn2file7 citeturn0search0  
- It makes “local-first” real at the data layer: users “own the data” locally; the system should work offline, degrade gracefully, and remain usable even without cloud services. citeturn0search3  
- It operationalizes your anti-noise intent: **events are cheap; tasks are expensive**. Create tasks only when human action is needed, using explicit escalation policy and idempotency. fileciteturn2file2 citeturn2search8 citeturn1search2  

One pragmatic refinement I recommend you adopt as a Sprint 6 “guardrail”:

**Make the Task Service the canonical escalation sink, but do not make Control Panel a second ops console.** Treat Gateway as runtime SoT, and Control Panel as decision SoT; embed only summaries + freshness + deep links for Gateway-derived signals. This is already codified in the boundary spec and should be enforced at schema and UI review time. fileciteturn20file4turn20file0turn20file2

## Benchmark-informed design principles

The following principles synthesize the proposed Sprint 6 direction with external best practice benchmarks (local-first systems, evolvable contracts, event/alert noise suppression, and Trello-class workflow ergonomics).

**Local-first means “user-owned data” and “offline writes,” not “local read-only forever.”** Control Panel’s product vision already frames “read-first where possible; controlled write surfaces where needed.” In local-first thinking, the client should stay useful without a network and preserve long-term access and control. fileciteturn63file0 citeturn0search3  
Practical implication for Sprint 6: even if the UI remains mostly read-first, your service contracts must assume **offline-first writes by automation** (schedule materialization, job ingestion), completed with idempotency and auditability.

**Bounded contexts are your leverage point for speed.** A bounded context exists to keep models internally consistent and to make the seams explicit when integration is needed. For Sprint 6, the “Task Service” boundary is the right seam—especially because you’re integrating three kinds of input: human tasks, recurrence, and runtime/job events. citeturn0search0 fileciteturn2file2  

**Do strict domain separation at rest, then aggregate via read models only.** Your Sprint 6 decision D4 is directionally correct: cross-domain “portfolio” views should be projections, not a blended write model. fileciteturn2file2  
This mirrors a common data scoping practice: each domain owns its model; aggregation happens downstream. citeturn0search10  

**Contract evolution must follow tolerant reading (and open-world enums) to avoid brittle local workspaces.** In heterogeneous local files and long-lived data, schema drift is guaranteed. The “tolerant reader” pattern recommends: ignore fields you don’t understand and make minimal assumptions about structures to preserve forward/backward compatibility. citeturn7search3  
Control Panel already embodies this in the Task schema by normalizing statuses, treating governed enums as optional, and dropping unknown enum values while still loading tasks. fileciteturn2file0

**Events are logs; tasks are tickets; only some tickets deserve to exist.** Google’s SRE guidance distinguishes monitoring outputs: alerts (immediate action), tickets (eventual action), and logs (no action). Humans should not be forced to interpret raw noise; software should. citeturn2search8  
Sprint 6’s “ingest job outputs as events; escalate by policy/severity” is exactly the right posture for cron/job handling—*if* you implement strong gating and deduplication. fileciteturn2file2

**Do not hand-roll event formats: adopt a standard envelope.** CloudEvents exists specifically because event producers otherwise force consumers to relearn metadata and routing per source. Use CloudEvents-style metadata for task-event ingestion, even if you store it locally. citeturn6search1turn6search2  

**Idempotency is non-negotiable anywhere retries exist.** Stripe’s documentation is a clean articulation of the principle: if a request is retried (timeouts, reconnects), an idempotency key is required to prevent duplicate side effects. Apply the same approach to schedule materialization and event-to-task escalation. citeturn1search2 fileciteturn2file7  

**Trello replacement is about fast capture + triage flow + filtering, not feature abundance.** Trello’s baseline ergonomics: add cards quickly, move them through lists, filter by member/label/due date, and use basic checklist/attachments when needed. citeturn8search0turn5search1turn5search6  
Sprint 6 should replicate the high-frequency parts of that loop (capture → triage → move → close) and explicitly defer “power-up creep.”

## Proposed contracts and schemas

These contracts are intentionally “Sprint 6 practical”: small enough to implement quickly, but opinionated enough to prevent later architectural debt. Where possible, they align with Control Panel’s existing workflow statuses and governed enums. fileciteturn2file2turn2file0

### Task model contract

Control Panel already uses a canonical status workflow and domain/type enums. Keep those, and add only the minimum additional structure needed for schedule/job provenance and SoT clarity. fileciteturn2file2turn2file0

```ts
// Stable enums (already present)
type TaskStatus = "inbox" | "triage" | "active" | "waiting" | "done" | "archived";
type TaskDomain = "os" | "px" | "shared";
type TaskType = "delivery" | "scheduled" | "support" | "discovery" | "incident";

// Opinionated provenance (new, replaces free-form "provenance" over time)
type TaskOrigin = "manual" | "schedule" | "job" | "import";

type ExternalRef =
  | { kind: "gateway_run"; id: string }
  | { kind: "gateway_job";  id: string }
  | { kind: "url";          url: string; label?: string }
  | { kind: "doc_path";     path: string };

interface Task {
  schema_version: "1.0.0";
  id: string;                 // stable; never reuse
  title: string;
  status: TaskStatus;

  domain: TaskDomain;         // REQUIRED once domain stores exist
  task_type: TaskType;        // REQUIRED for WIP accounting

  area?: string;              // runtime-validated against workflow-config.yaml per domain
  priority?: "p0"|"p1"|"p2"|"p3";  // prefer strict; tolerate legacy strings in readers
  owner?: string;             // keep string in S6; move to actor IDs later if needed

  created_at: string;         // RFC3339
  updated_at?: string;
  started_at?: string;
  due_at?: string;
  completed_at?: string;
  blocked_reason?: string;

  origin: {
    kind: TaskOrigin;
    idempotency_key?: string;     // REQUIRED when kind != manual
    source?: string;              // e.g. "schedule:<id>", "job:<name>", "import:trello"
    triggered_by_event_id?: string;
  };

  links?: ExternalRef[];       // unify "links" into typed references over time
}
```

Key invariants to enforce in Sprint 6 service logic:

- **`domain` must match the store** it lives in (hard fail at write-time; warning at read-time for legacy). fileciteturn2file2  
- **Scheduled tasks must not silently count toward delivery WIP** (you already do this exclusion at projection time; keep it). fileciteturn2file18  
- **Non-manual origins require idempotency** (already a guardrail in Sprint 6 brief). fileciteturn2file7  

### Schedule template contract

Recurring work is notoriously subtle (exceptions, timezones, daylight savings, skip dates). The iCalendar recurrence model shows how complex recurrence can become once you support full RRULE + EXDATE semantics. Sprint 6 should **support a minimal subset** and keep “exceptions” explicit (skip dates), not magical. citeturn3search2 fileciteturn2file2

```ts
type ScheduleKind = "cron5" | "rrule"; // keep small; pick one as default
type ScheduleState = "active" | "paused" | "archived";

interface ScheduleTemplate {
  schema_version: "1.0.0";
  id: string;

  domain: TaskDomain;
  state: ScheduleState;

  title_template: string;      // e.g. "Monthly backup verification"
  description_template?: string;

  schedule: {
    kind: ScheduleKind;
    expression: string;        // cron5 or RRULE string
    timezone: string;          // IANA TZ (e.g., "Europe/Stockholm")
    start_at: string;          // first eligible occurrence, RFC3339
    end_at?: string;           // optional stop
    skip_dates?: string[];     // YYYY-MM-DD (explicit exceptions)
  };

  task_defaults: {
    task_type: "scheduled";
    area?: string;
    owner?: string;
    priority?: "p0"|"p1"|"p2"|"p3";
    due_offset_days?: number;  // due date relative to occurrence
  };

  materialization: {
    horizon_days: number;      // e.g. 14 or 30
    max_open_instances: number;// anti-spam guardrail
  };

  // Deterministic instance identity
  instance_key_strategy: "template+date" | "template+datetime";
}
```

Materialization rule (opinionated and important): **create at most one open instance per occurrence, per domain**, and refuse to generate more if `max_open_instances` is exceeded (forcing humans to handle backlog rather than generating infinite debt). This directly supports “noise prevention is the default.” fileciteturn2file2  

### Task-event ingestion contract

For job/cron outputs, you already have a strong “job artifact” contract with `generated_at`, `freshness.stale_after`, `input_fingerprint`, and `run_metadata`—plus a capped run-log. This is an excellent foundation for event ingestion and dedup. fileciteturn62file0turn28file2  

Adopt a CloudEvents-style envelope for ingestion to avoid inventing metadata fields and to keep routing/versioning sane. citeturn6search1

```ts
type TaskEventSeverity = "debug"|"info"|"warning"|"error"|"critical";
type TaskEventType = "job.run" | "job.stale" | "schedule.materialized";

interface TaskEvent {
  // CloudEvents-style envelope
  specversion: "1.0";
  id: string;                  // event UUID
  source: string;              // e.g. "control-panel.jobs", "openclaw.gateway"
  type: TaskEventType;
  time: string;                // RFC3339
  subject?: string;            // e.g. job name, schedule id
  datacontenttype?: "application/json";

  // Task routing hints
  domain?: TaskDomain;
  severity: TaskEventSeverity;

  // Dedup + correlation (policy engine depends on this)
  dedup_key: string;           // stable correlation key, e.g. "job:risk-audit-daily"
  idempotency_key: string;     // stable per logical delivery attempt/window

  data: {
    job_name?: string;
    run_status?: "success"|"error";
    duration_ms?: number;
    input_fingerprint?: string;
    artifact_path?: string;
    stale_after?: string;
    error_message?: string;

    // Optional: minimal emissions for policy evaluation
    counters?: Record<string, number>;
    labels?: Record<string, string>;
  };
}
```

Policy contract (minimal but explicit): **event ingestion returns “accepted + decision”** so producers can see when/why escalation happened.

```ts
interface TaskEventIngestResponse {
  accepted: boolean;
  decision: "ignored" | "recorded_only" | "task_created" | "task_updated";
  task_id?: string;
  reason?: string;
}
```

This mirrors a proven pattern from incident/event tooling: accept all events, but only create actionable artifacts when rules say so. PagerDuty explicitly highlights dedup keys and suppression as the mechanism for noise control. citeturn1search0turn1search5  

### Cross-domain portfolio projection contract

Portfolio is a read model only: it can aggregate, but it must not become a covert cross-domain write surface. fileciteturn2file2turn2file7

Use one contract that serves Executive/Work “portfolio summary” needs:

```ts
interface PortfolioTasksSummary {
  schema_version: "1.0.0";
  generated_at: string;

  totals: {
    by_status: Record<TaskStatus, number>;
    by_domain: Record<TaskDomain, { total: number; active: number; blocked: number }>;
  };

  wip: {
    delivery_wip_by_domain: Record<TaskDomain, number>;
    wip_limit_by_domain?: Record<TaskDomain, number>;
    wip_warnings?: Array<{ domain: TaskDomain; actual: number; limit: number }>;
  };

  freshness: {
    // For local-first: "freshness" is about input sources, not server health
    by_source: Array<{ source: string; coverage: "full"|"partial"|"none"; stale?: boolean }>;
  };

  // Optional: ownership declarations for federated fields
  ownership?: Array<{ field: string; source: "gateway"|"control-panel" }>;
}
```

Implementation note: Control Panel already computes WIP warnings and aging warnings in its board projection logic; reuse that approach and simply extend it to “multi-store input.” fileciteturn2file18  

## Must/Should/Nice for Sprint 6

This section answers two things at once: (a) what you need to retire Trello in practice, and (b) what not to build so Sprint 6 doesn’t turn into a stealth “project management platform.”

### Must

**Task Service maturity**
- Ship the bounded Task Service as a coherent module with contracts and guardrails, explicitly *not* as a separately deployed runtime unit in Sprint 6. fileciteturn2file2turn2file7  
- Preserve the canonical workflow states `inbox → triage → active → waiting → done → archived` end-to-end (schemas, projections, UI). fileciteturn2file2turn2file0  

**Strict domain separation**
- Implement strict at-rest separation (`os`, `px`, optional `shared`) for tasks and schedules, and make portfolio aggregation projection-only. fileciteturn2file2turn2file7  

**Recurring/scheduled**
- Implement template→instance recurrence with deterministic materialization and idempotency (no duplicates; safe reruns). fileciteturn2file2turn2file7  
- Keep scheduled work visually and metrically distinct from delivery WIP (already modeled in board projection logic; keep it and make it multi-store). fileciteturn2file18  

**Cron/job events**
- Implement event ingestion (`POST /api/task-events`) with explicit policy-gated escalation and strong dedup/idempotency (default “record, don’t escalate”). fileciteturn2file2turn2file7  
- Base ingestion on your existing job artifact/run-log conventions (`input_fingerprint`, `freshness.stale_after`, run status), so “stale/missed runs” can be detected without inventing a second job telemetry format. fileciteturn62file0turn28file2  

**Practical Trello replacement loop**
- Provide a **fast inbox capture path** and **triage clarity**. If you are not building full write UI, ship an explicit “capture” mechanism (CLI, file snippet generator, or a tiny audited write endpoint) so the daily loop doesn’t regress from Trello’s “Add card → Enter.” citeturn8search0 fileciteturn63file0  
- Work surface must have a **usable Kanban view** and a **Scheduled view** that answers “what’s due, what’s repeating, what’s overdue.” fileciteturn2file7turn34file0  

### Should

- Implement cross-domain portfolio summary as a first-class endpoint (projection only), because “Executive/Plans” needs aggregate visibility to stay decision-grade. fileciteturn2file7turn63file0  
- Add “decision-context blocks” on task details: why it matters, owner, impact, next action (this is in your Sprint 6 brief and is crucial for adoption). fileciteturn2file7turn6file0  
- Add Trello retirement readiness checks that are measurable (e.g., “daily capture occurs in CP/task system ≥80% of days this sprint”; “weekly triage SLA met”). This matches the Sprint 6 backlog intent to make retirement measurable. fileciteturn6file3  

### Nice

- Calendar-style presentation for scheduled instances (view only) akin to Trello Calendar view—useful, but only after the underlying schedule contract is stable. citeturn8search1  
- Light analytics (cycle time, aging distributions) once data integrity is solid (Sprint 6 backlog already classifies this as “nice”). fileciteturn6file3  

### Explicit “do not build” list for Sprint 6

These are either bloat multipliers or boundary violations. Several are already explicitly deferred in Sprint 6 decisions and the Gateway↔Control Panel boundary spec; treat them as “PR cannot merge without justification.” fileciteturn2file2turn20file4turn43file0  

**Do not build (product bloat)**
- Generalized custom-field platform. fileciteturn2file2  
- Generalized automation/rules engine (beyond the minimal event escalation policy needed for cron/job noise control). fileciteturn2file2  
- Dependency graph engine. fileciteturn2file2  
- Broad time-tracking suite. fileciteturn2file2  
- Deep hierarchy model (space/folder/project nesting). fileciteturn2file2  

**Do not build (Gateway duplication)**
- Any competing “authoritative ops” UI for pairing, tokens/devices, provider/channel configuration, approvals execution queue, or gateway config editing inside Control Panel. fileciteturn20file4turn20file2  

## Gateway vs Control Panel ownership implications for Sprint 6

Sprint 6 should treat “ownership” as a **schema-level constraint**, not a philosophical statement, because drift here is how “decision cockpit” becomes “second ops dashboard.”

Your boundary spec and ownership matrix already establish the correct SoT split:

- Gateway is canonical for runtime/control-plane state (health, runs/sessions, pairing/trust, provider mechanics, execution state). Control Panel may summarize but must deep-link for details. fileciteturn20file4turn20file0  
- Control Panel is canonical for decision artifacts (priorities, blockers, rationale, governance posture, work portfolio narrative). fileciteturn20file4turn20file0turn63file0  

Sprint 6 implications for the **task** surface:

- **Tasks are Control Panel SoT** (even if tasks are created from Gateway-derived events). If a task references a Gateway run, store that as an external reference, not as an embedded “copied runtime record.” fileciteturn20file4turn20file0  
- **Gateway-derived facts shown on tasks must be labeled and freshness-stamped** (“last updated”, “source: Gateway”), and must deep-link to Gateway for the operational record. This is explicitly required by the de-dup backlog. fileciteturn20file2turn20file4  

Sprint 6 implications for the **capabilities** surface:

- Treat “capabilities” as two layers:
  - **Declared/owned catalog** (agents/skills/tools, governance policies): Control Panel SoT. fileciteturn20file0turn63file0  
  - **Runtime availability/status**: Gateway SoT. Control Panel shows summary counts + health + “Open in Gateway.” fileciteturn20file0turn20file4  
- For “federated” areas, implement field-level ownership (`source: gateway|control-panel`) in response schemas, as your Sprint 6 de-dup backlog recommends. fileciteturn20file2turn20file0  

Most important: add ownership labels (`gateway-owned`, `cp-owned`, `federated`) and freshness badges to every Gateway-derived widget in Sprint 6; this is low cost and prevents UI drift. fileciteturn20file2  

## Rollout plan for two sprint slices

### Slice one

**Goal:** ship the Task Service foundation that creates “decision-quality work visibility” and enables Trello retirement *without* sliding into platform bloat.

- Implement domain stores (`os`, `px`, optional `shared`) and migrate current single-source task loading into a “multi-input, single projection” model. This directly delivers D4 and enables portfolio projections without cross-domain write blending. fileciteturn2file2turn2file7  
- Implement schedule templates + deterministic materialization into domain task stores, with strict idempotency keys derived from `(template_id, occurrence, domain)`. fileciteturn2file7turn2file2  
- Implement `POST /api/task-events` using a CloudEvents-style envelope, backed by a minimal policy engine that defaults to “record only.” fileciteturn2file7turn2file2 citeturn6search1  
- Ship Work surface improvements: Kanban + Scheduled views + task detail “decision context blocks.” fileciteturn2file7turn6file3  
- Enforce Gateway boundary requirements: freshness badges + deep links + ownership labels for any Gateway-derived cards/widgets. fileciteturn20file2turn20file4  

### Slice two

**Goal:** harden anti-noise, governance, and adoption mechanics so the system stays useful under real cron/event volume.

- Add richer escalation policy primitives: consecutive-failure thresholds, cool-down windows, and auto-resolution rules (close incident tasks when health returns). citeturn2search1turn1search0  
- Add portfolio projection contract hardening: SemVer + tolerant reader discipline; make any new fields optional and keep schema evolution non-breaking. citeturn7search7turn7search3  
- Expand Trello retirement readiness checks with real metrics and a cutover rule; do not declare retirement until capture + triage + scheduled obligations are functioning end-to-end. fileciteturn6file3turn5search0  

## Risks, mitigations, and acceptance checks

The top failure modes below are the ones most likely to derail adoption or create long-term architectural drag. The acceptance checks are written as “testable truths,” not vibes.

| Failure mode | What it looks like | Mitigation pattern | Acceptance checks |
|---|---|---|---|
| Domain leakage | `os` and `px` tasks appear mixed in source stores, not just projections | Enforce domain-at-rest separation; reject writes to wrong store; projection-only aggregation | Multi-store tests prove no cross-domain writes; portfolio endpoint is read-only and traces source store |
| Cron/job spam creates task floods | Every job run becomes a task; users stop trusting Work view | SRE-style: events are logs; tasks are tickets; enforce dedup + suppression + thresholds + cool-downs citeturn2search8turn1search0 | “Task per run” is impossible by default; repeated failures correlate into one incident; daily task creation volume bounded per job |
| Flapping creates churn | “error/success/error/success” generates repeated escalations | Require minimum-duration persistence / consecutive failures before escalation (anti-flap) citeturn2search1 | Flapping test stream escalates at most once per cool-down window |
| Duplicate scheduled instances | Materialization reruns create duplicates, especially around timezone edge cases | Deterministic instance IDs + idempotency keys (template + occurrence + domain) fileciteturn2file7turn62file0 citeturn1search2 | Re-running materialization does not change open instance count; duplicates are impossible by contract |
| UX: Work becomes “busy” not “decisive” | Too many fields, unclear priorities; scheduled work pollutes delivery focus | Keep overview→filter→detail; exclude scheduled from delivery WIP; add decision-context blocks fileciteturn2file2turn2file18 | Work view answers: “what is active?”, “what is blocked?”, “what is due?” within 60 seconds |
| Gateway boundary drift | Control Panel grows duplicate operational screens | Enforce ownership labels + deep links + freshness badges; PR checklist requires ownership declaration fileciteturn20file2turn20file4 | No CP page presents itself as authoritative for gateway-owned capabilities |
| Security: local data exposure | Sensitive workspace data readable by other users/processes | Enforce local file perms for state/data dirs; keep fail-closed redaction patterns | Workspace/state dirs are locked down; security review items stay green; no secrets ever exposed by default UI surfaces fileciteturn20file7turn63file1 |
| Process drift: inbox/triage pile-up | Tasks accumulate; WIP limits ignored; Work becomes a graveyard | Encode workflow policy indicators (WIP warnings, inbox aging) and make them visible | WIP warnings rendered; inbox aging flagged; weekly review metrics tracked per policy fileciteturn2file18turn2file3 |

Two especially important acceptance checks to add early:

- **Noise acceptance:** “A healthy daily cron schedule produces *zero* new tasks by default.” (Events may be recorded; tasks should not.) fileciteturn2file2  
- **Boundary acceptance:** “Every Gateway-derived section has `source + freshness + Open in Gateway`.” fileciteturn20file2turn20file4