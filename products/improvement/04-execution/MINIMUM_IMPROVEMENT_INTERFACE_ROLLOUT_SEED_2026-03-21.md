# Minimum Improvement Interface Rollout Seed — 2026-03-21

Status: Active seed
Owner: Control Tower / Improvement

## Purpose
Turn the now-approved Phase 1 canonical improvement substrate into the first explicit rollout path for the broader minimum product-side improvement interface across active products.

## Why now
The substrate decision is no longer the main gap.
What remains is operational adoption: active products still need a small, explicit product-side interface that reliably converts material incidents, recurring misses, and review findings into canonical TDE-linked improvement work.

## Reference set
Use these as the canonical reference patterns for rollout:
- `IMP-ERR-20260315-ARCHIVED-REPO-MISUSE-01` — completed end-to-end incident-to-improvement conversion proof case
- `OPS-2026-066`
- `OPS-2026-067`
- `OPS-2026-068`
- `OPS-2026-069`

## Minimum product-side interface to deploy
Each active product should expose, at minimum:
1. a named signal source for improvement-relevant findings
   - incident/error artifact
   - review output
   - recurring operating miss
   - nightly or weekly product/job review
2. an explicit conversion rule
   - material incidents and repeated misses must become canonical TDE-linked improvement work rather than staying as prose-only notes
3. linkage expectations
   - source system
   - source reference
   - product scope
   - evidence links
   - improvement type
   - expected closure evidence
4. closure expectations
   - no improvement item closes without linked closure evidence and explicit source-to-closure trace
5. review cadence expectation
   - open improvement items must be visible in a recurring review loop until dispositioned or closed

## First deployment scope
Start with products/signals that already have the strongest live evidence or backlog pressure:
1. **Security**
   - target signal class: stale findings / explicit disposition gaps
   - seed references: `OPS-2026-067`, `OPS-2026-069`, `SEC-AUTO-20260307-01`, `SEC-AUTO-20260309-02`
2. **Task Management**
   - target signal class: compact-surface drift and product-control gaps
   - seed reference: 2026-03-21 nightly report signal on stale compact steering surfaces
3. **Governance / operating-model hygiene**
   - target signal class: completed proof-case retirement and durable protocol formalization
   - seed reference: `OPS-2026-068`

## First bounded rollout step
Use Security as the first explicit product-side deployment case because it already has live stale-finding items in canonical TDE state plus a clear conversion/disposition gap.

That bounded step should:
- define the stale-finding SLA/disposition expectation as a product-side improvement interface rule
- show how the rule links to canonical TDE items rather than a parallel tracker
- make closure-evidence expectations explicit for stale finding disposition

## Boundary rule
This rollout does **not** create a separate improvement execution system.
Task state remains canonical in TDE.
Improvement owns the closed-loop learning/prevention interface and the source-to-closure discipline around it.

## Intended next artifact consequence
Promote this seed into the canonical product-side interface language in:
- `products/improvement/06-architecture/INTERFACES.md`
- relevant active-product operating/execution surfaces starting with Security
