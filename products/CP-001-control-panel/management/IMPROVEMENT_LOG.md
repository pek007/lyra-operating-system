# Control Panel — Improvement Log

## Entry CP-L1
- Trigger: Portfolio-level need for a common product management framework.
- Observation: Product governance artifacts exist, but structure for vision/goal/plan/improvement is not standardized across products.
- Hypothesis: A single required artifact model will increase clarity, comparability, and execution quality.
- Change made: Published `PRODUCT_WAY_OF_WORKING_PROCESS_V1.md` + template + instantiated Control Panel baseline artifacts.
- Result: Initial framework established and ready for portfolio rollout.
- Decision (adopt/revert/continue-test): Adopt (v1 baseline).
- Follow-up: Apply to additional products and capture refinement deltas.

## Entry CP-L2
- Trigger: Product-model clarification and the need for a system-wide memory architecture rather than ad hoc memory behavior.
- Observation: Memory responsibilities were spread across sessions, jobs, knowledge assets, and operating artifacts, but without one formal process owner, scope model, or activation standard.
- Hypothesis: Making Memory an explicit Control Panel capability will improve continuity, portability, retrieval quality, and system learning.
- Change made: Published `MEMORY_PROCESS_V1.md`; updated `SITUATIONAL_AWARENESS.md`; aligned Control Panel goals/plan/decisions with memory capability ownership.
- Result: Initial memory governance baseline established.
- Decision (adopt/revert/continue-test): Adopt (v1 baseline).
- Follow-up: validate live retrieval behavior, define coordination-memory substrate, and clean up remaining live `Control Tower` terminology.
- Additional implementation artifacts: `MEMORY_IMPLEMENTATION_ROADMAP_V1.md`, `MEMORY_ACTIVATION_MAP_V1.md`.

## Entry CP-L3
- Trigger: Repeated evidence that Telegram topic/session separation is too weak as the primary product-runtime architecture, plus review of stronger boundary patterns in Vega / `pxs`.
- Observation: Current product handling in Lyra depends too much on conversational context for role identity, wake-up semantics, and coordination. Vega demonstrates the value of explicit runtime boundaries, shared-core discipline, and structured handoffs where boundaries genuinely matter.
- Hypothesis: A hybrid runtime topology will outperform both the current session-only model and a premature one-agent-per-product model.
- Change made: Published runtime topology decision memo (`DEC-2026-015`) and `RUNTIME_TOPOLOGY_MAP_V1.md`; updated Control Panel plan/tasks to make topology design an active workstream.
- Result: First explicit topology baseline established.
- Decision (adopt/revert/continue-test): Adopt (v1 topology baseline).
- Follow-up: map current sessions/products to the topology, define the lightweight intra-Lyra handoff protocol, and test at least one real job/product flow under the new coordination model.
- Additional implementation artifact: `RUNTIME_ASSIGNMENT_MAP_V1.md`.