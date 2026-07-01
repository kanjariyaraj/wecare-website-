# Automated Commit Loop Setup Instructions

This repository contains a Python script and a GitHub Actions workflow to automate a specific 5-day cycle of commits:
- Day 1: 2 commits
- Day 2: 4 commits
- Day 3: 1 commit
- Day 4: 5 commits
- Day 5: 7 commits

The cycle repeats indefinitely. The script works by modifying `commit_log.txt` to create genuine changes, and tracks its position in the cycle using `state.json`.

## Deployment Instructions

1. **Commit these files to your repository:**
   Ensure the following files are pushed to the `main` branch of your repository:
   - `auto_commit.py`
   - `state.json`
   - `commit_log.txt`
   - `.github/workflows/auto_commit.yml`
   - `INSTRUCTIONS.md`

2. **Configure Workflow Permissions in GitHub:**
   For the GitHub Action to be able to push commits back to your repository, you must grant it write permissions.
   - Go to your repository on GitHub.
   - Click on **Settings**.
   - In the left sidebar, click on **Actions** > **General**.
   - Scroll down to the **Workflow permissions** section.
   - Select **Read and write permissions**.
   - Click **Save**.

3. **Verify the Action (Optional but recommended):**
   - The workflow is configured with a `workflow_dispatch` trigger, meaning you can run it manually.
   - Go to the **Actions** tab in your repository.
   - Select the **Automated Commit Loop** workflow on the left.
   - Click the **Run workflow** dropdown on the right and click the green **Run workflow** button.
   - Wait for the job to complete and check that new commits were pushed to your `main` branch.

## How it works locally

If you run the script locally using `python auto_commit.py`, it will:
1. Read `state.json` to determine how many commits to make.
2. Modify `commit_log.txt` for each commit and create a commit using `git commit`.
3. Update `state.json` to the next day's index *only* on the final commit of the day.
4. **Skip pushing.** It detects it's not running in CI and won't execute `git push`, allowing you to inspect the local commits without messing up your remote repository.
