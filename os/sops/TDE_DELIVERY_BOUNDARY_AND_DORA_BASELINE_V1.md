# TDE Delivery Boundary and DORA Baseline v1

Status: Active
Owner: JOB-PROD-001
Date: 2026-03-04

## Purpose
Define a clear delivery boundary for TDE and establish a baseline DORA-aligned metrics record.

## Delivery boundary (v1)
- **Code integration boundary:** commit landed on `main`.
- **Runtime activation boundary:** behavior exercised by scheduled/runtime execution producing evidence artifact under `knowledge/evidence/`.
- **Release-ready boundary:** both integration + activation are present for the same capability slice.

## Metric mapping (v1)
- Deployment Frequency (proxy v1): count of release-ready slices per week.
- Lead Time for Changes (proxy v1): first commit timestamp for slice -> first activation evidence timestamp.
- Change Failure Rate (proxy v1): share of activation attempts with fail-closed/failure status that require fix-forward.
- Failed Deployment Recovery Time (proxy v1): time from failed activation evidence -> first passing activation evidence.
- Deployment Rework Rate (proxy v1): ratio of fix-forward commits tied to the same slice after first activation.

## Notes
- These are proxy definitions until dedicated deployment automation boundary is introduced.
- Update this SOP once CI/CD environment-based deployment gates are implemented.
