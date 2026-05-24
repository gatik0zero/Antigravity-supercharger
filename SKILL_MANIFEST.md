# Antigravity Supercharger Skill & SOP Manifest

> This manifest coordinates lazy-loading of all 35 SOPs, 24 workflows, and custom skills to maintain low-latency context windows.

---

## 1. Foundational Core (Always-On)
These files are critical for every developer session and must remain in the active context:
1. `rules/efficiency.md`: Atomic Output protocol & solution-first rules.
2. `rules/coding-standards.md`: JavaScript/TypeScript syntax and clean coding styles.
3. `rules/security.md`: Secrets management and zero-trust protocol enforcement.
4. `SOPs/SOP-INDEX.md`: Trigger mappings for lazy-loading conditional SOPs.

---

## 2. Dynamic SOP Lazy-Loading Mappings
Agents must ONLY load the full text of an SOP (using `view_file` or `read_file`) when the active task triggers a keyword listed below:

| SOP ID & Name | Scope / Trigger Keywords | Trigger Slash Command |
| :--- | :--- | :--- |
| **SOP-01-project-init-and-scaffolding.md** | new app, start project, initialize repository, scaffolding, vite, nextjs | `/setup` |
| **SOP-02-security-and-compliance.md** | environment secrets, secrets rotation, env validation, authentication, JWT | `/security` |
| **SOP-03-code-standards-and-efficiency.md** | code refactor, simplify code, code review, naming conventions | `/clean` |
| **SOP-04-workflows-and-data.md** | data pipeline, database migration, iot sensor, spark stream | `/data` |
| **SOP-05-review-and-deployment.md** | pull request, commit style, git branch, deploy staging, production push | `/deploy` |
| **SOP-06-10 (Strategy & Ideation)** | radical scalability, network effects, value curve, proprietary tech moats | `/ideation` |
| **SOP-11-15 (Architecture & Research)** | self-healing system, synthetic data generation, novel synthesis, research | `/research` |
| **SOP-16-20 (Growth)** | viral loop, frictionless checkout, time-to-magic, future-proofing | `/growth` |
| **SOP-21-25 (User & Cognitive Load)** | cognitive offloading, cross-pollination, synthetic user, value-first gen | `/cognitive` |
| **SOP-26-30 (Advanced Operations)** | state versioning, database tuning, tech-debt, predictive provisioning | `/advanced` |
| **SOP-31-35 (Resilience & Telepathy)** | chaos engineering, component telepathy, personalization UX, documentation | `/resilience` |

---

## 3. Global Skill Tiering Strategy
To avoid IDE UI threads freezing during startup:
1. **Tier 1 (Core)**: Checked globally under `~/.gemini/config/skills/.skill-tiers.json` and kept locally cached.
2. **Tier 2 (On-Demand)**: Never auto-indexed. Dynamically queried using `Context7` or folder search only.
