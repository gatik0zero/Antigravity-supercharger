# SOP-30: Feedback Loop Compounding

## Objective
To automatically integrate production telemetry and user feedback back into the IDE's context, informing future code generation and architectural decisions.

## Blue Ocean / Zero-to-One Strategy
The IDE should not be disconnected from production reality. Antigravity ingests crash reports, slow query logs, and user complaints, adjusting its own coding patterns so it never makes the same systemic mistake twice.

## Directives

### 1. Error Ingestion & Pattern Recognition
- **Action**: When a recurring error is identified (e.g., via Sentry logs), the agent analyzes the stack trace and commits the root cause pattern to the Memory MCP.
- **Prevention**: In all future code generation, the agent explicitly checks against this failure pattern (e.g., "Always check for null arrays before mapping, as learned from Prod Bug #402").

### 2. Performance Feedback Integration
- **Action**: Ingest slow query logs. Update the IDE's internal ruleset to enforce specific indexing strategies or caching layers for similar queries going forward.

### 3. UX Telemetry Loop
- **Action**: If telemetry indicates users are abandoning a specific form, the IDE proactively suggests a UX redesign ticket, providing a wireframe artifact of a lower-friction alternative.
