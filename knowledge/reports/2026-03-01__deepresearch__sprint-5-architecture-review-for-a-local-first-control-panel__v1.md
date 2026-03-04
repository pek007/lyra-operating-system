---
title: "Sprint 5 Architecture Review for a Local-First Control Panel"
date: 2026-03-01
source: deepresearch
ingest_from: "knowledge/inbox/external-analysis-dropzone/deep-research-report (17).md"
tags: [external-analysis, deepresearch]
decision_relevance: tbd
confidence: tbd
status: archived-source
---

# Sprint 5 Architecture Review for a Local-First Control Panel

## Reliability-first architecture validity

The core posture—a local-first, read-first dashboard that derives views from workspace artifacts via an Express API and a React UI—is a good fit for your stated outcomes (decision-grade visibility without a heavyweight backend). In particular, the “hybrid” direction (on-demand aggregation plus scheduled materialization of stable summaries) is a strong reliability move when the same computations are repeatedly needed and the underlying sources are file-based. fileciteturn24file2L1-L120

Where reliability is currently *undermined* is not the model, but the “contract stability” around configuration and routes:

- **Configuration is implicitly coupled to process working directory.** The API’s `.env` loading and monorepo-root/workspace-root resolution are computed from `process.cwd()`, and the fallback defaults to `./sample-data` when `WORKSPACE_ROOT` is not read. This makes production-like runs fragile: starting the API from a different directory can silently point the server at the wrong workspace (or sample data), which then cascades into “missing file” surfaces. fileciteturn30file0L1-L120  
- **Executive endpoint availability is “route-mounted-by-config,” not “route-visible-with-explicit-state.”** If `CONTROL_PANEL_TOKEN` is missing, `GET /api/executive/summary` is not mounted at all (effectively 404). The web client treats non-401/403 failures as a `[FETCH_ERROR]` banner, creating an avoidable reliability hit and confusing operator experience. fileciteturn30file0L1-L120 fileciteturn32file0L1-L120 fileciteturn34file2L1-L90 fileciteturn36file0L1-L80

**One-sprint validity call:** The reliability-first Sprint 5 target is valid, but you should treat “config + route contract hardening” as Sprint 5’s *primary* architectural deliverable—because it is the upstream cause of multiple downstream symptoms (executive fetch errors, “skills-policy not found,” and intermittent security surfaces). fileciteturn24file2L1-L120

Concrete one-sprint decisions that fit the current codebase:

- **Decision:** Make core routes *always present* (return explicit state/errors), rather than conditionally mounting routers.  
  **Acceptance check:** `/api/executive/summary` must return either (a) `200` with data, (b) `401/403` when a token is required/incorrect, or (c) a clear “disabled on server” error payload if the server is misconfigured—never a 404 due to route absence. fileciteturn32file0L1-L120 fileciteturn34file2L1-L90
- **Decision:** Move “workspace root + key file discovery” into a deterministic startup module that does not depend on `process.cwd()` (e.g., resolve from server file location OR walk upward to find `pnpm-workspace.yaml`).  
  **Acceptance check:** Starting the API from repo root, from `apps/api`, and from `dist/` must all resolve the same workspace root and show the same surface availability. fileciteturn30file0L1-L120
- **Decision:** Standardize the response envelope for “core surfaces” (Executive, Skills, Risk/Security, Build) to consistently include structured warnings/errors (even if other legacy endpoints remain string-based for now).  
  **Acceptance check:** UI never has to pattern-match error strings to decide whether to prompt for auth vs. show fallback. fileciteturn34file2L1-L90 fileciteturn36file0L1-L80

## Top risks for Sprint 5

| Failure mode | Impact | Likelihood | One-sprint mitigation |
|---|---:|---:|---|
| **Workspace root resolves incorrectly (cwd-coupled), leading to “missing” skills policy/security audit/tasks** | High: multiple tabs degrade simultaneously; trust collapse | High | Centralize workspace resolution (repo-root discovery), expose resolved paths + file existence via `/api/health` and UI banner; add one integration test that boots API from multiple working directories. fileciteturn30file0L1-L120 fileciteturn38file2L1-L60 |
| **Executive route not mounted without token → 404 → client shows `[FETCH_ERROR]` instead of auth or config guidance** | High: “flagship” surface appears broken | High | Always mount executive router; if token not configured, return explicit “EXECUTIVE_DISABLED” error payload; treat 404 (if it ever happens) as a bug. fileciteturn30file0L1-L120 fileciteturn34file2L1-L90 fileciteturn36file0L1-L80 |
| **Materialization jobs write JSON non-atomically; API reads mid-write → parse failure → intermittent rendering (security/audit especially)** | High: “sometimes blank” undermines confidence more than “always missing” | Medium | Implement `atomicWrite()` helper (write temp in same dir → rename/replace); ensure audit/security summary writers use it. Atomic rename is a known POSIX pattern. citeturn2search7turn2search0 |
| **IA consolidation breaks operator muscle memory / deep links; old routes die abruptly** | Medium: usability regression, perceived instability | Medium | Keep old routes for ≥1 sprint with redirects; show “moved” affordance; add route regression tests for `/`, `/next`, `/watch`, `/roles/security`. fileciteturn47file1L1-L40 |
| **Jobs introduce silent stale data (materialized artifacts present but outdated), creating false certainty** | High: decisions based on stale summaries | Medium | Embed freshness in every artifact (`generated_at`, input fingerprint, source timestamps); UI displays “age” + “last run status”; API emits warnings when stale beyond threshold. fileciteturn24file2L1-L120 |

## Materialization-job design guidance

Sprint 5’s brief already specifies a set of materialized artifacts (executive/risk-audit/capabilities/build) under governed workspace paths. Treat that as a *read model contract*: the jobs produce these artifacts; the API consumes them (with on-demand fallback). fileciteturn24file2L1-L120

### Idempotency

A practical one-sprint approach is “idempotent by input fingerprint”:

- **Define an input fingerprint** per job run, e.g.:
  - `workspace_revision` (git HEAD when available),
  - plus a small set of *non-git* source fingerprints for key files (mtime + size + optional hash for `.control-panel/skills-policy.yaml`, `knowledge/evidence/latest-security-audit.json`, etc.).  
  The code already uses git revision as a first-class concept in summaries; re-use that mental model. fileciteturn24file2L1-L120
- **If the fingerprint matches the last successful run’s fingerprint, skip rewriting.** Still update a “checked_at” timestamp in a lightweight run log if you want visibility.

For action/event materialization, you already have an idempotency pattern in your SQLite audit schema (unique index scoped by actor/action/subject/idempotency_key). That’s a useful precedent: idempotency is part of the architecture vocabulary, not a new concept. fileciteturn56file0L1-L60

### Freshness

Freshness should be explicit and machine-checkable:

- Every materialized JSON should include `meta: { generated_at, job_version, input_fingerprint, workspace_revision, sources: [...] }`.
- Each source entry should include:
  - `path` (or logical source name),
  - `last_modified_at` (read from filesystem),
  - `stale` boolean under a job-specific threshold.

This aligns with the S4 executive “freshness/confidence” intent, but makes it operational: jobs are the producers of freshness truth, not the UI guessing. fileciteturn24file2L1-L120

### Run evidence

Aim for *two layers* of evidence (one sprint, minimal):

- **Per-job “latest run” record**:  
  `knowledge/evidence/summaries/_runs/<job>/latest.json`
- **Append-only historical run records** (optional but valuable):  
  `knowledge/evidence/summaries/_runs/<job>/<YYYY-MM-DD>/<run_id>.json`

Each run record should contain: `{ run_id, started_at, finished_at, status, duration_ms, input_fingerprint, produced_paths, warnings_count, errors_count }`.

This gives you post-mortems and makes the UI trustworthy (“what ran, when, with what inputs?”) without adding a database.

### Atomicity and corruption resistance

Given you already observed “not rendering reliably,” assume concurrent read/write will happen (API reads while jobs write). The simplest mitigation is the standard atomic replacement pattern:

1. write `target.json.tmp` in the same directory,
2. fsync/close (optional in one sprint, but close is non-negotiable),
3. rename/replace to `target.json`.

On POSIX filesystems, rename is the canonical atomic switch from old to new name from the perspective of other processes. citeturn2search7turn2search0

### Scheduling and concurrency

For one-sprint practicality in a local-first system, prefer **external scheduling + single-purpose CLI** over in-process cron:

- Implement a `materialize` command in `@control-panel/api` (or a small `apps/api/src/jobs/` entrypoint) that takes `--job <name>` and uses the same workspace resolution code as the server.
- Let the OS-level scheduler (cron/launchd/systemd timers) call it hourly/daily.

This keeps the API server simpler (a reliability win) and avoids “jobs blocked by the web server event loop.”

**Acceptance checks (materialization):**
- Running the job twice with unchanged inputs does not change output bytes (or at least keeps stable `input_fingerprint` and does not generate duplicate “success” records).
- When the job is forcibly interrupted mid-write, the API still serves the previous valid artifact (no partial JSON). citeturn2search0turn2search7

## Information architecture consolidation guidance

### Current IA symptoms

Your top nav currently exposes **both intent-based views and role views at the same level**, which creates overlap: `Now`, `Next`, `Watch`, and role-based `Security` all compete for “what should I look at?” attention. fileciteturn47file1L1-L40

The overlap is structural, not cosmetic:
- `Watch` includes `securitySummary` and risk-related material.
- `Security` role summary also surfaces risk posture and audit findings. fileciteturn47file1L1-L40 fileciteturn40file1L1-L80 fileciteturn50file0L1-L120

### One-sprint tab model

Do *not* attempt a full re-architecture. Instead, use a “new IA shell with old pages” approach:

- **Top-level (proposed):** Executive · Work · Risk · Build · Changes · Capabilities · Roles  
  - **Executive** stays `/executive` (flagship).
  - **Work** becomes the primary for “Now/Next/Tasks.”  
    - `/work` shows “Now” content first.  
    - `/work/next` maps to the old Next view.  
    - Keep `/` and `/next` as redirects or thin wrappers for one sprint.
  - **Risk** unifies today’s `Watch` + “Security role” overlap.  
    - Create `/risk` as the consolidated landing.  
    - Keep `/watch` and `/roles/security` as redirects (or show a “Moved to Risk” banner).
  - **Build** is new (see next section).
  - **Capabilities** can be your existing Skills surface (renamed label only, not concept change).

This is consistent with the Sprint 5 target state (“decision intent” alignment) while keeping implementation bounded. fileciteturn24file2L1-L120 fileciteturn47file1L1-L40

### Migration safety

Rollout sequencing that avoids breaking trust:

- **Phase A (first half of sprint):** Add new routes *without* removing old ones. Add redirects, but keep old pages reachable.  
  **Acceptance check:** all existing routes still return 200 in the UI (or clean redirects), especially `/`, `/next`, `/watch`, `/roles/security`. fileciteturn47file1L1-L40
- **Phase B (second half):** Update nav to the new IA. Old routes become “legacy entry points.”  
  **Acceptance check:** a user can reach every previous surface in ≤2 clicks from the new nav; old deep links do not produce blank pages.

Add one integration test suite that asserts the route map and key redirects. This is cheap and directly guards the “route cleanup” scope.

## Fallback and error-handling for missing files and path issues

### What the code is doing today

A few reliability-relevant behaviors are clear from the current implementation:

- Workspace root selection is driven by `WORKSPACE_ROOT` with a default to `./sample-data`, and relative resolution depends on a monorepo-root computed from `process.cwd()`. fileciteturn30file0L1-L120
- Skills policy loads from a fixed relative policy path `.control-panel/skills-policy.yaml` and emits a warning when missing. fileciteturn38file2L1-L80
- Security audit summary is read from a JSON file and returns `null` when missing/unparseable, which can present as “intermittently missing” if reads collide with writes. fileciteturn40file1L1-L80
- The executive UI treats non-401/403 errors as generic fetch failures, so “disabled route” and “auth required” can become indistinguishable to an operator. fileciteturn34file2L1-L90 fileciteturn36file0L1-L80

### One-sprint fallback contract

Adopt a single operational rule:

**Core surfaces must never blank-screen due to missing files; they must degrade with explicit, structured warnings + “what path did you look at?” context.**

Concrete guidance:

- **Centralize “workspace diagnostics” at startup** and expose it via `/api/health`:
  - resolved `workspaceRoot`,
  - booleans for presence of key files (`TASKS.md`, `RISK_REGISTER.md`, `.control-panel/workflow-config.yaml`, `.control-panel/skills-policy.yaml`, `knowledge/evidence/latest-security-audit.json`),
  - feature flags: “executive enabled,” “actions enabled,” “audit DB path,” etc.  
  This turns “path issues” from a debugging exercise into an observable system state. (It also aligns with the idea that config should be explicit and separable from code.) citeturn0search0 fileciteturn30file0L1-L120
- **Make missing/disabled states first-class.** For example:
  - If executive is disabled because no server token is configured, return a structured error payload with code `EXECUTIVE_DISABLED` and an operator-facing remediation message.
  - Do not rely on “router not mounted.” fileciteturn32file0L1-L120
- **Standardize warnings/errors for core endpoints** to objects:
  - `{ code, message, scope, severity, evidence_ref? }`  
  This already exists on the executive side; extend the same shape to Skills + Risk + Build so the UI can render consistently. fileciteturn34file2L1-L90 fileciteturn38file2L1-L80
- **For file reads that can race with job writes**, treat “parse failure” as a warning and *retry once* (short delay) before declaring missing/unparseable. Combined with atomic writes, this becomes rare.

**Acceptance checks (fallback):**
- With an intentionally mis-pointed `WORKSPACE_ROOT`, every core page renders an explicit “workspace misconfigured” banner and shows resolved paths; no page shows only `[FETCH_ERROR]`.
- With `skills-policy.yaml` genuinely missing, Skills page shows “File not found” *as a warning*, and the rest of the UI remains functional. fileciteturn38file2L1-L80 fileciteturn34file2L1-L90

## Build-status summary design guidance

Sprint 5 calls out “build tracking” as distinct from the existing git commit list. Treat build status as: **what version is running, what content pipelines last ran, and whether the system is in a known-good state—without needing to infer from raw commits.** fileciteturn24file2L1-L120

### Minimal, local-first build summary contract

Implement `GET /api/build/summary` (as already proposed) with three layers:

- **Runtime identity**
  - `app_version` (package.json),
  - `app_commit` (git describe/HEAD for the control-panel repo),
  - `built_at` (inject at build time via an env var or a generated file).
- **Workspace identity**
  - `workspace_revision` (git HEAD of the workspace when available),
  - `workspace_is_git` boolean,
  - `workspace_path` (already in health).
- **Pipelines status**
  - for each materialization job: `last_run_at`, `status`, `artifact_path`, `input_fingerprint`, `duration_ms`, `warnings/errors counts`.

This gives you “software delivery status beyond git commit list” while staying local-first.

### How to populate it in one sprint

- Treat the **build summary itself as a materialized artifact** (`build-daily.json`), but allow the endpoint to “overlay” live runtime identity on top (because build info should be current even if jobs are stale).
- If you later want CI signals from entity["company","GitHub","code hosting platform"], make them **optional**: read a workspace file like `knowledge/evidence/build/ci-status.json` when present; otherwise emit a structured warning “CI status not configured.” Do not add network calls in Sprint 5.

**Acceptance checks (build status):**
- Build page loads on a fresh workspace with no special setup and shows at least runtime + workspace identity plus “pipelines not yet run” warnings (not empty).
- After running the daily jobs once, Build page shows “last run” timestamps and artifact paths for each job.

## Must/Should/Nice adjustments before implementation

### Must

- **Unbreak configuration determinism**
  - Replace cwd-based repo/workspace resolution with a deterministic approach (repo-root discovery).  
  - Surface resolved workspace root + key file existence in `/api/health` (and a UI banner when misconfigured). fileciteturn30file0L1-L120 citeturn0search0
- **Stabilize executive route contract**
  - Always mount `/api/executive/summary`.  
  - Return explicit “disabled” vs “auth required” states; update the UI to handle them without devolving to `[FETCH_ERROR]`. fileciteturn32file0L1-L120 fileciteturn34file2L1-L90
- **Add atomic-write primitive and use it for job outputs and any frequently-read JSON**
  - This directly targets “renders unreliably” failure modes. citeturn2search7turn2search0
- **Ship the content pipeline as a CLI + artifacts**
  - Create the artifact paths described in Sprint 5 (executive/risk-audit/capabilities/build).  
  - Even if only 1–2 jobs are fully populated, the pipeline framework and run evidence must exist. fileciteturn24file2L1-L120
- **IA consolidation with redirects, not removals**
  - Introduce `/work`, `/risk`, `/build`; keep `/`, `/next`, `/watch`, `/roles/security` functioning via redirects and/or legacy wrappers. fileciteturn47file1L1-L40

### Should

- **Unify warnings/errors to structured objects on core surfaces**
  - Executive already uses structured warnings/errors; extend the same shape to Skills and Risk-related endpoints to reduce bespoke UI handling. fileciteturn38file2L1-L80
- **Add “freshness + last-run” UI badges**
  - Every summary card should show its `generated_at` age and degrade visibly when stale (not silently).
- **Add small integration test suite**
  - “Starts from multiple working dirs,” “core endpoints return 200 + structured warnings on missing files,” “redirect map stable,” “jobs idempotent twice.”  
  This is the highest leverage harness for Sprint 5.

### Nice

- **Promote role views under a “Roles” grouping instead of top-level nav**
  - Keeps the top nav intent-based (Executive/Work/Risk/Build) while still supporting role drills.
- **Optional CI integration**
  - If you later bring in remote build statuses, prefer “drop a file into the workspace and let the panel read it” over API calls from inside the control panel.

### Rollout sequencing

A pragmatic sprint sequence that minimizes risk:

1. **Config + health diagnostics first**  
   Acceptance: “wrong cwd” no longer changes workspace resolution; `/api/health` shows resolved root + key file presence.
2. **Executive fetch reliability next**  
   Acceptance: Executive page never shows `[FETCH_ERROR]` due to route absence; it shows either auth prompt or explicit “disabled on server.”
3. **Atomic writes + first materialization job(s)**  
   Acceptance: jobs produce artifacts + run evidence; API can read them while job runs without intermittent null/parse failures.
4. **IA consolidation and redirects**  
   Acceptance: new nav reduces overlap; old routes still work; at least one automated redirect/regression test passes on CI/local.

This ordering turns Sprint 5 into a compounding reliability gain rather than three parallel change streams that can mask each other’s failures.