# Skill Architecture Standard v1

Status: Draft active standard
Owner: Lyra OS
Date: 2026-03-19

## Purpose
Define how Skills fit into the Lyra OS as-code architecture, how they should be governed, and how they move through a lifecycle from creation to retirement.

This standard exists to prevent loose, unowned skills and to make Skills operationally reliable rather than ad hoc prompt artifacts.

## Core rule
**No loose skills.**

Every skill must belong to one of these categories:
- **shared-platform**
- **product-capability**
- **transitional-local**

Every skill must also have:
- an owner
- a review path
- a lifecycle state
- a reason to exist

## Architectural position
Skills are **not** a top-level architecture layer on their own.

Use this stack:
- **Product** = why the system power exists and who it is for
- **Capability** = what useful power the product actually provides
- **Delivery mode** = how that capability reaches a consumer
- **Artifact** = the concrete implementation/package

In this stack, a Skill is one possible delivery artifact.

### Short rule
`Product -> Capability -> Delivery mode -> Artifact`

When the chosen delivery mode is `skill`, the artifact is a skill package/folder.

## Skill categories

### 1. shared-platform
Use when the skill mainly exposes or improves access to:
- tools
- CLIs
- APIs
- runtime helpers
- generic operator utilities

These skills do not need to map to a single product capability, but they must still belong to the shared/platform capability layer.

Examples:
- GitHub CLI operations
- weather lookup
- tmux control
- media extraction
- coding-agent routing

### 2. product-capability
Use when the skill packages a capability owned by a product.

These skills must be linked to:
- owning product
- capability ID
- delivery mode rationale
- evidence path

Examples:
- Control Panel coordination
- Governance VERIFY-cycle
- TDE operator workflow
- product-specific verification capability

### 3. transitional-local
Use when the skill is local, exploratory, or not yet mature enough for promotion.

This category is allowed only temporarily.
A transitional-local skill must still declare:
- intended owner
- expected promotion path or retirement trigger
- review date

## Decision rule: when to use a Skill
A Skill is a good fit when:
- the capability is mainly delivered through guided agent/operator behavior
- the interface is instructional, procedural, or workflow-shaped
- reusable references or scripts improve repeatability
- hard runtime enforcement is not the main requirement
- fast iteration matters

A Skill is a weak fit when the capability mainly needs:
- hard runtime behavior -> plugin or service
- machine-readable contract -> schema-pack
- cross-product rule enforcement -> policy-pack
- early local proof with no packaging need -> workspace artifact
- promoted multi-artifact transfer unit -> assembly

## Required ownership model

### All skills
Every skill must have:
- skill name
- category
- owner
- source path
- lifecycle state
- readiness state
- review date
- status

### Product-capability skills
Every product-capability skill must also have:
- owning product
- capability ID
- capability purpose
- primary consumers
- delivery mode rationale
- canonical artifact refs
- evidence refs
- improvement trigger
- retirement trigger

### Shared-platform skills
Every shared-platform skill must also have:
- shared capability area
- underlying tool/system owner where known
- dependency or contract notes where relevant

## Skill lifecycle management
Skills should be managed explicitly, similar to capabilities.

### Lifecycle states
Use these states:
- **proposed**
- **approved**
- **building**
- **testing**
- **active**
- **improving**
- **constrained**
- **retiring**
- **retired**

### Readiness states
Use these states:
- **draft**
- **usable**
- **proven**
- **scaled**

Lifecycle state answers: *where in the management process is this skill?*
Readiness answers: *how dependable and reusable is it?*

A skill may be:
- `active` but only `usable`
- `improving` and already `proven`
- `constrained` because of known limitations or safety concerns

## Lifecycle workflow

### 1. Create
Before creating a new skill, answer:
- what repeated problem does it solve?
- who owns it?
- is this truly a skill-shaped problem?
- is the skill shared-platform or product-capability?
- what evidence would prove it is useful?

For product-capability skills, define the capability link before promotion.

### 2. Design
Keep the design narrow.
Require:
- clear triggers
- bounded scope
- explicit non-goals
- references/scripts only where they add repeatable value

Prefer one job per skill.
Avoid mixed-purpose skills that span multiple categories.

### 3. Build
During build:
- keep `SKILL.md` lean
- put detailed material in `references/`
- put deterministic repeated logic in `scripts/`
- keep frontmatter limited to `name` and `description`
- ensure the registry stores the governance metadata not suitable for frontmatter

### 4. Test
Every new or materially changed skill should be tested.

Minimum test types:
- **trigger test** — does the description actually match intended use cases?
- **workflow test** — can the skill successfully guide one real or simulated task?
- **resource test** — do bundled scripts/references behave as expected?
- **boundary test** — does the skill stay within scope and escalate correctly?

If a skill includes scripts, actually run them.
If a skill is operational/procedural, test at least one representative run.

### 5. Activate
A skill becomes active only when:
- ownership is declared
- category is declared
- lifecycle/readiness are set
- tests have been run to a reasonable level
- registry entry exists

### 6. Improve
A skill should move to `improving` when:
- it repeatedly struggles in live use
- trigger quality is weak
- references/scripts are missing or stale
- output quality is inconsistent
- better verification or tighter boundaries are needed

Improvement inputs may come from:
- user friction
- review findings
- incidents
- capability reviews
- product reviews
- repeated model mistakes

### 7. Maintain
Active skills require periodic review.
Review should confirm:
- trigger still valid
- owner still correct
- linked capability still valid
- references/scripts still accurate
- delivery mode still appropriate
- evidence of value still exists

### 8. Constrain
Use `constrained` when a skill remains useful but has known limitations that matter.
Examples:
- auth/tooling prerequisites fragile
- high drift risk
- partial environment support only
- unsafe for unattended or high-impact use

A constrained skill should have explicit notes and an improvement or retirement path.

### 9. Retire
Retire a skill when:
- the capability is no longer needed
- another delivery mode replaced it
- a stronger canonical skill superseded it
- the underlying tool is obsolete
- maintenance cost exceeds value

Retirement should record:
- why it is retiring
- what replaces it, if anything
- whether the folder is removed, archived, or left as historical artifact

## Skill review cadence
Suggested default cadence:
- **new skills:** review within 2 weeks of activation
- **active product-capability skills:** monthly or product review cadence
- **shared-platform skills:** quarterly unless they change often
- **constrained skills:** more frequently until resolved

## Registry requirement
The canonical governance surface for skills should be a registry.

Suggested artifact:
- `SKILL_PORTFOLIO_REGISTRY.md`

The registry should carry the management metadata that does not belong in skill frontmatter.

## Testing and evidence rule
A skill is not fully trustworthy because it exists.
It should have evidence appropriate to its role.

Examples:
- shared-platform skill -> representative successful use cases
- product-capability skill -> linked evidence or product artifact outputs
- verification skill -> proof that it catches or validates the intended conditions

### Short rule
A skill without testing may exist, but it should not be treated as proven operational capability.

## Improvement loop rule
Skills should feed the same closed-loop improvement model used elsewhere:
- use
- observe friction/failure
- classify issue
- update skill or related artifacts
- retest
- record the result

This is effectively a **skill-for-skills** discipline, but it should live as architecture and governance rather than only as another skill.

## Anti-patterns
Avoid:
- loose skills with no owner
- skills with no declared category
- product-owned skills with no capability link
- using a skill where plugin/schema/policy/service is the better delivery mode
- giant mixed-purpose skills spanning several unrelated jobs
- bloated `SKILL.md` files that should have references/scripts
- inactive skills that remain installed without review

## Minimum registry record template
```md
| Skill | Category | Owner | Product | Capability ID | Lifecycle | Readiness | Review date | Notes |
|---|---|---|---|---|---|---|---|---|
```

## Practical operating rule
Before claiming a skill is part of the architecture, be able to answer:
1. who owns it?
2. what problem does it solve repeatedly?
3. what category is it?
4. if product-owned, which capability does it serve?
5. why is `skill` the right delivery mode?
6. what evidence shows it works?
7. what would improve, constrain, or retire it?

If those questions cannot be answered, the skill is not yet properly governed.

## Version
- v1.0
- Date: 2026-03-19
- Owner: Lyra OS
