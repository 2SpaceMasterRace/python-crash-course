# hotcache — Ticket Backlog

Status key: `[ ]` = not started, `[~]` = in progress, `[x]` = done

---

## Milestone 0: Project Bootstrap — `v0.0.1`

> **Goal:** A working development environment with FastAPI installed, all tooling configured, and a single health endpoint that returns 200. You should be able to run `uv run uvicorn hotcache.main:app` and hit it with curl. Same philosophy as socketcraft M0 — don't skip the foundation.

### Ticket 0.1: Initialize the repository

- [ ] Create a new git repository
- [ ] Write an initial README.md with a one-paragraph project description
- [ ] Add an MIT LICENSE file
- [ ] Create a `.gitignore` appropriate for Python
- [ ] First commit: `chore: initialize repository`

**Acceptance criteria:**
- `git log` shows one commit with a conventional commit message
- No junk files tracked

### Ticket 0.2: Set up uv and project structure

- [ ] Initialize with uv, configure `pyproject.toml` with project metadata (name, version `0.0.1`, python requires `>=3.12`)
- [ ] Add dependencies: `fastapi`, `uvicorn[standard]`
- [ ] Add dev dependencies: `pytest`, `hypothesis`, `httpx` (needed for FastAPI TestClient), `ruff`, `locust`
- [ ] Create the `src/hotcache/` package layout per the structure in CLAUDE.md
- [ ] Verify: `uv run python -c "import hotcache"` exits 0

**Acceptance criteria:**
- All dependencies install cleanly
- `uv run python -c "from fastapi import FastAPI"` works
- src layout is used

**Reading:**
- uv docs: dependency groups, dev dependencies
- Research: what is `uvicorn[standard]` vs plain `uvicorn`? What extras does it install and why?

### Ticket 0.3: Configure ruff

- [ ] Add ruff config to `pyproject.toml`
- [ ] Enable rule sets: `E`, `F`, `I`, `N`, `UP`, `B`, `SIM`, `ANN`, `ASYNC` (the ASYNC set is important here — research what it catches)
- [ ] Target Python 3.12, line length 88
- [ ] Both `ruff check .` and `ruff format --check .` pass clean

**Acceptance criteria:**
- ruff config with all specified rule sets
- Zero warnings on the project
- You can explain what the `ASYNC` rule set catches and why it matters for a FastAPI project

**Reading:**
- ruff docs: ASYNC rules specifically
- Research: common async pitfalls that linters can catch (blocking calls in async functions, missing awaits)

### Ticket 0.4: Configure pytest

- [ ] Configure pytest in `pyproject.toml` with strict mode, testpaths, pythonpath
- [ ] Add `anyio` as a dev dependency (research: why do you need this for testing async FastAPI code?)
- [ ] Configure `pytest-anyio` or the equivalent for async test support
- [ ] Write a smoke test that creates a FastAPI TestClient and hits a dummy endpoint
- [ ] `uv run pytest` passes

**Acceptance criteria:**
- pytest discovers and runs async tests
- TestClient works with your FastAPI app
- hypothesis is importable

**Reading:**
- FastAPI docs: testing section
- Research: what is `httpx.AsyncClient` vs `TestClient` and when do you use each?
- pytest-anyio or anyio docs for async test support

### Ticket 0.5: Health endpoint and app skeleton

- [ ] In `src/hotcache/main.py`, create the FastAPI app
- [ ] Implement a `GET /health` endpoint that returns `{"status": "ok"}`
- [ ] Use a Pydantic model for the response (yes, even for this — establish the pattern early)
- [ ] Run with `uv run uvicorn hotcache.main:app --reload`
- [ ] Verify: `curl http://localhost:8000/health` returns the expected JSON
- [ ] Verify: `http://localhost:8000/docs` shows the auto-generated Swagger UI

**Acceptance criteria:**
- Server starts, health endpoint works
- Response matches the Pydantic schema
- Swagger docs render correctly
- A test hits the health endpoint via TestClient and asserts the response

**Reading:**
- FastAPI docs: first steps, path operations, response models
- Research: what is the `--reload` flag and why should you never use it in production?

### Ticket 0.6: Create CHANGELOG and tag v0.0.1

- [ ] CHANGELOG.md in Keep a Changelog format
- [ ] Tag `v0.0.1`

---

## Milestone 1: The Key-Value Store (Core Data Structure) — `v0.1.0`

> **Goal:** Build the in-memory store that holds key-value pairs with TTLs. No HTTP yet (beyond health). This milestone is about getting the data structure right — the API layer comes next. Think about what invariants this store must maintain and how you'd verify them.

### Ticket 1.1: Store — basic get/set/delete

- [ ] In `src/hotcache/store.py`, implement a `Store` class
- [ ] `set(key: str, value: bytes, ttl_seconds: float | None = None) -> None`
- [ ] `get(key: str) -> bytes | None` — returns None if key doesn't exist or is expired
- [ ] `delete(key: str) -> bool` — returns True if key existed, False otherwise
- [ ] `exists(key: str) -> bool`
- [ ] Decide on the internal data structure. A plain dict? A dict plus a separate expiry index? Think about what operations you'll need to do efficiently and choose accordingly.
- [ ] Keys are strings, values are bytes. Justify why bytes and not str. (Hint: think about what a real cache stores.)

**Acceptance criteria:**
- Set a key, get it back, value matches
- Get a nonexistent key returns None
- Delete a key, verify it's gone
- Hypothesis test: for any sequence of set/get/delete operations, the store behaves like a dict (minus TTL behavior)
- Hypothesis test: keys are arbitrary non-empty strings, values are arbitrary bytes

**Reading:**
- Research: how does Redis store values internally? Why bytes?
- Research: what data structures would you use for efficient TTL expiry? (Sorted set by expiry time? Heap? Separate dict?)

### Ticket 1.2: Store — TTL and passive expiry

- [ ] When a key is set with a TTL, record its expiry timestamp
- [ ] On `get()`, check if the key has expired. If so, delete it and return None. This is "passive" or "lazy" expiry.
- [ ] Implement `ttl(key: str) -> float | None` — returns remaining TTL in seconds, None if no TTL or key doesn't exist
- [ ] Handle edge cases: what if TTL is 0? Negative? Extremely large?

**Acceptance criteria:**
- Set a key with TTL=1, wait 1.5s, get returns None
- Set a key with TTL=10, immediately get returns the value
- `ttl()` returns a value that decreases over time
- Keys without TTL never expire
- Hypothesis test: for any positive TTL, the key is accessible before expiry and inaccessible after

**Reading:**
- Research: passive vs active expiry — what are the tradeoffs? (Redis uses both. Why?)
- Research: `time.monotonic()` vs `time.time()` — which should you use for TTLs and why?

### Ticket 1.3: Store — active expiry (background cleanup)

- [ ] In `src/hotcache/expiry.py`, implement a background task that periodically scans for and removes expired keys
- [ ] This will eventually run as an asyncio background task, but for now, implement the logic as a standalone function: `collect_expired(store) -> list[str]` that returns the keys it removed
- [ ] Think about the scanning strategy: do you check every key every time? Only a sample? What are the performance implications?
- [ ] The expiry manager should be configurable: scan interval, max keys per scan

**Acceptance criteria:**
- `collect_expired` correctly identifies and removes expired keys
- Non-expired keys are not touched
- Performance: scanning 10,000 keys with 100 expired completes in reasonable time
- Test: set 100 keys with short TTLs, run collect_expired after they expire, verify all are gone

**Reading:**
- Research: how does Redis do active expiry? (Probabilistic sampling — read about it)
- Research: why not just check every key? What happens at 1M keys?

### Ticket 1.4: Store — metadata and stats

- [ ] Implement `info() -> StoreInfo` that returns: total keys, keys with TTLs, expired keys removed (lifetime counter), memory estimate
- [ ] Track operation counts: gets, sets, deletes, hits (get returned a value), misses (get returned None)
- [ ] These counters must be accurate under concurrent access (think about this now even though you're not concurrent yet)

**Acceptance criteria:**
- After a sequence of operations, `info()` returns accurate counts
- Hit/miss ratio is correct
- Hypothesis test: for any sequence of operations, hits + misses = total gets

### Ticket 1.5: Store tests — comprehensive

- [ ] Test every public method with normal inputs
- [ ] Test edge cases: empty string key, empty bytes value, very long keys, very long values, unicode keys
- [ ] Test TTL boundary conditions: TTL of 0, very small TTL (0.001), very large TTL
- [ ] Hypothesis stateful test: model the store as a dictionary, generate random sequences of set/get/delete, verify the store matches the model (ignoring TTL)
- [ ] All tests pass, no flakiness

**Acceptance criteria:**
- Full coverage of the Store public API
- At least one stateful hypothesis test
- Run the suite 10 times — no failures

**Reading:**
- hypothesis docs: stateful testing (this is the advanced feature — read it carefully)
- Research: what is a model-based test and why is it powerful for data structures?

### Ticket 1.6: Release v0.1.0

- [ ] Update CHANGELOG, tag, docs
- [ ] Write initial `docs/architecture.md` describing the Store's design and invariants

---

## Milestone 2: REST API for Key Operations — `v0.2.0`

> **Goal:** Expose the store over HTTP. Clients can set, get, delete, and list keys via a clean REST API. Every endpoint has proper status codes, validation, and error handling. After this milestone, you can interact with hotcache using curl or any HTTP client.

### Ticket 2.1: Pydantic models for request/response

- [ ] In `src/hotcache/models.py`, define:
  - `SetKeyRequest`: key (str), value (str, base64-encoded bytes), ttl_seconds (float | None)
  - `KeyResponse`: key, value, ttl_remaining (float | None), created_at
  - `DeleteResponse`: key, deleted (bool)
  - `StoreInfoResponse`: mirrors StoreInfo from the store
  - `ErrorResponse`: detail (str), error_code (str)
- [ ] Use Pydantic v2 features: field validators, model_config, computed fields where appropriate
- [ ] Decide: should the API accept raw bytes or base64-encoded strings? Research how other APIs handle binary data over JSON.

**Acceptance criteria:**
- All models serialize/deserialize correctly
- Validation rejects invalid inputs with clear error messages
- Hypothesis test: for any valid inputs, round-trip through JSON works (serialize → deserialize → compare)

**Reading:**
- Pydantic v2 docs: models, validators, serialization
- FastAPI docs: request body, response model
- Research: how do APIs like S3 or Redis HTTP proxies handle binary values?

### Ticket 2.2: Key CRUD endpoints

- [ ] In `src/hotcache/routes/keys.py`, implement:
  - `PUT /keys/{key}` — set a key (request body: value + optional TTL). Returns 201 on create, 200 on update.
  - `GET /keys/{key}` — get a key. Returns 200 with value, 404 if not found/expired.
  - `DELETE /keys/{key}` — delete a key. Returns 200 with deleted=true, 404 if not found.
  - `GET /keys` — list all keys (not values). Returns 200 with a list of key names. Think about pagination.
  - `HEAD /keys/{key}` — check existence without fetching value. Returns 200 or 404.
- [ ] Use FastAPI's dependency injection to provide the Store to route handlers (research: `Depends()`)
- [ ] All endpoints return appropriate Pydantic response models

**Acceptance criteria:**
- Full CRUD cycle works via curl
- Status codes are correct for every case (create vs update, found vs not found)
- Response bodies match the Pydantic schemas
- Swagger docs show all endpoints with correct schemas
- Test each endpoint with TestClient

**Reading:**
- FastAPI docs: path parameters, request body, status codes, response model, dependency injection
- Research: PUT vs POST for key creation — what does REST say? What does idempotency mean here?
- HTTP spec: what is HEAD and why does it exist?

### Ticket 2.3: Error handling and middleware

- [ ] In `src/hotcache/middleware.py`, implement:
  - A request logging middleware: log method, path, status code, latency for every request
  - A global exception handler: unhandled exceptions return 500 with an ErrorResponse, not a stack trace
- [ ] Ensure Pydantic validation errors return 422 with a clear message (FastAPI does this by default — verify and customize if needed)
- [ ] Add a request ID header (`X-Request-ID`) to every response for tracing

**Acceptance criteria:**
- Every request is logged with method, path, status, and latency
- Unhandled exceptions return 500 with JSON, not HTML or plaintext
- Validation errors return 422 with field-level detail
- `X-Request-ID` header is present on every response
- Test: trigger a validation error, verify the response format. Trigger a 500, verify no stack trace leaks.

**Reading:**
- FastAPI docs: middleware, exception handlers
- Starlette docs: middleware (understand the layer below FastAPI)
- Research: why is a request ID important? How is it used in production?

### Ticket 2.4: Configuration with pydantic-settings

- [ ] Add `pydantic-settings` as a dependency
- [ ] In `src/hotcache/config.py`, define a `Settings` class that reads from environment variables:
  - `HOST` (default: 0.0.0.0)
  - `PORT` (default: 8000)
  - `MAX_KEYS` (default: 10000)
  - `MAX_KEY_SIZE` (default: 256 bytes)
  - `MAX_VALUE_SIZE` (default: 1MB)
  - `DEFAULT_TTL` (default: 300 seconds)
  - `EXPIRY_SCAN_INTERVAL` (default: 1.0 seconds)
- [ ] Use the Settings in the app via dependency injection
- [ ] Enforce limits: reject keys/values that exceed configured maximums with 413

**Acceptance criteria:**
- Settings load from environment variables
- Overriding via env vars works: `MAX_KEYS=5 uv run uvicorn hotcache.main:app`
- Exceeding a limit returns 413 with a clear message
- Test: verify each limit is enforced

**Reading:**
- pydantic-settings docs
- Research: 12-factor app methodology — why environment variables for config?

### Ticket 2.5: Integrate active expiry as a background task

- [ ] Use FastAPI's lifespan feature to start the expiry manager as a background asyncio task on startup
- [ ] The task runs `collect_expired` on the configured interval
- [ ] On shutdown, the task is cancelled cleanly
- [ ] Log expiry events: how many keys were cleaned up each cycle

**Acceptance criteria:**
- Set a key with TTL=2 via curl, wait 3 seconds, GET returns 404
- Logs show the expiry manager running and cleaning up keys
- Shutting down the server doesn't hang or raise CancelledError tracebacks
- Test: set many keys with short TTLs, verify they're gone after expiry + scan interval

**Reading:**
- FastAPI docs: lifespan events (the modern way, not the deprecated `on_event`)
- asyncio docs: `create_task`, task cancellation, `CancelledError`
- Research: what happens if your background task raises an exception? Does FastAPI handle it? What should you do?

### Ticket 2.6: Release v0.2.0

- [ ] Update CHANGELOG, tag
- [ ] Update docs/architecture.md with the API design and endpoint list
- [ ] Swagger docs should be complete and accurate

---

## Milestone 3: Pub/Sub via WebSockets — `v0.3.0`

> **Goal:** Clients can subscribe to key changes over WebSockets. When a key is set, updated, deleted, or expires, all subscribers watching that key receive a notification. This is where the concurrency model gets interesting — multiple async tasks sharing mutable state, and you have to get the notification ordering right.

### Ticket 3.1: PubSub registry

- [ ] In `src/hotcache/pubsub.py`, implement a `PubSubRegistry` class
- [ ] `subscribe(key: str, callback: Callable) -> Subscription` — register interest in a key
- [ ] `unsubscribe(subscription: Subscription) -> None` — remove a subscription
- [ ] `notify(key: str, event: Event) -> None` — send an event to all subscribers of a key
- [ ] Define event types: `key_set`, `key_updated`, `key_deleted`, `key_expired`
- [ ] Decide: should notify be sync or async? What are the implications of each?

**Acceptance criteria:**
- Subscribe to a key, trigger a notification, callback is invoked with the correct event
- Unsubscribe, trigger again, callback is NOT invoked
- Multiple subscribers on the same key all receive the notification
- Subscribing to key "a" does not receive notifications for key "b"
- Hypothesis test: for any sequence of subscribe/unsubscribe/notify operations, only active subscribers receive notifications

**Reading:**
- Research: observer pattern — what is it and how does pub/sub relate?
- Research: what happens if a callback is slow or raises? Should it block other subscribers?
- asyncio docs: if you go async, how do you fan out notifications concurrently?

### Ticket 3.2: Wire pub/sub into the store

- [ ] Modify the Store to accept a PubSubRegistry
- [ ] On `set()`: emit `key_set` (new key) or `key_updated` (existing key)
- [ ] On `delete()`: emit `key_deleted`
- [ ] On expiry (both passive and active): emit `key_expired`
- [ ] The store should not know the details of pub/sub — it just calls `notify()`. Separation of concerns.

**Acceptance criteria:**
- Setting a new key triggers `key_set`
- Updating an existing key triggers `key_updated`
- Deleting triggers `key_deleted`
- Expiry triggers `key_expired`
- Test: subscribe, perform operations, verify the correct events in the correct order

### Ticket 3.3: WebSocket endpoint

- [ ] In `src/hotcache/routes/ws.py`, implement `WS /ws/subscribe/{key}`
- [ ] On connect: register a subscriber for the given key
- [ ] When a notification arrives: send a JSON message to the WebSocket client with the event type, key, and new value (if applicable)
- [ ] On disconnect: unsubscribe, clean up
- [ ] Handle: client disconnects unexpectedly, client sends invalid messages, server shutdown while clients are connected

**Acceptance criteria:**
- Connect via WebSocket, set the key via HTTP, WebSocket receives notification
- Multiple WebSocket clients watching the same key all receive the event
- Client disconnect doesn't crash the server or leak subscriptions
- Test: use httpx or a WebSocket test client to verify the flow end-to-end

**Reading:**
- FastAPI docs: WebSockets
- Starlette docs: WebSocket handling (understand the layer below)
- RFC 6455: at minimum, understand the handshake and close handshake
- Research: what is the difference between WebSocket close codes 1000, 1001, 1006?

### Ticket 3.4: Subscription to key patterns (stretch goal)

- [ ] Support subscribing to key patterns: `WS /ws/subscribe/users:*` matches `users:1`, `users:2`, etc.
- [ ] Decide on the pattern syntax: glob? prefix only? regex? (simpler is better — justify your choice)
- [ ] Existing exact-match subscriptions still work

**Acceptance criteria:**
- Pattern subscription receives notifications for all matching keys
- Non-matching keys don't trigger notifications
- Performance: 1000 pattern subscriptions, setting a key checks them in reasonable time

### Ticket 3.5: Release v0.3.0

- [ ] Update CHANGELOG, tag
- [ ] Update architecture docs with pub/sub design and WebSocket flow
- [ ] Document the WebSocket protocol (what messages the server sends, what format)

---

## Milestone 4: Concurrency Correctness — `v0.4.0`

> **Goal:** Prove that hotcache behaves correctly under concurrent access. This is the Antithesis-minded milestone. You're not adding features — you're finding and fixing bugs that only appear under load. What are the invariants, and can you break them?

### Ticket 4.1: Identify the invariants

- [ ] Write a document (in `docs/invariants.md`) listing every invariant the system should maintain:
  - A key that was set and has not expired or been deleted is always retrievable
  - A key past its TTL is never returned to a client
  - Every subscriber receives every event for its key, in order
  - Operation counters are accurate (gets = hits + misses)
  - Active connections count never goes negative
  - No subscriber receives events after unsubscribing
  - List at least 5 more that you discover by reading your own code
- [ ] For each invariant, describe how you would test it under concurrency

**Acceptance criteria:**
- `docs/invariants.md` exists with at least 10 invariants
- Each invariant has a proposed test strategy

### Ticket 4.2: Concurrent store access tests

- [ ] Write tests that hammer the store from multiple asyncio tasks simultaneously
- [ ] Test: 100 tasks setting the same key concurrently — final value should be one of the set values
- [ ] Test: tasks setting and getting the same key — get never returns a partial or corrupted value
- [ ] Test: tasks setting keys while the expiry manager runs — no crashes, no lost keys that aren't expired
- [ ] If you find races, fix them. Document what you found.

**Acceptance criteria:**
- All concurrent tests pass reliably (run 20 times)
- Any races found are documented and fixed with an explanation
- You can articulate which operations need synchronization and which don't

**Reading:**
- asyncio docs: Lock, Event, Condition — when do you need these?
- Research: in asyncio (single-threaded), when can races actually happen? (Hint: every `await`)

### Ticket 4.3: WebSocket stress tests

- [ ] Write a test that connects 50 WebSocket clients to the same key, sets the key 100 times rapidly, and verifies all clients received all 100 notifications
- [ ] Write a test where clients connect and disconnect rapidly while events are firing
- [ ] Write a test where the server shuts down with active WebSocket connections
- [ ] Verify no memory leaks: connect 100 clients, disconnect them all, check that subscriptions are cleaned up

**Acceptance criteria:**
- All WebSocket stress tests pass
- No leaked subscriptions after disconnect
- Server shutdown with active connections is clean

### Ticket 4.4: Adversarial client tests

- [ ] Test: client sends an enormous key (exceeds MAX_KEY_SIZE) — rejected with 413
- [ ] Test: client sends an enormous value — rejected
- [ ] Test: client sends requests as fast as possible — server stays responsive
- [ ] Test: client opens a WebSocket and never reads from it (backpressure) — what happens?
- [ ] Test: client sends garbage over WebSocket — connection closed cleanly
- [ ] For each scenario, define the expected behavior before writing the test

**Acceptance criteria:**
- Every adversarial scenario has a test with explicit expected behavior
- The server survives all scenarios without crashing
- No resource leaks

### Ticket 4.5: Release v0.4.0

- [ ] Update CHANGELOG, tag
- [ ] `docs/invariants.md` is complete
- [ ] Document any races found and how they were fixed

---

## Milestone 5: Load Testing & Observability — `v0.5.0`

> **Goal:** Measure hotcache's actual performance under load and add enough observability to understand what's happening inside. You should be able to answer: how many requests/sec can it handle, where is the bottleneck, and what breaks first?

### Ticket 5.1: Locust load tests

- [ ] In `loadtests/locustfile.py`, define user behaviors:
  - Set random keys with random TTLs
  - Get random keys (mix of hits and misses)
  - Delete random keys
  - (If possible) WebSocket subscribers watching popular keys
- [ ] Run with 100, 500, 1000 simulated users
- [ ] Record: requests/sec, p50/p95/p99 latency, error rate
- [ ] Find the breaking point: at what load does the server start failing?

**Acceptance criteria:**
- Locust runs and produces a report
- You can identify the bottleneck and explain why
- Results are recorded in docs or README

**Reading:**
- Locust docs: writing locustfiles, custom load shapes
- Research: what is Little's Law and how does it relate to server capacity?

### Ticket 5.2: Stats endpoint

- [ ] Enhance `GET /health` or create `GET /stats` to return:
  - Uptime
  - Total keys, keys with TTLs, expired count
  - Operation counters (gets, sets, deletes, hits, misses)
  - Active WebSocket connections
  - Request count, error count
  - Memory usage estimate
- [ ] This endpoint should be fast — no expensive computation on the request path

**Acceptance criteria:**
- Stats endpoint returns accurate, real-time data
- Under load, the stats update correctly
- Hitting /stats doesn't measurably impact performance

### Ticket 5.3: Structured logging

- [ ] Replace any remaining print statements with structured logging
- [ ] Log format: JSON lines (one JSON object per log line)
- [ ] Include: timestamp, level, message, request_id, key (when relevant), latency (for requests)
- [ ] Configure log levels: DEBUG for per-request detail, INFO for lifecycle, WARNING for degradation, ERROR for failures

**Acceptance criteria:**
- Logs are valid JSON
- Grepping logs by request_id traces a full request lifecycle
- Log level filtering works correctly

**Reading:**
- Research: why JSON logging? What tools consume structured logs in production? (Datadog, Grafana Loki, etc.)
- Python logging docs: custom formatters, filters

### Ticket 5.4: Release v0.5.0

- [ ] Update CHANGELOG, tag
- [ ] Add performance section to README with load test results
- [ ] Architecture docs updated with observability design

---

## Milestone 6: Hardening — `v0.6.0`

> **Goal:** Make hotcache resilient to real-world operational scenarios. Memory limits, graceful degradation, proper shutdown, rate limiting. This is the difference between a toy and a service.

### Ticket 6.1: Memory management

- [ ] Enforce `MAX_KEYS` limit — when reached, reject new keys with 507 (Insufficient Storage) or implement an eviction policy
- [ ] If you implement eviction: choose a strategy (LRU, LFU, random, closest-to-expiry). Justify your choice.
- [ ] Track approximate memory usage. When approaching a configurable limit, start evicting or rejecting.

**Acceptance criteria:**
- Exceeding MAX_KEYS results in defined behavior (rejection or eviction)
- If eviction: the correct keys are evicted according to the policy
- Memory usage tracking is approximately correct (doesn't need to be byte-exact)
- Test: fill the store to capacity, verify behavior

**Reading:**
- Research: LRU vs LFU vs random eviction — tradeoffs in practice
- Research: how does Redis handle `maxmemory`? What eviction policies does it support?

### Ticket 6.2: Rate limiting

- [ ] Implement per-client rate limiting (by IP address)
- [ ] Use a token bucket or sliding window algorithm (implement it yourself, don't use a library)
- [ ] Configurable: requests per second, burst size
- [ ] Return 429 (Too Many Requests) with a `Retry-After` header when limited

**Acceptance criteria:**
- A client exceeding the rate limit gets 429
- `Retry-After` header is present and accurate
- Burst allows short spikes above the sustained rate
- Different clients have independent limits
- Test: send requests at 2x the limit, verify ~half are rejected

**Reading:**
- Research: token bucket vs sliding window vs fixed window — tradeoffs
- Research: what is the `Retry-After` header and what format does it use?
- Research: how do production services (Stripe, GitHub API) implement rate limiting?

### Ticket 6.3: Graceful shutdown

- [ ] On SIGTERM/SIGINT: stop accepting new connections, finish in-flight requests, close WebSocket connections with a proper close frame, shut down the expiry manager, then exit
- [ ] Add a shutdown timeout: if in-flight work doesn't complete in N seconds, force exit
- [ ] Log the shutdown sequence

**Acceptance criteria:**
- Sending SIGTERM during load test results in clean shutdown
- In-flight requests complete, new ones are rejected
- WebSocket clients receive a close frame (not a broken pipe)
- Server exits within the timeout

**Reading:**
- Uvicorn docs: shutdown behavior, graceful shutdown
- Research: SIGTERM vs SIGINT vs SIGKILL — what's the difference and which should trigger graceful shutdown?

### Ticket 6.4: Release v0.6.0

- [ ] Update CHANGELOG, tag
- [ ] Document operational behavior: shutdown, rate limiting, eviction

---

## Milestone 7: Polish & Ship — `v1.0.0`

> **Goal:** Ship it. Clean code, complete docs, CI, a proper README, and a tagged release you'd put on your resume.

### Ticket 7.1: README overhaul

- [ ] Project description, motivation
- [ ] Quick start: install, run, hit with curl
- [ ] API reference: all endpoints with examples
- [ ] WebSocket protocol documentation
- [ ] Architecture overview with diagram
- [ ] Performance characteristics
- [ ] Configuration reference (all env vars)
- [ ] What you learned

### Ticket 7.2: CI with GitHub Actions

- [ ] On push: ruff check, ruff format --check, pytest
- [ ] On tag: create GitHub release with changelog
- [ ] Badge in README

### Ticket 7.3: Dockerfile (optional but recommended)

- [ ] Multi-stage build: install deps, then copy app
- [ ] Run as non-root user
- [ ] Health check in the Dockerfile
- [ ] Document how to run with Docker in README

**Reading:**
- Research: multi-stage Docker builds — why?
- Research: why run as non-root in containers?

### Ticket 7.4: Final review

- [ ] Read every file. Remove dead code. Fill missing docstrings. Fix flaky tests.
- [ ] Run the full load test. Record final numbers.
- [ ] Ensure Swagger docs are complete and accurate.

### Ticket 7.5: Release v1.0.0

- [ ] Final CHANGELOG entry
- [ ] Tag `v1.0.0`
- [ ] Push to GitHub
- [ ] Done.

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
