# Security Research — Implement Now

Date: 2026-03-14
Source: deep research review of A-004 Security

## Immediate implementation set
1. Make OS↔PXS boundary enforcement the top security priority and close the current FAIL on cross-domain reads.
2. Harden the tool/evidence execution surfaces that currently act as policy-enforcement points, especially shell-based evidence ingestion and domain-unaware execution paths.
3. Close the posture → evidence → enforcement loop for PXS consumption with committed/reproducible evidence and explicit promotion checks.
4. Align product-local plan, priorities, risks, metrics, and interfaces to the actual highest-risk execution reality.

## Defer / later
- broader alias/path discoverability work if still needed for older A-004-style references
- larger TDE/runtime enforcement expansion beyond the highest-leverage boundary and high-risk action controls
