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
    """Parses a simple skills YAML file structure.

    Args:
        content: The YAML file contents.

    Returns:
        A nested dictionary representing the parsed YAML structure.
    """
    data: Dict[str, Any] = {}
    lines = content.split("\n")

    current_key = None
    section_data: Dict[str, Any] = {}
    skills_data: List[Dict[str, Any]] = []

    current_category: Dict[str, Any] = {}
    current_item: Dict[str, Any] = {}

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped == "---":
            continue

        indent = len(line) - len(line.lstrip(" "))

        # Match list items like "- name: Programming Languages" or "- name: Python"
        if stripped.startswith("- "):
            list_stripped = stripped[2:].strip()
            list_match = re.match(r"^([^:]+):\s*(.*)$", list_stripped)
            if list_match:
                k = list_match.group(1).strip()
                v = list_match.group(2).strip().strip('"').strip("'")
                if indent == 2:
                    current_category = {"name": v, "items": []}
                    skills_data.append(current_category)
                elif indent == 6:
                    current_item = {"name": v}
                    if "items" in current_category:
                        current_category["items"].append(current_item)
            continue

        # Match key-value pairs like "section:" or "weight: 2"
        match = re.match(r"^([^:]+):\s*(.*)$", stripped)
        if not match:
            continue

        k = match.group(1).strip()
        v = match.group(2).strip().strip('"').strip("'")

        if indent == 0:
            current_key = k
            if k == "section":
                data["section"] = section_data
            elif k == "skills":
                data["skills"] = skills_data
        elif indent == 2:
            if current_key == "section":
                # Convert types
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
        elif indent == 8:
            if current_item is not None:
                # Convert types
                if v.lower() == "true":
                    val = True
                elif v.lower() == "false":
                    val = False
                else:
                    try:
                        val = int(v)
                    except ValueError:
                        val = v
                current_item[k] = val

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
            log("ERRO", f"Skill category at index {idx} is missing required field 'name'")
            return False

        category_name: str = skill["name"]
        categories.add(category_name)
        
        items = skill.get("items", [])
        if not isinstance(items, list):
            log(
                "ERRO",
                f"Category '{category_name}' has 'items' which is not a list",
            )
            return False
            
        for item_idx, item in enumerate(items):
            if "name" not in item:
                log(
                    "ERRO",
                    f"Item at index {item_idx} in category '{category_name}' "
                    f"must contain 'name'",
                )
                return False
            skill_names.append(item["name"])

    # Verify required categories are present
    expected_categories: Set[str] = {
        "Programming Languages",
        "DevOps & CI/CD",
        "Frameworks & Tools",
    }
    missing_categories: Set[str] = expected_categories - categories
    if missing_categories:
        log("ERRO", f"Missing required categories: {missing_categories}")
        return False

    # Verify required skills are present
    expected_skills: Set[str] = {
        "Python",
        "Go",
        "Bash",
        "Hugo",
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
