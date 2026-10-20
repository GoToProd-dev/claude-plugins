#!/usr/bin/env python3
"""Regenerate references/<group>.md from the installed `hcloud` CLI's --help output.

Run after upgrading hcloud so the references match the installed version:

    python3 scripts/gen_references.py            # writes into ../references
    python3 scripts/gen_references.py --out DIR  # writes elsewhere
"""

import argparse
import re
import subprocess
from pathlib import Path

NON_COMMAND_SECTIONS = {"Usage", "Aliases", "Flags", "Global Flags", "Examples", "Columns"}
SKIP_TOP_LEVEL = {"help", "completion", "version"}
SECTION_RE = re.compile(r"^([A-Z][A-Za-z ]*):\s*$")
COMMAND_LINE_RE = re.compile(r"^  ([a-z][a-z0-9-]*)\s+(\S.*)$")


def help_text(path):
    result = subprocess.run(
        ["hcloud", *path, "--help"], capture_output=True, text=True, check=True
    )
    return result.stdout


def parse(text):
    """Split help output into (description, {section: [lines]})."""
    description, sections, current = [], {}, None
    for line in text.splitlines():
        match = SECTION_RE.match(line)
        if match:
            current = match.group(1)
            sections[current] = []
        elif current is None:
            description.append(line)
        else:
            sections[current].append(line)
    return "\n".join(description).strip(), sections


def subcommands(sections):
    found = []
    for name, lines in sections.items():
        if name in NON_COMMAND_SECTIONS:
            continue
        for line in lines:
            match = COMMAND_LINE_RE.match(line)
            if match:
                found.append((match.group(1), match.group(2).strip()))
    return found


def clean_block(lines):
    lines = [l for l in lines if not re.match(r"^\s+-h, --help\b", l)]
    while lines and not lines[-1].strip():
        lines.pop()
    while lines and not lines[0].strip():
        lines.pop(0)
    return "\n".join(l[2:] if l.startswith("  ") else l for l in lines)


def render_leaf(path, out):
    description, sections = parse(help_text(path))
    out.append(f"### `hcloud {' '.join(path)}`\n")
    if description:
        out.append(description + "\n")
    columns = [l.strip(" -") for l in sections.get("Columns", []) if l.strip()]
    if columns:
        out.append(f"**Columns:** {', '.join(columns)}\n")
    # Free-form sections like "Example file content" are part of the command's docs.
    for section in sections:
        if section not in NON_COMMAND_SECTIONS:
            out.append(f"**{section}:**\n\n```\n{clean_block(sections[section])}\n```\n")
    for section in ("Usage", "Aliases", "Flags", "Examples"):
        block = clean_block(sections.get(section, []))
        if block:
            out.append(f"**{section}:**\n\n```\n{block}\n```\n")


def walk(path, out):
    description, sections = parse(help_text(path))
    children = subcommands(sections)
    if not children:
        render_leaf(path, out)
        return
    # Groups with a one-line summary add nothing; longer ones (e.g. `config`) carry real docs.
    if "\n" in description:
        out.append(f"## `hcloud {' '.join(path)}`\n\n```\n{description}\n```\n")
    for name, _ in children:
        walk([*path, name], out)


def main():
    parser = argparse.ArgumentParser(description="Regenerate references from hcloud --help.")
    parser.add_argument(
        "--out", type=Path, default=Path(__file__).resolve().parent.parent / "references"
    )
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    version = subprocess.run(
        ["hcloud", "version"], capture_output=True, text=True, check=True
    ).stdout.strip()
    _, root_sections = parse(help_text([]))
    for group, summary in subcommands(root_sections):
        if group in SKIP_TOP_LEVEL:
            continue
        out = [
            f"# `hcloud {group}` — {summary}\n",
            f"Generated from `--help` output of {version}. "
            "Global flags (--context, --config, --endpoint, --debug, --quiet, ...) "
            "apply to every command and are omitted here.\n",
        ]
        walk([group], out)
        (args.out / f"{group}.md").write_text("\n".join(out))
        print(f"wrote {group}.md")


if __name__ == "__main__":
    main()
