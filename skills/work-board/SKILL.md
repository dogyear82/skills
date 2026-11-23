---
name: work-board
description: 'Use when asked to "work the board", drain a tracker board, or continuously pick up eligible reviews and stories across board columns.'
---

# Work Board

Work an existing tracker board from the stage closest to Done toward earlier stages: Review, In Progress, Ready, then Blocked. This skill owns selection and repetition; `review-pr` owns PR review and conditional merge, and `work-story` owns implementation and delivery. Read and invoke those skills when their work is selected rather than duplicating their procedures. If a required skill is unavailable, report the missing dependency before performing that phase.

## Establish Context

Resolve the board, repository scope, applicable `AGENTS.md`, `CLAUDE.md`, README files, tracker conventions, and current agent identity. Discover the board's actual Review, In Progress, Ready, Blocked, and Done mappings, ownership mechanism, and item order. Do not assume literal column names or treat an untriaged backlog as Ready. Ask only when missing context blocks correct selection.

Determine ownership from the established agent/worker field, claim feature, or claim comments using repository conventions, not merely the authenticated user or PR author. Match the current agent's identity consistently with `work-story`. Do not hard-code provider names. Unknown or conflicting ownership is not evidence of another agent's claim. Record gaps and leave ambiguous items untouched until resolved.

Read all relevant board items, including paginated results, and preserve board ordering. Do not reconfigure the board, create stories, reassign another worker's claim, or start additional workers merely to empty columns. Invoking this workflow authorizes the selected work's normal tracker updates, PR comments, publication, and conditional squash merge under the delegated skills, subject to any narrower user instruction.

## Selection Loop

Refresh board state and select one eligible item at a time in this priority order. A column with items but none eligible for this agent does not prevent checking the next column.

1. **Review:** In board order, select a story claimed by a different agent, with a linked PR ready for review. Invoke `review-pr` with its story, PR, repository guidance, and ownership context. Preserve the implementer's claim. Never review or merge your own claimed story through this loop. Do not treat an unclaimed or ambiguously claimed story as eligible for independent review.

2. **In Progress:** If no eligible Review work exists, select a story claimed by the current agent, in board order, and invoke `work-story` to resume it. Read its existing branch, worktree, PR, progress, and review findings; reuse the existing work rather than creating a duplicate branch or starting implementation over. Never take another agent's In Progress work. Do not start a second session on the same story if a current session is actively working it; require an explicit handoff or evidence the prior session has ended.

3. **Ready:** If neither earlier column has eligible work, take the top eligible story in the board's order and invoke `work-story`, which assesses readiness and claims it before implementation. Respect existing claims and active work; do not bypass a higher item simply because another looks easier. Recheck ownership and status immediately before claiming, use a conditional claim if supported, and confirm the result. If another worker took it, refresh and restart selection. Do not overwrite the competing claim.

4. **Blocked:** If no eligible work exists in Review, In Progress, or Ready, inspect Blocked stories in board order. Read each recorded blocker, linked dependencies, recent completions, and subsequent answers or decisions. Check whether completed work is merged and available where needed, and whether answers actually resolve the blocking question; a comment or closed dependency alone does not prove readiness. Move a story to Ready only when every blocker is resolved and the story meets readiness requirements. Leave a concise story comment linking the evidence, verify the transition, and immediately restart at Review. Never claim or implement a story while inspecting Blocked. Leave genuinely blocked stories in place and report what remains unresolved.

After any story changes column, immediately refresh and restart selection at Review before choosing another item. Finish the delegated skill's necessary bookkeeping for that same transition (such as verifying tracker state) first. Also refresh after a delegated operation completes without a transition; do not reuse an obsolete board snapshot.

## Progress and Stopping

Keep a compact durable progress record using repository conventions: board identity, selected story and revision, delegated action, observed result, transitions, and any item awaiting external change. Resume from verified tracker and repository state after interruption rather than repeating completed work or comments.

When a selected item cannot progress, record the concrete reason and evidence, then continue to other eligible items. Where tracker conventions support it, move truly blocked implementation work to Blocked with a blocker explanation; do not move an item merely to make a column empty. An unready Ready story stays unclaimed and is reported or moved to Blocked only when an actual blocker and valid transition are established.

Avoid repeatedly selecting an unchanged stalled item: reconsider it when relevant evidence changes, such as its revision, check results, ownership, blocker answer, or dependency completion. Do not repeatedly post the same comment. Do not wait indefinitely on another agent or silently cycle through the board without progress.

Complete this run when all of the following are verified against a fresh board snapshot:

- Ready is empty.
- In Progress contains no story claimed by the current agent. Other agents may still have In Progress work.
- Review contains no story claimed by another agent. The current agent's own completed stories may remain in Review awaiting independent review; this is an expected successful outcome, not an incomplete run.
- Blocked has been reassessed against the work and answers available during this run, and every remaining item has a verified unresolved blocker.

A successful review moves another agent's story to Done; review findings return it to its owner's In Progress work. Neither outcome requires taking over that owner's implementation. Never self-review merely to empty Review. Report the run as complete with the current agent's stories awaiting independent review and other agents' In Progress work identified separately; do not claim the whole board is empty.

If Ready still contains items, the current agent still owns In Progress work, or other agents still own Review work that cannot progress, stop only with an accurate waiting/incomplete report explaining the blocker. Ambiguous ownership, unavailable access, or unverified Blocked items also prevent claiming successful completion. Identify the stories and the actor, access, or answer needed to continue. Do not break ownership rules to satisfy the stopping condition.

Report completed and returned-for-correction reviews, implemented stories, stories unblocked, and remaining blockers or ownership constraints with tracker and PR links. Do not merge outside `review-pr`'s verified gates or broaden this workflow into new story creation.
