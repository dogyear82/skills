# Work Story Generic Workflow Design

## Goal

Rewrite `work-story` as a portable end-to-end workflow that does not depend on `analyze-requirements`, `plan-implementation`, or named Superpowers skills.

## Trigger

Keep the existing invocation intent: start, begin, implement, complete, or pick up a tracked story or the next story on a board. Limit the frontmatter description to trigger conditions so agents load the full workflow.

## Workflow

1. Resolve the story and read its linked material and repository instructions.
2. Inspect available skills and invoke any that apply before acting.
3. Assess readiness using the repository's Definition of Ready plus four required checks:
   - the need remains relevant
   - the story has one coherent outcome
   - the story delivers a complete, observable, testable slice
   - the acceptance criteria are clear and testable
4. If readiness fails, stop before creating a branch, worktree, plan, or goal. Return concise reasons and specific options.
5. If readiness passes, create an isolated worktree and branch from the latest remote default branch.
6. Investigate the codebase and create an implementation plan covering the acceptance criteria, affected areas, tests, risks, and assumptions.
7. Create one goal from the plan and pursue it through implementation, verification, synchronization, and PR creation.
8. Implement the smallest coherent change, following repository instructions and applicable skills.
9. Run required automated and manual verification, then review the complete diff.
10. Rebase onto the latest default branch, rerun affected checks, push, and open a non-draft PR.
11. Mark the goal complete only when the PR is ready for review and all completion checks pass.

## Skill Selection

The workflow describes required outcomes, not named skill dependencies. At each phase, the agent must inspect the skills available in its current runtime and invoke those that apply. Missing optional skills must not stop the workflow when the required outcome can still be achieved safely.

## Boundaries

- Never begin implementation when readiness fails.
- Never work directly on the default branch.
- Keep story changes inside the isolated worktree.
- Do not broaden the story beyond its accepted outcome.
- Do not merge the PR or remove its branch or worktree.

## Validation

Forward-test at least these cases:

- an unready story stops before repository mutation and gives concise options
- a ready story reaches planning without referring to removed or named skills
- the skill remains discoverable from the existing example invocations
- structural validation passes and no stale skill references remain
