# ADR 001: Testing Framework Selection

## Status
Accepted

## Date
2025-04-18

## Deciders
Jeff Wright

## Context
The project requires a reliable testing framework to validate audio tone generation and CLI logic. The framework must support isolated test execution, be compatible with VS Code and CI tools, and provide extensible options for future backend/API testing.

## Decision
Adopt `pytest` as the project's primary testing framework.

## Rationale
- Concise and readable syntax with minimal boilerplate
- Rich fixture support for mocking audio and CLI components
