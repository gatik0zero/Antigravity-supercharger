---
name: Code Review
description: "Comprehensive code review checklist for all changed files."
trigger: "/review"
---

# Code Review Workflow

## Step 1: Identify & Review
- List changed files and summarize changes.
- Apply `@code-review` skill for each file: security scan, performance analysis, maintainability, and correctness.

## Step 2: Cross-Cutting Concerns
- Verify consistency, missing files (tests, docs, migrations), pattern adherence, and breaking API changes.

## Step 3: Summary Report
- Output summary report using the template below.

## Summary Report
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