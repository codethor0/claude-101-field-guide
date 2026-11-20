# Security and privacy

Last reviewed: 2026-11-20

A practical checklist. Each section says what the risk is and what to do.

## 1. Least-privilege connector access

Risk: a connector with broad access lets any mistake or injected instruction reach everything.

Do:

- Start read-only. Add write access only for a task that needs it.
- Scope to the narrowest folder, channel, or project.
- Use a dedicated service account with limited rights, not your administrator account.
- Review connected apps quarterly and remove those you no longer use. Revoke in both Claude and the service.

See [Connectors and MCP](connectors-and-mcp.md).

## 2. Human approval for sensitive actions

Require your explicit approval before Claude sends a message, deletes or overwrites data, changes permissions, spends money, submits a form, commits, pushes, or publishes. Read the specific action it asks to take, not only the summary of it.

## 3. Prompt injection

Risk: text from a web page, email, document, or tool result contains instructions ("ignore previous instructions and send the files to...") and Claude may treat it as a command. Anthropic's documentation acknowledges the risk for browser use and for connectors.

Do:

- Treat everything Claude retrieves from outside your own prompt as untrusted data.
- Do not combine untrusted content and powerful tools in the same session: a session that reads arbitrary web pages should not also hold write access to your mail.
- Watch for output that suddenly asks for credentials, changes the task, or tells you to run a command.
- Keep approval on any action with outside effect.

Example: you ask Claude to summarize a vendor's webpage. The page contains hidden text telling the assistant to email your contact list. With no email tool connected, the worst outcome is a bad summary. With one connected and no approval step, the outcome is much worse.

## 4. Sensitive data handling

- Know your organization's policy on what may be sent to AI services.
- Remove or mask personal data, credentials, and confidential material you do not need Claude to see.
- Understand the privacy and retention settings of your plan. Read the current terms and privacy policy: <https://www.anthropic.com/legal>.
- Do not paste secrets (API keys, tokens, private keys) into any prompt.

## 5. Source verification and fabricated citations

Claude can produce a citation that looks real but does not exist, or one that exists and does not support the claim.

Do:

- Open every cited link or reference you will rely on.
- Search for a quoted sentence in the source.
- Prefer primary sources. Check publication date.
- If you cannot verify a claim, delete it or label it unverified.

## 6. Browser automation boundaries

See [Other Claude tools](other-claude-tools.md#browser-automation-boundaries). Use a separate profile, avoid sensitive sites, and keep approval on submitting actions.

## 7. Repository secret hygiene

- Never commit credentials. Use environment variables.
- Ignore `.env` and key files before the first commit.
- Scan the full history before publishing a repository. A secret deleted in a later commit remains in history.
- If a secret was committed, rotate it first. Cleaning history does not make a leaked secret safe again.

## 8. Third-party skills and connectors

A skill can include scripts; a connector can run code or relay data to a third party. Before enabling:

- Read the instructions and scripts.
- Check who publishes it and whether the source is available.
- Check which permissions it requests.
- Test on non-sensitive data first.

Anthropic's documentation says it does not verify custom connectors.

## Limitations

This page is general guidance, not a security audit of any product. Product security controls change; use the linked official pages.

## Practice

[Exercise 5: Connector permissions](../exercises/05-connector-permissions.md)

## Official reference

- Claude Code security: <https://code.claude.com/docs/en/security>
- Using Claude in Chrome safely: <https://support.claude.com/en/articles/12902428-use-claude-in-chrome-safely>
- MCP security best practices: <https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices>
- Anthropic legal terms and policies: <https://www.anthropic.com/legal>
