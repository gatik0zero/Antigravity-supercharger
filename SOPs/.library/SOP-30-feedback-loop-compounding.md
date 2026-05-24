# SOP-30: Feedback Loop Compounding

## Goal & Scope
Automatically integrate production telemetry and user feedback back into the IDE's context, informing future code generation and architectural decisions.

## Strategy
The IDE should not be disconnected from production reality. Antigravity ingests crash reports, slow query logs, and user complaints, adjusting its own coding patterns so it never makes the same systemic mistake twice.

## Directives
- **Error Ingestion & Pattern Recognition**: When a recurring error is identified (e.g., via Sentry logs), the agent analyzes the stack trace and commits the root cause pattern to the Memory MCP. **Prevention**: In all future code generation, the agent explicitly checks against this failure pattern (e.g., "Always check for null arrays before mapping, as learned from Prod Bug #402").
- **Performance Feedback Integration**: Ingest slow query logs. Update the IDE's internal ruleset to enforce specific indexing strategies or caching layers for similar queries going forward.
- **UX Telemetry Loop**: If telemetry indicates users are abandoning a specific form, the IDE proactively suggests a UX redesign ticket, providing a wireframe artifact of a lower-friction alternative.
