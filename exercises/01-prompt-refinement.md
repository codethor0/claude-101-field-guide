# Exercise 1: Prompt refinement

Last reviewed: 2026-11-20

## Objective

Turn a vague request into a prompt with context, task, and rules, and see the difference in output.

## Prerequisites

Access to Claude on any plan. Read [Prompt engineering](../docs/prompt-engineering.md).

## Input data

Synthetic scenario: you run a volunteer food bank. Volunteers sometimes miss shifts because the sign-up reminder is easy to overlook. You want a reminder message.

Vague request:

```text
Write a reminder message for volunteers.
```

## Copy-ready prompt

Structured version, to run after the vague one. Adapt it to your own wording:

```text
Context: I coordinate a food bank with about 40 volunteers. Most are
students and retirees. They sign up for Saturday shifts online and
sometimes forget. We use text messages.

Task: Write a text-message reminder sent on Friday at 6 pm.

Rules:
- Under 280 characters.
- Friendly and plain; no exclamation marks.
- Include the shift time as the placeholder [TIME] and the address as [ADDRESS].
- Give one line on how to cancel: reply CANCEL.
- Do not mention donations.
```

## Steps

1. Run the vague request. Save the output.
2. Run the structured prompt above. Save the output.
3. Give one targeted correction to the second output, for example: "Keep the same message but address the volunteer by [NAME] and remove the closing thanks."

## Expected result characteristics

- The second output meets every stated rule, so you can check each one.
- The first output is longer, more generic, or in a tone you did not choose.
- After the correction, only the requested parts changed.

## Verification checklist

- [ ] Character count is under 280.
- [ ] Placeholders `[TIME]` and `[ADDRESS]` are present and unchanged.
- [ ] No exclamation marks.
- [ ] The cancel instruction is present.
- [ ] No mention of donations.
- [ ] After step 3, the rest of the message is unchanged.

## Common failure modes

- Count is a little over the limit. Say the number again and ask for a shorter version.
- Placeholders are filled with invented values. Add "Never invent a time or address."
- The correction rewrites everything. Add "Change only X; keep everything else identical."

## Follow-up

Ask Claude to write three variants for different audiences (students, retirees, a new volunteer), then write a rule for each audience that explains how the variants should differ.
