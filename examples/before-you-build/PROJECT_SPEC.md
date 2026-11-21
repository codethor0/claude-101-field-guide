# Project specification: tidy slugs

A completed one-page brief for a small change to the sample project. It uses the `slugify` function from [examples/sample-repo](../sample-repo/).

## Objective

Make `slugify` produce a single hyphen where the title has several spaces or hyphens in a row.

## Intended user

Someone who builds web page addresses from article titles and wants clean results such as `hello-world`, not `hello--world`.

## Current behavior

Repeated spaces or hyphens in the title produce repeated hyphens.

- `slugify("a  b")` returns `a--b` (two spaces)
- `slugify("a--b")` returns `a--b` (two hyphens)

## Desired behavior

Any run of spaces and hyphens becomes one hyphen. A slug never starts or ends with a hyphen.

- `slugify("a  b")` returns `a-b`
- `slugify("a - b")` returns `a-b`
- `slugify("--a--")` returns `a`

## Files in scope

- `slugify.py`: change the function.
- `test_slugify.py`: add new tests only.

## Explicit exclusions

- Do not change any other file, including `README.md`.
- Do not change or delete the three existing tests.
- Do not add dependencies, new files, or new features (no accent handling, no length limits).

## Acceptance criteria

1. The three examples under Desired behavior return the stated results.
2. These still return the same results as before: `Hello World` gives `hello-world`, `Hello, World!` gives `hello-world`, and `  Hello World  ` gives `hello-world`.
3. The change is small enough to read in a few minutes.

## Required tests

- Before the change, the new tests fail. This proves they detect the problem.
- After the change, all tests pass, old and new.
- Run them with `python3 -m unittest` from the project directory.

## Security restrictions

- No network access.
- No secrets, tokens, or personal data in any file.
- No commits, pushes, or installs without approval from the human owner.

## Definition of done

- Every acceptance criterion is met.
- The tests were run and the results are reported with the exact command used.
- The human owner has read the diff and approved it.
