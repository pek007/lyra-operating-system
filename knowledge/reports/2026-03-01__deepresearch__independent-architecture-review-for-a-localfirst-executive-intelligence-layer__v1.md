---
title: "Independent Architecture Review for a Local‑First Executive Intelligence Layer"
date: 2026-03-01
source: deepresearch
ingest_from: "knowledge/inbox/external-analysis-dropzone/deep-research-report (16).md"
tags: [external-analysis, deepresearch]
decision_relevance: tbd
confidence: tbd
status: archived-source
---

# Independent Architecture Review for a Local‑First Executive Intelligence Layer

## Architecture validity for read‑first executive intelligence

Your current direction—treating canonical markdown/JSON as the baseline read source while adding a panel‑owned, append‑only action/audit log—remains the right structural move for a read‑first “executive intelligence” layer, **provided you keep strict traceability and don’t blur “summary” with “source of truth.”** The Sprint 2 architecture brief explicitly separates the read model (registry parsing) from the write model (control actions) and recommends a panel‑owned action log instead of writing back into the registries, mainly for safety, auditability, and lower coupling. fileciteturn8file3L1-L120

### What’s already architecturally “on the rails”
The platform has three ingredients that executive intelligence depends on:

1. **A structured read substrate** (markdown tables + registries) plus parsing warnings. Tasks (`TASKS.md`) and risks (`RISK_REGISTER.md`) are loaded from markdown and validated, with non‑fatal warnings emitted when rows don’t validate. fileciteturn45file0L1-L80 fileciteturn47file0L1-L80  
2. **A controlled action layer with auditability by default.** The control action API requires auth and returns a stable envelope with `data/warnings/errors/meta`; it emits audit events for both allow and deny decisions. fileciteturn23file0L1-L110 fileciteturn25file0L1-L180  
3. **Role summaries already behave like an “intelligence projection.”** The role summary service loads tasks, risks, evidence, and registries once, computes KPIs and queues, and includes `meta` with schema version, generation timestamp, and workspace revision. fileciteturn38file0L1-L120

This is important because executive intelligence is mostly a **higher‑level projection** over the same ingredients: capabilities, costs, “what has been done,” plans/priorities, risks/safety posture, and daily status/blockers.

### What needs tightening for executive intelligence (enterprise → solution → system → data → security/UX)

**Enterprise / operating model fit.** Your artifacts already encode an operating model: decisions are “role‑laned,” work is explicit in `TASKS.md`, risk is explicit in `RISK_REGISTER.md`, and evidence exists as time‑stamped records plus a “latest security audit” JSON. fileciteturn38file0L1-L200 fileciteturn51file0L1-L120  
Executive intelligence should therefore be framed as: **“decision‑grade rollups with drill‑downs that preserve accountability.”** The failure mode is producing an executive view that *sounds authoritative* but can’t be traced back to concrete artifacts.

**Solution architecture.** A single “Executive Summary” endpoint is feasible in one sprint if it is:
- purely read‑first (no side effects),
- a composition over existing services (`tasksService`, `riskService`, `kpiService`, `gitService`, the audit DB),
- and exposes quality signals (freshness + confidence) alongside the narrative.

Preferred choice (one sprint): **one endpoint, one schema, many sections.**  
Implement `GET /api/executive/summary` returning the six Sprint 4 questions as sections, rather than six endpoints. This keeps cross‑section consistency (freshness, confidence, redaction) and reduces UI complexity.

**System design.** You already have a workable service shape: `buildRoleSummary()` loads all underlying sources once, then computes derived structures. fileciteturn38file0L1-L120  
Mirror this with `buildExecutiveSummary()` that calls:
- `loadTasks()` and optionally `getBoardProjection()` for blockers/WIP/aging, fileciteturn45file3L1-L220  
- `loadRisks()` and security summary for risk posture, fileciteturn47file0L1-L80 fileciteturn51file0L60-L120  
- `loadRegistries()` for subscriptions/process/agents (capabilities proxy), fileciteturn49file0L1-L120  
- `loadChanges()` + audit events for “what has been done,” fileciteturn53file0L1-L80 fileciteturn23file0L1-L110  
- KPI functions where a numeric signal is defensible (but avoid precision theater). fileciteturn42file0L1-L220

**Data architecture.** The audit log is currently SQLite with WAL enabled; the schema includes a monotonically increasing `sequence`, a constrained `decision` field, and a constrained `reconciliation_state` set. fileciteturn27file0L1-L80  
That is a good foundation for executive “what happened” reporting because it gives you a durable, queryable event trail (also aligned with common log management guidance from entity["organization","National Institute of Standards and Technology","us standards body"]). citeturn0search0turn0search5

**Security and UX.** Sprint 2 release notes explicitly call out authenticated action routes and localhost binding. fileciteturn8file0L1-L30  
Executive intelligence, however, is usually *more sensitive than role dashboards* because it aggregates “the whole story.” That means you need explicit redaction rules and safe defaults (see Security guidance section).

## Top risks

| Risk | Failure mode | Impact | Likelihood | Mitigation (one‑sprint practical) |
|---|---|---|---|---|
| Over‑confident summaries | Executive layer states “cost is $X” or “risk posture is OK” when underlying data is missing, stale, or parsed heuristically (e.g., substring matching for finance tasks; regex cost parsing). fileciteturn38file0L60-L170 fileciteturn42file0L70-L140 | Bad executive decisions; loss of trust in the control panel | High | Add **confidence + freshness** to every section; surface data coverage (e.g., “% subscriptions with parseable cost”); degrade to ranges and “unknown” instead of forcing numbers. fileciteturn42file0L70-L140 citeturn1search3turn1search6 |
| Redaction failure on executive surfaces | Aggregated views leak credentials, internal paths, or sensitive evidence details (especially via freeform metadata fields and security audit JSON). fileciteturn25file0L80-L140 fileciteturn51file0L60-L120 | Confidentiality breach; “exec view” becomes the easiest exfiltration target | Medium‑High | Introduce a **denylist + allowlist** for what can appear in executive output; treat evidence bodies as “redacted by default”; follow entity["organization","OWASP","web security nonprofit"] logging guidance on excluding sensitive data. citeturn0search1turn0search7 |
| Inconsistent contract semantics | Some endpoints put `meta` at top level; others embed it inside `data` (role summary). This complicates composability and makes UI error handling inconsistent. fileciteturn23file0L1-L110 fileciteturn38file0L20-L80 fileciteturn37file0L1-L60 | UI/clients become brittle; hard to add confidence/freshness consistently | High | Standardize: always return `{data,warnings,errors,meta}` for executive surfaces and for any new “intelligence” endpoints; keep `meta` sibling to `data` everywhere. fileciteturn23file0L1-L110 |
| Audit log durability/operability gaps | SQLite WAL grows unbounded; no retention/rollover; no alerting if logging fails; executive layer relies on logs that silently stop. fileciteturn27file0L1-L80 | Blind spots in “what happened”; compromised audit trail | Medium | Add: (a) log DB size watermark warnings, (b) “last event timestamp” health, (c) documented retention policy and optional export. This aligns with log management and audit failure considerations in NIST guidance. citeturn0search0turn0search4 |
| Status scoring becomes gameable | Teams optimize for the metric (“close tasks fast,” “relabel risks”) rather than outcomes; scoring drifts into vanity. fileciteturn45file3L120-L220 fileciteturn42file0L150-L240 | Executive dashboard induces perverse incentives | Medium | Use **transparent, factor‑based scoring** with immutable or high‑friction inputs (age, WIP overages, open high risks, days since audit), and show the top drivers. Borrow the “dashboard + budgets” discipline from entity["company","Google","technology company"] SRE thinking (explainable error budgets). citeturn0search6 |

## Summary contract design recommendations

You already have a strong precedent on the action routes: response envelope with `data`, `meta`, `warnings`, and `errors`. fileciteturn23file0L1-L110  
Your executive surfaces should **standardize** on this envelope and extend it to include **confidence** and **freshness** as first‑class concepts because executive readers are uniquely harmed by silent uncertainty.

### Preferred contract (one sprint, minimal disruption)
Use:

- `data`: the executive summary sections
- `warnings`: non‑fatal degradations (missing files, parse failures, staleness, redactions applied)
- `errors`: fatal (cannot compute anything actionable)
- `meta`: global generation + quality context (schema, timestamps, revision, freshness, confidence)

Concrete recommendation (shape):

- `meta.schema_version`: string
- `meta.generated_at`: RFC3339/ISO timestamp (already used) fileciteturn23file0L40-L80
- `meta.workspace_revision`: git short SHA (already used in role summaries) fileciteturn38file0L40-L80 fileciteturn53file0L40-L80
- `meta.freshness`:
  - `overall`: `{ tier: "fresh"|"stale"|"unknown", max_age_seconds, explanation }`
  - `sources`: per source `{ seen_at, source_revision, stale_after_seconds, status }`
- `meta.confidence`:
  - `overall`: `0..1`
  - `by_section`: `{capabilities:…, costs:…, done:…, plans:…, risks:…, status:…}`
  - `drivers`: list of why confidence is lower (e.g., “30% subscriptions missing parseable cost”)
- `meta.redaction`:
  - `policy_version`
  - `fields_redacted_count`
  - `examples`: a few safe placeholders like `"evidence.body"` (never the sensitive raw)

### Warnings and errors should be structured, not strings
Today, some services already surface parsing warnings as strings (e.g., invalid markdown table rows). fileciteturn45file0L35-L80  
For executive intelligence, I’d formalize warnings/errors minimally:

- `{code, message, scope, severity, evidence_ref?}`

Where `scope` could be `"SUBSCRIPTION_REGISTER"`, `"TASKS"`, `"SECURITY_AUDIT"`, `"AUDIT_DB"`, and `evidence_ref` links to a subject id (task/risk/subscription).

### Contract consistency fix you should make now
Role summary route currently returns `{data,warnings,errors}` and embeds `meta` inside `data`. fileciteturn36file1L1-L40 fileciteturn38file0L40-L80  
Control actions return `meta` as a top‑level sibling. fileciteturn23file0L40-L80  
For executive intelligence, pick one: **top‑level `meta`** is the better long‑term bet because it makes composition simpler across endpoints and doesn’t force clients to drill into `data` to manage caching, staleness, or schema versioning.

## Cost and activity telemetry quality guidance

Your current finance KPI implementation parses costs from a string field using a regex and sums “monthly cost” across active subscriptions, then emits a dollar‑prefixed string like `"$123.45"`. fileciteturn42file0L70-L140  
This is a perfectly reasonable Sprint 2 MVP move—but it is exactly where executive dashboards tend to drift into **false precision**.

### Cost telemetry: what to do in one sprint
Preferred decision: **show “decision‑grade cost,” not “accounting‑grade cost.”**

Concretely:

1. **Round and bucket by default.**  
   If you only have string costs, show:
   - `total_recurring_estimate`: `"$450/mo (≈)"` rounded to nearest 10/50
   - `coverage`: `% of active subs with parseable cost`
   - `unknown_cost_items`: count + top 5 list for cleanup  
   This “coverage + rounding” pattern preserves trust.

2. **Split recurring vs variable vs unknown.**  
   Even if you can’t model variable usage, label it explicitly as “not captured.” This aligns with standard FinOps expectations that cost data quality and allocation matter for trustworthy reporting. citeturn1search3turn1search6

3. **Introduce “allocation readiness” as an executive metric.**  
   Borrowing from FinOps practices: track simple quality indicators like “% allocatable spend” / “% tagged/attributed,” because executives can act on *data quality gaps* faster than they can on ambiguous totals. citeturn1search6turn1search8

4. **Avoid pretending renewal dates are always reliable.**  
   Your role decision queue logic already treats renewal as optional and ignores placeholders. fileciteturn38file0L80-L150  
   Executive cost views should similarly show “renewal completeness” and default to “unknown” when parsing fails.

### Activity telemetry: executive‑grade without vanity metrics
You have two credible “activity” sources:

- **Git history as “change evidence”** (`git log`, revision) fileciteturn53file0L1-L80  
- **Action audit trail as “controlled ops activity”** (append‑only DB events with `sequence` and `timestamp`) fileciteturn27file0L1-L80 fileciteturn25file0L1-L180

Guidance:
- Treat git commits as **weak evidence** of progress (“something changed”), not a completion signal.
- Treat completed tasks + closed risks + executed control actions as **stronger evidence**, but still show the evidence path (task IDs, risk IDs, action sequences).

Also: don’t optimize for “count of actions.” That encourages noise. Use **bounded, meaningful activity**: “actions taken on high‑severity risks,” “blocked tasks unblocked,” “renewals reviewed.”

## Security and redaction guidance for executive surfaces

Executive intelligence is an aggregation layer; aggregation changes the threat model because it becomes a single “high‑value scroll.”

### Redaction rules: strong defaults
Use entity["organization","OWASP","web security nonprofit"] logging guidance as your baseline: do not log or expose secrets, tokens, credentials, sensitive personal data, payment details, or higher‑classification data than the sink can protect; prefer masking/pseudonymization where identity isn’t required. citeturn0search1turn0search8

In your context, the highest‑risk fields are:
- `metadata` inside audit events (it is freeform JSON today) fileciteturn25file0L80-L140  
- security audit JSON payloads and any embedded evidence bodies fileciteturn51file0L1-L120

One‑sprint practical guardrail:
- Define `metadata_allowlist_keys` per `action_type`, and strip everything else at write time (not display time).
- Cap metadata size (bytes) and depth.
- For executive summary, expose only:
  - counts by class,
  - top IDs/titles (if safe),
  - and links to local drill‑downs that are more strictly permissioned.

### Audit log integrity and failure handling
You already enforce append‑only semantics at the application level and store events in SQLite with WAL mode. fileciteturn27file0L1-L80  
From a log‑management perspective (NIST guidance), the missing layer is operational: detection and handling when logging degrades or stops. citeturn0search0turn0search4

One sprint adds:
- `audit_log_health` block in executive meta:
  - `last_event_at`
  - `db_size_bytes`
  - `writable` (can write a test transaction? careful—read‑first surfaces should not write; just check file stats)
  - warning thresholds (“approaching capacity”) consistent with audit failure guidance. citeturn0search4

### Authentication expectations for executive endpoints
Control actions require authentication middleware. fileciteturn23file0L1-L40  
Role summaries currently do not show auth enforcement at the route layer. fileciteturn36file1L1-L40  
Executive intelligence should be treated closer to “action‑grade sensitivity” than “public dashboard” sensitivity. **Recommend: require auth for executive endpoints even if the system is local‑first**, because “local” often becomes “screen‑shared,” “demoed,” or “forwarded.”

## Executive status scoring design

This must be **transparent, explainable, and hard to game**—which means: deterministic rules, limited inputs, and a “show your work” breakdown.

### Preferred approach: factor score + explicit drivers
Build a score from 5–7 factors, each with an explicit threshold table. Example:

- **Risk posture (weight 30%)**  
  Inputs: `open_high_risks`, `open_critical_risks` from risk parsing. fileciteturn47file0L1-L80  
  Rule: any open critical → red; else if ≥3 open high → amber/red.

- **Safety evidence (weight 20%)**  
  Inputs: `days_since_audit`, `open_findings` via security KPI logic. fileciteturn42file0L1-L90  
  Rule: “no audit date” → red (unknown treated as unsafe).

- **Execution flow (weight 20%)**  
  Inputs: WIP warnings + aging warnings (SLE target) from task center projection. fileciteturn45file3L120-L220  
  Rule: if any column exceeds WIP limit → amber/red; if aging warnings exist → amber.

- **Plan integrity (weight 15%)**  
  Inputs: `triage` backlog size, blocked tasks count. fileciteturn45file0L1-L80  
  Rule: too much triage or blocked → amber/red.

- **Cost control (weight 15%)**  
  Inputs: recurring subscription total *with coverage*, upcoming renewals, and “unknown cost count.” fileciteturn42file0L70-L140  
  Rule: if cost coverage < X% → amber (data quality signal); if renewals within 30 days > N → amber.

### Non‑gamability tactics (practical)
- **Use aging and WIP, not “tasks touched.”** WIP/aging penalize cosmetic movement. fileciteturn45file3L120-L220  
- **Use immutable or high‑friction signals** (open high risks; days since audit) rather than self‑reported statuses. fileciteturn47file0L1-L80 fileciteturn42file0L1-L90  
- **Publish the scoring rubric in the UI.** Executives trust what they can audit.

If you want an analogy that executives intuitively accept, use the “budget” idea: Google SRE uses error budgets and dashboards to communicate reliability status and trend without pretending to be perfectly precise. citeturn0search6

## Must/Should/Nice adjustments before implementation

### Must
Unblockers that make Sprint 4 feasible without quality collapse:

1. **Standardize the executive response envelope** to `{data,warnings,errors,meta}` with top‑level `meta`, and include `freshness` + `confidence`. Use the control‑actions envelope as the pattern. fileciteturn23file0L1-L110  
2. **Implement “coverage and degradations” everywhere costs or plans appear.** Do not emit a single scalar without coverage (e.g., cost parse rate). fileciteturn42file0L70-L140 citeturn1search3turn1search6  
3. **Redaction by construction**: allowlist audit `metadata` keys per action type; default‑redact evidence bodies in executive output. fileciteturn25file0L80-L140 citeturn0search1  
4. **Executive status scoring v1**: deterministic, factorized, with top‑drivers and “what would change the score.” Prefer boring clarity over cleverness. fileciteturn45file3L120-L220  
5. **Audit log operability checks** (DB size watermark, last event time) surfaced as warnings; log‑failure awareness aligns with good audit/log management practice. fileciteturn27file0L1-L80 citeturn0search0turn0search4

### Should
Improvements that materially raise executive usefulness, still sprint‑plausible if scope is managed:

- **Capabilities inventory as a registry**, not inferred. Today “capabilities we have” would be a guess based on agents/processes/subscriptions. Add a lightweight `CAPABILITIES.md` with stable IDs, owners, and evidence links; the executive layer should read it. (This is the same “markdown as system of record” pattern you already use.) fileciteturn8file3L50-L90  
- **Normalize cost fields** in the subscription register to reduce regex parsing. Treat this as “data contract work,” not UI work. fileciteturn42file0L70-L140  
- **Tie “what has been done” to three sources**: git changes, audit actions, and task state transitions—presented as three separate subsections so the reader understands what kind of “done” is meant. fileciteturn53file0L1-L80

### Nice
High leverage later, but risky to cram into one sprint without eroding trust:

- Natural‑language Q&A that synthesizes across artifacts (unless you can guarantee citations and redaction—otherwise it becomes a confidence illusion).
- Trend charts across weeks (requires retention strategy, stable schemas, and backfill rules).
- Rich drill‑downs for cost allocation (requires stronger FinOps data discipline; see FinOps allocation and showback concepts). citeturn1search5turn1search6