# TDE PO Nightly Report Adapter Contract v1

Status: Draft active
Owner: Peter + Lyra
Product: Task Management (`A-007`)
Date: 2026-03-14
Related:
- `products/task-management/06-architecture/TDE_INTAKE_INTERFACE_CONTRACT_V1.md`
- `governance/TDE_PRODUCT_OWNER_OPERATING_INSTRUCTION_V1.md`
- `schemas/tde_po_nightly_report/v1.0.0.schema.json`
- `schemas/tde_intake_packet/v1.0.0.schema.json`
- `tools/tde_po_nightly_report_adapter.py`

## Purpose
Define the first producer adapter for the nightly product-owner report flow.

This adapter translates a structured nightly product-owner report into a canonical TDE intake packet so the signal can enter TDE through a machine-valid path rather than chat interpretation alone.

## Why this adapter exists
A nightly product-owner report is operationally important, but it is usually not itself a task.

Per TDE intake policy, it should normally enter as a `signal` and only later be promoted into:
- updated existing work
- new work
- a decision item
- or recorded/no-action state

This contract makes that path explicit.

## Producer chain
The intended chain is:
1. product owner produces a structured nightly report
2. control panel may enrich/prioritize the report
3. the adapter emits a canonical `tde_intake_packet`
4. TDE triages the packet under `intake_class = signal`

## Input artifact
Canonical input artifact:
- `tde_po_nightly_report@1.0.0`

Defined in:
- `schemas/tde_po_nightly_report/v1.0.0.schema.json`

## Output artifact
Canonical output artifact:
- `tde_intake_packet@1.0.0`

Defined in:
- `schemas/tde_intake_packet/v1.0.0.schema.json`

## Required semantic mapping
### Output class
The adapter must emit:
- `intake_class = signal`

### Provenance
The adapter must preserve:
- original report id
- original source reference
- product id / product name
- product owner
- report date
- any control-panel enrichment that materially affects triage

### Signal typing
The adapter should emit `signal_types` based on report contents.

Recommended mapping:
- always include `status`
- include `blocker` when blockers are present
- include `risk` when risks are present
- include `priority_proposal` when proposed TDE actions or control-panel priority are present

### Priority hint
The adapter should map priority as follows:
- if `control_panel_priority` exists, use it
- else if `overall_health = red`, use `high`
- else if `overall_health = yellow`, use `medium`
- else default to `unspecified`

This remains advisory, not authoritative.

## Canonical packet shape expectations
The output packet should set:
- `artifactType = tde_intake_packet`
- `schemaVersion = 1.0.0`
- `intake_id = intake:<product_id>:<report_date>:<report_id>`
- `intake_class = signal`
- `source_system = tde_po_nightly_report_adapter`
- `source_type = report`
- `source_reference = <source_reference from report>`
- `submitted_by = <product_owner>`
- `workspace_scope = <consumer workspace>`
- `product_scope = <product_id>`
- `proposed_action = triage_nightly_po_signal`

## Body requirements
The adapter output body should preserve a structured summary of:
- overall health
- summary
- top priorities
- blockers
- risks
- proposed TDE actions
- report metadata

The adapter must not silently flatten away blocker type or risk meaning.

## Related entities guidance
The adapter should include at least:
- the product as a related entity
- any linked TDE ids referenced in blockers when present

## Evidence links guidance
The adapter should pass through report evidence links directly unless normalization is required.

## Validation requirements
The adapter must validate:
1. input report against `tde_po_nightly_report@1.0.0`
2. output packet against `tde_intake_packet@1.0.0`

Invalid input must fail closed.
The adapter must not emit a canonical packet from an invalid source report.

## Control Panel enrichment rule
The Control Panel may enrich the report with prioritization or presentation metadata, but must not silently change:
- report identity
- product identity
- blocker meaning
- risk meaning
- source provenance

If enrichment materially changes urgency or routing recommendation, that enrichment should remain inspectable in the output body.

## Minimal example interpretation
If a nightly report says:
- health = yellow
- 2 blockers
- 1 risk
- 3 proposed TDE actions

Then the adapter should normally emit:
- `intake_class = signal`
- `signal_types = [status, blocker, risk, priority_proposal]`
- a structured body preserving the report content
- `priority_hint = medium` unless overridden by control-panel enrichment

## Implementation note
The first adapter implementation now exists at:
- `tools/tde_po_nightly_report_adapter.py`

This implementation is the first thin as-code bridge from a real upstream operational producer into the canonical TDE intake contract.
