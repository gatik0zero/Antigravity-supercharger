---
name: Apache Superset BI
description: "Data visualization and business intelligence dashboarding."
trigger: "/superset"
---

# Apache Superset BI Workflow

## Overview
This workflow utilizes the globally integrated `@superset` skill to interact with the repository.

## Step 1: Environment Analysis
- Locate the configured instance or local repository in the global skills directory.
- Verify API keys or environment variables required for connection.

## Step 2: Deployment & Configuration
- Set up the application infrastructure.
- Apply configurations or seed databases.

## Step 3: API & Extensibility
- Integrate custom scripts via the application's REST/GraphQL API.
- Create custom plugins/modules using the repository's framework.

## Tools
- **Filesystem MCP**: Browse the cloned repository locally.
- **Fetch MCP**: Connect to the running instance's API.
- **Postgres/SQLite MCP**: Interact with the application's database.
