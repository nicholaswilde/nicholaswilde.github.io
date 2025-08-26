# Profile

My [profile page](https://nicholaswilde.io/).

---

## :gear: Config

Update files in the `data/en` folder to modify the site.

---

## Build and Serve

This project is a Hugo site using the Toha theme. Here are the instructions for building and serving it:

### Local Development Server

You can run a local development server using the following methods:

1.  **Using Docker:**
    ```bash
    docker run -it --rm -v "${PWD}":/src hugomods/hugo server -w --bind=0.0.0.0
    ```
2.  **Using a local Hugo installation:**
    ```bash
    hugo server --theme toha --watch --bind=0.0.0.0
    ```

### Building for Deployment

To build the site for deployment, follow these steps:

1.  **Tidy Hugo modules:**
    ```bash
    hugo mod tidy
    ```
2.  **Install npm dependencies:**
    ```bash
    npm install
    ```
3.  **Build the Hugo site with minification:**
    ```bash
    hugo --minify
    ```

---

## :balance_scale:&nbsp; License

[Apache 2.0 License](./LICENSE)

---

## :pencil:&nbsp; Author

This project was started in 2021 by [Nicholas Wilde].

[Nicholas Wilde]: https://github.com/nicholaswilde/
