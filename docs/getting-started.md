# Getting started

Last reviewed: 2026-11-20

## What Claude is

Claude is an AI assistant made by Anthropic. You write to it in natural language, and it responds with text, code, analysis, or files. People use it for writing, research, coding, data analysis, document work, and working through problems.

It differs from narrower tools in what it keeps track of while it works:

| Tool | Typical strength | Where it falls short for multi-step work |
|---|---|---|
| Search engine | Finds documents that match a query | Returns links; you do the reading and synthesis |
| Simple chatbot or voice assistant | Fixed tasks: timers, FAQs, short answers | Limited ability to work with your files or hold a long task together |
| Claude | Reads your material, drafts, revises, and explains its reasoning in one conversation | Can be wrong, and sounds equally confident when it is |

The last row matters most. Claude produces fluent output whether or not it is correct, so every workflow in this guide includes a way to check the result.

## When to use it, and when not to

Use Claude when the task is mostly reading, writing, restructuring, or reasoning over material you can supply, and when you can check the result.

Avoid or add safeguards when:

- A wrong answer is costly and you cannot verify it (medical, legal, financial decisions).
- The input contains data you are not permitted to share with the service.
- The task needs a guaranteed-exact computation. Ask Claude to write and run code, or use a spreadsheet, and check the numbers.

## Five-minute first session

1. Sign in at claude.ai. Most of this guide works on any plan; paid-plan features are flagged where they appear.
2. Paste a short text you wrote (an email draft, a README section).
3. Ask: "Rewrite this for a reader who has never seen the project. Keep it under 120 words. List anything you changed in meaning."
4. Compare the result with your original. Did it change facts? The last sentence of the prompt asks Claude to surface that.
5. Reply with one targeted correction ("Shorter, and keep the second sentence unchanged") rather than starting over.

You have just used the three habits the rest of the guide builds on: supply context, state the task and rules, and iterate with specific feedback. See [Prompt engineering](prompt-engineering.md).

## Where to go next

- Need to pick a feature for a task: [Choosing the right tool](choosing-the-right-tool.md).
- Want repeatable habits for judging output: [AI Fluency and evaluation](ai-fluency-and-evaluation.md).
- Using Claude with company data or external tools: [Connectors and MCP](connectors-and-mcp.md) and [Security and privacy](security-and-privacy.md).

## Limitations

Feature names, plan requirements, and limits change. This page states general behavior only. Check the Help Center for current details.

## Official reference

- Claude 101 course: <https://academy.claude.com/courses/claude-101>
- Help Center: <https://support.claude.com/>
