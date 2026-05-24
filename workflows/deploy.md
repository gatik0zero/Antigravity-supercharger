---
name: Deploy
description: "Build, test, and deploy application to production."
trigger: "/deploy"
---

# Deploy Workflow

## Step 1: Pre-Flight & Build
- Verify tests pass, no lints, correct env variables, no secrets, ready migrations.
- Run build command:
```bash
npm run build
```
- Verify clean build output, check bundle size budget, and verify all assets.

## Step 2: Deploy Platform
- Deploy to Cloud Run (use Cloud Run MCP), Vercel (`npx vercel --prod`), Netlify (`npx netlify deploy --prod`), GitHub Pages, or project scripts.

## Step 3: Post-Deploy & Rollback
- Visit URL, run smoke tests, verify APIs, and check Sentry error logs.
- If issues occur, revert to previous deployment, investigate, fix, and redeploy.

## Completion Report
```
## Deployment Report

**Version**: [version/commit]
**Platform**: [where deployed]
**URL**: [production URL]
**Status**: [✅ Success / ❌ Failed]
**Notes**: [any issues or observations]
```