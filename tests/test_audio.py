# tests/test_audio.py

import pytest
from unittest import mock
from audio import note_to_freq, play_note

def test_note_to_freq_valid():
    assert note_to_freq("A4") == pytest.approx(440.0, abs=0.01)
    assert note_to_freq("C4") == pytest.approx(261.63, abs=0.05)

def test_note_to_freq_invalid():
    with pytest.raises(ValueError):
        note_to_freq("Z9")

@mock.patch("audio.play_tone")
def test_play_note_calls_play_tone(mock_play):
    play_note("G3", duration=1.2)
    mock_play.assert_called_once()
    freq_arg = mock_play.call_args[0][0]
    assert round(freq_arg, 1) == 196.0  # G3 ≈ 196.00 Hz