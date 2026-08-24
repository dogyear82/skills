---
name: brief-next-story
description: Use when reviewing, browsing, briefing, selecting, or finding the next workable story from a repository tracker queue.
---

# Brief Next Story

## Select

1. Resolve the repository tracker and requested source queue from repository instructions, remotes, documentation, or available integrations. Default to `Todo`.
2. Read the queue in its tracker priority order. Preserve its position for this conversation.
3. Apply the repository Definition of Ready. If none exists, require exactly:
   - clear acceptance criteria
   - the smallest end-to-end change that delivers observable, verifiable behavior across every affected layer
   - a change that can be manually tested and verified
   - all assumptions clarified
   - no remaining clarifying question needed to understand the work
4. Add no other readiness checks. Assess tracker, linked, and repository evidence faithfully; do not treat documented assumptions or verification as absent. Skip unready stories and choose the first workable story.

## Brief

Present exactly one story, in ordinary language and without implementation detail:

```text
KEY-123 — Short title

Ask: <plain-language summary>
Current: <what happens now>
Desired: <what should happen instead>
```

Include the tracker link when available. Derive the brief from story, linked material, and relevant repository evidence.

## Conversation

Keep the presented story active during follow-up questions. Answer from evidence and label assumptions as assumptions. Do not implement while clarifying. If clarification shows it is unready, state why briefly and wait; search again only when asked for the next story.

On `next`, resume the same queue position, never repeat a considered story in this conversation, and present the next workable story. A new conversation starts a new search.

Only explicit acceptance, such as `work on this`, selects the active story. Then begin the available repository implementation workflow. Before that, do not create a branch, plan, goal, code change, or tracker mutation. End this skill when that workflow accepts the selected story.

## Boundaries

Selection and clarification are read-only: do not change tracker status, assignment, priority, labels, or other data. If the tracker or source queue cannot be resolved safely, ask one concise question. State plainly if access is unavailable or no workable stories remain.
