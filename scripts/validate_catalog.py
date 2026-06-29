from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "tools.json"
REQUIRED_FIELDS = {
    "category",
    "name",
    "url",
    "summary_zh",
    "language",
    "open_source",
    "stage",
}
VALID_STAGES = {"入门", "进阶", "生产"}


def validate_url(value: str) -> None:
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError(f"invalid url: {value}")


def main() -> None:
    tools = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    if not isinstance(tools, list):
        raise ValueError("catalog must be a list")

    seen_names: set[str] = set()
    for index, tool in enumerate(tools, start=1):
        if not isinstance(tool, dict):
            raise ValueError(f"item {index} must be an object")

        missing = REQUIRED_FIELDS - set(tool)
        if missing:
            raise ValueError(f"{tool.get('name', f'item {index}')} missing fields: {sorted(missing)}")

        name = tool["name"].strip()
        if not name:
            raise ValueError(f"item {index} has empty name")
        if name.lower() in seen_names:
            raise ValueError(f"duplicate project name: {name}")
        seen_names.add(name.lower())

        validate_url(tool["url"])
        if not isinstance(tool["open_source"], bool):
            raise ValueError(f"{name}: open_source must be boolean")
        if tool["stage"] not in VALID_STAGES:
            raise ValueError(f"{name}: stage must be one of {sorted(VALID_STAGES)}")
        if len(tool["summary_zh"]) > 100:
            raise ValueError(f"{name}: summary_zh should stay under 100 characters")

    print(f"Validated {len(tools)} projects.")


if __name__ == "__main__":
    main()
