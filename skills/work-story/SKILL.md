---
name: work-story
description: 'Use when asked to "start story #123", "begin work on XYZ", "start on the next story on the board", or otherwise start, implement, complete, or pick up a tracked story or issue end to end.'
---

# Work Story

## Overview

Take a tracked story from readiness assessment through a verified implementation and ready-for-review pull request. Stop early when the story is not ready.

## Workflow

Before each phase, inspect the skills available in the current runtime and invoke those whose triggers match the work. The workflow depends on completed outcomes, not particular skill names.

1. Resolve the story and repository guidance. Retrieve the named tracked story, or use the story text supplied by the user. Read linked specifications, documentation, acceptance criteria, applicable `AGENTS.md`, repository guidance, and tracker guidance. Determine the default integration branch.

2. Assess readiness. Check the story's relevance, atomicity, complete slice, and acceptance criteria, and apply any repository Definition of Ready. Require a current unmet need, one coherent outcome, a complete observable and testable slice, and clear testable acceptance criteria.

3. Stop when not ready. Do not create a branch, worktree, implementation plan, or goal. State concise reasons and the information or decision needed to make the story ready. Ask a question only when the user can resolve it immediately.

4. Create an isolated worktree from the latest remote default branch. Fetch it, confirm that no active branch or worktree conflicts with the story, and follow repository naming and location conventions. Otherwise use `agent/<story-key>-<short-slug>` and a sibling worktree named `<repository>-<story-key>-<short-slug>`. Perform all remaining work in that worktree.

5. Investigate and write an implementation plan. Work in the new worktree, inspect relevant implementations and tests, identify existing patterns, and produce a plan covering every acceptance criterion with no blocking open question. Save it using repository conventions.

6. Establish one explicit goal covering implementation, verification of every acceptance criterion, synchronization with the default branch, and publication of a ready-for-review pull request. Do not set a token budget unless the user requested one.

7. Implement the smallest coherent change described by the plan. Follow existing patterns, reuse existing utilities, avoid unrelated changes, add or update tests alongside behavior, and commit small working changes with concise messages.

8. Verify acceptance criteria and review the diff. Run relevant tests, linting, type checking, and build; manually verify acceptance criteria when required. Review the complete diff against the default branch for correctness, missing tests, unrelated changes, and generated or temporary files. Fix material findings.

9. Rebase, rerun checks, push, and open a non-draft pull request. Fetch the latest default branch, rebase the story branch without discarding unrelated work, rerun affected checks, push the branch, and open a ready-for-review pull request targeting the default branch. Include the outcome, implementation summary, verification, risks, and manual test instructions.

10. Complete the goal only when the pull request is ready: every acceptance criterion is verified, required checks pass, the branch is synchronized, and the pull request is open and ready for review. Do not merge the pull request or delete the branch or worktree.

## Operating Rules

- Follow the workflow without bypassing readiness.
- Never implement from an unclear or incomplete story.
- Never work directly on the default branch.
- Preserve existing user changes and keep all story work inside its worktree.
- Do not broaden the story while pursuing the goal.
- Do not claim success when tests, acceptance criteria, synchronization, or pull-request creation remain incomplete.
- Follow the goal tool's rules when work is blocked; do not mark an incomplete goal complete.

## Completion Criteria

Execution is complete only when:

- the story passed the readiness assessment
- the work was performed in its isolated worktree and branch
- the implementation follows the plan and satisfies every acceptance criterion
- relevant automated and manual verification passed
- the final diff is reviewed and contains no unrelated or temporary files
- the branch is rebased onto the latest default branch
- a non-draft pull request is open and ready for review
- the goal is marked complete
