---
name: Code Review
description: "Comprehensive code review checklist for all changed files."
trigger: "/review"
---

# Code Review Workflow

## Step 1: Identify Changes
- List all modified/added/deleted files
- Summarize the purpose of the changes

## Step 2: Review Each File
For each changed file, apply the `@code-review` skill:
- Security scan
- Performance analysis
- Maintainability check
- Correctness verification

## Step 3: Cross-Cutting Concerns
- Are all changes consistent with each other?
- Are there any missing files (tests, docs, migrations)?
- Do the changes follow the project's existing patterns?
- Are there any breaking changes to existing APIs?

## Step 4: Summary Report
```
## Review Summary

### Files Reviewed: [count]
### Overall Assessment: [APPROVE / REQUEST CHANGES / NEEDS DISCUSSION]

### Critical Issues
[list or "None found"]

### Suggestions
[list of improvements]

### Positive Notes
[what's done well]
```
