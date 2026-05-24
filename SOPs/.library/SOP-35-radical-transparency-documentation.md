# SOP-35: Radical Transparency Documentation

## Goal & Scope
Automatically generate and publish decision matrices, trade-offs, and failure logs for every major architecture choice, creating a culture of engineering transparency.

## Strategy
Documentation is usually written after the fact and only highlights the "happy path." Antigravity documentation captures the messy reality: *why* an approach was chosen, what alternatives were rejected, and what technical debt was intentionally accepted.

## Directives
- **Architecture Decision Records (ADRs) on Autopilot**: Whenever an agent makes a fundamental change (e.g., switching from REST to GraphQL, or changing a database schema), it must automatically draft an ADR. The ADR must list: Context, Options Considered, The Selected Option, The Trade-offs (specifically what is worse now), and The Intended Lifespan of the decision.
- **Public "Wall of Shame" for Tech Debt**: Maintain an auto-generated dashboard within the project documentation that ranks modules by their complexity, lack of test coverage, and known vulnerabilities. By making the debt hyper-visible, it incentivizes the team (and background agents via SOP-29) to clean it up.
- **Incident Autopsy Generation**: When a production incident is resolved, the agent parses the Slack logs, Sentry traces, and git commits to automatically draft a blameless post-mortem, detailing the timeline, root cause, and the automated rules put in place to prevent recurrence.
