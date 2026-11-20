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
| Claude Design availability | [Get started](https://support.claude.com/en/articles/14604416-get-started-with-claude-design) | Confirmed |
| AI Fluency: 4Ds; Dakan and Feller; CC BY-NC-SA 4.0 on the course page | [Course page](https://academy.claude.com/courses/ai-fluency-framework-foundations) | Confirmed for the course page. The framework document's own license was not checked |

## Supporting details checked in the same pages

These details appear in the guides and were read in the Help Center articles above on 2026-11-20: skills need code execution enabled; project retrieval applies on paid plans; artifact sharing settings are managed on web or desktop; Enterprise Search uses Anthropic-maintained instructions and is not on mobile; Claude Tag setup is by an Owner; Research typically runs for a few minutes.

## Not confirmed

| Item | Notes |
|---|---|
| Claude for Excel, PowerPoint, Word, Outlook | No official page was found during the review. The course page says "Claude for Microsoft 365". Described as unverified in the guide |
| Anthropic brand and trademark guidance for third parties | The URLs guessed during research returned 404. The disclaimer wording is a plain nominative statement, not a reviewed approved text. See [NOTICE.md](../NOTICE.md) |
| Public badge verification URL | The Academy FAQ says badges have a public verification link but does not give a URL pattern. No badge link is included |
| Whether Academy course content may be reused | The Academy FAQ says Anthropic does not offer content licensing. This repository therefore contains no Academy content, only links |
| Extended thinking behavior | The guides describe it generally (reasoning without web access). No page was cited for it; check the Help Center |
| Artifact comments and version history | Not confirmed; the artifacts guide says so |
| Desktop extension removal steps | Not found in the documentation reviewed |

## Link review

All entries in [official-links.md](official-links.md) returned HTTP 200 on 2026-11-20. A 200 shows the page was reachable, not that its content still matches the description. External links are checked by hand before each release, not in CI, so that outages and rate limits do not fail pull requests.

## Re-review

Date-sensitive pages: [other-claude-tools.md](../docs/other-claude-tools.md), [enterprise-search.md](../docs/enterprise-search.md), [artifacts.md](../docs/artifacts.md). Re-check them first.
