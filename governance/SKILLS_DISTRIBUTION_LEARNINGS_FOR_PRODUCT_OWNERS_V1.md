# Skills Distribution Learnings for Product Owners v1

Status: Active
Owner: Lyra
Date: 2026-03-09
Source: `knowledge/reports/2026-03-09__deepresearch__identifying-and-implementing-skills-in-openclaw-for-lyra-os-and-pxs__v1.md`

## Purpose
Provide a short, reusable conclusion for Product Owners on how Lyra OS should use OpenClaw Skills as a product-distribution mechanism.

## Short conclusion
The report supports using OpenClaw Skills as a **distribution surface for Products**, but only if we treat them as **versioned, policy-governed capability modules**, not as loose prompt add-ons.

## What we should implement now
1. Define a **Lyra Skill Contract** for first-party skills:
   - stable name
   - version
   - owner
   - risk class
   - JSON input/output contract
   - explicit permission requirements
   - structured error codes
   - resource limits
   - observability/evidence outputs

2. Start with **deterministic, low-coupling skills**:
   - release envelope builder
   - activation execution receipt
   - milestone snapshot
   - owner gate packet
   - observation/work-packet validators

3. Ship skills as **`skill-pack` artifacts inside product assemblies**.

4. Use **pinned versions and explicit promotion/rollback** when distributing skills to PXS or other consumer workspaces.

5. Keep **hard enforcement logic** in plugins/services where bypass must not be possible; do not rely on `SKILL.md` guidance alone for critical controls.

## What we should not do
- Do not auto-update production skills.
- Do not treat public/community skills as trusted by default.
- Do not start with the most stateful or high-side-effect TDE mutation paths.
- Do not blur Lyra OS and PXS workspace boundaries while distributing skills.

## Why this matters
This gives us a native OpenClaw-compatible way to distribute reusable product capabilities while preserving:
- boundary control
- version pinning
- rollback
- approvals
- auditability

## Link
See full report:
`knowledge/reports/2026-03-09__deepresearch__identifying-and-implementing-skills-in-openclaw-for-lyra-os-and-pxs__v1.md`
