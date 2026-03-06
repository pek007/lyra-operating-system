# LYRA_OS_PXS_INTEGRATION_PLAN_V1

Status: Draft for sponsor review  
Owner: Lyra (main)  
Sponsor: Peter Eklind  
Date: 2026-03-06

## 1) Purpose

Turn the Lyra OS ↔ PXS relationship into an explicit, enforceable operating model:
- Lyra OS = control plane + reusable capability provider
- PXS = domain instance + product execution layer

This plan operationalizes the boundary already described in:
- `governance/VEGA_PX_INSTANCE_BOUNDARY_SPEC_V1.md`
- `governance/VEGA_ACCEPTANCE_TEST_RUN_SHEET_V1.md`

## 2) Target architecture (v1)

### 2.1 Separation model
- Keep separate workspaces:
  - Lyra OS: `/Users/lyra/.openclaw/workspace`
  - Vega/PXS: `/Users/lyra/.openclaw/workspace-px-internal-dev`
- No default cross-domain reads.
- Cross-domain exchange only via explicit handoff artifacts and register.

### 2.2 Capability delivery model
- Reusable OS capabilities are delivered to PXS as **versioned capability bundles**.
- Preferred transport:
  1. Shared skill packs (fast path)
  2. Plugin/service endpoint for high-assurance enforcement paths (hard policy gates)

### 2.3 Data and authority model
- PXS owns product/domain state and evidence.
- Lyra OS owns operating contracts, governance mechanisms, and shared operational primitives.
- No self-approval for authority increases (retain existing governance rule).

## 3) Scope of OS exports (v1)

Lyra OS may export only these capability classes to PXS:

1. **TDE kernel contracts + deterministic runners**
2. **Job/authority lifecycle primitives**
3. **Process registry + cadence templates**
4. **Tool/external-service governance baselines**
5. **Validation utilities (schema/rules/checks) that are domain-agnostic**

Everything else stays internal to Lyra OS engineering unless explicitly promoted.

## 4) Implementation phases

## Phase A — Boundary hardening (Immediate)

### A1. Confirm runtime configuration
- Vega remains bound to:
  - isolated workspace
  - dedicated agentDir
  - explicit account binding (`telegram accountId=vega`)
- Keep `sandbox.mode` and tool policy decisions documented with rationale.

### A2. Enforce handoff-only exchange
- Use `governance/handoffs/*.yaml` + `HANDOFF_REGISTER_V1.md` for any cross-domain transfer.
- Reject transfers missing owner/purpose/checksum.

### A3. Acceptance gate refresh
- Re-run and update `VEGA_ACCEPTANCE_TEST_RUN_SHEET_V1.md` after each boundary change.

Deliverables:
- Updated acceptance run sheet with pass/fail status
- Any config diffs linked as evidence

## Phase B — Capability packaging (1–2 sprints)

### B1. Create shared skill-pack structure
- Add a dedicated capability-pack repo or directory with versioning:
  - `lyra-tde`
  - `lyra-jobs-authority`
  - `lyra-process-cadence`
  - `lyra-tool-governance`

### B2. Add release semantics
- Semantic version tags for each capability pack.
- Compatibility notes per release.
- Explicit rollback version references.

### B3. Configure load strategy
- Prefer shared skills path for stable capability distribution.
- Keep workspace override ability for emergency local hotfixes.

Deliverables:
- Capability-pack manifest
- Versioning/compatibility policy file
- Initial released bundle set (v0.x)

## Phase C — Enforcement uplift (2–4 sprints)

### C1. Promote critical paths to plugin/service mode
Start with highest-risk controls:
- TDE mutation gates
- Authority change gates
- High-impact tool-action gates

### C2. Define deterministic interfaces
- Strict input schemas
- Deterministic pass/fail outputs
- Structured audit logs

### C3. Wire evidence pipeline
- Record all gate results into evidence logs by domain and date.

Deliverables:
- Plugin/service spec
- Pilot implementation for one critical gate
- Verification report with fail-closed tests

## Phase D — Production operating lanes (v1.1)

### D1. Two-lane operating model
- **PXS production lane:** minimal tool surface, pinned capability versions, strict controls
- **Lyra OS engineering lane:** faster iteration, separate profile/runtime, controlled promotion path

### D2. Promotion workflow
- Engineering lane → candidate release → acceptance tests → production lane promotion.

Deliverables:
- Lane policy spec
- Promotion checklist
- First successful promoted release evidence

## 5) Decision log (initial)

1. **Adopt service-provider model** (not monolithic “OS contains product”)
2. **Keep hard workspace separation by default**
3. **Use skill packs as baseline distribution channel**
4. **Escalate to plugin/service for hard enforcement paths**
5. **Require explicit handoff artifacts for cross-domain data movement**

## 6) Risks and controls

### Risk 1: Capability drift across workspaces
Control:
- Version pinning + compatibility notes + acceptance checks before upgrade

### Risk 2: Boundary erosion via convenience path shortcuts
Control:
- No default cross-domain reads; handoff register mandatory; periodic audit checks

### Risk 3: Over-centralizing sensitive logic in uncontrolled scripts
Control:
- Migrate high-impact controls to deterministic plugin/service interfaces

### Risk 4: Runtime/config regressions during tuning
Control:
- Treat config changes as production changes with diff, rollback, and evidence

## 7) Success criteria

This plan is considered active and successful when:
1. Vega runs daily PXS operations fully inside isolated workspace
2. PXS consumes shared OS capabilities through versioned bundles
3. At least one high-risk control is enforced through deterministic service/plugin path
4. Cross-domain transfers are traceable in handoff register only
5. Acceptance sheet status is PASS on all mandatory boundary checks

## 8) Immediate next actions (starting now)

1. Validate current Vega boundary against this plan and log evidence.
2. Draft `LYRA_CAPABILITY_PACK_SPEC_V1.md` with bundle list + versioning rules.
3. Select one high-risk gate (recommended: TDE mutation gate) for plugin/service pilot.
4. Schedule acceptance rerun after capability-pack baseline is in place.

---

Prepared by Lyra based on:
- `knowledge/reports/2026-03-06__deepresearch__lyra-os-as-operating-system-for-pxs-in-openclaw__v1.md`
- Existing governance boundary docs in `governance/`.
