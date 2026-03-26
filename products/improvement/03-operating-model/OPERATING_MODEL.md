# Operating Model

Improvement runs as a portfolio loop: observe friction, incidents, misses, and review findings; convert them into explicit improvement work; test or deploy safely; and retain what demonstrably improves the system.

Improvement is therefore a compounding loop product. It should work closely with Task Management, but it should not collapse into being merely the task board itself.

## Phase 1 canonical execution model
Improvement uses Task Management / TDE as its canonical execution substrate without changing the product boundary.

In Phase 1, the conversion step from signal to canonical work is:

`signal -> intake packet -> canonical TDE task -> execution -> closure evidence -> standardization decision/update`

The canonical rule is:
- Improvement owns the learning/prevention loop, intake expectations, and closure-evidence standard.
- TDE owns canonical task-state execution.
- A signal is not canonical improvement work until it has both a TDE task and a linked intake artifact satisfying the Improvement intake contract.

## Mandatory intake contract for canonical work
Every canonical improvement intake must include:
- `source_system`
- `source_reference`
- `product_scope`
- `evidence_links`
- `improvement_type`
- `expected_closure_evidence`

Reference contract: `products/improvement/04-execution/intake/CANONICAL_IMPROVEMENT_INTAKE_CONTRACT_V1.md`

## Closure discipline
Canonical improvement work does not close on discussion alone or on an unlinked implementation claim.

Closure requires:
1. linked closure evidence,
2. explicit source-to-closure trace, and
3. retention of product context so the improvement can later be reviewed, compared, and standardized.

## Active-product minimum interface maintenance
For active products with a canonical `TOP_PRIORITIES.md` surface, the minimum product-side improvement interface is now a current operating requirement rather than a rollout aspiration.

At the point of product review or product-surface change:
- reuse `products/improvement/04-execution/MINIMUM_IMPROVEMENT_INTERFACE_STANDARD_REFERENCE_SET_2026-03-22.md` as the default reference package,
- verify the product still exposes the five required interface elements named in `products/improvement/06-architecture/INTERFACES.md`, and
- correct any drift immediately rather than carrying it as an implicit future cleanup item.

This keeps the selected Control Tower priority (`OPS-2026-070`) alive as a maintained operating rule instead of a one-time deployment burst.

## Minimum measurement-and-follow-up responsibility
Improvement owns the minimum cross-system standard for lightweight measurement and follow-up on recurring operational loops, beginning with the overnight loop.

The management intent is deliberately narrow:
- know whether the loop ran according to plan,
- know whether it made a meaningful contribution,
- know whether the audit trail is clear enough to reconstruct what happened,
- detect stuckness, drift, and repeated low-value activity early,
- and trigger replan/escalate/record-no-action decisions when repetition by inertia appears.

Improvement should keep this layer lean and decision-oriented. It should not expand into broad reporting bureaucracy or attempt to own every product-local metric.

Current minimum references:
- `OVERNIGHT_LOOP_MINIMUM_PERFORMANCE_STANDARD_V1.md`
- `OVERNIGHT_LOOP_LEDGER_CONTRACT_V1.md`

## External AI-agent opportunity scouting
Improvement also owns a bounded external opportunity-sensing loop for AI agent systems in general and OpenClaw in particular.

The purpose is not broad trend collection. The purpose is to:
- scan for high-signal new use cases, operating patterns, tools, and deployment practices,
- identify ideas that could materially improve Lyra OS, PX Strategy, or downstream workspaces,
- maintain explicit dispositions so the same low-value ideas are not repeatedly re-evaluated,
- and route worthwhile opportunities into watch, reject, or TDE-linked test/adoption paths.

This opportunity-sensing loop should stay compact and executive-useful.
Each materially logged opportunity should answer, at minimum:
- what the idea/use case is,
- why it matters to us,
- where it appears most relevant,
- what evidence would justify testing or adoption,
- and its current disposition (`watch`, `reject`, `worth_testing`, `routed`, `adopted`, or equivalent).

The default cadence can include lightweight recurring review, including a compact executive briefing on the most relevant newly observed opportunities.
