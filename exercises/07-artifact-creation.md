# Exercise 7: Artifact creation

Last reviewed: 2026-11-20

## Objective

Turn notes into a short document and evaluate it against acceptance criteria defined in advance.

## Prerequisites

Artifacts available on your plan (a document or similar). Python 3 for the optional script check. Read [Artifacts](../docs/artifacts.md).

## Input data

[`examples/meeting-notes.md`](../examples/meeting-notes.md), a synthetic meeting record.

## Acceptance criteria (write these first)

1. Contains the headings "Decisions", "Open questions", "Actions".
2. Lists both decisions from the notes and no others.
3. Lists both open questions, each with an owner or the word "unassigned".
4. Lists both actions with the person named in the notes.
5. Under 200 words.
6. Contains no names or facts absent from the notes.

## Copy-ready prompt

```text
Turn the attached meeting notes into a one-page document.
Headings: Decisions, Open questions, Actions.
Rules:
- Use only information in the notes. Do not add names, dates, or facts.
- For each open question, give the owner if the notes say, otherwise write "unassigned".
- Under 200 words.
```

## Steps

1. Generate the artifact.
2. Check each criterion by hand.
3. Run the script check below on the document's text (paste into `brief.txt`).
4. Revise only the failing parts: "Fix only criterion 3; leave everything else."
5. Re-check all criteria, not just the one you fixed.

## Script check (criteria 1 and 5)

Save as `check_brief.py` and run `python3 check_brief.py brief.txt`.

```python
import sys

text = open(sys.argv[1], encoding="utf-8").read()
required = ["decisions", "open questions", "actions"]
headings = [ln.lstrip("# ").strip().lower() for ln in text.splitlines()
            if ln.strip() and (ln.startswith("#") or len(ln.split()) <= 3)]
missing = [h for h in required if h not in headings]
words = len(text.replace("#", " ").split())

print("missing headings:", missing or "none")
print("word count:", words, "(limit 200)")
sys.exit(1 if missing or words >= 200 else 0)
```

The script treats a line as a heading if it starts with `#` or has three words or fewer, and ignores case. Scripts only check structure and length. Criteria 2, 3, 4, and 6 need you to read the notes.

## Expected result characteristics

- A short document in the requested structure.
- Possibly a minor invented detail on the first pass, which criterion 6 should catch.

## Verification checklist

- [ ] All six criteria were checked individually.
- [ ] The script exit status was observed.
- [ ] A revision changed only the failing sections.
- [ ] All criteria were rechecked after revision.
- [ ] If exported, the exported file was opened and inspected.

## Common failure modes

- A tidy layout hides a changed fact.
- "Open questions" are turned into decisions.
- The revision alters text you had accepted.

## Follow-up

Ask for a three-slide version for stakeholders, write a new set of acceptance criteria for slides, and check it the same way.
