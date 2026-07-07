# GitHub Auto-Commit Automation Setup Instructions

This guide provides step-by-step instructions on how to set up the automated commit script in your GitHub repository. The script follows a strict 5-day cycle of 2, 4, 1, 5, and 7 commits per day.

## Files Created

1. **`state.json`**: This file tracks the current day of the 5-day commit cycle (starts at index 0).
2. **`commit_log.txt`**: This file is created and updated by the script. It appends a timestamp and random string to ensure each commit contains a unique, verifiable change.
3. **`auto_commit.py`**: The core Python script that handles the logic, configures Git, makes the commits, updates the state file, and pushes the changes.
4. **`.github/workflows/auto_commit.yml`**: The GitHub Actions workflow file that runs the Python script automatically every day.

## Setup Instructions

### 1. Ensure Files are in Your Repository
Ensure that all the files listed above are present in your main repository branch.

### 2. Configure Repository Permissions
By default, GitHub Actions workflows might not have permission to push changes back to the repository. To fix this, you must grant write permissions to the `GITHUB_TOKEN`:

1. Go to your repository on GitHub.
2. Click on the **Settings** tab.
3. On the left sidebar, expand the **Actions** menu and select **General**.
4. Scroll down to the **Workflow permissions** section.
5. Select the **Read and write permissions** option.
6. Click **Save**.

### 3. (Optional) Run the Action Manually
The GitHub Action is scheduled to run daily at 12:00 UTC. However, you can also run it manually to test the setup.

1. Go to the **Actions** tab in your repository.
2. Under "All workflows", click on **Automated Commits**.
3. Click the **Run workflow** dropdown button on the right.
4. Click **Run workflow**.

## How the Logic Works
- The `state.json` tracks which day index the loop is on (0 to 4).
- The array `[2, 4, 1, 5, 7]` determines the exact number of commits to make for the current day.
- For each loop execution, the script appends to `commit_log.txt` to register genuine file changes.
- To avoid disrupting the exact commit count rules, the final update to `state.json` for the next day's index is deliberately staged and included as part of the *final commit* of the day.
- Finally, the script executes `git push origin HEAD:main` to push all the commits directly to the `main` branch.
