# Intake Normalization

Use this reference to turn an ad hoc user request into a story-like execution brief before any implementation starts.

## Normalization Goal

Produce a concise brief that captures:

- the problem to solve
- the requested behavior
- acceptance criteria
- constraints
- dependencies
- risks and unknowns

If the request is vague, normalize it into the smallest workable increment instead of coding against an unclear prompt.

## Inputs

Sources for the brief may include:

- the current user message
- earlier chat context
- repository structure and existing implementation
- local documentation or code comments

## Required Output Shape

Before execution, establish:

- what should change
- what should not change
- how success will be judged
- what evidence will be needed to call the work complete

## Ambiguity Handling

If the request is ambiguous:

- infer conservatively from repository patterns
- call out assumptions explicitly
- use the product-owner role when acceptance criteria or scope need sharpening

## Scope Control

- Prefer bounded, testable increments.
- Avoid broad refactors unless they are necessary to satisfy the request.
- Distinguish between required behavior and nice-to-have cleanup.

## Handoff Into Execution

Once normalized, the brief should be strong enough for:

- a researcher to trace impact
- an implementer to make bounded changes
- a tester to verify behavior
- a reviewer to assess correctness and risk
