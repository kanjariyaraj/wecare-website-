# Deployment Instructions for Auto Commit Setup

Here are step-by-step instructions on how to deploy this auto-commit script and GitHub Actions workflow to your repository:

## 1. Prepare your Repository
1. Ensure your repository is created on GitHub.
2. The default branch is assumed to be `main`. If yours is `master`, update the push command in the `auto_commit.py` script.

## 2. Add the Files
1. Add `auto_commit.py` to the root of your repository.
2. Create the `.github/workflows` directories if they don't exist, and add the `auto_commit.yml` file inside:
   `.github/workflows/auto_commit.yml`
3. Optional: Create an empty `commit_log.txt` file and a `state.json` file with `{"day": 1}`. If you don't, the script will create them automatically on the first run.

## 3. Commit and Push
1. Stage these new files:
   ```bash
   git add auto_commit.py .github/workflows/auto_commit.yml
   ```
2. Commit them to your repository:
   ```bash
   git commit -m "Setup auto-commit loop script and workflow"
   ```
3. Push to your GitHub repository.

## 4. Configure GitHub Actions Permissions
By default, GitHub Actions might not have permission to push changes back to your repository.
1. Go to your repository on GitHub.
2. Click on **Settings**.
3. In the left sidebar, click on **Actions** > **General**.
4. Scroll down to **Workflow permissions**.
5. Select **Read and write permissions**.
6. Click **Save**.

*(Note: The workflow file `auto_commit.yml` also explicitly sets `permissions: contents: write`, which is best practice.)*

## 5. Test the Automation
You don't have to wait until midnight to test it!
1. Go to your repository on GitHub.
2. Click on the **Actions** tab.
3. In the left sidebar, click on the **Auto Commit Loop** workflow.
4. On the right side, click the **Run workflow** dropdown, and then click the **Run workflow** button.
5. Watch the action run. Once it finishes, go to your repository's code and check that `commit_log.txt` and `state.json` were created/updated, and that there are new commits in your history.

## How it works
- The GitHub Action runs every day at 00:00 UTC.
- It executes `auto_commit.py`.
- The script reads the `state.json` file to check the current day (1-5).
- It makes the correct number of commits (Day 1: 2, Day 2: 4, Day 3: 1, Day 4: 5, Day 5: 7).
- Each commit appends a random string to `commit_log.txt`.
- On the final commit of the day, it updates `state.json` to the next day in the loop.
- It then pushes all the commits to the `main` branch.
