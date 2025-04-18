# src/cli.py
import argparse
from audio import play_note

def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Music Tutor CLI: Train your musical ear and recognize guitar notes."
    )
    parser.add_argument(
        "--note", type=str, help="Play this note (e.g. E2, A3, C#4)"
    )
    parser.add_argument(
        "--duration", type=float, default=1.0, help="Duration of the tone in seconds (default: 1.0)"
    )
    parser.add_argument(
        "--version", action="version", version="music-tutor 0.1"
    )
    return parser.parse_args(argv)

def main(argv=None):
    args = parse_args(argv)

    if args.note:
        try:
            play_note(args.note, args.duration)
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("No command provided. Try --note A4 or --help.")
