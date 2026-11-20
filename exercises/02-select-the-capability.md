# Exercise 2: Select the right capability

Last reviewed: 2026-11-20

## Objective

Match four tasks to the most suitable capability and justify each choice.

## Prerequisites

Read [Choosing the right tool](../docs/choosing-the-right-tool.md). This is a reasoning exercise; no special plan is needed, though you can test your answers on a paid plan.

## Input data

| # | Scenario (fictional) |
|---|---|
| A | You need the current opening hours of a public library for tomorrow. |
| B | A city council is deciding on a bike-lane proposal. You want to understand the evidence from public traffic-safety studies, including where studies disagree. |
| C | You have a 12-task project with dependencies and deadlines pasted in. You want to know whether the schedule is feasible. |
| D | You work at a company. You want to find what your team decided last quarter about vendor selection, which was discussed in documents and chat. |

Options: quick web search, Research, extended thinking, Enterprise Search, a connector to one tool.

## Steps

1. For each scenario, pick one option and write two sentences on why.
2. Name one risk of your choice.
3. Name one way you would verify the answer.
4. Compare with the answer key below.

## Copy-ready prompt (optional check)

```text
Here are four tasks. For each, recommend one of: quick web search, Research,
extended thinking, Enterprise Search, a connector to a single tool. Explain
in two sentences and name the main risk. Tasks: [paste table]
```

Then compare Claude's answer with yours. Disagreement is useful; decide who is right.

## Expected result characteristics

Each choice is tied to the number of sources and where the information lives. Each risk is specific to its scenario. Claude's answer, if you run the optional check, may differ from the key; decide which reasoning holds up.

## Answer key (for these scenarios only)

| # | Suggested choice | Why | Risk | Verification |
|---|---|---|---|---|
| A | Quick web search | One current fact | Outdated page | Open the library's official page; note the date |
| B | Research | Many sources; disagreement is the point | Mismatched definitions across studies | Open each cited study; compare methods |
| C | Extended thinking | All inputs are supplied; no outside facts needed | Arithmetic slips | Recompute the critical path yourself |
| D | Enterprise Search | Internal documents and chat | Missed or conflicting sources | Open cited documents; check dates |

Other reasonable answers exist. Note for D: if Enterprise Search is unavailable, a connector to the document store and the chat tool is a fallback.

## Verification checklist

- [ ] Each choice is justified by number of sources and where the information lives.
- [ ] Each risk is specific to the scenario.
- [ ] Each verification step is something you could actually do.

## Common failure modes

- Choosing Research for a one-fact lookup.
- Choosing web search for a question that needs source comparison.
- Choosing Enterprise Search for public information.

## Follow-up

Write two scenarios of your own where the right choice is not obvious, and trade them with someone.
