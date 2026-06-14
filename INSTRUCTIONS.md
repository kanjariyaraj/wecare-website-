# Automated Commit Loop Setup

This repository contains an automated script and GitHub Actions workflow to generate daily commits following a specific 5-day cycle:
- Day 1: 2 commits
- Day 2: 4 commits
- Day 3: 1 commit
- Day 4: 5 commits
- Day 5: 7 commits
(The loop resets to Day 1 after Day 5)

## Files Created
- `auto_commit.py`: The Python script that handles git configuration, figures out the current day, appends to the log, stages files, and makes commits.
- `state.json`: A simple JSON file tracking the current day of the loop.
- `commit_log.txt`: A text file appended with a new timestamp and random string for every commit to ensure a real file change.
- `.github/workflows/auto_commit.yml`: The GitHub Actions workflow file that runs `auto_commit.py` daily via cron.

## Step-by-Step Deployment Guide

1. **Commit the Files**
   Ensure `auto_commit.py`, `state.json`, `commit_log.txt`, and `.github/workflows/auto_commit.yml` are committed and pushed to the default branch (e.g., `main` or `master`) of your repository.

2. **Verify Repository Permissions**
   By default, GitHub Actions may have restricted permissions. You must ensure the workflow has permission to push commits to your repository:
   - Go to your repository **Settings**.
   - Navigate to **Actions** > **General** on the left sidebar.
   - Scroll down to the **Workflow permissions** section.
   - Select **Read and write permissions**.
   - Click **Save**.

3. **Test the Automation Manually**
   The workflow is configured with `workflow_dispatch`, meaning you can trigger it manually to test.
   - Go to the **Actions** tab in your repository.
   - Click on the **Automated Commit Loop** workflow on the left side.
   - Click the **Run workflow** dropdown button on the right side.
   - Select the branch (e.g., `main`) and click **Run workflow**.
   - Once it runs, you should see new commits pushed to your repository, and `state.json` will be updated to the next day automatically on the final commit of the run.

4. **Let it Run**
   The workflow is also set with a cron schedule (`0 12 * * *`), which means it will run automatically every day at 12:00 UTC. No further action is required.
