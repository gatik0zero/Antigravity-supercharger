# SOP-31: Chaos Engineering by Default

## Goal & Scope
Inject deliberate latency and failure points during local development, ensuring the system is architected for resilience from day one.

## Strategy
Developers usually build in pristine, zero-latency local environments, leading to brittle production code. Antigravity fundamentally breaks this by simulating the hostile reality of production networks directly in the IDE.

## Directives
- **Simulated Hostility**: Intercept local network requests (e.g., via Playwright/Puppeteer or local proxies) and inject randomized latency (50ms - 3000ms), packet loss, and 500-level HTTP errors. **Enforcement**: If the application crashes or the UI hangs without graceful error handling, the agent blocks the commit and generates a fix implementing exponential backoff or skeleton loaders.
- **Dependency Disruption**: Randomly kill critical dependencies (like a local Redis cache or Postgres database) for short intervals during active development. **Verification**: The agent verifies if the application degrades gracefully (e.g., serving stale cache) or fails catastrophically.
- **Resilience Profiling**: Generate a "Resilience Score" for every PR based on how well the new code handled the injected chaos, preventing fragile code from ever reaching the `main` branch.
