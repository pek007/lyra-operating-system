# Vega PX Boundary Acceptance Test Run Sheet v1

Run owner: Lyra (main)
Run date/time (UTC): 2026-03-05T18:46:00Z
Environment: OpenClaw local gateway (macOS)
Agent ID: `px-internal-dev` (Vega)

## Test objective
Verify Vega can operate as a true PX instance under Pattern A:
- hard workspace/state separation
- pinned platform-core dependency model
- explicit handoff-only cross-domain exchange

---

## A. Workspace and state isolation

### A1. Agent identity and workspace
- [x] Confirm Vega agent exists and is distinct from main agent
- [x] Confirm Vega workspace root is isolated (not Lyra workspace)
- [x] Confirm Vega `agentDir` is distinct

Evidence:
- `openclaw agents list --json`
- Vega workspace: `/Users/lyra/.openclaw/workspace-px-internal-dev`
- Vega agentDir: `/Users/lyra/.openclaw/agents/px-internal-dev/agent`

Result: PASS

### A2. No Lyra-path dependency in normal operation
- [x] Run representative Vega tasks (read/write docs, git status, planning artifacts)
- [x] Verify all file paths are inside Vega workspace (for normal tasks run)
- [x] Verify no required reads from Lyra workspace paths (for normal tasks run)

Evidence:
- Vega self-check run (created/read `acceptance_probe.txt`, git status in Vega workspace)
- Reported no dependency on `/Users/lyra/.openclaw/workspace` for that normal run

Result: PASS (normal operation), with boundary caveat captured in E2

---

## B. PX repo placement and working flow

### B1. `pxs` repo in Vega workspace
- [ ] Confirm `pxs` exists inside Vega workspace
- [ ] Confirm Vega can run normal git operations inside that repo

Evidence:
- `ls -la /Users/lyra/.openclaw/workspace-px-internal-dev` shows no `pxs` repo present

Result: FAIL

---

## C. Platform-core dependency (Pattern A)

### C1. Pinned dependency present
- [ ] Confirm platform-core is consumed as pinned dependency (e.g., submodule ref)
- [ ] Confirm pinned commit/tag is documented
- [ ] Confirm update path requires intentional bump

Evidence:
- No platform-core submodule/dependency configuration found yet in Vega workspace

Result: FAIL

### C2. No duplicate canonical policy copies
- [ ] Spot-check canonical shared policy/process docs are dependency-based, not manually duplicated across workspaces

Evidence:
- Not verifiable until C1 is implemented

Result: FAIL

---

## D. Context safety and governance injection

### D1. Bootstrap/context limits
- [x] Inspect Vega context report (`/context list` or equivalent)
- [x] Confirm governance-critical files are present and not truncated

Evidence:
- Agent run metadata `injectedWorkspaceFiles` showed injected files with `truncated: false`

Result: PASS

---

## E. Cross-domain handoff enforcement

### E1. Handoff artifact validation
- [x] Create one test handoff using `HANDOFF_ARTIFACT_TEMPLATE_V1.yaml`
- [x] Validate required fields: owner, purpose, checksum, approval
- [x] Register entry in `HANDOFF_REGISTER_V1.md`

Evidence:
- `governance/handoffs/HO-20260305-001.yaml`
- `governance/HANDOFF_REGISTER_V1.md` updated

Result: PASS

### E2. No direct cross-domain read by default
- [ ] Attempt non-handoff cross-domain read (expected denied by policy/process)
- [ ] Confirm only registered handoff path is used for transfer

Evidence:
- Original 2026-03-05 check: Vega test explicitly listed `/Users/lyra/.openclaw/workspace` successfully (read allowed)
- 2026-03-15 config hardening: `px-internal-dev.tools.fs.workspaceOnly=true` is now enforced for filesystem tools
- However `px-internal-dev` still has `sandbox.mode=off` plus gateway `exec` with `security=full` and `ask=off`, so cross-domain host reads remain operationally possible via shell execution even after the filesystem-tool narrowing
- Post-change validation artifact: `products/task-management/04-execution/VEGA_PXS_BOUNDARY_POST_CHANGE_VALIDATION_2026-03-15.md`

Result: FAIL (improved but not yet deny-by-default across the full runtime surface)

---

## F. TDE isolation readiness (if active in PX)

### F1. Domain-local execution
- [ ] Run TDE checks in PX-local paths
- [ ] Confirm bindings/objectives/evidence resolve within PX domain only
- [ ] Confirm fail-closed behavior on invalid inputs

Evidence:
- Not executed in this pass

Result: N/A

---

## Final gate

Overall result: FAIL

Blocking failures:
1. `pxs` repo not present in Vega workspace (B1)
2. Platform-core pinned dependency not implemented (C1/C2)
3. Cross-domain read is currently allowed (E2), boundary not enforced

Remediation owner: Lyra + Peter
Target date: 2026-03-06

Approval to activate boundary v1:
- Sponsor (Peter): ____________________  Date: __________
- Run owner: Lyra (main)                Date: 2026-03-05
