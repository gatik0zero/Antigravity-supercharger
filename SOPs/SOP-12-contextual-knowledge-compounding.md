# SOP 12: Contextual Knowledge Compounding

## 1. Objective
To build a proprietary knowledge graph and personalized environment by continuously storing user interactions, decisions, architectural choices, and system patterns into memory.

## 2. Scope
Applies to the AI agent's interaction loop, debugging sessions, and architecture planning.

## 3. Directives
### 3.1. The Memory Moat
- An intelligent IDE must remember. Do not ask the user for the same architectural preference twice. If a user states a preference (e.g., "Always use Zustand for state"), store it permanently.
- Use the `mcp_memory` server to map relationships between features, bugs, and specific files to build a semantic understanding of the codebase.

### 3.2. Proactive Context Retrieval
- Before initiating a major refactor or starting a new feature, query the knowledge graph or existing `.md` rule files to understand the historical context and avoid repeating past mistakes.

### 3.3. System-Level Compounding
- Every bug fixed and every architecture designed should make the next task faster. Document patterns in the `/rules/` directory or as new `SOPs` dynamically if they prove highly effective.

## 4. Executable Actions
- Call `mcp_memory_add_observations` whenever the user makes a significant architectural decision or clarifies a business rule.
- Call `mcp_memory_search_nodes` before starting a complex task to retrieve related past context.
