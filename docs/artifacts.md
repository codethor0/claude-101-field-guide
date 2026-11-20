# Artifacts

Last reviewed: 2026-11-20

## What they are

An artifact is a standalone piece of output that Claude creates next to the conversation, such as a document, a slide deck, a design, a page, a diagram, or a small interactive tool. You can open it, edit it, and ask Claude to revise it, instead of copying text out of a chat.

Per the Help Center (reviewed 2026-11-20), artifact types include Docs, Slides, and Design templates, plus code, single-page sites, diagrams, dashboards, and small interactive tools. Some types (Sheets, Whiteboards, Motion) are described as beta or limited to certain plans. This list changes; see the official page.

## When to use an artifact

- The output will be reused, edited, or shared: a report, a deck, a prototype.
- You want to revise one section without regenerating everything.
- You want something you can interact with (a calculator, a small dashboard).

Avoid it when a short answer in chat is enough, or when the content is sensitive and you have not confirmed who can view a shared link.

## Working with an artifact

| Action | How it helps |
|---|---|
| Ask for a revision | "Tighten section 2 to three sentences. Leave the rest unchanged." |
| Edit directly | Fix a number or a name yourself; faster and exact. |
| Comments and revisions | Where your plan and artifact type support them, mark a specific passage or return to an earlier version. Not verified here; check the Help Center. |

State what must not change. Without that, a revision may alter text you already approved.

## Sharing

Per the Help Center, artifacts start private. Sharing changes who can view or edit. Treat sharing as a permission decision:

- Who can open the link, and can they edit?
- Does the artifact contain data the viewers should not see?
- On Team and Enterprise plans, administrators may control which artifact types are available.

Sharing settings are managed on web or desktop, not the mobile app, per the Help Center.

## Editable artifact versus exported file

| | Artifact | Exported file (for example .docx, .pptx, PDF) |
|---|---|---|
| Edited in | Claude | The target application |
| Revisions with Claude | Yes | Only if you bring it back |
| Fidelity to another tool's formatting | May differ | Depends on export |
| Recipient needs | Access to the artifact, if shared | The file only |

Export when someone needs a file to send or archive. Keep the artifact if you expect more Claude-assisted revisions. After export, open the file in its target application and check layout, fonts, and tables.

## Example

Turn meeting notes into a one-page brief with a defined acceptance test:

1. Paste the notes. Ask for a one-page document with sections "Decisions", "Open questions", "Owners".
2. Check against acceptance criteria: every decision in the notes appears; nothing appears that is not in the notes; each open question has an owner or is marked "unassigned".
3. Revise only the failing section.

[Exercise 7](../exercises/07-artifact-creation.md) turns this into a scripted check.

## Verify the result

Compare against source material, not against how polished the artifact looks. Presentations and designs in particular can look finished while containing wrong numbers.

## Limitations

Availability, plan requirements, administrator controls, and storage limits change. Do not rely on this page for them.

## Official reference

- What are artifacts: <https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them>
- Claude Design: <https://support.claude.com/en/articles/14604416-get-started-with-claude-design>
