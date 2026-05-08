# SOP 10: Multi-Agent Swarm Orchestration

## 1. Objective
To leverage the full capabilities of the Antigravity global environment by utilizing multiple specialized agents or sub-routines in parallel to solve complex, multi-faceted problems at unprecedented speeds.

## 2. Scope
Applies to massive refactors, full-stack application generation, and cross-domain research tasks.

## 3. Directives
### 3.1. Parallel Execution
- When given a massive task, do not execute it linearly. Break it down into discrete chunks (e.g., Frontend, Backend, Database, Docs) and utilize concurrent tool calls or sub-agents (via `browser_subagent` or `run_command` async tasks) to execute them simultaneously.

### 3.2. Asynchronous Tool Chaining
- Dispatch long-running background tasks (like `npm install` or massive database migrations) using `WaitMsBeforeAsync` and immediately proceed to write code or analyze docs while waiting.
- Check statuses using `command_status` periodically.

### 3.3. Specialized Delegation
- Use the right MCP server for the right job. Do not do web research with `fetch` if `mcp_brave-search` is faster. Do not read documentation locally if `mcp_context7` has the latest version. Orchestrate these tools like a conductor.

## 4. Executable Actions
- Issue concurrent tool calls (e.g., `<call:tool_1><call:tool_2>`) to fetch data, write to a file, and start a build process in the same turn.
- Use the `sequential-thinking` MCP tool for complex reasoning while simultaneously dispatching build commands.
