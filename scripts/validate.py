#!/usr/bin/env python3
"""Validate repository structure, links, metadata, and hygiene.

Uses only the Python standard library and makes no network requests.
Usage: python3 scripts/validate.py [repo_root]
Exit status is 0 when all checks pass and 1 otherwise.
"""

import ast
import hashlib
import json
import re
import sys
from pathlib import Path

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "CONTENT_LICENSE.md",
    "NOTICE.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CHANGELOG.md",
    ".gitignore",
    ".github/workflows/validate.yml",
    ".github/ISSUE_TEMPLATE/documentation-issue.yml",
    "docs/getting-started.md",
    "docs/prompt-engineering.md",
    "docs/ai-fluency-and-evaluation.md",
    "docs/projects-and-skills.md",
    "docs/artifacts.md",
    "docs/connectors-and-mcp.md",
    "docs/enterprise-search.md",
    "docs/research.md",
    "docs/claude-code.md",
    "docs/other-claude-tools.md",
    "docs/security-and-privacy.md",
    "docs/choosing-the-right-tool.md",
    "docs/troubleshooting.md",
    "exercises/README.md",
    "resources/official-links.md",
    "resources/sources-and-verification.md",
]

DISCLAIMER = (
    "Independent educational resource. Not affiliated with, sponsored by, or "
    "endorsed by Anthropic or Claude Academy. Claude and associated product "
    "names belong to their respective owners."
)

EXERCISE_HEADINGS = [
    "Objective",
    "Prerequisites",
    "Verification checklist",
    "Common failure modes",
    "Follow-up",
]
MIN_EXERCISES = 5

ALLOWED_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".csv", ".txt", ""}
ALLOWED_NO_SUFFIX = {"LICENSE", ".gitignore"}

# Patterns are written so that this file does not match its own checks.
HYGIENE_PATTERNS = {
    "private key block": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}"),
    "Anthropic API key": re.compile(r"\bsk-ant-[A-Za-z0-9_-]{20,}"),
    "AWS access key id": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "home directory path": re.compile(r"/(?:Users|home)/[a-z][a-z0-9_.-]+/"),
    "AI co-author trailer": re.compile(r"Co-Authored-[B]y:", re.I),
    "personal email address": re.compile(
        r"\b[A-Za-z0-9._-]+@(?:gmail|icloud|outlook|hotmail|yahoo)\.com\b"
    ),
}

SKIP_DIRS = {".git", "__pycache__", ".pytest_cache"}
FENCE = re.compile(r"^\s*```")
LINK = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
DATE = re.compile(r"^Last reviewed: \d{4}-\d{2}-\d{2}\s*$", re.M)


def list_files(root: Path):
    for path in sorted(root.rglob("*")):
        if path.is_file() and not (set(path.relative_to(root).parts) & SKIP_DIRS):
            yield path


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def strip_fences(text: str) -> str:
    out, inside = [], False
    for line in text.splitlines():
        if FENCE.match(line):
            inside = not inside
            continue
        if not inside:
            out.append(line)
    return "\n".join(out)


def heading_slugs(text: str) -> set:
    slugs = set()
    for line in strip_fences(text).splitlines():
        m = re.match(r"^#{1,6}\s+(.*?)\s*#*\s*$", line)
        if m:
            s = re.sub(r"[^\w\- ]", "", m.group(1).lower()).strip().replace(" ", "-")
            slugs.add(s)
    return slugs


def check_required_files(root: Path, required=REQUIRED_FILES):
    return [f"missing required file: {f}" for f in required if not (root / f).is_file()]


def check_disclaimer(root: Path):
    errors = []
    for name in ("README.md", "NOTICE.md"):
        path = root / name
        if path.is_file():
            flat = " ".join(path.read_text(encoding="utf-8").split())
            if DISCLAIMER not in flat:
                errors.append(f"{name}: disclaimer text missing or altered")
    return errors


def check_links(root: Path):
    errors = []
    for path in list_files(root):
        if path.suffix != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for target in LINK.findall(strip_fences(text)):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                continue  # external or mailto; not checked offline
            file_part, _, anchor = target.partition("#")
            dest = path if not file_part else (path.parent / file_part).resolve()
            if file_part and not dest.exists():
                errors.append(f"{rel(path, root)}: broken link {target}")
                continue
            if anchor and dest.suffix == ".md" and dest.is_file():
                if anchor.lower() not in heading_slugs(dest.read_text(encoding="utf-8")):
                    errors.append(f"{rel(path, root)}: missing anchor {target}")
    return errors


def check_review_dates(root: Path):
    errors = []
    for folder in ("docs", "exercises", "resources"):
        for path in sorted((root / folder).glob("*.md")):
            if not DATE.search(path.read_text(encoding="utf-8")):
                errors.append(f"{rel(path, root)}: missing 'Last reviewed: YYYY-MM-DD' line")
    return errors


def check_docs_have_reference(root: Path):
    errors = []
    for path in sorted((root / "docs").glob("*.md")):
        if "## Official reference" not in path.read_text(encoding="utf-8"):
            errors.append(f"{rel(path, root)}: missing '## Official reference' section")
    return errors


def check_exercises(root: Path):
    errors = []
    files = sorted(p for p in (root / "exercises").glob("[0-9][0-9]-*.md"))
    if len(files) < MIN_EXERCISES:
        errors.append(f"exercises: found {len(files)}, need at least {MIN_EXERCISES}")
    for path in files:
        text = path.read_text(encoding="utf-8")
        for heading in EXERCISE_HEADINGS:
            if not re.search(rf"^##\s+{re.escape(heading)}\b", text, re.M):
                errors.append(f"{rel(path, root)}: missing section '{heading}'")
    index = root / "exercises" / "README.md"
    if index.is_file():
        body = index.read_text(encoding="utf-8")
        for path in files:
            if path.name not in body:
                errors.append(f"exercises/README.md: does not link {path.name}")
    return errors


def check_duplicates(root: Path):
    errors = []
    seen = {}
    paragraphs = {}
    for path in list_files(root):
        if path.suffix != ".md" or path.name in ("CONTENT_LICENSE.md",):
            continue
        data = path.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        if digest in seen:
            errors.append(f"duplicate file content: {rel(path, root)} == {seen[digest]}")
        seen[digest] = rel(path, root)
        for para in strip_fences(data.decode("utf-8")).split("\n\n"):
            norm = " ".join(para.split())
            if len(norm) >= 200 and not norm.startswith("|"):
                first = paragraphs.setdefault(norm, rel(path, root))
                if first != rel(path, root):
                    errors.append(
                        f"duplicated paragraph in {rel(path, root)} and {first}: {norm[:50]}..."
                    )
    return errors


def check_code(root: Path):
    errors = []
    for path in list_files(root):
        name = rel(path, root)
        if path.suffix == ".py":
            try:
                ast.parse(path.read_text(encoding="utf-8"), filename=name)
            except SyntaxError as exc:
                errors.append(f"{name}: Python syntax error: {exc}")
        elif path.suffix == ".md":
            lines = path.read_text(encoding="utf-8").splitlines()
            lang, buf, start = None, [], 0
            for i, line in enumerate(lines, 1):
                if FENCE.match(line):
                    if lang is None:
                        lang = line.strip()[3:].strip().lower() or ""
                        buf, start = [], i
                    else:
                        errors += _check_block(name, lang, "\n".join(buf), start)
                        lang = None
                elif lang is not None:
                    buf.append(line)
            if lang is not None:
                errors.append(f"{name}:{start}: unclosed code fence")
    return errors


def _check_block(name, lang, code, line):
    try:
        if lang in ("python", "py"):
            ast.parse(code)
        elif lang == "json":
            json.loads(code)
    except (SyntaxError, ValueError) as exc:
        return [f"{name}:{line}: invalid {lang} block: {exc}"]
    return []


def check_hygiene(root: Path):
    errors = []
    for path in list_files(root):
        name = rel(path, root)
        if path.suffix not in ALLOWED_SUFFIXES or (
            path.suffix == "" and path.name not in ALLOWED_NO_SUFFIX
        ):
            errors.append(f"{name}: file type not allowed in this repository")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"{name}: not valid UTF-8 text")
            continue
        for label, pattern in HYGIENE_PATTERNS.items():
            m = pattern.search(text)
            if m:
                errors.append(f"{name}: possible {label}")
    return errors


def check_workflow(root: Path):
    path = root / ".github/workflows/validate.yml"
    if not path.is_file():
        return []
    text = path.read_text(encoding="utf-8")
    errors = []
    if "pull_request_target" in text:
        errors.append("workflow: pull_request_target is not allowed")
    if not re.search(r"^permissions:\s*\n\s+contents:\s*read\s*$", text, re.M):
        errors.append("workflow: top-level 'permissions: contents: read' required")
    if "persist-credentials: false" not in text:
        errors.append("workflow: checkout must set persist-credentials: false")
    if "timeout-minutes:" not in text:
        errors.append("workflow: timeout-minutes required")
    for use in re.findall(r"uses:\s*(\S+)", text):
        if not re.search(r"@[0-9a-f]{40}$", use):
            errors.append(f"workflow: action not pinned to a full commit SHA: {use}")
    return errors


CHECKS = [
    ("required files", check_required_files),
    ("disclaimer", check_disclaimer),
    ("relative links", check_links),
    ("review dates", check_review_dates),
    ("official reference sections", check_docs_have_reference),
    ("exercises", check_exercises),
    ("duplicates", check_duplicates),
    ("code blocks and syntax", check_code),
    ("hygiene", check_hygiene),
    ("workflow security", check_workflow),
]


def main(argv):
    root = Path(argv[1] if len(argv) > 1 else ".").resolve()
    failed = 0
    for label, fn in CHECKS:
        errors = fn(root)
        status = "PASS" if not errors else "FAIL"
        print(f"{status}  {label}")
        for err in errors:
            print(f"      {err}")
        failed += bool(errors)
    print(f"\n{len(CHECKS) - failed}/{len(CHECKS)} checks passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
