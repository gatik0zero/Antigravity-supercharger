---
name: Component Generator
description: "Generate web components following project patterns with proper structure, styling, and accessibility."
---

# Component Generator Skill

## Trigger
Use this skill when asked to create a new UI component, page section, or widget.

## Process

### 1. Analyze Existing Patterns
- Check existing components for structure and style conventions
- Identify the project's CSS methodology (vanilla, modules, Tailwind, etc.)
- Note the JavaScript framework in use (vanilla, React, Vue, etc.)

### 2. Design the Component
- Define the component's responsibility (single purpose)
- List props/inputs and their types
- Identify internal state needs
- Plan accessibility requirements

### 3. Generate Component
Follow this structure:
- **HTML**: Semantic markup with proper ARIA attributes
- **CSS**: Following project conventions, mobile-first responsive
- **JS**: Event handlers, state management, data binding
- **Tests**: Basic test cases for key functionality

### 4. Integration
- Show how to import/use the component
- Document props with types and defaults
- Provide usage examples

## Design Requirements
- Must be keyboard-navigable
- Must meet WCAG AA contrast requirements
- Must work across modern browsers (Chrome, Firefox, Safari, Edge)
- Must be responsive (320px to 1920px)
- Include loading/error/empty states where applicable
- Add smooth transitions (150-300ms) for state changes
