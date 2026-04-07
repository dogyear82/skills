---
name: create-story
description: Turn a user request into one or more tracked stories using an ordered planning workflow with conditional multi-agent support. Use when Codex needs to analyze requested work, gather only the necessary planning input at each stage, include a product owner, break the work into implementable stories, and create those stories in Jira or another accessible work tracker.
---

# Create Story

## Overview

Use this skill to convert a user request into actionable tracked work.
The workflow is fixed and predictable: normalize, inspect, analyze, decompose, synthesize, and create. Agents are used only where they improve planning quality.

## Ordered Workflow

1. Normalize the request.
Turn the user request into a concise planning brief: problem, desired outcome, constraints, dependencies, and any obvious unknowns. Always include a `product_owner` in this workflow so the final output is expressed as tracker-ready stories.

2. Build enough context to plan.
Inspect the repository, local [AGENTS.md], and any directly relevant code or documentation needed to understand the request well enough to break it down. Use a `researcher` when the implementation surface or dependencies are not obvious.

3. Analyze design and dependency risk.
Use an `architect` only when subsystem boundaries, migration order, or interface decisions affect how the stories should be split. Use a `debugger` only when the request is driven by a failure or regression and the root cause affects decomposition.

4. Decompose the work.
Break the request into the smallest sensible set of stories: distinct outcomes, dependencies, sequencing, risks, and acceptance criteria inputs. See [references/story-decomposition.md](references/story-decomposition.md).

5. Product-owner synthesis.
Use the product owner to convert the analysis into tracker-ready stories with:
- clear summary
- concise description
- acceptance criteria
- dependencies or ordering notes
- scope boundaries

6. Create the stories.
Create the resulting stories in Jira or another accessible tracker using the rules in [references/tracker-creation.md](references/tracker-creation.md).

## Conditional Agent Use

Use agents only at the stage where they add value:

- `product_owner` during normalization and final synthesis
- `researcher` during repository inspection when context is unclear
- `architect` during design-risk analysis when boundaries affect the story split
- `debugger` during analysis when failure or regression context affects decomposition

Do not use implementer, tester, or reviewer agents for this skill unless the request has drifted into execution rather than story creation.

## Operating Rules

- Always include a product owner in the planning workflow.
- Spawn only the minimum additional analysis agents needed at the current stage.
- Prefer fewer, sharper stories over a noisy backlog of tiny tickets.
- Break work into stories that can be implemented and reviewed independently.
- Keep implementation detail out of the stories unless it materially affects scope, feasibility, or acceptance criteria.
- If a tracker is inaccessible, produce tracker-ready stories and report that creation could not be completed.

## Completion Criteria

Treat the workflow as complete only when all of the following are true:

- The request has been decomposed into the smallest sensible set of implementable stories.
- Each story has a clear summary, description, and acceptance criteria.
- Dependencies or sequencing constraints are explicit where needed.
- The stories have been created in an accessible tracker, or the inability to create them has been stated clearly.

## References

- Story breakdown and decomposition rules: [references/story-decomposition.md](references/story-decomposition.md)
- Tracker selection and story creation rules: [references/tracker-creation.md](references/tracker-creation.md)
