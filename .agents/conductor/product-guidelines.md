# Product Guidelines - Personal Profile Website

These guidelines govern the content, design, and user experience standards for the personal profile website.

## 1. Prose & Tone Style
- **Tone**: Professional, inviting, authentic, and clear. Avoid overly verbose descriptions.
- **Perspective**: Written primarily in the first person ("I", "my") for personal bio/about/projects, but third person is acceptable where appropriate (e.g., formal references or citations).
- **Formatting**: Use clean Markdown. Always use standard headings, list formats, and code blocks. Keep sentences and paragraphs short for readability.

## 2. Branding & Visual Design
- **Theme**: Stick to the Toha theme's core aesthetics, which feature clean grids, circular avatars, and professional timeline visuals.
- **Typography**: Primary font family should be clean and readable (Mulish is default for Toha).
- **Color Palette**: Use standard light/dark modes with accessible contrast ratios. Accent colors should be professional (e.g., slate, navy blue, teal) and consistent.
- **Assets**: All images (avatar, backgrounds) must be high quality and optimized for web delivery.

## 3. User Experience (UX) & UI
- **Mobile First**: Design content layouts to render beautifully on mobile devices, tablets, and desktops.
- **Accessibility (a11y)**:
  - Provide descriptive alternative text (`alt` attribute) for all images.
  - Ensure correct heading hierarchy (e.g., `h1` -> `h2` -> `h3`).
  - Keep interactive elements easily clickable on touchscreens.
- **Performance**: Minimize heavy JS/CSS bundles. Keep the total page load time under 2 seconds.

## 4. Content Maintenance Guidelines
- **Data Integrity**: Store section content within YAML data files (`data/en/sections/*.yaml`) to separate content structure from the presentation layer.
- **Link Integrity**: Avoid broken links. Check external references (e.g., social links, GitHub projects) regularly.
