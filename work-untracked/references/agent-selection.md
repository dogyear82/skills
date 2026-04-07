# Agent Selection

Use this reference to decide which agents to add within each stage of the ordered workflow for an untracked development request.

## Selection Rules

- Prefer repo-local agents over global agents when both define the same role.
- Do not spawn every available agent by default.
- Select agents based on ambiguity, technical risk, and verification needs at the current stage.
- Keep planning, implementation, testing, debugging, and review concerns distinct when that separation improves quality.

## Stage Mapping

- Normalization stage: consider `product_owner`
- Repository inspection stage: consider `researcher`
- Breakdown and design-risk stage: consider `architect` or `debugger`
- Implementation stage: use `implementer`
- Validation stage: consider `tester`
- Review stage: use `reviewer`

## Role Triggers

### product_owner

Use when the request is ambiguous, missing acceptance criteria, or likely too broad.

Expected output:
- clarified goal
- scope boundaries
- acceptance criteria
- risks and dependencies

### researcher

Use when the codebase area is unfamiliar or the impact surface is unclear.

Expected output:
- relevant files and flows
- constraints and dependencies
- likely implementation surface

### architect

Use when the request crosses module boundaries, changes interfaces, or introduces non-trivial design tradeoffs.

Expected output:
- recommended design approach
- tradeoffs
- migration or sequencing guidance

### implementer

Use for bounded code changes once the task is clear enough to execute.

Expected output:
- working code
- focused diffs
- relevant verification

### debugger

Use when expected behavior is failing, the request exposes a regression, or the root cause is not obvious.

Expected output:
- reproduced issue or narrowed failure surface
- root cause
- minimal fix path

### tester

Use when behavior needs stronger verification, regression coverage, or clearer boundary-case coverage.

Expected output:
- tests added or improved
- gaps in confidence
- verification evidence

### reviewer

Use after implementation and testing for an independent quality pass.

Expected output:
- prioritized findings or explicit no-findings result
- residual risks

## Default Compositions

### Small request or bug fix

- implementer
- tester
- reviewer

Add `debugger` if reproduction or root cause is unclear.

### Ambiguous feature request

- product_owner
- researcher
- implementer
- tester
- reviewer

Add `architect` if the change crosses boundaries or needs interface decisions.

### Cross-cutting change

- researcher
- architect
- implementer
- tester
- reviewer

Add `product_owner` when scope needs to be reduced to a workable increment.

## Exit Rule

Do not treat the work as complete until reviewer feedback is resolved and the implemented behavior matches the normalized acceptance criteria closely enough to stand as finished work without further clarification.
