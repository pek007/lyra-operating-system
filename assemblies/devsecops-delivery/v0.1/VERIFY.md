# Verification — DevSecOps Delivery v0.1

## Goal
Verify that Delivery v0.1 can be activated and used credibly in a consuming environment with explicit evidence, gate use, and rollback discipline.

## Verification baseline
A successful VERIFY cycle should demonstrate:
- the distribution lane used is explicit
- the target scope is explicit
- the Delivery gate was applied to one real or representative change
- evidence outputs were captured
- rollback notes were captured
- pass/fail outcome is explicit

## Verification procedure
### 1. Confirm distribution lane
Record one of:
- pinned assembly lane active
- interim copy lane active

If interim copy lane is used, confirm provenance and lock tracking are present.

### 2. Select one representative change
Choose one real or representative release/change item that is small enough to verify end to end.

### 3. Apply the Delivery gate
Run:
- `artifacts/ops-pack/DELIVERY_GATE_CHECKLIST.md`

Record:
- risk class
- checks performed
- evidence generated
- rollback path used/validated

### 4. Produce evidence pack
Capture at minimum:
- change identifier / scope
- gate completion status
- evidence references
- rollback notes
- pass/fail verdict
- reviewer/operator if relevant

### 5. Record verification outcome
The VERIFY run should end with one of:
- PASS
- FAIL
- PARTIAL / INCOMPLETE

## Pass criteria
PASS requires all of the following:
- distribution lane explicit
- gate applied
- evidence outputs captured
- rollback notes captured
- no material unresolved ambiguity about the verification result

## Fail criteria
FAIL if any of the following occur:
- delivery lane unclear
- gate not actually applied
- evidence missing
- rollback path not credible enough for the tested change
- verification result not inspectable from artifacts

## First pilot expectation
The first real Delivery v0.1 pilot should produce one canonical verification artifact/evidence pack that can be cited in product review and future activation work.
