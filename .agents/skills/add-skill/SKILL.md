---
name: add-skill
description: Guides the agent on how to add a new skill to the portfolio skills list
---
## 1.0 SYSTEM DIRECTIVE
You are an AI coding assistant. Your task is to add or guide the agent in adding a skill to Nicholas Wilde's personal portfolio. You must follow the instructions below to ensure data integrity, layout consistency, and that validation tests pass.

---

## 2.0 DATA SCHEMA FOR SKILLS
All skills are stored in `data/en/sections/skills.yaml`.

### 2.1 Skills Section Structure
The document has a `section` header, a list of filter buttons under `buttons`, and a flat list of items under `skills`:

```yaml
section:
  name: Skills
  id: skills
  enable: true
  weight: 2
  showOnNavbar: true
  filter: true

buttons:
  - name: "All"
    filter: "all"
  - name: "Category Display Name"
    filter: "category-id"

skills:
  - name: "Skill Name"             # String: Display name of the skill (e.g. Python, Git)
    icon: "fab fa-python"          # String: FontAwesome icon class (e.g., fab fa-golang, fas fa-robot)
    categories: ["category-id"]    # Array of Strings: Category ID filters matching a button filter
    url: "https://example.com/"    # String: Link to the official website of the skill
    summary: "Skill summary."      # String: Brief description of proficiency and experience
```

### 2.2 Adding a Skill
1. Locate `data/en/sections/skills.yaml`.
2. Determine which category/categories the skill belongs to (e.g., `languages`, `devops`, `tools`).
3. If a new category filter is required:
   - Add it to the `buttons` list under the root of the file, specifying its `name` and `filter` (lowercase identifier).
4. Append the new skill to the flat `skills` list using the following keys:
   - `name`: The skill's display name.
   - `icon`: The FontAwesome class (e.g., `fab fa-...` or `fas fa-...`).
   - `categories`: An inline array containing the category string filter ID (e.g., `["languages"]`).
   - `url`: The URL to the official website of the tool/language.
   - `summary`: A concise, professional description of experience with the skill.
   - **Do NOT add a `logo` field.** (Use `icon` instead of `logo` to maintain site consistency unless specifically instructed otherwise).

---

## 3.0 VERIFICATION STEPS
After modifying `data/en/sections/skills.yaml`, you must run validation and build checks:

1. **Run Validation Script:** Run the python validation test to ensure the schema is correct:
   ```bash
   python3 scripts/test_skills.py
   ```
2. **Task lint:** Run the lint task to verify yamllint and validation checks pass:
   ```bash
   task lint
   ```
3. **Build Test:** Build the Hugo site to verify it compiles without template errors:
   ```bash
   hugo
   ```
