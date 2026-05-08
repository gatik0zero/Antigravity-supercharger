# SOP 05: Code Review, Version Control, and Deployment

## 1. Objective
To outline the standard operating procedures for reviewing code, managing git workflows, and deploying applications using the Antigravity global environment.

## 2. Scope
Applies to all bug fixes, pull request creations, branch management, and deployment operations.

## 3. Directives

### 3.1. Code Review & Quality Assurance
- **Use the `/Code Review` workflow** to ensure comprehensive reviews of all changed files.
- Ensure the code follows the guidelines in `coding-standards.md`.
- Read all relevant files before suggesting changes. Mentally test changes before proposing them.
- Look out for missing error handling, hardcoded secrets, and inefficient algorithms.

### 3.2. Git Workflow & Version Control
- **Branching Strategy**: 
  - `main` — production-ready code
  - `develop` — integration branch
  - `feature/<name>` — new features
  - `fix/<name>` — bug fixes
- **Commit Messages**: Format as `<type>(<scope>): <description>` (e.g., `feat(auth): add JWT refresh token rotation`).
- Use the imperative mood, keep subjects under 72 characters, and explain the WHY and WHAT in the body.
- **GitHub Integrations**: Use the `mcp_github` server to automatically create issues, pull requests, and review comments. Keep PRs focused on a single feature or fix.

### 3.3. Deployment & CI/CD
- **Use the `/Deploy` workflow** for building, testing, and deploying the application.
- If integrating with specific platforms (e.g., Coolify), refer to their specific contributing and deployment guidelines (`coolify_CONTRIBUTING`).
- Ensure all CI tests pass locally using `pnpm test` or similar before pushing.
- For E2E tests, utilize integrated playwright/puppeteer workflows as referenced in the `n8n_CONTRIBUTING` rules if applicable.

## 4. Executable Commands & Actions
- `mcp_github_create_branch`
- `mcp_github_create_pull_request`
- `mcp_github_push_files`

## 5. Situational Triggers
- **Trigger**: The user says "The feature is complete, let's ship it."
- **Action**: Run the `/Code Review` workflow mentally or explicitly. Create a descriptive commit. Push to a new branch, and create a Pull Request using the Github MCP tool.
- **Trigger**: A bug is reported in production.
- **Action**: Use the `/Bug Fix` workflow. Investigate the root cause, create a `hotfix/` branch, implement the fix, add tests to prevent regression, and submit a PR.
