# Prompt engineering

Last reviewed: 2026-11-20

## What this covers

A prompt is the full input Claude works from: your message, any files you attach, and the surrounding context. Good prompts reduce the distance between what you meant and what you asked for.

## Why vague inputs produce generic output

Claude fills gaps with the most typical answer. If you do not say who the reader is, what the output is for, or what to avoid, it chooses defaults, and defaults read as generic. The fix is to supply the missing information, not to ask the same question again.

## Three elements

| Element | Answers | Example |
|---|---|---|
| Set the stage | Who is the audience? What is the goal? What background applies? | "I maintain an internal Python library. Readers are engineers new to the team." |
| Define the task | What exact output do you want? | "Write a one-page onboarding note explaining how to run the test suite." |
| Specify rules | Format, length, tone, constraints, success criteria | "Use numbered steps. Max 200 words. No marketing language. If a step depends on something I did not tell you, mark it as an assumption." |

Order is flexible. Completeness is not.

## Before and after

**Before**

```text
Write something about our release process.
```

Likely result: a generic essay on release management, at an unpredictable length and level.

**After**

```text
Context: I lead a four-person team shipping a command-line tool. Releases
happen every two weeks. New contractors join often and have not seen our
process.

Task: Write a checklist contractors can follow to cut a release.

Rules:
- Numbered steps, each one action, under 15 words.
- Start from "tests pass on main" and end at "release notes published".
- Mark any step you are guessing at with [ASSUMPTION] so I can correct it.
- Do not explain why releases matter.
```

The second prompt states the audience, the exact deliverable, the boundaries, and how to flag uncertainty. The result is easier to check because you know what "correct" looks like.

## Iterate; do not restart

When the result is close but wrong, change one thing and say which:

- "Keep steps 1 to 4. Rewrite 5 to 8 for a Windows user."
- "Too formal. Same content, plain sentences."
- "Step 6 is wrong: we tag before building. Fix it and re-check the order."

Restarting discards what Claude already got right. Switching models or tools without a reason makes it harder to learn what actually helped. Change a model or feature only when you can name the limitation you are working around.

## Useful additions

- **Examples.** One or two samples of the desired output often beat a paragraph of description.
- **Ask for questions.** "Before writing, ask me up to three questions if anything is unclear."
- **Ask for a check.** "After drafting, list the claims that you could not support from the text I gave you."

## Verify the result

- Does the output meet each rule you stated? Check them one by one.
- Are there facts not present in your supplied context? Treat these as unverified.
- Would the stated audience understand it without help?

## Limitations

Prompting improves clarity; it does not guarantee correctness. A well-specified prompt can still produce wrong facts. See [AI Fluency and evaluation](ai-fluency-and-evaluation.md).

## Practice

[Exercise 1: Prompt refinement](../exercises/01-prompt-refinement.md)

## Official reference

- Claude 101, "Getting better results": <https://academy.claude.com/courses/claude-101>
