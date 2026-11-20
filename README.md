# Claude 101 Field Guide

A practical, independently written guide to using Claude: how to prompt it, choose the right feature, connect it to tools, check its output, and work with it safely. It includes seven hands-on exercises with synthetic data and a small validation script for the documentation itself.

> Independent educational resource. Not affiliated with, sponsored by, or endorsed by Anthropic or Claude Academy. Claude and associated product names belong to their respective owners.

The guide is a companion to Anthropic's Claude Academy course [Claude 101](https://academy.claude.com/courses/claude-101), written by the maintainer after taking it. It contains original explanations and exercises, not course material. See [NOTICE.md](NOTICE.md).

## Who it is for

| Reader | Start with | Then |
|---|---|---|
| **Beginner**: never used Claude | [Getting started](docs/getting-started.md) | [Prompt engineering](docs/prompt-engineering.md), [Exercise 1](exercises/01-prompt-refinement.md) |
| **Working professional**: wants repeatable workflows | [Choosing the right tool](docs/choosing-the-right-tool.md) | [Projects and Skills](docs/projects-and-skills.md), [Research](docs/research.md), [Artifacts](docs/artifacts.md) |
| **Developer or technical practitioner** | [Claude Code](docs/claude-code.md) | [Connectors and MCP](docs/connectors-and-mcp.md), [Evaluation](docs/ai-fluency-and-evaluation.md), [Exercise 6](exercises/06-safe-coding-workflow.md) |

## Five-minute quick start

1. Read [Getting started](docs/getting-started.md) (about three minutes).
2. Do the first-session steps in it with a short text of your own.
3. Open [Exercise 1](exercises/01-prompt-refinement.md) and compare a vague prompt with a structured one.

No installation is needed to read or follow the guides.

## Learning path

| Step | Guide | Question it answers |
|---|---|---|
| 1 | [Getting started](docs/getting-started.md) | What is Claude, and when should I use it? |
| 2 | [Prompt engineering](docs/prompt-engineering.md) | How do I ask for what I mean? |
| 3 | [AI Fluency and evaluation](docs/ai-fluency-and-evaluation.md) | How do I judge and verify the result? |
| 4 | [Choosing the right tool](docs/choosing-the-right-tool.md) | Which capability fits this task? |
| 5 | [Projects and Skills](docs/projects-and-skills.md) | How do I reuse context and procedures? |
| 6 | [Artifacts](docs/artifacts.md) | How do I create and share documents, decks, and designs? |
| 7 | [Connectors and MCP](docs/connectors-and-mcp.md) | How do I connect external tools safely? |
| 8 | [Enterprise Search](docs/enterprise-search.md) | How does organization-wide search differ? |
| 9 | [Research](docs/research.md) | How do I run and check a multi-source investigation? |
| 10 | [Claude Code](docs/claude-code.md) | How do I use it for software work without losing control? |
| 11 | [Other Claude tools](docs/other-claude-tools.md) | What do the other products do, and what is verified? |
| 12 | [Security and privacy](docs/security-and-privacy.md) | What are the practical risks and controls? |
| Ref | [Troubleshooting](docs/troubleshooting.md) | Something went wrong. What do I check? |

## Hands-on exercises

Seven original exercises. Each has an objective, prerequisites, input data, a copy-ready prompt, expected result characteristics, a verification checklist, common failure modes, and a follow-up; the validator enforces these headings. Index: [exercises/README.md](exercises/README.md).

1. [Prompt refinement](exercises/01-prompt-refinement.md)
2. [Select the right capability](exercises/02-select-the-capability.md)
3. [Projects versus Skills](exercises/03-projects-vs-skills.md)
4. [Research verification](exercises/04-research-verification.md)
5. [Connector permissions](exercises/05-connector-permissions.md)
6. [Safe coding workflow](exercises/06-safe-coding-workflow.md)
7. [Artifact creation](exercises/07-artifact-creation.md)

Generated output varies between runs. The exercises describe what to look for, not exact text.

## Author background

The maintainer completed the Claude Academy course Claude 101 and earned its completion badge on 2026-11-20: [badge verification page](https://academy.claude.com/verify/945193f993a9384624baa3f84e8931b8). The badge shows course completion only. It is not a professional certification, and it does not mean Anthropic reviewed or endorses this repository.

## Prerequisites

- To read: a web browser.
- To do exercises: a Claude account. Some features need a paid plan; each exercise says so.
- To run the repository checks: Python 3 (standard library only; no packages to install) and Git.

## Running the checks

From the repository root:

```sh
python3 -m unittest discover -s scripts   # tests for the validator
python3 scripts/validate.py               # structure, links, hygiene, code syntax
(cd examples/sample-repo && python3 -m unittest)   # sample repository tests
```

The validator makes no network requests. It checks required files, the disclaimer, relative links and anchors, review dates, exercise structure, duplicated content, code-block syntax, forbidden file types, secret-like strings, and the CI workflow's security settings. GitHub Actions runs the same commands on pull requests and pushes to `main`.

External links are reviewed by hand before releases and are not checked in CI.

## Official Claude Academy links

- [Claude 101 course](https://academy.claude.com/courses/claude-101)
- [Academy use cases](https://academy.claude.com/all?kind=use-case)
- [Academy FAQ](https://academy.claude.com/help/faq)

The full annotated list is in [resources/official-links.md](resources/official-links.md). How claims were checked is in [resources/sources-and-verification.md](resources/sources-and-verification.md).

## Security and privacy

Read [Security and privacy](docs/security-and-privacy.md) before connecting tools or sharing data. The short version: grant the minimum access, require approval for actions that change things, treat retrieved content as untrusted, open every citation, and never paste secrets into a prompt. To report a problem with this repository, see [SECURITY.md](SECURITY.md).

## Known limitations

- Product features, plans, and limits change. Each page has a review date; check the linked official source before relying on a detail.
- Product statements about Claude for Microsoft 365 come from Anthropic's product page and were not tested hands-on. See [Other Claude tools](docs/other-claude-tools.md).
- Anthropic has not reviewed or approved this repository's use of its names. See [NOTICE.md](NOTICE.md).
- The guide has not been tested against every plan or administrator configuration.
- Exercises were written against the product behavior described on 2026-11-20 and may need adjustment.
- This is not a substitute for the official documentation or for professional advice.

## Licensing and attribution

- Code and scripts: [MIT](LICENSE).
- Original written content: [CC BY 4.0](CONTENT_LICENSE.md).
- Anthropic's course materials, trademarks, and product assets are not covered by these licenses and are not included. The AI Fluency framework is by Rick Dakan and Joseph Feller; this guide summarizes it and links to the source.

Scope details are in [NOTICE.md](NOTICE.md).

## Contributing

Corrections are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md). Do not submit Academy lesson text, quiz questions, or screenshots.

## Maintainer

[codethor0](https://github.com/codethor0)
