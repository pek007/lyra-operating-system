# TOP_PRIORITIES

Product: Task Management
Last updated: 2026-03-14
Owner: Product Owner / Control Tower

## Priority 1
**Title:** Make TDE deployment/readiness status easier to assess and act on
**Why this matters now:** Task Management is structurally strong, but readiness is still easier to describe than to judge quickly from current evidence.
**Current status:** Active high-leverage priority with explicit scorecard and readiness artifacts already in place.
**Next concrete step:** Strengthen compact evidence and readiness judgment so current-state assessment becomes faster and less interpretive.
**Links:** `products/task-management/04-execution/PLAN.md`, `products/task-management/05-performance/READINESS_SCORECARD.md`, `products/task-management/05-performance/METRICS.md`

## Priority 2
**Title:** Improve the path for `pxs` to consume Task Management capability
**Why this matters now:** Downstream consumability is one of the clearest tests of whether the product is becoming operationally real rather than just well-modeled.
**Current status:** First formal consumption interface exists and the `pxs` workspace package has been bootstrapped, but evidence of low-friction real use is still limited.
**Next concrete step:** Produce clearer proof points and execution evidence that `pxs` can consume Task Management with minimal extra explanation.
**Links:** `products/task-management/04-execution/PLAN.md`, `products/task-management/06-architecture/PXS_CONSUMPTION_INTERFACE.md`, `products/task-management/05-performance/READINESS_SCORECARD.md`

## Priority 3
**Title:** Clarify and maintain the product boundary between Task Management, governance, and downstream workspaces
**Why this matters now:** TDE can only scale coherently if authority boundaries stay explicit and hidden coupling is reduced.
**Current status:** Boundary work is active and materially advanced, but still important as workspace-package and delivery-mode logic grows.
**Next concrete step:** Keep provider/consumer boundaries explicit in the product model and in downstream workspace operating packages.
**Links:** `products/task-management/04-execution/PLAN.md`, `products/task-management/03-operating-model/GOVERNANCE.md`, `products/task-management/07-decisions/DELIVERY_MODE_DECISION_PXS_V1.md`
