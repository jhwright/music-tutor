# ADR 002: Project Structure

## Status
Accepted

## Date
2025-04-18

## Deciders
Jeff Wright

## Context
The project requires a modular, testable layout to support growth toward a full iOS app. It must support CLI use for tone generation and interval training as a prototype.

## Decision
Organize the project as follows:
music-tutor/
├── src/                # Core Python code
├── tests/              # Pytest unit tests
├── .vscode/            # Editor settings
├── docs/adr/           # Architectural Decision Records
├── .gitignore
├── README.md
└── requirements.txt

## Consequences
- Code is discoverable and clearly divided by responsibility
- Testing is fully isolated
- ADRs can be tracked and evolved via version control
