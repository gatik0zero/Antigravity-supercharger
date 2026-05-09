---
name: Restore State
description: "Rollback code, database schema, and agent memory to a specific snapshot."
trigger: "/restore-state"
---

# Restore State Workflow

## Step 1: Identify Snapshot
- List available snapshots in `.antigravity/snapshots/`
- Select the target snapshot based on commit hash or timestamp

## Step 2: Revert Code
```bash
git checkout [commit-hash]
```

## Step 3: Rollback Database
- Identify the matching schema dump in the snapshot
- Run the rollback script (e.g., `sqlite3 database.db < snapshot/schema.sql`)

## Step 4: Reload Agent Memory
- Import the memory graph snapshot into Memory MCP
- Verify the graph state matches the snapshot

## Step 5: Verify
- Run a smoke test to ensure the system is functional
- Check that the regression is indeed gone
