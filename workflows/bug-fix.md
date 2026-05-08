---
name: Bug Fix
description: "Structured bug investigation, fix, and verification workflow."
trigger: "/bug-fix"
---

# Bug Fix Workflow

## Step 1: Reproduce
- Confirm the bug exists
- Document exact steps to reproduce
- Note the environment (browser, OS, Node version)

## Step 2: Investigate
Apply the `@debug-assistant` skill:
- Read error messages and stack traces
- Form 3 hypotheses for the root cause
- Test each hypothesis systematically

## Step 3: Fix
- Apply the minimal fix that addresses the root cause
- Don't fix symptoms — fix the disease
- Update any related code that has the same pattern

## Step 4: Verify
- Confirm the original bug is fixed
- Run all existing tests
- Test edge cases around the fix
- Check for regressions in related features

## Step 5: Prevent
- Add a test that would catch this bug
- Update documentation if needed
- Consider if the root cause indicates a broader issue

## Completion Report
```
## Bug Fix Report

**Bug**: [description]
**Root Cause**: [explanation]
**Fix Applied**: [what changed]
**Files Modified**: [list]
**Tests Added**: [list]
**Verified**: ✅
```
