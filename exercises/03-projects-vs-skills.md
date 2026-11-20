# Exercise 3: Projects versus Skills

Last reviewed: 2026-11-20

## Objective

Split a recurring workflow into persistent context (project) and reusable procedure (skill), and justify the split.

## Prerequisites

Read [Projects and Skills](../docs/projects-and-skills.md). Creating a real project or skill is optional; the written design is the exercise.

## Input data

Fictional scenario: a small bakery owner writes a weekly newsletter. Facts that stay the same: shop hours, address, allergen policy, the owner's voice (warm, brief, no puns). The weekly process: pick three products, write a 150-word intro, add one customer story from a list, include an allergen reminder, end with the hours.

## Steps

1. List everything above as one of: **background fact** or **procedure step**.
2. Draft the project's instructions and knowledge list.
3. Draft the skill: a name, a one-line trigger description, and numbered steps.
4. Explain one case where you would change only the project, and one where you would change only the skill.

## Copy-ready prompt

```text
Here is a weekly workflow: [paste the scenario]. Split it into (1) background
facts that belong in a project and (2) a repeatable procedure that belongs in
a skill. Output a project instruction block and a skill outline with a name,
a description of when it applies, and numbered steps. Do not duplicate
content between the two.
```

## Expected result characteristics

- The project holds hours, address, allergen policy, and voice.
- The skill holds the weekly sequence and its output format.
- No content appears in both.
- The skill description says when to use it.

## Verification checklist

- [ ] No procedure is stored as a fact and no fact is embedded in the steps.
- [ ] Changing the shop hours requires editing one place.
- [ ] Changing the newsletter structure requires editing one place.
- [ ] You can state what happens if the skill is used outside this project.

## Common failure modes

- Copying the hours into the skill steps, so they go stale.
- A skill description so broad that it applies to every task.
- A project with only instructions and no source material.

## Follow-up

Add a second newsletter (for a market stall) that reuses the skill with a different project. Note what you had to change.
