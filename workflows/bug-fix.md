---
name: Bug Fix
description: "Structured bug investigation, fix, and verification workflow."
trigger: "/bug-fix"
---

# Bug Fix Workflow

## Step 1: Reproduce & Investigate
- Confirm bug existence and document exact replication steps and environment.
- Apply `@debug-assistant` skill: analyze errors/stack traces, form 3 hypotheses, and test systematically.

## Step 2: Fix & Verify
- Apply minimal root-cause fix (not symptom). Update related pattern occurrences.
- Confirm bug fix, run tests, verify edge cases, and check for regressions.

## Step 3: Prevent & Report
- Add regression tests and update documentation.
- Output completion report template below.

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