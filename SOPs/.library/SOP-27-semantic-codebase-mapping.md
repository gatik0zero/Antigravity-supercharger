# SOP-27: Semantic Codebase Mapping

## Goal & Scope
Generate and maintain a continuously updated, human-readable, and machine-queryable map of the codebase's purpose, architecture, and data flows.

## Strategy
Codebases become black boxes over time. Antigravity acts as a cartographer, using the Memory MCP to maintain a living, semantic map of the repository that explains *why* things exist, not just *what* they are.

## Directives
- **Autonomous Cartography**: Background agents continuously scan the codebase for new entities, services, and modules. **Mapping**: For every new entity discovered, create a node in the Memory MCP detailing its Single Source of Truth, its upstream dependencies, and its downstream consumers.
- **Visual Architecture Generation**: Upon request, generate high-fidelity Mermaid.js C4 architecture diagrams that represent the *current* state of the code, completely eliminating stale documentation.
- **Blast Radius Calculation**: Before modifying a core utility or database schema, query the semantic map to calculate the exact "blast radius" of the change, alerting the developer to all indirect side-effects before a single line of code is written.
