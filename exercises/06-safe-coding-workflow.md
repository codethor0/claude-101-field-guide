# Exercise 6: Safe coding workflow

Last reviewed: 2026-11-20

## Objective

Use inspect, plan, implement, validate, review, report on a small repository, with approval before any edit.

## Prerequisites

Python 3 and a coding assistant such as Claude Code. Read [Claude Code](../docs/claude-code.md). The sample is [`examples/sample-repo`](../examples/sample-repo/README.md). Copy it out of this repository so you work in your own repo:

```sh
PRACTICE=$(mktemp -d)
cp -R examples/sample-repo/. "$PRACTICE"
cd "$PRACTICE"
find . -name __pycache__ -prune -exec rm -rf {} +
git init -q -b main && git add . && git commit -q -m "Initial sample"
python3 -m unittest
```

Expected: 3 tests pass.

## Input data

The repository's `slugify` function. Known gap: `slugify("a  b")` returns `a--b`. Desired: `a-b`.

## Copy-ready prompt (stage 1)

```text
Inspect this repository: layout, how tests run, git status. Change nothing.
Then propose a plan to make slugify collapse repeated spaces and hyphens
into a single hyphen. List the files you will touch, the new tests you will
add, and how you will validate. Stop and wait for my approval.
```

## Steps

1. Run stage 1. Read the plan. Check it against the repository yourself.
2. Approve with limits: "Edit only slugify.py, test_slugify.py, and the known-gap line in README.md. Do not commit."
3. Let it implement. Read the diff (`git diff`).
4. Run `python3 -m unittest` yourself.
5. Ask for a review: "List any behavior you did not test, and any existing test you changed."
6. Ask for a short report: what changed, what was run, what was not verified.
7. Commit only when satisfied.

## Expected result characteristics

- The plan names `slugify.py`, `test_slugify.py`, and the README note about the known gap, and nothing else.
- New tests cover `"a  b"`, `"a - b"`, and `"a---b"`.
- Existing tests are unchanged.
- The report separates what was run from what was assumed.

## Verification checklist

- [ ] No file outside the stated scope changed (`git status`).
- [ ] Existing assertions are unchanged (`git diff test_slugify.py`).
- [ ] All tests pass when you run them yourself.
- [ ] You can name one case the tests do not cover (for example, an empty string, or non-ASCII letters).
- [ ] The commit author is your own identity.

## Common failure modes

- The assistant edits a test to make it pass.
- It reports "tests pass" without running them.
- It changes more than asked (reformatting, new dependencies).
- It commits before you approved.

## Follow-up

Ask for a test for `slugify("")` and `slugify("Café")`. Decide what the correct behavior is before asking for the implementation.
