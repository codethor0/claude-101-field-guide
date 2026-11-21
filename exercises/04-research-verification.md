# Exercise 4: Research verification

Last reviewed: 2026-11-20

## Objective

Verify a researched claim by comparing sources, publication dates, and evidence quality.

## Prerequisites

Research or web search. Read [Research](../docs/research.md). Needs internet access to open sources.

## Input data

A public question with several credible sources:

```text
How has the global average price of lithium-ion battery packs changed
over the last ten years, and how confident are the estimates?
```

Price surveys from different publishers may use different methods and scopes, so their figures may differ. Part of the exercise is finding out whether they do.

## Copy-ready prompt

```text
Research how the average price of lithium-ion battery packs (per kWh) has
changed over the last ten full years.

Requirements:
- Use at least three independent sources, preferring original survey
  publishers over news summaries.
- For each source give: publisher, publication date, the year range covered,
  how the figure is defined (pack or cell, which sectors), and the headline number.
- Present a table, then explain why the numbers differ.
- End with "What I could not confirm" and "How confident this conclusion is".
```

## Steps

1. Run the prompt. Save the report.
2. For each cited source, open the link. Record whether it opens, whether the date matches, and whether the figure matches the report.
3. Classify each source: primary survey, secondary summary, or unclear.
4. Decide which numbers are comparable and which are not.

## Expected result characteristics

- A table with several sources and clearly different definitions.
- An explanation of differences (scope, year, currency, definition).
- Honest hedging.

## Verification checklist

- [ ] Every cited URL opens.
- [ ] At least three figures were checked against the page.
- [ ] Publication dates are stated and recent enough to be useful.
- [ ] Definitions are compared like for like.
- [ ] Any mismatch between report and source is recorded.
- [ ] Your conclusion states what you cannot confirm.

## Common failure modes

- A citation points to a page that does not contain the number.
- Two figures are compared though one is cell-level and one is pack-level.
- A news article is cited in place of the survey it describes.
- A confident one-line conclusion hides disagreement between sources.

## Follow-up

Ask Claude to list the three claims in its report it is least sure of, then verify those first.
