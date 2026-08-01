---
name: work-story
description: Take a tracked development story from readiness assessment through implementation and a ready-for-review pull request. Use when Codex is asked to work, implement, complete, or pick up a story or issue end to end. Gate the work with $analyze-requirements, create an isolated worktree from the latest default branch only when ready, produce a plan with $plan-implementation, create and pursue a goal, verify the result, and publish the completed branch without merging it.
---

# Work Story

## Overview

Execute a story through a strict sequence: retrieve, assess readiness, isolate, plan, set a goal, implement, verify, review, and publish. Stop early when the story is not ready.

## Ordered Workflow

1. Resolve the story.
Retrieve the named story from its tracker, or use the story text supplied by the user. Read its linked specifications, documentation, and acceptance criteria. If the story cannot be retrieved, stop and state what is missing.

2. Load repository instructions.
Read the applicable `AGENTS.md`, repository documentation, and tracker guidance before assessing or changing anything. Determine the repository's default integration branch from local instructions, repository metadata, or remote HEAD.

3. Run the readiness gate with `$analyze-requirements`.
Apply its normalization, ambiguity detection, and sufficiency checks to the story. Use the repository's Definition of Ready when one exists. Otherwise require:

- a clear problem and outcome
- testable acceptance criteria
- a smallest coherent end-to-end scope
- a manual verification path
- clarified material assumptions
- no unanswered question that prevents safe implementation

Use `$analyze-requirements` only for this readiness decision; do not create its requirements artifact during the gate.

4. Stop if the story is not ready.
Do not create a branch, worktree, implementation plan, or goal. Respond only with:

```text
Not ready: <short reason>

Options:
- <specific way to resolve the gap>
- <another option only when useful>
```

Keep the explanation short. Ask a question only when the user can make the story ready by answering it immediately.

5. Create an isolated worktree from the latest default branch.
Fetch the default branch from its remote. Confirm the story does not already have an active branch or worktree that would conflict. Follow repository naming and worktree-location conventions; otherwise use `agent/<story-key>-<short-slug>` and a sibling worktree named `<repository>-<story-key>-<short-slug>`. Create both from the fetched remote default branch. Perform all remaining work inside the new worktree.

6. Create the implementation plan with `$plan-implementation`.
Run the skill inside the worktree using the retrieved story and repository context. Require a plan that covers every acceptance criterion and has no blocking open question. Save the plan using the repository's established convention or the planning skill's supported location.

7. Create the goal.
Use the goal tool to create one goal covering implementation of the plan, verification of every acceptance criterion, synchronization with the default branch, and publication of a ready-for-review pull request. Do not set a token budget unless the user requested one.

8. Pursue the goal.
Implement the smallest coherent change described by the plan. Follow existing patterns, reuse existing utilities, and avoid unrelated changes. Add or update tests alongside behavior. Commit small working changes with concise messages and push them as useful.

9. Verify and review.
Run the relevant tests, linting, type checking, and build. Manually verify the acceptance criteria when required. Review the complete diff against the default branch for correctness, missing tests, unrelated changes, and generated or temporary files. Fix material findings.

10. Synchronize and publish.
Fetch the latest default branch and rebase the story branch onto it. Resolve any conflicts without discarding unrelated work, then rerun affected checks. Push the branch and open a non-draft pull request targeting the default branch. Include the outcome, implementation summary, verification, risks, and manual testing instructions.

11. Complete the goal.
Mark the goal complete only after every acceptance criterion is verified, all required checks pass, the branch is synchronized, and the pull request is ready for review. Do not merge the pull request or delete the branch or worktree.

## Operating Rules

- Follow the ordered workflow without bypassing the readiness gate.
- Treat `$analyze-requirements` and `$plan-implementation` as required dependencies. If either is unavailable, stop and name the missing skill.
- Never implement from an unclear or incomplete story.
- Never work directly on the default branch.
- Preserve existing user changes and keep all story work inside its worktree.
- Do not broaden the story while pursuing the goal.
- Do not claim success when tests, acceptance criteria, synchronization, or PR creation remain incomplete.
- Follow the goal tool's rules when work is blocked; do not mark an incomplete goal complete.

## Completion Criteria

Treat execution as complete only when:

- the story passed the readiness gate
- the work was performed in its isolated worktree and branch
- the implementation follows the plan and satisfies every acceptance criterion
- relevant automated and manual verification passed
- the final diff is reviewed and contains no unrelated or temporary files
- the branch is rebased onto the latest default branch
- a non-draft pull request is open and ready for review
- the goal is marked complete
