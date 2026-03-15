---
title: "As-Code Environment Uplift for Lyra OS and PXS"
date: 2026-03-15
source_report: "knowledge/reports/2026-03-15__deepresearch__advancing-an-as-code-environment-across-lyra-os-and-pxs__v1.md"
status: draft-distilled
priority: high
---

# As-Code Environment Uplift for Lyra OS and PXS

## Core judgment
The report is directionally strong.
Its best insight is not “do more as-code,” but:
- treat **Lyra OS as the platform/standards repo**
- treat **PXS as the consuming product/company repo**
- connect them through **shared contracts, policy enforcement, and auditable exchange artifacts**

That fits our current architecture.

## What we should implement

### Implement now
1. **Repo integrity guardrails**
   - fail CI on merge conflict markers
   - broaden forbidden-pattern scanning where useful

2. **GitHub Actions hardening baseline**
   - least-privilege permissions
   - pin third-party actions where practical
   - tighten secret-handling discipline

3. **Make PXS quality gates real**
   - replace placeholder lint/typecheck/build scripts with enforceable checks

4. **Design a shared As-Code Contract Pack**
   - shared schemas or schema fragments
   - shared taxonomy/enums
   - mapping between PXS execution objects and Lyra OS artifact types

### Implement next
5. **Policy-as-code layer for shared governance rules**
   - likely OPA/Conftest or equivalent
   - only after contract surface is cleaner

6. **Cross-repo execution bridge MVP**
   - PXS exports decisions/tasks/evidence bundle
   - Lyra OS validates and ingests it
   - high-risk transformations require explicit approval

7. **Tighten schema strictness for high-value Lyra OS evidence types**
   - reduce permissive artifact shapes where attestation value matters

### Keep as later-stage direction
8. **Unified telemetry / SLO layer**
9. **Supply-chain provenance, SBOM, signing**

## What not to overreact to
- Do not launch a large observability or OpenTelemetry program yet.
- Do not introduce broad policy-as-code everywhere before the contract surface is stable.
- Do not treat every cited best practice as equally urgent.

## Best near-term use of the report
Use it as justification and design input for:
- CI hygiene hardening
- contract-pack design
- policy-pack design
- execution-bridge architecture

## Recommended owner mapping
- **Security**: GitHub Actions hardening, supply-chain posture, policy-risk review
- **Delivery**: repo integrity gates, real CI quality gates, release/evidence discipline
- **Interfaces / Task Management**: shared contract pack and execution bridge shape
- **Control Tower**: sequencing and cross-product coordination
