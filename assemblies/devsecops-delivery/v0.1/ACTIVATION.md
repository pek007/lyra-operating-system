# Activation — DevSecOps Delivery v0.1

## Purpose
Activate the Delivery v0.1 assembly in a consuming environment such as PXS so that release/change work follows explicit delivery gates, evidence capture, and rollback discipline.

## Activation rule
This assembly is only "real" when it is:
1. distributed into the consumer scope through a known lane
2. used on at least one real or representative change
3. verified through the Delivery VERIFY baseline
4. backed by evidence and rollback notes

## Supported activation lanes
### Preferred lane
- version-pinned assembly distribution into the consumer workspace

### Temporary lane
- interim copy lane, only while pinned-lane distribution is not yet active
- when using interim copy, also follow:
  - `artifacts/ops-pack/INTERIM_COPY_SYNC_PROTOCOL.md`

## Activation prerequisites
Before use on a change, confirm:
- consuming workspace and scope are explicit
- the relevant work/change has scope and risk classification
- acceptance criteria or equivalent completion bar is explicit
- a verification/evidence path exists
- rollback path is credible enough for the change class

## Activation steps
1. Install or copy the Delivery artifacts into the target consumer scope through the approved lane.
2. Record provenance/lock information if using an interim or pinned lane.
3. Use `artifacts/ops-pack/DELIVERY_GATE_CHECKLIST.md` on one representative real or simulated change.
4. Capture the required evidence outputs.
5. Capture rollback notes.
6. Run `VERIFY.md` for the Delivery assembly.
7. Record the resulting verification artifact/evidence pack.

## Minimum evidence expectations
A valid first activation should produce evidence covering:
- distribution lane used
- target scope / change scope
- gate applied
- checks/evidence produced
- rollback notes
- pass/fail outcome

## Failure rule
If the gate cannot be applied, evidence cannot be produced, or rollback is not credible enough for the change class, activation should be treated as failed or incomplete rather than silently accepted.

## Related artifacts
- `VERIFY.md`
- `artifacts/ops-pack/DELIVERY_GATE_CHECKLIST.md`
- `artifacts/ops-pack/INTERIM_COPY_SYNC_PROTOCOL.md`
