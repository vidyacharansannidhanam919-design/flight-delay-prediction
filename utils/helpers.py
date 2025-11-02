from __future__ import annotations

import re

import requests


def get_example_homepage_title() -> str:
    """Fetch example.com and extract the <title> text.

    Returns a fallback string if the title cannot be found.
    """
    response = requests.get("https://example.com", timeout=10)
    response.raise_for_status()
    match = re.search(r"<title>(.*?)</title>", response.text, flags=re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else "(no title found)"

