# Technology Stack - Personal Profile Website

This document outlines the technologies, tools, and build setup used for this project.

## Core Technologies
- **Static Site Generator**: [Hugo](https://gohugo.io/) (extended version recommended for asset processing, version 1.21 or higher specified in `go.mod`).
- **Theme**: [Toha Theme](https://themes.gohugo.io/themes/toha/) (v4), managed via Hugo Modules.

## Dependency Management
- **Hugo Modules**: Used to fetch and manage the Toha theme.
- **npm / Node.js**: Used to manage and install front-end dependencies and build tooling (defined in `package.json`).

## Frontend Frameworks & Libraries
- **Styling**: Bootstrap 5 (integrated via SCSS styling).
- **Icons**: FontAwesome 6, Feather Icons, Flag Icons.
- **Interactions**:
  - **itpyed**: For typing animations in the banner.
  - **Katex**: For LaTeX mathematical expression rendering.
  - **Mermaid**: For diagrams and flowcharts.
  - **Plyr**: For custom video/audio player support.
  - **Fuse.js**: For client-side search.
  - **Highlight.js**: For code syntax highlighting.

## Build & Asset Processing
- **PostCSS & Autoprefixer**: Used for processing, vendor-prefixing, and minifying CSS/SCSS styles.
- **Taskfile**: Configured via `Taskfile.yaml` to define local development and build commands.

## Development Quality Assurance
- **Pre-commit Hooks**: Defined in `.pre-commit-config.yaml` to enforce code and format formatting before commits.
- **Linter**: ESLint for Javascript, Yamllint for YAML files.

## Hosting & CI/CD
- **GitHub Actions**: Deploys the static site to GitHub Pages automatically upon pushes to the source branch.
