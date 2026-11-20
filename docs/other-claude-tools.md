# Other Claude tools

Last reviewed: 2026-11-20

This page separates what Anthropic documents from what is not verified here. Availability, plans, and names change quickly. Each row points to the current source.

## Summary

| Tool | Purpose (per official documentation) | Verified in this repository | Note |
|---|---|---|---|
| Claude desktop app: Chat, Cowork, Code | The Claude 101 course describes three shapes of work: turn-by-turn conversation, handing work off, and building software | Course page only | Check the Help Center for current naming and plans |
| Claude Code | Agentic coding tool in terminal, IDE, desktop, and web | Yes: [overview](https://code.claude.com/docs/en/overview) | See [Claude Code](claude-code.md) |
| Claude Tag | Tag @Claude in Slack to work in channels | Yes: [support article](https://support.claude.com/en/articles/15594475-what-is-claude-tag) | Described as beta for Team and Enterprise; set up by an Owner |
| Claude Design | Create designs, prototypes, and one-pagers | Yes: [support article](https://support.claude.com/en/articles/14604416-get-started-with-claude-design) | Available as an artifact template; the article notes a standalone site is closing in December 2026 |
| Claude in Chrome | Browser extension that acts on websites on your behalf | Yes: [safety article](https://support.claude.com/en/articles/12902428-use-claude-in-chrome-safely) | Beta; paid plans; prompt injection risk is acknowledged |
| Claude for Excel, PowerPoint, Word, Outlook | Works inside each Microsoft 365 application: Excel (cells, formulas, models), PowerPoint (slides in your template), Word (tracked changes, comment threads), Outlook (inbox triage, drafts, scheduling) | Yes: [product page](https://claude.com/claude-for-microsoft-365) | The page states these are generally available on all paid plans; check the Help Center for plan and admin details |

"Verified" means the cited page described the product on 2026-11-20. It does not mean this repository tested the product.

## Practical uses

- **Desktop app.** Use the conversation mode for quick back-and-forth, delegated mode for longer tasks you review later, and code mode for software work. Pick by how much supervision the task needs.
- **Claude Tag.** Questions and tasks that arise inside a team's Slack channels. Check what channel content Claude can see and who can see its output, since a channel is a shared space.
- **Claude Design.** Visual drafts you will refine; check exported output for text and layout errors.
- **Microsoft 365 integrations.** Working inside spreadsheets, documents, decks, or email you already have open. Anthropic's page says edits are reviewable (tracked changes in Word, highlighted cells in Excel, Outlook drafts that wait for you to send). That is a product claim: confirm the behavior on a harmless file first, and verify formulas, tracked changes, and any message before it is sent.
- **Claude in Chrome.** Repeating web steps (filling forms, gathering information from pages). Use the safety guidance below.

## Browser automation boundaries

Anthropic's article on using Claude in Chrome safely states that prompt injection risk "is not zero" and describes mitigations, including permissions, blocked sites, and approval steps. Reasonable practice:

- Use a separate browser profile with no saved sensitive sessions.
- Do not run it on banking, health, or admin consoles.
- Keep human approval on actions that submit, purchase, send, or delete.
- Watch what it does on pages you do not control.

## Product capability versus marketing

When a page says a tool "automates" or "transforms" something, look for: what exact actions it can take, what it needs permission for, what plan is required, and what the documentation says it cannot do. Test on a harmless task before trusting it with a real one.

## Limitations

This page is the most likely in the repository to go stale. Verify against the linked source before acting on it.

## Official reference

- Claude 101, "Other ways to work with Claude": <https://academy.claude.com/courses/claude-101>
- Claude for Microsoft 365: <https://claude.com/claude-for-microsoft-365>
- Help Center: <https://support.claude.com/>
