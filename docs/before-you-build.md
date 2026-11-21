# Before You Build: Your First Claude Code Project

Last reviewed: 2026-11-20

A bonus walkthrough for readers with no programming background. You will write a one-page specification, turn it into a `CLAUDE.md` file, let Claude Code make one small change in a practice copy, and decide for yourself whether to accept it. Read [Claude Code](claude-code.md) first for the general workflow.

## What you need

- Claude Code installed and signed in. Follow Anthropic's official setup instructions.
- Python 3 and Git.
- A terminal. Every command below is copy-ready.

## The worked example

The example is a real, small defect in the sample project. `slugify("a  b")` returns `a--b`, with a doubled hyphen. The goal is a single hyphen. Two files carry the whole example:

- [PROJECT_SPEC.md](../examples/before-you-build/PROJECT_SPEC.md): the completed one-page specification.
- [CLAUDE.md](../examples/before-you-build/CLAUDE.md): the project rules derived from it.

Read both now. They are short.

## How the specification becomes CLAUDE.md

`CLAUDE.md` is a plain text file that Claude Code reads at the start of a session in that directory. It gives Claude standing instructions so you do not retype them. Here the example was written by hand from the specification, not generated.

| Specification section | Becomes in CLAUDE.md |
|---|---|
| Objective, current and desired behavior | What this project does, Current task |
| Files in scope, exclusions | Files: may inspect, may change, must not change |
| Acceptance criteria | Behavior to preserve |
| Required tests | How to work (the VALIDATE step) |
| Security restrictions, definition of done | Needs human approval first, Prohibited, Reporting |

`CLAUDE.md` is advice, not enforcement. Claude can still misread it or ignore it. Claude Code's permission prompts and your own review are the real controls. See [Security and privacy](security-and-privacy.md).

## The ten steps

### Steps 1 and 2: describe it, then write the specification

Say in one or two sentences what you want, then fill in the one-page specification. Writing it forces you to decide what "done" means before any code changes. If you cannot state the acceptance criteria, Claude cannot be checked against them. The completed example is linked above.

### Step 3: turn it into CLAUDE.md

Use the table above. Keep it short and concrete. List what may change, what may not, and what needs your approval.

### Step 4: make a practice project and start Claude Code

Work in a temporary folder, never in this guide's repository. These commands copy the sample project and the two example files, then record the starting point so you can see changes later.

```sh
mkdir -p ~/claude-practice && cd ~/claude-practice
cp /path/to/claude-101-field-guide/examples/sample-repo/{slugify.py,test_slugify.py,README.md,.gitignore} .
cp /path/to/claude-101-field-guide/examples/before-you-build/{PROJECT_SPEC.md,CLAUDE.md} .
git init
git add .
git commit -m "Starting point"
python3 -m unittest
claude
```

Replace `/path/to/` with where you cloned this guide. The copied `.gitignore` keeps Python cache files out of Git status. The `git commit` here is only in your private practice folder. It gives you a baseline to compare against. The tests should show 3 passing.

### Step 5: ask for a plan, with no edits

```text
Read PROJECT_SPEC.md and CLAUDE.md. Inspect the project and run the tests.
Do not edit any file. Propose a plan: which files you will change and which
tests you will add. Wait for my approval.
```

Planning makes no file changes and shows whether Claude understood the brief. It still uses the model, so it may count toward your usage limits or incur charges, depending on your plan.

### Step 6: review and approve

Check the plan against the specification. The files must match the "Files in scope" list. If the plan mentions a new dependency, a new file, or any other file, reply with a correction instead of approving. Approve in plain words, for example: "Approved. Add the three tests first and confirm they fail, then make the change."

### Step 7: let Claude implement

Claude will edit the two files and run the tests. If it asks to run a command you do not understand, deny it and ask what it does.

### Step 8: inspect what changed

In a second terminal, in the practice folder:

```sh
git status
git diff
```

`git status` lists changed and new files. `git diff` shows every changed line.

### Step 9: run the tests yourself

Do not rely on Claude's report alone.

```sh
python3 -m unittest
```

Expect `OK` and 6 tests. If you ask Claude to show that the new tests fail on the old code, expect 3 failures, then none after the fix.

### Step 10: accept, revise, or reject

- **Accept** if the diff matches the specification and the tests pass. Committing is your decision, made by you, after reading the diff.
- **Revise** if it is close. Say exactly what to fix.
- **Reject** if it touched things outside scope. Run `git restore .` to return tracked files to the starting point. Delete any new untracked files by hand after looking at them.

## How to read a diff

Lines starting with `+` were added. Lines starting with `-` were removed. Lines without either are context. In the example, the acceptable change to `slugify.py` is one line replaced by one line:

```diff
-    return cleaned.strip().replace(" ", "-")
+    return re.sub(r"[ -]+", "-", cleaned).strip("-")
```

In `test_slugify.py`, the acceptable change is only added lines: three new test methods and no removed lines. Your diff may differ in wording but not in shape.

Now look for what should not be there:

| What you see | Verdict | Why |
|---|---|---|
| Only the two listed files changed | Acceptable | Matches the specification |
| A line such as `-    def test_basic(self):` | Unacceptable | A test was deleted |
| `-self.assertEqual(slugify("a  b"), "a--b")` replacing a correct check | Unacceptable | The assertion was changed to match the defect |
| A new `requirements.txt` or an `import` of a package you did not approve | Unacceptable | Unapproved dependency |
| A string that looks like `API_KEY = "..."` or a token | Unacceptable | A secret in a file |
| `README.md` or `CLAUDE.md` changed | Unacceptable | Outside the approved file list |
| A new file you did not expect | Investigate | Usually out of scope |

Files such as `__pycache__` are generated when Python runs. They are harmless, but they should not appear in a commit.

## Human review checklist

- [ ] `git status` lists only the approved files.
- [ ] No removed or weakened tests. Old tests are unchanged.
- [ ] New tests check real behavior from the specification.
- [ ] No new dependencies, imports you cannot explain, or network calls.
- [ ] No secrets, keys, or personal data anywhere in the diff.
- [ ] I ran the tests myself and saw the result.
- [ ] I can explain every changed line in my own words.

## Limits

- Passing tests is necessary, not sufficient. Tests only check what they were written to check. A wrong test passes a wrong change. Read the diff as well.
- This example uses a tiny function. Larger changes need smaller steps and more review, not less.
- Do not paste real credentials or private data into a practice project.

## Practice

[Exercise 6: Safe coding workflow](../exercises/06-safe-coding-workflow.md) covers the same inspect, plan, implement, validate cycle on the sample repository.

## Official reference

- Claude Code overview: <https://code.claude.com/docs/en/overview>
- Memory and CLAUDE.md files: <https://code.claude.com/docs/en/memory>
