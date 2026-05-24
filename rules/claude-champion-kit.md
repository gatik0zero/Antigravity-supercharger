# Claude Code Champion Playbook (Directive Dense)

## Core Behaviors
1. **Share Discoveries**: Post actual prompts, screenshots, and small wins in existing engineering channels, standups, or PR descriptions. Specific examples are highly persuasive.
2. **Respond with Prompts**: When asked how a task was done, reply with the exact prompt used (e.g. *"The test in @tests/scheduler.test.ts is flaky, figure out why"*).
3. **Establish Shared Habits**: Set up a dedicated `#claude-code` channel, post a weekly "show-and-tell" thread, or share reusable `.md` custom skills.

## Tactical FAQ & Answers
- **What to try first?**: Contain tasks, legacy code edits, test scaffolding, or boring chores.
- **Trusting the code**: Showcase "Plan Mode" (`Shift+Tab` to toggle) where changes are previewed and approved before modifying any file.
- **Conventions & Context**: Run `/init` to generate a `CLAUDE.md` to define repository conventions and directories to skip. Mention exact `@file` or `@directory/` references.
- **Handling Hallucinations**: Paste actual error traces, failing test outputs, or compiler outputs back to the agent rather than rephrasing the original prompt.

## Playbook & Execution
- **Week 1**: Create a dedicated `#claude-code` channel, pin a quickstart, and share 2 real examples.
- **Week 2**: Start a weekly Friday show-and-tell thread. Share 1 custom skill.
- **Week 3**: Offer a quick 15-minute pairing session to colleagues who show interest. Pin an FAQ.
- **Week 4**: Delegate channel ownership to another champion to grow organic adoption.

## Standard Objections Resolved
- *"I'm faster without it"*: Reframe to target boring scaffolding, deep research, or unfamiliar legacy files where agent leverage is highest.
- *"AI makes juniors weaker"*: Reframe as an active tutor. Ask the agent to explain a file and its call sites before writing code.
- *"Unsafe for production"*: Plan mode + PR diff review enforces standard code review before code goes live.
