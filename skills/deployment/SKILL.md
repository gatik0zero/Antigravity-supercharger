---
name: Deployment
description: "Build, test, and deploy applications with CI/CD pipeline setup and cloud deployment."
---

# Deployment Skill

## Trigger
Use this skill when asked to deploy, set up CI/CD, or configure hosting.

## Pre-Deployment Checklist
- [ ] All tests pass
- [ ] No linting errors
- [ ] Environment variables documented and configured
- [ ] Build succeeds in production mode
- [ ] Security audit (no hardcoded secrets, dependencies audited)
- [ ] Performance budget met
- [ ] Database migrations ready (if applicable)
- [ ] Rollback plan documented

## Deployment Platforms (Free Tier)

### Static Sites
| Platform | Best For | Deploy Command |
|---|---|---|
| **Vercel** | Next.js, React | `npx vercel` |
| **Netlify** | JAMstack, static | `npx netlify deploy` |
| **GitHub Pages** | Documentation, static | Push to `gh-pages` branch |
| **Cloudflare Pages** | Edge-first sites | `npx wrangler pages deploy` |

### Full-Stack
| Platform | Best For | Deploy Command |
|---|---|---|
| **Cloud Run** | Containers, APIs | Use Cloud Run MCP |
| **Railway** | Full-stack apps | `railway up` |
| **Render** | Web services, DBs | Git push to deploy |
| **Fly.io** | Global edge deploy | `fly deploy` |

### Databases (Free)
| Service | Type | Limit |
|---|---|---|
| **Supabase** | PostgreSQL + Auth | 500MB |
| **PlanetScale** | MySQL | 1 billion rows read/mo |
| **Neon** | Serverless Postgres | 0.5GB |
| **MongoDB Atlas** | Document DB | 512MB |

## CI/CD Pipeline Template (GitHub Actions)
```yaml
name: Deploy
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npm test
      - run: npm run build
      - run: [deploy command]
```

## Post-Deployment
- Verify the deployment URL is accessible
- Run smoke tests against production
- Monitor error rates for the first hour
- Set up uptime monitoring (UptimeRobot free tier)
