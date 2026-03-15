# Current Plan

## Current objectives
1. Enforce the OS↔PXS boundary as a real control and close the current acceptance failure on cross-domain reads.
2. Harden the tool and evidence execution surfaces that function as policy-enforcement points.
3. Close the posture → evidence → enforcement loop for PXS consumption with reproducible evidence and explicit promotion checks.
4. Establish the as-code security hardening baseline for Lyra OS and PXS automation surfaces.
5. Keep product-local status, risk, and baseline artifacts aligned with the actual highest-risk execution reality.

## Added as-code rollout focus
- harden GitHub Actions baseline across Lyra OS and PXS
- define minimum workflow-security standard for automation-heavy repos
- identify which evidence artifact classes require tighter schema strictness first
- sequence these changes as enabling controls before broader policy-as-code and execution-bridge work
