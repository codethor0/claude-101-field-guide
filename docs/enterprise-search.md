# Enterprise Search

Last reviewed: 2026-11-20

## What it is

Enterprise Search lets people in an organization ask questions that are answered from the organization's own connected systems, such as documents, chat, and email. Per the Help Center (reviewed 2026-11-20), it appears as a pre-configured project in the sidebar and is available on Team and Enterprise plans.

## How it differs from a normal conversation with connectors

| | Conversation with connectors | Enterprise Search |
|---|---|---|
| Who configures | Each user adds connectors they choose | An organization Owner completes guided setup |
| Required sources | Whatever the user connects | Per the Help Center: a document connector and a chat connector; email recommended |
| Instructions | Yours | Search instructions maintained by Anthropic |
| Intended use | Ad hoc tasks with chosen tools | Organization-wide questions across authorized sources |

## Setup and permissions

1. An Owner completes setup and enables the required organizational connectors.
2. Each user authenticates individually with each connector.
3. Results follow the user's permissions in each source system. Someone who cannot open a document in the source system should not see it surfaced here.

Two caveats:

- Permissions are inherited from the source, so they are only as good as the source's access control. An over-shared folder is over-shared in search too. Fix sharing at the source.
- A connector configured with a shared credential returns what that credential can see, not what each person can see. Per the Help Center, this applies to custom connectors with shared credentials. Avoid shared credentials for this use.

## When to use it

- "What did we decide about vendor X, and where is that written down?"
- Finding which team owns a process, across documents and chat.

## When to avoid it

- Questions about public facts: use [Research or web search](research.md).
- Questions where an incomplete answer is dangerous (compliance, legal holds). Search recall is not guaranteed.
- If your plan or administrator has not enabled it.

## How to verify the result

1. Require citations in the prompt: "Cite the document title and location for each claim."
2. Open the cited sources. Confirm the cited passage says what the answer claims, and check its date.
3. When sources conflict, prefer the system of record (for example, the signed policy over a chat message) and note the discrepancy.
4. Ask a second question that should yield the same facts from a different angle.

## Example prompt

```text
Search our connected documents and chat for the current process to request
a new software license. List the steps, who approves each, and the most
recent date any source mentions this process. Cite each source. If you find
conflicting versions, show them side by side.
```

## Limitations

- Plan, administrator, and connector requirements change. Not available on mobile per the Help Center as of the review date.
- Retrieval can miss relevant documents. A statement that nothing was found is not proof that nothing exists.

## Official reference

- Use Enterprise Search: <https://support.claude.com/en/articles/12489464-use-enterprise-search>
