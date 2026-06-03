# :man: Profile
[![task](https://img.shields.io/badge/Task-Enabled-brightgreen?style=for-the-badge&logo=task&logoColor=white)](https://taskfile.dev/#/)
[![docs](https://img.shields.io/github/actions/workflow/status/nicholaswilde/nicholaswilde.github.io/deploy.yaml?label=deploy&style=for-the-badge&branch=source)](https://github.com/nicholaswilde/nicholaswilde.github.io/actions/workflows/deploy.yaml)

My [profile page](https://nicholaswilde.io/).

---

## :gear: Config

Update files in the `data/en` folder to modify the site.

---

## :hammer: Build and Serve

This project is a Hugo site using the Toha theme. Here are the instructions for building and serving it:

### :laptop: Local Development Server

You can run a local development server using the following methods:

1.  **Using Docker:**
    ```bash
    docker run -it --rm -v "${PWD}":/src hugomods/hugo server -w
    ```
2.  **Using a local Hugo installation:**
    ```bash
    hugo server --watch
    ```

### :building_construction: Building for Deployment

To build the site for deployment, follow these steps:

1.  **Bootstrap dependencies:**
    You can automatically initialize Hugo modules, pack dependency descriptors, and install NPM dependencies (including the cytoscape workaround) by running:
    ```bash
    task bootstrap
    ```

    *(Alternatively, you can run the steps manually:)*
    ```bash
    hugo mod get -u github.com/hugo-toha/toha/v4
    hugo mod tidy
    hugo mod npm pack
    npm install
    npm install cytoscape@3.30.2 --save-dev
    ```

2.  **Build the Hugo site with minification:**
    ```bash
    hugo --minify
    ```

---

## :balance_scale: License

[Apache 2.0 License](./LICENSE)

---

## :pencil: Author

This project was started in 2021 by [Nicholas Wilde].

[Nicholas Wilde]: https://github.com/nicholaswilde/
