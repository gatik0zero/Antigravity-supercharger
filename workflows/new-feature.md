---
name: New Feature
description: "End-to-end feature development: plan → implement → test → document."
trigger: "/new-feature"
---

# New Feature Workflow

## Step 1: Requirements & Plan
- Determine feature purpose, target user, and acceptance criteria.
- Create plan: list files, dependencies, data model, sketch UI, estimate complexity.

## Step 2: Implement & Test
- Order: Data layer → Business logic → API routes → UI components → Integration.
- Test: Write unit/integration tests, verify UI, check edge cases and error states.

## Step 3: Document & Review
- Update README, add JSDocs/inline comments, update API docs.
- Run `@code-review` skill on all modified files.

## Completion
- Output summary of created/modified files, test instructions, and future improvements.
