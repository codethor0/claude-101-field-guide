# Research

Last reviewed: 2026-11-20

## Choosing a mode

| Need | Use | Why |
|---|---|---|
| One or two facts, current | Quick web search | Fast and cheap |
| Question needing many sources compared, with a report | Research | Plans an investigation, runs many searches that build on each other, synthesizes with citations |
| Reasoning over material you already have, no web needed | Extended thinking | Spends effort on the problem itself |
| Question about your organization's own documents and chat | Enterprise Search | Uses connected internal sources with source permissions |

Per the Help Center (reviewed 2026-11-20), Research is available on paid plans, requires web search to be on, and typically takes a few minutes. Check the current page for availability.

## What a systematic investigation does

1. **Plan.** Break the question into sub-questions.
2. **Gather.** Search several independent sources per sub-question.
3. **Compare.** Note where sources agree and conflict.
4. **Synthesize.** Write up what is supported, with citations, and what is uncertain.

You can do the same steps by hand, and you should check each one in the output.

## Inspect before trusting

For every source cited:

- **Date.** Is it current enough for the question?
- **Origin.** Is it the primary source (the dataset, the regulation, the paper) or a summary of one?
- **Method.** How was the figure produced? Sample, definition, time window.
- **Uncertainty.** Does the claim hedge? Does the synthesis keep the hedge?
- **Existence.** Open the link. Fabricated or mismatched citations occur.

## Worked example (public, non-sensitive)

Question: "Has the share of electricity generated from solar in the United States grown over the last decade, and by how much?"

Prompt:

```text
Research the share of U.S. electricity generation from solar (utility-scale
and small-scale) from 2015 to the most recent full year available.

Requirements:
- Use primary data from U.S. government statistics where possible.
- State the exact definition each source uses (utility-scale only, or
  including rooftop estimates).
- Give the figure for 2015 and the latest year, with the source and
  publication date for each.
- If two sources disagree, show both and explain the likely reason.
- End with a section "What I could not confirm".
```

What to check in the result:

- The two figures come from sources using the same definition. A comparison of utility-scale in one year to utility plus rooftop in another is invalid.
- The cited statistics agency page exists and shows those numbers. Open it.
- "Latest year" is stated with its actual year, not "recent".
- The "could not confirm" section is present and honest.

If a number cannot be matched to the cited page, treat it as unverified and say so. [Exercise 4](../exercises/04-research-verification.md) uses a similar question.

## When to avoid Research

- A one-fact lookup: slower and costlier than needed.
- Questions where the sources are paywalled or require login; Research cannot read what it cannot reach, and the report may under-represent them.

## Limitations

- Output quality depends on what is publicly reachable and indexed.
- A synthesis can read more certain than the underlying evidence. Look for the caveats and add your own.
- Treat the report as a draft that tells you where to look.

## Official reference

- Use Research: <https://support.claude.com/en/articles/11088861-use-research-on-claude>
- Academy use cases: <https://academy.claude.com/use-cases/plan-your-literature-review>, <https://academy.claude.com/use-cases/verify-statistics-from-raw-data>
