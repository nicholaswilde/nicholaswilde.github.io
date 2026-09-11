---
name: add-skill
description: Guides the agent on how to add a new skill to the portfolio skills list
---
## 1.0 SYSTEM DIRECTIVE
You are an AI coding assistant. Your task is to guide the user or proceed with adding a skill to Nicholas Wilde's personal portfolio. You must follow the instructions below to ensure data integrity and layout consistency.

---

## 2.0 DATA SCHEMA FOR SKILLS
All skills are stored in `data/en/sections/skills.yaml`.

### 2.1 Skill Entry Structure
Each skill entry under the `skills:` list should adhere to the following schema:

```yaml
- name: "Skill Name"                  # String: Name of the skill (display name)
  icon: "fas fa-terminal"             # String: (Optional) FontAwesome icon class
  logo: "url-to-logo"                 # String: (Optional) URL to logo image (use either icon or logo)
  url: "https://..."                  # String: (Optional) Link to official website or documentation
  summary: "Brief experience summary" # String: 1-2 sentence description of proficiency/experience
  categories: ["languages", "tools"]  # Array of Strings: Category tags for filtering
```

### 2.2 Adding a Skill Category and Button
1. Check the `categories` specified in the new skill.
2. Verify if these categories are present under the `buttons:` list in `data/en/sections/skills.yaml`.
3. If a category is not present, add a corresponding button configuration under `buttons:`:
   ```yaml
   - name: Category Name Display
     filter: "category-filter"
   ```

---

## 3.0 AUTOMATED ADDITION VIA TASK / SCRIPT
You can use the automated Python script or Taskfile task to append a new skill to `data/en/sections/skills.yaml`.

### 3.1 Using the Task (Recommended)
Run the following command from the root of the repository:
```bash
task add-skill -- --name="Skill Name" --summary="Brief description of experience." --categories="languages,tools"
```

### 3.2 Supported Arguments
The script/task supports the following command-line arguments:
* `--name`: (Required) Display name of the skill.
* `--summary`: (Required) Brief summary of your experience with the skill.
* `--icon`: (Optional) FontAwesome icon class (e.g., `fas fa-robot`).
* `--logo`: (Optional) URL to a logo image (use either `--icon` or `--logo`).
* `--url`: (Optional) Link to the skill's official website.
* `--categories`: (Optional) Comma-separated list of categories (e.g., `languages,tools`).

---

## 4.0 VERIFICATION STEPS
After modifying `data/en/sections/skills.yaml`, you must run validation and check quality gates:

1. **Syntax Check:** Ensure the YAML file compiles correctly.
2. **Build Test:** Build the Hugo site to verify it compiles:
   ```bash
   hugo --minify
   ```
3. **Verify Links:** Check that the newly added `url` links are valid and active.
