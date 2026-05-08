# SOP-33: Component Telepathy

## Objective
To build frontend and backend pairs that negotiate their own APIs dynamically, eliminating the need for rigid schemas or manual GraphQL/REST endpoint maintenance.

## Blue Ocean / Zero-to-One Strategy
API contracts are brittle and slow down development. Antigravity uses "Component Telepathy," where UI components declare their data needs, and the backend dynamically satisfies them without pre-defined routes.

## Directives

### 1. Declarative Data Needs
- **Action**: Frontend components specify the exact shape of the data they require directly within the component file (e.g., using a dynamic query syntax or tRPC-like inference).

### 2. Dynamic Backend Satisfaction
- **Action**: The backend does not have hardcoded `/api/users` routes. Instead, a central agentic resolver parses the frontend's request, dynamically constructs the optimal SQL/NoSQL query on the fly, and returns the exact payload.

### 3. Compile-Time Optimization
- **Action**: During the build step, the IDE analyzes these dynamic negotiations and hardcodes them into optimized, secure endpoints, giving the flexibility of dynamic querying during development and the speed/security of rigid endpoints in production.
