---
name: work-untracked
description: Execute an untracked development request end-to-end using an ordered workflow with conditional multi-agent support. Use when Codex needs to handle ad hoc development work that is not stored in Jira or another tracker, but should still be analyzed like a story, broken into a workable slice, inspected in the codebase, implemented, tested, and independently reviewed without creating branches, commits, or pull requests.
---

# Work Untracked

## Overview

Use this skill for direct development requests that are not tied to a tracked work item.
The workflow is fixed and predictable: normalize, inspect, break down, implement, test, and review. Agents are used only where they improve the quality of a specific stage.

## Ordered Workflow

1. Normalize the request into an execution brief.
Treat the user request like a story. Extract the problem, requested behavior, acceptance criteria, constraints, risks, and unknowns. See [references/intake-normalization.md](references/intake-normalization.md) for the normalization rules. Use a `product_owner` only when the request needs sharper scope, success criteria, or non-goal definition.

2. Build repository context.
Inspect the repository, local [AGENTS.md], test setup, relevant modules, and any repo-local agent definitions. Prefer repository rules and local agent variants when they exist. Use a `researcher` when the relevant code paths or impact surface are not obvious.

3. Break the work down and evaluate design risk.
Reduce the request to the smallest working increment that satisfies the normalized acceptance criteria. Use an `architect` only if the change crosses boundaries or introduces meaningful design tradeoffs. Use a `debugger` only if the request originates from a failure or the root cause is still unclear.

4. Implement the work.
Use an `implementer` once the task is clear enough to execute. Keep the worktree coherent, and reduce scope if the request expands beyond the normalized acceptance criteria.

5. Test and look for edge cases.
Run the smallest relevant checks first. Use a `tester` when stronger regression or boundary-case coverage is needed.

6. Run independent review.
Use a `reviewer` after implementation and testing. Resolve material findings before treating the work as complete.

## Conditional Agent Use

Use agents only at the stage where they add value:

- `product_owner` during normalization when the request is ambiguous
- `researcher` during repository inspection when context is unclear
- `architect` during breakdown when design tradeoffs affect the slice
- `debugger` during breakdown or implementation when failure analysis is needed
- `implementer` during execution for bounded code changes
- `tester` during validation when extra verification depth is needed
- `reviewer` during final quality review

Prefer repo-local agents over global agents for the same role.

## Operating Rules

- Do not create branches for this workflow.
- Do not create commits as part of this workflow.
- Do not assume the request is complete or well-scoped; normalize it first.
- Prefer the smallest working increment over broad scope expansion.
- Follow the ordered workflow; do not skip directly to implementation unless the earlier stages are already clearly satisfied.
- Use repo-local instructions and agent definitions when they conflict with global defaults.
- Treat tester and reviewer output as quality gates, not optional polish.

## Completion Criteria

Treat the work as complete only when all of the following are true:

- The implemented behavior matches the normalized acceptance criteria.
- Relevant tests pass, or any missing verification is stated explicitly.
- Reviewer findings are resolved or documented as non-blocking with clear rationale.
- No commit was created as part of the workflow.

## References

- Request normalization and scope tightening: [references/intake-normalization.md](references/intake-normalization.md)
- Conditional agent use and default compositions: [references/agent-selection.md](references/agent-selection.md)
