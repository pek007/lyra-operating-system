# Vega PX Boundary Acceptance Test Run Sheet v1

Run owner: ____________________
Run date/time (UTC): ____________________
Environment: ____________________
Agent ID: `px-internal-dev` (Vega)

## Test objective
Verify Vega can operate as a true PX instance under Pattern A:
- hard workspace/state separation
- pinned platform-core dependency model
- explicit handoff-only cross-domain exchange

---

## A. Workspace and state isolation

### A1. Agent identity and workspace
- [ ] Confirm Vega agent exists and is distinct from main agent
- [ ] Confirm Vega workspace root is isolated (not Lyra workspace)
- [ ] Confirm Vega `agentDir` is distinct

Evidence:
- ________________________________________________

Result: PASS / FAIL

### A2. No Lyra-path dependency in normal operation
- [ ] Run representative Vega tasks (read/write docs, git status, planning artifacts)
- [ ] Verify all file paths are inside Vega workspace
- [ ] Verify no required reads from Lyra workspace paths

Evidence:
- ________________________________________________

Result: PASS / FAIL

---

## B. PX repo placement and working flow

### B1. `pxs` repo in Vega workspace
- [ ] Confirm `pxs` exists inside Vega workspace
- [ ] Confirm Vega can run normal git operations inside that repo

Evidence:
- ________________________________________________

Result: PASS / FAIL

---

## C. Platform-core dependency (Pattern A)

### C1. Pinned dependency present
- [ ] Confirm platform-core is consumed as pinned dependency (e.g., submodule ref)
- [ ] Confirm pinned commit/tag is documented
- [ ] Confirm update path requires intentional bump

Evidence:
- ________________________________________________

Result: PASS / FAIL

### C2. No duplicate canonical policy copies
- [ ] Spot-check canonical shared policy/process docs are dependency-based, not manually duplicated across workspaces

Evidence:
- ________________________________________________

Result: PASS / FAIL

---

## D. Context safety and governance injection

### D1. Bootstrap/context limits
- [ ] Inspect Vega context report (`/context list` or equivalent)
- [ ] Confirm governance-critical files are present and not truncated

Evidence:
- ________________________________________________

Result: PASS / FAIL

---

## E. Cross-domain handoff enforcement

### E1. Handoff artifact validation
- [ ] Create one test handoff using `HANDOFF_ARTIFACT_TEMPLATE_V1.yaml`
- [ ] Validate required fields: owner, purpose, checksum, approval
- [ ] Register entry in `HANDOFF_REGISTER_V1.md`

Evidence:
- ________________________________________________

Result: PASS / FAIL

### E2. No direct cross-domain read by default
- [ ] Attempt non-handoff cross-domain read (expected denied by policy/process)
- [ ] Confirm only registered handoff path is used for transfer

Evidence:
- ________________________________________________

Result: PASS / FAIL

---

## F. TDE isolation readiness (if active in PX)

### F1. Domain-local execution
- [ ] Run TDE checks in PX-local paths
- [ ] Confirm bindings/objectives/evidence resolve within PX domain only
- [ ] Confirm fail-closed behavior on invalid inputs

Evidence:
- ________________________________________________

Result: PASS / FAIL / N/A

---

## Final gate

Overall result: PASS / FAIL

Blocking failures:
1. ________________________________________________
2. ________________________________________________

Remediation owner: ____________________
Target date: ____________________

Approval to activate boundary v1:
- Sponsor (Peter): ____________________  Date: __________
- Run owner: ____________________        Date: __________
