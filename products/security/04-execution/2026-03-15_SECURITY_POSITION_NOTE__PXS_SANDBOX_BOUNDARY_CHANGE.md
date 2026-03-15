# Security Product position note — pxs sandbox boundary change

Date: 2026-03-15  
Owner: Security Product  
Status: advisory position for decision support

## Purpose

Summarize what Security now knows about using sandboxing to improve the Lyra OS ↔ pxs boundary, what remains uncertain, and what must be proven before any sandbox-based boundary change is approved.

## Position

Security should **not approve sandbox changes merely because sandboxing sounds like the right control**.

Security should approve only a **research-backed, testable boundary design** where sandbox is treated as one possible enforcement layer inside a broader control model.

Current recommended stance:
- **Do not rush into sandbox changes** for pxs.
- **Do continue research and design work** on sandbox as a candidate control.
- **Prefer explicit product/interface delivery from Lyra to pxs over ambient filesystem visibility**.
- **Treat one-gateway sandboxing as hardening inside a single trust boundary, not as full hostile multi-tenant isolation**.

## What we now know

### 1. The historical failures were real and explainable

The documented problems were not vague operator impressions. We have evidence for at least three concrete failure classes:
- **dependency failure**: sandbox-required modes were enabled without Docker available
- **execution-environment mismatch**: missing paths, read-only targets, missing toolchain inside the sandbox
- **boundary-overstatement**: some surfaces were tightened while other effective execution paths still bypassed the intended boundary

This means the correct lesson is not “sandbox never works.” The correct lesson is:
**sandboxing was previously introduced without full runtime readiness, full surface closure, or disciplined rollout controls.**

### 2. Sandbox is not a magic boundary by itself

OpenClaw’s own trust model matters here.
Within a single gateway, sandboxing can reduce blast radius and improve containment, but it does **not automatically create a strong hostile-tenant boundary**.

That implies two valid but different designs:
- **strong design**: separate gateways / OS users / hosts, then explicit capability flow
- **interim practical design**: one gateway, separate agents/workspaces, restrictive tool policy, careful sandboxing, and no Lyra mounts into pxs

Security should be explicit about which design is being pursued, because the approval standard differs.

### 3. The old “sandbox lock-in” experience is now better understood

The new research sharpens the prior diagnosis into a practical model:
- **workspace clamp** — sandbox cannot see the expected repo/workspace
- **tool-policy clamp** — sandbox-specific allow/deny policy silently removes needed tools
- **environment clamp** — minimal image, no network, missing binaries, wrong setup assumptions

That is useful because it turns “sandbox made the agent useless” from folklore into a checklist of specific conditions to verify.

### 4. Productized capability flow remains the right direction

The strongest recurring theme across the research base is that pxs should consume Lyra outputs as **published products/interfaces** rather than through broad file visibility into Lyra internals.

This remains the most security-coherent direction regardless of whether the eventual runtime pattern is:
- shared managed skills
- service endpoints / aaS
- versioned packs / policies / templates
- or a stronger split-gateway model

## What remains uncertain

Security should treat the following as unresolved until proven with direct evidence:

1. **Target trust model**
   - Are we hardening within one trusted operator boundary?
   - Or are we trying to create something closer to adversarial tenant separation?

2. **Target operating model for pxs**
   - Should pxs edit its own workspace directly?
   - Should pxs consume only published skills/packs/services?
   - Is sandbox meant to support normal daily operation, or only limit certain execution surfaces?

3. **Exact enforcement surface**
   - Which tools must be inside the sandboxed boundary?
   - Is `exec` included and constrained sufficiently?
   - Are there any remaining host-side escape paths that would invalidate the security claim?

4. **Workspace visibility model**
   - `workspaceAccess: none`, `ro`, or `rw`?
   - What does pxs actually need to read/write to function?
   - Which binds, if any, are allowed?

5. **Functional runtime model**
   - Which image will be used?
   - Which binaries must exist in the container?
   - Is network intentionally disabled?
   - If not, what exfiltration posture is being accepted?

6. **Operational safety of rollout**
   - What preflight checks block unsafe activation?
   - What canary proves the design works before broader rollout?
   - What rollback path returns the system to a known-good state quickly?

## What must be proven before approval

Security should require a decision pack that proves all of the following.

### A. The security claim is precise
The proposal must say exactly what claim is being made, for example:
- “pxs cannot read Lyra workspace files through normal fs tools”
- “pxs cannot reach Lyra workspace via exec either”
- “this is hardening within one gateway, not full tenant isolation”

No vague claims like “sandboxed so safe.”

### B. Effective runtime closure is demonstrated
The proposal must show that all material execution surfaces align with the intended boundary, including:
- fs tools
- exec
- process/runtime tools
- binds
- workspace access mode
- elevated/host escape hatches

A boundary claim fails if one major surface still bypasses it.

### C. The sandbox is functional enough for the intended job
Before approval, the target runtime must be demonstrated to support the real pxs workflow, including:
- required repo/path visibility
- required write paths if applicable
- required binaries/toolchain
- any required network posture
- expected skill/policy availability inside the sandboxed context

### D. Preflight and drift controls exist
At minimum, the change pack should include evidence for:
- Docker readiness
- effective sandbox config inspection
- container/image/config drift check
- forced recreate when config/image changed
- explicit rollback plan
- canary results

### E. Boundary tests pass end-to-end
Security should require explicit tests proving both sides:
- **positive**: pxs can still do the intended work
- **negative**: pxs cannot inspect or mutate Lyra internals through the covered surfaces

## Recommended next decision path

1. **Do not approve a broad sandbox posture change yet.**
2. **Approve a narrow Security research/design phase** that produces a formal decision pack.
3. **Require the decision pack to compare at least two options**:
   - one-gateway hardened design
   - split-trust design (separate gateway/OS user/host)
4. **Use productized capability flow as the design anchor** for Lyra → pxs interaction.
5. **Approve implementation only after canary evidence and end-to-end boundary tests pass.**

## Decision-ready summary

Security’s current position is:

> Before any sandbox changes are made for the pxs interface, Security should complete extensive research and require direct evidence on trust model, enforcement closure, runtime functionality, and rollout safety. The known past failures are now better understood, but that increases the burden for disciplined design; it does not reduce it.

## Key supporting artifacts

- `products/security/04-execution/2026-03-15_SANDBOX_USAGE_RESEARCH_MEMO.md`
- `knowledge/evidence/2026-03-03__inc-2026-003__openclaw-sandbox-docker-regression-investigation.md`
- `knowledge/reports/2026-03-07__deepresearch__sandbox-governance-and-operations-framework-for-openclaw-with-docker-sandboxes__v1.md`
- `knowledge/reports/2026-03-07__deepresearch__operational-separation-between-lyra-os-and-pxs-in-openclaw__v1.md`
- `knowledge/reports/2026-03-15__deepresearch__secure-scalable-boundary-between-lyra-os-and-pxs-in-openclaw__v1.md`
