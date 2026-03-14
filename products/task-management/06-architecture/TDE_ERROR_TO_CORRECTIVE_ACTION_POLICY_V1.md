# TDE Error-to-Corrective-Action Policy v1

Status: Draft active
Owner: Peter + Lyra
Product: Task Management (`A-007`)
Date: 2026-03-14
Related:
- `ERROR_REPORTING_STANDARD_V1.md`
- `ERROR_REPORT_TEMPLATE_V1.md`
- `CLOSED_LOOP_IMPROVEMENT_MODEL_V1.md`
- `products/task-management/06-architecture/TDE_INTAKE_INTERFACE_CONTRACT_V1.md`
- `schemas/tde_error_report/v1.0.0.schema.json`
- `tools/tde_error_report_adapter.py`

## Purpose
Define the bridge between structured error/control reporting and canonical TDE corrective action handling.

This policy exists to ensure that a meaningful issue does not stop at description.
If an issue requires corrective or preventive work, that work must enter TDE in canonical form.

## Core rule
When a meaningful issue is reported:
1. capture the issue in the appropriate error/control artifact
2. if corrective or preventive action is required, create or update canonical TDE work through the intake contract

Interpretation:
- the error report is the learning/control layer
- TDE is the action/closure layer
- both should be linked when meaningful action is required

## Ownership rule
Follow the existing ownership model:
- product-local issue -> owning product owns the error report and the corrective action path
- cross-product/system issue -> shared/system owner owns the error report and any shared corrective action path

This policy does not justify a parallel central action layer.
Corrective execution still belongs in TDE.

## Mapping rule
### Error artifact
Use the error-reporting standard to answer:
- what happened
- why it matters
- who owns it
- what changed structurally

### TDE corrective action
Use TDE canonical intake to answer:
- what work must now be done
- by whom / in which scope
- what needs tracking, follow-through, and closure

## Recommended intake-class mapping
### `work`
Use when the corrective action is bounded and directly actionable.

Examples:
- update process artifact
- implement guardrail/fix
- add verification step
- repair broken interface

### `decision`
Use when a meaningful judgment or approval is required before corrective work can proceed.

Examples:
- trade-off on remediation approach
- architectural choice
- authority/risk boundary decision

### `incident`
Use when the issue requires urgent operational handling.

Examples:
- active failure
- control break with live risk
- immediate containment/remediation need

### `direction`
Use only when the issue reveals a larger systemic change need that is not yet execution-ready.

## Minimum linkage rule
If action is required, the system should preserve at least:
- error id
- source reference
- owning product/scope
- linked evidence refs
- linked corrective action refs

A meaningful issue without a linked action path is incomplete.
A corrective action without a linked issue artifact is weak if the issue warranted formal reporting.

## Producer adapter rule
Meaningful structured error reports should have an adapter path into canonical TDE intake.

That adapter should:
- validate the source error report
- classify the correct intake class
- preserve provenance and ownership
- carry corrective-actions text and linked artifacts into canonical intake shape
- avoid silently treating all error reports as urgent incidents

## Initial v1 stance
Default mapping for structured error reports should be conservative:
- active urgent failure -> `incident`
- otherwise if explicit corrective actions exist -> `work`
- if corrective path requires higher-order judgment -> `decision`

This keeps the default action path operational rather than merely descriptive.

## Bottom line
If an issue should be fixed, the fix should exist in TDE canonically.

Error reporting explains the issue.
TDE carries the corrective execution and closure path.
