---
title: "Designing a Secure, Scalable Boundary Between Lyra OS and pxs in OpenClaw"
date: 2026-03-15
source: deepresearch
ingest_from: "telegram attachment deep-research-report_79---1cbee53d-7f0c-47bb-9d7e-660e2e5671a9.md"
tags: [external-analysis, deepresearch, sandbox, security, pxs, lyra-os, trust-boundary]
decision_relevance: high
confidence: medium-high
status: archived-source
---

# Designing a Secure, Scalable Boundary Between Lyra OS and pxs in OpenClaw

## Problem statement and security invariants

You are trying to draw a hard boundary between two “workspaces” inside the same agent ecosystem: **Lyra OS** (a platform workspace that develops general capabilities) and **pxs** (a “company-as-code” workspace that consumes those capabilities to operate the business). The intended asymmetry is clear: **pxs should be able to use everything Lyra produces, but pxs should not be able to inspect or mutate Lyra OS internals** (especially filesystem state). That is, you want *capability flow* without *ambient authority*.

A useful way to formalize this is the classic security-design framing of **least privilege** and **least common mechanism**: give pxs only the minimum permissions needed (least privilege), and avoid shared subsystems/state that become accidental cross-tenant channels (least common mechanism). These principles are foundational precisely because they reduce blast radius from mistakes, compromise, or misalignment. citeturn19search9

The key tension: a “workspace” boundary inside one OpenClaw Gateway instance is *not automatically* a strong isolation boundary. OpenClaw’s own security model is explicitly a **personal-assistant trust model** (one trusted operator boundary per gateway). It warns that it is **not** a hostile multi-tenant boundary for mutually untrusted users sharing a single gateway/agent. When adversarial or mixed-trust separation is required, OpenClaw recommends **splitting trust boundaries**—separate gateways and ideally separate OS users/hosts. citeturn14view0

So your design task naturally falls into two tracks:

1. **Within-one-gateway hardening**: “good fences” using sandboxing + tool policy + workspace scoping, recognizing it is not equivalent to an adversarial tenant boundary. citeturn14view0turn16view0  
2. **Real separation**: “separate gateways / separate OS users / separate hosts” for a robust boundary, then reintroduce capability flow via explicit APIs/products. citeturn14view0  

Your reported experience—sandboxing causing the agent to “lock in” to a minimal environment and lose actionability—is a known failure mode when sandbox defaults and tool-policy layering are not treated as part of your product architecture.

## OpenClaw’s sandbox mechanism in detail

OpenClaw’s sandboxing is **Docker-based tool execution isolation**: the **Gateway remains on the host**, but (when enabled) **tool execution runs in containers** to reduce filesystem/process blast radius. OpenClaw’s docs are explicit that this helps materially, but it is “not a perfect security boundary.” citeturn9view0

### What is actually sandboxed

When sandboxing is enabled, OpenClaw runs tool execution—e.g., `exec`, filesystem tools (`read`, `write`, `edit`, `apply_patch`), and process supervision—in the container. The Gateway itself is not sandboxed. citeturn9view0

There is also an optional **sandboxed browser** container configuration (“sandbox browser”) with its own network and related controls; and there are explicit “escape hatches” for running on the host (notably elevated execution for `exec`). citeturn9view0turn16view0

### Three knobs that define your effective security model

OpenClaw separates three concepts that are easy to conflate but must be managed explicitly:

- **Sandbox** (`agents.*.sandbox.*`) decides *where tools run* (host vs container). citeturn16view0  
- **Tool policy** (`tools.*`, plus sandbox-specific tool policy) decides *which tools exist/are callable* at all—deny wins. citeturn16view0turn8search3  
- **Elevated** (`tools.elevated.*`) is an **exec-only** escape hatch to run on the host while sandboxed; it does **not** grant new tools, and it cannot override a denied tool. citeturn16view0turn8search2  

This separation is central to understanding your “loss of abilities” experience: you may have sandboxed the session *and* inadvertently ended up with an unexpectedly restrictive sandbox tool policy + minimal filesystem visibility + minimal container image.

### Mode, scope, and workspace access

The sandbox has three key operational parameters:

- `mode`:  
  - `"off"` = no sandboxing  
  - `"non-main"` = only non-main sessions are sandboxed (common “surprise” in group/channel contexts)  
  - `"all"` = everything sandboxed citeturn9view0turn16view0  

- `scope`: how many containers are created: `"session"` (default), `"agent"`, or `"shared"`. citeturn9view0turn10view0  

- `workspaceAccess`: what the container can see:  
  - `"none"` (default): tools operate in an isolated sandbox workspace under `~/.openclaw/sandboxes`  
  - `"ro"`: mount the agent workspace read-only (and disables write/edit/apply_patch)  
  - `"rw"`: mount the agent workspace read/write at `/workspace` citeturn9view0  

A key nuance for your “deliver products via Skills” idea: when `workspaceAccess: "none"`, OpenClaw will **mirror eligible skills into the sandbox workspace** so they remain readable from inside the sandbox-rooted `read` tool. citeturn9view0turn8search4  
This is a strong alignment with “capabilities as delivered artifacts,” provided you treat skills as *products* rather than as “just files in Lyra’s repo.”

### Bind mounts and why they can silently break your boundary

OpenClaw supports `docker.binds` for mounting host directories into the container. This is the primary footgun for your Lyra→pxs separation goal: bind mounts **pierce** the sandbox filesystem boundary—whatever you mount becomes visible with the mode you set (`:ro`/`:rw`). citeturn9view0turn16view0

OpenClaw documents that it blocks some dangerous bind sources by default (e.g., paths that would expose `/proc`, `/sys`, `/dev`, and warns strongly about `/var/run/docker.sock`). citeturn9view0turn16view0  
For your use case, the principle is stricter: **never mount Lyra’s workspace into pxs’s sandbox**, and avoid broad mounts that could allow traversal into Lyra-OS-managed state.

### Container images, network, and “why my sandbox is useless”

OpenClaw’s docs highlight that:

- The default sandbox image is minimal and **does not include Node**, and likely not all toolchains you expect. citeturn9view0  
- By default, sandbox containers run with **no network** (Docker network = `"none"`), and you must override this if you want package installs or network-dependent tooling. citeturn9view0  
- `setupCommand` runs once per container creation and has common pitfalls: no egress by default, read-only root can prevent installs, and you may need to run as root inside the container. citeturn9view0  
- Sandbox exec does **not** inherit host `process.env`; environment must be provided via sandbox config env or baked into the image. citeturn9view0  

This cluster of defaults is the primary technical explanation for the “lock-in to a minimal environment” pattern.

## Why sandboxing causes “capability collapse” and how to diagnose it

Your symptom (“almost all abilities to take actions disappear”) typically results from **three interacting clamps**:

### Workspace clamp

If `workspaceAccess: "none"` (default), the agent cannot see its normal workspace; reads/writes happen in the sandbox workspace directory. This feels like amnesia unless you deliberately stage inputs into the sandbox workspace or rely on mirrored skills only. citeturn9view0

For pxs specifically, if you expect it to operate “company-as-code” *by editing its repo*, you generally need `workspaceAccess: "rw"` (pxs edits its own workspace) or an explicit pipeline that materializes tasks into the sandbox workspace, commits outside the sandbox via a controlled promotion mechanism.

### Tool-policy clamp (including sandbox-specific tool policy)

Sandboxing does not imply “all tools still exist.” Tool policy is evaluated independently; if tools are denied globally/per-agent, sandboxing won’t resurrect them. Additionally, OpenClaw supports **sandbox-only tool policy** (`tools.sandbox.tools.*`) that applies *only when sandboxed*. Misconfigured allow/deny lists here commonly cause “I can’t do anything” failures—especially if `allow` is set but incomplete, since allowlists block everything else. citeturn16view0turn8search3

### Environment clamp (image + network + dependencies)

A sandbox container is *not your host environment*. If the default image lacks your dependency chain, and network is `"none"`, `setupCommand` cannot install missing packages. If root is read-only, even writing to install locations fails. citeturn9view0  
OpenClaw explicitly provides a more functional sandbox build script (`scripts/sandbox-common-setup.sh`) intended to produce an image with common tooling like `curl`, `jq`, `nodejs`, `python3`, `git`, and then you set your sandbox image to that. citeturn9view0

### Debugging workflow that avoids guesswork

OpenClaw provides a “ground truth” inspector:

- `openclaw sandbox explain` prints the effective mode/scope/workspace access, whether the session is currently sandboxed, effective sandbox tool allow/deny, and elevated gates (plus the config keys that caused them). citeturn16view0turn10view0  

For lifecycle issues (stale containers that don’t reflect new config/image):

- `openclaw sandbox list` shows container image match, age, idle time, session/agent association. citeturn10view0  
- `openclaw sandbox recreate` is the supported way to force recreation after config/image/setup changes; this matters because containers may persist indefinitely for regularly used agents and otherwise prune only after idle windows. citeturn10view0  

These tools are especially relevant when you’re iterating on the boundary design, because a “fixed config” might not take effect until containers are recreated. citeturn10view0

## Architectural options for a Lyra–pxs boundary

Your requirement (“pxs can use all Lyra capabilities, but cannot access Lyra’s workspace”) maps onto a spectrum of designs. The correct choice depends on how “hard” you need the boundary to be and how much operational complexity you can tolerate.

### Strong boundary: split trust domains, then reintroduce capability flow

If you want robust, adversarial-grade separation between Lyra OS and pxs, OpenClaw’s own guidance points toward **separate gateways and ideally separate OS users/hosts** per trust boundary. citeturn14view0

In your case, treat:

- **Lyra OS gateway** as the privileged “platform/control plane” (where capabilities are built, secrets live, tool surface can be broader).  
- **pxs gateway** as the “tenant plane” (restricted tool surface, no access to Lyra state, only consumes published products).

Then, define a formal “capability product interface” between them: signed skill packs, versioned APIs, or a service endpoint.

This architecture aligns with two core security principles:

- Least common mechanism: separate disk state, separate auth stores, separate runtime credentials. citeturn19search9turn14view0  
- Least privilege: pxs only gets the published capability interfaces, not the platform internals. citeturn19search9  

Operationally, it also aligns with OpenClaw multi-agent documentation that emphasizes per-agent credential stores and warns against reusing agent directories. citeturn17view0

### Medium boundary: one gateway, two agents, different sandboxes and tool profiles

If you accept the “one trusted operator boundary” model (i.e., you’re not defending against a malicious co-tenant who can modify host/config), you can often get a practical boundary using OpenClaw’s multi-agent support:

- Lyra agent: sandbox off (or selectively sandboxed); full toolset  
- pxs agent: sandbox mode `"all"` (or at least for the relevant sessions), with restrictive tool policy and carefully controlled workspace access

OpenClaw explicitly supports per-agent sandbox overrides (`agents.list[].sandbox` overriding defaults) and per-agent tool restrictions. It also shows practical patterns like “personal + restricted family bot” and “different sandbox modes per agent.” citeturn17view0

This design can be robust against prompt injection and “accidental misuse,” but it is still bounded by OpenClaw’s baseline assumption: the host/config boundary is trusted; authenticated operator access inside one gateway is a control-plane role, not a tenant boundary. citeturn14view0

### Minimal boundary: no sandbox; rely on workspace-only filesystem + tool denial

The “trusted-boundary with compensating controls” approach (which your Lyra OS repo governance notes appear to have been converging toward) is a valid operating mode when:

- the operator boundary is single-trust, and  
- the ingress surfaces are allowlisted, and  
- runtime tools are tightly constrained, and  
- filesystem access is workspace-scoped

OpenClaw explicitly recommends a hardened baseline that includes denying high-risk tool groups by default and enabling workspace-only filesystem limits (`tools.fs.workspaceOnly: true`) as part of a “start small then widen” hardening strategy. citeturn14view0

However: this option is sensitive to path-escape and guard bugs. As of March 2026, OpenClaw has had a published advisory where `@`-prefixed absolute paths could bypass some workspace boundary checks in affected versions, fixed in 2026.2.24. citeturn13search0turn13search2  
If you pick this option, **version hygiene becomes part of your security boundary**.

## Configuration patterns that preserve pxs autonomy without Lyra filesystem access

Below is a configuration strategy that directly targets your goal: pxs can work on its own codebase (“company-as-code”), can consume skills/capabilities produced by Lyra, but cannot see or traverse Lyra’s workspace.

### Separate workspaces + per-agent auth stores

OpenClaw supports per-agent workspaces and keeps credentials per agent in per-agent auth stores; it explicitly warns not to reuse agent directories across agents. citeturn17view0  
This is your first line of separation: **make Lyra workspace and pxs workspace disjoint at the filesystem level** and avoid shared agentDir/credential files.

### Treat Lyra capabilities as published products, not mountable state

Your direction—turning off pxs direct file access and replacing it with delivered products (“Skills”)—fits OpenClaw’s skills model well:

- Skills can be loaded from bundled, managed (`~/.openclaw/skills`), and workspace skill folders (`<workspace>/skills`), with workspace taking precedence in name conflicts. citeturn8search4  
- In multi-agent setups, each agent has its own workspace, so workspace skills are per-agent, while `~/.openclaw/skills` is shared across agents on the same machine. citeturn8search4turn17view0  

A clean pattern is:

- Lyra publishes “capability packs” into **managed/shared skills** (`~/.openclaw/skills`) or into a controlled external registry workflow.  
- pxs consumes those managed skills without any need to read Lyra’s repo.  
- If pxs is sandboxed with `workspaceAccess: "none"`, eligible skills are mirrored into the sandbox workspace so pxs can still read them with sandbox-rooted `read`. citeturn9view0turn8search4  

This is conceptually aligned with capability-based security: the consumer only receives specific, delegable rights (skills/calls), not a global namespace (Lyra’s filesystem internals). citeturn19search7turn19search9

### Make the pxs sandbox *functional*, not minimal

To avoid your historical “sandbox lock-in,” treat the sandbox container as a **first-class runtime product**:

- Use a tool-rich sandbox image (OpenClaw documents a “common tooling” sandbox build and how to set the image). citeturn9view0  
- Keep default “no network” unless you explicitly need egress; if you do need installs in `setupCommand`, you must enable network egress and ensure the container is writable and running as root for installation. citeturn9view0  
- Set sandbox env explicitly for API keys or service endpoints; sandbox exec doesn’t inherit host environment. citeturn9view0  

### Constrain pxs with tool policy, especially in sandbox contexts

Use tool policy to ensure pxs can do its job but cannot “break glass” back into Lyra:

- Deny `tools.elevated` for pxs (or deny `exec` escape hatches entirely) and keep approvals strict if host exec is ever needed. Elevated is an exec-only host escape hatch when sandboxed. citeturn16view0turn8search2  
- Use sandbox-specific tool policy (`tools.sandbox.tools.*`) for pxs so that **being sandboxed never silently removes required tools** and never silently grants prohibited tools. citeturn16view0  

OpenClaw’s tool policy model is explicit: deny wins, allowlists are exclusive when present, and sandbox tool policy is an additional clamp that only applies when sandboxed. citeturn16view0turn8search3

### A concrete “two-agent boundary” template

The following illustrates the shape of what you want (adapt it to your exact paths and tool surface). The key is: **pxs workspace is mounted read/write for pxs only**, and **Lyra workspace is never mounted into pxs’s sandbox**, while Lyra-published capabilities are delivered via shared managed skills or remote services.

```json
{
  "agents": {
    "list": [
      {
        "id": "lyra",
        "default": true,
        "workspace": "/path/to/lyra-workspace",
        "sandbox": { "mode": "off" }
      },
      {
        "id": "pxs",
        "workspace": "/path/to/pxs-workspace",
        "sandbox": {
          "mode": "all",
          "scope": "agent",
          "workspaceAccess": "rw",
          "docker": {
            "image": "openclaw-sandbox-common:bookworm-slim",
            "network": "none",
            "binds": []
          }
        },
        "tools": {
          "profile": "coding",
          "deny": ["gateway", "nodes"],
          "sandbox": {
            "tools": { "allow": ["group:fs", "group:runtime"], "deny": ["browser"] }
          },
          "elevated": { "enabled": false }
        }
      }
    ]
  },
  "skills": {
    "load": {
      "extraDirs": ["/home/user/.openclaw/skills"]
    }
  }
}
```

This structure is justified by multiple OpenClaw primitives:

- Per-agent sandbox and tool overrides are supported and have defined precedence. citeturn17view0  
- `workspaceAccess` defines what the sandbox sees and whether writes are possible. citeturn9view0  
- `docker.binds` pierces sandbox boundaries; leaving it empty is how you avoid accidental host exposure. citeturn9view0turn16view0  
- Tool policy and sandbox-specific tool policy are separate controls, and `deny` wins. citeturn16view0turn8search3  

If you later decide you need network egress for pxs tools, you should treat that as a major change to the pxs trust envelope: OpenClaw defaults to no network for sandbox containers for a reason, and changing it changes the exfiltration story. citeturn9view0turn14view0  

## Operational hardening and failure-mode playbooks

### Treat versioning and advisory response as part of the boundary

Because you are explicitly relying on workspace scoping and sandbox boundaries, OpenClaw version hygiene is security-critical. OpenClaw 2026.2.24 release notes include:

- Introduction of a trust-model heuristic for likely shared-user ingress, clarifying personal-assistant assumptions and hardening guidance. citeturn13search2turn14view0  
- Fixes for workspace filesystem boundary checks, including normalizing `@`-prefixed paths in workspace-only read/write/edit and related guards. citeturn13search2turn13search0  

In other words: if your boundary depends on workspace-only behavior, you must track these releases the way you’d track kernel/container boundary fixes in more traditional systems.

### Automate “trust boundary drift detection”

OpenClaw’s `security audit` is designed to warn about footguns and mismatches between declared trust model and enabled surfaces, and it recommends running it regularly, especially after config changes. citeturn14view0turn8search5

For your Lyra–pxs boundary, drift detection should minimally include:

- current sandbox mode per agent / per default  
- whether workspace scoping is enabled where you rely on it  
- whether elevated exec is enabled for pxs  
- whether binds exist that pierce the boundary  
- tool policy deltas for pxs (especially sandbox tool policy)

OpenClaw’s docs also emphasize that authenticated operator access is inherently control-plane access within one gateway instance; this is why drift detection should include not only config but also deployment/exposure posture. citeturn14view0

### Make sandbox configuration changes “safe to roll out”

OpenClaw’s sandbox containers can persist with old config and images; that creates a common “it’s fixed but it’s still broken” period unless you force recreation. OpenClaw explicitly recommends `openclaw sandbox recreate` after image/config/setup changes. citeturn10view0

A disciplined rollout workflow for pxs sandbox changes is therefore:

- change config or image  
- run `openclaw sandbox explain` to confirm intended effective state citeturn16view0turn10view0  
- `openclaw sandbox recreate --agent pxs` (or `--all` when appropriate) citeturn10view0  
- run `openclaw security audit --deep` and record the output as an artifact (auditable “company-as-code” evidence) citeturn14view0turn8search5  

### Don’t confuse “read-only” with “safe”

OpenClaw’s security docs include a baseline “hardened in 60 seconds” config that denies runtime/fs tool groups by default and keeps the gateway local-only. It’s a great reference for “default deny then selectively widen.” citeturn14view0

But for Lyra–pxs separation, the more subtle point is: **read-only mounts and no-write policies reduce integrity risk, not confidentiality risk**. A read-only mount can still leak secrets; a sandbox with web access can still exfiltrate. That’s why OpenClaw’s recommended approach for mixed-trust/adversarial setups is splitting trust boundaries across gateways/hosts. citeturn14view0turn9view0

## Bottom line

If you want a boundary that is robust in the way security engineers mean “robust,” the architecture that best fits both your goal and OpenClaw’s own security model is:

- **Lyra OS** runs as a privileged trust domain (gateway/host).  
- **pxs** runs as a separate trust domain (ideally separate gateway + OS user/host).  
- Capabilities flow from Lyra to pxs only via **explicit, versioned products**: shared managed skills, signed artifacts, or services/APIs—never via filesystem visibility. citeturn14view0turn8search4turn19search9  

If you keep both in one gateway, you can still get a practical boundary with multi-agent + sandbox + tool policy + careful workspace separation—but treat it as **hardening inside a single trust boundary**, not equivalent to hostile multi-tenant isolation. citeturn14view0turn17view0turn16view0