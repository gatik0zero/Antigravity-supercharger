---
name: Deploy
description: "Build, test, and deploy application to production."
trigger: "/deploy"
---

# Deploy Workflow

## Step 1: Pre-Flight Checks
- [ ] All tests pass
- [ ] No linting errors
- [ ] Build succeeds in production mode
- [ ] Environment variables are configured
- [ ] No hardcoded secrets in codebase
- [ ] Database migrations are ready

## Step 2: Build
```bash
npm run build
```
- Verify build output is clean (no warnings)
- Check bundle size against budget
- Verify all assets are included

## Step 3: Deploy
Based on the target platform, use the appropriate deployment:
- **Cloud Run**: Use Cloud Run MCP tool
- **Vercel**: `npx vercel --prod`
- **Netlify**: `npx netlify deploy --prod`
- **GitHub Pages**: Push to `gh-pages` branch
- **Custom**: Follow project-specific deployment script

## Step 4: Post-Deploy Verification
- [ ] Visit the production URL
- [ ] Run smoke tests (login, core actions)
- [ ] Check error monitoring (Sentry) for new errors
- [ ] Verify API endpoints respond correctly
- [ ] Confirm static assets load (images, fonts, scripts)

## Step 5: Rollback Plan
If issues are detected:
1. Revert to previous deployment
2. Investigate the failure
3. Fix and re-deploy

## Completion
```
## Deployment Report

**Version**: [version/commit]
**Platform**: [where deployed]
**URL**: [production URL]
**Status**: [✅ Success / ❌ Failed]
**Notes**: [any issues or observations]
```
