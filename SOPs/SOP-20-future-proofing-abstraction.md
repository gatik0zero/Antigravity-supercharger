# SOP 20: Future-Proofing via Ultimate Abstraction

## 1. Objective
To build highly decoupled, interface-driven systems that can instantly swap underlying technologies (such as LLM providers, databases, or payment gateways) to avoid vendor lock-in and ensure infinite scalability.

## 2. Scope
Applies to backend architecture, integration logic, and repository structure.

## 3. Directives
### 3.1. The Adapter Pattern
- Never hardcode direct calls to external APIs (e.g., `openai.createCompletion()`) in the core business logic.
- Always create a generic interface (e.g., `LLMService`) and implement specific adapters. This allows the system to switch from OpenAI to Anthropic or a local open-source model by changing a single environment variable.

### 3.2. Repository Pattern for Data
- Do not litter UI or controller code with direct SQL queries or ORM calls. Abstract database interactions behind repository interfaces, allowing seamless migration from SQLite to Postgres to MongoDB as the product scales.

### 3.3. Infrastructure as Code (IaC)
- Ensure all infrastructure is defined in code (Terraform, Docker Compose). Do not rely on manual dashboard configurations in AWS or Vercel.

## 4. Executable Actions
- When scaffolding a new backend, always generate a `services/` or `adapters/` directory.
- Review all code to ensure core domain logic is entirely agnostic of the delivery mechanism or storage medium.
