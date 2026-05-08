# SOP-27: Semantic Codebase Mapping

## Objective
To generate and maintain a continuously updated, human-readable, and machine-queryable map of the codebase's purpose, architecture, and data flows.

## Blue Ocean / Zero-to-One Strategy
Codebases become black boxes over time. Antigravity acts as a cartographer, using the Memory MCP to maintain a living, semantic map of the repository that explains *why* things exist, not just *what* they are.

## Directives

### 1. Autonomous Cartography
- **Action**: Background agents continuously scan the codebase for new entities, services, and modules.
- **Mapping**: For every new entity discovered, create a node in the Memory MCP detailing its Single Source of Truth, its upstream dependencies, and its downstream consumers.

### 2. Visual Architecture Generation
- **Action**: Upon request, generate high-fidelity Mermaid.js C4 architecture diagrams that represent the *current* state of the code, completely eliminating stale documentation.

### 3. Blast Radius Calculation
- **Action**: Before modifying a core utility or database schema, query the semantic map to calculate the exact "blast radius" of the change, alerting the developer to all indirect side-effects before a single line of code is written.
