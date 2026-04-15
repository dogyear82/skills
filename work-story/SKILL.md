---
name: work-story
description: Execute a tracked work item end-to-end using an ordered workflow with conditional multi-agent support. Use when Codex needs to pull a story, bug, task, or similar ticket from Jira or another connected tracker, analyze requirements, break the work down, inspect the codebase, use only the needed agents at each phase, implement the work on a branch, validate it, review it, and move the item to In Review when it is ready.
---

# Work Story

## Overview

Use this skill to work a tracked item from intake through review readiness.
The workflow is fixed and predictable: intake, normalize, inspect, plan, implement, test, review, and update the tracker. Agents are used inside those stages only when they add value.
Treat the default integration branch as the repository's normal PR target branch. Determine it from repo-local instructions first, then the repository or hosting-service default branch setting, then remote HEAD or an equivalent Git default-branch signal.

## Ordered Workflow

1. Fetch the work item from the named source.
If the user gives a Jira issue key and Jira is connected, use Jira first. Otherwise use the named tracker that Codex can access. See [references/source-adapters.md](references/source-adapters.md) for source selection and fallback rules.

2. Normalize the work item into an execution brief.
Extract the summary, problem, required behavior, acceptance criteria, constraints, dependencies, linked references, and current status. If the ticket is vague, tighten it into concrete, testable outcomes before implementation begins. Use a `product_owner` only when the ticket needs scope clarification, sharper acceptance criteria, or non-goal definition.

3. Build repository context.
Inspect the repository, local [AGENTS.md], test setup, relevant modules, and any repo-local agent definitions. Prefer repository rules and local agent variants when they exist. Use a `researcher` when the impact surface, relevant files, or existing behavior are not obvious.

4. Break the work down and evaluate design risk.
Decide the smallest working increment that satisfies the story. Use an `architect` only if the change crosses module boundaries, alters interfaces, or has meaningful migration tradeoffs. Use a `debugger` only if the story is driven by a failure or the root cause is still unclear.

5. Create a work branch.
Inspect the current branch before implementation begins. If the current branch is the default integration branch, or if its purpose does not clearly match the fetched work item, create a new branch from the default integration branch before making changes. Only continue on the current branch when it is already dedicated to the same work item and scope. Name work branches with the work item key first, followed by a short descriptive slug, such as `DOT-13-short-description`.

6. Implement the smallest viable increment.
Use an `implementer` once the task is clear enough to execute. Keep the branch coherent, commit as useful, and reduce scope if the story expands beyond the normalized acceptance criteria.

7. Test and look for edge cases.
Run the smallest relevant checks first. Use a `tester` when behavior needs stronger regression coverage, boundary-case coverage, or clearer verification than the main thread can provide quickly.

8. Run independent review.
Use a `reviewer` after implementation and testing. Review the work in PR style against the default integration branch, looking for bugs, regressions, missing tests, risky assumptions, and scope mismatches. Resolve material findings, then review again. Repeat the review-and-fix loop until no further material issues are found.

9. Update the tracker.
When the story is implemented, tested, and reviewed to a clean state, update the work item and move it to `In Review`, and leaving clear manual testing instructions in the comments. If the environment supports it, prepare or open a Pull Request targeting the default integration branch. If progress is blocked by something that requires human intervention, such as a missing external dependency, unavailable credential, inaccessible system, or unclear requirement that cannot be responsibly inferred, move the work item to `Blocked` instead and leave a comment that explains why it is blocked and what is needed to unblock it.

## Conditional Agent Use

Use agents only at the stage where they add value:

- `product_owner` during normalization when the ticket is ambiguous
- `researcher` during repository inspection when the codebase context is unclear
- `architect` during breakdown when design tradeoffs affect the implementation slice
- `debugger` during breakdown or implementation when failure analysis is needed
- `implementer` during execution for bounded code changes
- `tester` during validation when extra verification depth is needed
- `reviewer` during final quality review

Prefer repo-local agents over global agents for the same role.

## Operating Rules

- Never commit directly to the default integration branch.
- Check whether the current branch matches the fetched work item before starting implementation; if it does not, create a new branch from the default integration branch.
- Name the branch with the work item key as the prefix, followed by a short descriptive slug, such as `DOT-13-short-description`.
- Do not move the work item to `In Review` if acceptance criteria are still unmet.
- Before moving to `In Review`, complete the PR-style review loop described in step 8.
- If a human-only blocker prevents completion, move the work item to `Blocked` and leave a comment describing the blocker and the specific unblock action needed.
- Prefer the smallest working increment over broad scope expansion.
- Follow the ordered workflow; do not skip directly to implementation unless the earlier stages are already clearly satisfied.
- Use repo-local instructions and agent definitions when they conflict with global defaults.
- Treat tester and reviewer output as quality gates, not optional polish.
- If the work item cannot be fetched from an accessible source, stop and report the missing access or identifier clearly.

## Completion Criteria

Treat the story as ready for `In Review` only when all of the following are true:

- The required behavior matches the normalized acceptance criteria.
- Relevant tests pass, or any missing verification is stated explicitly.
- The step 8 PR-style review loop no longer surfaces material issues, and any remaining findings are documented as non-blocking with clear rationale.
- The work exists on a non-default-integration branch whose purpose matches the work item.
- A Pull Request targeting the default integration branch has been prepared or opened when the environment supports it.
- The tracked item has been updated and transitioned to `In Review`.

## References

- Source handling and tracker fallback: [references/source-adapters.md](references/source-adapters.md)
- Agent selection and default compositions: [references/agent-selection.md](references/agent-selection.md)
