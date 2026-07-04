# Automated Commit Loop Setup Instructions

This repository contains a Python script and a GitHub Actions workflow to automate Git commits based on a strict 5-day cycle.

## Cycle Rules
- **Day 1**: 2 commits
- **Day 2**: 4 commits
- **Day 3**: 1 commit
- **Day 4**: 5 commits
- **Day 5**: 7 commits
*(After Day 5, it resets back to Day 1).*

## How it Works
1. **`auto_commit.py`**: A Python script that reads the current day from `state.json`. Based on the day, it loops to create the specified number of commits. It appends a log entry to `commit_log.txt` for each commit, stages, and commits the file. On the last commit of the day, it also updates and stages `state.json`. Finally, it pushes the commits to the `main` branch.
2. **`state.json`**: A JSON file storing the current day in the cycle.
3. **`commit_log.txt`**: A log file that gets modified with random strings and timestamps to ensure Git detects real file changes for every commit.
4. **`.github/workflows/auto_commit.yml`**: A GitHub Actions workflow configured to run `auto_commit.py` every day at 12:00 UTC.

## Deployment Steps

1. **Commit these files to your repository**:
   Ensure `auto_commit.py`, `state.json`, `commit_log.txt`, and `.github/workflows/auto_commit.yml` are pushed to your repository's `main` branch.

2. **Verify GitHub Actions Permissions**:
   By default, GitHub Actions might not have permission to push code back to your repository.
   - Go to your repository **Settings**.
   - Navigate to **Actions > General**.
   - Scroll down to **Workflow permissions**.
   - Select **Read and write permissions**.
   - Click **Save**.

3. **Manual Testing (Optional)**:
   - Go to the **Actions** tab in your repository.
   - Select the **Automated Commit Loop** workflow from the left sidebar.
   - Click **Run workflow** to manually trigger the script.
   - Check your commit history to verify the correct number of commits were made.

## Local Execution
If you want to run the script locally to test it:
1. Make sure you have Python installed.
2. Run `python auto_commit.py` in your terminal.
3. It will read `state.json`, create local commits, and attempt to push to the `main` branch.
