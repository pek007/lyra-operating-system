---
title: "Operational Separation Between Lyra OS and PXS in OpenClaw"
date: 2026-03-07
source: deepresearch
ingest_from: "telegram attachment deep-research-report_62---83cf4d52-3493-4135-b021-41012aff2fe6.md"
tags: [external-analysis, deepresearch, lyra-os, pxs, architecture, governance, product-assembly]
decision_relevance: high
confidence: medium-high
status: archived-source
---

# Operational Separation Between Lyra OS and PXS in OpenClaw

## Situation appraisal

You have already taken the most important step: you have made the separation explicit in the PXS repo. The accepted ADR states that PXS should be a standalone repository for “product implementation” while the OpenClaw OS workspace remains the “operating and governance layer,” with the primary consequence being clearer ownership boundaries and safer iteration without coupling—at the cost of coordination overhead. fileciteturn127file0L1-L20

That intent is consistent with how PXS itself describes “Framework vs Instance” separation: keep reusable IP (taxonomies, governance logic, templates/schemas) separate from company-specific implementation content. fileciteturn126file0L1-L35

In the Lyra OS repo, you have already laid down the primitives needed to turn “separation” into something operational:

- A formal product portfolio registry whose purpose is to “maintain explicit product boundaries across OS and PX initiatives” and reduce coupling, and which explicitly constrains dependencies and requires published interfaces/versioning for cross-product reuse. fileciteturn114file0L1-L62  
- A product-boundary template that forces you to write down ownership boundaries, data/runtime boundaries, dependency policies, interface contracts, and operational controls. fileciteturn116file0L1-L59  
- A “shared codebase, separated instances” service-boundary design: reuse modules, but run separate `os` and `px` instances with strong isolation requirements and explicit domain namespacing. fileciteturn117file0L1-L56  

The net is: your repositories already imply a “platform + instance” model. What’s left is to make the “productization surfaces” explicit and repeatable so PXS can reliably consume Lyra OS outputs.

## Assessing your hypothesis

Your hypothesis: classify Lyra OS artifacts into (a) **Lyra OS internal** and (b) **Products**; then classify products into (1) **Skills** (OpenClaw-native distribution), (2) **aaS** (service delivery like TDE), and (3) **Capabilities** (everything else that must come with a distribution mechanism).

This is a strong starting point because it separates *development exhaust* from *distributable IP*. That mirrors PXS’s “framework vs instance” logic and helps prevent accidental leakage of sprint noise or experimental docs into an operational company system. fileciteturn126file0L1-L35

Where it needs refinement is in two places:

**A product is rarely a single deliverable type.**  
TDE is not just “aaS”; it is “aaS + contracts + policy + test/evidence surfaces.” Your own TDE canonical index makes that explicit by enumerating contracts, runtime tools, verification tests, runtime state files, and evidence surfaces. fileciteturn122file0L1-L50  
Similarly, skills governance is not “just a skill”; it is: a human-readable policy, a machine-readable policy YAML, and (ideally) enforcement hooks.

**“Capabilities” will explode unless you constrain it.**  
Right now it is a catch-all category. You need a second-level taxonomy inside “Capabilities” that encodes *how it is consumed* (prompt-time guidance vs machine-enforced gates vs code libraries vs templates/schemas), otherwise every new artifact becomes a bespoke distribution problem.

So: the hypothesis is viable, but only if you (1) allow *products to be composable assemblies of artifacts*, and (2) treat *distribution/activation* as a first-class property, not an afterthought.

## What the repos imply about “how it should work” in practice

### The OS-to-PXS boundary is already described as multi-instance services

Your service-boundary design is effectively the operating model you’re searching for: “shared codebase, separated instances,” with explicit `domain=os` vs `domain=px`, separate `.env.os`/`.env.px`, and strict isolation of data, secrets, policy config, dashboards, and access controls. fileciteturn117file0L1-L56

This is a “Lyra OS as provider of services” model, not an “OS as a magical layer that injects itself into PXS.” In other words: **Lyra OS can be an OS in the *platform engineering* sense (shared modules + governance), while PXS is an instance/tenant that consumes those services with separated state.**

### The OS already treats product boundaries as a governance object

The Product Portfolio Registry has explicit rules that are *exactly* what you need when PXS and Lyra OS have separate repos and workspaces: products should not directly depend on each other, cross-product reuse requires versioning and published interfaces, and SaaS-candidate products need strong isolation of data/identity/deployment. fileciteturn114file0L1-L62

It also already defines at least one product (Control Panel) and explicitly prohibits direct runtime dependencies on PX product codebases. fileciteturn114file0L1-L62

That is a key clue: you’re not inventing a taxonomy from scratch—you’re aligning your “Products” idea with the OS’s existing boundary discipline.

### The OS already has “policy-as-code” primitives (skills policy, tool governance)

You have both normative policy and a machine-readable representation:

- Skills governance defines risk classes (S0–S3), default rules (sandbox+disabled, version pinning, no prod auto-updates), action gates for side effects, and an explicit lifecycle workflow. fileciteturn118file0L1-L99  
- The YAML policy encodes defaults (sandbox, disabled, evidence pack required, version pin required), risk-class controls, and a concrete list of approval-gated actions. fileciteturn119file0L1-L121  

This strongly supports your “capability” category—but it also suggests you should name one important subclass explicitly: **policy packs** (human policy + machine policy + enforcement hook).

Similarly, tool/external service governance defines minimum enforceable controls (default-deny for high-impact actions, managed secrets, request/response controls, structured audit records) and a change gate requiring evidence pack, risk class, approval gate, and rollback/kill-switch. fileciteturn124file0L1-L23

### “Processes” and “jobs” are already “exportable IP” (and are designed to govern authority)

Your JOBS_PROCESS is plainly not “internal sprint documentation.” It governs the lifecycle of jobs “as first-class operating objects,” explicitly classifies change types by authority impact, and defines controls such as: no self-approval for authority increases, machine-readable authority diffs for higher-risk changes, and approval gates including dual control for the highest risk. fileciteturn120file0L1-L54

This is exactly the kind of governance that PXS would want imported rather than re-invented, because it constrains escalation and side effects (which is where agentized systems fail noisily).

### TDE is already structured as a service with deterministic, fail-closed semantics

TDE’s job tick contract is purpose-built for service-style execution: it defines triggers (cron default, heartbeat exception), default mode (isolated cron run), and “delivery default: internal/silent” unless escalation conditions are met. fileciteturn123file0L1-L89  

It also encodes fail-closed conditions and strict binding/objective validation before side-effecting mutations—i.e., it is designed to prevent unsafe writes absent the right context and authority proof. fileciteturn123file0L1-L89

This is a clean “aaS” anchor for your taxonomy, with one caveat: technically it’s more “service-in-your-environment” than “SaaS.” That naming matters because it changes what you optimize for (operational isolation and deterministic execution) versus what you *don’t* yet need (true multi-tenant billing, external auth, etc.).

## Distribution mechanisms that fit OpenClaw

Your open question is essentially: “What mechanisms exist in OpenClaw that can carry structural assets across workspaces?” Skills are the obvious answer—and the docs provide a very crisp model.

### Skills as a built-in distribution bus

OpenClaw loads skills from three locations—bundled, managed/local `~/.openclaw/skills`, and `<workspace>/skills`—with precedence: workspace > managed/local > bundled. It also supports `skills.load.extraDirs` for additional skill folders at *lowest precedence*. citeturn7view0

This gives you three practical transfer patterns:

1. **Shared baseline pack (cross-workspace, same machine):** put “Lyra shared” skills in `~/.openclaw/skills`, visible to all agents/workspaces on the gateway. citeturn7view0  
2. **Domain-specific overrides:** keep PXS-specific skills in `<pxs-workspace>/skills` and OS-specific overrides in `<lyra-os-workspace>/skills`; they will shadow shared skills when names conflict. citeturn7view0  
3. **Shared-but-low-precedence pack:** put a “skills pack repo checkout” somewhere stable and list it under `skills.load.extraDirs`, so it’s shared but cannot override either workspace. This is very close to what you want for “OS provides services/policies, instances may override locally.” citeturn7view0  

This directly answers your question “can Lyra OS artifacts be converted into skills?”—*many can*, because a skill is simply a versioned folder with a `SKILL.md` and optional supporting files/scripts. citeturn7view0 The constraint is not “can you convert it,” but “should it live in prompt-time instructions” versus “should it be enforced via code.”

### Plugin-shipped skills for “harder” packaging

OpenClaw also supports plugins that can ship their own skills by listing skill directories in `openclaw.plugin.json`; those skills participate in normal precedence and can be gated via config requirements. citeturn7view0

That’s a credible future vehicle for packaging “Lyra OS product bundles” (skills + tools + config gating) in a way that is operationally cleaner than copying folders around. You likely don’t need to lead with this unless you want strong enable/disable semantics across the environment.

### Scheduling as part of the service model

TDE’s job tick semantics are explicitly aligned with cron and heartbeat. fileciteturn123file0L1-L89 OpenClaw documentation clarifies that cron jobs can run in isolated sessions (clean context, avoids polluting main history), support model overrides, and provide precise scheduling; heartbeat is context-aware periodic awareness in the main session. citeturn8view0

So “aaS inside OpenClaw” is not hand-wavy—it can literally be implemented as: **domain-scoped cron jobs that run deterministic service routines (TDE kernels), plus skills that interpret/control them**.

## Refining the hypothesis into an implementable taxonomy

A workable refinement is:

- Keep your top-level split: **Internal** vs **Products**.
- Evolve “Products” into **Product Assemblies** that can include multiple artifact types.
- Replace “Capabilities (catch-all)” with **Packs**, and define a small, fixed set of pack subtypes.

### Proposed product types and their required properties

| Product type (top-level) | What it *is* | Key property that must exist | Best-native OpenClaw distribution | What you already have that maps to it |
|---|---|---|---|---|
| Skill Pack | Prompt-time operational knowledge + optional scripts | A `SKILL.md` entrypoint and gating/versioning | `~/.openclaw/skills`, `<workspace>/skills`, or `extraDirs`; optionally plugin-shipped | Skills policy + governance strongly imply this should exist as a first-class deliverable. fileciteturn118file0L1-L99 fileciteturn119file0L1-L121 citeturn7view0 |
| Service (aaS) | Deterministic runnable module(s) with clear contracts and state | A stable contract + domain-scoped config + run/schedule mechanism | Cron (isolated) for deterministic runs; heartbeat for periodic monitoring | TDE contracts + runtime tools + evidence surfaces. fileciteturn122file0L1-L50 fileciteturn123file0L1-L89 citeturn8view0 |
| Pack (Capability Pack) | Non-skill “reusable IP” such as policies, schemas, templates, validators | A distribution & versioning mechanism + (ideally) enforcement hook | Git-pinned dependency (submodule/subtree) or plugin; optionally referenced by skills | Product boundary template + external service governance + OpenClaw config SOP are already “pack-shaped.” fileciteturn116file0L1-L59 fileciteturn124file0L1-L23 fileciteturn125file0L1-L88 |

This preserves your three product classes, but makes “capabilities” finite by renaming it to “pack” and giving it minimal required properties.

### Concrete classification of what exists today

Based on the current repositories, the most defensible classification looks like this:

**Internal (Lyra OS internal)**  
Development and research exhaust: work orders, evidence bundles, deep research reports, sprint cadence/briefs, and other documents that exist to get to a product (not to be consumed as a product). TDE’s index explicitly treats “knowledge/evidence” and “knowledge/reports” as surfaces, which is useful internally but not something you should blindly replicate into PXS as-is. fileciteturn122file0L1-L50

**Products → Services (aaS)**  
- **TDE** (service) is already a service-shaped product: contracts, deterministic runtime tools, verification tests, and explicit “real vs simulated” capability declarations. fileciteturn122file0L1-L50  
- The job tick contract defines deterministic execution, strict validation, and fail-closed guarantees—these are service semantics. fileciteturn123file0L1-L89  

**Products → Skill Packs (should be created; not yet explicitly present as a bundle)**  
- Skills governance and skills policy should be exposed as a *governance skill pack* that teaches the PXS agent(s) “how to select/enable skills safely,” and references the YAML for machine-checking. fileciteturn118file0L1-L99 fileciteturn119file0L1-L121  
- Jobs/process governance (your “jobs” model) should be exposed as an operational skill pack because it governs authority changes and approvals. fileciteturn120file0L1-L54  
- OpenClaw config change control should be exposed as a skill pack for operational reliability if PXS will ever touch gateway config (or rely on OS-managed changes). fileciteturn125file0L1-L88  

**Products → Packs (capabilities)**  
- **Policy pack:** `TOOL_EXTERNAL_SERVICE_GOVERNANCE_V1.md` + related enforcement expectations. fileciteturn124file0L1-L23  
- **Boundary/governance pack:** product portfolio + product boundary template (these are reusable governance assets PXS should adopt when it consumes OS services). fileciteturn114file0L1-L62 fileciteturn116file0L1-L59  
- **Operating model pack:** jobs/process docs that define safe authority evolution and acceptance governance (if you treat them as process-as-code later). fileciteturn120file0L1-L54  

## Recommendation

### Adopt “Lyra OS as platform services + distributable packs,” with explicit domain-scoped instances

Your own architectural docs already describe the right target state:

- Reuse modules, but run separate `os` and `px` instances, enforce separate secrets/state/storage/config, and default-deny cross-domain reads. fileciteturn117file0L1-L56  
- Treat each initiative as a product with explicit boundaries and prohibit direct runtime dependency from OS products into PX codebases. fileciteturn114file0L1-L62  
- Treat PXS as its own product repo/workspace, and accept that “cross-repo coordination” is the cost you pay for safety and clean release management. fileciteturn127file0L1-L20  

Given that alignment, the recommendation is:

**Make “product assembly” the unit of transfer, and make distribution/activation explicit per assembly.**  
Concretely:

1. **Keep “Internal vs Products” as the top-level split**, but require that anything classified as “Product” has:
   - a product record entry (in the product portfolio registry),
   - a boundary doc (using the product boundary template),
   - an explicit “distribution mechanism” field (skill install location / cron wiring / repo dependency / plugin).

   This is exactly what your portfolio/boundary templates were created to enforce. fileciteturn114file0L1-L62 fileciteturn116file0L1-L59

2. **Use OpenClaw skills as the primary “human/agent interface layer,”** but do not confuse that with the underlying capability.  
   - Put shared, reusable skill packs in `~/.openclaw/skills` (or `extraDirs` if you want it strictly lowest precedence) and keep PXS overrides in `<pxs-workspace>/skills`. This uses OpenClaw’s built-in precedence model explicitly. citeturn7view0  
   - Where you want hard enable/disable semantics, move toward plugin-shipped skills later. citeturn7view0  

3. **Treat TDE as “aaS inside OpenClaw,” not as an external SaaS (yet).**  
   - Run `px` and `os` instances separately (per the service boundary doc) and schedule job ticks via cron isolated sessions for determinism and clean context. fileciteturn117file0L1-L56 fileciteturn123file0L1-L89 citeturn8view0  
   - Expose a `tde-operator` skill pack that: (a) reads the latest verdict artifacts, (b) triggers reruns safely, (c) escalates to human approval when fail-closed reasons occur. This is consistent with the job tick contract’s “internal/silent” default and explicit fail-closed semantics. fileciteturn123file0L1-L89  

4. **Convert “Capabilities” into “Pack products” with a strict definition.**  
   You already have strong candidates:
   - Skills governance policy + YAML policy: policy pack + enforcement configuration. fileciteturn118file0L1-L99 fileciteturn119file0L1-L121  
   - External tool/service governance: policy pack that mandates evidence packs, approval gates, managed secrets, and auditable calls. fileciteturn124file0L1-L23  
   - OpenClaw config change SOP: operations pack guarding changes to OpenClaw config and sandbox behavior. fileciteturn125file0L1-L88  
   - Jobs governance: operating model pack that constrains authority evolution (critically important once PXS becomes truly agentic). fileciteturn120file0L1-L54  

   These packs should be imported into PXS as *version-pinned dependencies* (e.g., submodule/subtree or a release artifact). This aligns with the PXS ADR’s intent: separate repos with cleaner release management, at the cost of explicit coordination. fileciteturn127file0L1-L20

5. **Enforce “products are assemblies” in the product portfolio record itself.**  
   Today, your product record schema has the right boundary-related fields (domain, type, tenant model, canonical repo, dependency constraints, public interfaces). fileciteturn114file0L1-L62  
   Improve it by adding a small “Artifacts” list per product, e.g.:
   - `artifacts: [service, skill-pack, policy-pack, schema-pack]`
   - `distribution: {service: cron|daemon, skills: managed|extraDirs|plugin, packs: submodule|release-zip}`
   - `enforcement: {required_checks: [...], gates: [...], evidence_pack: required}`

This turns your hypothesis into an operational contract: every time Lyra OS produces something intended for PXS, it is produced as a **versioned assembly** with a declared activation mechanism, and it is consumed by PXS via an explicit dependency lane—not by copy/paste or ad-hoc referencing.

In short: keep the hypothesis, but make two changes: **(1) products are multi-artifact assemblies,** and **(2) “capabilities” becomes “packs” with a fixed, enforceable schema (distribution + activation + versioning + controls).**