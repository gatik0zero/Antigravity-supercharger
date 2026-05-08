# SOP-21: Cognitive Load Offloading

## Objective
To autonomously handle context switching and mental state restoration for the developer, ensuring zero friction when resuming complex tasks.

## Blue Ocean / Zero-to-One Strategy
Standard IDEs require developers to manually track where they left off. Antigravity acts as a cognitive exoskeleton. It captures the exact mental state, active files, unresolved thoughts, and intended next steps, packaging them into a restorable context payload.

## Directives

### 1. State Snapshotting
- **Trigger**: Upon session termination or prolonged inactivity.
- **Action**: Agents must snapshot all active files, terminal states, and current focus areas.
- **Documentation**: Automatically generate a `CONTEXT_RESTORE.md` summarizing what was being worked on, the immediate roadblock, and the next logical action.

### 2. Contextual Rehydration
- **Trigger**: Upon session start.
- **Action**: Read the context snapshot and pre-fetch relevant documentation (using Context7) and database schemas (using Postgres/SQLite MCP).
- **Presentation**: Provide the developer with a 3-bullet summary of where they left off and pre-fill the terminal with the next suggested command.

### 3. Unresolved Thread Tracking
- **Action**: Monitor code for `TODO` or `FIXME` comments that reflect cognitive blocks rather than actual tasks (e.g., `// TODO: why does this return null?`).
- **Resolution**: Spawning background agents to investigate these cognitive blocks while the developer focuses elsewhere, presenting the solution asynchronously.
