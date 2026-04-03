# Wiki Maintenance in Nightly Loops

Date: 2026-04-03
Owner: Lyra
Status: Draft integration note

## Purpose
Define how wiki maintenance should fit into nightly loops in a bounded and useful way.

The goal is to make the wiki part of the operating system’s compounding cycle without turning every nightly run into uncontrolled documentation churn.

---

## 1. Core principle
Nightly loops should **inform and maintain** the wiki, not blindly rewrite it.

That means:
- nightlies should identify candidate wiki updates
- nightlies should detect wiki gaps and stale areas
- nightlies may apply bounded improvements where confidence is high
- but nightlies should not treat the wiki as a dumping ground for every research or planning artifact

---

## 2. The role of nightlies in the loop
Nightlies already do research, learning, and replanning.

Wiki maintenance should plug into that by adding four questions:

1. What new research or evidence from today deserves a path into raw/evidence storage?
2. What durable insights from recent work deserve wiki promotion or wiki-page updates?
3. What wiki pages are stale, thin, weakly supported, or missing?
4. What planning/action gaps surfaced that should become next research or wiki work?

---

## 3. What nightlies should do

### A. Surface promotion candidates
At the end of a nightly learn/replan pass, identify whether any of the following emerged:
- a reusable concept
- a reusable topic update
- a stable synthesis worth promoting
- a comparison worth keeping
- a page that now needs updating

### B. Surface wiki gaps
The nightly should ask:
- what page should exist but does not?
- what current page is obviously too thin or stale?
- what repeated question indicates missing wiki structure?

### C. Classify, not just create
Nightlies should classify each candidate as:
- `promote_now`
- `update_existing_page`
- `create_new_page`
- `research_next`
- `watch`
- `ignore`

### D. Apply only bounded wiki changes
If the nightly applies wiki updates directly, they should be small and high-confidence.

Good examples:
- update a hub page
- strengthen one obviously stale page
- promote one strong synthesis into a living page
- add a missing link or related-page section

Bad examples:
- large uncontrolled multi-page rewrites
- mass generation of pages from weak material
- rewriting important wiki clusters without clear review value

---

## 4. Where this should happen

### Product / capability nightlies
Each product or capability nightly should surface:
- relevant new research/evidence
- relevant wiki promotion candidates
- domain-specific wiki gaps

### Cross-Lyra wiki maintenance pass
A separate lightweight cross-Lyra maintenance pass should:
- review the Lyra wiki root and domain hubs
- review coverage/gap surfaces
- review stale or weak areas across domains
- make only bounded high-value updates

This avoids overloading every nightly with too much wiki responsibility.

---

## 5. Recommended operating pattern

### Nightly layer 1 — domain-specific signal generation
Product/capability/domain nightlies produce:
- research outputs
- synthesis outputs
- promotion candidates
- gap signals

### Nightly layer 2 — wiki maintenance pass
A lighter cross-cutting pass consumes those signals and decides:
- what to promote now
- what to update
- what to defer
- what to route back into research

This preserves both discipline and compounding.

---

## 6. Guardrails

### Guardrail 1 — wiki is not the raw archive
Do not use nightlies to dump all reports into the wiki.

### Guardrail 2 — wiki is not operational truth
Do not use nightlies to silently rewrite plans/priorities/risks/decisions under the guise of wiki maintenance.

### Guardrail 3 — bounded change only
Nightly wiki maintenance should remain small enough to be trustworthy and maintainable.

### Guardrail 4 — quality over volume
The goal is a clearer, stronger wiki, not more pages.

---

## 7. What the first implementation should look like

### First implementation step
Add a simple nightly wiki-maintenance question set to relevant nightlies:
- what research from today should be preserved in raw/evidence?
- what durable knowledge from today should be promoted into the wiki?
- what wiki page is now missing, stale, or too thin?
- what should be done now vs later?

### Then
Add one bounded cross-Lyra wiki maintenance pass that:
- reviews those signals
- applies small updates
- records remaining gaps

---

## 8. Success condition
The nightly integration is working when:
- useful research reliably finds a path into raw/evidence and then into the wiki
- the wiki becomes progressively more useful and less stale
- plans/actions expose gaps that become the next research and wiki work
- the wiki compounds without becoming noisy or overgrown

---

## 9. Bottom line
Wiki maintenance should be integrated into nightly loops as a bounded compounding function:
- domain nightlies generate promotion and gap signals
- a lighter wiki-maintenance pass handles bounded updates and gap recording
- the result is a wiki that improves through recurring work rather than only through manual wiki-building sessions
