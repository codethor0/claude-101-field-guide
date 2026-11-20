# Sources and verification

Last reviewed: 2026-11-20

How the claims in this repository were checked, and what was not.

## Method

- Product statements come from official pages (support.claude.com, code.claude.com, academy.claude.com, modelcontextprotocol.io), read on 2026-11-20.
- The content brief was the author's own learning notes from taking Claude 101. Those notes were not copied into the repository. Explanations, examples, and exercises were written fresh.
- Where a statement is time-sensitive, the page says "per the Help Center" and carries a review date.

## Verified statements

| Statement | Source | Status on 2026-11-20 |
|---|---|---|
| Project knowledge uses retrieval when it nears context limits; capacity expands up to 10x | [RAG for projects](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects) | Confirmed in the Help Center. Presented as a documented figure |
| Skills are folders of instructions loaded when relevant; format described as open | [What are skills](https://support.claude.com/en/articles/12512176-what-are-skills) | Confirmed |
| Remote connectors run from Anthropic's cloud; local servers reach only the desktop app | [Remote MCP](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp), [Local MCP](https://support.claude.com/en/articles/10949351-getting-started-with-local-model-context-protocol-mcp-servers-on-claude-desktop) | Confirmed |
| Anthropic does not verify custom connectors | Remote MCP article | Confirmed |
| Enterprise Search: Team and Enterprise; Owner setup; document and chat connectors required; results permission-aware | [Use Enterprise Search](https://support.claude.com/en/articles/12489464-use-enterprise-search) | Confirmed |
| Research: paid plans, requires web search, multi-search cited reports | [Use Research](https://support.claude.com/en/articles/11088861-use-research-on-claude) | Confirmed |
| Artifact types and sharing defaults | [What are artifacts](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them) | Confirmed |
| Claude Code description | [Overview](https://code.claude.com/docs/en/overview) | Confirmed |
| Claude in Chrome: beta, paid plans, injection risk "not zero" | [Safety article](https://support.claude.com/en/articles/12902428-use-claude-in-chrome-safely) | Confirmed |
| Claude Tag: Slack, beta, Team and Enterprise | [What is Claude Tag](https://support.claude.com/en/articles/15594475-what-is-claude-tag) | Confirmed |
| Claude for Excel, PowerPoint, Word, Outlook exist; GA on all paid plans (page statement) | [Product page](https://claude.com/claude-for-microsoft-365) | Confirmed on the page on 2026-11-20. Feature claims such as "nothing is saved until you say so" are Anthropic's own and were not tested here |
| Claude Design availability | [Get started](https://support.claude.com/en/articles/14604416-get-started-with-claude-design) | Confirmed |
| AI Fluency: 4Ds; "Copyright 2025 Rick Dakan, Joseph Feller, and Anthropic. Released under the CC BY-NC-SA 4.0 license." on the course page | [Course page](https://academy.claude.com/courses/ai-fluency-framework-foundations) | Confirmed for the course page. The framework document's own license was not checked |

## Supporting details checked in the same pages

These details appear in the guides and were read in the Help Center articles above on 2026-11-20: skills need code execution enabled; project retrieval applies on paid plans; artifact sharing settings are managed on web or desktop; Enterprise Search uses Anthropic-maintained instructions and is not on mobile; Claude Tag setup is by an Owner; Research typically runs for a few minutes.

## Not confirmed

| Item | Notes |
|---|---|
| Permission to use Anthropic names | The [Trademark Guidelines](https://www.anthropic.com/legal/trademark-guidelines) (effective 2024-08-01) allow use of the marks only as Anthropic specifically permits and in materials it approves beforehand, and they contain no stated exception for descriptive references. No permission has been requested or granted. See [NOTICE.md](../NOTICE.md) |
| Badge details | The README links the maintainer's badge verification page. That page renders its content in the browser; the name and issue date shown on it were not read programmatically, so the issue date in the README is the maintainer's statement |
| Whether Academy course content may be reused | The Academy FAQ says Anthropic does not offer content licensing. This repository therefore contains no Academy content, only links |
| Extended thinking behavior | The guides describe it generally (reasoning without web access). No page was cited for it; check the Help Center |
| Artifact comments and version history | Not confirmed; the artifacts guide says so |
| Desktop extension removal steps | Not found in the documentation reviewed |

## Link review

All entries in [official-links.md](official-links.md) returned HTTP 200 on 2026-11-20. A 200 shows the page was reachable, not that its content still matches the description. External links are checked by hand before each release, not in CI, so that outages and rate limits do not fail pull requests.

## Re-review

Date-sensitive pages: [other-claude-tools.md](../docs/other-claude-tools.md), [enterprise-search.md](../docs/enterprise-search.md), [artifacts.md](../docs/artifacts.md). Re-check them first.
