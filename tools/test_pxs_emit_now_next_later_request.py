#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from pxs_emit_now_next_later_request import build_request, write_request
from pxs_tm_contract_processor import write_processed_response

ROOT = Path(__file__).resolve().parents[1]


def run_tests() -> None:
    request = build_request(title="Build first vertical slice")
    assert request["artifactType"] == "pxs_tm_request_envelope"
    assert request["payload_inline"]["title"] == "Build first vertical slice"

    with tempfile.TemporaryDirectory() as td:
        request_dir = Path(td) / "requests"
        response_dir = Path(td) / "responses"
        request_path = write_request(request, output_dir=request_dir)
        assert request_path.exists()

        response_path = write_processed_response(
            request_path=request_path,
            search_root=response_dir,
            output_dir=response_dir,
        )
        assert response_path.exists()
        response = json.loads(response_path.read_text(encoding="utf-8"))
        assert response["artifactType"] == "pxs_tm_response_envelope"
        assert response["status"] == "accepted"
        assert response["request_id"] == request["request_id"]

    print("[PASS] PXS now-next-later producer tests passed")


if __name__ == "__main__":
    run_tests()
