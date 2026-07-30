# Requirements Output

Use this reference when the product idea is mature enough to document for handoff.

## Goal

Produce a requirements artifact that is strong enough for architectural review and later work-item creation.
Write the artifact to disk as Markdown so it can be reviewed outside the chat session.

## Default File Path

Unless the repository has a stronger local convention, write the artifact to:

- `requirements/<slug>.md`

Use a short, stable slug derived from the product or feature name.

## Required Sections

### Problem Statement

Describe:

- what problem exists
- who experiences it
- why it matters

### User Personas

Identify the relevant users and their goals.
Use lightweight personas when detailed personas are unnecessary.

### Core Use Cases

Describe the main workflows the product must support.
These should be concrete enough to guide architecture and later story breakdown.

### Functional Requirements

List required behaviors in concrete, testable language.
Avoid vague wording such as "easy," "fast," or "user-friendly" unless it is defined.

### Non-Functional Requirements

Capture expectations around:

- performance
- security
- reliability
- usability
- compliance
- scalability
- maintainability

Only include what is actually relevant to the request.

### Constraints

List fixed boundaries such as:

- technology restrictions
- timeline limits
- budget limits
- platform requirements
- integration requirements

### Open Questions

List unresolved decisions that still matter for architecture or delivery.

## Quality Bar

The output is ready only if:

- an architect could review it without first re-interviewing the user from scratch
- major ambiguities are either resolved or explicitly listed as open questions
- the artifact distinguishes confirmed facts from assumptions where needed
- the artifact exists on disk as a Markdown file for later review
