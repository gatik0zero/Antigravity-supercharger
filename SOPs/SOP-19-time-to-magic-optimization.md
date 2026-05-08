# SOP 19: Time-to-Magic (TTM) Optimization

## 1. Objective
To ruthlessly minimize the time it takes for a new user to experience the core "magic" or primary value proposition of the application.

## 2. Scope
Applies to frontend workflows, onboarding funnels, and initial data loading architectures.

## 3. Directives
### 3.1. Defer Signups
- If the application generates value (e.g., an AI generator, a specific calculation, a visualized chart), let the user do it immediately without creating an account. Require an account only to *save* or *export* the result.

### 3.2. Skeleton to Interactive in < 1s
- The architecture must prioritize the First Input Delay (FID) and Largest Contentful Paint (LCP). Use Server-Side Rendering (SSR) or Static Site Generation (SSG) for the landing experience.
- Pre-fetch critical interactive components so the magic happens instantly upon click.

### 3.3. Contextual Onboarding
- Eliminate generic "Welcome Tours". Provide tooltips and guidance strictly in the context of the user's immediate action.

## 4. Executable Actions
- When generating React/Next.js components, enforce strict lazy loading for anything not required for the immediate "magic" moment.
- Strip out any mandatory email verification flows blocking the core product usage during MVP generation.
