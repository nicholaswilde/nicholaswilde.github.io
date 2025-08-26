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

### :laoptop: Local Development Server

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

1.  **Install theme:**
    ```bash
    hugo mod get -u github.com/hugo-toha/toha/v4
    ```
    
2.  **Tidy Hugo modules:**
    ```bash
    hugo mod tidy
    ```
3.  **Install npm dependencies:**
    ```bash
    npm install
    ```
4.  **Build the Hugo site with minification:**
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
