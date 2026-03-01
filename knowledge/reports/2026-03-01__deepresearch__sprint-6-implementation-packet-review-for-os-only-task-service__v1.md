---
title: "Sprint 6 Implementation Packet Review for OS-only Task Service"
date: 2026-03-01
source: deepresearch
ingest_from: "knowledge/inbox/external-analysis-dropzone/deep-research-report (22).md"
tags: [external-analysis, deepresearch]
decision_relevance: tbd
confidence: tbd
status: archived-source
---

# Sprint 6 Implementation Packet Review for OS-only Task Service

## Executive assessment

**Conditional Go.** The packet is directionally coherent (bounded task-service, template→instance scheduling, anti-noise job-event escalation, OS-only scope, and a strict Gateway vs Control Panel boundary), but it is not yet “handoff-grade” for a 3rd-party implementation supplier because several execution-critical specs remain underspecified and the acceptance matrix is not yet testable/traceable enough to serve as a build contract. fileciteturn48file0L6-L35 fileciteturn49file0L6-L39 fileciteturn50file0L6-L37 fileciteturn52file0L6-L16

This packet also collides with at least one existing product statement: the Control Panel is explicitly described as **“Local-first, read-only”** with **“no write-back to markdown files,”** while Sprint 6 flows assume a **Task API (create)** and writes to a “Task store.” That mismatch must be resolved before execution or the supplier will improvise fundamentals (storage, mutation model, authz/audit) that you likely want to control. fileciteturn50file6L1-L3 fileciteturn50file6L255-L257 fileciteturn51file0L13-L17

Finally, your own 3PP delivery standard says a sprint is ready only when the packet is internally consistent and acceptance tests are “explicit and testable,” with traceability from requirement IDs to evidence. The current packet is not there yet. fileciteturn72file0L40-L45 fileciteturn72file0L31-L38

## Critical gaps

- **Write model vs “read-only” baseline is unresolved (must decide + document).** The Sprint 6 flow explicitly includes `UI -> Task API (create) -> Task store`, implying mutation and persistent writes. fileciteturn51file0L13-L15 At the same time, the product’s README frames the Control Panel as “read-only” and explicitly states “no write-back to markdown files.” fileciteturn50file6L1-L3 fileciteturn50file6L255-L257  
  **Why it’s must-fix:** every downstream design depends on it (storage choice, concurrency, audit logging, auth, data migrations, rollback story, test strategy).

- **Task-store / template-store / event-log are named but not specified enough to implement consistently.** The data architecture lists “Task store,” “Schedule templates,” and “Task-event ingestion log” as systems of record but does not specify storage medium, schema, versioning, invariants, or retention. fileciteturn50file0L6-L10  
  **Why it’s must-fix:** without a concrete SoR contract, “idempotency” and “deterministic generation” are untestable and different implementations will diverge. fileciteturn50file0L28-L31 fileciteturn52file0L10-L12

- **API contracts are only described as “high level,” but acceptance requires schema-correct endpoints.** Output contracts are currently just bullets (“Task query endpoints,” “Scheduled view endpoint,” etc.). fileciteturn50file0L33-L37 Yet acceptance requires endpoints to “respond with expected schema,” which is presently undefined. fileciteturn52file0L8-L10  
  **Why it’s must-fix:** absent request/response schemas, a supplier can “pass” subjectively (or build incompatible shapes), making verification and future reuse brittle.

- **OS-only enforcement is asserted but not operationalized (data-at-rest + API-level rules).** The PRD and decision log state OS-only scope and “must not contain PX domain data.” fileciteturn48file0L9-L12 fileciteturn53file0L19-L22 Acceptance criterion similarly requires “No PX data surfaced.” fileciteturn52file0L9-L10  
  **Why it’s must-fix:** the current task schema explicitly supports `domain: os|px|shared`, meaning PX-shaped data can exist in the task model today unless filtered/blocked deliberately. fileciteturn56file0L30-L33

- **Schedule template semantics are missing in the places the supplier will look first.** The packet and decisions establish template→instance and “exactly once” generation. fileciteturn49file0L16-L19 fileciteturn53file0L9-L11 Acceptance hinges on determinism and no duplicates. fileciteturn52file0L10-L11  
  **Why it’s must-fix:** you need minimally: recurrence representation, timezone rule, “generation window” definition, idempotency key definition, and conflict/late-run behavior.

- **Job-event ingestion/escalation policy is underdefined (thresholds, cool-down, dedup).** Decisions specify “events ingested” and escalation “only by policy/severity,” defaulting to noise prevention. fileciteturn53file0L13-L16 Use cases require “task created only if escalation policy threshold met.” fileciteturn49file0L21-L24 Yet no policy model is defined (what thresholds? consecutive failures? cooldown?) even though the Sprint 6 backlog explicitly calls out anti-noise controls like cool-down windows and consecutive-failure thresholds. fileciteturn48file4L26-L31  
  **Why it’s must-fix:** without explicit defaults, suppliers will invent policy logic that may flood tasks or hide real failures.

- **Backward compatibility requirement is non-actionable as written.** The matrix says “Existing critical S1–S5 routes still pass” but does not enumerate which routes, what constitutes “pass,” or whether route-level redirects are acceptable. fileciteturn52file0L16-L16  
  **Why it’s must-fix:** “regression tests” need a target list; otherwise, verification is informal and incomplete.

## Recommended edits by file

### `docs/S6_PRD_TASK_SERVICE.md` fileciteturn48file0L1-L35

- `+` Add a **“Definitions and scope guardrails”** section that hard-defines: “Task Service,” “OS-only,” “Scheduled obligation,” “Job event,” “Decision context block,” and “Gateway-derived runtime reference,” so terms like “decision-grade” and “low-noise” become implementable targets. (This directly supports the PRD problem statement.) fileciteturn48file0L6-L8
- `~` Clarify Goal 1 (“Trello retirement path”) into **Sprint-6-scoped deliverables** and **explicit non-deliverables** (e.g., “S6 outcome is X; Trello cutover is Y and measured by Z”). fileciteturn48file0L14-L18
- `+` Add a **“Mutation model”** statement: either (A) “still read-only, capture happens via X external file + ingestion” or (B) “write-enabled into store Y with audit,” explicitly reconciling PRD expectations with existing product positioning. fileciteturn51file0L13-L15 fileciteturn50file6L255-L257
- `+` Add **Success criteria → measurable checks** (e.g., “duplicate task generation rate = 0” becomes a specific acceptance test definition and measurement method). fileciteturn48file0L26-L36
- `~` Tighten Product boundary wording to specify **what “OS-only” excludes** (at minimum: any `domain=px` tasks, PX workflow areas, PX operational views), aligning with Decisions D4 and Acceptance S6‑R2. fileciteturn48file0L9-L12 fileciteturn53file0L19-L22 fileciteturn52file0L9-L10

### `docs/S6_USE_CASES.md` fileciteturn49file0L1-L39

- `~` Upgrade each UC to a **handoff-grade use case template** by adding: Preconditions, Inputs, Main flow, Alternate flows, Error cases, Postconditions, and Acceptance notes. Right now, each UC is a single outcome line, which is insufficient for deterministic implementation. fileciteturn49file0L6-L39
- `+` Add **explicit invariants per UC**, e.g.:
  - UC‑03: idempotency behavior, duplicate suppression, window definition. fileciteturn49file0L16-L19
  - UC‑04: default `record_only`, escalation thresholds, dedup keys. fileciteturn49file0L21-L24
- `+` Add an OS-only “negative UC”: **attempt to create or surface PX tasks must be rejected/filtered**, mapping directly to S6‑R2. fileciteturn52file0L9-L10
- `+` Add traceability hooks: `UC-ID`, links to `S6-R*`, and decision references `D*` so the acceptance matrix can be mechanically cross-checked. fileciteturn52file0L8-L16 fileciteturn53file0L6-L22

### `docs/S6_DATA_ARCHITECTURE.md` fileciteturn50file0L1-L37

- `+` Replace “Systems of record” bullets with a **SoR contract block per entity**: storage medium, file/path or DB, schema versioning, key fields, invariants, retention, and migration notes. fileciteturn50file0L6-L10
- `+` Add **canonical schemas** (minimal, testable) for:
  - `Task` (including origin, domain rules, scheduled/delivery WIP rules). fileciteturn50file0L12-L17
  - `ScheduleTemplate` (timezone rule, recurrence expression, idempotency key strategy). fileciteturn50file0L12-L17
  - `TaskEvent` (event ID, source job identifier, severity, dedup keys, escalation outcome). fileciteturn50file0L12-L17
- `+` Make “Gateway-derived runtime references” concrete: allowed fields, ownership label requirement, freshness timestamp requirement, and required deep-link. This aligns directly with the boundary spec’s UX handoff model. fileciteturn50file0L6-L10 fileciteturn54file0L39-L43
- `+` Add explicit **field-level SoT declarations** for any federated fields, consistent with the boundary governance rule. fileciteturn54file0L50-L54

### `docs/S6_SYSTEM_CONTEXT_AND_FLOWS.md` fileciteturn51file0L1-L31

- `+` For each flow (F1–F5), add **implementation-critical details**: idempotency boundary (where it is checked), failure handling, retries, and how “structured warnings” are emitted. fileciteturn51file0L13-L27 fileciteturn50file0L28-L31
- `+` Add an explicit **authn/authz + audit** note for any write or action endpoint (especially if “Task API (create)” is real). The boundary spec allows Control Panel to “invoke” Gateway actions only under strict conditions; task writes will need similarly explicit constraints to avoid uncontrolled mutation. fileciteturn51file0L13-L15 fileciteturn54file0L26-L29
- `~` Expand “External boundary” into enforceable “what we do / do not do,” using the approved boundary spec language (summary embed, deep link, action invoke constraints). fileciteturn51file0L29-L31 fileciteturn54file0L23-L29

### `docs/S6_ACCEPTANCE_TEST_MATRIX.md` fileciteturn52file0L1-L16

- `~` Tighten each requirement into a **testable statement**, and split combined requirements into smaller ones where needed. For example, “Task service contracts implemented” should list which endpoints/contracts are in-scope for S6. fileciteturn52file0L8-L9
- `+` Add columns for **UC coverage** and **Decision references** (e.g., S6‑R3 ↔ UC‑03 ↔ D2). fileciteturn49file0L16-L19 fileciteturn53file0L9-L11
- `+` Add explicit **negative and edge-case tests** for idempotency, noise controls, domain leakage, and gateway boundary requirements (details in the next section). fileciteturn52file0L10-L16
- `+` Replace “manual checklist” ambiguity with a named checklist artifact (or a test plan section) so a supplier can produce evidence consistently. fileciteturn72file0L31-L38

### `docs/S6_3PP_WORK_ORDER.md` fileciteturn50file1L1-L30

- `+` Add a **“Repo + execution instructions”** section: repo(s) in scope, branch name convention, how to run tests (`pnpm test`), how to run the app, and required verification artifacts. (Right now it only says “Implement Sprint 6 …” with no execution details.) fileciteturn50file1L6-L9
- `+` Add a “**Definition of Done for this work order**” that is explicitly “acceptance matrix verified + evidence,” aligning the work order with the delivery process doc’s DoD and traceability requirements. fileciteturn50file1L19-L24 fileciteturn72file0L47-L52
- `~` Strengthen “Guardrails” by referencing the canonical “Deferred / not building” list in Decisions D6 (and/or restating it succinctly). fileciteturn50file1L26-L30 fileciteturn53file0L26-L33
- `+` Add a required output: **traceability table** (Claim → Req ID → Test/Evidence → Files), consistent with your own 3PP traceability rule. fileciteturn72file0L31-L38

### `docs/DECISIONS_TASK_MGMT_S6.md` fileciteturn53file0L1-L45

- `+` For each decision D1–D8, add a short “**Implementation implications**” block with:
  - MUST/SHOULD/MAY constraints,
  - defaults (e.g., event ingestion default `record_only`), and
  - what would constitute a violation. fileciteturn53file0L13-L16 fileciteturn53file0L6-L8
- `+` Add explicit “**OS-only enforcement rule**” language that is testable (e.g., reject `domain=px` on create; filter on read) to support S6‑R2. fileciteturn53file0L19-L22 fileciteturn52file0L9-L10
- `~` Link D5 workflow invariants to acceptance tests (status model + scheduled WIP segregation), because those are already acceptance requirements. fileciteturn53file0L23-L25 fileciteturn52file0L12-L13

### `docs/GATEWAY_CONTROL_PANEL_BOUNDARY_SPEC.md` fileciteturn54file0L1-L54

- `+` Add a **“Field ownership labeling requirement”** section: any gateway-derived field must include `source_system`, `fetched_at`, and an `open_in_gateway_url` (or equivalent). This directly operationalizes the existing UX handoff model. fileciteturn54file0L39-L43
- `+` Add “**Enforcement hooks**”:
  - a linter/test checklist for any new gateway-adjacent UI surface,
  - a schema rule that requires ownership metadata on gateway-derived data. fileciteturn54file0L50-L54
- `+` Consider adding the ownership matrix as an annex or referenced normative doc, because it provides concrete “who owns what” mapping that the boundary spec is otherwise describing qualitatively. fileciteturn55file0L5-L22

### New files to add before execution

- `+ docs/S6_TASK_SERVICE_CONTRACTS.md` (or similar): minimal API/request/response schemas, error codes, idempotency contract, and versioning. This closes the biggest under-spec gap implied by “explicit contracts” and “expected schema.” fileciteturn48file0L14-L18 fileciteturn52file0L8-L10
- `+ docs/S6_TEST_PLAN.md`: named checklists for the “manual” parts and a single place to define evidence expectations (screenshots, logs, test output). This aligns with your traceability requirement. fileciteturn72file0L31-L38
- `+ docs/S6_PACKET_INDEX.md`: versioned, frozen v1.0 entrypoint for the supplier (“these are the normative docs”), reducing ambiguity and preventing “doc drift.” fileciteturn72file0L18-L24

## Missing acceptance tests and traceability improvements

Your acceptance matrix is a good skeleton, but it is currently too high-level to be a build contract: “expected schema,” “usable,” and “consistent” are not defined, and the matrix does not map to use cases or decisions. fileciteturn52file0L8-L16 fileciteturn49file0L6-L39 fileciteturn53file0L6-L25

A practical Sprint 6 upgrade is to keep S6‑R1…S6‑R9, but add (a) test case IDs and (b) explicit traceability columns: `UC-ID`, `Decision-ID`, `Test Case ID`, `Evidence`. This matches your delivery process requirement that each implementation claim must map to requirement ID and code/test evidence. fileciteturn72file0L31-L38

Key missing tests to add (focused on Sprint 6 execution, not “nice to have”):

- **Write-path determinism and safety (only if F1 is truly in-scope).**
  - *Test:* Create task via UI/API → persisted → appears in Work views; restart server → task persists.  
  - *Negative test:* invalid/missing “minimum required fields” rejected with structured error. fileciteturn49file0L6-L9 fileciteturn51file0L13-L15
  - *Traceability:* UC‑01 → S6‑R1 (+ new requirement if needed) → evidence.

- **OS-only enforcement at both read and write boundaries.**
  - *Test:* Any list/summary endpoint returns only OS-scoped tasks; no `domain=px` values are present in payloads or UI. fileciteturn52file0L9-L10
  - *Negative test:* Attempt to create task with `domain=px` rejected/blocked, and attempt to import/ingest PX tasks results in warnings + filtered output (choose one, document it).  
  - *Rationale:* current schema supports `os|px|shared`, so enforcement must be explicit. fileciteturn56file0L30-L33

- **Schedule template materialization correctness beyond “no duplicates.”**
  - *Tests:*  
    - same template + same window run twice → identical instance IDs; no duplicates. fileciteturn52file0L10-L11  
    - window overlaps (run A generates days 1–7, run B generates days 5–10) → no duplicates for overlap.  
    - timezone/DST rule explicitly tested using your chosen canonical timezone policy (even one test is better than none).  
  - *Traceability:* UC‑03 → D2 → S6‑R3. fileciteturn49file0L16-L19 fileciteturn53file0L9-L11 fileciteturn52file0L10-L11

- **Job-event ingestion anti-noise behavior (policy defaults + edge cases).**
  - *Baseline test:* Ingest event → persisted in event log; default outcome is `record_only`. fileciteturn51file0L19-L21 fileciteturn52file0L11-L12
  - *Escalation test:* Only escalates to task when explicit threshold rules are met. fileciteturn49file0L21-L24
  - *Missing from matrix today:* cool-down windows / consecutive-failure thresholds (explicitly called out as “Should” in Sprint 6 backlog). fileciteturn48file4L26-L31
  - *Dedup test:* same event ID ingested twice → no duplicate escalation side effects. fileciteturn50file0L28-L31

- **Scheduled vs delivery WIP accounting (separation is explicitly required but needs crisp definition).**
  - *Test:* Create N “scheduled” tasks due today → they appear in Scheduled view, but delivery WIP metric remains unchanged. fileciteturn52file0L12-L13
  - *Traceability:* D5 + S6‑R5. fileciteturn53file0L23-L25

- **Backward compatibility: define and test the exact “critical S1–S5 routes.”**
  - *Add to matrix:* a concrete list of endpoints and routes (API + UI) that must remain compatible. The README already enumerates key endpoints and legacy routes; use that list as the initial “critical” set. fileciteturn50file6L137-L166 fileciteturn52file0L16-L16
  - *Test:* contract tests (status code + schema) for each critical endpoint.

- **Gateway boundary contract tests (enforceable, not aspirational).**
  - *Test:* any gateway-derived field shown in CP response includes `source`, `freshness`, and “Open in Gateway” deep link metadata, matching both the acceptance matrix and boundary spec UX handoff model. fileciteturn52file0L15-L16 fileciteturn54file0L39-L43
  - *Negative test:* a gateway-owned operational surface (e.g., pairing/config admin) is not implemented in CP (validate via “do-not-build” list review gate). fileciteturn54file0L30-L37

## Risk register

**Scope note:** these are the top execution risks based on gaps between the packet’s intent (bounded service + safety + low noise) and what is currently specified/testable. fileciteturn48file0L14-L18 fileciteturn53file0L13-L16

- **Write-model ambiguity causes architecture thrash.**  
  *Trigger:* supplier interprets “Task store” as a new DB and introduces write paths that conflict with “read-only” assumptions. fileciteturn51file0L13-L15 fileciteturn50file6L255-L257  
  *Mitigation:* freeze one clear Sprint 6 decision: (A) still read-only + ingestion, or (B) controlled write-enabled store + audit/auth; reflect consistently in PRD, data architecture, flows, and acceptance.

- **OS-only boundary leaks PX data (privacy + product boundary violation).**  
  *Trigger:* domain filtering is done only in UI, or only in one endpoint, or not at all; `domain=px` still passes through. fileciteturn52file0L9-L10 fileciteturn56file0L30-L33  
  *Mitigation:* enforce at the earliest gate (ingestion/create + query layer), add explicit tests, and define what happens to “shared” domain.

- **Schedule generation edge cases undermine “deterministic, no duplicates” promise.**  
  *Trigger:* overlapping runs, late runs, timezone/DST surprises create duplicates or missing obligations. fileciteturn52file0L10-L11  
  *Mitigation:* minimally specify: window semantics, timezone rule, idempotency key composition; add overlap test coverage.

- **Job-event escalation floods the system or hides incidents.**  
  *Trigger:* default policy is unclear and supplier implements “task per run,” contradicting decision D3; or thresholds are arbitrary. fileciteturn53file0L13-L16  
  *Mitigation:* define default policy explicitly (record_only), define at least one threshold mode (e.g., consecutive failures), include cool-down windows as called out in backlog, and add dedup tests. fileciteturn48file4L26-L31

- **Gateway/Control Panel boundary drift creates duplicated control-plane surfaces.**  
  *Trigger:* CP begins to implement detailed Gateway diagnostics/actions beyond “summary + deep link.” fileciteturn54file0L10-L10 fileciteturn54file0L23-L29  
  *Mitigation:* add an “ownership declaration” gate per feature (already required by governance rule) plus contract tests requiring ownership metadata + deep links for any gateway-derived data. fileciteturn54file0L50-L54

## Final recommended packet structure

This structure is optimized for immediate Sprint 6 execution: it preserves your current packet components but adds two small “missing middle” artifacts (contracts + test plan) and an index/freeze mechanism, consistent with your 3PP delivery process. fileciteturn72file0L9-L24

**Sprint 6 Packet v1.0 (single entrypoint + frozen references)**

- `docs/S6_PACKET_INDEX.md` *(new; v1.0 freeze page)*  
  Normative doc list, version, date frozen, and “this packet supersedes all other notes” rule. fileciteturn72file0L18-L24

- `docs/S6_PRD_TASK_SERVICE.md`  
  Outcome goals, explicit scope guardrails, and reconciled mutation model. fileciteturn48file0L6-L35

- `docs/S6_USE_CASES.md`  
  Expanded handoff-grade UCs with preconditions/alt flows and traceability hooks. fileciteturn49file0L6-L39

- `docs/S6_DATA_ARCHITECTURE.md`  
  Concrete SoR definitions, entity schemas, invariants, retention, and SoT declarations. fileciteturn50file0L6-L31

- `docs/S6_SYSTEM_CONTEXT_AND_FLOWS.md`  
  Flow details including idempotency boundaries, error handling, and boundary patterns. fileciteturn51file0L13-L31

- `docs/S6_TASK_SERVICE_CONTRACTS.md` *(new)*  
  Endpoint list + request/response schemas + idempotency contract + error codes + versioning. (This converts “explicit contracts” into implementable truth.) fileciteturn48file0L14-L18

- `docs/S6_ACCEPTANCE_TEST_MATRIX.md` *(updated)*  
  Requirements refined + linked to use cases and decisions + explicit test cases/evidence expectations. fileciteturn52file0L8-L16

- `docs/S6_TEST_PLAN.md` *(new)*  
  Named manual checklists, required evidence artifacts, and how to report results, aligned with traceability rules. fileciteturn72file0L31-L38

- `docs/S6_3PP_WORK_ORDER.md` *(updated)*  
  Execution instructions + deliverable format + DoD aligned to acceptance evidence. fileciteturn50file1L19-L30

- `docs/DECISIONS_TASK_MGMT_S6.md`  
  Decision constraints with “implementation implications” addendum. fileciteturn53file0L6-L45

- `docs/GATEWAY_CONTROL_PANEL_BOUNDARY_SPEC.md`  
  Boundary policy with enforcement hooks and required ownership metadata. fileciteturn54file0L6-L54

- `docs/GATEWAY_CP_OWNERSHIP_MATRIX.md` *(recommended annex)*  
  Concrete ownership mapping that makes the boundary enforceable in reviews/tests. fileciteturn55file0L5-L22