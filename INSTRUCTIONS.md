# Auto Commit Automation Instructions

This repository contains an automated script that creates commits in a specific daily pattern:
- Day 1: 2 commits
- Day 2: 4 commits
- Day 3: 1 commit
- Day 4: 5 commits
- Day 5: 7 commits

The loop automatically resets after Day 5 and continues indefinitely.

## Files Included

1. **`auto_commit.py`**: The core Python script that handles the logic. It reads `state.json` to know the current day, appends to `commit_log.txt` the required number of times for that day, stages the files, and creates distinct commits for each iteration. It pushes the result back to the origin.
2. **`.github/workflows/auto_commit.yml`**: The GitHub Actions workflow file that automatically runs `auto_commit.py` every day at 12:00 PM UTC. It gives the workflow write permissions to push the commits.
3. **`state.json`** (Created dynamically): A small state file that tracks the current day index (0-4). The auto-commit script stages and commits this file on the final commit of each day.
4. **`commit_log.txt`** (Created dynamically): The tracker log file modified to trigger Git changes.

## Prerequisites and Setup

1. **Commit these files to `main`**: Ensure `auto_commit.py` and `.github/workflows/auto_commit.yml` are pushed to your default branch (e.g., `main`).
2. **GitHub Actions Permissions**:
   - Go to your repository settings on GitHub.
   - Navigate to **Settings** > **Actions** > **General**.
   - Under **Workflow permissions**, ensure **Read and write permissions** is selected. This allows the GitHub Action to push the new commits back to the repository.

## How to Test or Run Manually

You can test this script locally or trigger it manually on GitHub:

### Trigger on GitHub
1. Go to the **Actions** tab in your repository.
2. Select the **Daily Auto Commit** workflow on the left sidebar.
3. Click the **Run workflow** button on the right and confirm.
4. Wait for the workflow to complete. It will create the commits for the current day of the cycle.

### Run Locally
1. Clone the repository.
2. Run the script: `python auto_commit.py`.
3. The script will output the number of commits it is making. Check `git log` to verify the commits were created successfully.

**Note:** If you run the script locally and you do not have a remote configured, the `git push` command at the end will issue a warning, but the script will not crash.
