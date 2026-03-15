# Sandbox usage in this OpenClaw / Lyra OS environment — research memo

Date: 2026-03-15  
Owner: Security research pass  
Scope: decision-grade review of how sandboxing is supposed to work here, what failures are documented, likely root-cause categories, what must be true before retry, and why future failures could be avoided.

## Executive summary

The evidence base is good enough to support a near-term Security decision, though it is partly fragmented across incident notes, governance records, acceptance sheets, and research reports rather than a single canonical runtime spec.

**Bottom line:**
- In this environment, sandboxing is supposed to be the **runtime enforcement layer** for tool execution, implemented through **Docker-backed containers** managed by OpenClaw, with behavior determined by sandbox mode, workspace visibility, and optional bind mounts.
- The documented historical failures were **real and material**. The clearest one is the 2026-03-03 regression where sandbox-required modes were enabled **without Docker available**, producing repeated failures across cron lanes and follow-on path/toolchain issues inside the sandboxed environment.
- There is also a second, distinct failure class: **boundary claims without full runtime enforcement**. Current Vega/PXS evidence shows that even after narrowing filesystem tools to `workspaceOnly=true`, the boundary still fails in practice because `exec` remains unsandboxed and unrestricted enough to reach host paths.
- The main pattern is not “sandbox is bad.” It is: **sandbox was introduced or reasoned about without deterministic preflight, without end-to-end surface coverage, and without a stable operating model for pathing, mounts, toolchain, and change control**.
- Security should **not** recommend another sandbox retry as a general posture change yet. A retry becomes credible only after dependency readiness, effective-config verification, canary validation, runtime-surface closure, and rollback discipline are all proven.

My recommendation: **do not treat sandbox as the next immediate fix for Vega/PXS boundary work.** For that boundary, the urgent issue is broader runtime enforcement design, not merely flipping sandbox on. Sandbox can be retried later as part of a governed, narrow, testable change set.

---

## 1. How sandbox is supposed to work here

## Evidence

Across the workspace, OpenClaw sandboxing is consistently described as:
- a **Docker-based tool execution isolation layer**, with the gateway remaining on the host and tools running in a container (`knowledge/reports/2026-03-07__deepresearch__sandbox-governance-and-operations-framework-for-openclaw-with-docker-sandboxes__v1.md`)
- a control plane distinct from tool policy and elevated/host execution (`docs/architecture/openclaw-agent-deployment-report-2026-02-28.md`; `knowledge/reports/2026-03-01__research__research-report-ai-agent-deployment-and-jobs-vs-agents-in-openclaw__v1.md`)
- something that only becomes a hard boundary when the runtime config actually enforces it; workspace files and prompts are guidance, not enforcement (`docs/architecture/openclaw-agent-deployment-report-2026-02-28.md`; multiple March 1–7 reports)

The intended mechanics described in the evidence are:
1. OpenClaw receives a request and routes it to an agent/session.
2. Tool policy decides whether a tool is callable.
3. If sandboxing is enabled for that context, tool execution occurs in a Docker sandbox.
4. What the sandbox can see depends on:
   - `sandbox.mode`
   - sandbox scope
   - workspace access mode (`none` / `ro` / `rw`)
   - explicit Docker bind mounts
5. Binds and workspace visibility determine whether repos or host paths are visible inside the container.
6. `exec` can still be an escape hatch if it is configured to run on the host or in elevated mode.

There is also explicit internal guidance, post-incident, that:
- the **main lane** should keep `agents.defaults.sandbox.mode=off` unless there is an explicit change window, canary/isolated validation, and rollback plan (`knowledge/evidence/2026-03-04__ops-reliability-s27-sandbox-guardrail.md`)
- sandbox-related changes are treated as **high-risk runtime changes** under the broader config-change governance posture

## Interpretation

In this environment, sandbox is supposed to be:
- a **runtime containment mechanism for tools**, not a general symbolic “safe mode”
- dependent on **Docker availability and correct container configuration**
- only as strong as the **least-restricted active execution surface**

That last point matters most. A boundary is not genuinely sandboxed if one tool surface remains unsandboxed and broad enough to bypass the intended restriction.

---

## 2. What documented failures or problems we have had

## Evidence

### A. 2026-03-03 sandbox/Docker regression was the major documented failure

The clearest incident record is:
- `knowledge/evidence/2026-03-03__inc-2026-003__openclaw-sandbox-docker-regression-investigation.md`

That record shows:
- `agents.defaults.sandbox.mode` was changed into sandbox-requiring modes (`all`, later `non-main`)
- Docker was not installed or not available in PATH
- the gateway produced repeated failures: _“Sandbox mode requires Docker, but the 'docker' command was not found in PATH...”_
- cron/autonomous lanes kept running and amplified the issue
- repeated config writes and gateway restarts extended the disturbance window

The same incident also recorded secondary failures after sandboxed/isolated execution paths were attempted:
- `Sandbox FS error (ENOENT)` for memory/workspace targets
- `Sandbox path is read-only`
- missing binaries/tools inside the execution environment: `git: not found`, `python3: not found`, `openclaw: not found`

### B. Pathing / context-split problems are documented as a real class

The 2026-03-07 sandbox governance report describes a recurring pattern of:
- host shows expected repos
- active runtime is in a fresh/stale sandbox workspace
- expected repo paths are missing
- operator trust collapses because host and sandbox no longer match

The same report states that a “minimal sandbox containing only bootstrap files” is often expected when `workspaceAccess: "none"` is used.

That means at least some previously experienced “empty or wrong sandbox” symptoms were not necessarily random bugs; they could also have been **policy outcomes that were not operationally understood or made visible**.

### C. Boundary-enforcement failures remain live even after partial tightening

For Vega/PXS specifically:
- the original acceptance sheet recorded that Vega could directly list `/Users/lyra/.openclaw/workspace` (`governance/VEGA_ACCEPTANCE_TEST_RUN_SHEET_V1.md`)
- the 2026-03-15 enforcement-surface check confirmed that this was config-backed, not just historical accident, because `px-internal-dev.tools.fs.workspaceOnly=false` and `sandbox.mode=off` were live (`products/task-management/04-execution/VEGA_PXS_BOUNDARY_ENFORCEMENT_SURFACE_CHECK_2026-03-15.md`)
- after a later hardening change set `px-internal-dev.tools.fs.workspaceOnly=true`, the post-change validation still concluded E2 must remain FAIL because `exec` still allowed unsandboxed host-path access (`products/task-management/04-execution/VEGA_PXS_BOUNDARY_POST_CHANGE_VALIDATION_2026-03-15.md`)

This is not the same as the March 3 outage. It is a different failure mode:
- **partial enforcement on one tool surface while another surface still bypasses the intended boundary**

### D. Security warnings have persisted because the environment remains partly unsandboxed

Security audit evidence repeatedly shows:
- current/trailing posture includes contexts with `sandbox=off`
- current/trailing posture includes runtime/process tools in group-capable contexts
- current/trailing posture included `px-internal-dev` with `fs.workspaceOnly=false` until today’s tightening
- the accepted model has therefore been a **trusted-operator boundary**, not hostile multi-user isolation (`knowledge/evidence/latest-security-audit.json`; `governance/TRUST_BOUNDARY_POLICY_RECORD_2026-03-04.md`; `governance/GO_RISK_DECISION_2026-03-06.md`)

## Interpretation

The documented problem history is not one single bug. It includes at least three distinct classes:
1. **Dependency failure**: sandbox enabled without Docker
2. **Execution-environment mismatch**: wrong/missing files, read-only paths, missing tools inside sandbox
3. **Boundary-overstatement**: claiming isolation while another runtime surface still bypasses it

---

## 3. Likely root-cause categories

This section combines direct evidence with inference. I am labeling them separately.

## Evidence-backed categories

### 3.1 Dependency-readiness failure

Direct evidence: March 3 incident enabled sandbox-required modes while Docker was unavailable. This is the most explicit root cause on record.

### 3.2 Change-control failure

Direct evidence:
- repeated config writes changed sandbox mode multiple times during live operations on March 3
- repeated gateway restarts extended the outage window
- post-incident controls explicitly added a preflight script and a rule that main lane should keep sandbox off unless in a change window with canary and rollback

This strongly supports: sandbox failure was not just technical incompatibility; it was **unsafe runtime change practice**.

### 3.3 Pathing / visibility-model mismatch

Direct evidence:
- `ENOENT` errors
- read-only path errors
- missing expected repos in sandbox
- research artifact explicitly documenting silent context split between host and sandbox

This indicates a recurring mismatch between:
- where operators thought files lived
- what the sandbox could actually see
- what access mode/binds actually provided

### 3.4 Toolchain/image mismatch

Direct evidence from incident file:
- `git`, `python3`, and `openclaw` were reported missing inside the execution environment

That implies sandbox image/runtime assumptions were not aligned with what workloads expected.

### 3.5 Incomplete enforcement-surface design

Direct evidence from Vega/PXS records:
- filesystem-tool hardening improved the boundary
- but unsandboxed `exec` still left host-path access available

This shows a structural design issue: **controls were applied per surface, but the security claim required all material execution surfaces to align**.

## Inference-backed categories

### 3.6 Weak runtime observability of effective sandbox state

Inference: several artifacts recommend `openclaw sandbox explain`, `openclaw sandbox list`, and `openclaw sandbox recreate`, but the operational record here does not show those primitives becoming a normal daily control loop before or during the incident.

Likely consequence: operators may have been reasoning from intended config rather than the actual effective runtime/container state.

### 3.7 Policy-to-enforcement gap

Inference, but strongly supported by repeated research findings: the workspace contains strong governance language about sandboxing, isolation, and default-safe postures, but many artifacts also warn that prose is not enforcement. The repeated persistence of boundary failures suggests the system has often had **good declared policy, weaker mechanical closure**.

### 3.8 Overloading sandbox as both security control and workflow substrate

Inference: some failures appear to come from treating sandboxing simultaneously as:
- a trust-boundary hardening mechanism
- a change in normal developer/runtime ergonomics

Those are related, but not identical. If the workflow substrate is not ready for sandboxed execution, flipping sandbox to harden trust boundaries can break normal operations before the security benefit is actually realized.

---

## 4. What would have to be true before sandbox could be retried safely

This is the key decision section.

## Minimum prerequisites

### 4.1 Docker dependency readiness must be proven, not assumed

Must be true:
- Docker is installed
- `docker` is in PATH for the actual gateway runtime context
- the preflight gate passes before any sandbox mode change

Existing evidence already created the first thin control here:
- `tools/openclaw_sandbox_preflight.py`

But that script is only a basic dependency check. It is necessary, not sufficient.

### 4.2 Effective sandbox configuration must be inspectable and captured

Must be true:
- Security/Operations can show the effective sandbox configuration for the target context
- sandbox mode, scope, workspace access, and binds are known before the change
- container/config drift is checked, not guessed

The research record repeatedly points to:
- `openclaw sandbox explain`
- `openclaw sandbox list`
- `openclaw sandbox recreate`

A safe retry should require captured evidence from those commands as part of the change pack.

### 4.3 Required files and repos must be visible in the intended way

Must be true:
- for the candidate workflow, Security knows whether workspace access should be `none`, `ro`, or `rw`
- any required repos or paths are either under the canonical workspace root or mounted explicitly and minimally
- there is no reliance on undocumented host path assumptions or symlink magic

### 4.4 Required toolchain must exist inside the sandbox image/runtime

Must be true:
- every critical workflow has a minimal toolchain check inside sandbox
- required binaries actually exist (`git`, `python3`, `openclaw`, etc., as applicable)
- failures are fail-closed in preflight/canary, not discovered by production automation

### 4.5 Sandbox retry must be narrow and canaried

Must be true:
- no global/default posture flip first
- retry occurs on a single low-risk lane, agent, or test scenario
- high-autonomy cron loops are paused or isolated during the first change
- rollback path is prepared in advance

This is directly consistent with the post-incident guardrail.

### 4.6 The full runtime surface must be evaluated, not just filesystem tools

Must be true:
- Security defines the boundary claim precisely
- if the claim is “no direct host cross-domain reads,” then **all relevant surfaces** must be covered, especially `exec`
- a retry cannot be called successful if `fs` is sandboxed but `exec` still bypasses the same boundary

This is the critical lesson from Vega/PXS.

### 4.7 Sandbox use case must be explicit

Must be true:
- are we retrying sandbox for **availability-safe shared/group trust hardening**, or for **developer workflow isolation**, or for **Vega/PXS boundary enforcement**?
- each of these has different access/mount/toolchain requirements

Without an explicit use case, sandbox will likely be retried too broadly and then judged against the wrong success criteria.

---

## 5. Why future failures could be avoided

Future failures are avoidable if sandbox moves from “aspirational posture” to “governed runtime product.”

## Evidence-backed reasons for optimism

### 5.1 There is already a post-incident guardrail

The environment now has:
- a preflight script checking Docker availability
- a documented rule that main lane remains `sandbox.mode=off` unless there is an explicit change window + canary + rollback

That does not solve everything, but it directly targets the March 3 trigger condition.

### 5.2 The environment now has clearer diagnosis of the boundary problem

The Vega/PXS boundary work has already improved precision:
- the live blocker was narrowed from a vague “boundary issue” to specific config-backed control surfaces
- post-change validation correctly refused to overstate success when `exec` remained open

That is exactly the kind of precision needed to avoid repeating a “partial fix declared as full boundary.”

### 5.3 The workspace contains solid conceptual guidance on sandbox operations

The March 7 research report is unusually explicit about:
- workspace access policy
- bind-mount discipline
- recreate/drift management
- session vs agent scope choices
- canaries and preflight

If converted into actual operating steps, that should materially reduce recurrence.

## Conditions under which future failures are avoidable

Future failures become much less likely if:
1. sandbox retries are **narrow, evidence-captured changes**, not default flips
2. effective runtime state is checked before and after change
3. workload compatibility is tested in-canary before autonomous loops resume
4. Security validates the **entire runtime surface**, not just one tool class
5. trust-boundary design is separated from convenience/developer ergonomics

## Remaining limitation

Even if all of the above is done well, OpenClaw’s own documented model is still **not a hostile multi-tenant hard-isolation platform on one shared gateway**. Multiple artifacts repeat that one gateway is fundamentally one trusted-operator boundary.

So future failures can be reduced substantially, but sandbox should not be sold internally as a perfect substitute for:
- separate gateways
- separate OS users/hosts
- stricter trust-boundary splits where needed

---

## Implications for Vega/PXS boundary work right now

This is the practical Security conclusion for the current portfolio bottleneck.

### What the evidence says

Right now:
- the earlier broad `px-internal-dev.tools.fs.workspaceOnly=false` exception was real and mattered
- tightening that to `true` improved the filesystem-tool boundary
- but `sandbox.mode=off` plus unsandboxed/host-capable `exec` means the overall runtime boundary is still not deny-by-default

### Security implication

For the Vega/PXS boundary, **sandbox retry is not the immediate first-order move** unless it is part of a broader runtime-surface redesign.

Why:
- the live blocker is not simply “sandbox is off”
- the live blocker is that the claimed no-direct-read boundary is still not fully enforced across the total execution surface

### Recommended stance right now

Security should say:
- **do not mark Vega/PXS boundary PASS yet**
- **do not claim sandbox as the fix by itself**
- first decide which of these is the real desired boundary:
  1. filesystem-tool-only isolation, or
  2. true runtime no-direct-host-read isolation

If the desired boundary is (2), then current evidence says the remaining control work must include `exec` posture and/or actual sandboxed execution design, not only `fs.workspaceOnly`.

### Practical implication for downstream PXS work

Until that is resolved, downstream consumption should assume:
- the boundary is **partially tightened but not fully enforced**
- handoff-only claims remain stronger in governance intent than in runtime guarantee
- Security sign-off should remain conditional

---

## What Security needs to answer before any sandbox retry

1. **What exact problem is the retry solving?**  
   Shared/group trust hardening, Vega/PXS cross-domain boundary enforcement, or sandboxed development ergonomics?

2. **What is the boundary claim?**  
   “Filesystem tools limited to workspace” is materially different from “no direct host path access from this runtime.”

3. **Which execution surfaces must conform?**  
   At minimum: `fs` tools, `exec`, elevated paths, browser/web side effects if relevant.

4. **What is the candidate sandbox profile?**  
   Mode, scope, workspace access, binds, image/toolchain, expected writable paths.

5. **Is Docker definitely available in the actual gateway runtime context?**  
   Not just on the host in general.

6. **What files/repos must the workflow see, and how will they be made visible?**  
   Under workspace root, or explicit binds, with clear read/write modes.

7. **What minimal toolchain must exist inside the sandbox?**  
   Which binaries are mandatory for the target workflow?

8. **What is the canary workflow?**  
   One narrow task, one lane, with explicit success/failure criteria.

9. **What automation must be paused during first retry?**  
   Especially autonomous cron loops that can amplify failure.

10. **What evidence pack will be captured before declaring success?**  
    Effective config, drift status, runtime health, canary outputs, and explicit negative tests.

11. **What is the rollback path and who owns the window?**  
    This must be decided up front.

12. **If the goal is true hard trust separation, why is sandbox preferred over separate gateway / separate OS-user boundary?**  
    Security should explicitly answer that trade-off rather than assuming sandbox is enough.

---

## Decision-oriented conclusion

The current record supports a clear Security position:

- **Sandboxing here is intended to be a real runtime enforcement mechanism, but only when Docker, workspace visibility, mounts, toolchain, and execution-surface closure are all aligned.**
- **The environment has already experienced a serious sandbox-related regression caused by enabling sandbox without dependency readiness and while autonomous jobs remained active.**
- **The current Vega/PXS boundary evidence shows a second, equally important lesson: partial hardening on one surface does not create a real boundary if another surface still bypasses it.**

Therefore:
- **Do not recommend a broad sandbox retry yet.**
- **Do recommend a future retry only as a narrow, canaried, evidence-backed change with full-surface validation.**
- **For Vega/PXS right now, the honest Security position is that boundary enforcement remains incomplete.**

If the evidence base is thin in one area, it is mainly around the exact current live sandbox/container state, because those details are discussed in research/runbook form more than captured as routine operational evidence. That gap itself supports the recommendation for stronger effective-state evidence before any retry.
