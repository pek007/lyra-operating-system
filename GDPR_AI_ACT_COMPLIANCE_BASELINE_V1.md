# GDPR_AI_ACT_COMPLIANCE_BASELINE_V1.md

Status: Active (v1)
Owner: Peter (A), Lyra (R)

## Purpose
Create a minimum compliance baseline for GDPR + EU AI Act readiness in Lyra OpenClaw operations.

## Mandatory baseline artifacts
1. AI Act role/classification memo (provider/deployer and risk class assumptions)
2. RoPA-lite (records of processing activities)
3. Vendor/DPA register
4. Retention + deletion schedule linked to processing activities
5. Breach decision log template (72h assessment path)

## Compliance sweep checks (minimum)
- Artifact presence and freshness (review date SLA)
- DPA coverage for in-scope vendors
- Retention evidence generated on cadence
- AI Act classification memo age <= 90 days

## Cadence
- Weekly: compliance quick sweep
- Monthly: GDPR package review
- Quarterly: AI Act classification and risk review

## Guardrail
If any mandatory artifact is missing, compliance status is "incomplete" and remediation task must be opened immediately.
