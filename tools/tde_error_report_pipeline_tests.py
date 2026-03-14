#!/usr/bin/env python3
from __future__ import annotations

import tempfile
from pathlib import Path

from tde_error_report_adapter_tests import _sample_report
from tde_error_report_pipeline import run_pipeline


def run_tests() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        report_path = root / "ERR-TEST.json"
        packet_path = root / "INTAKE.json"
        db_path = root / "tde.sqlite"
        result = run_pipeline(
            report=_sample_report(),
            report_out=report_path,
            packet_out=packet_path,
            workspace_scope="lyra-os-root",
            db_path=db_path,
        )
        assert report_path.exists()
        assert packet_path.exists()
        assert result["ingest"]["status"] == "ingested"
        assert result["intake_class"] == "work"
    print("[PASS] TDE error report pipeline tests passed")


if __name__ == "__main__":
    run_tests()
