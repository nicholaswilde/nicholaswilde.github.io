# Project Overview

This project is a personal profile website built using the [Hugo](https://gohugo.io/) static site generator and the [Toha](https://themes.gohugo.io/themes/toha/) theme. It leverages Hugo Modules for theme management and Node.js/npm for handling front-end dependencies and asset processing.

# Building and Running

## Dependencies

To build and run this project, you will need:

*   **Hugo (extended version):** The static site generator.
*   **Node.js and npm:** For managing front-end dependencies.

## Build Commands (for deployment)

The following sequence of commands is used to build the site for deployment, as observed in the GitHub Actions workflow:

1.  Initialize and clean up Hugo modules:
    ```bash
    hugo mod tidy
    ```
2.  Prepare `package.json` for npm dependencies from Hugo modules:
    ```bash
    hugo mod npm pack
    ```
3.  Install Node.js dependencies:
    ```bash
    npm install
    ```
4.  Build the Hugo site with minification:
    ```bash
    hugo --minify
    ```

## Local Development Server

You can run a local development server using the following methods, as defined in `Taskfile.yaml`:

*   **Using Docker:**
    ```bash
    docker run -it --rm -v "${PWD}":/src hugomods/hugo server -w
    ```
*   **Using a local Hugo installation:**
    ```bash
    hugo server -w
    ```

# Development Conventions

*   **Hugo Structure:** The project follows the standard Hugo directory structure for content, layouts, and static assets.
*   **Hugo Modules:** The Toha theme and potentially other components are managed as Hugo Modules.
*   **Node.js/npm:** Used for managing JavaScript and CSS dependencies, as well as for asset compilation (e.g., PostCSS).
*   **Taskfile:** Common development tasks (like serving the site) are defined in `Taskfile.yaml`.
*   **Pre-commit Hooks:** The presence of `.pre-commit-config.yaml` suggests that pre-commit hooks are used to enforce code quality and formatting standards.

# Data Files

*   `data/en/sections/projects.yaml`: This file houses the project data displayed on the website, primarily detailing projects related to Nicholas Wilde's GitHub repositories.
