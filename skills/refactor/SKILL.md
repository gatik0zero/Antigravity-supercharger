---
name: Refactor
description: "Safe code refactoring with dependency analysis, risk assessment, and verification."
---

# Refactor Skill

## Trigger
Use this skill when asked to refactor, restructure, or reorganize code.

## Process

### 1. Understand Scope
- What needs to change and why?
- What are the boundaries of the refactor?
- Who/what depends on the code being changed?

### 2. Dependency Analysis
- Map all files that import/reference the target code
- Identify all callers of functions being changed
- Check for dynamic references (string-based imports, reflection)
- Note any external API contracts that must be preserved

### 3. Risk Assessment
| Risk Level | Criteria |
|---|---|
| 🟢 Low | Internal function, no external callers, has tests |
| 🟡 Medium | Multiple callers, some test coverage |
| 🔴 High | Public API, many dependents, no tests |

### 4. Execute Refactor
- Make one logical change at a time
- Preserve all existing behavior (unless explicitly changing it)
- Update all call sites simultaneously
- Update related tests
- Update documentation

### 5. Verify
- All existing tests pass
- No new TypeScript/linting errors
- Manual smoke test of affected features
- Verify no circular dependencies introduced

## Refactoring Patterns
- **Extract Function**: When a code block does too much
- **Rename**: When names don't convey intent
- **Move**: When code is in the wrong module
- **Inline**: When abstraction adds no value
- **Replace Conditional with Polymorphism**: When switch/if chains grow
- **Introduce Parameter Object**: When function has 4+ parameters
