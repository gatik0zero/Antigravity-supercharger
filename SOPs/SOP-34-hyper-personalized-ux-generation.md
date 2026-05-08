# SOP-34: Hyper-Personalized UX Generation

## Objective
To create user interfaces that adapt their complexity, layout, and copy based on the specific user's interaction history and persona.

## Blue Ocean / Zero-to-One Strategy
One-size-fits-all UIs force a compromise between power users and beginners. Antigravity generates UIs that are fluid. The interface a user sees on day 1 is drastically different from the interface they see on day 100.

## Directives

### 1. Skill-Based Progressive Disclosure
- **Action**: By default, generate interfaces that hide advanced settings behind "Advanced" toggles.
- **Adaptation**: If the backend telemetry detects the user frequently uses keyboard shortcuts or advanced features, the UI autonomously refactors itself for that specific user, surfacing power-user tools and dense data views.

### 2. Dynamic Micro-Copy
- **Action**: Tooltips, onboarding modals, and error messages are not static strings. They are generated contextually.
- **Implementation**: If a user repeatedly fails form validation, the system dynamically generates a more explicit, step-by-step error message rather than repeating the same static string.

### 3. A/B Testing as a Native Primitive
- **Action**: When an agent generates a new UI component, it automatically generates a "Variant B" with a distinct psychological approach (e.g., Urgency vs. Trust). The system natively routes traffic between them without developer intervention.
