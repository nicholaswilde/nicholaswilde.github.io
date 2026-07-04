#!/usr/bin/env python3
"""Script to automate adding a new project to projects.yaml.

This script appends a new project entry to the projects configuration file.
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
    parser = argparse.ArgumentParser(description="Add a new project to projects.yaml")
    parser.add_argument("--name", required=True, help="Name of the project")
    parser.add_argument("--role", default="Owner", help="Role in the project (default: Owner)")
    parser.add_argument("--logo", help="Path or icon class for project logo (optional)")
    parser.add_argument("--repo", help="Link to project repository (optional)")
    parser.add_argument("--url", help="Link to live demo/homepage (optional)")
    parser.add_argument("--timeline", default="Present", help="Timeline of the project (default: Present)")
    parser.add_argument("--summary", required=True, help="Brief summary of the project")
    parser.add_argument("--tags", help="Comma-separated list of tags (optional)")

    args = parser.parse_args()

    file_path = "data/en/sections/projects.yaml"
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.", file=sys.stderr)
        sys.exit(1)

    # Read existing content
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Basic duplicate detection
    name_escaped = args.name.replace('"', '\\"')
    if f'name: "{name_escaped}"' in content or f'name: {args.name}' in content:
        print(f"Warning: Project '{args.name}' might already exist in {file_path}.", file=sys.stderr)

    # Format tags list
    tags_list = []
    if args.tags:
        tags_list = [t.strip() for t in args.tags.split(",") if t.strip()]
    
    # Format YAML entry
    entry_lines = []
    
    # Ensure there is a newline at the end of the file before appending
    if content and not content.endswith("\n"):
        entry_lines.append("")
        
    entry_lines.append(f"  - name: {escape_yaml_string(args.name)}")
    entry_lines.append(f"    role: {escape_yaml_string(args.role)}")
    if args.logo:
        entry_lines.append(f"    logo: {escape_yaml_string(args.logo)}")
    if args.repo:
        entry_lines.append(f"    repo: {args.repo}")
    if args.url:
        entry_lines.append(f"    url: {args.url}")
    entry_lines.append(f"    timeline: {escape_yaml_string(args.timeline)}")
    entry_lines.append(f"    summary: {escape_yaml_string(args.summary)}")
    
    if tags_list:
        tags_str = ", ".join(f'"{tag}"' for tag in tags_list)
        entry_lines.append(f"    tags: [{tags_str}]")
    else:
        entry_lines.append("    tags: []")
    
    entry_lines.append("") # Final empty line to separate entries

    entry = "\n".join(entry_lines)

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(entry)

    print(f"Successfully added project '{args.name}' to {file_path}")

if __name__ == "__main__":
    main()
