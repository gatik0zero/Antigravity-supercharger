# SOP-26: Multi-Dimensional State Versioning

## Goal & Scope
Version not just code, but database schema, agent memory, and infrastructure config as a single atomic snapshot.

## Strategy
Git tracks code, but applications are composed of code, data state, and environment state. Antigravity treats the entire holistic state of the application as a single versioned entity, allowing for perfect time-travel debugging.

## Directives
- **Atomic Snapshots**: When creating a significant commit or milestone, the agent must dump the local database schema and critical state, export the current IDE environment variables (sanitized), and snapshot the Memory MCP knowledge graph. **Storage**: Bundle these artifacts alongside the code commit using a `.antigravity/snapshots/` registry.
- **Time-Travel Restoration**: If a regression occurs, the agent can use a `/restore-state` command to revert the code, rollback the database to the exact matching schema, and reload the agent's memory to that specific point in time.
- **State-Aware Diffing**: When reviewing PRs, agents must provide a "Multi-Dimensional Diff"—showing not just what code changed, but how the database schema morphed and what new architectural concepts were added to the memory graph.
