# src/audio.py

import numpy as np
import sounddevice as sd

NOTE_FREQUENCIES = {
    'C': 16.35, 'C#': 17.32, 'Db': 17.32,
    'D': 18.35, 'D#': 19.45, 'Eb': 19.45,
    'E': 20.60,
    'F': 21.83, 'F#': 23.12, 'Gb': 23.12,
    'G': 24.50, 'G#': 25.96, 'Ab': 25.96,
    'A': 27.50, 'A#': 29.14, 'Bb': 29.14,
    'B': 30.87
}

def note_to_freq(note_name: str) -> float:
    """Convert a note name like A4 or C#3 to frequency in Hz."""
    name = note_name[:-1]
    octave = int(note_name[-1])

    base_freq = NOTE_FREQUENCIES.get(name.upper())
    if base_freq is None:
        raise ValueError(f"Unknown note name: {note_name}")

    return base_freq * (2 ** octave)

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