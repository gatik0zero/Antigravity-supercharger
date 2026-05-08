---
trigger: always
---

# Security Rules

## Secrets Management
- NEVER hardcode API keys, tokens, passwords, or connection strings
- Use `.env` files for local development (always in `.gitignore`)
- Use environment variables for production
- If a secret is accidentally committed, rotate it immediately

## Input Validation
- Validate ALL user inputs on both client and server side
- Sanitize HTML inputs to prevent XSS attacks
- Use parameterized queries — NEVER concatenate user input into SQL
- Validate file uploads: check type, size, and sanitize filenames
- Rate-limit API endpoints to prevent abuse

## Authentication & Authorization
- Hash passwords with bcrypt (minimum 12 rounds)
- Use JWT with short expiry + refresh tokens
- Implement role-based access control (RBAC)
- Always verify permissions server-side (never trust the client)

## Data Protection
- Use HTTPS for all communications
- Encrypt sensitive data at rest
- Never log sensitive information (passwords, tokens, PII)
- Implement CORS properly — don't use `*` in production
- Set secure cookie flags: `HttpOnly`, `Secure`, `SameSite`

## Dependencies
- Keep dependencies up to date — run `npm audit` regularly
- Review new dependencies before installing (check downloads, maintainers, issues)
- Pin dependency versions in production
- Remove unused dependencies
