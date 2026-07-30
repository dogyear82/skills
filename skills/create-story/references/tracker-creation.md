# Tracker Creation

Use this reference when creating stories in Jira or another accessible tracker.

## Source Priority

1. If the user names a tracker explicitly, use that tracker if Codex has access.
2. If Jira is connected and the user does not name another tracker, use Jira.
3. If no accessible tracker is available, stop after producing tracker-ready stories and report the limitation clearly.

## Jira Creation Rules

When Jira is available:

- Create issues in the named project if the user provided one.
- If the project is not specified, use the accessible project the user indicates or stop and ask for the target project only if it cannot be inferred safely.
- Use `Story` as the default issue type unless the request clearly calls for another type.
- Keep summaries short and descriptions actionable.
- Put acceptance criteria directly in the description when no dedicated field is available.

## Multi-Story Requests

When the request breaks into multiple stories:

- create them in dependency order when possible
- preserve naming consistency across the set
- note blocking relationships in the description when explicit linking is not available

## If Creation Fails

- return the full set of drafted stories
- explain which tracker action failed
- include enough detail that the user can create the stories manually if needed
