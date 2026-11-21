# CLAUDE.md

Operating rules for this project. They guide Claude Code but do not enforce anything. Tool permissions and the human owner's approval are what actually control what happens.

## What this project does

A small Python module. `slugify(title)` turns a title into a URL-friendly slug. No dependencies. Tests use `unittest`.

## Current task

Make repeated spaces or hyphens become one hyphen, and never start or end a slug with a hyphen. Full details are in `PROJECT_SPEC.md`.

## Files

- May inspect: every file in this directory.
- May change: `slugify.py`, and `test_slugify.py` (add tests only).
- Must not change: `README.md`, `PROJECT_SPEC.md`, this file, or anything outside this directory.

## Behavior to preserve

- `slugify("Hello World")` returns `hello-world`.
- `slugify("Hello, World!")` returns `hello-world`.
- `slugify("  Hello World  ")` returns `hello-world`.

## How to work

Follow INSPECT, PLAN, IMPLEMENT, VALIDATE, REVIEW, REPORT.

1. INSPECT: read the files and run the tests. Change nothing.
2. PLAN: list the files you will touch and the tests you will add. Stop and wait for approval.
3. IMPLEMENT: make only the approved change.
4. VALIDATE: run `python3 -m unittest` from this directory.
5. REVIEW: run `git status` and `git diff` and check that only the approved files changed.
6. REPORT: see below.

## Reporting

State the exact commands you ran and their real output. Say which tests failed before the change and which passed after. List every file changed. If you did not run something, say so. Do not call the work finished unless the checks ran.

## Needs human approval first

- Editing any file, until the plan is approved.
- Installing anything.
- Deleting any file.
- Any `git commit`, `git push`, or change to Git settings.

## Prohibited

- Commits or pushes of any kind, unless the owner asks in that message.
- Force pushes.
- Changing credentials or Git configuration.
- Installing dependencies without approval.
- Destructive commands without approval.
- Expanding scope beyond the files and behavior above.
- Editing, weakening, or deleting an existing test to make it pass.
- Claiming success without running the tests.
