# Token Optimization & Efficiency Plan: Antigravity Supercharger

## 1. Executive Summary
The Antigravity workspace currently suffers from "Skill Proliferation" (>1000 folders) and "Instruction Bloat" (35+ SOPs). This results in high token usage, increased latency, and potential context drift. This plan introduces **Recursive Context Pruning** and **Skill Consolidation** to reduce token usage by an estimated 60-80% while increasing execution speed.

## 2. Phase 1: Skill Consolidation (The "Great Compression")
- **Problem**: 1000+ folders in `/skills/` create massive overhead for file discovery and context mapping.
- **Action**: 
  - Merge redundant skills (e.g., 10+ `azure-*` skills into a single `master-azure.md`).
  - Implement **Metadata Sharding**: Use a flat file structure for related skills instead of deep nesting.
  - Archive or delete duplicate/low-value skills.
- **Target**: Reduce folder count from 1000+ to <50 master categories.

## 3. Phase 2: Dynamic SOP Orchestration
- **Problem**: 35 SOPs are currently "Always-On" or listed in the global context.
- **Action**: 
  - Create an `SOP-INDEX.md` with 1-sentence summaries of each SOP.
  - Agents must use `grep` or `read_file` on specific SOPs *only* when the task matches the trigger.
  - Compress SOPs into "Atomic Instructions" (max 50 lines each).
- **Target**: Context window saving of ~30KB per session.

## 4. Phase 3: Efficiency Enforcement (Atomic Precision)
- **Problem**: Conversational filler and non-parallel tool usage.
- **Action**:
  - Update `rules/efficiency.md` to enforce **Atomic Output**: Start with code/solution, no bridge phrases ("Sure," "I've updated").
  - Mandatory **Parallelism**: Group file reads/edits into single turns.
  - **Memory MCP Integration**: Offload session history to the `memory` MCP instead of relying on chat history.
- **Target**: 50% fewer turns per task.

## 5. Phase 4: Automated Maintenance
- **Problem**: New skills and rules are added without optimization.
- **Action**:
  - Update `scripts/update_manifest.js` to flag unoptimized skills.
  - Implement a `skill-optimizer` tool that automatically compresses markdown files.

## 6. Next Steps (Audit Completion)
1. [ ] **Finalize Categorization**: Map current 1000 skills to Master Categories.
2. [ ] **Prototype Master Skill**: Convert `/skills/azure-*` to `/skills/master-azure.md`.
3. [ ] **Deploy Efficiency Core**: Update `rules/efficiency.md`.

---
*Prepared by Gemini CLI | Date: 2026-05-23*
