---
name: Testing
description: "Generate comprehensive test suites: unit, integration, and E2E tests."
---

# Testing Skill

## Trigger
Use this skill when asked to write tests, improve test coverage, or set up a testing framework.

## Test Types

### Unit Tests
- Test individual functions/methods in isolation
- Mock external dependencies
- Cover: happy path, edge cases, error cases
- Naming: `describe('functionName', () => { it('should...') })`

### Integration Tests
- Test component interactions
- Use real (or test) database connections
- Verify API endpoint contracts
- Test authentication flows

### End-to-End (E2E) Tests
- Test complete user workflows
- Use Playwright/Puppeteer for browser testing
- Cover critical user journeys:
  - Sign up → Login → Core action → Logout
  - Search → Select → Purchase/Submit
  - Error states and recovery

## Test Structure (AAA Pattern)
```javascript
it('should return user profile when authenticated', async () => {
  // Arrange — set up test data and conditions
  const user = createTestUser({ name: 'Alice' });
  const token = generateToken(user);

  // Act — execute the code under test
  const response = await api.get('/profile', { auth: token });

  // Assert — verify the result
  expect(response.status).toBe(200);
  expect(response.body.name).toBe('Alice');
});
```

## Coverage Targets
| Type | Target |
|---|---|
| Statements | > 80% |
| Branches | > 75% |
| Functions | > 85% |
| Critical paths | 100% |

## Rules
- Tests must be deterministic — no random failures
- Each test must be independent — no shared mutable state
- Test behavior, not implementation details
- Name tests descriptively — they serve as documentation
- Fast tests run first, slow tests (E2E) run separately
