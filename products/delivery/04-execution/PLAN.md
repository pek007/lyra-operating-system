# Current Plan

## Current objectives
1. Keep delivery pathways clear and dependable.
2. Reduce hidden work and verification debt.
3. Improve the system for getting capabilities safely into use.

## Current execution order
1. Define `DELIVERY_UNIT_SCHEMA_V1.yaml` ✅
2. Define state-transition policy v1 ✅
3. Define rendered packet templates v1 ✅
4. Add repo-integrity gates for merge markers and other fail-fast hygiene checks
5. Replace placeholder PXS quality gates with real enforceable checks
6. Run one real Delivery v0.1 pilot end to end and publish the evidence pack
7. Upgrade the Delivery gate from checklist to contract and add at least one machine-checkable validation hook
8. Run the first low-noise weekly Delivery scorecard snapshot and review

## Added as-code rollout focus
- make CI trustworthiness real before increasing automation scope
- treat repo integrity and meaningful quality gates as Delivery-owned enabling controls
- support later policy-pack and execution-bridge work by reducing "green but weak" delivery signals

## Coordination transition
- the interim inbox experiment produced useful learning but is now superseded
- next coordination focus: TDE-native assigned work with assignee wake/notification
- reference: `TDE_ASSIGNED_WORK_WAKEUP_MODEL_V1.md`

## Pilot continuation
- define a compact Delivery-side pilot contract for the One-Iteration TDE UI Pilot
- make explicit the smallest viable delivery shape, minimum production bar, minimum evidence set, and early gate questions
