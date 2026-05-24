# SOP 19: Time-to-Magic (TTM) Optimization

## Goal & Scope
Ruthlessly minimize the time it takes for a new user to experience the core "magic" or primary value proposition of the application. | Scope: frontend workflows, onboarding funnels, and initial data loading architectures.

## Actions
- When generating React/Next.js components, enforce strict lazy loading for anything not required for the immediate "magic" moment.
- Strip out any mandatory email verification flows blocking the core product usage during MVP generation.
