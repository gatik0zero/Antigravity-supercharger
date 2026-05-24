# SOP-25: Ephemeral Infrastructure

## Goal & Scope
Create environments that construct and destruct themselves precisely around the lifetime of a specific feature branch, testing phase, or agent task.

## Strategy
Staging environments are archaic and prone to configuration drift. Antigravity treats infrastructure as a disposable, on-demand resource. Environments exist only for the exact microsecond they are needed and vanish immediately after.

## Directives
- **Just-In-Time Provisioning**: When a new feature is conceptualized, the agent automatically generates docker-compose or Kubernetes manifests required to run the feature in total isolation. **Execution**: Spin up local containers (using bash/docker commands) solely for testing the specific feature, populated with synthetic data.
- **Auto-Destruction Protocols**: Once the PR is merged or the agent task is verified, a teardown hook is automatically executed. **Validation**: Ensure zero zombie containers, orphaned volumes, or dangling network interfaces remain.
- **Infrastructure as Memory**: The exact configuration that successfully ran the ephemeral environment is hashed and stored in the Memory MCP. If the feature needs to be revisited, the environment is resurrected identically in seconds.
