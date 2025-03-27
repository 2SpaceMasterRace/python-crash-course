# socketcraft — Ticket Backlog

Status key: `[ ]` = not started, `[~]` = in progress, `[x]` = done

---

## Milestone 0: Project Bootstrap — `v0.0.1`

> **Goal:** A working development environment with all tooling configured. No server code yet. You should be able to run `uv run pytest`, `uv run ruff check .`, and see everything pass (even if there are zero tests). This milestone is about the foundation. Do not skip it. Do not half-ass it. Every decision here compounds.

### Ticket 0.1: Initialize the repository

- [ ] Create a new git repository
- [ ] Write an initial README.md with a one-paragraph project description
- [ ] Add an MIT LICENSE file
- [ ] Create a `.gitignore` appropriate for Python (research what belongs here — don't just copy one blindly. Understand every line.)
- [ ] Make your first commit. It should be: `chore: initialize repository`

**Acceptance criteria:**
- `git log` shows exactly one commit with a conventional commit message
- No junk files tracked (no `__pycache__`, no `.venv`, no `.ruff_cache`)

### Ticket 0.2: Set up uv and project structure

- [ ] Initialize the project with uv. Read the uv docs to understand what `uv init` does vs setting up `pyproject.toml` manually. Make a deliberate choice.
- [ ] Configure `pyproject.toml` with project metadata (name, version `0.0.1`, python version requirement, description, author)
- [ ] Create the `src/socketcraft/` package layout with an `__init__.py`
- [ ] Create the `tests/` directory with an empty `conftest.py`
- [ ] Verify you can run `uv run python -c "import socketcraft"` successfully

**Acceptance criteria:**
- `uv run python -c "import socketcraft"` exits 0
- `pyproject.toml` has correct metadata and uses the `[project]` table (PEP 621)
- The src layout is used (not flat layout). Research why src layout matters.

**Reading:**
- uv docs: project management, `pyproject.toml` configuration
- Python packaging: src layout vs flat layout debate

### Ticket 0.3: Configure ruff

- [ ] Add ruff as a dev dependency
- [ ] Configure ruff in `pyproject.toml` under `[tool.ruff]`
- [ ] Enable at minimum these rule sets: `E` (pycodestyle errors), `F` (pyflakes), `I` (isort), `N` (pep8-naming), `UP` (pyupgrade), `B` (bugbear), `SIM` (simplify), `ANN` (annotations)
- [ ] Set target Python version to 3.12
- [ ] Set line length to 88
- [ ] Run `uv run ruff check .` and `uv run ruff format --check .` — both should pass

**Acceptance criteria:**
- ruff config exists in `pyproject.toml` with all specified rule sets
- Running ruff on the project produces zero warnings
- You can explain what each rule set does and why it's included

**Reading:**
- ruff docs: rule selection, configuration
- Read through the rules for each set you're enabling. Know what you're enforcing.

### Ticket 0.4: Configure pytest

- [ ] Add pytest as a dev dependency
- [ ] Add hypothesis as a dev dependency
- [ ] Configure pytest in `pyproject.toml` under `[tool.pytest.ini_options]`
- [ ] Set `testpaths`, `pythonpath`, and configure strict mode and strict markers
- [ ] Write a single dummy test in `tests/test_smoke.py` that asserts `True`. This proves the pipeline works.
- [ ] Run `uv run pytest` and see it pass

**Acceptance criteria:**
- `uv run pytest` discovers and passes 1 test
- pytest config includes strict mode (unknown markers are errors)
- hypothesis is importable: `uv run python -c "import hypothesis"`

**Reading:**
- pytest docs: configuration, discovery, conftest.py purpose
- hypothesis docs: quick start (just read it, you'll use it soon)

### Ticket 0.5: Set up pre-commit hooks (optional but recommended)

- [ ] Research pre-commit framework or git hooks
- [ ] Set up a hook that runs `ruff check` and `ruff format --check` before each commit
- [ ] Verify that a commit with a linting violation is rejected

**Acceptance criteria:**
- Making a commit with a ruff violation fails with a clear error
- Making a clean commit succeeds

### Ticket 0.6: Create the initial CHANGELOG and tag v0.0.1

- [ ] Create `CHANGELOG.md` following Keep a Changelog format (https://keepachangelog.com)
- [ ] Add an entry for v0.0.1 under `[0.0.1] - YYYY-MM-DD` with what was set up
- [ ] Tag the commit: `git tag v0.0.1`

**Acceptance criteria:**
- CHANGELOG.md exists and follows the format
- `git tag` shows `v0.0.1`
- The tag points to a commit where all tooling works

---

## Milestone 1: A Single-Threaded Echo Server — `v0.1.0`

> **Goal:** A TCP server that listens on a port, accepts one connection at a time, reads bytes from the client, and echoes them back. No HTTP yet. No threads. This is where you learn what a socket actually is, what the kernel does for you, and what happens at the byte level. You should be able to `telnet localhost <port>` and see your typed text come back.

### Ticket 1.1: TCP listener — bind, listen, accept

- [ ] In `src/socketcraft/server.py`, create a function or class that:
  - Creates a TCP socket (`AF_INET`, `SOCK_STREAM`)
  - Sets `SO_REUSEADDR` (research why this matters — what happens without it?)
  - Binds to a given host and port
  - Calls `listen()` with a backlog (research what the backlog parameter means)
  - Accepts a single connection and prints the client address
  - Closes everything cleanly
- [ ] You should be able to run the server and connect with `telnet` or `nc`

**Acceptance criteria:**
- Server starts without error and prints the address it's bound to
- `nc localhost <port>` connects successfully
- Server prints the client's address on connection
- Server shuts down cleanly with Ctrl+C (no tracebacks, sockets closed)

**Reading:**
- `man 2 socket`, `man 2 bind`, `man 2 listen`, `man 2 accept`
- `man 7 tcp` — understand the TCP state machine at a high level
- Python `socket` module docs
- Beej's Guide, chapters 5-6
- Research: what is `SO_REUSEADDR` and what bug does it prevent during development?

### Ticket 1.2: Read and echo loop

- [ ] After accepting a connection, read data from the client in a loop
- [ ] Echo every chunk back to the client exactly as received
- [ ] Handle the client disconnecting gracefully (what does `recv` return when the client closes the connection? Read the docs.)
- [ ] Handle the case where `send` can't write all bytes at once (research: what is a short write and when does it happen?)

**Acceptance criteria:**
- Connect with `nc`, type messages, see them echoed back
- Disconnecting the client doesn't crash the server
- Server is ready to accept a new connection after the previous client disconnects
- No data is silently dropped (verify by sending a known string and checking the response)

**Reading:**
- `man 2 recv`, `man 2 send`
- Research: blocking vs non-blocking sockets, what does the `MSG_WAITALL` flag do
- Research: `sendall()` in Python — what does it do that `send()` doesn't?

### Ticket 1.3: Accept loop — handle multiple sequential connections

- [ ] Wrap the accept-and-echo logic in an outer loop so the server handles one client, then waits for the next
- [ ] The server should run indefinitely until interrupted
- [ ] Add signal handling for `SIGINT` (Ctrl+C) — close the listening socket and exit cleanly

**Acceptance criteria:**
- Connect, chat, disconnect, connect again — works repeatedly
- Ctrl+C shuts down without `OSError` or socket leak warnings
- No zombie sockets left behind (research: `ss` or `lsof` commands to verify)

### Ticket 1.4: Write your first real tests

- [ ] Write a test that starts the server in a background thread, connects a client socket, sends data, and verifies the echo response
- [ ] Write a test that verifies graceful handling of client disconnect
- [ ] Write a hypothesis property test: for any arbitrary byte string, the server echoes it back identically

**Acceptance criteria:**
- `uv run pytest` passes all tests
- The hypothesis test runs at least 100 examples
- Tests clean up after themselves (no leaked threads, no ports left bound)
- Tests use a random available port (not hardcoded — research how to do this)

**Reading:**
- pytest docs: fixtures, conftest, parametrize
- hypothesis docs: strategies for binary data (`st.binary()`)
- Research: how to pick an available port for testing (hint: port 0)

### Ticket 1.5: Structured logging

- [ ] Create `src/socketcraft/log.py` with a configured logger
- [ ] Use Python's `logging` module (not print statements)
- [ ] Log: server start (address + port), client connect (address), client disconnect, bytes received/sent, errors
- [ ] Use appropriate log levels: INFO for lifecycle events, DEBUG for byte-level detail, ERROR for failures
- [ ] Replace all print statements in the server with log calls

**Acceptance criteria:**
- Running the server shows clean, structured log output
- Setting log level to DEBUG shows byte transfer details
- Setting log level to WARNING silences normal operation
- No print statements remain in server code

### Ticket 1.6: Release v0.1.0

- [ ] Update CHANGELOG.md
- [ ] Ensure all tests pass, ruff is clean
- [ ] Tag `v0.1.0`
- [ ] Write a brief section in `docs/architecture.md` describing the accept-echo loop with a diagram (ASCII art is fine)

**Acceptance criteria:**
- `git tag` shows `v0.1.0`
- CHANGELOG has a complete entry
- `docs/architecture.md` exists with a description of the current architecture

---

## Milestone 2: HTTP/1.1 Request Parsing — `v0.2.0`

> **Goal:** Parse raw bytes from a TCP connection into structured HTTP request objects. This is where you read RFC 9112 and understand what HTTP actually looks like on the wire. Your server should be able to receive a real HTTP request from `curl` and parse it into a method, path, headers, and body.

### Ticket 2.1: HTTP request line parser

- [ ] In `src/socketcraft/http.py`, implement parsing of the HTTP request line: `METHOD SP REQUEST-TARGET SP HTTP-VERSION CRLF`
- [ ] Support at minimum: GET, POST, HEAD, DELETE
- [ ] Validate the HTTP version (accept HTTP/1.1, reject others with a clear error)
- [ ] Return a structured object (dataclass or named tuple) — not a dict, not a raw tuple
- [ ] Handle malformed request lines: missing fields, wrong delimiters, absurdly long lines

**Acceptance criteria:**
- Parsing `b"GET /index.html HTTP/1.1\r\n"` returns a structured object with method=GET, path=/index.html, version=1.1
- Parsing garbage bytes raises a well-defined exception (not a generic ValueError — define your own)
- Hypothesis property test: no byte string crashes the parser (it either parses or raises your custom exception)

**Reading:**
- RFC 9112 Section 3: Request Line
- Research: CRLF vs LF, why HTTP uses CRLF, what happens in practice
- Research: what is request smuggling and why does strict parsing matter?

### Ticket 2.2: Header parser

- [ ] Parse HTTP headers: `field-name ":" OWS field-value OWS CRLF`
- [ ] Headers end with an empty line (`CRLF CRLF`)
- [ ] Handle duplicate headers (research: which headers can appear multiple times?)
- [ ] Handle header folding / continuation lines (research: is this still valid in HTTP/1.1?)
- [ ] Enforce a maximum header count and maximum header size (pick reasonable limits — justify your choices)

**Acceptance criteria:**
- Parses standard headers from a `curl` request correctly
- Handles `Content-Length`, `Host`, `Connection`, `Content-Type` at minimum
- Rejects headers that exceed size limits with a 431 status
- Hypothesis test: no byte sequence crashes the header parser

**Reading:**
- RFC 9110 Section 6.3: Header Fields
- RFC 9112 Section 5: Field Syntax
- Research: what is a header injection attack and how does header parsing prevent it?

### Ticket 2.3: Body reading

- [ ] Read the request body based on `Content-Length` header
- [ ] If `Content-Length` is present, read exactly that many bytes
- [ ] If `Content-Length` is absent on a POST, decide what to do (read the RFC for guidance)
- [ ] Handle the case where the client sends fewer bytes than `Content-Length` claims (timeout or error)
- [ ] Do NOT implement chunked transfer encoding yet (but note where you'd add it)

**Acceptance criteria:**
- `curl -X POST -d "hello" http://localhost:<port>/` — server correctly reads "hello" as the body
- A request with `Content-Length: 5` but only 3 bytes sent results in a timeout or error, not a hang
- Hypothesis test: for any valid Content-Length and matching body, parsing succeeds

### Ticket 2.4: Assemble the full request parser

- [ ] Combine request line + headers + body parsing into a single `parse_request(conn: socket) -> HttpRequest` function
- [ ] Define an `HttpRequest` dataclass with: method, path, version, headers (dict), body (bytes)
- [ ] The parser reads from the socket incrementally (not "read everything then parse")
- [ ] Add a total request timeout — if a complete request isn't received within N seconds, close the connection

**Acceptance criteria:**
- `curl http://localhost:<port>/hello` is parsed into a complete HttpRequest
- Slow clients (sending one byte per second) eventually get timed out
- Integration test: start server, send real HTTP request, verify parsed fields match
- All edge case tests from 2.1-2.3 still pass

### Ticket 2.5: Release v0.2.0

- [ ] Update CHANGELOG.md
- [ ] All tests pass, ruff is clean
- [ ] Tag `v0.2.0`
- [ ] Update `docs/architecture.md` with the request parsing pipeline

---

## Milestone 3: HTTP Response Building & Routing — `v0.3.0`

> **Goal:** Build HTTP responses from structured data and route requests to handler functions based on path and method. After this milestone, `curl` gets a real HTTP response back and you can define multiple endpoints.

### Ticket 3.1: HTTP response builder

- [ ] In `src/socketcraft/http.py`, create an `HttpResponse` dataclass: status_code, status_text, headers (dict), body (bytes)
- [ ] Implement `to_bytes() -> bytes` that serializes the response into a valid HTTP/1.1 response
- [ ] Support common status codes: 200, 201, 400, 404, 405, 408, 413, 431, 500
- [ ] Automatically set `Content-Length`, `Date`, and `Connection` headers
- [ ] Provide convenience constructors: `HttpResponse.ok(body)`, `HttpResponse.not_found()`, `HttpResponse.bad_request(reason)`, etc.

**Acceptance criteria:**
- `HttpResponse.ok(b"hello").to_bytes()` produces a valid HTTP response that `curl` can parse
- `curl -v http://localhost:<port>/` shows correct status line, headers, and body
- Hypothesis test: for any status code and body, `to_bytes()` produces parseable HTTP

**Reading:**
- RFC 9112 Section 6: Response
- RFC 9110 Section 15: Status Codes
- Research: why is `Content-Length` critical? What goes wrong without it?

### Ticket 3.2: Router

- [ ] In `src/socketcraft/router.py`, implement a router that maps (method, path) pairs to handler functions
- [ ] A handler function has the signature: `(request: HttpRequest) -> HttpResponse`
- [ ] Support registering routes with a decorator or method call (your design choice — justify it)
- [ ] If no route matches, return 404. If the path matches but the method doesn't, return 405.
- [ ] Support simple path parameters: `/users/{id}` should match `/users/42` and pass `id="42"` to the handler

**Acceptance criteria:**
- Registering a handler for `GET /hello` and hitting it with curl returns the expected response
- Hitting `POST /hello` (when only GET is registered) returns 405
- Hitting `/nonexistent` returns 404
- Path parameters are extracted correctly
- Test: register 5+ routes, verify each one matches correctly and wrong methods return 405

### Ticket 3.3: Wire it all together

- [ ] Update the server's connection handler to: parse request → route → call handler → build response → send
- [ ] Define a few demo handlers: `GET /` returns a welcome message, `GET /health` returns 200, `POST /echo` returns the request body back
- [ ] Handle exceptions in handlers: if a handler raises, return 500 (don't crash the server)

**Acceptance criteria:**
- `curl http://localhost:<port>/` returns welcome message with 200
- `curl http://localhost:<port>/health` returns 200
- `curl -X POST -d "test" http://localhost:<port>/echo` returns "test"
- A handler that raises an exception returns 500 and the server stays up
- `curl http://localhost:<port>/nope` returns 404

### Ticket 3.4: Release v0.3.0

- [ ] Update CHANGELOG, tag, docs

---

## Milestone 4: Thread Pool — `v0.4.0`

> **Goal:** Build a thread pool from scratch. Requests are dispatched to worker threads instead of being handled sequentially. This is the core concurrency milestone. You will understand why thread pools exist, how worker threads consume from a shared queue, and what happens when things go wrong.

### Ticket 4.1: Thread pool — basic implementation

- [ ] In `src/socketcraft/pool.py`, implement a `ThreadPool` class
- [ ] Constructor takes a `size` parameter (number of worker threads). Validate it (what should happen if size is 0? Negative?)
- [ ] Worker threads pull callables from a shared `queue.Queue`
- [ ] Implement `submit(fn, *args, **kwargs)` to enqueue work
- [ ] Worker threads run in a loop: get task from queue → execute → repeat
- [ ] All worker threads should be daemon threads (research: what does this mean and why does it matter here?)

**Acceptance criteria:**
- Creating a ThreadPool(4) starts 4 threads
- Submitting 10 tasks to a pool of 4 processes them (verify with a shared counter or log output)
- Tasks execute concurrently (time 4 sleep(1) tasks on a pool of 4 — should take ~1s, not ~4s)
- Pool handles exceptions in tasks without killing the worker thread

**Reading:**
- `threading` module docs: Thread, daemon threads, Event, Lock
- `queue` module docs: Queue, put, get
- Research: why a queue and not just spawning threads? What problem does the pool pattern solve?
- Research: what is the GIL and how does it affect this design? (Important: sockets release the GIL during I/O)

### Ticket 4.2: Graceful shutdown

- [ ] Implement `shutdown(wait=True)` on the thread pool
- [ ] When shutdown is called: stop accepting new tasks, let in-flight tasks finish, then join all threads
- [ ] Use a sentinel value or Event to signal workers to exit (your design choice)
- [ ] Handle the case where a task is stuck (add an optional timeout to shutdown)
- [ ] Wire this into the server's SIGINT handler: on Ctrl+C, shut down the pool gracefully

**Acceptance criteria:**
- Calling `shutdown(wait=True)` blocks until all in-progress tasks complete, then returns
- After shutdown, submitting new tasks raises an exception
- Ctrl+C on the server completes in-flight requests, then exits
- No threads are left running after shutdown (verify with `threading.enumerate()`)

**Reading:**
- Research: what is the difference between graceful and hard shutdown?
- Research: what is a sentinel value pattern in concurrent programming?

### Ticket 4.3: Integrate the thread pool with the server

- [ ] Replace the sequential accept loop with: accept connection → submit connection handler to thread pool
- [ ] The accept loop runs in the main thread; handlers run in pool workers
- [ ] Prove it works: add a handler with `time.sleep(2)`, hit it with two concurrent `curl` requests, verify both return in ~2s not ~4s

**Acceptance criteria:**
- Two slow requests complete concurrently
- Fast requests aren't blocked by slow ones
- Server handles at least 20 concurrent connections without errors
- All existing tests still pass

### Ticket 4.4: Thread pool tests

- [ ] Test: pool executes submitted tasks
- [ ] Test: pool limits concurrency to pool size
- [ ] Test: graceful shutdown waits for in-flight tasks
- [ ] Test: exception in a task doesn't kill the worker
- [ ] Test: submitting after shutdown raises
- [ ] Hypothesis test: for any sequence of tasks (with random sleep durations), all tasks eventually complete

**Acceptance criteria:**
- All tests pass
- No flaky tests (run the suite 10 times)

### Ticket 4.5: Release v0.4.0

- [ ] Update CHANGELOG, tag, docs
- [ ] Architecture doc should now describe the threading model with a diagram

---

## Milestone 5: Hardening & Load Testing — `v0.5.0`

> **Goal:** Make the server robust under adversarial conditions and measure its actual performance. This is where you develop the Antithesis mindset: what invariants does the server maintain, and how do you break them?

### Ticket 5.1: Connection limits and backpressure

- [ ] Set a maximum number of concurrent connections. When the limit is reached, new connections get a 503 response.
- [ ] Track active connection count (thread-safe)
- [ ] Research: what happens to TCP connections when the server can't accept fast enough? What is the kernel's listen backlog doing?

**Acceptance criteria:**
- With max_connections=5, the 6th concurrent client gets 503
- When a connection finishes, the slot is freed and new connections work
- The count never goes negative, never exceeds the limit (test under concurrent load)

### Ticket 5.2: Timeouts everywhere

- [ ] Implement a read timeout: if the client doesn't send a complete request within N seconds, close the connection with 408
- [ ] Implement a write timeout: if the client stops reading the response, don't hang the worker thread forever
- [ ] Implement an idle timeout: if a connection has no activity for N seconds, close it
- [ ] Make all timeouts configurable

**Acceptance criteria:**
- A client that connects but sends nothing gets disconnected after the read timeout
- A client that sends headers very slowly (slowloris attack) gets timed out
- All timeouts are exercised in tests

**Reading:**
- Research: what is a slowloris attack and why are timeouts the defense?
- Research: `socket.settimeout()` vs `select`/`selectors`

### Ticket 5.3: Fault injection testing

- [ ] Write tests that simulate: client disconnects mid-request, client sends malformed HTTP, client sends a request body larger than your limit, client sends headers with illegal characters, half-open connections (client disappears without closing)
- [ ] For each scenario, define what the server SHOULD do (not just "it shouldn't crash")
- [ ] Research: what is a half-open connection and how does TCP handle it?

**Acceptance criteria:**
- Every fault scenario has a test with a specific expected behavior
- The server survives all scenarios without crashing, leaking resources, or hanging
- No file descriptor leaks (check with `os.getpid()` + `/proc/<pid>/fd` or equivalent)

### Ticket 5.4: Locust load testing

- [ ] Create `loadtests/locustfile.py`
- [ ] Define user behaviors: hit GET /, GET /health, POST /echo with random payloads
- [ ] Run Locust against your server with 100, 500, 1000 simulated users
- [ ] Record: requests/sec, latency percentiles (p50, p95, p99), error rate
- [ ] Identify the bottleneck. Is it the thread pool? The GIL? The parsing? Socket I/O? Prove it.

**Acceptance criteria:**
- Locust runs and produces a report
- You can articulate where the bottleneck is and why
- The server doesn't crash under sustained load

**Reading:**
- Locust docs: quickstart, writing locustfiles
- Research: what is p99 latency and why do people care about it more than average?

### Ticket 5.5: Release v0.5.0

- [ ] Update CHANGELOG, tag, docs
- [ ] Add a "Performance" section to the README with your load test results

---

## Milestone 6: Trio Rewrite — `v0.6.0`

> **Goal:** Rewrite the concurrency layer using Trio's structured concurrency. The HTTP parser, router, and response builder stay the same. Only the accept loop, connection handling, and "thread pool" equivalent change. After this, you'll understand why structured concurrency exists and what it buys you over raw threads.

### Ticket 6.1: Learn Trio fundamentals

- [ ] Read the Trio tutorial end-to-end
- [ ] Build a throwaway script: a Trio echo server (not part of socketcraft, just for learning)
- [ ] Understand: nurseries, cancellation, checkpoints, structured concurrency guarantees
- [ ] Write notes (in a file, not just in your head) on how Trio's model differs from threading

**Acceptance criteria:**
- You can explain in your own words: what is a nursery, why can't tasks outlive their parent, what is a checkpoint
- Your throwaway echo server works

**Reading:**
- Trio docs: tutorial, design principles
- Nathaniel J. Smith's "Notes on structured concurrency" blog post
- Research: what problem does structured concurrency solve that threads don't?

### Ticket 6.2: Trio accept loop and connection handler

- [ ] Rewrite `server.py` to use Trio's socket support (`trio.open_tcp_listeners`)
- [ ] Each connection is handled in a child task inside a nursery
- [ ] Connection handling reuses the same HTTP parser and router (they're pure functions on bytes — they don't care about the concurrency model)
- [ ] Graceful shutdown via nursery cancellation

**Acceptance criteria:**
- `curl` works against the Trio server exactly as it did against the threaded server
- All existing integration tests pass with the Trio server (you may need a test fixture that selects the backend)
- Ctrl+C shuts down cleanly with no orphaned tasks

### Ticket 6.3: Compare threaded vs Trio under load

- [ ] Run the same Locust load test against both implementations
- [ ] Compare: throughput, latency percentiles, resource usage (memory, FDs, threads)
- [ ] Write up the comparison in `docs/architecture.md`

**Acceptance criteria:**
- Both implementations survive the same load test
- You have quantitative data comparing them
- You can explain why one outperforms the other in specific scenarios (or why they're similar, if they are)

### Ticket 6.4: Release v0.6.0

- [ ] Update CHANGELOG, tag, docs
- [ ] README now describes both backends and how to select them

---

## Milestone 7: Polish & Ship — `v1.0.0`

> **Goal:** Make this a project you'd be proud to show in an interview or put on your GitHub. Clean code, complete docs, a proper README, CI, and a tagged release.

### Ticket 7.1: README overhaul

- [ ] Project description, motivation, design choices
- [ ] Quick start: how to run the server
- [ ] Architecture overview with diagram
- [ ] Performance characteristics
- [ ] What you learned (brief, honest)
- [ ] Reference the Rust book chapter as inspiration, credit where due

### Ticket 7.2: CI with GitHub Actions

- [ ] On every push: run ruff check, ruff format --check, pytest
- [ ] On tag push: create a GitHub release with changelog entry
- [ ] Badge in README for CI status

### Ticket 7.3: Final review

- [ ] Read every file in the project. Is there dead code? Remove it.
- [ ] Is there a function without a docstring? Fix it.
- [ ] Is there a test that's flaky? Fix it or delete it.
- [ ] Run the full load test one more time. Record final numbers.

### Ticket 7.4: Release v1.0.0

- [ ] Final CHANGELOG entry
- [ ] Tag `v1.0.0`
- [ ] Push to GitHub
- [ ] You're done.

---

## Notes for Claude Code

When Hari says "I'm working on ticket X.Y":
1. Confirm you know which ticket he means
2. Ask what his plan is before he starts coding
3. If his plan is solid, let him go
4. If his plan has gaps, ask questions that expose the gaps — don't point them out directly
5. Never write code for him. Not even "something like this." If he needs pseudocode, he'll ask.

When Hari says "I'm stuck":
1. Ask what he's tried
2. Ask what he expected vs what happened
3. Point him to specific documentation sections
4. If he's stuck on a concept, explain the concept — but not how to implement it

When Hari says "I give up":
1. Now you can provide pseudocode, diagrams, and step-by-step guidance
2. Still don't write the actual Python. Walk him through the logic.
3. After he implements it, ask him to explain it back to you.
