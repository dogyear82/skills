---
name: find-duplicate-files
description: Find duplicate files in a folder by comparing file contents. Use this when the user wants to scan a directory and list duplicate files, but not delete or modify anything.
---

# Find Duplicate Files

Use this skill when the user asks to find duplicate files in a directory.

## What this skill does
- Recursively scans a target folder
- Compares files by content, not just filename
- Lists duplicate groups clearly
- Reports skipped unreadable files
- Never deletes, moves, or renames files

## Rules
- Do not modify files
- Prefer content-based hashing over filename matching
- Ignore unreadable files, but mention them
- If no folder is specified, ask for one or use the folder the user explicitly names
- Return results grouped by identical content

## Workflow
1. Determine the target folder.
2. Run the helper script in `scripts/find_duplicates.py`.
3. Parse the results.
4. Show duplicate groups with file paths, size, and hash.
5. If there are no duplicates, say so plainly.