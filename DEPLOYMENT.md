# Deploying Watch Together

This guide provides step-by-step instructions to deploy your backend to **Render** and your frontend to **GitHub Pages**.

## Prerequisites
1. You need a [GitHub](https://github.com/) account.
2. You need a [Render](https://render.com/) account (you can sign in with GitHub).
3. If you haven't already, install [Git](https://git-scm.com/downloads) on your computer.

---

## Step 1: Push Your Code to GitHub

First, you need to turn your local project into a Git repository and push it to GitHub.

1. Create a new, empty repository on GitHub (e.g., named `watch-together`). Do **not** initialize it with a README, .gitignore, or license.
2. Open your VS Code terminal and make sure you are in the root directory `d:\watch-together`.
3. Run the following commands:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   # Replace <YOUR_USERNAME> with your actual GitHub username and <YOUR_REPO_NAME> with your new repo name
   git remote add origin https://github.com/<YOUR_USERNAME>/<YOUR_REPO_NAME>.git
   git push -u origin main
   ```

---

## Step 2: Deploy the Backend to Render

Now we'll deploy the `backend` folder as a Web Service on Render.

1. Go to your [Render Dashboard](https://dashboard.render.com/) and click **New +** > **Web Service**.
2. Select **"Build and deploy from a Git repository"** and connect the GitHub repository you just created.
3. In the configuration settings, fill out the following:
   * **Name:** Give your backend a name (e.g., `watch-together-backend`).
   * **Root Directory:** Type `backend` (very important!).
   * **Environment:** Python 3.
   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Select the **Free** instance type and click **Create Web Service**.
5. Wait a few minutes for the build to finish. Once it says "Live", copy the provided URL at the top left (it will look something like `https://watch-together-backend-xxxxx.onrender.com`).

---

## Step 3: Update Frontend Configuration

Now that you have a live backend URL, you need to point your frontend to it.

1. Open `frontend/index.html` in VS Code.
2. Find the constant on line 69:
   ```javascript
   const BACKEND_URL = "http://127.0.0.1:8000"; // Change this to your Render URL
   ```
3. Replace `"http://127.0.0.1:8000"` with your Render URL. **Make sure not to leave a trailing slash `/` at the end.**
   ```javascript
   const BACKEND_URL = "https://watch-together-backend-xxxxx.onrender.com";
   ```
4. Do the exact same thing in `frontend/script.js` on line 3:
   ```javascript
   const BACKEND_URL = "https://watch-together-backend-xxxxx.onrender.com";
   ```

---

## Step 4: Deploy the Frontend to GitHub Pages

Now that the frontend is configured with your live backend, let's push the update and publish it!

1. Commit your configuration changes:
   ```bash
   git add .
   git commit -m "Update BACKEND_URL for production"
   git push
   ```
2. Go to your repository on GitHub.
3. Click on the **Settings** tab at the top.
4. On the left sidebar, scroll down and click on **Pages**.
5. Under **Build and deployment**, find the **Source** section. Leave the dropdown as "Deploy from a branch".
6. Under **Branch**, select `main` and change the folder from `/ (root)` to `/frontend`, if GitHub allows.
   * *Note: GitHub Pages usually expects an `index.html` at the root. If you cannot select `/frontend`, simply move the contents of your `frontend` folder into the main repository root and commit those changes.*
   * Alternatively, if you want to leave it in the `frontend` folder, select `/ (root)`, hit **Save**, and your site will be available at `https://<YOUR_USERNAME>.github.io/<YOUR_REPO_NAME>/frontend/`.
7. Wait a couple of minutes, refresh the page, and GitHub will provide you with a link to your live site at the top of the Pages settings page!

Enjoy your live Watch Together app!
