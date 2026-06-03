---
name: add-project
description: Guides the agent on how to add a new project to the portfolio projects list
---
## 1.0 SYSTEM DIRECTIVE
You are an AI coding assistant. Your task is to guide the user or proceed with adding a project to Nicholas Wilde's personal portfolio. You must follow the instructions below to ensure data integrity and layout consistency.

---

## 2.0 DATA SCHEMA FOR PROJECTS
All projects are stored in `data/en/sections/projects.yaml`.

### 2.1 Project Entry Structure
Each project entry under the `projects:` list should adhere to the following schema:

```yaml
- name: "project-name"               # String: Name of the project (display name)
  role: "Owner"                       # String: Role in the project (e.g., Owner, Contributor, Lead)
  logo: "/images/custom-logo.png"     # String: (Optional) Path to project image under static directory
  repo: "https://github.com/.../..."   # String: (Optional) Link to project repository
  url: "https://..."                  # String: (Optional) Link to live demo or project home page
  timeline: "Month Year - Present"    # String: Timeline range (e.g. "Present", "June 2023 - Present")
  summary: "Brief project summary."   # String: 1-2 sentence description
  tags: ["hobby", "code"]             # Array of Strings: Category tags for filtering
```

### 2.2 Adding a Project Tag and Button
1. Check the `tags` specified in the new project.
2. Verify if these tags are present under the `buttons:` list in `data/en/sections/projects.yaml`.
3. If a tag is not present, add a corresponding button configuration under `buttons:`:
   ```yaml
   - name: Tag Name Display
     filter: "tag-name-filter"
   ```

---

## 3.0 VERIFICATION STEPS
After modifying `data/en/sections/projects.yaml`, you must run validation and check quality gates:

1. **Syntax Check:** Ensure the YAML file compiles correctly.
2. **Build Test:** If local tools are available, build the Hugo site:
   ```bash
   hugo --minify
   ```
3. **Verify Links:** Check that the newly added `repo` or `url` links are valid and active.
