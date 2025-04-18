# tests/test_audio.py

import pytest
from src.audio import note_to_freq, play_interval, NOTE_FREQUENCIES
from unittest.mock import patch

def test_note_to_freq_middle_c():
    assert note_to_freq("C4") == pytest.approx(261.63, rel=1e-3)

def test_note_to_freq_a4():
    assert round(note_to_freq("A4"), 2) == 440.00

def test_note_to_freq_invalid_note():
    with pytest.raises(ValueError):
        note_to_freq("H2")

def test_note_to_freq_enharmonic():
    # C#3 and Db3 should be the same frequency
    c_sharp = note_to_freq("C#3")
    d_flat = note_to_freq("Db3")
    assert round(c_sharp, 2) == round(d_flat, 2)

@patch("src.audio.play_note")
@patch("src.audio.sd.sleep")
def test_play_interval(mock_sleep, mock_play_note):
    # Test that play_interval calls play_note and sd.sleep correctly
    play_interval("C4", "E4", duration=1.0, gap=0.5)
    mock_play_note.assert_any_call(note_name="C4", duration=1.0)
    mock_play_note.assert_any_call(note_name="E4", duration=1.0)
    mock_sleep.assert_called_once_with(500)  # Gap of 0.5 seconds

def note_to_freq(note_name: str) -> float:
    """Convert a note name like A4 or C#3 to frequency in Hz."""
    enharmonic_map = {
        "Db": "C#",
        "Eb": "D#",
        "Gb": "F#",
        "Ab": "G#",
        "Bb": "A#"
    }

    name = note_name[:-1]
    octave = int(note_name[-1])

    # Normalize flat notes to sharps
    name = enharmonic_map.get(name, name)

    base_freq = NOTE_FREQUENCIES.get(name.upper())
    if base_freq is None:
        raise ValueError(f"Unknown note name: {note_name}")

    return base_freq * (2 ** (octave - 4))
