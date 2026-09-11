#!/usr/bin/env python3
"""Script to automate adding a new skill to skills.yaml.

This script appends a new skill entry to the skills configuration file.
It validates input parameters, formats them as YAML, and appends them.
"""

import argparse
import os
import sys

def escape_yaml_string(val: str) -> str:
    """Escapes backslashes and double quotes for YAML double-quoted string."""
    escaped = val.replace('\\', '\\\\').replace('"', '\\"')
    return f'"{escaped}"'

def main() -> None:
    parser = argparse.ArgumentParser(description="Add a new skill to skills.yaml")
    parser.add_argument("--name", required=True, help="Name of the skill")
    parser.add_argument("--icon", help="FontAwesome icon class (e.g. 'fas fa-terminal') (optional)")
    parser.add_argument("--logo", help="URL to a logo image (optional)")
    parser.add_argument("--url", help="Link to the skill's official website (optional)")
    parser.add_argument("--summary", required=True, help="Brief summary of your experience with the skill")
    parser.add_argument("--categories", help="Comma-separated list of categories (e.g. 'languages,tools') (optional)")

    args = parser.parse_args()

    file_path = "data/en/sections/skills.yaml"
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.", file=sys.stderr)
        sys.exit(1)

    # Read existing content
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Basic duplicate detection
    name_escaped = args.name.replace('"', '\\"')
    if f'name: "{name_escaped}"' in content or f'name: {args.name}' in content:
        print(f"Warning: Skill '{args.name}' might already exist in {file_path}.", file=sys.stderr)

    # Format categories list
    categories_list = []
    if args.categories:
        categories_list = [c.strip() for c in args.categories.split(",") if c.strip()]
    
    # Format YAML entry
    entry_lines = []
    
    # Ensure there is a newline at the end of the file before appending
    if content and not content.endswith("\n"):
        entry_lines.append("")
        
    entry_lines.append(f"  - name: {escape_yaml_string(args.name)}")
    if args.icon:
        entry_lines.append(f"    icon: {escape_yaml_string(args.icon)}")
    if args.logo:
        entry_lines.append(f"    logo: {escape_yaml_string(args.logo)}")
    if categories_list:
        categories_str = ", ".join(f'"{c}"' for c in categories_list)
        entry_lines.append(f"    categories: [{categories_str}]")
    else:
        entry_lines.append("    categories: []")
    if args.url:
        entry_lines.append(f"    url: {escape_yaml_string(args.url)}")
    entry_lines.append(f"    summary: {escape_yaml_string(args.summary)}")
    
    entry_lines.append("") # Final empty line to separate entries

    entry = "\n".join(entry_lines)

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(entry)

    print(f"Successfully added skill '{args.name}' to {file_path}")

if __name__ == "__main__":
    main()
