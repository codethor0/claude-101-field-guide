# Claude Code

Last reviewed: 2026-11-20

## What it is

Claude Code is Anthropic's agentic coding tool. Per its overview documentation, it reads a codebase, edits files, runs commands, and integrates with development tools. It runs in a terminal, and the documentation also lists IDE extensions, a desktop app, and a web version. Install instructions change; use the official page.

Typical uses: navigating an unfamiliar repository, implementing a change, running tests, debugging a failure, and preparing commits.

## A workflow that keeps you in control

```text
INSPECT → PLAN → IMPLEMENT → VALIDATE → REVIEW → REPORT
```

| Stage | What happens | Your check |
|---|---|---|
| Inspect | Read the repository, git status, existing conventions, and how tests run, before any change | Does the summary match what you know? |
| Plan | State the change, files affected, and how success will be checked | Is the scope what you intended? |
| Implement | Make the smallest change that meets the plan | Does the diff match the plan? |
| Validate | Run tests, linters, and the program itself | Did the commands actually run, and what did they print? |
| Review | Read the diff as a reviewer would; look for unintended changes | Anything outside the plan? |
| Report | Summarize what changed, what was verified, and what was not | Does the report separate evidence from assumption? |

Ask for this structure in your prompt or project instructions. It makes the work inspectable.

## Approval boundaries

Claude Code asks permission before actions such as running commands or editing files, depending on your settings. Decide in advance what needs your explicit approval:

- Always: deleting data, force-pushing, rewriting history, changing credentials, publishing a package or repository, spending money.
- Usually: installing dependencies, changing CI or deployment configuration.
- Rarely: reading files and running tests.

Permission to commit is not permission to push, and permission to push to a branch is not permission to change visibility or release. Grant approval per action and per scope. See the permissions and security pages for the current settings.

## Why passing tests does not prove correctness

Tests check what they were written to check. A change can pass every test and still be wrong if:

- The tests do not cover the case that matters.
- The test was edited to match the new behavior.
- The test passes for the wrong reason (it asserts nothing meaningful).
- The failure is in an area outside the tests (security, performance, concurrency).

Review the diff of the tests as carefully as the diff of the code. Be suspicious of a fix that changes an assertion.

## Example prompt

```text
Inspect this repository first: layout, how to run tests, git status. Do not
change anything yet. Then propose a plan to make `slugify` handle repeated
hyphens, listing the files you will touch and the test you will add. Wait
for my approval before editing.
```

[Exercise 6](../exercises/06-safe-coding-workflow.md) practices this on a small sample repository.

## Repository secret hygiene

- Keep secrets out of the working tree. Use environment variables or a secret manager.
- Add `.env` and key files to `.gitignore` before the first commit. Ignoring a file does not remove it from history if it was already committed.
- Before making a repository public, scan the whole history, not just the latest files.
- Do not paste secrets into prompts.

## Verify the result

Run the checks yourself, in a clean environment where possible. Read the diff. Confirm commits have the author you expect.

## Limitations

Claude Code can misread a codebase, make plausible but wrong edits, and report success when a command failed. Read command output rather than relying on a summary.

## Official reference

- Overview: <https://code.claude.com/docs/en/overview>
- Security: <https://code.claude.com/docs/en/security>
