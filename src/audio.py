import numpy as np
import sounddevice as sd

NOTE_FREQUENCIES = {
    'C': 261.63, 'C#': 277.18,
    'D': 293.66, 'D#': 311.13,
    'E': 329.63,
    'F': 349.23, 'F#': 369.99,
    'G': 392.00, 'G#': 415.30,
    'A': 440.00, 'A#': 466.16,
    'B': 493.88
}

def note_to_freq(note_name: str) -> float:
    """Convert a note name like A4 or C#3 to frequency in Hz."""
    enharmonic_map = {
        "Db": "C#",
        "Eb": "D#",
        "Gb": "F#",
        "Ab": "G#",
        "Bb": "A#"
    }

    name = note_name[:-1]  # Extract the note name (e.g., "C" from "C4")
    octave = int(note_name[-1])  # Extract the octave (e.g., 4 from "C4")

    # Normalize flat notes to sharps
    name = enharmonic_map.get(name, name)

    base_freq = NOTE_FREQUENCIES.get(name.upper())  # Get the base frequency
    if base_freq is None:
        raise ValueError(f"Unknown note name: {note_name}")

    # Adjust the frequency for the given octave
    return base_freq * (2 ** (octave - 4))

def play_tone(freq: float, duration: float = 1.0, sample_rate: int = 44100):
    """Play a sine wave of a given frequency and duration."""
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = 0.3 * np.sin(2 * np.pi * freq * t)
    tone = np.clip(tone, -1.0, 1.0)  # Guard against overdrive
    sd.play(tone, samplerate=sample_rate)
    sd.wait()

def play_note(note_name: str, duration: float = 1.0):
    """Convenience function to convert and play a named note."""
    freq = note_to_freq(note_name)
    play_tone(freq, duration)

def play_interval(note1: str, note2: str, duration: float = 1.0, gap: float = 0.3):
    """Play two notes in sequence with a gap."""
    play_note(note_name=note1, duration=duration)  # Play the first note
    sd.sleep(int(gap * 1000))  # Wait for the gap
    play_note(note_name=note2, duration=duration)  # Play the second note

# tests/test_audio.py

import pytest
from src.audio import note_to_freq, NOTE_FREQUENCIES, play_tone

def test_note_to_freq_middle_c():
    assert round(note_to_freq("C4"), 2) == 261.63

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

def test_play_tone():
    play_tone(440.0, duration=1.0)  # Play an A4 tone
    sd.sleep(1000)  # Ensure the tone has time to play

def test_play_tone_interactive():
    """Play a test tone interactively."""
    print("Playing a 440 Hz tone (A4) for 1 second...")
    play_tone(440.0, duration=1.0)  # Play an A4 tone
    print("Tone finished.")
