# SOP 16: Viral Loop Architecture

## 1. Objective
To direct the AI agent to architect products where user acquisition is fundamentally built into the code, making the product intrinsically better the more it is shared (Network Effects via Viral Loops).

## 2. Scope
Applies to feature conceptualization, onboarding flows, database schemas, and external sharing components.

## 3. Directives
### 3.1. Inherent Shareability
- Do not build isolated single-player apps. Every core action the user takes should naturally generate an artifact or a link that must be shared with someone else for the user to get maximum value (e.g., a collaborative document, a multiplayer game, a split-bill app).

### 3.2. Asymmetric Value Hooks
- Code mechanisms that allow non-registered users to experience 80% of the value just by clicking a shared link, reducing the friction to join the network.

### 3.3. Embedded Referral Mechanics
- Instead of adding a generic "Invite Friends" button at the end of a flow, embed the invitation process directly into the core workflow (e.g., "Assign task to a teammate" -> triggers email invite).

## 4. Executable Actions
- When generating schemas, always include fields for tracking `invited_by`, `viral_coefficient`, or `shared_resource_ids`.
- During UI generation, ensure that sharing and collaboration buttons are primary actions, not hidden in settings menus.
