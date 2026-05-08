---
trigger: glob
globs: ["**/*.ts", "**/*.tsx", "**/*.js", "**/*.jsx", "**/*.py", "**/*.go", "**/*.rs", "**/*.java", "**/*.cpp", "src/**/*", "lib/**/*"]
---

# Coding Standards

## Naming
- Variables/functions: `camelCase`
- Classes/components: `PascalCase`
- Files: `kebab-case`
- Constants: `SCREAMING_SNAKE_CASE`
- CSS classes: `kebab-case`

## Structure
- One component/class per file
- Max function length: 50 lines (refactor if longer)
- Max file length: 300 lines (split if longer)
- Import order: external → internal → relative → styles

## Documentation
- Every exported function: brief JSDoc comment (what + params + returns)
- Complex algorithms: inline comments explaining the WHY
- README.md: required for every project/module
- Never document obvious code (e.g., `// increment counter` before `counter++`)

## Error Handling
- Always use try/catch for async operations
- Provide meaningful error messages with context
- Log errors with enough detail to debug (but never log sensitive data)
- Fail gracefully — show user-friendly messages, log technical details

## Code Quality
- No `any` types in TypeScript (use proper typing)
- No magic numbers — use named constants
- No nested callbacks deeper than 2 levels — use async/await
- Remove dead code — don't comment it out
- No console.log in production — use proper logging