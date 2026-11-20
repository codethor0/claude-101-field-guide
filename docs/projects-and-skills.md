# Projects and Skills

Last reviewed: 2026-11-20

## The distinction

| | Projects | Skills |
|---|---|---|
| Holds | Background: documents, instructions, and context for an ongoing body of work | A procedure: how to do a specific, repeatable task |
| Answers | "What should Claude know about this work?" | "How should Claude do this task?" |
| When it applies | Chats inside that project | When the task matches the skill, across conversations |
| Example | Product spec, style notes, past decisions | "Turn meeting notes into our standard status report" |

Per Anthropic's help documentation (reviewed 2026-11-20), project content is available to chats in the project, while a skill's detailed instructions are loaded only when relevant. Skills are folders of instructions, and optionally scripts and resources. The format is described as an open standard.

## When to use which

- **Project:** you keep returning to the same material (a client, a codebase, a research topic) and want Claude to start from it each time.
- **Skill:** you keep giving the same instructions (report layout, review checklist, brand rules) and want them applied consistently.
- **Both:** a project holds the client's facts and a skill holds your report procedure. Each does one job and can change independently.

Avoid putting procedures in project knowledge or facts in a skill. A procedure buried in a project is easy to ignore, and a skill with facts embedded goes stale.

## Knowledge retrieval and context

Claude can only attend to a limited amount of text at once (its context window). Two approaches to large material:

1. **Load everything.** All documents sit in context. Simple, but limited by window size.
2. **Retrieve.** Claude searches the knowledge base and brings in only passages relevant to the question. This allows a larger knowledge base, but the answer depends on what the search surfaces. A relevant passage that is not retrieved is not seen.

Anthropic's help pages say that on paid plans, a project switches to retrieval when its knowledge approaches the context limit, and that this expands capacity by up to 10 times. That figure appears in the official help article [Retrieval Augmented Generation (RAG) for projects](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects) as of 2026-11-20. It is a documented figure, not a guarantee of answer quality. Check the current page before relying on it.

Practical consequences:

- Name things consistently so searches find them.
- Ask for the source passage with an answer, so you can check retrieval found the right one.
- For a question that needs every document (for example, "what contradicts across all of these?"), do not assume retrieval covers everything.

How context is managed can change as the products change. Treat the behaviors above as current descriptions, not permanent guarantees.

## Example

A freelance analyst serves one client.

- **Project "Acme quarterly reporting":** client glossary, last four reports, data dictionary, a note saying "Acme calls churn 'lost accounts'".
- **Skill "quarterly-report":** steps: read the new data export, compute the standard metrics, draft in the standard section order, list any metric that changed more than 20% for manual review.

New quarter: upload the export, ask for the report. The project supplies the client vocabulary and history. The skill supplies the procedure.

## Verify the result

- Does the output use the project's terms and facts? Spot-check against the source.
- Did the skill's steps run in order? Ask Claude to list the steps it followed.
- If you edit a skill, retest on at least two earlier inputs (see [evaluation](ai-fluency-and-evaluation.md)).

## Limitations and trust

- Features and plan availability vary. Skills require code execution to be enabled, per the help documentation.
- Third-party skills can contain instructions or scripts you did not write. Read them before enabling. See [Security and privacy](security-and-privacy.md).

## Practice

[Exercise 3: Projects versus Skills](../exercises/03-projects-vs-skills.md)

## Official reference

- What are projects: <https://support.claude.com/en/articles/9517075-what-are-projects>
- What are skills: <https://support.claude.com/en/articles/12512176-what-are-skills>
- Package your brand guidelines in a skill (Academy use case): <https://academy.claude.com/use-cases/package-your-brand-guidelines-in-a-skill>
