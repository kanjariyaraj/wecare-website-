# Auto Commit Automation

This repository contains an automated script and GitHub Actions workflow designed to make daily commits following a specific loop pattern:

- **Day 1**: 2 commits
- **Day 2**: 4 commits
- **Day 3**: 1 commit
- **Day 4**: 5 commits
- **Day 5**: 7 commits
- **Loop resets to Day 1**

## Files Included

1. **`auto_commit.py`**: The core Python script that reads the state, calculates how many commits to make, updates `commit_log.txt`, and pushes changes.
2. **`state.json`**: A JSON file used to track the current day in the loop (1 through 5).
3. **`commit_log.txt`**: The file where new random log lines are appended. This provides the required file modification for Git to detect a change.
4. **`.github/workflows/auto_commit.yml`**: The GitHub Actions workflow file that runs `auto_commit.py` daily on a cron schedule.

## How to Deploy / Setup

The automation is designed to work out of the box when pushed to a GitHub repository, but you should ensure the following requirements are met:

1. **Push to GitHub**: Commit these files (`auto_commit.py`, `state.json`, `commit_log.txt`, and `.github/workflows/auto_commit.yml`) and push them to your repository's default branch (e.g., `main`).
2. **Permissions Settings**:
   - Ensure GitHub Actions has read and write permissions to the repository.
   - In your GitHub repo, go to **Settings > Actions > General**.
   - Under **Workflow permissions**, ensure **"Read and write permissions"** is selected. Check the box to allow actions to create and approve pull requests if needed, and save.
3. **Verify Action**:
   - Go to the **Actions** tab in your repository.
   - You can manually trigger the workflow by selecting the **"Daily Auto Commit"** workflow on the left, clicking **"Run workflow"**, and clicking the green Run workflow button.

## Running Locally

If you want to run the script manually on your local machine:

1. Ensure you have Python installed.
2. Ensure Git is configured with your user name and email (the script handles basic defaults if missing).
3. Open a terminal and navigate to the repository root.
4. Run the script:
   ```bash
   python auto_commit.py
   ```
5. The script will read `state.json`, determine the number of commits, modify `commit_log.txt`, commit the changes, update `state.json` for the next run, and push to the remote branch.