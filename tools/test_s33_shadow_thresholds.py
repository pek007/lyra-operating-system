#!/usr/bin/env python3
from __future__ import annotations

import tempfile
from pathlib import Path

from tde_job_tick_runner import _shadow_state_evaluate_threshold


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        alert = Path(tmp) / "alerts.jsonl"

        r1 = _shadow_state_evaluate_threshold("mismatch", alert, 2)
        assert r1["threshold_exceeded"] is False
        assert r1["consecutive_failures"] == 1

        r2 = _shadow_state_evaluate_threshold("mismatch", alert, 2)
        assert r2["threshold_exceeded"] is True
        assert r2["consecutive_failures"] == 2

        r3 = _shadow_state_evaluate_threshold("ok", alert, 2)
        assert r3["threshold_exceeded"] is False
        assert r3["consecutive_failures"] == 0

    print("[PASS] S33 shadow threshold checks passed")


if __name__ == "__main__":
    main()
