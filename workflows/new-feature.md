---
name: New Feature
description: "End-to-end feature development: plan → implement → test → document."
trigger: "/new-feature"
---

# New Feature Workflow

## Step 1: Requirements
Ask the user (or determine from context):
- What should this feature do?
- Who is the target user?
- What are the acceptance criteria?

## Step 2: Plan
Create an implementation plan:
1. List all files that need to be created or modified
2. Identify dependencies and order of implementation
3. Define the data model / state changes
4. Sketch the UI (if applicable)
5. Estimate complexity (simple / medium / complex)

## Step 3: Implement
Execute in this order:
1. **Data layer** — models, schemas, database changes
2. **Business logic** — services, utilities, core functions
3. **API layer** — endpoints, routes, controllers
4. **UI layer** — components, pages, styles
5. **Integration** — wire everything together

## Step 4: Test
- Write unit tests for business logic
- Write integration tests for API layer
- Manually verify UI behavior
- Test edge cases and error states

## Step 5: Document
- Update README if the feature is user-facing
- Add JSDoc/inline comments for complex logic
- Update API documentation if endpoints changed

## Step 6: Review
Run the `@code-review` skill on all changed files.

## Completion
Provide a summary:
- Files created/modified
- How to test the feature
- Any known limitations or future improvements
