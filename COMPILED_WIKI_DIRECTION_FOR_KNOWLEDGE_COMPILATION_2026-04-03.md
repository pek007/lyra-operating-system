# Compiled Wiki Direction for Knowledge Compilation

Date: 2026-04-03
Owner: Lyra
Status: Draft design note

## Purpose
Define how the Knowledge Compilation capability should evolve in the direction of a genuinely useful compiled wiki, and clarify how that should differ between Lyra and PXS.

This note exists because the current pilots are structurally strong but not yet fully human-legible in the richer sense that a compiled wiki could provide.

---

## 1. Core position
Knowledge Compilation is the capability.

A **compiled wiki** is a major human-facing representation mode of that capability.

That means:
- the wiki is not the whole capability
- but it is the most important browse/navigation/view layer for humans
- and a likely key requirement if the capability is to become genuinely useful for management, synthesis, and reuse

---

## 2. Why move in the wiki direction

The current system already does several important things:
- raw ingest
- source summaries
- concept pages
- topic pages
- synthesis notes
- indexes
- output artifacts

But this is still closer to a disciplined compiled knowledge archive than a fully legible compiled wiki.

The wiki direction matters because it improves:
- human understanding of coverage
- discoverability
- navigability
- reusability
- gap visibility
- cross-linking between ideas
- confidence that the system is building usable knowledge rather than only more files

In short:
- a knowledge compiler helps create structure
- a compiled wiki helps humans see and use that structure

---

## 3. The intended architecture

### Capability layer
**Knowledge Compilation**
- ingest
- compile
- structure
- link
- synthesize
- lint
- file back outputs

### Representation/view layer
**Compiled Wiki**
- living topic pages
- living concept pages
- entity pages where useful
- comparison pages
- synthesis hubs
- browse indexes and domain maps
- visibility into coverage and gaps

### Governance boundary
**Operational truth remains separate**
- plans
- priorities
- decisions
- risks
- canonical state
- governance commitments

The compiled wiki may support these areas, but it should not silently replace them as system-of-record surfaces.

---

## 4. Lyra wiki vs PXS wiki

These should not be one merged wiki.

### Lyra wiki
Purpose:
- represent Lyra-level capabilities, architecture, controls, workflows, patterns, and cross-workspace knowledge

Likely domains:
- capabilities
- architecture
- control/security concepts
- operating patterns
- tools and agent patterns
- governance concepts
- knowledge-compilation and wiki methods themselves

Character:
- platform/system oriented
- reusable across workspaces
- capability and architecture heavy
- more general and cross-context

### PXS wiki
Purpose:
- represent PX Strategy business/domain intelligence and delivery-relevant knowledge

Likely domains:
- offerings
- industries/themes
- clients/accounts
- markets
- business units
- tools/products in PXS context
- delivery patterns
- commercial and strategic intelligence

Character:
- business/domain oriented
- tied to PXS use and value creation
- less meta/platform-centric than the Lyra wiki

### Shared logic, separate instances
The two wikis should share:
- the Knowledge Compilation capability model
- structural conventions where helpful
- some templates and patterns

But they should remain separate knowledge spaces with distinct purpose and scope.

---

## 5. What makes something a wiki page

A useful distinction:

### Usually not wiki pages
- raw source captures
- transient logs
- many one-off output artifacts
- ephemeral execution notes

### Usually yes, wiki pages
- concept pages
- topic pages
- entity pages
- comparison pages
- stable synthesis pages
- domain maps / index hubs / coverage pages

### Borderline / conditional
- synthesis notes
- some output artifacts
- some research notes

Rule of thumb:
If the artifact is meant to be a durable browseable node in the knowledge space, it should become or feed a wiki page.

---

## 6. Wiki page types to standardize

### A. Concept pages
Purpose:
- define reusable concepts
- distinguish nearby ideas
- link to supporting sources and related topics

### B. Topic pages
Purpose:
- aggregate a domain/theme
- hold current understanding, subthemes, open questions, related concepts/sources

### C. Entity pages
Purpose:
- represent a specific company, tool, standard, actor, protocol, product, or named object where useful

### D. Comparison pages
Purpose:
- compare approaches, tools, models, patterns, or positions side-by-side

### E. Synthesis hub pages
Purpose:
- aggregate major syntheses and current position in an area

### F. Domain/index/map pages
Purpose:
- provide navigation, coverage view, and gap visibility

---

## 7. What is still missing from our current implementation

### 1. Dense cross-linking
Pages should more actively link across concepts, topics, sources, and syntheses.

### 2. Backlink-aware maintenance
As concepts evolve, linked pages should be revisited intentionally.

### 3. Better browse hubs
The current indexes are useful but still thin.
We need richer domain maps and coverage pages.

### 4. More living pages, fewer frozen dated notes
Some current syntheses and notes should eventually be promoted into living wiki pages rather than remaining only date-stamped artifacts.

### 5. More explicit gap visibility
A compiled wiki should help answer:
- what do we know?
- what is weakly supported?
- what is missing?
- what should exist but does not yet?

### 6. Better human view layer
Even without a new app, stronger wiki navigation should make the system visibly legible to a human browsing the files.

---

## 8. Recommended next moves

### For Lyra wiki direction
- define top-level Lyra wiki domains
- create first richer hub pages in the Lyra capability space
- promote major concept/topic pages into more clearly living wiki pages

### For PXS wiki direction
- identify the first bounded PXS knowledge domain that would benefit from a compiled wiki view
- keep it separate from Lyra platform/capability knowledge
- apply the same capability model with business-domain page types

### For the capability overall
- standardize page types and templates
- define promotion rules from note -> wiki page
- add backlink/related-page conventions
- add coverage/gap pages

---

## 9. Design rule
The goal is not to create a messy freeform wiki.

The goal is to create a **disciplined compiled wiki**:
- source-traceable
- artifact-backed
- linked
- human-browseable
- LLM-maintained where appropriate
- clearly separate from governed operational truth

---

## 10. Bottom line
The right direction is:
- keep **Knowledge Compilation** as the capability
- evolve the compiled layer into a stronger **compiled wiki** representation
- maintain **separate Lyra and PXS wiki instances**
- and make the wiki legible enough that a human can see what is covered, what is missing, and how the knowledge space is structured.
