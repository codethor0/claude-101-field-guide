# Choosing the right tool

Last reviewed: 2026-11-20

Use this page to match a task to a capability. Capability names and availability change; confirm in the Help Center.

## Decision table

| Your situation | Start with | Notes |
|---|---|---|
| I need a quick fact or recent news item | Web search in a conversation | Open the sources it cites |
| I need a comparison drawn from many public sources | [Research](research.md) | Slower; verify citations |
| I have a hard reasoning, math, or planning problem and all the inputs | Extended thinking | No web required |
| I need an answer from my organization's documents and chat | [Enterprise Search](enterprise-search.md) | Team and Enterprise plans |
| I need Claude to read or act in one specific tool | [Connector](connectors-and-mcp.md) | Least privilege |
| I keep working on the same body of material | Project | [Projects and Skills](projects-and-skills.md) |
| I keep repeating the same procedure | Skill | [Projects and Skills](projects-and-skills.md) |
| I need a document, deck, design, or interactive page | [Artifact](artifacts.md) | Check sharing |
| I need to change code in a repository | [Claude Code](claude-code.md) | Approval boundaries |
| I need to repeat web steps | Claude in Chrome | [Security](security-and-privacy.md) |

## Four test questions

1. **How many sources does the answer need?** One: search. Many: Research.
2. **Where does the information live?** The public web, your files, or your organization's systems.
3. **Does the task read or change things?** If it changes things, require approval and narrow the permission.
4. **Will I do this again?** If yes, save context in a project or the procedure in a skill.

## Worked comparisons

| Request | Choice | Reason |
|---|---|---|
| "What time zone is Lisbon in?" | Quick search or no tool | One fact |
| "Compare three public datasets on commute times and tell me where they disagree" | Research | Several sources, comparison |
| "Is my reasoning in this schedule consistent?" with the schedule pasted | Thinking | All inputs supplied |
| "Where did we write down the data retention policy?" | Enterprise Search | Internal knowledge |

[Exercise 2](../exercises/02-select-the-capability.md) practices this with its own scenarios.

## Limitations

A tool choice is a starting point. If the result is poor, say what is wrong and adjust, rather than switching tools at random.

## Official reference

- Claude 101: <https://academy.claude.com/courses/claude-101>
