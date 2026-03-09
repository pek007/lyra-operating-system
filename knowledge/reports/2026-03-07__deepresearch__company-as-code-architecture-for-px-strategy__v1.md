---
title: "Company-as-Code Architecture for PX Strategy"
date: 2026-03-07
source: deepresearch
ingest_from: "pxs/docs/instances/px-strategy/operating-system/library/operating-system-d4-company-as-code-deep-research-report-v0.1.md"
tags: [external-analysis, deepresearch, company-as-code, px-strategy, operating-model, governance]
decision_relevance: high
confidence: medium-high
status: archived-source
---

# Company-as-Code Architecture for PX Strategy

## Why Company-as-Code is a coherent direction

“Company-as-Code” is not a made-up phrase; it is already used to describe treating a company’s operational reality (policies, structure, and the configuration of business systems) as version-controlled, reviewable, testable artifacts—similar to Infrastructure-as-Code and related “Everything-as-Code” practices. citeturn9search3turn9search4turn8search1

What your description adds (and what makes it powerful for a one-person, high-leverage firm) is a unifying ambition: not merely “store docs in Git,” but make the company *run* from a structured model that drives decisions, generates work, and produces evidence. That lines up strongly with three mature patterns from software/DevOps that translate well to an “operating system for a firm”:

A docs-as-code workflow treats documentation like software: version control, pull requests and reviews, automated checks, and tight coupling to the system it documents. citeturn0search0turn0search5  
GitOps generalizes “source of truth in Git” into a governance pattern: desired state is declared in a version control system and automated agents continuously reconcile reality to match that state, improving traceability and rollbacks. citeturn0search2turn0search6  
Policy-as-code separates **policy decision** from **policy enforcement**, so that policies can be expressed declaratively and evaluated consistently in tooling or pipelines rather than relying on prose and memory. citeturn1search5turn1search2

Your stated end state—“mainly runs on code”—is achievable if you’re explicit about which parts must become *machine-checkable* (schemas, metadata, validation, routing), and which parts remain prose but become *governed* (templates, review cadence, ownership, change control). citeturn8search1turn0search0

## What your current repos already imply about the right approach

Your existing foundation in the `pek007/pxs` repository is already pointed straight at Company-as-Code, even if you don’t label it that way.

PXS is explicitly positioned as an “execution system” for PX Strategy with a focus on decisions, tasks, and operational cadence. fileciteturn4file1turn4file2  
The repo also already draws a **product boundary**: “product behavior belongs in PXS” while “operating system behavior belongs in the OS repo.” fileciteturn4file4  
You’ve already captured the “separate repo” decision as an accepted ADR, which is consistent with ADR best practices (small, durable records of significant decisions with context and consequences). fileciteturn4file5 citeturn2view0

Most importantly, you already have an opinionated “model backbone” in place:

The accepted taxonomy decision adopts an A/B/C/D structure (Governance/Financial/Business/Operating) as the canonical backbone, explicitly positioning it as reusable IP and separating “framework” from “instance” content. fileciteturn4file9turn20file0  
The taxonomy document itself includes the “uneven depth rule” (some areas deep, some intentionally sparse) which matches your “drill down as needed” plan. fileciteturn18file0  
A node-card template exists, and the PX Strategy instance already has L2 node files scaffolded plus an index. fileciteturn22file0turn53file2turn53file0  
You’ve even started formalizing machine-checkable structure with a JSON Schema for model nodes. fileciteturn4file10

Your operating charter inside the PX Strategy instance already asserts several “Company-as-Code” invariants: single source of truth, explicit ownership, versioned evolution, and mandatory metadata fields per artifact (domain, subdomain, owner, status, review date, version, links), plus a mandatory rule that accepted OS changes must be reflected in GitHub commits/issues. fileciteturn4file0

On the Lyra/OpenClaw side (`pek007/lyra-operating-system`), you have policies and architecture principles that map cleanly to your requested confidentiality and boundary needs:

The system charter centers “decision value” and “execution reliability,” and explicitly prefers “hard config for hard boundaries.” fileciteturn30file8  
The service boundary document states an explicit “shared codebase, separated instances” approach (`domain=os` vs `domain=px`) and enumerates isolation requirements across data directories, secrets, logs, and dashboards. fileciteturn30file17  
The OpenClaw change-control SOP treats runtime configuration changes as risky and enforces preview/approval/backup/validate/rollback. fileciteturn27file1  
You also already have a trust-boundary posture recommendation (“hardened single trust boundary now, pre-plan split boundary with triggers”)—which is very similar to the way strong security programs evolve without over-engineering on day one. fileciteturn27file9

Taken together, the repos strongly suggest that your *direction* is right; your main work is to unify your “PXS_structure.md” top-level taxonomy with the A/B/C/D node backbone and to make “confidentiality boundaries” more than a folder convention. fileciteturn18file0turn30file17turn0file0

## Analysis of your proposed structure against the existing PXS model backbone

Your uploaded structure defines five top-level domains: Model, Departments, Business Units, Client Projects, and Operating System. fileciteturn0file0  
That is conceptually sound, but there is an important alignment opportunity: your “Model” section already contains Strategy/Vision + Governance + Financial + Operating + Business, which corresponds almost one-for-one with the PXS taxonomy’s “Enterprise Model (L0) + A/B/C/D.” fileciteturn0file0turn18file0

The key design question is: do you want the “Model” to be a pure tree, or a tree-plus-graph?

A strict tree is excellent for “reference” style documentation, where the structure should mirror the thing being described (like a map). That’s explicitly recommended by Diátaxis for reference documentation architecture, and it maps cleanly to your “drill down” idea. citeturn0search17turn0search12  
But company reality is full of cross-cutting constraints (customer segmentation affects pricing, which affects route-to-market, which affects workflow design, which affects tooling). If you force cross-cutting truth into a tree, you either duplicate content or you hide dependencies. The sustainable pattern is: “one primary classification path + typed links between nodes.” This is also how well-run docs-as-code systems avoid document sprawl: keep a single canonical place per artifact, but allow links and generated indexes to provide multiple “views.” citeturn0search0turn0search5

Your existing PXS artifacts already anticipate this “tree-plus-graph” reality:

The OS charter requires every artifact to map to one primary domain/subdomain (tree), but it also requires “links” to related artifacts/issues/PRs (graph edges) and a governance cadence. fileciteturn4file0  
The PXS domain model explicitly encodes traceability from decisions to tasks to evidence to review, which is exactly a graph laid over your reference taxonomy. fileciteturn4file7

Where your proposed top-level domains need refinement is mostly about *semantics* and *boundaries*:

“Departments” and “Business Units” are not separate from the Operating Model; they are expressions of D3 (organization structure), D1 (capabilities), D2 (value streams), D5 (tech backbone), and D7 (talent system). Treating them as top-level folders is fine for navigation and operational convenience, but you’ll want them to be explicitly mapped back into the model nodes so the company blueprint remains coherent. fileciteturn18file0turn53file2  
“Client Projects” cannot be “shielded” by convention alone. If the same agents, same workspace, same secrets, and same repo have access, you don’t have a boundary—you have a polite fiction. Your Lyra/OpenClaw service-boundary doc already gives you the right abstraction: separate instances with separate storage and secrets namespaces. fileciteturn30file17  
“Operating System” is explicitly defined in your PXS architecture boundary as belonging in the OS repo (agent operating model, runtime orchestration, prompting policy, cross-project standards). So the practical interpretation is: PXS should contain OS *integration points* and PX Strategy-specific OS overlays, but the canonical OS should live in the Lyra/OpenClaw repo. fileciteturn4file4turn30file8

## Confidentiality and trust boundaries for client projects

Your client-project requirement (“confidential, must be shielded”) is the area where Company-as-Code most often fails in practice, because Git-based workflows make it deceptively easy to “just put it in the repo.” Strong boundaries require layered controls: human access control, system access control, and agent/tooling access control. citeturn4search1turn7search3  

A practical way to reason about this is to treat confidentiality as a first-class system objective and to implement least privilege by default. The entity["organization","National Institute of Standards and Technology","us standards body"] defines least privilege as restricting access to the minimum needed, and defines confidentiality as preserving authorized restrictions on access and disclosure (including protection of proprietary information). citeturn4search1turn7search3

### OpenClaw-specific implications

OpenClaw’s own docs make two boundary-critical points:

The agent workspace is separate from `~/.openclaw/` (state/config/credentials/sessions) and is “the only working directory used for file tools and for workspace context.” citeturn3search0  
The workspace is the default working directory but **not** a hard sandbox; absolute paths can still reach elsewhere unless sandboxing is enabled and configured. citeturn3search0

This means: if you keep client materials in the same workspace (or in reachable host paths) and your tool policies allow file access, then client confidentiality becomes fragile—especially in multi-agent or multi-channel contexts. citeturn3search0turn7search3

OpenClaw does, however, give you a clean path to isolation:

You can maintain multiple workspaces via profiles (the docs describe `OPENCLAW_PROFILE`-based workspace separation) and manage isolated agents with explicit workspace paths via `openclaw agents`. citeturn3search0turn3search5

### GitHub review controls are necessary but not sufficient

On the repo side, review controls help with integrity and governance, but they do not enforce read access boundaries.

You can require reviews from code owners via a CODEOWNERS file plus branch protection (“Require review from Code Owners”), which is useful for enforcing domain ownership and preventing silent drift in critical directories. citeturn1search0turn1search9  
You should also treat secret leakage as inevitable unless you put push-time guardrails in place; GitHub push protection (a secret scanning feature) is explicitly designed to block detected secrets at push time and generate audit alerts when bypassed. citeturn5search1

Those controls improve governance, but if people/tools can still *read* client material they shouldn’t, you haven’t solved your “shielding” requirement. For that, you need structural separation: separate repositories and/or separate OpenClaw instances (`domain=px` vs client instances), consistent with your service boundary architecture. fileciteturn30file17

## Recommended implementation in pxs

The goal is to make “Company-as-Code” work *without* turning your company into a documentation museum. The implementation should therefore be: small number of canonical artifact types, governed creation/update paths, and automatic validation + index generation.

### A naming recommendation that won’t box you in later

Given the existing ecosystem, “Company-as-Code” is understandable and externally legible (and already used by others). citeturn9search3turn9search4  
Internally, you may find it easier to be more precise about layers:

“Model-as-Code” for the business blueprint (A/B/C/D + node cards). fileciteturn18file0turn53file2  
“Policy-as-Code” for anything you intend to enforce automatically (access rules, review gates, tool policies). citeturn1search5turn1search2  
“Execution-as-Code” for decision/task/evidence/review flows implemented in PXS the product. fileciteturn4file7turn4file1

This vocabulary reduces ambiguity between “the model decides how we work” and “the operating system decides how we run changes to the model,” which are different but complementary truths. fileciteturn4file0turn30file8

### A concrete directory design for `docs/instances/px-strategy/`

You already have `docs/instances/px-strategy/` and a `nodes/` folder for the model, plus an `operating-system/` folder for the OS charter. fileciteturn11file0turn53file2turn4file0  
The main gap is to implement your other domains as first-class instance subtrees, while keeping the A/B/C/D node backbone authoritative.

A concrete target layout that stays compatible with what you already have is:

```text
docs/
  framework/                        # portable taxonomy / semantics
  schemas/                          # JSON schemas for validation

  instances/
    px-strategy/
      README.md                     # instance entrypoint

      model/
        enterprise-model.md         # Level 0: strategy & vision (your "Strategy & Vision")
        nodes/                      # current A1..D7 L2 node cards (already exists)
        decisions/                  # model-level decisions that change the blueprint
        evidence/                   # evidence supporting blueprint decisions

      departments/
        INDEX.md                    # registry of departments and their service menus
        executive-office/
          charter.md
          systems.md                # e.g., todo/work tracking tools
          cadences.md
        it-infrastructure/
          charter.md
          asset-register.md
          service-catalog.md
        finance-accounting/
          charter.md
          systems.md
          controls.md
        # ...

      business-units/
        INDEX.md
        pxs-consulting/
          charter.md                # positioning, offerings, P&L model, KPI set
          pipeline.md               # links to CRM views, templates
          assets/                   # reusable deliverables (non-confidential)
        pxs-media/
          charter.md
          editorial-system.md
          asset-inventory.md
        # ...

      client-projects/
        INDEX.md                    # non-confidential index: client list, repo links, status
        templates/
          project-start-packet.md
          security-classification.md

      operating-system/
        pxs-os-charter.md           # current charter (already exists)
        integration-notes.md        # how this instance uses Lyra/OpenClaw

      registries/
        systems.md                  # SaaS/tools in use, owners, renewal dates
        subscriptions.md
        it-assets.md
        partners.md
```

This achieves four things simultaneously:

It preserves your existing “instance” concept and your A/B/C/D model node backbone. fileciteturn20file0turn53file2  
It implements your intended top-level navigation (Model, Departments, Business Units, Client Projects, Operating System) as explicit directories, matching your uploaded structure. fileciteturn0file0turn4file0  
It creates a natural place for “department registries” (CRM, IT assets, subscriptions) without confusing them with the higher-level blueprint. fileciteturn0file0turn18file0  
It creates a deliberate “client-projects index only” pattern, so the sensitive content can live elsewhere (separate repos/workspaces) while the operating system still has visibility into portfolio status. fileciteturn30file17turn7search3

### Make metadata mandatory, then generate everything else

Your OS charter already mandates per-artifact metadata fields and enforces “single canonical location per artifact.” fileciteturn4file0  
To make that scale, the best practice move is: store minimal machine-readable metadata in each artifact and generate indexes/registries automatically (rather than manually curating “master lists” forever). That is the core “docs-as-code + GitOps” sustainability trick: humans write source-of-truth artifacts; machines keep navigation current and detect drift. citeturn0search0turn0search2

In PXS terms, you already have the beginning of this with:

A model-node schema for required fields like id, class, owner, status. fileciteturn4file10  
A node-card template that naturally maps to those fields. fileciteturn22file0  
A “domain model” for decisions/tasks/evidence/reviews, which can become the graph layer that ties everything together. fileciteturn4file7

The next implementation step is to standardize frontmatter for *all* operational artifacts (not only nodes), then:

validate (CI),  
index (build step),  
publish (static site or control panel view).

This is directly aligned with docs-as-code practice (code review + automated checks) and with GitOps governance (Git as source of truth + automated reconciliation/generation). citeturn0search0turn0search6

### Use ADRs for structural decisions, not only software decisions

You already have ADR practice seeded in PXS. fileciteturn4file5turn4file9  
Best practice ADR guidance emphasizes that ADRs are small text files capturing the rationale for significant decisions, kept in-repo, and superseded rather than deleted. citeturn2view0

For Company-as-Code, ADRs become even more valuable because your “architecture” includes organization and governance, not only software. For example, these are ADR-worthy:

“Client projects are stored in separate private repos; instance repo contains only indexes and sanitized metadata.” fileciteturn30file17turn7search3  
“Department registries are generated from frontmatter + YAML inventories; manual edits to INDEX.md are forbidden.” fileciteturn4file0turn0search0  
“Model depth rule: L2 is mandatory baseline, L3+ is optional and only created when a decision requires it.” fileciteturn18file0

### Implement PXS the product as the “execution graph” over the company model

Your PXS v0 domain model defines a minimal end-to-end execution flow: Decision → Task → Evidence → Review, with explicit rules (e.g., tasks can’t be done without evidence). fileciteturn4file7  
Your scope v1 explicitly targets that vertical slice. fileciteturn50file0  
Your backlog seeds already translate this into buildable issues (schema, write paths, lifecycle rules, evidence/review flow, demo). fileciteturn4file6turn4file11

For your Company-as-Code vision, this suggests a very pragmatic implementation stance:

Markdown files remain the human-legible “rulebook” and evidence store (especially for the model and operating policies). citeturn0search0turn0search5  
PXS (software) becomes the system that turns those rules into executable work with traceability, status, and auditability. fileciteturn4file1turn4file7  
Your “Model” tree is the primary classification taxonomy; PXS stores pointers to model nodes (`model_node_ids`), department IDs, business unit IDs, and project IDs to create the graph layer that a tree alone cannot represent. fileciteturn53file2turn4file7

This also aligns tightly with your Lyra/OpenClaw OS principle “jobs first, agents second, runtime third”: define the work objects and lifecycle first, then add agent orchestration on top. fileciteturn30file8turn30file2

## An implementation roadmap that keeps the ambition but avoids “process cosplay”

### Establish the canonical information model and governance gates

Treat this as your “minimum viable Company-as-Code” layer:

Adopt the instance directory design and formalize what goes where (the PXS architecture boundary already supports this separation of concerns). fileciteturn4file4turn20file0  
Make artifact frontmatter mandatory for all operational docs (your OS charter already defines the required fields). fileciteturn4file0  
Add repo-level enforcement: CODEOWNERS mapped to domain owners, branch protection requiring reviews, and secret-scanning push protection for prevention at the perimeter. citeturn1search0turn1search9turn5search1

### Implement client confidentiality as a real boundary

Given OpenClaw’s “workspace is not a hard sandbox” warning, treat client isolation as structural, not procedural:

Create separate OpenClaw workspaces (or separate agents) per client or per confidentiality class, using the documented workspace/profile patterns. citeturn3search0turn3search5  
Follow your own service-boundary rule: separate instances with separate data directories and secrets namespaces. fileciteturn30file17  
Use your existing OpenClaw config change control SOP for any change that impacts tool permissions, sandbox posture, routing, or gateways. fileciteturn27file1

### Build PXS the product in the order your own backlog already recommends

Because your PXS documents already specify v0 entities, rules, and “first five issues,” the sensible move is to honor that sequence and avoid premature UI/perfectionism:

Start with persistence + APIs for Decision/Task/Evidence/Review. fileciteturn4file7turn4file6  
Add lifecycle enforcement (evidence required, blocked requires note), because that’s where “execution quality” becomes real rather than aspirational. fileciteturn4file7turn4file6  
Only then build convenient views (Now/Next/Later, domain views), to avoid optimizing dashboards before you have reliable data. fileciteturn50file0turn30file8

### Mature from docs-as-code to policy-as-code where it matters

You don’t need to “OPA everything,” but the pattern is valuable when you want enforcement rather than guidance:

Use policy-as-code for rules like: “No client project may appear in the PX Strategy instance repo except in INDEX.md,” “All artifacts must have owner + review date,” “No task may be marked done without evidence,” and “No OpenClaw config change merges without the validation bundle output attached.” citeturn1search5turn1search2turn2view0  
Where possible, implement these as CI checks, not human discipline; that is the practical difference between a governable system and a nice wiki. citeturn0search0turn0search2

If you execute the roadmap above, your original structure (Model → Departments → Business Units → Client Projects → Operating System) becomes more than folders: it becomes an enforceable operating reality where decisions propagate into tasks, tasks produce evidence, and audits become queries rather than archaeology. fileciteturn0file0turn4file7turn4file0
