# AI Fluency and evaluation

Last reviewed: 2026-11-20

## The framework

The AI Fluency framework was developed by Rick Dakan (Ringling College of Art and Design) and Joseph Feller (University College Cork). Anthropic's Academy offers a course based on it, [AI Fluency: Framework & Foundations](https://academy.claude.com/courses/ai-fluency-framework-foundations). The framework names four competencies, the "4Ds". The descriptions below are this guide's own summary; use the course for the authors' definitions.

| Competency | In practice |
|---|---|
| Delegation | Decide which parts of a task to give to Claude, which to keep, and which to do together. |
| Description | Tell Claude what you want clearly enough to be useful: goal, context, constraints, and the kind of interaction you want. |
| Discernment | Evaluate what comes back: is it accurate, relevant, complete, and appropriate? |
| Diligence | Stay accountable for the result: check before sharing, disclose AI involvement where it matters, and handle data responsibly. |

The first two happen before and during the request. The last two happen after. Skipping Discernment and Diligence is the usual way people get into trouble, because fluent output feels finished.

The course page states that it is released under CC BY-NC-SA 4.0. This repository does not copy the course or framework text and does not relicense it; the table above is an original summary, not an adaptation. See [NOTICE.md](../NOTICE.md).

## Applying the 4Ds to one task

Task: summarize a 40-page vendor contract for a manager.

- **Delegation.** Claude can draft the summary and extract dates and obligations. You keep the decision on whether to sign, and you read the clauses the summary flags as risky.
- **Description.** "Summarize for a non-lawyer manager in under 300 words. List renewal date, termination notice period, and payment terms. Quote the clause number for each."
- **Discernment.** Open the contract and confirm each quoted clause exists and says what the summary claims.
- **Diligence.** Do not forward the summary as legal advice. Say it is an AI-assisted summary. Do not upload the contract if your agreement with the vendor or your employer prohibits it.

## A simple evaluation loop

Discernment scales into evaluation when you will run the same task many times (a template, a skill, a recurring report). Use this loop:

1. **Define observable success criteria.** "Every claim has a clause reference" is checkable. "Good summary" is not.
2. **Collect representative examples.** Five to ten real or realistic inputs, including at least one awkward case.
3. **Run the same task** on each example, with the same prompt.
4. **Inspect outputs** against what you already know the right answer to be.
5. **Record failures** with the input, the output, and what was wrong.
6. **Make one targeted change** to the prompt, context, or instructions.
7. **Retest** the full set, not just the failure you fixed.

Keep the examples and results in a file. A change that fixes one case and breaks another is common.

## Four checks worth scripting where possible

| Check | Question | Method |
|---|---|---|
| Factual accuracy | Is each stated fact true? | Compare to the source document or a primary reference. |
| Citation | Does each cited source exist, and does it say that? | Open every link or reference. Do not trust a citation you have not opened. |
| Completeness | Did it cover everything required? | Compare against a checklist written before the run. |
| Instruction following | Did it obey the format and constraints? | Count words, check headings, check forbidden terms. Many of these can be scripted. |

A scripted check for instruction following (word limit, required headings) is shown in [exercise 7](../exercises/07-artifact-creation.md).

## Limitations

- A small example set shows failures; it does not prove reliability.
- Passing your own criteria means the output met those criteria, not that it is correct.
- Output can differ between runs. Evaluate patterns across several runs rather than single results.

## Official reference

- AI Fluency course: <https://academy.claude.com/courses/ai-fluency-framework-foundations>
