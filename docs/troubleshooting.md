# Troubleshooting

Last reviewed: 2026-11-20

Problems seen when working with Claude, with a check and a fix for each.

| Symptom | Likely cause | Check | Fix |
|---|---|---|---|
| Generic, bland answer | Missing audience, goal, or constraints | Does the prompt say who it is for and what it is for? | Add context and rules. See [Prompt engineering](prompt-engineering.md) |
| Output ignores a rule | Rule buried or conflicting | Are rules listed plainly and do any contradict? | Put rules in a short list; remove conflicts; restate the one that failed |
| A fact is wrong | Model error or missing source | Is the fact in your supplied material? | Supply the source and require quotes; verify independently |
| Citation does not exist or does not support the claim | Fabricated or mismatched citation | Open the link; search for the quote | Delete the claim or replace the source. Ask for quotes with URLs |
| Long chat drifts from the original task | Context grows; early instructions weaken | Does the answer still follow the first message? | Restate key rules or start a fresh chat with a short summary of decisions |
| Project answers miss content that is in the files | Retrieval did not surface the passage | Ask where it found the answer; ask it to search for a specific term | Use consistent names; split large files; ask directly for the passage |
| Connector returns nothing or too little | Permissions, scope, or auth expired | Can your account open that item in the source tool? | Reconnect; check scope; confirm the item is in the connected folder or channel |
| Enterprise Search cannot be found | Not enabled for the plan or organization | Ask the administrator | Owner completes setup |
| Research result looks too confident | Evidence is thin or definitions differ | Read the sources' definitions and dates | Ask for a "what I could not confirm" section; verify key numbers |
| Exported file looks different | Formatting differs between tools | Open in the target application | Fix in the target; re-export if needed |
| Claude Code reports success but nothing changed | Command failed or wrong directory | Read the actual command output; run `git status` and `git diff` | Rerun the command yourself; ask for the exact output |

## General approach

1. Reproduce with the smallest input.
2. Identify which of prompt, context, tool, or permission is responsible.
3. Change one thing.
4. Retest.

## Limitations

Product behavior changes. If a symptom is not here or the fix does not work, use the Help Center: <https://support.claude.com/>.

## Official reference

- Help Center: <https://support.claude.com/>
- Academy FAQ: <https://academy.claude.com/help/faq>
