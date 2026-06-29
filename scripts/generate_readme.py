from __future__ import annotations

import json
from collections import OrderedDict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "tools.json"
README_FILE = ROOT / "README.md"
START = "<!-- BEGIN GENERATED -->"
END = "<!-- END GENERATED -->"


def load_tools() -> list[dict]:
    with DATA_FILE.open("r", encoding="utf-8") as file:
        tools = json.load(file)
    if not isinstance(tools, list):
        raise ValueError("data/tools.json must contain a list")
    return tools


def group_by_category(tools: list[dict]) -> OrderedDict[str, list[dict]]:
    grouped: OrderedDict[str, list[dict]] = OrderedDict()
    for tool in tools:
        category = tool["category"]
        grouped.setdefault(category, []).append(tool)
    return grouped


def render_table(tools: list[dict]) -> str:
    lines = [
        "| 项目 | 简介 | 语言 | 开源 | 适合阶段 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for tool in tools:
        open_source = "是" if tool["open_source"] else "否"
        lines.append(
            "| [{name}]({url}) | {summary} | {language} | {open_source} | {stage} |".format(
                name=tool["name"],
                url=tool["url"],
                summary=tool["summary_zh"],
                language=tool["language"],
                open_source=open_source,
                stage=tool["stage"],
            )
        )
    return "\n".join(lines)


def render_generated_section(tools: list[dict]) -> str:
    sections: list[str] = []
    for category, category_tools in group_by_category(tools).items():
        sections.append(f"### {category}\n\n{render_table(category_tools)}")
    return "\n\n".join(sections)


def replace_generated_section(readme: str, generated: str) -> str:
    start_index = readme.index(START) + len(START)
    end_index = readme.index(END)
    return readme[:start_index] + "\n\n" + generated + "\n\n" + readme[end_index:]


def main() -> None:
    tools = load_tools()
    readme = README_FILE.read_text(encoding="utf-8")
    generated = render_generated_section(tools)
    README_FILE.write_text(replace_generated_section(readme, generated), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
