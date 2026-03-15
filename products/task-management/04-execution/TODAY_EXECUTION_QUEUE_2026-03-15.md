# Today Execution Queue — 2026-03-15

Owner: Lyra  
Context: morning follow-through from overnight Control Tower synthesis and TDE state

## Objective
Convert the overnight synthesis into an immediately executable day plan with explicit order, decision gates, and evidence expectations.

## Today’s execution order

### 1. Vega/PXS boundary enforcement decision and apply sequence
**Why first**  
This is the clearest current portfolio bottleneck and the top gating dependency for safe downstream `pxs` consumption.

**Linked TDE item**  
- `TASK-20260314-VEGA-PXS-BOUNDARY-PASS`

**Current known state**  
- B1 stale fail is effectively resolved by current topology.
- C1 materially improved; pinned `platform-core` submodule exists.
- E2 remains the live blocking fail.
- Current blocker is a real config-backed enforcement gap: `px-internal-dev` still has broader filesystem access than the declared boundary model allows.

**Decision required**  
- Approve the minimal filesystem-boundary narrowing for `px-internal-dev`, then execute the apply/validate runbook.

**Execution artifact chain**  
- `products/task-management/04-execution/VEGA_PXS_BOUNDARY_CHANGE_REQUEST_2026-03-15.md`
- `products/task-management/04-execution/VEGA_PXS_BOUNDARY_MORNING_APPLY_RUNBOOK_2026-03-15.md`

**Definition of success today**  
- Approved config change applied cleanly
- Gateway/runtime healthy after restart
- E2 direct cross-domain read denied
- Vega-local smoke still passes
- Acceptance sheet refreshed for B1/C1/C2/E2
- Post-change validation artifact published

**If blocked**  
- If Peter does not approve narrowing, explicitly route to formal exception path rather than pretending the acceptance sheet can PASS.

---

### 2. Control Panel → TDE assignment acceptance fix
**Why second**  
The POC failure is now diagnosed. The assignment path is not operationally trustworthy until acceptance and feedback are explicit.

**Linked TDE item**  
- `TASK-20260315-CP-TDE-ASSIGNMENT-ACCEPTANCE`

**Current known state**  
- The POC appears to have written directly into canonical TDE state instead of using canonical intake.
- A task could look inserted without visible execution pickup or producer feedback.
- This creates a silent-limbo trust gap.

**Primary fix scope**  
- Introduce canonical assignment adapter / intake path
- Return explicit assignment acceptance states
- Make no-runner / no-binding / blocked conditions visible
- Add observability for inserted-without-pickup failure mode

**Key reference artifacts**  
- `products/task-management/errors/ERR-2026-03-14-control-panel-assignment-silent-limbo.md`
- `products/task-management/06-architecture/TDE_ASSIGNMENT_ACCEPTANCE_CONTRACT_V1.md`
- `products/task-management/06-architecture/TDE_INTAKE_INTERFACE_CONTRACT_V1.md`

**Definition of success today**  
- Fix plan narrowed into the first thin executable slice
- Clear decision on canonical interface path vs any transitional shim
- First implementation slice selected and ready to run

---

### 3. Governance assembly packaging / consumability decision
**Why third**  
Important and now explicitly captured, but lower immediate leverage than boundary enforcement and assignment-path trust repair.

**Linked intake**  
- `intake:governance:2026-03-15:assembly-packaging-decision`

**Definition of success today**  
- Decision frame clarified enough to either create a concrete TDE task or close as a bounded decision record.

---

## Lower-priority signals captured but not promoted first
- Delivery: first real end-to-end pilot evidence pack still missing; gate semantics still too checklist-like.
- Improvement: execution reality still split across canonical and legacy/generated surfaces.
- Interfaces: assembly metadata/docs inconsistency and missing closed-loop downstream verification evidence.

These should remain visible, but not outrank today’s top two execution blockers.

## Recommended immediate working sequence
1. Get Peter approval/decision on Vega boundary narrowing.
2. Execute the Vega runbook and publish the validation artifact.
3. Refresh acceptance sheet and confirm PASS/FAIL honestly.
4. Open the first implementation slice for assignment acceptance.
5. Only then move to governance packaging stance.

## Operator note
The main risk today is not lack of analysis. It is letting documentary intent continue to outrun enforced reality on the top two control surfaces:
- boundary enforcement
- assignment acceptance

That should define the day.
