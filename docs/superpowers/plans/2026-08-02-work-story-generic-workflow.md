# Work Story Generic Workflow Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite `work-story` as a portable end-to-end workflow with inline readiness checks and no named skill dependencies.

**Architecture:** Keep one self-contained `SKILL.md` that defines required outcomes and phase gates. Let each runtime select applicable skills dynamically while preserving deterministic readiness, isolation, planning, goal, verification, and PR requirements.

**Tech Stack:** Markdown skill instructions, YAML frontmatter, `agents/openai.yaml`, skill validation script, Git.

## Global Constraints

- Preserve the existing invocation examples.
- Keep relevance, atomicity, complete-slice, and acceptance-criteria checks inline.
- Do not name or require `analyze-requirements`, `plan-implementation`, or Superpowers skills.
- End with a non-draft PR ready for review; do not merge it.

---

### Task 1: Establish the baseline failure

**Files:**
- Inspect: `skills/work-story/SKILL.md`

**Interfaces:**
- Consumes: current installed skills and the existing `work-story` workflow.
- Produces: recorded evidence that hard-coded missing dependencies are unreliable.

- [ ] **Step 1: Run the unready-story scenario against the current skill**

Use this prompt with a fresh agent and prohibit repository changes:

```text
Start this story: Modernize duplicate-file handling. Add a database table for future scan jobs, change command output to JSON, and add duplicate deletion. Acceptance criteria: duplicate handling works correctly.
```

- [ ] **Step 2: Record the baseline result**

Record whether the agent stops because named skills are unavailable, silently ignores the mandatory dependency rule, or produces another inconsistent result. The baseline already observed that the agent ignored the mandatory missing-skill rule while still returning a readiness decision.

### Task 2: Rewrite the generic workflow

**Files:**
- Modify: `skills/work-story/SKILL.md`
- Inspect: `skills/work-story/agents/openai.yaml`

**Interfaces:**
- Consumes: a tracked story, repository instructions, available runtime skills, tracker access, Git, and a PR-capable hosting workflow.
- Produces: either a concise not-ready decision or a verified implementation on an isolated branch with a ready-for-review PR.

- [ ] **Step 1: Replace the frontmatter description**

Use a trigger-only description:

```yaml
---
name: work-story
description: 'Use when asked to "start story #123", "begin work on XYZ", "start on the next story on the board", or otherwise start, implement, complete, or pick up a tracked story or issue end to end.'
---
```

- [ ] **Step 2: Replace named dependencies with outcome-based phases**

Write one concise ordered workflow that requires:

```text
resolve story and repository guidance
invoke applicable available skills
check relevance, atomicity, complete slice, and acceptance criteria
stop concisely when not ready
create worktree from latest remote default branch
investigate and write an implementation plan
establish one explicit goal
implement the smallest coherent change
verify acceptance criteria and review the diff
rebase, rerun checks, push, and open a non-draft PR
complete the goal only when the PR is ready
```

- [ ] **Step 3: Preserve portable skill selection**

State the contract positively:

```text
Before each phase, inspect the skills available in the current runtime and invoke those whose triggers match the work. The workflow depends on completed outcomes, not particular skill names.
```

- [ ] **Step 4: Verify UI metadata remains accurate**

Confirm `skills/work-story/agents/openai.yaml` still describes the rewritten skill. Regenerate it only if its display name, short description, or default prompt is stale.

### Task 3: Validate, test, and publish

**Files:**
- Test: `skills/work-story/SKILL.md`
- Test: `skills/work-story/agents/openai.yaml`
- Include: `docs/superpowers/specs/2026-08-02-work-story-generic-workflow-design.md`
- Include: `docs/superpowers/plans/2026-08-02-work-story-generic-workflow.md`

**Interfaces:**
- Consumes: rewritten skill and validation tooling.
- Produces: validated branch and ready-for-review PR.

- [ ] **Step 1: Run structural validation**

```bash
python3 /home/tan/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/work-story
git diff --check
```

Expected: both commands exit successfully.

- [ ] **Step 2: Check for stale named dependencies**

```bash
rg -n 'analyze-requirements|plan-implementation|superpowers:' skills/work-story
```

Expected: no matches.

- [ ] **Step 3: Forward-test an unready story**

Run the Task 1 scenario with the rewritten skill. Expected: concise readiness failures and options, with no branch, worktree, plan, goal, or code changes.

- [ ] **Step 4: Forward-test a ready story in a disposable repository**

Use a temporary local Git repository with a small existing implementation and a complete story. Expected: the agent reaches investigation and planning using applicable available skills without referring to removed or named skills. Stop the scenario before external publication and remove the disposable repository afterward.

- [ ] **Step 5: Review and synchronize**

```bash
git fetch origin main
git rebase origin/main
git diff --check origin/main...HEAD
git status --short
```

Expected: branch is current, diff checks pass, and only intended files are present.

- [ ] **Step 6: Commit and publish**

```bash
git add skills/work-story/SKILL.md skills/work-story/agents/openai.yaml docs/superpowers/specs/2026-08-02-work-story-generic-workflow-design.md docs/superpowers/plans/2026-08-02-work-story-generic-workflow.md
git commit -m "Rewrite work story workflow"
git push -u origin agent/rewrite-work-story-skill
```

Open a non-draft PR targeting `main` with the design, behavior change, and validation results.
