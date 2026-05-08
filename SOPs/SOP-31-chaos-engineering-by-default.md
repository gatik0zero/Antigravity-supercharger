# SOP-31: Chaos Engineering by Default

## Objective
To inject deliberate latency and failure points during local development, ensuring the system is architected for resilience from day one.

## Blue Ocean / Zero-to-One Strategy
Developers usually build in pristine, zero-latency local environments, leading to brittle production code. Antigravity fundamentally breaks this by simulating the hostile reality of production networks directly in the IDE.

## Directives

### 1. Simulated Hostility
- **Action**: Intercept local network requests (e.g., via Playwright/Puppeteer or local proxies) and inject randomized latency (50ms - 3000ms), packet loss, and 500-level HTTP errors.
- **Enforcement**: If the application crashes or the UI hangs without graceful error handling, the agent blocks the commit and generates a fix implementing exponential backoff or skeleton loaders.

### 2. Dependency Disruption
- **Action**: Randomly kill critical dependencies (like a local Redis cache or Postgres database) for short intervals during active development.
- **Verification**: The agent verifies if the application degrades gracefully (e.g., serving stale cache) or fails catastrophically.

### 3. Resilience Profiling
- **Action**: Generate a "Resilience Score" for every PR based on how well the new code handled the injected chaos, preventing fragile code from ever reaching the `main` branch.
