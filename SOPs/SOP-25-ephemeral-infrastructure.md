# SOP-25: Ephemeral Infrastructure

## Objective
To create environments that construct and destruct themselves precisely around the lifetime of a specific feature branch, testing phase, or agent task.

## Blue Ocean / Zero-to-One Strategy
Staging environments are archaic and prone to configuration drift. Antigravity treats infrastructure as a disposable, on-demand resource. Environments exist only for the exact microsecond they are needed and vanish immediately after.

## Directives

### 1. Just-In-Time Provisioning
- **Action**: When a new feature is conceptualized, the agent automatically generates docker-compose or Kubernetes manifests required to run the feature in total isolation.
- **Execution**: Spin up local containers (using bash/docker commands) solely for testing the specific feature, populated with synthetic data.

### 2. Auto-Destruction Protocols
- **Action**: Once the PR is merged or the agent task is verified, a teardown hook is automatically executed.
- **Validation**: Ensure zero zombie containers, orphaned volumes, or dangling network interfaces remain.

### 3. Infrastructure as Memory
- **Action**: The exact configuration that successfully ran the ephemeral environment is hashed and stored in the Memory MCP. If the feature needs to be revisited, the environment is resurrected identically in seconds.
