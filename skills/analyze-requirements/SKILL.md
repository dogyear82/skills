---
name: analyze-requirements
description: 'Analyze whether a story, issue, ticket, or other piece of development work is ready to implement. Use for requests such as "is this ready for work?", "look at 935. is it ready?", "analyze 935 for readiness", or other requests to review requirements, assess story readiness, check whether work is still relevant, determine whether a work item is atomic and delivers a complete testable slice, evaluate acceptance criteria, or provide the readiness gate for another workflow such as $work-story.'
---

# Analyze Requirements

## Overview

Assess a piece of work against four readiness checks: relevance, atomicity, completeness, and acceptance criteria. Return a concise decision without planning or implementing the work.

## Ordered Workflow

1. Resolve the work item.
Read the supplied story, issue, ticket, or specification and its linked material. If only an identifier is given, retrieve it from the named or clearly implied accessible tracker. Read applicable repository instructions before evaluating it.

2. Gather current evidence.
Inspect the relevant implementation, tests, documentation, issue history, and recent changes. Gather only enough evidence to decide whether the described problem or need still exists and whether the proposed work is verifiable.

3. Check relevance.
Confirm that the work still addresses a current unmet need. Treat it as not ready when the behavior is already fixed, the requirement is obsolete, the affected feature no longer exists, or available evidence cannot establish that the issue remains relevant. Do not rely only on the tracker status.

4. Check atomicity.
Confirm that the work asks for one coherent change with one primary outcome. Changes across several files or layers can still be atomic when all are necessary for that outcome. Treat unrelated outcomes, separable behaviors, or multiple independent fixes as work that should be split.

5. Check for a complete slice.
Confirm that the work delivers observable functionality that can be tested and verified end to end. Treat scaffolding, plumbing, or a single implementation layer as incomplete when it produces no independently verifiable behavior.

6. Check acceptance criteria.
Confirm that the acceptance criteria describe clear, observable, and testable outcomes. Require enough detail to determine success, including important boundaries or failure behavior when they materially affect the result. Do not require implementation instructions.

7. Return the readiness decision.
Mark the work ready only when all four checks pass. If evidence is missing, do not silently assume the check passes.

## Output

For ready work, respond:

```text
Ready: <short confirmation grounded in the evidence.>
```

For work that is not ready, list only the failed checks:

```text
Not ready:
- <failed check>: <short reason>

Options:
- <specific way to make the work ready>
- <another option only when useful>
```

Keep the response short and specific. Useful options include closing work that is already complete, updating an obsolete requirement, splitting independent outcomes, expanding the work into a testable end-to-end slice, or adding measurable acceptance criteria.

## Operating Rules

- Remain read-only. Do not edit code, tracker items, or requirements artifacts.
- Do not create an implementation plan, design a solution, or begin implementation.
- Evaluate the work as written and against current evidence.
- Distinguish missing evidence from evidence that the work is obsolete.
- Do not confuse an atomic outcome with a single-file or single-layer change.
- Do not approve implementation-only scaffolding as a complete slice.
- Do not make vague requirements appear ready by supplying unstated assumptions.
- Suggest only solutions that address a failed readiness check.

## Completion Criteria

Complete the analysis only when:

- current relevance has been checked against available evidence
- the work has been assessed for one coherent outcome
- the work has been assessed as an observable, testable slice
- the acceptance criteria have been assessed for clarity and verifiability
- the final response clearly states `Ready` or `Not ready`
