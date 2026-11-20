# Connectors and MCP

Last reviewed: 2026-11-20

## What they are

A connector lets Claude read from, and in some cases act in, an external service such as a document store, a chat tool, or a task tracker.

The Model Context Protocol (MCP) is an open standard that defines how an AI application talks to such services. A service exposes an MCP server; Claude acts as the client. One protocol means one integration approach instead of one per tool. See <https://modelcontextprotocol.io/>.

## Two forms

| | Remote (web) connector | Local server or desktop extension |
|---|---|---|
| Runs | On the service provider's infrastructure | On your computer |
| Reached from | Anthropic's cloud, so the server must be reachable over HTTPS | The Claude desktop app only |
| Typical setup | Add the connector, sign in | Install an extension package or configure a local server |
| Main risk | Over-broad access granted to a remote service | Code running on your machine with your file access |

Per Anthropic's help documentation (reviewed 2026-11-20), local servers do not reach claude.ai in the browser or cloud sessions. Check the current pages for setup steps.

## Authentication, scope, and revocation

- **Authentication.** Most connectors use OAuth: you sign in with the service, and Claude does not see your password. Some use an API key or token, which is a stored credential, so treat it like a password.
- **Scope.** Claude can reach only what the connected account or token can reach. Connecting a tool does not grant more than the account has, and it also does not limit Claude below what the account has. Account-level permissions are the real boundary.
- **Data retrieval versus actions.** Reading a document and creating or deleting something are different permissions. Many connectors offer both. Review which tool calls are enabled and require approval for anything that changes data.
- **Revocation.** Disconnect in Claude's settings, and also revoke the grant in the service's own security settings. Removal in only one place may leave access active in the other.
- **Least privilege.** Grant the narrowest access that does the job: read-only before read-write, one project before the whole workspace, a service account before a personal admin account.

Connecting a tool does not authorize unlimited access or unlimited action. Each tool call still happens within the permissions you or an administrator granted, and you can disable individual tools or require approval.

## Trust

Anthropic's documentation states it does not verify custom connectors and warns that a malicious server can hide prompt injection. Treat a connector like software you install:

- Prefer connectors from the directory or the service's own vendor.
- Read what permissions it requests.
- Do not add a server from an unknown source because a document or webpage suggested it.

Content that a connector retrieves is also untrusted input. See [Security and privacy](security-and-privacy.md).

## Sanitized workflow: weekly project status

Goal: produce a weekly status update for a fictional project, "Orchard Migration".

Connected (read-only where possible):

- Document store: the project plan folder only.
- Chat: two project channels only.
- Task tracker: the Orchard project board.

Prompt:

```text
Using only the Orchard Migration plan folder, the #orchard and #orchard-ops
channels, and the Orchard board, draft a status update for the last 7 days.

Sections: Done, In progress, Blocked, Decisions needed.
For every item, name the source (document title, channel and date, or task ID).
If sources disagree, say so and show both. Do not create or change any task.
```

Why it is shaped this way:

- Scoped sources limit what can be read.
- "Do not create or change any task" states intent, but the real control is that the tracker connection is read-only or that write actions require approval. A prompt is not a permission.
- Requiring a source for each item makes the output checkable.

Verification: open five randomly chosen items and confirm the cited source says that. Check that no blocked item is missing from the board's own blocked list.

## Limitations

- Availability and behavior differ across plans, apps, and administrator settings.
- A connector can return incomplete results (pagination, permissions, search limits). Absence of an item in the answer does not mean it does not exist.

## Practice

[Exercise 5: Connector permissions](../exercises/05-connector-permissions.md)

## Official reference

- Custom connectors using remote MCP: <https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp>
- Local MCP servers on Claude Desktop: <https://support.claude.com/en/articles/10949351-getting-started-with-local-model-context-protocol-mcp-servers-on-claude-desktop>
- MCP security best practices: <https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices>
- Academy use case: <https://academy.claude.com/use-cases/generate-project-status-reports>
