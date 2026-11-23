---
name: work-story
description: 'Use when asked to "start story #123", "begin work on XYZ", "start on the next story on the board", or otherwise start, implement, complete, or pick up a tracked story or issue end to end.'
---

# Work Story

## Overview

Take a tracked story from readiness assessment through a verified implementation and ready-for-review pull request. Stop early when the story is not ready. Discover each repository's standards, tools, test commands, and CI requirements; do not assume a particular language, framework, tracker, hosting provider, or development environment.

## Workflow

Before each phase, inspect the skills available in the current runtime and invoke those whose triggers match the work. Delegate planning, implementation, testing, and code-review procedures to applicable skills; supply them with the story, acceptance criteria, and applicable repository standards. Their procedures must satisfy this skill's readiness, automated verification, and delivery requirements. If no applicable skill is available, perform the phase directly. No particular skill package, including Superpowers, is required.

Identify the story's board and map its actual statuses or columns to To Do, In Progress, and Review using tracker configuration and repository conventions; do not assume literal names. If the story or destination is ambiguous, report the gap and ask only for the missing information before changing tracker state. Apply these stage meanings:

- To Do: the story is ready, but implementation has not started. Do not move an already-started story backward merely because this workflow is invoked, or mark an unready story as ready.
- In Progress: move the story here when implementation starts; keep it here while implementation, verification, or required checks remain incomplete.
- Review: move the story here when the non-draft PR is open and all required checks pass.
- Done: handled by the review workflow after successful merge; this skill does not move stories to Done.

Use the board's allowed transitions and verify each resulting state. Story transitions are part of this workflow; avoid redundant transitions when the story is already in the appropriate state.

This workflow includes pushing the story branch and opening a ready-for-review pull request; do not introduce a separate integration-choice checkpoint for those steps. It does not authorize merging. Apply the user's existing authorization and repository guidance throughout.

Rebasing the story branch on top of the latest version of the default branch is the preferred method of keeping the story branch in sync with the default branch.

## Concurrent Work

Assess unmet need and implementability against the latest remote default branch, not proposed changes in other PRs. Never reject, defer, skip, or move a story to Blocked because another open or draft PR touches the same files, panels, interfaces, or behavior, proposes the same change, or might create a merge conflict. Do not wait for that PR to merge or investigate unrelated PRs to reserve areas of the codebase. Existing tracker comments citing overlap or anticipated conflicts do not establish a blocker; reassess against the default branch and proceed when the story is otherwise ready.

Continue independently in the story's isolated worktree. Resolve actual conflicts if competing work reaches the default branch before this branch is synchronized, then rerun affected checks. If this work merges first, the other PR's owner handles its subsequent conflicts. Supply this rule to delegated planning, implementation, and review skills so they do not reintroduce overlap as a readiness gate.

Ownership protection applies to another worker actively implementing this same tracked story, not a different story or PR with overlapping code. A genuine missing prerequisite must be demonstrated from the story requirements and current default branch; file overlap or planned changes elsewhere are never sufficient evidence.

## Story Execution

1. Before assessing readiness or making any mutation, resolve the story and repository guidance with read-only evidence gathering. Retrieve the named tracked story, or use the story text supplied by the user. If asked to start on the next story on a board, identify the applicable board from repository, tracker, and user context; use that board's ordering and status conventions to select the next eligible story. Ask one concise clarifying question only when the board or its ordering cannot be determined safely; never select arbitrarily. Read linked specifications, documentation, acceptance criteria, applicable `AGENTS.md`, `CLAUDE.md`, README files, repository guidance, tracker guidance and issue history, current relevant implementation and tests, and recent relevant changes or releases when applicable. Determine the default integration branch. Compare the requested outcome with this evidence to establish whether a current unmet need remains.

2. Assess readiness. Check the story's relevance, atomicity, complete slice, and acceptance criteria, and apply any repository Definition of Ready. Require a current unmet need, one coherent outcome, a complete observable and testable slice, and clear testable acceptance criteria.

3. Stop when not ready. Do not create a branch, worktree, implementation plan, or goal. State concise reasons and the information or decision needed to make the story ready. Ask a question only when the user can resolve it immediately.

Before creating the worktree, claim the ready story using the tracker's established ownership mechanism and repository conventions. Prefer a designated agent/worker field, assignment, or claim feature that can represent the current agent accurately. Recheck existing ownership and active work first; do not overwrite another worker's claim or duplicate active implementation of this same tracked story without an explicit handoff. Overlap with a different story or PR does not prevent claiming this story. Use the current agent's known identity rather than hard-coded provider names, and do not represent the authenticated human account as the agent. If no suitable ownership mechanism exists, leave a story comment identifying the agent and stating that it is taking the work; include a session or task reference when available to distinguish concurrent workers. Verify the claim was recorded before implementation. If claiming is unavailable or ownership is ambiguous, report the gap before starting implementation. Do not create accounts, change tracker configuration, or assign a hosted coding agent merely to record ownership, since assignment may launch a separate worker.

4. Create an isolated worktree from the latest remote default branch. Fetch it, reuse an existing workspace for this same story when appropriate and avoid branch-name or worktree-path collisions, and follow repository naming and location conventions. Otherwise use `<agent-name>/<story-key>-<short-slug>` and a sibling worktree named `<repository>-<story-key>-<short-slug>`. Perform all remaining work in that worktree and preserve existing user changes. Do not fall back to implementing on the default branch or outside the isolated worktree.

5. Produce an implementation plan in the new worktree using applicable planning skills and repository conventions. Require a mapping of every acceptance criterion to automated checks, with no blocking open question.

6. Track implementation, acceptance verification, synchronization with the default branch, and publication of a ready-for-review pull request in the implementation plan. Create a goal only when the user explicitly requests one. Do not set a token budget unless the user requested one. Follow the goal tool's rules when work is blocked; do not mark an incomplete goal complete.

7. Execute the plan using applicable implementation and testing skills, within the story scope.

8. Obtain automated acceptance evidence and a review of the complete diff against the default branch using applicable verification and code-review skills. Follow the Automated Verification requirements below and resolve material findings before publication.

9. Ensure the story branch is synced up with the default branch, rerun affected checks, push the branch, and open a ready-for-review pull request targeting the default branch. Include the outcome, implementation summary, acceptance evidence, verification commands and results, and material risks or unverified criteria. Follow required CI checks through completion and resolve failures caused by the change.

10. Complete the work only when the Completion Criteria below are met. Do not merge the pull request or delete the branch or worktree.

## Automated Verification

- Discover verification commands and required services from repository guidance, build scripts, existing tests, and CI configuration. Reuse the existing harness rather than prescribing a particular stack.
- Map every acceptance criterion to an observable automated check at the appropriate layer. Reuse coverage that proves the criterion; add or update focused tests when coverage is missing. For user-facing behavior, use the repository's browser or end-to-end harness when needed to verify the complete interaction.
- Run checks through test commands or CI. Do not routinely launch a separate development environment, leave an app running, perform manual browser click-throughs, or ask the user to test the change. Tests may start temporary applications, databases, or other services they need; use isolated state and ensure cleanup on success and failure.
- If no suitable harness exists, add the smallest reusable automation needed for the story when it fits the scope. If meaningful verification needs substantial new infrastructure or unavailable access, report the concrete gap and leave the affected acceptance criterion unverified. Do not silently substitute manual testing or claim completion.
- If the user explicitly requests a running environment or manual testing, perform it within that authorization. If repository guidance explicitly requires manual verification, surface the conflict with this automated workflow before proceeding with that step.
- Run checks appropriate to the changed behavior and all required repository gates. After a rebase or fix, rerun affected checks; repeat broader checks only when changes or unresolved failures warrant it. Record observed results, including failures and skips. A skipped required check is not a pass.

## Completion Criteria

Execution is complete only when:

- the story passed the readiness assessment
- the work was performed in its isolated worktree and branch
- the implementation follows the plan and satisfies every acceptance criterion
- every acceptance criterion has automated evidence and relevant required checks passed
- the final diff is reviewed and contains no unrelated or temporary files
- the branch is rebased onto the latest default branch
- a non-draft pull request is open and ready for review
- the story is in its board's Review status or column
- all explicitly requested goals are marked complete
