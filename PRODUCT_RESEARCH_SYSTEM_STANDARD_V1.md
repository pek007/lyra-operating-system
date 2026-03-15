# Product Research System Standard v1

Status: Draft active standard
Owner: Peter / Lyra
Date: 2026-03-15

## Purpose
Define the canonical Product-as-Code standard for how PX Strategy products should build, maintain, and use research capability over time.

This standard exists to prevent product research from degrading into:
- prompt theater
- nightly freeform reporting
- link hoarding
- narrow local optimization
- context-window pollution in Control Tower

The intent is to make research a durable product capability expressed through artifacts, registries, and update flows.

## Core principles
1. **Artifact-first, not prompt-first**
   Prompts may trigger work, but artifacts hold the operating model.
2. **Broad radar, selective depth**
   Each product should watch broadly enough to avoid blind spots, while going deep only where decision value is high.
3. **Research must translate into product impact**
   Valuable research changes doctrine, decisions, plans, controls, interfaces, or roadmap.
4. **Product-local cognition, portfolio-level synthesis**
   Research evaluation belongs inside the relevant product context. Control Tower consumes compact deltas, not raw thought streams.
5. **Doctrine over accumulation**
   The objective is not to collect more text. The objective is to improve the product's current view of reality.

## Design objective
Each product should, over time, become:
- broadly aware of the external and internal developments that matter to it
- explicitly strong in a few critical areas at any given time
- able to explain what it currently believes
- able to show which new findings changed that view
- able to connect research directly to product change

## Research operating model
Each product research system should have two complementary layers.

### 1. Radar layer
Purpose:
- maintain broad situational awareness
- avoid missing important developments
- track themes without prematurely deep-diving them

Characteristics:
- broad coverage
- lightweight entries
- frequent refresh
- low commitment per item

### 2. Deep-dive layer
Purpose:
- develop stronger doctrine in the few areas that matter most now
- support hard decisions and architecture/control changes

Characteristics:
- narrower scope than radar
- richer synthesis
- explicit implications for the product
- maintained only for currently important themes

## Required artifact set
Each product should maintain the following research artifacts under:

`products/<slug>/08-research/`

Recommended structure:

```text
products/<slug>/08-research/
  RESEARCH_MODEL.yaml
  DOMAIN_MAP.md
  RADAR.md
  DEEP_DIVE_INDEX.md
  DOCTRINE.md
  IMPLICATIONS.md
  SOURCES.md
```

Optional subfolders when the product needs them:

```text
products/<slug>/08-research/deep-dives/
products/<slug>/08-research/intake/
products/<slug>/08-research/sources/
```

## Mandatory artifacts

### 1. `RESEARCH_MODEL.yaml`
Purpose:
- machine-readable research backbone
- support automation, validation, and synthesis

Should contain at minimum:
- `product_id`
- `product_name`
- `owner`
- `broad_domains`
- `priority_themes`
- `watch_sources`
- `review_cadence`
- `deep_dive_limit`
- `promotion_rules`
- `artifact_paths`
- `last_reviewed_at`

### 2. `DOMAIN_MAP.md`
Purpose:
- define the full domain surface the product should watch
- preserve big-picture scope boundaries

Should answer:
- what domains materially affect this product?
- which domains are core, adjacent, and peripheral-but-relevant?
- which areas are currently priority themes for depth?
- which areas are monitored mainly for change detection?

Rule:
- prefer slightly too broad over too narrow
- do not confuse domain coverage with equal depth everywhere

### 3. `RADAR.md`
Purpose:
- maintain the broad watch surface
- record meaningful developments at lightweight resolution

Entries should be short and classified, for example:
- new practice or pattern
- new risk/threat
- new tool/platform capability
- new standard or regulatory development
- new architecture idea
- new evidence affecting prior belief

Each entry should state:
- what changed
- why it matters or may matter
- theme/domain
- disposition: `ignore | watch | deepen | incorporate | escalate`

### 4. `DEEP_DIVE_INDEX.md`
Purpose:
- track active and recent deep analyses
- keep deep work bounded and visible

Should contain:
- active deep-dive topics
- why each topic matters now
- owner/session
- current status
- linked deep-dive artifact
- expected decision or product impact

Rule:
- every product should maintain only a limited number of active deep dives at once
- broad awareness should not imply broad deep work

### 5. `DOCTRINE.md`
Purpose:
- capture the product's current synthesized view
- become the stable "what we believe now" artifact

Should focus on:
- current best understanding
- important principles/patterns
- current default positions
- known unresolved questions
- confidence and limits stated plainly in words

Rule:
- this is the main anti-junk-drawer artifact
- update only when understanding meaningfully changes

### 6. `IMPLICATIONS.md`
Purpose:
- connect research directly to product change

Should record implications for:
- architecture
- controls
- roadmap
- priorities
- delivery mode
- interfaces
- operational posture
- escalation needs

Rule:
- if research matters, the impact should appear here or in a linked canonical product artifact

### 7. `SOURCES.md`
Purpose:
- document preferred source hierarchy and notable recurring sources
- make source quality explicit

Should include:
- canonical internal sources
- vendor/product documentation
- standards/frameworks/regulatory sources
- trusted technical/security research sources
- lower-priority discovery channels

Rule:
- source quality should be explicit rather than left to runtime improvisation

## Optional artifact patterns
Use only when justified.

### `08-research/deep-dives/<TOPIC>.md`
For substantial analysis of an active priority theme.

### `08-research/intake/YYYY-MM-DD__<topic>.md`
For temporary intake/scratch synthesis before promotion into radar, doctrine, or implications.

### `08-research/sources/<source-group>.md`
For stable curated source lists where needed.

## Standard lifecycle

### Daily / nightly cycle
The product runtime should:
1. scan relevant source surfaces
2. compare candidate findings against existing domain map, radar, and doctrine
3. discard obvious duplicates and low-value noise
4. update `RADAR.md` only for meaningful deltas
5. create or update deep dives only when promotion rules are met
6. update `IMPLICATIONS.md` and linked product artifacts if product impact is real
7. emit only a compact machine-usable synthesis delta for Control Tower

### Weekly cycle
The product runtime should:
1. review radar patterns
2. decide which watch items should be promoted, downgraded, or dropped
3. refresh active deep-dive priorities
4. update doctrine where accumulated evidence changed the product's view
5. prune stale or low-value material

### Monthly / milestone cycle
The product owner should:
1. review whether the domain map is still broad enough
2. test for blind spots or overconcentration
3. reassess source quality and deep-dive allocation
4. update the product model if research changes strategic or architectural posture

## Promotion rules
A radar item should be promoted to deeper analysis only when at least one of the following is true:
- it could materially change architecture, controls, roadmap, or operating posture
- it indicates a rising risk or major opportunity
- it conflicts with current doctrine
- it affects a live decision or blocker
- repeated weak signals now form a meaningful pattern

Otherwise it should remain light, be watched, or be discarded.

## Breadth rule
Products should optimize to avoid blind spots, not to prove exhaustive expertise in every subdomain.

Default posture:
- broad awareness across the full relevant domain surface
- deliberate depth in a few currently critical themes
- explicit acknowledgment of out-of-focus areas rather than silent omission

## Source hierarchy rule
Prefer sources in this order unless product-specific doctrine says otherwise:
1. internal canonical artifacts and runtime evidence
2. official product/vendor documentation
3. standards, regulations, and primary technical references
4. high-quality technical or security analysis
5. secondary commentary and industry summaries
6. social/media chatter for weak-signal discovery only

## Translation rule
Research work is incomplete unless it lands in at least one of these places:
- `DOCTRINE.md`
- `IMPLICATIONS.md`
- a linked canonical product artifact
- a decision artifact
- a roadmap/plan/control update
- an explicit no-action record with rationale

## Reporting rule
Control Tower should not receive full product research narratives by default.

Products should emit only compact deltas such as:
- doctrine changed
- new risk/opportunity added to radar
- deep dive opened/closed
- product implication recorded
- escalation required

The 06:00 report should synthesize those deltas into a short portfolio view.

## Anti-patterns
Avoid:
- using prompts as the primary system of record
- treating article accumulation as research maturity
- narrowing the domain map to only current work items
- deep-diving every topic equally
- pushing raw research streams into the main session
- using color statuses as a substitute for explicit factual state
- storing findings without product implications

## Minimal implementation expectation
A product research system is minimally valid when it has:
1. a defined domain map
2. a broad radar surface
3. a bounded deep-dive mechanism
4. a current doctrine artifact
5. an implication trail into product change
6. a machine-readable research model
7. compact synthesis output for Control Tower

## Relationship to Product-as-Code
This research layer extends the product model; it does not replace it.

Research artifacts should feed:
- `02-strategy/*`
- `03-operating-model/*`
- `04-execution/*`
- `05-performance/*`
- `06-architecture/*`
- `07-decisions/*`

A product that researches without updating its canonical model is not learning as code.

## Example: Security product scope pattern
For `products/security/`, a broad but relevant domain map would likely include:
- OpenClaw security architecture and controls
- agent runtime isolation and trust boundaries
- identity, auth, and secret handling
- tool permission and execution safety
- model risk, prompt injection, and output misuse
- browser, node, and device attack surfaces
- dependency and supply-chain security
- infrastructure exposure posture for local, VPS, and tailnet setups
- monitoring, logging, auditability, and incident response
- external cyber developments that could materially affect AI-agent environments

Depth should then be concentrated only on the few themes most decision-relevant now.

## Version
- v1.0
- Date: 2026-03-15
- Owner: Peter / Lyra
