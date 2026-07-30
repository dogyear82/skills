---
name: plan-implementation
description: Create evidence-based, execution-ready implementation plans for stories, issues, features, bugs, and other development work. Use when Codex is asked to write or create an implementation plan, detail how a work item will be completed, plan a named tracker issue such as issue 955, identify affected code and tests before implementation, or explain the intended technical approach without making the changes.
---

# Plan Implementation

## Overview

Turn a work item into a code-informed plan that another developer can execute. Inspect the source material, repository, documentation, implementation, and tests before proposing changes; planning is not implementation.

## Ordered Workflow

1. Resolve the work item.
Read the story, issue, specification, or request supplied by the user. If only an identifier is given, retrieve it from the named or clearly implied accessible tracker. Extract the objective, required behavior, acceptance criteria, constraints, dependencies, and linked material. Do not change the tracker.

2. Read repository guidance.
Inspect the applicable `AGENTS.md` files, repository documentation, build and test configuration, and conventions governing the affected area. Follow the most specific instructions.

3. Investigate the current behavior.
Trace the relevant entry points, control flow, data flow, interfaces, persistence, configuration, and tests. Search for existing utilities and patterns that can be reused. For a defect, gather enough evidence to identify the likely failure point and plan the correction.

4. Determine the smallest coherent change.
Compare the requested behavior with the current implementation. Identify affected layers, contracts, compatibility concerns, migrations, rollout needs, and test coverage. Prefer the repository's established patterns and avoid unrelated cleanup.

5. Resolve material uncertainty.
Separate confirmed facts from assumptions and open questions. Ask the user only when an unanswered question would substantially change scope, architecture, public behavior, data handling, or the plan itself. Otherwise state the assumption and its effect.

6. Write the implementation plan.
Use the compact structure in [references/implementation-plan-template.md](references/implementation-plan-template.md) by default: Goal, Changes, Tests, and, when relevant, Rollout, Risks, Assumptions, and Open Questions. Include exact paths and symbols when verified. Expand the format only when complexity or uncertainty makes the extra detail useful.

7. Check the plan.
Confirm that every acceptance criterion maps to a proposed change and verification. Ensure the sequence respects dependencies, names relevant tests, identifies meaningful risks, and contains enough evidence for another developer to begin without repeating the investigation.

## Investigation Depth

Match investigation to the work:

- For a focused change, inspect the target implementation, its callers, and nearby tests.
- For a cross-layer change, trace the behavior through every affected layer and contract.
- For a defect, distinguish the observed symptom from the supported root-cause hypothesis.
- For a migration or externally visible change, include compatibility, rollout, and rollback considerations.

Stop when further inspection would not materially improve the plan. Do not turn planning into speculative redesign.

## Operating Rules

- Remain read-only unless the user separately asks for implementation or another mutation.
- Do not edit code, create branches, commit, push, open pull requests, or update tracker items.
- Do not invent files, symbols, APIs, database objects, commands, or tests. Label proposed new names as proposals.
- Cite repository paths, symbols, work-item fields, or documentation that support important conclusions.
- Distinguish confirmed behavior, inferred behavior, assumptions, and open questions.
- Reuse existing utilities, components, and project patterns where they fit.
- Keep changes outcome-focused and ordered; avoid both vague phases and line-by-line coding instructions.
- Prefer a short, specific plan over a long document when both are equally actionable.
- Include only template sections relevant to the work. Omit empty boilerplate.
- Do not claim that acceptance criteria or tests pass; describe how they will be verified.

## Completion Criteria

Treat the plan as complete only when:

- The objective, scope, and relevant current behavior are clear.
- The affected areas and dependencies are supported by repository evidence.
- The ordered steps cover the smallest coherent end-to-end change.
- Automated and manual verification are specific to the behavior.
- Every acceptance criterion is covered by a proposed change and verification method.
- Risks, assumptions, and unresolved questions are explicit when present.
- No implementation or external state change was performed.

## Reference

- Plan structure and section guidance: [references/implementation-plan-template.md](references/implementation-plan-template.md)
