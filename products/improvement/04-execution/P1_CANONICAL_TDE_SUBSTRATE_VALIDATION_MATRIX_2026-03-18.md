# P1 Canonical TDE Substrate — Validation Matrix

Date: 2026-03-18
Prepared by: Overnight execution loop
Selected priority source: `control/CT-OVERNIGHT-SYNTHESIS-2026-03-17.md` (priority 3)
Related prep note: `products/improvement/04-execution/P1_CANONICAL_TDE_SUBSTRATE_SESSION_PREP_2026-03-18.md`

## Purpose
Create the smallest useful validation surface for the next focused P1 session without attempting to design the full substrate overnight.

This matrix makes the bridge explicit between:
1. the Control Tower selected priority,
2. the current canonical TDE work already present in `os/runtime/TASKS_from_db.md`, and
3. the specific substrate-definition questions those live cases must answer.

## Canonical TDE frontier preflight
- **Canonical TDE store:** `os/runtime/tde_state.sqlite`
- **Human-readable projection:** `os/runtime/TASKS_from_db.md`
- **Authority index:** `os/tde/INDEX.md`
- **Operating alignment note:** `governance/TDE_OPERATING_ALIGNMENT_NOTE__MEMORY_HANDOFFS_AND_FRONTIER_PREFLIGHT_V1.md`
- **Continuous-improvement operating instruction:** `governance/LYRA_CONTINUOUS_IMPROVEMENT_OPERATING_INSTRUCTION_V1.md`

This confirms the current P1 follow-through should stay grounded in DB-canonical TDE state rather than chat/memory alone.

## Selected priority → live validation set
| TDE item | Current board state | Source artifact | Product scope | Why it is a useful P1 test case |
|---|---|---|---|---|
| `OPS-2026-066` | Inbox | `products/improvement/04-execution/intake/intake-ops-2026-066-final.json` | improvement | Tests release-triggered operational improvement intake, cross-linking to a recurring job and release delta evidence. |
| `OPS-2026-067` | Inbox | `products/improvement/04-execution/intake/intake-ops-2026-067-final.json` | security | Tests whether improvement substrate can carry policy/SLA work that spans job definition + stale task disposition. |
| `OPS-2026-068` | Inbox | `products/improvement/04-execution/intake/intake-ops-2026-068-final.json` | governance | Tests job-bundle retirement + handoff standardization work, which is durable and artifact-heavy. |
| `OPS-2026-069` | Inbox | `products/improvement/04-execution/intake/intake-ops-2026-069-final.json` | security | Tests explicit disposition work where closure depends on decision/evidence integrity, not just implementation. |

## What each live case pressures the substrate to define
| Substrate question | `OPS-2026-066` | `OPS-2026-067` | `OPS-2026-068` | `OPS-2026-069` |
|---|---|---|---|---|
| **Routing rule** — when does a signal become canonical improvement work? | Release delta creates a concrete job-validation item. | Repeated stale findings create operating-improvement work. | Completed proof cases and handoff drift create governance-improvement work. | Aged unresolved findings create disposition-improvement work. |
| **Minimum metadata** — what fields are mandatory? | Needs source release + affected job + expected smoke path. | Needs SLA target + affected job + retroactive scope. | Needs bundle list + archive target + governance artifact target. | Needs linked stale findings + disposition path + evidence expectation. |
| **Linkage rule** — what source/evidence links are non-optional? | Release evidence + memory signal + job ref. | Review source + job ref + stale finding refs. | Review source + job bundle refs + resulting governance doc. | Security task refs + resulting decision/risk-acceptance artifacts. |
| **Closure evidence** — what proves done? | Updated cron/job config + smoke result + checklist update. | Updated JOB-SEC-001 rule + retroactive stale dispositions. | Archived bundles + handoff protocol artifact + done-jobs index. | Formal disposition records and/or approved fallback documentation. |
| **Decision path** — when is a decision record required? | Only if delivery model options conflict. | Required if SLA threshold or enforcement posture is contested. | Required if archive model or canonical handoff owner is disputed. | Required if risk acceptance vs remediation remains unresolved. |

## Emerging minimum P1 rule set implied by the validation set
The next focused session should be able to decide or reject the following candidate minimum rules:

1. **Every improvement item must name a triggering source artifact and at least one owning operational entity** (job, task, product, release, or decision).
2. **Every improvement item must declare its expected closure evidence type up front** rather than leaving closure semantics implicit.
3. **Improvement items that primarily resolve stale or blocked judgment must name the required disposition path** (decision, risk acceptance, fallback approval, or implementation proof).
4. **Cross-product improvement items may remain in canonical TDE even when the product scope differs from the improvement home** as long as product scope and owner links are explicit.

These are candidate rules for the focused P1 session, not yet approved substrate policy.

## Immediate overnight outcome
One additional concrete step is now complete:
- the previously named validation set (`OPS-2026-066` through `OPS-2026-069`) is no longer just listed;
- it is now mapped to the exact substrate-definition questions the next session must resolve.

This keeps the chain explicit:
`CT selected priority` -> `canonical TDE live cases` -> `P1 design questions` -> `next-session decision surface`.
