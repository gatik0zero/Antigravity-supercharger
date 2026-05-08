# SOP 18: Zero Trust Security as a Feature

## 1. Objective
To move beyond basic security compliance and implement cutting-edge, Zero Trust architectures that turn the product's security posture into a core marketing feature and a Blue Ocean differentiator.

## 2. Scope
Applies to network architecture, authentication flows, data storage, and environment configurations.

## 3. Directives
### 3.1. Verify Everything
- Never trust the internal network. Every microservice, every internal API call, and every database query must be authenticated and authorized. Implement mTLS (Mutual TLS) between all internal components.

### 3.2. Ephemeral Environments
- Do not rely on static production environments. Architect the deployment pipeline (via Coolify/Docker) to spin up ephemeral, short-lived instances that handle specific requests and then self-destruct, radically reducing the attack surface.

### 3.3. Advanced Biometric/Hardware Auth
- Bypass basic username/password schemas. Push for WebAuthn, Passkeys, and hardware-level encryption by default. Make the login experience passwordless.

## 4. Executable Actions
- During project setup, enforce the integration of Passkey libraries or advanced OAuth providers.
- Configure network routing to explicitly deny all traffic by default, only allowing whitelisted internal communication.
