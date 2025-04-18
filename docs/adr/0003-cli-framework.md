# ADR 003: CLI Framework

## Status
Accepted

## Date
2025-04-18

## Deciders
Jeff Wright

## Context
The application needs an ergonomic and extendable command-line interface to allow for interval training, audio generation, and logging without a GUI.

## Decision
Use [Typer](https://typer.tiangolo.com/) to build the CLI interface.

## Rationale
- Built on Click, but offers Pythonic syntax with rich type hints
- Clean integration with `__main__.py`
- Easy to extend with subcommands
- Generates help docs and usage messages automatically

## Consequences
- Rapid CLI prototyping with minimal boilerplate
- Tight coupling to Typer/Click ecosystem (manageable)
- Will need to migrate or refactor if GUI replaces CLI later
- Typer's auto-generated help and documentation features will save time and improve usability
- Typer's support for subcommands allows for easy expansion of CLI functionality
- Typer's type hinting and validation features will help catch errors early in the development process
- Typer's integration with Click allows for easy customization and extension of the CLI

## Workflow Reminder
- Periodically run `git fetch` to ensure your local repository stays in sync with the remote repository. This is especially useful if changes are made directly on the remote (e.g., via GitHub) or if you plan to collaborate in the future.
