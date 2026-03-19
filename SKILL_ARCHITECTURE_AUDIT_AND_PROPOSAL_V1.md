# Skill Architecture Audit and Proposal v1

Status: Draft
Owner: Lyra
Date: 2026-03-19

## Purpose
Assess the current skill estate against the emerging Product-as-Code and Capability-as-Code architecture, and define a practical operating model that prevents loose, unowned skills.

## Core conclusion
The right rule is **not** `Products > Capabilities > Skills` as a mandatory universal hierarchy.

The right rule is:

**Products own capabilities. Capabilities choose delivery modes. Skills are one delivery mode / artifact form for some capabilities.**

This preserves architectural clarity while preventing the creation of loose skills that are not connected to an owning product and capability.

## Architectural position

### Canonical stack
- **Product** = why the system power exists and who it is for
- **Capability** = what useful power the product actually provides
- **Delivery mode** = how that capability reaches a consumer
- **Artifact** = the concrete implementation/package used in that delivery mode

In shorthand:

`Product -> Capability -> Delivery mode -> Artifact`

### Skill rule
A skill should be treated as:
- a delivery artifact for a capability, or
- a platform/shared enablement artifact in the shared capability layer

A skill should **not** be created as an orphaned convenience object with no explicit owner, no capability link, and no evidence path.

## Relevant architectural anchors already present
This proposal aligns with:
- `CAPABILITY_MODEL_STANDARD_V1.md`
- `DELIVERY_MODES_DECISION_FRAMEWORK_V1.md`
- `PRODUCT_PORTFOLIO_REGISTRY.md`
- `SKILL_CONCEPTS_FIRST_WAVE_V1.md`

Those artifacts already imply:
- products remain the strategic ownership unit
- capabilities are the unit of useful system power
- skills are one delivery mode among several
- product-local skill work should be capability-linked, narrow, and evidence-oriented

## Audit scope
Scanned skill roots:
- core OpenClaw skills: 53
- ACP extension skills: 1
- workspace-local skills: 1

Total scanned: **55 skills**

## High-level audit findings

### 1. The current estate is dominated by platform/tool wrapper skills
Most installed skills are generic wrappers around:
- CLIs
- APIs
- device integrations
- communication tools
- media utilities
- coding/runtime helpers

Examples:
- `github`
- `1password`
- `weather`
- `tmux`
- `notion`
- `gog`
- `xurl`
- `openai-whisper`

These are generally **shared/platform enablement skills**, not product-owned capabilities.

### 2. Very few skills are explicitly tied to Product-as-Code ownership
Only one clearly local, product-shaped skill is present:
- `skills/control-panel-coordination`

This means the current skill layer is useful, but architecturally shallow. It mostly improves tool access, not product capability embodiment.

### 3. Most skills are thin wrappers rather than capability bundles
Observed pattern:
- many skills have only `SKILL.md`
- a minority include `references/`
- a smaller minority include `scripts/`
- almost none visibly connect to product capability records, evidence paths, or readiness states

This is acceptable for platform/shared utility skills, but weak for product-owned capability delivery.

### 4. Verification-oriented skills are underrepresented
The strongest gap relative to high-leverage architecture is verification.

The current estate includes useful operational and tool-facing skills, but there are few explicit capability-linked skills for:
- proof/verification loops
- evidence packaging
- post-change validation
- operational integrity checks
- capability readiness confirmation

### 5. Metadata quality is inconsistent
Notable examples:
- `canvas` has an empty description
- workspace `control-panel-coordination` lacks YAML frontmatter metadata entirely

That weakens trigger quality and architectural discoverability.

## Current skill classification

### A. Platform/shared enablement skills
These are acceptable as shared capabilities or shared delivery artifacts.
They do **not** need to map directly to a single product capability, but they should be recognized as platform/shared capability assets.

#### Tool/API/communication skills
- `1password`
- `apple-notes`
- `apple-reminders`
- `bear-notes`
- `bluebubbles`
- `discord`
- `github`
- `gog`
- `himalaya`
- `imsg`
- `notion`
- `obsidian`
- `slack`
- `things-mac`
- `trello`
- `wacli`
- `xurl`

#### Device/media/environment skills
- `camsnap`
- `eightctl`
- `gifgrep`
- `nano-banana-pro`
- `nano-pdf`
- `openai-image-gen`
- `openai-whisper`
- `openai-whisper-api`
- `openhue`
- `peekaboo`
- `sag`
- `sherpa-onnx-tts`
- `songsee`
- `sonoscli`
- `spotify-player`
- `video-frames`
- `voice-call`
- `weather`

#### Runtime/tooling/operator skills
- `acp-router`
- `blogwatcher`
- `blucli`
- `clawhub`
- `coding-agent`
- `gemini`
- `gh-issues`
- `goplaces`
- `mcporter`
- `model-usage`
- `node-connect`
- `oracle`
- `ordercli`
- `session-logs`
- `skill-creator`
- `summarize`
- `tmux`

### B. Product capability skills
Current clear example:
- `control-panel-coordination`

This is the strongest signpost for the desired future pattern: narrow, bounded, process-shaped, and tied to an explicit operating need.

### C. Misaligned / weakly-formed skills
These should be reviewed first because they weaken trust in the skill layer.

#### Immediate metadata/quality issues
- `canvas` — empty description; poor triggerability and unclear scope
- `control-panel-coordination` — no YAML frontmatter metadata; should be upgraded to valid skill shape

#### Ambiguous ownership or mixed-purpose patterns
These are not necessarily bad, but should be reviewed for boundary clarity:
- `healthcheck` — potentially a strong product capability skill, but currently reads partly as a generic host audit skill
- `coding-agent` — powerful routing/operator skill, but broad enough that it risks spanning too many intents
- `gh-issues` — workflow-heavy and valuable, but more like a mini operational subsystem than a simple skill
- `node-connect` — likely a good product capability skill if anchored clearly to the relevant product/capability owner

## Proposed architectural model for skills

### Skill categories
Every skill should belong to exactly one primary category.

#### 1. Shared platform skill
Use when the skill mainly exposes or teaches a tool, API, runtime, or shared operator utility.

Required control questions:
- What shared capability does this support?
- Who owns the underlying platform/tool contract?
- Is this a stable shared asset or an ad hoc local convenience?

#### 2. Product capability skill
Use when the skill packages a specific product-owned capability for guided use.

Required control questions:
- Which product owns this?
- Which capability ID does it implement or expose?
- Why is `skill` the right delivery mode?
- What evidence proves the capability works?

#### 3. Transitional/local skill
Use only when a skill is still exploratory or workspace-local.

Required control questions:
- What product/capability is it expected to attach to later?
- What would promote it to a formal capability-linked skill?
- What would retire or replace it?

This category should be temporary.

## Required rule for future product-owned skills
Before creating or promoting any **product-owned** skill, define:
- owning product
- capability ID
- capability purpose
- consumer(s)
- delivery mode rationale
- canonical artifact refs
- evidence / verification path
- readiness state
- lifecycle state

If those do not exist, the skill should remain either:
- a shared platform skill, or
- a temporary local workspace artifact

## Delivery-mode selection rule
Use a skill only when the capability is primarily delivered through guided agent/operator behavior.

A skill is a good fit when:
- the capability is workflow-oriented
- the main interface is instructions + references + optional scripts
- iteration speed matters
- hard enforcement is not the core requirement
- bounded verification can be expressed procedurally

A skill is a weak fit when the capability mainly needs:
- hard runtime enforcement -> plugin/service
- machine-readable contract -> schema-pack
- cross-product rule enforcement -> policy-pack
- local early proof with no packaging need -> workspace artifact
- multi-artifact promoted release unit -> assembly

## First-wave product capability skill proposal
These are the best next candidates for capability-linked skills.

### 1. Control Panel coordination skill
- **Product:** `CP-001` Control Panel
- **Likely capability:** bounded coordination / same-runtime handoff orchestration
- **Delivery mode fit:** strong skill fit
- **Need:** add proper metadata, capability linkage, evidence references

### 2. Governance VERIFY-cycle skill
- **Product:** `A-008` Governance
- **Likely capability:** bounded governance verification cycle execution
- **Delivery mode fit:** strong skill fit
- **Need:** evidence/output path and escalation criteria already conceptually clear

### 3. Task Management / TDE operator skill
- **Product:** `A-007` Task Management
- **Likely capability:** bounded TDE operator workflow / continuity-safe task-state action
- **Delivery mode fit:** good skill + ops-pack pairing
- **Need:** explicit link to DB-canonical/TDE authority model

### 4. Delivery verification skill
- **Product:** `A-006` Delivery
- **Likely capability:** evidence-backed verification of shipped work
- **Delivery mode fit:** strong skill fit if paired with scripts and evidence templates
- **Gap addressed:** current underweight verification layer

### 5. Security / deployment health audit skill
- **Product:** `A-004` Security
- **Likely capability:** bounded host/gateway posture verification
- **Delivery mode fit:** skill + scripts, possibly later plugin/policy support
- **Note:** could absorb/refine current `healthcheck` patterns in a product-owned form

### 6. Interfaces contract-pack validation skill
- **Product:** `A-009` Interfaces
- **Likely capability:** contract/package/compatibility validation for downstream consumers
- **Delivery mode fit:** skill + schema/ops-pack companion artifacts
- **Value:** supports the as-code export/import boundary discipline

## Specific recommendations for the current skill estate

### Immediate fixes
1. Repair invalid/weak metadata
   - add description/frontmatter to `control-panel-coordination`
   - add missing/clear description to `canvas`

2. Create a lightweight skill portfolio map
   - classify each skill as `shared-platform`, `product-capability`, or `transitional-local`
   - record owner and review status

3. Define review gate for new local skills
   - no new local skill without ownership classification
   - no product-owned skill without capability linkage

### Near-term structural work
4. Promote first-wave concept skills into real capability-linked implementations
   - control-panel-coordination
   - governance-verify-cycle
   - task-management-tde-operator

5. Add at least one high-value verification skill
   - preferably Delivery or Security first

6. Push deterministic logic into scripts/references
   - keep SKILL.md lean
   - use references for detailed instructions
   - use scripts for stable repeated checks

### Governance / architecture work
7. Add a formal skill architecture standard
   Define:
   - skill categories
   - ownership rules
   - capability linkage rules
   - delivery mode decision rule
   - promotion/retirement path
   - evidence expectations for product-owned skills

8. Add a shared capability inventory entry for platform/shared skills
   This prevents generic tool skills from looking ownerless while avoiding fake product-local ownership.

## Proposed minimum metadata model for skill governance
For governance purposes, every skill should have a registry entry with at least:
- skill name
- category (`shared-platform|product-capability|transitional-local`)
- owner
- source path
- owning product (if applicable)
- capability ID (if applicable)
- delivery mode rationale
- readiness
- evidence refs
- review date
- status (`active|improving|retiring`)

This metadata does **not** need to live in YAML frontmatter if the runtime expects only `name` and `description` there.
A separate registry is cleaner.

## Recommended canonical rule
**No loose skills.**

Interpretation:
- every skill must either belong to a shared/platform capability layer or to an explicit product capability
- no skill should exist without declared ownership, scope, and review path
- product-owned skills must be capability-linked before promotion

## Recommended next actions
1. Normalize the current local skill (`control-panel-coordination`) into a valid frontmatter-based skill.
2. Create `SKILL_ARCHITECTURE_STANDARD_V1.md`.
3. Create a `SKILL_PORTFOLIO_REGISTRY.md` with ownership/classification.
4. Define the first 3 product capability skill records:
   - Control Panel coordination
   - Governance VERIFY-cycle
   - Task Management / TDE operator
5. Select one verification-heavy skill to build next, likely under Delivery or Security.

## Bottom line
The current skill estate is useful, but mostly as a shared tooling layer.
To fit the broader as-code architecture, the next step is not “more skills” — it is **governed skills**:
- owned
- capability-linked where relevant
- delivery-mode justified
- evidence-aware
- narrow enough to remain legible

That gives Lyra OS a skill layer that behaves like architecture, not just convenience.
