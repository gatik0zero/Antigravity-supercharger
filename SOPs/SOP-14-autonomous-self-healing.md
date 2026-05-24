# SOP 14: Autonomous Self-Healing & Resilience

## Goal & Scope
Write code that inherently expects failure and automatically recovers, diagnoses, and restarts without human intervention, creating a "Zero-Ops" environment. | Scope: backend services, external API integrations, background workers, and CI/CD pipelines.

## Actions
- When writing fetching logic or database queries, always wrap them in robust `try/catch` blocks with custom error classes.
- Generate automated tests that specifically simulate network failures and service outages to verify self-healing mechanisms.
