#!/usr/bin/env python3
from __future__ import annotations

import unittest

from tde_chaining import evaluate_ready_promotions


class TDEReadyPromotionEdgesTest(unittest.TestCase):
    def test_missing_predecessor_skips(self) -> None:
        tasks = [
            {"task_id": "B", "status": "Triage", "metadata": {"depends_on": ["A"], "activation_rule": "all_predecessors_done", "chain_policy": {"pilot_enabled": True}}}
        ]
        result = evaluate_ready_promotions(tasks, tick_id="t1", current_time="2026-03-09T00:00:00+00:00")
        self.assertEqual(result["promoted"], [])
        self.assertEqual(result["skipped"][0]["reason"], "missing_predecessor")

    def test_partial_predecessor_completion_skips(self) -> None:
        tasks = [
            {"task_id": "A", "status": "Waiting", "metadata": {}},
            {"task_id": "B", "status": "Triage", "metadata": {"depends_on": ["A"], "activation_rule": "all_predecessors_done", "chain_policy": {"pilot_enabled": True}}},
        ]
        result = evaluate_ready_promotions(tasks, tick_id="t2", current_time="2026-03-09T00:00:00+00:00")
        self.assertEqual(result["promoted"], [])
        self.assertEqual(result["skipped"][0]["reason"], "predecessors_not_done")

    def test_broader_rollout_promotes_without_pilot_enabled(self) -> None:
        # Broader rollout authorized 2026-03-17 by Peter: pilot_enabled gate removed.
        # Tasks with chain_policy (e.g. {family: pilot-a}) but no pilot_enabled=True
        # should now be promoted when predecessors are done.
        tasks = [
            {"task_id": "A", "status": "Done", "metadata": {}},
            {"task_id": "B", "status": "Triage", "metadata": {"depends_on": ["A"], "activation_rule": "all_predecessors_done", "chain_policy": {"family": "pilot-a"}}},
        ]
        result = evaluate_ready_promotions(tasks, tick_id="t3", current_time="2026-03-09T00:00:00+00:00")
        self.assertEqual(len(result["promoted"]), 1)
        self.assertEqual(result["promoted"][0]["task_id"], "B")

    def test_multiple_successors_promote_but_tick_can_bound_claims(self) -> None:
        tasks = [
            {"task_id": "A", "status": "Done", "metadata": {}},
            {"task_id": "B", "status": "Triage", "metadata": {"depends_on": ["A"], "activation_rule": "all_predecessors_done", "chain_policy": {"pilot_enabled": True}}},
            {"task_id": "C", "status": "Waiting", "metadata": {"depends_on": ["A"], "activation_rule": "all_predecessors_done", "chain_policy": {"pilot_enabled": True}}},
        ]
        result = evaluate_ready_promotions(tasks, tick_id="t4", current_time="2026-03-09T00:00:00+00:00")
        self.assertEqual(len(result["promoted"]), 2)


if __name__ == "__main__":
    unittest.main()
