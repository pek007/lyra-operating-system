#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from tde_intent_intake import detect_request_class, form_basic_gui_request
from tde_formation_creator import create_from_formation


def run_tests() -> None:
    assert detect_request_class('Create a basic GUI for TDE') == 'basic_tde_gui'
    assert detect_request_class('Investigate database performance') is None

    formation = form_basic_gui_request(
        request_text='Create a basic GUI for TDE',
        source_ref='telegram:test:gui',
    )
    assert formation['artifactType'] == 'tde_intent_formation_record'
    assert formation['proposed_workflow_family'] == 'implementation_verification_readiness'

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        formation_path = root / 'formation.json'
        formation_path.write_text(json.dumps(formation, indent=2), encoding='utf-8')
        result = create_from_formation(
            formation_path=formation_path,
            db_path=root / 'tde_state.sqlite',
            objectives_path=root / 'tde_objectives.json',
            tasks_projection_path=root / 'TASKS_from_db.md',
        )
        assert result['formation_id'] == formation['formation_id']
        assert len(result['created_tasks']) == 2

    print('[PASS] TDE intent intake tests passed')


if __name__ == '__main__':
    run_tests()
