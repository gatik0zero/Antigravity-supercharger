# SOP 04: Workflows, Data, and Advanced Integrations

## 1. Objective
To leverage the full suite of specialized workflows, MCP servers, and data handling protocols within the Antigravity global environment for tasks involving data science, IoT, machine learning, and contextual knowledge generation.

## 2. Scope
Applies to tasks requiring data analysis, external documentation lookups, database queries, mathematical calculations, and execution of global workflows.

## 3. Directives

### 3.1. Utilizing Workflows
- **Always use dedicated workflows for complex tasks:**
  - `/Data Pipeline` for ingestion, cleaning, analysis, and visualization.
  - `/IoT Simulation` for mocking and analyzing IoT telemetry data.
  - `/ML Training` for end-to-end model training.
- Workflows are located in the IDE's global configuration directory (e.g., `~/.gemini/antigravity/workflows/`).
- If a workflow file contains `// turbo` above a step, agents can auto-run the `run_command` tool for that step (`SafeToAutoRun: true`). If `// turbo-all` is present, auto-run all commands.

### 3.2. Data Science & ML Protocols
- **Data Handling**: Always inspect data before processing (shape, dtypes, null counts). Never modify raw data; create processed copies. Handle missing values explicitly.
- **Analysis**: Start with EDA. Use appropriate statistical tests. Report confidence intervals.
- **Machine Learning**: Split data (train/val/test) BEFORE preprocessing. Track experiments. Never tune on the test set.
- **Visualization**: Every chart needs a title, labeled axes, and a legend. Use colorblind-friendly palettes.
- **Math/Data Integrity**: **NEVER hallucinate math or data.** Always write a script or query an MCP server to run calculations rather than guessing.

### 3.3. MCP Server Integrations
- **Context7 (`mcp_context7`)**: When writing code involving any library, framework, or API, automatically use Context7 tools to look up current documentation. Do not rely on potentially outdated training data.
- **Databases (`mcp_sqlite`, `mcp_postgres`)**: Use these servers for parsing large datasets or querying databases directly instead of reading files line-by-line.
- **Web Content (`mcp_fetch`, `mcp_brave-search`)**: Use `fetch` to read static content, API endpoints, or public pages. Use brave-search to gather recent web information.
- **Memory (`mcp_memory`)**: When discovering important project facts, architectural decisions, or recurring patterns, store them in the Memory MCP knowledge graph for future reference.

## 4. Executable Actions
- `mcp_context7_resolve-library-id` -> `mcp_context7_query-docs` (To fetch latest framework docs)
- `mcp_sqlite_read_query` (For local data analysis)
- `mcp_memory_add_observations` (To persist learned project context)

## 5. Situational Triggers
- **Trigger**: User asks "How do I do X in Next.js 14?"
- **Action**: Do not guess. Query Context7 for Next.js 14 documentation first, then provide the solution.
- **Trigger**: User uploads a 50MB CSV file for analysis.
- **Action**: Do not try to `view_file`. Load it into SQLite or run a Python script to analyze it.
