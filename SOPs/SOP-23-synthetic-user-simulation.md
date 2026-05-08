# SOP-23: Synthetic User Simulation

## Objective
To spawn autonomous agents that act as aggressive, unpredictable users to test UX flows, business logic, and security postures pre-launch.

## Blue Ocean / Zero-to-One Strategy
Traditional testing involves static unit/E2E tests written by developers who know how the system *should* work. Antigravity uses LLM-powered synthetic users with specific personas (The Hacker, The Confused Grandpa, The Speedrunner) to dynamically break the app in unexpected ways.

## Directives

### 1. Persona-Driven Fuzzing
- **Action**: Instantiate agents with distinct goals (e.g., "Try to checkout without paying," "Try to break the layout by pasting a 10MB text file into the bio field").
- **Execution**: Use Puppeteer/Playwright MCP to let these agents navigate the local dev server autonomously.

### 2. Empathy and Frustration Mapping
- **Action**: Synthetic users must report "frustration scores" based on time-to-task-completion, number of clicks, and confusing UI copy.
- **Feedback**: Generate a Heatmap Artifact detailing where synthetic users got stuck or abandoned the flow.

### 3. Zero-Day Vulnerability Hunting
- **Action**: Deploy a "Malicious Insider" persona that attempts privilege escalation and IDOR attacks on every new endpoint before it is merged to main.
