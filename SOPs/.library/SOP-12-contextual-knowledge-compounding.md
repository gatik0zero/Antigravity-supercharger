# SOP 12: Contextual Knowledge Compounding

## Goal & Scope
Build a proprietary knowledge graph and personalized environment by continuously storing user interactions, decisions, architectural choices, and system patterns into memory. | Scope: the AI agent's interaction loop, debugging sessions, and architecture planning.

## Actions
- Call `mcp_memory_add_observations` whenever the user makes a significant architectural decision or clarifies a business rule.
- Call `mcp_memory_search_nodes` before starting a complex task to retrieve related past context.

## Operational Context & Execution Guidelines
- **Implementation Focus**: Ensure that this standard operating procedure is strictly followed in conjunction with all secondary systems. Prioritize correct functionality and maintain the integrity of all triggers and associated actions under any circumstances. Keep operations robust, reliable, and well-documented.
