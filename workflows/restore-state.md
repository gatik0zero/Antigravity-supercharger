---
name: Restore State
description: "Rollback code, database schema, and agent memory to a specific snapshot."
trigger: "/restore-state"
---

# Restore State Workflow

## Step 1: Revert Code
- List snapshots in `.antigravity/snapshots/`.
- Revert code using:
```bash
git checkout [commit-hash]
```

## Step 2: Revert DB & Memory
- Run schema rollback (e.g. `sqlite3 database.db < snapshot/schema.sql`).
- Load memory graph snapshot into Memory MCP.

## Step 3: Verify
- Run smoke tests to ensure regression is resolved and system is functional.
