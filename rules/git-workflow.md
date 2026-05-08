---
trigger: manual
description: "Git workflow conventions. Invoke with @git."
---

# Git Workflow Rules

## Commit Messages
Format: `<type>(<scope>): <description>`

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`

Examples:
- `feat(auth): add JWT refresh token rotation`
- `fix(api): handle null response from payment gateway`
- `docs(readme): add deployment instructions`

Rules:
- Use imperative mood ("add" not "added")
- Keep subject line under 72 characters
- No period at the end of the subject line
- Body: explain WHAT and WHY, not HOW

## Branching
- `main` — production-ready code
- `develop` — integration branch
- `feature/<name>` — new features
- `fix/<name>` — bug fixes
- `hotfix/<name>` — urgent production fixes

## Pull Requests
- Title follows commit message format
- Description includes: what changed, why, how to test
- Link related issues
- Keep PRs focused — one feature/fix per PR
- Self-review before requesting review
