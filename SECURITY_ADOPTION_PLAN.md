# SECURITY_ADOPTION_PLAN.md

Status: Active  
Owner: Peter (decision owner), Lyra (implementation coordination)

## Objective
Adopt high-impact cybersecurity controls for OpenClaw quickly, with minimal operational friction and clear verification.

## Principles
1. Secure-by-default beats secure-by-documentation.
2. Enforce controls in code/config, not only in runbooks.
3. Prefer reversible changes with explicit rollback.
4. Measure completion using acceptance criteria, not intent.

---

## Wave 1 — Immediate hardening (target: 7 days)

### 1) Loopback-only API + strict CORS + limits
- **Priority:** P0
- **Owner:** Engineering
- **Effort:** 0.5–1 day
- **Scope:** Control Panel API runtime config
- **Actions:**
  - Bind API listener to `127.0.0.1`
  - Restrict CORS origins to localhost UI origins only
  - Add request size limit
  - Add baseline rate limit
- **Acceptance criteria:**
  - API not reachable from LAN interface
  - Non-localhost origins rejected by CORS
  - Oversized payload rejected with expected status
  - Rate limit triggers under abuse test
- **Rollback:**
  - Revert server config commit and restart API

### 2) Remove shell-based command execution
- **Priority:** P0
- **Owner:** Engineering
- **Effort:** 1–2 days
- **Scope:** Git change feed + evidence ingestion scripts
- **Actions:**
  - Replace shell execution with exec-file semantics
  - Remove `shell=True` from Python subprocess calls
  - Pin command paths and sanitize env
- **Acceptance criteria:**
  - No shell invocation in target paths
  - Commands still function in normal workflows
  - PATH-hijack simulation fails to alter command resolution
- **Rollback:**
  - Restore previous command invocation path and rerun smoke tests

### 3) Trusted workspace boundary enforcement
- **Priority:** P0
- **Owner:** Engineering
- **Effort:** 2–5 days
- **Scope:** All workspace reads by control panel/services
- **Actions:**
  - Realpath boundary check on all file reads
  - Reject symlinks for system-of-record files
  - Enforce max file size limits before parse
- **Acceptance criteria:**
  - Path escape attempts blocked
  - Symlinked registry files rejected
  - Oversized file parsing prevented
- **Rollback:**
  - Temporarily disable strict mode via feature flag (if implemented)

### 4) Secrets/state permission hardening
- **Priority:** P0
- **Owner:** Ops
- **Effort:** 0.5–1 day
- **Scope:** `~/.openclaw`, `.secrets`, key local artifacts
- **Actions:**
  - Enforce strict directory/file permissions
  - Verify no plaintext secrets in shared docs/logs
  - Re-run security audit after hardening
- **Acceptance criteria:**
  - Permission audit passes baseline policy
  - Security audit shows no critical permission findings
- **Rollback:**
  - Restore previous perms only if functionality breaks; log exception

---

## Wave 2 — Enforcement and integrity (target: 2–4 weeks)

### 5) High-risk action policy enforcement
- **Priority:** P1
- **Owner:** Peter + Engineering
- **Effort:** 3–7 days
- **Scope:** Agent action layer and governance checks
- **Actions:**
  - Enforce approval gates for high-risk actions
  - Enforce per-agent tool allowlists
  - Log action decision trail (who/what/why/when)
- **Acceptance criteria:**
  - Blocked action tests pass for non-approved requests
  - Approved flow logs complete audit records
  - Policy bypass attempts are denied and logged
- **Rollback:**
  - Switch to monitor-only mode while preserving logs

### 6) Supply-chain minimum baseline
- **Priority:** P1
- **Owner:** Engineering
- **Effort:** 1–3 weeks
- **Scope:** Build pipeline and artifacts
- **Actions:**
  - Lockfile enforcement in CI
  - SBOM generation for artifacts
  - Build provenance/signing pipeline
- **Acceptance criteria:**
  - CI fails on lockfile drift
  - SBOM generated per build
  - Signed artifact verification step passes in deployment flow
- **Rollback:**
  - Keep CI checks in warn mode temporarily, with deadline to re-enforce

---

## Wave 3 — Scale-triggered controls (only when required)

### 7) Remote mode security profile
- **Priority:** P2 (conditional)
- **Trigger:** Any non-loopback deployment
- **Actions:**
  - Identity-aware front door (OIDC or mTLS)
  - TLS 1.3 policy
  - Network segmentation between gateway and API/UI
- **Acceptance criteria:**
  - Unauthenticated remote access blocked
  - Authenticated access path tested end-to-end

### 8) Attestation/update-chain hardening
- **Priority:** P2 (conditional)
- **Trigger:** Appliance/distributed deployment path
- **Actions:**
  - Select update framework (TUF/Uptane/SUIT as fit)
  - Define rollback protection strategy
  - Evaluate TPM-backed attestation for high-risk action gating
- **Acceptance criteria:**
  - Signed update chain verified
  - Downgrade/rollback prevention test passes

---

## Tracking model
Use this table in weekly review:

| Control | Priority | Owner | Status | Due | Evidence link | Notes |
|---|---|---|---|---|---|---|
| Loopback + CORS + limits | P0 | Engineering | Planned | YYYY-MM-DD |  |  |
| Remove shell exec paths | P0 | Engineering | Planned | YYYY-MM-DD |  |  |
| Workspace boundary checks | P0 | Engineering | Planned | YYYY-MM-DD |  |  |
| Secrets/permissions hardening | P0 | Ops | Planned | YYYY-MM-DD |  |  |
| High-risk policy enforcement | P1 | Peter/Engineering | Planned | YYYY-MM-DD |  |  |
| Supply-chain baseline | P1 | Engineering | Planned | YYYY-MM-DD |  |  |

---

## Done definition (program-level)
Security adoption wave is “done” when:
1. Every scoped control has objective evidence attached.
2. Smoke tests pass after each control rollout.
3. Security audit baseline is re-run and reviewed.
4. Exceptions are documented with owner + expiry date.
5. DR runbook includes recovery impact of new controls.

---

## Change safety
- Implement P0 controls behind short-lived feature flags where feasible.
- Roll out in small increments; test after each step.
- If a control disrupts operations, fallback to prior known-good config and log incident.
