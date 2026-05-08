---
name: Debug Assistant
description: "Systematic debugging with root cause analysis, hypothesis testing, and fix verification."
---

# Debug Assistant Skill

## Trigger
Use this skill when asked to debug, fix, or investigate an issue.

## Process

### 1. Understand the Problem
- What is the expected behavior?
- What is the actual behavior?
- When did it start happening? (What changed?)
- Can it be reproduced consistently?

### 2. Gather Evidence
- Read error messages and stack traces carefully
- Check logs for relevant entries
- Inspect the state at the point of failure
- Identify the last known working state

### 3. Form Hypotheses
List 3 most likely causes, ranked by probability:
1. [Most likely cause + reasoning]
2. [Second most likely + reasoning]
3. [Third most likely + reasoning]

### 4. Test Hypotheses
For each hypothesis:
- What specific test would confirm/deny it?
- Execute the test
- Record the result
- Move to next hypothesis if disproven

### 5. Implement Fix
- Apply the minimal fix that addresses the root cause
- Don't mask symptoms — fix the actual problem
- Verify the fix resolves the issue
- Check for side effects in related code

### 6. Prevent Recurrence
- Add a test that would catch this bug
- Update documentation if the issue stemmed from unclear behavior
- Consider if similar patterns exist elsewhere in the codebase

## Output Format
```
## 🔍 Debug Report

**Symptom**: [what's broken]
**Root Cause**: [why it's broken]
**Fix**: [what was changed]
**Verification**: [how we confirmed it works]
**Prevention**: [test or guard added]
```
