#!/usr/bin/env python3
from __future__ import annotations

import tempfile
from pathlib import Path

from tde_request_entry import run_request_entry


def run_tests() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        proceed = run_request_entry(
            request_text="Create a basic GUI for TDE",
            source_ref="telegram:test:request-entry-gui",
            formation_out=root / "gui-formation.json",
            db_path=root / "tde_state.sqlite",
            objectives_path=root / "tde_objectives.json",
            tasks_projection_path=root / "TASKS_from_db.md",
        )
        assert proceed["request_class"] == "basic_tde_gui"
        assert proceed["recommended_next_action"] == "proceed_with_assumptions"
        assert "canonical_creation" in proceed

        ask = run_request_entry(
            request_text="Build an internal tool",
            source_ref="telegram:test:request-entry-tool",
            formation_out=root / "tool-formation.json",
            db_path=root / "tde_state_2.sqlite",
            objectives_path=root / "tde_objectives_2.json",
            tasks_projection_path=root / "TASKS_from_db_2.md",
        )
        assert ask["request_class"] == "internal_tool"
        assert ask["recommended_next_action"] == "ask_clarifying_questions"
        assert ask["required_clarifications"]
        assert "canonical_creation" not in ask

    print("[PASS] TDE request entry tests passed")


if __name__ == "__main__":
    run_tests()
