---
name: Code Review
description: "Performs a comprehensive code review covering security, performance, maintainability, and correctness."
---

# Code Review Skill

## Trigger
Use this skill when asked to review code, audit a file, or check for issues.

## Process

### 1. Security Scan
- Check for hardcoded secrets (API keys, passwords, tokens)
- Identify SQL injection vulnerabilities
- Look for XSS attack vectors
- Verify input validation on all user-facing inputs
- Check for insecure dependencies

### 2. Performance Analysis
- Identify N+1 query patterns
- Check for unnecessary re-renders (React) or DOM manipulation
- Look for memory leaks (unclosed connections, uncleared intervals)
- Identify blocking operations that should be async
- Check for missing indexes on database queries

### 3. Maintainability Check
- Code readability and naming clarity
- Function length and complexity (cyclomatic complexity)
- DRY violations (duplicated logic)
- Proper error handling and edge cases
- Test coverage gaps

### 4. Correctness Verification
- Logic errors and off-by-one mistakes
- Race conditions in async code
- Null/undefined handling
- Type mismatches
- Boundary conditions

## Output Format
```
## Code Review Summary

### 🔴 Critical (Must Fix)
- [issue description + file:line + fix suggestion]

### 🟡 Warning (Should Fix)
- [issue description + file:line + fix suggestion]

### 🟢 Suggestions (Nice to Have)
- [improvement + rationale]

### ✅ What's Good
- [positive observations]
```
