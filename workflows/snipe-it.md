---
name: Snipe-IT Asset Management
description: "IT asset management and API integration workflow."
trigger: "/snipe-it"
---

# Snipe-IT Asset Management Workflow
Utilizes globally integrated `@snipe-it` skill.

## Steps
- **1. Env Analysis**: Locate configured instance/repo. Verify API keys / env vars.
- **2. Deploy & Config**: Set up application infrastructure. Apply configurations, seed databases.
- **3. API & Extend**: Integrate scripts via REST/GraphQL API. Create custom plugins/modules.

## Tools
- **Filesystem MCP**: Browse cloned repository locally.
- **Fetch MCP**: Connect to running instance API.
- **Postgres/SQLite MCP**: Interact with database.
