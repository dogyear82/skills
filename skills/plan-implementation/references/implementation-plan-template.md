# Implementation Plan Template

Use this compact format by default:

```markdown
Goal: <One sentence describing the observable outcome.>

Changes:

- `path/to/file` — <Specific behavior or responsibility to add or change.>
- `path/to/other-file` — <Specific behavior or responsibility to add or change.>

Tests:

- <Automated test covering the main behavior and important boundaries.>
- <Integration, end-to-end, or manual verification when relevant.>

Rollout:

- <Feature flag, migration order, staged release, monitoring, or rollback plan.>

Risks:

- <Concrete risk> — <Mitigation or observation plan.>

Assumptions:

- <Material working assumption and how it affects the plan.>

Open Questions:

- <Decision needed before implementation and how the answer changes the plan.>
```

## Adapt the Template

- Always include `Goal`, `Changes`, and `Tests`.
- Include `Rollout` for migrations, flags, compatibility changes, operational risk, or staged releases.
- Include `Risks` only for meaningful failure modes, regressions, or tradeoffs. Pair each risk with a mitigation.
- Include `Assumptions` or `Open Questions` only when they affect scope, design, or safe execution.
- Add a short `Current State` section for defects, unfamiliar flows, or decisions that need repository evidence.
- Add `Non-goals` when the work could easily expand beyond the requested outcome.
- Add an acceptance-criteria mapping table only when several criteria make coverage hard to see in the compact plan.

## Write the Changes Section

For each affected area:

- Name a verified repository path and relevant symbol or component when useful.
- Describe the resulting behavior rather than a low-level edit.
- Label an unverified path or newly introduced name as proposed.
- State sequencing or dependencies when order matters.
- Mention reused utilities, components, and patterns where they affect the approach.

For cross-layer work, list every affected layer needed to deliver the behavior end to end. Do not add speculative areas merely to make the plan look complete.

## Write the Tests Section

Cover the observable behavior and important boundaries at the appropriate levels:

- unit tests for isolated rules and edge cases
- integration or contract tests across boundaries
- end-to-end tests for critical user flows
- manual checks that cannot reasonably be automated
- relevant lint, type-check, build, or targeted test commands when verified

Describe expected results. Do not merely list test filenames or say “add tests.”

## Expand for Complex Work

When the compact format is not enough, add only the sections needed from this list:

- `Current State`: verified flow, data transitions, coverage gaps, or supported root-cause hypothesis
- `Proposed Approach`: architectural strategy and why it fits existing patterns
- `Data and Interfaces`: migrations, backfills, APIs, events, configuration, and compatibility
- `Dependencies`: external work or ordering constraints
- `Acceptance Criteria Coverage`: criterion-to-change-to-verification mapping

The final plan should remain the shortest document that another developer can execute confidently.
