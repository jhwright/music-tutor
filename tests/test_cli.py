# tests/test_cli.py

import pytest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cli import parse_args

def test_parse_note_flag():
    args = parse_args(["--note", "A3"])
    assert args.note == "A3"
    assert args.duration == 1.0

def test_parse_note_and_duration():
    args = parse_args(["--note", "E4", "--duration", "2.5"])
    assert args.note == "E4"
    assert args.duration == 2.5

def test_version_flag(capsys):
    with pytest.raises(SystemExit):
        parse_args(["--version"])
    captured = capsys.readouterr()
    assert "music-tutor 0.1" in captured.out
