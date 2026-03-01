---
title: "Task Management Service Design Brief for a Local-First Control Panel"
date: 2026-03-01
source: deepresearch
ingest_from: "knowledge/inbox/external-analysis-dropzone/deep-research-report (19).md"
tags: [external-analysis, deepresearch]
decision_relevance: tbd
confidence: tbd
status: archived-source
---

# Task Management Service Design Brief for a Local-First Control Panel

## Executive Summary

A high-adoption task system inside a local-first control panel should optimize for three operator behaviors: fast capture, disciplined triage, and flow-based execution with decision support. Your existing control panel already has several strong foundations worth preserving: a canonical six-state workflow (`inbox → triage → active → waiting → done → archived`), a governed domain dimension (`os | px | shared`), a governed task type dimension that already distinguishes scheduled work (`delivery | scheduled | support | discovery | incident`), and a projection-oriented Task Center that computes WIP warnings and aging indicators while excluding scheduled items from delivery WIP counting. fileciteturn3file0L3-L11 fileciteturn3file0L30-L34 fileciteturn3file16L157-L181

For the next implementation phase, the highest-leverage move is to formalize tasks as a clean bounded context (service boundary) with: (a) strict domain partitioning at rest, (b) a single canonical Task model for *all* work items (kanban, scheduled obligations, and event-driven “cron outputs”), and (c) a small set of opinionated “decision UX” projections (Now/Next/Board/Role/Portfolio) rather than feature proliferation. This aligns with local-first principles: the system should remain fully usable offline with user-controlled data stored locally, even if synchronization exists later. citeturn0search3

The central product decision: **model recurring/scheduled work as templates that generate task instances**, not as “one task whose due date keeps moving.” Market-leading tools that treat recurring work as auto-generated new items (e.g., Notion repeating database templates; Trello Card Repeater; monday.com recurring automations) avoid ambiguity, preserve per-occurrence history, and map cleanly to cron-driven tasks. citeturn2search1turn2search6turn2search0 In contrast, “recurs on completion” semantics (seen in multiple ecosystems) are useful but create forecast confusion unless explicitly modeled and visualized as a different recurrence anchor. citeturn6search0turn6search3turn1search1

Your special constraints (domain separation + unified overview + scheduled tasks, including cron-generated) imply an architecture with three layers:

1. **Domain Stores (systems of record):** separate task and schedule registries per domain (`os`, `px`, and optional `shared`) to keep data strictly separated at rest.
2. **Engines:** a scheduling engine (RRULE-class recurrence) plus an event ingestion engine (cron/job outputs) that create task *instances* idempotently with provenance.
3. **Projections (read models):** portfolio and role views that can aggregate across domains without merging the underlying stores.

To keep adoption high and feature bloat low, the next phase should explicitly *not* implement: deep project hierarchies, generalized custom fields, dependency graphs, time tracking, full wiki/docs, OKRs, or a generalized automation/rules engine. This recommendation is supported both by “feature fatigue” research (more capability can reduce satisfaction/usage) and by the consistent pattern in mature task tools: most daily value comes from a narrow set of high-frequency primitives (capture, assign, status, due date, search, and a small number of views). citeturn3search8

## Benchmark Matrix

The matrix below focuses on: (a) what users touch every day, (b) what tends to become a complexity trap, and (c) how each tool models recurring/scheduled work (critical for your cron + obligations requirement).

| Tool | Core / high-frequency features in practice | Over-engineered or low-usage traps | Recurring/scheduled model signals | Key takeaway for your build |
|---|---|---|---|---|
| Asana | Task metadata and lightweight automation primitives (custom fields and rules) are positioned as key building blocks for sorting/filtering and workflow automation. citeturn5search2turn5search6 | A “config explosion” risk when teams over-invest in fields/rules without governance. (This is a common feature-fatigue failure mode, especially when each team invents its own taxonomy.) citeturn3search8turn5search6 | Recurring tasks exist and include “periodically” (anchor-to-completion) semantics, which can be valuable but ambiguous for planning if not clearly distinguished. citeturn6search0turn6search3 | Support both “calendar-anchored” and “completion-anchored” recurrence, but make the anchor explicit in the model and UX—default to calendar-anchored for obligations. citeturn6search0turn0search1 |
| ClickUp | The product centers on hierarchical organization plus task views; tasks are anchored in Lists and can inherit statuses and configuration. citeturn7search1turn7search0 | Deep hierarchy choices (Spaces/Folders/Lists) add cognitive load and governance overhead; per-container custom statuses can fragment shared understanding. citeturn7search0turn7search1 | Recurring is feature-rich: start dates, due dates, and the “On Schedule” option exist to control whether recurrence happens on close vs on schedule; future instances visibility is plan-dependent. citeturn1search1turn1search0 | Avoid a multi-level hierarchy. Keep a single board workflow per domain and a small governed vocabulary; implement recurrence as templates → instances with one or two explicit options, not a full matrix of recurrence behaviors. citeturn1search1turn3search8 |
| Jira | Strength is workflow and automation depth (scheduled triggers, JQL-based targeting, and rule-driven creation/notifications). citeturn1search2turn1search4 | Configuration gravity: workflows, fields, permissions, and automation rules can become a “full-time admin” burden. citeturn1search4turn3search8 | Scheduling is commonly implemented via “scheduled trigger runs daily + conditions + create work item,” including business-day logic patterns. citeturn1search2turn1search4 | Copy the *pattern* (schedule trigger → condition → create task), but keep it productized: provide a simple schedule registry + deterministic generator rather than a general automation rules engine. citeturn1search2turn0search1 |
| Linear | High frequency: issues, cycles (sprint-like timeboxes), and labeling/grouping for organization; cycles auto-create and roll unfinished work forward. citeturn5search0turn4search1 | Fewer built-in “traps” by design, but teams can still over-label or create too many parallel views. citeturn4search1turn3search8 | Cycles are strongly modeled as recurring timeboxes; rollovers are system behavior (unfinished work rolls over). citeturn5search0 | Strong model for “cadence” without heavy configuration. Borrow the idea of automated cadence constructs, but keep your core task workflow stable and governed. citeturn5search0turn3search1 |
| Notion | High-frequency use is database-driven task lists and lightweight personalization via templates. citeturn2search1 | The “build-your-own-tool” trap: teams spend time constructing systems rather than executing work; taxonomy diverges easily. citeturn2search1turn3search8 | Repeating database templates create new entries on a schedule (including custom schedules). citeturn2search1turn2search2 | This is the cleanest mental model for obligations: recurring template → auto-generated instance. Implement this, but with strict schema + domain partitioning. citeturn2search1turn0search3 |
| Trello | Core is the board/list/card model; global “find my work” patterns help users avoid context switching across boards. citeturn7search3turn7search4 | Power-Up sprawl and inconsistent per-board conventions can create fragmentation. citeturn7search4turn3search8 | Card Repeater makes scheduled copies; scheduled automation is also positioned in Butler examples (e.g., “add card every Monday”). citeturn2search6turn2search5 | Your unified overview should mimic Trello’s “My Work” concept: a cross-domain personal queue that does not require navigation. citeturn7search4turn0search3 |
| monday.com | High-frequency is board items + automations; recurring work is handled via automation templates that create new groups/items on schedule. citeturn2search0 | Overuse of columns + automations can create brittle “board programming” and data quality drift. citeturn2search0turn3search8 | Recurring tasks create new items rather than updating existing items (and docs emphasize instance tracking). citeturn2search0 | This is exactly the instance-based model you want for obligations and cron outputs: generate tasks as new instances with provenance and lifecycle. citeturn2search0turn0search1 |
| Todoist | High-frequency is fast capture + due dates + recurring due dates; filters are a power feature for personal workflows. citeturn0search6turn7search2 | Missing primitives (e.g., no true start dates) cause “workaround behavior” (e.g., creating extra subtasks to simulate start dates). citeturn0search4 | Recurring dates exist (including start/end phrasing) and can be “complete forever” to stop open-ended recurrence. citeturn0search4turn0search6 | Implement real “start vs due” semantics for scheduled obligations and avoid workaround-driven UX. Also, steal the idea that filters/queries are powerful—but keep them bounded and role-friendly (not a full query language). citeturn0search4turn7search2 |

## Core Feature Set Recommendation

**Must (build now, optimize for adoption):**  
A single capture surface with near-zero friction (“new task” must be possible from anywhere) plus a small governed schema: status, domain, type, owner, due (optional), and links/provenance. Your current schema and workflow already embody this direction and add domain/task_type vocabulary for cross-domain stability. fileciteturn3file0L3-L11 fileciteturn3file0L65-L87 The core experience should be: (1) capture into `inbox`, (2) mandatory triage into a clearly defined outcome, and (3) execute with strict WIP limits and visible blockers—consistent with your operating policy that treats WIP limits, triage rules, and review cadence as first-class. fileciteturn3file3L16-L29 fileciteturn3file3L128-L139 A Task Center board projection with WIP and aging warnings is already present; keep and extend it rather than replacing it. fileciteturn3file16L169-L188

For scheduled work, “scheduled” must remain a distinct type and must not silently count toward delivery WIP; that rule is already in your projection logic and should become a product invariant. fileciteturn3file16L157-L181

**Should (next increment once Must is stable):**  
A minimal write path (create, update key fields, transition status) with strict guardrails and auditing. Your platform already has an authenticated, audited control-action mechanism that validates the subject and records decisions; reusing this pattern for task mutations is lower-risk than adding ad-hoc write endpoints. fileciteturn31file2L15-L54 A schedule registry + generator for recurring obligations (template → instance) and a simple ingestion contract for cron/job outputs (event → task instance) should follow immediately after basic edits because they directly address your requirements and reduce manual overhead. citeturn2search1turn2search0turn2search6

**Nice (explicitly defer to avoid bloat):**  
General-purpose automation/rules engine (Jira-class), arbitrary custom fields (Asana-class), complex hierarchies (ClickUp-class), dependency graphs, time tracking, and OKR/goals modules. These features are where teams most often incur governance load and “feature fatigue,” and they are not required to deliver your stated decision-support outcomes. citeturn3search8turn1search4turn7search0

## Task Model Recommendation

Your current task schema is a strong baseline: it already encodes a governed status set, a governed domain enum, and a governed `task_type` enum with `scheduled` and `incident`. fileciteturn3file0L3-L11 fileciteturn3file0L30-L34 The recommendation below preserves what you have and adds the minimum structure necessary to model recurring obligations and cron/job outputs in a way that remains local-first and domain-partitionable.

**Canonical schema fields (proposed vNext, additive):**  
Keep existing fields (`id`, `title`, `status`, `priority`, `owner`, `due`, `description`, `domain`, `area`, `task_type`, `source`, `links`, `blocked_reason`, `started_at`, `completed_at`, `created_at`, `provenance`). fileciteturn3file0L65-L87 Add only:

- `origin`: `{ manual | schedule | job | import }` (explicit provenance class; do not infer from strings).  
- `template_id`: nullable; points to a schedule template when `origin=schedule`.  
- `occurrence`: nullable; an RFC3339 timestamp or `{start,end}` window indicating the scheduled occurrence this instance represents.  
- `idempotency_key`: optional but strongly recommended for non-manual origins (schedule/job/import) to guarantee “no duplicates” under retries.  
- `severity`: optional; primarily for `incident` or job-generated tasks (supports role-based triage).

This is intentionally *not* a generalized “custom fields” system; governed vocabularies are a deliberate design choice to prevent taxonomy drift (which your current code explicitly anticipates by validating/normalizing and warning on unknowns). fileciteturn3file0L20-L63 fileciteturn3file16L92-L114

**Status/workflow model:**  
Keep the canonical 6 statuses; they map cleanly to a Definition of Workflow (DoW) that supports WIP control and explicit policies, matching established Kanban guidance: define work items, started/finished points, states, WIP control, explicit policies, and a service level expectation (SLE). fileciteturn3file0L3-L11 citeturn3search1

Treat workflow configuration as “Definition-of-Workflow as data,” which is already your architecture: per-domain workflow states, WIP limits, policy text, and SLE fields in `.control-panel/workflow-config.yaml`, with schema validation and safe fallback behavior. fileciteturn10file0L7-L78 fileciteturn12file0L4-L22

**Recurring/scheduled model:**  
Use a separate **Schedule Template** entity (stored per domain) and generate Task instances. Choose an RRULE-class representation (iCalendar recurrence rules) because it is a mature standard that explicitly supports inclusion/exclusion patterns (`RRULE`, `RDATE`, `EXDATE`) and avoids ad-hoc recurrence edge cases. citeturn0search1turn0search2

Recommended schedule template fields (minimal):

- `template_id` (stable)  
- `domain` (`os|px|shared`)  
- `task_type` (usually `scheduled`, sometimes `support`)  
- `title_template` (string)  
- `rrule` + `dtstart` (+ optional `timezone`)  
- `exdate[]` (optional)  
- `default_owner` / `default_area` / `default_priority` (optional)  
- `instance_policy`: `{ create_instance | reopen_existing }` (default `create_instance`)  
- `horizon_days`: how far ahead to materialize instances (default 14)

Why instance generation is the default: multiple leading tools implement recurring work by creating new instances (Notion repeating templates, Trello Card Repeater, monday.com recurring automations), which makes late completion, auditability, and per-occurrence evidence straightforward—crucial in an operator control panel. citeturn2search1turn2search6turn2search0

**Cron/job-generated task handling:**  
Model cron outputs as events that can optionally escalate into tasks. Do not let every cron run produce a task by default; that becomes noise. Instead:

- A cron/job writes an **Event** record: `{job_id, run_id, timestamp, domain, severity, summary, evidence_link, payload_hash}`.
- The ingestion engine applies a policy: “create task only if severity ≥ threshold OR policy says human action required.”
- When a task is created, set `origin=job`, `source=cron:<job_id>`, `provenance=<run_id or log ref>`, and `idempotency_key=job_id:run_id[:finding_id]`.

This matches the pattern in your workspace routing registry example (“trigger: new-task”) and aligns with the broader control panel’s philosophy of routing and governance for operational items. fileciteturn3file8L1-L14

## Architecture Recommendation

**Treat task management as a service boundary:** yes—*as a bounded context*, not necessarily as a separately deployed microservice. The control panel is already implemented as a local API + UI that parses local workspace files. fileciteturn23file0L1-L40 A well-defined internal service boundary reduces coupling, makes domain separation enforceable, and lets you evolve storage formats without rewriting UI logic.

A practical service decomposition for your environment:

**Task Service (system of record + invariants)**  
Responsibilities: CRUD (eventually), validation, enforced vocabularies, status transitions, and idempotent creation hooks for non-manual origins. This is a natural evolution of the existing `tasksService` + `taskCenterService` approach, which already loads tasks from `TASKS.md` and produces deterministic projections. fileciteturn3file14L35-L70 fileciteturn3file16L78-L90

**Schedule Service (templates + materialization)**  
Responsibilities: store schedule templates per domain and materialize instances up to a horizon, using RRULE semantics. RRULE is explicitly designed to generate a recurrence set and handle omissions (`EXDATE`) cleanly. citeturn0search1turn0search2

**Event Ingestion Service (cron/job outputs)**  
Responsibilities: accept job/run events and create tasks only when needed; enforce idempotency; attach provenance/evidence links.

**Projection Service (read models)**  
Responsibilities: produce the Task Center board, role-based queues, and portfolio-level overview across domains, without violating domain separation at rest. Your current Task Center projection already demonstrates the pattern: load tasks + load workflow config once, apply filters, compute WIP warnings, compute aging warnings, and return a stable contract. fileciteturn3file16L78-L114 fileciteturn3file16L169-L188

**Service APIs and integration contracts (minimal set):**  
You already expose read endpoints for task-center projections and task detail. fileciteturn3file12L4-L60 For next phase, add:

- `GET /api/tasks?domain=&status=&owner=&type=&due_lte=` (queryable list; used by role/portfolio views)  
- `POST /api/tasks` (create manual task; gated behind the same safety model you use for control actions if needed)  
- `PATCH /api/tasks/:id` (status transition + key field updates; enforce DoR/DoD constraints if you choose)  
- `GET /api/schedules?domain=` and `POST /api/schedules` (manage schedule templates)  
- `POST /api/task-events` (cron/job event ingestion; creates tasks conditionally)

For write operations, the preferred option is to reuse the existing authenticated, audited “control action” mechanism (subject validation, duplication detection, and audit meta) rather than inventing a parallel, less governed write plane. fileciteturn31file2L15-L54

**Data separation model (os/px) and aggregate reporting:**  
Right now, tasks are loaded from a single `TASKS.md` path under a workspace root. fileciteturn3file14L35-L41 That is convenient but not “strict separation at rest.” For strict separation while enabling unified overview:

- Store tasks per domain in separate files/directories (e.g., `domains/os/TASKS.*`, `domains/px/TASKS.*`, optional `domains/shared/TASKS.*`).  
- Store workflow config per domain (or as one file containing three domain entries, which you already support via `workflows[]` with domain selection and fallback). fileciteturn10file0L93-L105  
- Build a portfolio projection that reads all domain stores and aggregates counts/alerts. The portfolio view is a read model; it does not merge stores.

This design preserves the local-first principle that users own and control their data locally and can keep sensitive domains separated, while still enabling cross-domain projections. citeturn0search3

## UX Best Practices

The UX should be built around information hierarchy and review loops, not around “feature completeness.”

**Information hierarchy (recommended):**  
A three-tier “overview → filter → detail” pattern is already explicitly described as a density strategy in your sprint brief and implemented in the Task Center UI (board + filter bar + detail drawer). fileciteturn3file6L10-L16 fileciteturn3file10L106-L133 Extend the same pattern to scheduled obligations and job-generated items:

- Portfolio Overview: counts by domain and by “attention required” buckets (WIP exceeded, overdue scheduled, aging active/waiting).  
- Domain Board (Task Center): flow view with WIP and aging warnings. fileciteturn3file16L169-L188  
- Detail Drawer: show provenance, links, and last-occurrence/evidence for scheduled/job-origin tasks. fileciteturn3file0L65-L87

**Daily/weekly review patterns (make them first-class):**  
Your operating task policy already specifies daily checks (Active WIP and blockers) and weekly triage/refinement. fileciteturn3file3L128-L139 The system should directly support these routines with purpose-built views:

- Daily “Now”: Active + Waiting with blockers, plus overdue scheduled instances due today/this week.  
- Weekly “Triage”: Inbox/Triage with forced aging indicators (e.g., “inbox older than 7 days”), consistent with your SLA intent. fileciteturn3file3L47-L54  
- Weekly “Scheduled”: upcoming obligations (next 14 days) grouped by domain, showing “missed last occurrence” explicitly.

**Anti-bloat principles (hard rules):**  
Feature bloat measurably increases the risk of reduced satisfaction and adoption (“feature fatigue”); this is not theoretical—there is published research showing consumers can be less satisfied with products that have too many features. citeturn3search8 Translate that into product rules:

- Governed vocabularies over arbitrary fields (you already do this for `domain` and `task_type`). fileciteturn3file0L30-L34  
- A small fixed set of “blessed” views (Board, Triage, Scheduled, Portfolio, Role). Avoid “views as a platform.”  
- Scheduled tasks must be visible but not allowed to drown the board: keep separate counting semantics and default filtering. fileciteturn3file16L157-L181  
- Prefer links over attachments; prefer provenance references over embedded logs (keeps the task object lean and auditable). fileciteturn3file0L65-L87

## Implementation Guidance for next 1–2 sprints

The guiding principle for the next two sprints: **change the minimum surface area needed to unlock daily use**, while respecting your current architectural guardrails (read-first safety, deterministic projections, and schema validation). fileciteturn3file6L64-L71 fileciteturn10file0L32-L78

**Sprint 1 (foundation + one “killer loop”): domain-separated stores + schedule templates + instance materialization**  
Deliverables:

- Introduce per-domain storage layout (tasks + schedules). Keep the existing loader working, but add domain-aware loading so the portfolio view can read multiple stores without mixing data at rest. (This is the minimum to satisfy “strict separation + unified overview.”) fileciteturn3file14L35-L41  
- Implement Schedule Template registry and instance generator using RRULE semantics with a 14-day horizon and idempotency keys (template_id + occurrence timestamp). citeturn0search1turn2search1  
- Add a “Scheduled” view in the UI: upcoming instances grouped by domain, plus missed/overdue highlighting. Align semantics to the existing distinction that scheduled items are separate from delivery WIP. fileciteturn3file16L169-L181  
- Tests: idempotent generation, EXDATE handling, domain partitioning invariants, and projection stability.

Why this sprint is “high adoption”: recurring obligations are universally painful when handled manually, and multiple leading systems center recurring work around “generate the next instance” patterns. citeturn2search1turn2search6turn2search0

**Sprint 2 (actionability without bloat): minimal write path + cron/job ingestion**  
Deliverables:

- Add a minimal, governed write path for: create task, move status, set owner/priority/due/domain/area/type, and add links/provenance. Keep it constrained. Use the existing audited control-action pattern if you want an approval gate or duplication detection. fileciteturn31file2L15-L54  
- Implement Event Ingestion endpoint/contract for cron/job outputs + policy-driven escalation to tasks (with idempotency). This closes the loop for “cron-generated tasks.” fileciteturn3file8L1-L14  
- Extend role-based views to use explicit fields over keyword heuristics where possible. Today, role summaries scan tasks (and other registries) and build decision queues/actionables; upgrading task classification improves UX and reduces misrouting. fileciteturn35file0L20-L63 fileciteturn35file0L103-L136  
- Add a portfolio overview widget that lists: WIP violations, aging warnings, and upcoming scheduled obligations by domain. (Your projection code already computes WIP and aging warnings—reuse it.) fileciteturn3file16L169-L188

Explicitly deferred in these two sprints: generalized automation rules engine (Jira-style scheduled triggers + arbitrary conditions), arbitrary custom fields, dependencies, time tracking, and deep hierarchies. citeturn1search4turn5search2turn7search0turn3search8

## Risks and Mitigations

A lean task system fails more often from governance/UX issues than from missing features. The sections below focus on the most common failure modes for your environment (local-first + multi-domain + scheduled + cron).

**Governance and taxonomy drift (high likelihood if not addressed):**  
Risk: domain/area semantics drift, role views become unreliable, and cross-domain reporting becomes meaningless. This is already recognized as a risk (“taxonomy confusion”) in your architecture brief. fileciteturn3file6L103-L110  
Mitigation: keep governed vocabularies (domain, task_type) and make `area` domain-configured and validated (warn on unknown but do not hard-fail). Your current projection already warns on unknown areas and still includes tasks. fileciteturn3file16L103-L114

**Noise explosion from scheduled and cron-generated items (high impact on adoption):**  
Risk: the system becomes a “firehose,” users stop trusting it, and scheduled work crowds out delivery work. Multiple tools address this by separating recurrence handling and views; your system already distinguishes scheduled vs delivery in WIP counting, which should be enforced as a product invariant. fileciteturn3file16L157-L181  
Mitigation: instance-materialization horizon (e.g., 14 days), severity gating for cron-to-task escalation, and a dedicated Scheduled view that defaults to “what needs attention,” not “everything that exists.” citeturn2search0turn0search1

**Feature bloat and low adoption (medium-to-high likelihood if scope expands):**  
Risk: you rebuild a “mini enterprise PM tool” and lose the decision-support focus. Empirical research on feature fatigue supports the idea that more features can reduce satisfaction, especially without clear governance. citeturn3search8  
Mitigation: a written “Not Building” list (custom fields platform, generalized rules engine, dependencies, time tracking) and a strict “one new concept requires removing another” product rule.

**Data quality and auditability gaps (high impact in a control panel):**  
Risk: missing owners, unclear outcomes, no evidence links, and inconsistent DoD/DoR degrade trust. Your operating policy already defines DoR/DoD and evidence expectations. fileciteturn3file3L57-L83 fileciteturn3file3L87-L103  
Mitigation: enforce lightweight required fields at transition time (e.g., cannot move to `active` without `owner`; cannot move to `done` without `provenance`/evidence link). This aligns with your policy and keeps enforcement localized to transitions rather than making capture expensive. fileciteturn3file3L57-L71

**Cross-domain overview violating “strict separation” (architectural integrity risk):**  
Risk: a portfolio view accidentally becomes a merged store (harder to secure, harder to reason about).  
Mitigation: enforce separation at rest (separate stores per domain) and implement the overview strictly as a projection/read model. This mirrors your existing architecture pattern: parse sources → serve JSON projections. fileciteturn23file0L1-L40 citeturn0search3

**Recurring edge cases (timezones, exceptions, duplicates) (medium likelihood, high annoyance):**  
Risk: missed obligations, duplicate instances, or incorrect schedules around daylight savings.  
Mitigation: use RRULE/DTSTART + timezone explicitly (RFC-defined semantics) and track idempotency keys; support EXDATE for exceptions. citeturn0search1turn0search2