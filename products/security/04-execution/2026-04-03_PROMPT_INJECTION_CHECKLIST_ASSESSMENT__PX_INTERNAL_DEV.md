# Prompt Injection Checklist Assessment — `px-internal-dev`

Status: Draft applied assessment
Product: Security (`A-004`)
Owner: Lyra
Date: 2026-04-03

## Purpose
Apply the Prompt Injection Defense Control Checklist to the `px-internal-dev` runtime as the first high-blast-radius assessment target.

## Assessment target
- Agent/runtime: `px-internal-dev`
- Current notable configuration:
  - `sandbox.mode = off`
  - `tools.exec.security = full`
  - `tools.exec.ask = off`
  - `fs.workspaceOnly = true`
- Binding:
  - Telegram account `vega`

## Bottom line
`px-internal-dev` is **not yet aligned** with the desired prompt injection defense posture.

The main issue is not theoretical model risk alone. It is the combination of:
- broad runtime authority
- no ask-gating on exec
- no sandboxing
- a messaging-bound agent context
- a system that can ingest or be influenced by untrusted content paths

This makes `px-internal-dev` a high-priority hardening target.

## Checklist assessment

### 1. Untrusted content handling
- **Partial / unclear** — the broader platform increasingly treats external content as untrusted, but there is no runtime-specific evidence here that `px-internal-dev` has explicit prompt-injection-oriented untrusted-content controls beyond general operating discipline.
- **Finding:** runtime-specific trust-boundary handling is not explicit enough.

### 2. Authority reduction
- **Fail** — `tools.exec.security = full` with `ask = off` means broad authority is present and not narrowly justified in the runtime itself.
- **Partial** — `fs.workspaceOnly = true` is a useful boundary, but not enough to offset unrestricted exec trust.
- **Finding:** authority is broader than the target posture allows for a non-break-glass runtime.

### 3. High-risk action gating
- **Partial / fail** — workspace-level rules conceptually require approval for high-risk actions, but runtime exec configuration bypasses an important technical approval layer by using full trust with ask off.
- **Finding:** policy intent exists, but technical gating is weaker than the desired posture.

### 4. Workflow design
- **Fail / unclear** — there is no evidence in the runtime configuration that high-risk recurring tasks are forced into bounded workflows rather than broad agent latitude.
- **Finding:** the runtime posture appears too open relative to prompt-injection risk.

### 5. Runtime safeguards
- **Fail** — `sandbox.mode = off`
- **Partial** — monitoring/audit signals exist at the platform level, but not enough to treat this as strongly contained.
- **Finding:** runtime containment is materially weaker than the posture we want.

### 6. Review and evidence
- **Pass (partial)** — the risk is now explicitly recognized in Security product artifacts and this assessment creates a first concrete evidence record.
- **Finding:** evidence is improving, but control state is still behind the desired posture.

## Main gaps identified
1. Broad exec trust is active in a runtime that should be treated as prompt-injection-sensitive.
2. Exec ask-gating is disabled where it would provide an important consequence-limiting control.
3. Sandboxing is off.
4. Runtime-specific untrusted-content handling and review are not yet explicit enough.

## Risk judgment
This runtime should be treated as a **high-priority prompt injection consequence-risk surface**.
The main reason is blast radius: if the runtime is influenced through untrusted content or broad task steering, it has too much immediate authority relative to the target posture.

## Recommended next actions
1. Reclassify `px-internal-dev` as break-glass-only if `security=full` truly remains necessary.
2. Otherwise, reduce `tools.exec.security` from `full` toward `allowlist` and restore approval gating.
3. Evaluate whether sandboxing can be turned on for this runtime by default.
4. Add an explicit note in Security execution surfaces that `px-internal-dev` is a prompt-injection-sensitive high-blast-radius path until hardened.

## Current assessment result
**Assessment result: not aligned; hardening recommended before treating posture as acceptable.**
