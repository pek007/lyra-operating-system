---
title: "Deep research on structuring the Lyra OpenClaw markdown workspace"
date: 2026-03-01
source: deepresearch
ingest_from: "telegram attachment file_92"
tags: [external-analysis, deepresearch, workspace-structure]
decision_relevance: "information-architecture and migration governance"
confidence: tbd
status: archived-source
---

# Deep research on structuring the Lyra OpenClaw markdown workspace

## Current state and the core structural failure mode

The repository is functioning as an OpenClaw agent workspace: it contains canonical OpenClaw bootstrap files (for example `IDENTITY.md`, `USER.md`, and a `memory/` daily log pattern) alongside an expanding set of operating documents, governance artifacts, automation scripts, and knowledge assets. This is consistent with how OpenClaw documents the agent workspace as the “home” directory for bootstrap context and memory continuity. fileciteturn22file0L1-L80 citeturn6search0

Your “big dump” impression is not because the system is unstructured in intent; it’s because the structure is being represented in *documents that reference other documents* (registries and indexes) rather than in the filesystem layout itself. Three internal patterns already exist:

- A “single-pane index” control surface (`CONTROL_PANEL.md`) meant to point to core registries and operating docs (principles, systems, processes, risks, subscriptions, etc.). fileciteturn25file0L1-L30 fileciteturn29file0L90-L110  
- A “process registry” approach that treats docs as managed objects with review cadence and status (including data contracts, templates, policies, and even scripts). fileciteturn29file0L100-L135 fileciteturn51file0L55-L70  
- A knowledge base subsystem with defined folders, a naming convention, and a workflow (“inbox → reports → distilled → decisions → indexes”). fileciteturn20file0L1-L120

Those are good primitives, but they currently coexist with a filesystem that still uses the workspace root as the default catch‑all. The result is predictable: the *meaningful structure lives in human-maintained tables and lists*, while the file tree remains non-semantic and accumulates entropy.

A second failure mode is “policy duplication”: governance intent, runtime chartering, and persona content can easily sprawl across `AGENTS.md`, `SOUL.md`, `USER.md`, and governance docs. You already have an explicit rule that mission/objectives/guardrails live in `AGENTS.md` + `governance/`, and that `SOUL.md` should not duplicate operating policy. That rule is directionally correct and should be enforced by structure rather than memory. fileciteturn51file0L1-L30

## OpenClaw constraints and what is safe to change without breaking the runtime

OpenClaw’s behavior creates hard constraints, soft constraints, and “purely conventional” areas.

**Hard constraints (treat as invariant unless you’re deliberately changing how the workspace is bootstrapped):**

OpenClaw expects a set of standard bootstrap files in the agent workspace (loaded at session start), including `AGENTS.md`, `SOUL.md`, `USER.md`, `IDENTITY.md`, and optional files like `TOOLS.md`, `HEARTBEAT.md`, `BOOT.md`, and `BOOTSTRAP.md`, plus a `memory/YYYY-MM-DD.md` pattern for daily context. OpenClaw explicitly documents this file map and that missing files do not prevent startup (but you lose bootstrap context). citeturn6search0

It also documents the default workspace location (`~/.openclaw/workspace` by default, configurable), and explicitly distinguishes the workspace from the state directory `~/.openclaw/` which contains config, credentials, sessions, and logs (which should not be committed into the workspace repo). citeturn6search0

**Soft constraints (changeable, but expect tool/process edit work):**

- If you have automations that assume specific paths (for example `TASKS.md` as the Trello sync input, or `knowledge/evidence/YYYY-MM/` as an evidence sink), moving those requires either:  
  (a) updating tooling configuration/defaults, or  
  (b) keeping stable “compatibility stubs” at the old paths.  
  The current Trello sync approach is explicitly designed around `TASKS.md` and fixed list headings. fileciteturn21file0L1-L120  
  Release-delta and continuous-improvement ops explicitly reference `knowledge/evidence/YYYY-MM/` as a target location. fileciteturn42file0L20-L80
- OpenClaw configuration (`~/.openclaw/openclaw.json` plus included fragments) is operationally sensitive; you already treat changes to channel policy, auth, tool policy, sandboxing, and routing as high risk, with mandatory diff/backup/rollback/validate steps. That implies any restructure that touches “enforced guardrails” needs a disciplined change-control lane. fileciteturn52file0L1-L120

**Purely conventional zones (high freedom):**

OpenClaw does **not** impose any particular folder taxonomy for your operating documents (SOPs, standards, templates, registries, reports) beyond the bootstrap file basenames and the optional `skills/` and `canvas/` folders. You can refactor most of the document library into a coherent directory layout as long as bootstrap files remain in place (or remain injectable). citeturn6search0

Two advanced OpenClaw capabilities matter for “how far you can go”:

- The bundled `bootstrap-extra-files` hook can inject additional bootstrap files from configured paths/globs during agent bootstrap, but only for recognized bootstrap basenames, and it preserves the subagent allowlist (`AGENTS.md` and `TOOLS.md` only for subagents). This is a mechanism to support monorepo-style layouts (for example multiple packages each carrying their own bootstrap overlays) without breaking OpenClaw’s bootstrap contract. citeturn6search2
- Skills have their own loading precedence and can be placed in `<workspace>/skills` (highest precedence) or in shared managed skill directories under `~/.openclaw/skills`. Skill folders require a `SKILL.md` with YAML frontmatter, which implies that if you introduce a workspace “meta tooling layer,” you can align your information model and validation scripts with skills-based execution. citeturn6search4

The practical conclusion: you should treat the workspace root as a **runtime control plane** (bootstrap + tiny entrypoints), and treat the rest as a **document library** that is free to reorganize—provided you preserve a compatibility plan for scripts and cross-links.

## Best-practice patterns for markdown-based operating systems and docs-as-code libraries

Your problem is less “markdown organization” and more “information architecture under version control.” The best practices that map cleanly onto your situation are:

**Filesystem naming: optimize for portability and retrieval, not aesthetics.** Widely used documentation guidance recommends lowercase ASCII names and hyphens over underscores for cross-platform compatibility and searchability, while still prioritizing consistency within existing directories if wholesale renaming is impractical. citeturn7search0 A second, more implementation-minded guideline is to standardize on kebab-case because mixed case and punctuation create subtle interoperability and sorting problems across filesystems and URIs. citeturn7search2

**Documentation taxonomy: separate “kinds of docs” instead of mixing them in one stream.** The Diátaxis framework is the cleanest high-signal abstraction here: tutorials, how‑to guides, reference, and explanation serve different user needs; mixing them produces navigation and maintenance failure. It also recommends that reference documentation’s architecture should reflect the structure of the system being described (map-like). citeturn7search5

Applied to your workspace, this implies: a policy or config reference should not sit in the same folder taxonomy as a workflow template or a daily evidence log, even if they are linked.

**Make “metadata truth” machine-readable, then generate human indexes.** Your current approach relies on manually maintained indexes (control panel, registries). That scales until it doesn’t. In docs-as-code systems, the sustainable pattern is: embed minimal metadata in each artifact, then generate registries, indexes, and dashboards from that metadata (and validate them in CI or cron). Diátaxis tells you what kinds of docs exist; metadata tells you what each file *is*; generation keeps indexes current.

You already have the conceptual seed for this with (a) process registry cadence tracking and (b) a knowledge workflow with normalized naming. fileciteturn20file0L1-L120 The next step is to stop encoding “type” and “version” inconsistently across filenames and document bodies.

## Recommended information model updates aligned to OpenClaw realities

The information model needs to support three properties simultaneously:

- **Runtime efficiency:** keep OpenClaw bootstrap context small and stable; OpenClaw truncates large bootstrap injections by default and encourages keeping heartbeat checklists tiny to avoid token burn. citeturn6search0
- **Operational auditability:** policy → enforcement → evidence chains must be reconstructable, especially for OpenClaw config changes and security posture. fileciteturn52file0L1-L120
- **Library-scale maintainability:** prevent “dump growth” by turning ad-hoc file creation into governed artifact creation.

A workable expert-grade information model for this workspace is an **artifact graph** with controlled vocabularies and typed relationships.

### Artifact types and lifecycle

Define a controlled `artifact_type` vocabulary (examples drawn from what you already use in registries and governance):

- `bootstrap` (OpenClaw session bootstrap files)
- `governance` (charters, policy registers, contracts)
- `policy` (enforceable or normative rules)
- `standard` (definitions of done, naming standards, linking standards)
- `sop` (procedures, change-control, intake/triage)
- `runbook` (ops/security incident/restore procedures)
- `registry` (tables that inventory systems, principles, processes, products)
- `template` (WO/CA/start packet/data contract inventory/system ownership contract)
- `spec` (UI specs, connector specs, architecture specs)
- `guide` (prompting/system prompting guides)
- `log` / `evidence` (security reviews, restore tests, release-delta evidence)
- `knowledge_report` / `knowledge_distilled` / `knowledge_index` (your knowledge subsystem stages) fileciteturn20file0L1-L120

Each artifact gets a lifecycle status: `draft | active | superseded | archived`. You already use “Superseded” in several places; formalize it as a field rather than a convention.

### Metadata schema

Put a short YAML frontmatter block at the top of every non-trivial artifact (excluding OpenClaw bootstrap files where you want to minimize token burn). The model should include:

- `id`: stable identifier (for example `SOP-001`, `ADR-001`, `OPS-001`, or `EVID-...`)
- `artifact_type`: from a controlled vocabulary
- `domain`: from a controlled vocabulary (for example `openclaw`, `security`, `delivery_3pp`, `cadence`, `product`, `knowledge`)
- `owner`: role or person
- `status`
- `created`
- `last_reviewed`
- `next_review`
- `supersedes` / `superseded_by`
- `enforcement`: `prose | tool | config | mixed`
- `evidence_refs`: list of evidence artifact IDs or paths
- `task_refs`: list of task IDs (your `OPS-YYYY-NNN` convention) fileciteturn29file0L140-L165

This model directly supports your stated goal: filesystem structure and the information model evolve in tandem, because the structure becomes *a projection* of the metadata (domain/type), not an arbitrary storage choice.

### Relationship model

At minimum, define these typed edges:

- `implements`: (tool/config/script) → (policy/standard/sop)
- `produces_evidence`: (cron/job/runbook) → (evidence/log artifact)
- `governed_by`: (process/runbook) → (standard/policy)
- `depends_on`: (spec/template/process) → (system of record / registry / data contract)
- `supersedes`: explicit version lineage

Your own governance direction-package work already treats governance docs as source-of-truth and `AGENTS.md` as a compiled runtime charter. Extend that same “source → compiled runtime” idea to registries and indexes: *authoritative metadata lives with artifacts; indexes are generated views.* fileciteturn51file0L1-L40

## Recommended target directory structure and naming conventions

The recommended structure is conceptually a split between:

- **Runtime control plane** (workspace root): OpenClaw bootstrap + minimal human entrypoints.
- **Document library** (subdirectories): everything else, structured by domain and artifact type.
- **Knowledge pipeline** (existing `knowledge/`): keep, but align evidence/log conventions.
- **Automation surface** (`tools/`, `skills/`, optionally `hooks/`): operational code and skill packs.

A target tree that is compatible with OpenClaw’s expectations looks like:

```text
workspace-root/
  AGENTS.md
  SOUL.md
  USER.md
  IDENTITY.md
  TOOLS.md
  HEARTBEAT.md
  BOOT.md
  BOOTSTRAP.md
  MEMORY.md
  memory/

  control/
    control-panel.md
    situational-awareness.md

  registries/
    principles-registry.md
    system-registry.md
    process-registry.md
    risk-register.md
    subscription-register.md
    product-portfolio-registry.md

  governance/
    system-charter.md
    policy-register.md
    agent-catalog.md
    playbook-inventory.md
    task-decision-engine-contract.md
    direction-package.md
    research/

  os/
    principles/
    policies/
    standards/
    sops/
    runbooks/
    models/
    templates/
    adr/

  integrations/
    openclaw/
      config-change-sop.md
      config-change-checklist.md
      prompting-guides/
    trello/

  knowledge/
    inbox/
    reports/
    distilled/
    decisions/
    indexes/
    evidence/

  prompts/
  tools/
  skills/
  assets/
```

### Naming rules

Apply a two-tier naming policy (this is the key to avoiding “dump by version proliferation”):

**Mutable governance/operating artifacts (policies, SOPs, standards, templates, registries):**

- File name is **stable** (no version in filename).
- Version is in metadata/frontmatter (and, if needed, repeated in the doc body).
- For new file names: lowercase + hyphens + ASCII (kebab-case). citeturn7search0 citeturn7search2  
- Keep OpenClaw bootstrap filenames in their conventional forms (`AGENTS.md`, etc.) because OpenClaw expects them by basename. citeturn6search0

**Immutable knowledge/evidence artifacts (reports, evidence captures, time-bound logs):**

- Date-prefixed naming is correct and should remain.
- Keep your existing convention for knowledge assets: `YYYY-MM-DD__source__topic__vN.md`, and treat these as append-only records rather than “living docs.” fileciteturn20file0L25-L70
- Partition high-churn evidence by month (`knowledge/evidence/YYYY-MM/`) as you already do in release-delta and evidence conventions. fileciteturn42file0L20-L80

### Compatibility strategy

To avoid breaking anything while you refactor:

- Keep the workspace root files required by OpenClaw in place. citeturn6search0
- For any file currently referenced widely (control panel, registries, scripts), choose one of two approaches:
  - **Hard move + stub redirect:** leave a thin file at the old path saying “Moved to …” and linking to the new canonical path (preserves old links and human muscle memory).
  - **Soft move via index-only:** keep file where it is but treat the folder path as a taxonomy *for new artifacts only* (lower change risk, slower cleanup).

Given your “don’t destroy anything” constraint, the redirect-stub approach is the most robust: it lets you reorganize aggressively without requiring a simultaneous, perfectly correct global link update.

## Migration and validation plan that preserves runtime integrity

What follows is a sequence that minimizes runtime risk and avoids breaking OpenClaw or your operational tooling.

### Establish invariants and freeze the bootstrap plane

1. Declare the workspace root a **reserved namespace** for OpenClaw bootstrap + a small number of top-level entrypoints (for example `TASKS.md` if you keep Trello defaults). OpenClaw’s own documentation makes clear that these bootstrap files are the stable “workspace file map.” citeturn6search0  
2. Enforce the existing rule “mission/objectives/guardrails live in `AGENTS.md` + `governance/`” as a structural constraint: don’t put system direction in templates or random SOPs. fileciteturn51file0L25-L40

### Build the new folder skeleton and move by artifact class

3. Create the directory skeleton first (empty folders committed). This is low risk and makes the target shape explicit.
4. Move documents by *artifact type*, not by topic:
   - `registries/`: move all registries together so downstream references are easy to update as a block.
   - `os/`: move SOP/STD/Policy/Runbook/Template/ADR by type subfolders.
   - `integrations/openclaw/`: consolidate OpenClaw operational governance (config change-control artifacts, prompting guides, release-delta SOP). Your existing config change SOP already scopes itself to `~/.openclaw/openclaw.json` and related runtime settings, so keeping all OpenClaw “operational governance” together is coherent. fileciteturn52file0L20-L70
   - `governance/`: keep source-of-truth governance artifacts and add a `governance/research/` subfolder for research that informs governance (you already have research vs package separation). fileciteturn19file0L70-L120

5. For each move, leave redirect stubs at the old locations until:
   - control panel links are updated,
   - registries are updated,
   - and link validation passes.

### Align tooling and automations to the new structure

6. Treat every automation as a contract that must be made location-agnostic:
   - For the Trello sync, stop hardcoding the default assumption that `TASKS.md` is at root *unless you want that invariant*; otherwise, update the default path and keep a stub `TASKS.md` at root that points to the canonical location. The current sync script is explicitly keyed to `TASKS.md` and list headings, so moving the file without a compatibility plan will break the integration. fileciteturn21file0L1-L120
7. Keep evidence sinks stable (`knowledge/evidence/YYYY-MM/`) because both release-delta tracking and hygiene/evidence practices rely on that convention. If you need a different evidence taxonomy, layer it under `knowledge/evidence/` rather than renaming the root evidence folder. fileciteturn42file0L20-L80

### Make drift mechanically difficult

8. Implement three validations and run them in cron/CI:
   - **Link integrity:** verify every relative markdown link resolves (including redirects).
   - **Registry integrity:** verify every path referenced in registries exists and (optionally) that each artifact has required metadata.
   - **Type placement rules:** verify that an artifact of type `policy` is under `os/policies/`, `registry` under `registries/`, etc. (exceptions allowed via explicit metadata override).

This is the decisive shift: you stop relying on humans to keep the information model consistent, and instead you let the model *enforce* structure.

### Review gate for OpenClaw config and runtime behavior

9. Any restructure that implies changes to OpenClaw configuration (workspace path changes, multi-agent layouts, sandboxing, hook enablement) must go through your existing change-control workflow (diff, backup, validate, rollback). This is already codified and should remain non-negotiable. fileciteturn52file0L1-L120

If you later decide to adopt a monorepo-style “multiple packages/workspaces” pattern, the safest path is to use the documented `bootstrap-extra-files` hook to inject only recognized bootstrap basenames from subpaths (rather than moving bootstrap files away from the workspace root). citeturn6search2

---

**Bottom line recommendation:** keep the OpenClaw bootstrap plane stable at the workspace root; move everything else into a domain/type-based library layout; introduce a minimal frontmatter-based information model that can generate registries and validate structure; and use redirect stubs to avoid breaking links or scripts during migration. This gives you a filesystem that *expresses* your information model rather than fighting it, while remaining fully compatible with OpenClaw’s documented workspace expectations. citeturn6search0