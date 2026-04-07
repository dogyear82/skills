# Story Decomposition

Use this reference to turn a request into a clean set of stories.

Apply it after the ordered workflow has already normalized the request and inspected enough repository context to make decomposition decisions.

## Goal

Break the request into the smallest set of independently valuable, implementable stories.

Each story should be:

- meaningful on its own
- reviewable on its own
- small enough to execute without excessive hidden scope
- explicit about dependencies when it cannot stand alone

## Decomposition Rules

- Start from user-visible outcomes and work backward into implementation slices.
- Group tightly coupled work into one story when splitting would create fake independence.
- Split work when sequencing, ownership, or reviewability clearly improve.
- Avoid stories that are just internal notes with no actionable acceptance criteria.
- Prefer vertical slices over horizontal layers when possible.

## What to Capture Per Story

- summary
- problem or goal
- scope boundaries
- acceptance criteria
- dependencies or ordering notes
- notable risks or open questions

## When to Use More Analysis

Add `researcher` when:
- relevant code paths are unclear
- the impact surface is wide
- hidden dependencies are likely

Add `architect` when:
- interface or boundary decisions will shape the story split
- migration order matters
- the request crosses multiple subsystems

Add `debugger` when:
- the request originates from a production issue or regression
- root cause affects how the work should be split

## Product Owner Synthesis

The product owner should turn raw analysis into stories that are:

- written from an outcome perspective
- concrete enough to execute
- narrow enough to estimate and review
- clear about non-goals when scope could expand
