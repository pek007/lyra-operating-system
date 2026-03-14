#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from tde_error_report_adapter import adapt_error_report
from tde_intake_ingest import ingest_packet


def run_pipeline(*, report: dict[str, Any], report_out: Path | None, packet_out: Path | None, workspace_scope: str, db_path: Path | None) -> dict[str, Any]:
    if report_out is not None:
        report_out.parent.mkdir(parents=True, exist_ok=True)
        report_out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    packet = adapt_error_report(report=report, workspace_scope=workspace_scope)
    if packet_out is not None:
        packet_out.parent.mkdir(parents=True, exist_ok=True)
        packet_out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")

    result = {
        "report_path": str(report_out) if report_out else None,
        "packet_path": str(packet_out) if packet_out else None,
        "intake_id": packet["intake_id"],
        "intake_class": packet["intake_class"],
    }
    if db_path is not None:
        result["ingest"] = ingest_packet(packet=packet, db_path=db_path)
    return result


def main() -> None:
    ap = argparse.ArgumentParser(description="Run structured error-report -> TDE intake -> ingest pipeline")
    ap.add_argument("--report-path", required=True)
    ap.add_argument("--workspace-scope", required=True)
    ap.add_argument("--packet-out", default=None)
    ap.add_argument("--db-path", default=None)
    args = ap.parse_args()

    report = json.loads(Path(args.report_path).read_text(encoding="utf-8"))
    result = run_pipeline(
        report=report,
        report_out=Path(args.report_path),
        packet_out=Path(args.packet_out) if args.packet_out else None,
        workspace_scope=args.workspace_scope,
        db_path=Path(args.db_path) if args.db_path else None,
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
