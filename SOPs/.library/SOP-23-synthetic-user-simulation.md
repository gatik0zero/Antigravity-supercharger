# SOP-23: Synthetic User Simulation

## Goal & Scope
Spawn autonomous agents that act as aggressive, unpredictable users to test UX flows, business logic, and security postures pre-launch.

## Strategy
Traditional testing involves static unit/E2E tests written by developers who know how the system *should* work. Antigravity uses LLM-powered synthetic users with specific personas (The Hacker, The Confused Grandpa, The Speedrunner) to dynamically break the app in unexpected ways.

## Directives
- **Persona-Driven Fuzzing**: Instantiate agents with distinct goals (e.g., "Try to checkout without paying," "Try to break the layout by pasting a 10MB text file into the bio field"). **Execution**: Use Puppeteer/Playwright MCP to let these agents navigate the local dev server autonomously.
- **Empathy and Frustration Mapping**: Synthetic users must report "frustration scores" based on time-to-task-completion, number of clicks, and confusing UI copy. **Feedback**: Generate a Heatmap Artifact detailing where synthetic users got stuck or abandoned the flow.
- **Zero-Day Vulnerability Hunting**: Deploy a "Malicious Insider" persona that attempts privilege escalation and IDOR attacks on every new endpoint before it is merged to main.
