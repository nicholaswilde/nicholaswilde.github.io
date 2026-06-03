---
name: add-skill
description: Guides the agent on how to add a new skill to the portfolio skills list
---
## 1.0 SYSTEM DIRECTIVE
You are an AI coding assistant. Your task is to guide the user or proceed with adding a skill to Nicholas Wilde's personal portfolio. You must follow the instructions below to ensure data integrity, layout consistency, and that validation tests pass.

---

## 2.0 DATA SCHEMA FOR SKILLS
All skills are stored in `data/en/sections/skills.yaml`.

### 2.1 Skills Section Structure
The document has a `section` header and a list of categories under `skills`:

```yaml
section:
  name: Skills
  id: skills
  enable: true
  weight: 2
  showOnNavbar: true

skills:
  - name: "Category Name"          # String: Name of the category (e.g. Programming Languages, DevOps & CI/CD)
    items:
      - name: "Skill Name"         # String: Display name of the skill (e.g. Python, Git)
        percentage: 90             # Integer: Proficiency percentage (e.g., 50 to 100)
        icon: "fab fa-python"      # String: (Optional) FontAwesome icon class
        logo: "/images/logo.png"   # String: (Optional) Path to custom image under static/
```

### 2.2 Adding a Skill
1. Locate the correct category under `skills` in `data/en/sections/skills.yaml`.
2. If the category does not exist, create it with a new `- name: "Category Name"` block and an empty `items:` list.
3. Append the new skill to the `items` list under the target category using the schema format.
4. Choose an appropriate visual helper:
   * **FontAwesome Icon (`icon`):** Find standard classes (e.g. `fab fa-golang`, `fas fa-terminal`).
   * **Image Logo (`logo`):** Place image assets in the `static/` folder and link to them.

---

## 3.0 VERIFICATION STEPS
After modifying `data/en/sections/skills.yaml`, you must run validation and build checks:

1. **Run Validation Script:** Run the python validation test to ensure the schema is correct and all required categories/skills are intact:
   ```bash
   python3 scripts/test_skills.py
   ```
2. **Task lint:** Alternatively, run `task lint` if configured.
3. **Build Test:** Build the Hugo site with minification:
   ```bash
   hugo --minify
   ```
