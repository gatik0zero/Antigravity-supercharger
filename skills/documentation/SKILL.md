---
name: Documentation
description: "Auto-generate comprehensive documentation: README, API docs, JSDoc, and inline comments."
---

# Documentation Skill

## Trigger
Use this skill when asked to document code, generate a README, or create API docs.

## Documentation Types

### README.md
```markdown
# Project Name

Brief description (1-2 sentences).

## Features
- Feature 1
- Feature 2

## Quick Start
[Installation and first-run instructions]

## Usage
[Code examples for common use cases]

## API Reference
[Key functions/endpoints with parameters]

## Configuration
[Environment variables and config options]

## Contributing
[How to contribute]

## License
[License type]
```

### Function Documentation (JSDoc)
```javascript
/**
 * Brief description of what the function does.
 *
 * @param {string} name - Description of the parameter
 * @param {Object} options - Configuration options
 * @param {number} options.timeout - Timeout in milliseconds
 * @returns {Promise<Result>} Description of return value
 * @throws {ValidationError} When input is invalid
 *
 * @example
 * const result = await fetchUser('john', { timeout: 5000 });
 */
```

### Inline Comments
- Comment the WHY, not the WHAT
- Explain business logic and non-obvious decisions
- Mark workarounds with `// WORKAROUND: <reason>`
- Mark technical debt with `// TODO: <description>`

## Rules
- Documentation must be accurate — wrong docs are worse than no docs
- Update docs when code changes
- Include runnable examples where possible
- Keep language simple and direct
