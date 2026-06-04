#!/usr/bin/env python3
"""Validation script for Hugo Toha theme skills section configuration file.

This script verifies that the skills configuration file exists, is valid YAML, and
conforms to the schema expected by the Toha theme, including required categories
and specific skills. It uses a custom parser to avoid external library dependencies
like PyYAML.
"""

import os
import re
import sys
from typing import Dict, Any, List, Set


def log(status: str, message: str) -> None:
    """Logs a message with a specific status prefix.

    Args:
        status: The severity level (e.g., INFO, ERRO).
        message: The log message.
    """
    print(f"[{status}] {message}")


def parse_simple_yaml(content: str) -> Dict[str, Any]:
    """Parses a simple flat skills YAML file structure with categories.

    Args:
        content: The YAML file contents.

    Returns:
        A dictionary representing the parsed YAML structure.
    """
    data: Dict[str, Any] = {}
    lines = content.split("\n")

    current_section = None
    section_data: Dict[str, Any] = {}
    buttons_data: List[Dict[str, Any]] = []
    skills_data: List[Dict[str, Any]] = []

    current_button: Dict[str, Any] = {}
    current_skill: Dict[str, Any] = {}

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped == "---":
            continue

        indent = len(line) - len(line.lstrip(" "))

        if indent == 0:
            if stripped.endswith(":"):
                current_section = stripped[:-1].strip()
            continue

        if current_section == "section":
            parts = stripped.split(":", 1)
            if len(parts) == 2:
                k = parts[0].strip()
                v = parts[1].strip().strip('"').strip("'")
                if v.lower() == "true":
                    val: Any = True
                elif v.lower() == "false":
                    val = False
                else:
                    try:
                        val = int(v)
                    except ValueError:
                        val = v
                section_data[k] = val

        elif current_section == "buttons":
            if stripped.startswith("- "):
                current_button = {}
                buttons_data.append(current_button)
                stripped = stripped[2:].strip()
            parts = stripped.split(":", 1)
            if len(parts) == 2:
                k = parts[0].strip()
                v = parts[1].strip().strip('"').strip("'")
                current_button[k] = v

        elif current_section == "skills":
            if stripped.startswith("- ") and indent == 2:
                current_skill = {"categories": []}
                skills_data.append(current_skill)
                stripped = stripped[2:].strip()
            
            parts = stripped.split(":", 1)
            if len(parts) == 2:
                k = parts[0].strip()
                v = parts[1].strip().strip('"').strip("'")
                if k != "categories":
                    current_skill[k] = v
                else:
                    match = re.match(r'^\[(.*)\]$', v)
                    if match:
                        items = [x.strip().strip('"').strip("'") for x in match.group(1).split(",")]
                        current_skill["categories"].extend([x for x in items if x])
            elif stripped.startswith("-") and indent == 6:
                cat_val = stripped[1:].strip().strip('"').strip("'")
                current_skill["categories"].append(cat_val)

    data["section"] = section_data
    data["buttons"] = buttons_data
    data["skills"] = skills_data
    return data


def test_skills_config() -> bool:
    """Validates the skills.yaml configuration file.

    Returns:
        True if the configuration is valid and meets all requirements,
        False otherwise.
    """
    file_path = "data/en/sections/skills.yaml"

    # 1. Verify file existence
    if not os.path.exists(file_path):
        log("ERRO", f"File does not exist: {file_path}")
        return False

    # 2. Parse YAML content
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            data = parse_simple_yaml(content)
    except Exception as e:
        log("ERRO", f"Failed to parse YAML file: {e}")
        return False

    if not data:
        log("ERRO", "YAML configuration file is empty or could not be parsed")
        return False

    # 3. Verify section configuration
    section: Dict[str, Any] = data.get("section", {})
    if not section:
        log("ERRO", "Missing 'section' configuration block")
        return False

    required_section_keys: List[str] = ["name", "id", "enable", "weight"]
    for key in required_section_keys:
        if key not in section:
            log("ERRO", f"Missing required key '{key}' in section config")
            return False

    if section["id"] != "skills":
        log("ERRO", f"Expected section id to be 'skills', got '{section['id']}'")
        return False

    # 4. Verify skills list
    skills: List[Dict[str, Any]] = data.get("skills", [])
    if not skills:
        log("ERRO", "Missing 'skills' configuration list")
        return False

    categories: Set[str] = set()
    skill_names: List[str] = []

    for idx, skill in enumerate(skills):
        if "name" not in skill:
            log("ERRO", f"Skill at index {idx} is missing required field 'name'")
            return False
        skill_names.append(skill["name"])
        for cat in skill.get("categories", []):
            categories.add(cat)

    # Verify required categories are present
    expected_categories: Set[str] = {
        "languages",
        "devops",
        "tools",
    }
    missing_categories: Set[str] = expected_categories - categories
    if missing_categories:
        log("ERRO", f"Missing required categories in skills: {missing_categories}")
        return False

    # Verify required skills are present
    expected_skills: Set[str] = {
        "Bash",
        "Git",
        "Kubernetes",
    }
    missing_skills: Set[str] = expected_skills - set(skill_names)
    if missing_skills:
        log("ERRO", f"Missing required skills: {missing_skills}")
        return False

    log("INFO", "Validation passed successfully!")
    return True


def main() -> None:
    """Main execution function."""
    if test_skills_config():
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()

