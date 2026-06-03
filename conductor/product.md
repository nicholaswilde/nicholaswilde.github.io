# Product Guide - Personal Profile Website

## Vision
A premium, highly performant personal profile and portfolio website that showcases Nicholas Wilde's professional experience, skills, projects, and contributions. The website is built using the Hugo static site generator and the Toha theme, offering a clean, modern, and responsive user experience.

## Target Audience
- Recruiters and potential employers looking for professional history and skills.
- Developers and collaborators interested in open-source projects and GitHub repositories.
- Peers and community members in the software development space.

## Key Features & Sections
- **Hero/Banner**: Dynamic introduction with background image, profile photo, and interactive typing effect (ityped).
- **About Section**: High-level bio and introduction of Nicholas Wilde.
- **Experience**: Timeline of professional career history, highlighting key responsibilities and achievements.
- **Skills**: Structured presentation of technical skills (languages, frameworks, tools) categorized by proficiency or type.
- **Projects**: Showcase of personal and open-source projects, linking to GitHub repositories and demo sites (sourced from `data/en/sections/projects.yaml`).
- **Contact Info**: Links to professional profiles (GitHub, LinkedIn, Email) and contact form or links.

## Product Architecture & Content Management
- **Static Site Generation**: Fully compiled static HTML/CSS/JS files for ultra-fast loading and SEO.
- **Data-Driven Configuration**: Sections and content are managed as structured YAML files in `data/en/sections/` to separate content from design/code.
- **Theme Customization**: Using Hugo Modules to import and manage the Toha theme, allowing clean updates and extension.
