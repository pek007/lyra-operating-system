# VEGA PX Instance Boundary Spec v1

Status: Draft for activation
Owner: Head of Internal Development (Vega)
Sponsor: Peter Eklind
Effective date: 2026-03-05
Decision: Adopt Pattern A (separate PX instance + pinned platform-core dependency)

## 1) Objective
Create a hard-separated PX runtime (Vega) that can execute PX strategy work without sharing Lyra OS development context, while still consuming reusable OS capabilities through a controlled dependency model.

## 2) Scope
In scope:
- Vega runtime boundary
- Workspace/data/state separation
- Platform-core dependency model (pinned)
- Cross-domain handoff protocol
- Acceptance checks for go-live

Out of scope:
- Client-facing PX product design details
- Model/provider routing changes outside Vega

## 3) Boundary model (mandatory)

### 3.1 Runtime isolation
- Vega runs as its own persistent agent identity.
- Vega has its own:
  - workspace root
  - agent state directory (sessions/auth/state)
  - session history and memory files
  - credential provisioning
- No reuse of Lyra `agentDir`.

### 3.2 Filesystem policy
- Keep `tools.fs.workspaceOnly = true` posture.
- Vega must complete day-to-day work fully inside Vega workspace paths.
- No default read/write access to Lyra workspace.

### 3.3 Repo placement
- `pxs` repository must live in Vega workspace (clone or mounted equivalent).
- Vega should not depend on `pxs` inside Lyra workspace paths.

## 4) Platform-core dependency model (Pattern A)

### 4.1 Principle
Reusable OS mechanisms are consumed as versioned dependency, not copied per workspace.

### 4.2 Initial mechanism
- Use a pinned dependency (Git submodule recommended for v1).
- Pin to explicit commit/tag.
- Upgrades require intentional bump + changelog + validation pass.

### 4.3 What belongs in platform-core
- Shared schemas, validators, and governance tooling
- TDE runtime contracts/utilities
- Reusable process/runbook assets that are genuinely cross-domain

### 4.4 What stays domain-local
- PX tasks, evidence, logs, decisions, notes
- PX memory/state artifacts
- Domain-specific strategy drafts and business-unit plans

## 5) Cross-domain handoff protocol (Lyra ↔ Vega)

### 5.1 Rule
No cross-domain reads by default. Exchange only through explicit handoff artifacts.

### 5.2 Handoff artifact schema (minimum)
```yaml
handoff_id: "HO-YYYYMMDD-###"
from_domain: "os|px"
to_domain: "os|px"
owner: "name/role"
purpose: "why this transfer exists"
classification: "internal|restricted"
created_at: "ISO-8601"
expires_at: "ISO-8601|null"
source_refs:
  - "path/or/uri"
checksum: "sha256:..."
approved_by: "name/role"
```

### 5.3 Operational controls
- Every handoff logged in a handoff register.
- Expiry enforced for temporary artifacts.
- Reject handoff artifacts missing owner/purpose/checksum.

## 6) Vega operating profile (v1)
- Primary role: Head of Internal Development at PX.
- Scope: PX only.
- First-quarter focus:
  - models/departments/IP/knowledge/business unit structure
  - operating cadence and dashboarding
  - reusable internal development playbooks

## 7) Acceptance criteria (go-live)
All must pass:
1. Vega can run git + docs + delivery actions entirely inside Vega workspace.
2. Vega does not require Lyra workspace paths for normal operation.
3. Platform-core is consumed via pinned dependency (not duplicate policy copies).
4. `/context list` (or equivalent context report) shows governance-critical files are not truncated.
5. Cross-domain transfers happen only via registered handoff artifacts.
6. TDE checks (if used in PX) pass in PX-local paths with fail-closed behavior.

## 8) Implementation checklist
- [ ] Create/confirm Vega isolated workspace and state dir
- [ ] Place `pxs` repo inside Vega workspace
- [ ] Provision Vega credentials explicitly (least privilege)
- [ ] Add platform-core pinned dependency in PX workspace
- [ ] Create `handoff-register` + template
- [ ] Run acceptance checks and record evidence
- [ ] Activate v1 boundary in operations

## 9) Change control
Any change to boundary, cross-domain access, or credential sharing requires sponsor approval and documented rationale.
