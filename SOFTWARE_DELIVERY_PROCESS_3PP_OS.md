# SOFTWARE_DELIVERY_PROCESS_3PP_OS.md

Status: Active
Owner: Peter + Lyra

## Purpose
OS-level software delivery process for any project (not project-specific).

## Process modes (important)
We use two delivery modes:

1. **3PP mode (current focus)**
   - Uses external supplier lanes (e.g., Claude Code, Deep Research).
   - Best for larger, higher-risk, architecture-heavy work.
   - Strong packet/traceability/governance requirements.

2. **Internal fast mode (Lyra-only)**
   - Fully internal execution for smaller/low-risk tasks.
   - No mandatory external supplier or research handoff.
   - Optimized for speed and low overhead.

Long-run expectation: internal fast mode becomes the default for most work, while 3PP mode is used selectively for larger or higher-risk initiatives.

## Outcome-first principle
Outcome quality is primary.
Process is support to increase quality, safety, and execution reliability.

If process and intended outcome diverge:
1) pause,
2) clarify desired outcome,
3) adjust process usage to fit outcome.

## Standard 3PP flow (all projects)
1. Define outcome and non-goals
2. Build implementation packet (PRD/use-cases/data/contracts/tests/work order)
3. Challenge packet (research/architecture review)
4. Freeze packet v1.0
5. Execute with supplier (Claude Code or equivalent)
6. Verify against acceptance matrix
7. Closeout + release + backlog update
8. Log misses and preventive controls

## Mandatory artifacts (generic)
- PRD
- Use cases
- Data architecture
- System context/flows
- Contracts
- Acceptance test matrix
- Work order
- Miss log entry (if applicable)

## Governance
- Keep implementation prompts outcome/constraint driven (avoid unnecessary micromanagement).
- Require requirement-to-evidence traceability for non-trivial deliveries.

## Mode selection rule
Choose **internal fast mode** by default when:
- scope is small and well-understood,
- risk is low,
- no major architecture/security decisions are involved.

Choose **3PP mode** when:
- scope is large or cross-cutting,
- architecture and contracts need external challenge,
- auditability/traceability needs are high,
- specialized implementation throughput is beneficial.
