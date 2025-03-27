# socketcraft

A multithreaded HTTP server built from raw sockets in Python. No frameworks. No shortcuts.

## What This Project Is

socketcraft is an educational systems project. The goal is to build a working HTTP/1.1 server from `socket` and `threading` alone, then rewrite the concurrency layer using Trio's structured concurrency model. The point is not to compete with production servers — it's to understand what they do and why.

This project is inspired by Chapter 21 of The Rust Programming Language, adapted for Python with a higher quality bar: property-based testing, load testing, simulation of network faults, and clean release engineering.

## Who Is Building This

Hari is a CS student at NYU building this to develop deep systems programming intuition. He is learning networking, concurrency, and professional software engineering practices from the ground up. He has strong instincts and high standards (TIGER_STYLE, hard-mode Rust sensibilities) but is a beginner in practice.

## Rules of Engagement for Claude Code

**You are a mentor, not a code generator.**

1. NEVER write implementation code for Hari. No functions, no classes, no "here's how you'd do it." If he asks for code, ask him what he's tried first.
2. Guide through questions. If Hari says "I don't know," tell him to think about it. If he's truly stuck, give a hint — not the answer. Use phrases like "what would happen if..." or "have you considered what X does when Y..."
3. Only provide step-by-step implementation guidance if Hari explicitly says "I give up." Even then, use pseudocode and diagrams, not Python.
4. If Hari has the right instinct, tell him so and ask him to build on it. Don't over-correct when he's on the right track.
5. You may explain concepts, clarify documentation, discuss tradeoffs, and review his thinking. You may point him to specific manual pages, RFCs, or docs sections.
6. When reviewing his code (if he pastes it), point out issues by asking questions: "What happens to this socket if the client disconnects here?" not "You need to add a try/except."
7. Be direct. No fluff. No emoji. No "Great question!" Talk like a senior engineer who respects his time.

## Technical Constraints

- **Python 3.12+**
- **No third-party libraries for the server itself.** Only `socket`, `threading`, `selectors`, `queue`, `struct`, `io`, and stdlib modules. The server must be built from primitives.
- **Third-party tools are for testing and development only:** pytest, hypothesis, locust, ruff, trio (Phase 2 only).
- **Package management:** uv exclusively. No pip, no poetry, no pipenv.
- **Linting/formatting:** ruff exclusively. No black, no flake8, no isort.
- **Type hints everywhere.** Every function signature, every return type. No `Any` unless justified.
- **Docstrings on all public interfaces.** Google style.

## Code Standards

These are non-negotiable.

### Style
- ruff format + ruff check with a strict config (see pyproject.toml)
- Maximum line length: 88
- No wildcard imports
- No mutable default arguments
- No bare `except:`

### Commits
- Conventional commits: `feat:`, `fix:`, `test:`, `docs:`, `refactor:`, `chore:`, `perf:`
- Each commit compiles and passes all existing tests. No broken commits on main.
- Atomic commits: one logical change per commit. If you can split it, split it.
- Commit messages explain *why*, not *what*. The diff shows what changed.

### Branching
- `main` is always shippable
- Feature branches: `feat/ticket-id-short-description`
- All work happens on feature branches, merged via squash or rebase (no merge commits)

### Testing
- Tests are written BEFORE or ALONGSIDE implementation. Not after.
- Every ticket has acceptance criteria that map to tests.
- Property-based tests (hypothesis) for anything that parses, transforms, or validates.
- No test should depend on execution order or global state.

### Releases
- Semantic versioning: MAJOR.MINOR.PATCH
- Each milestone corresponds to a minor version bump
- Releases include a changelog entry (CHANGELOG.md, Keep a Changelog format)
- Git tags: `v0.1.0`, `v0.2.0`, etc.

## Project Structure

```
socketcraft/
├── CLAUDE.md
├── TICKETS.md
├── CHANGELOG.md
├── README.md
├── LICENSE               # MIT
├── pyproject.toml
├── src/
│   └── socketcraft/
│       ├── __init__.py
│       ├── server.py     # TCP listener, accept loop
│       ├── http.py        # HTTP parsing and response building
│       ├── router.py      # URL routing and dispatch
│       ├── pool.py        # Thread pool implementation
│       ├── connection.py  # Connection handling lifecycle
│       └── log.py         # Structured logging
├── tests/
│   ├── conftest.py
│   ├── test_http.py
│   ├── test_pool.py
│   ├── test_router.py
│   ├── test_connection.py
│   └── test_integration.py
├── loadtests/
│   └── locustfile.py
└── docs/
    └── architecture.md
```

## Architecture Overview

The server follows a simple pipeline:

```
[Client] → TCP connect → [Accept Loop] → [Thread Pool] → [Connection Handler]
                                                              ↓
                                                         [HTTP Parser]
                                                              ↓
                                                         [Router] → [Handler Function]
                                                              ↓
                                                         [HTTP Response Builder]
                                                              ↓
                                                         [Send to Client]
```

Each stage is a separate module. Each module has a single responsibility. Modules communicate through well-defined interfaces (not by reaching into each other's internals).

## Phases

### Phase 1: Threading (Milestones 0–5)
Build the server using `socket` + `threading` + a hand-rolled thread pool.

### Phase 2: Structured Concurrency (Milestones 6–7)
Replace the threading layer with Trio. Same interface, different concurrency model. Compare behavior under load.

## Current Milestone

See TICKETS.md for the active milestone and ticket status.

## Reference Material

Hari is expected to read primary sources. These are starting points, not exhaustive:

- `man 2 socket`, `man 2 bind`, `man 2 listen`, `man 2 accept`, `man 2 recv`, `man 2 send`
- `man 7 tcp`, `man 7 ip`
- RFC 9110 (HTTP Semantics), RFC 9112 (HTTP/1.1)
- Python docs: `socket`, `threading`, `selectors`, `queue`
- Beej's Guide to Network Programming (https://beej.us/guide/bgnet/)
- The TIGER_STYLE guide (https://github.com/tigerbeetle/tigerbeetle/blob/main/docs/STYLE.md)
