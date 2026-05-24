# SOP 02: Security and Compliance

## 1. Objective
To guarantee that all code generated, modified, or reviewed by AI agents adheres to strict security standards, manages secrets appropriately, and complies with established vulnerability reporting workflows from integrated open-source projects (Akaunting, Chatwoot, Coolify, Dolibarr, ERPNext, Mautic, n8n, OpenProject, Snipe-IT, Superset).

## 2. Scope
This SOP applies to all backend logic, API integrations, data handling, and infrastructure configuration tasks.

## 3. Directives

### 3.1. Secrets Management (Global Rule)
- **NEVER hardcode API keys, tokens, passwords, or connection strings.**
- Use `.env` files for local development (which MUST be in `.gitignore`).
- Use environment variables for production environments.
- If a secret is accidentally committed during development, rotate it immediately and remove it from git history.

### 3.2. Application Security
- **Input Validation**: Validate ALL user inputs on both client and server sides. Assume all input is malicious.
- **SQL Injection Prevention**: Use parameterized queries or established ORMs. NEVER concatenate user input into SQL.
- **XSS Prevention**: Sanitize HTML inputs before rendering.
- **Authentication**: Hash passwords with bcrypt (minimum 12 rounds). Use JWT with short expiry and refresh tokens.
- **Authorization**: Implement Role-Based Access Control (RBAC) and verify permissions server-side.
- **Data Protection**: Default to HTTPS for all external requests. Encrypt sensitive data at rest. Do not log sensitive information (PII).

### 3.3. Vulnerability Reporting & Awareness
When dealing with integrated components, adhere to their specific security policies:
- **Scope Verification**: Always verify the supported versions before attempting to patch or test security issues (e.g., Snipe-IT 8.x is supported; < 4.0 is EOL).
- **No Production Testing**: Do not perform testing against production services (e.g., Chatwoot). Use self-hosted local instances for penetration testing or debugging.
- **Non-Qualifying Issues**: Do not report out-of-scope issues (e.g., missing HTTP headers, theoretical attacks without POC, automated scanner reports).
- **Responsible Disclosure**: If an agent discovers a vulnerability in an integrated tool, it MUST flag it for the user to report securely via the project's official security email (e.g., `security@coollabs.io`, `security@akaunting.com`) and NOT disclose it publicly in an issue or PR.

## 4. Executable Commands & Actions
- `npm audit` (Run regularly to check for vulnerable dependencies)
- `grep_search` (Search for hardcoded secrets like `password = "`, `API_KEY = "`)

## 5. Situational Triggers
- **Trigger**: Writing authentication logic or database queries.
- **Action**: Enforce bcrypt hashing, parameterized queries, and environment variable usage.
- **Trigger**: Identifying a security flaw in a third-party integrated module.
- **Action**: Draft a private security report for the user to send to the module's security contact.
