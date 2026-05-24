# SOP 20: Future-Proofing via Ultimate Abstraction

## Goal & Scope
Build highly decoupled, interface-driven systems that can instantly swap underlying technologies (such as LLM providers, databases, or payment gateways) to avoid vendor lock-in and ensure infinite scalability. | Scope: backend architecture, integration logic, and repository structure.

## Actions
- When scaffolding a new backend, always generate a `services/` or `adapters/` directory.
- Review all code to ensure core domain logic is entirely agnostic of the delivery mechanism or storage medium.
