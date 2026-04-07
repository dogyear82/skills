#!/usr/bin/env python3
"""Recursively find duplicate files by content."""

from __future__ import annotations

import argparse
import hashlib
import os
import sys
from collections import defaultdict


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Find duplicate files in a folder by comparing file contents."
    )
    parser.add_argument(
        "folder",
        nargs="?",
        default=".",
        help="Target folder to scan recursively. Defaults to the current directory.",
    )
    return parser.parse_args()


def sha256_file(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    args = parse_args()
    root = os.path.abspath(args.folder)

    if not os.path.exists(root):
        print(f"error: path does not exist: {root}", file=sys.stderr)
        return 1
    if not os.path.isdir(root):
        print(f"error: path is not a directory: {root}", file=sys.stderr)
        return 1

    files_by_size: dict[int, list[str]] = defaultdict(list)
    skipped: list[tuple[str, str]] = []

    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            if not os.access(path, os.R_OK):
                skipped.append((path, "unreadable"))
                continue
            try:
                files_by_size[os.path.getsize(path)].append(path)
            except OSError as exc:
                skipped.append((path, str(exc)))

    duplicate_groups: list[tuple[int, str, list[str]]] = []

    for size in sorted(files_by_size):
        candidates = files_by_size[size]
        if len(candidates) < 2:
            continue

        files_by_hash: dict[str, list[str]] = defaultdict(list)
        for path in candidates:
            try:
                files_by_hash[sha256_file(path)].append(path)
            except OSError as exc:
                skipped.append((path, str(exc)))

        for digest, paths in sorted(files_by_hash.items()):
            if len(paths) > 1:
                duplicate_groups.append((size, digest, sorted(paths)))

    print(f"Scanned: {root}")
    print(f"Duplicate groups: {len(duplicate_groups)}")
    print(f"Skipped files: {len(skipped)}")

    if duplicate_groups:
        print("")
        for index, (size, digest, paths) in enumerate(duplicate_groups, start=1):
            print(f"Group {index}")
            print(f"Size: {size} bytes")
            print(f"SHA-256: {digest}")
            for path in paths:
                print(path)
            print("")
    else:
        print("")
        print("No duplicate files found.")

    if skipped:
        print("")
        print("Skipped:")
        for path, reason in skipped:
            print(f"{path}: {reason}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
