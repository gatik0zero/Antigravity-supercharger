# SOP 13: Asymmetric Resource Utilization

## 1. Objective
To leverage cheap, free-tier, or open-source resources, serverless architectures, and edge computing to build massive scale and capabilities with near-zero initial cost.

## 2. Scope
Applies to infrastructure choices, database selection, hosting, and third-party API integrations.

## 3. Directives
### 3.1. Edge Over Center
- Deploy logic to the edge (e.g., Cloudflare Workers, Vercel Edge) to achieve global scale and minimal latency for free or pennies on the dollar. Do not default to heavy, centralized Kubernetes clusters for MVP projects.

### 3.2. Open Source Supremacy
- Utilize powerful open-source alternatives over expensive proprietary SaaS whenever possible. (e.g., Supabase over Firebase, PostHog over Mixpanel).
- Configure self-hosted versions using tools like Coolify to drastically reduce OPEX while maintaining complete control over data.

### 3.3. Serverless Databases
- Architect data layers using serverless databases (e.g., Neon, Turso) that scale to zero when not in use, ensuring that idle projects cost absolutely nothing to maintain.

## 4. Executable Actions
- When writing deployment scripts or Dockerfiles, configure them for platforms like Coolify or Vercel.
- Include `.env.example` configurations that default to open-source or free-tier providers.
