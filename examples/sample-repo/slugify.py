"""Turn a title into a URL-friendly slug."""

import re


def slugify(title: str) -> str:
    """Lowercase the title and replace each run of spaces with hyphens.

    Non-alphanumeric characters other than spaces and hyphens are removed.
    """
    cleaned = re.sub(r"[^a-z0-9 -]", "", title.lower())
    return cleaned.strip().replace(" ", "-")
