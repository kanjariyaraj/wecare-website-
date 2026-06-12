# Automated Commit Loop Setup

This repository is configured with an automated commit script (`auto_commit.py`) managed by a GitHub Actions workflow (`.github/workflows/auto_commit.yml`).

## How it works

The automation follows a 5-day cycle:
- **Day 1**: 2 commits
- **Day 2**: 4 commits
- **Day 3**: 1 commit
- **Day 4**: 5 commits
- **Day 5**: 7 commits

The script updates `commit_log.txt` with timestamps and random text, commits the changes, updates the internal `state.json` tracker, and pushes the changes back to the repository. The workflow runs daily at 12:00 PM UTC.

## Deployment Instructions

1. **Add files to your repository:** Ensure the following files are present in the root of your GitHub repository:
   - `auto_commit.py`
   - `state.json`
   - `commit_log.txt`
   - `.github/workflows/auto_commit.yml`

2. **Grant Workflow Permissions:**
   - Go to your GitHub repository on github.com.
   - Click on **Settings** > **Actions** > **General**.
   - Scroll down to the **Workflow permissions** section.
   - Select **Read and write permissions**. This is required so the GitHub Actions bot can push the commits back to your repository.
   - Click **Save**.

3. **Manually Trigger the Workflow (Optional):**
   - Go to the **Actions** tab in your repository.
   - Select **Auto Commit Loop** from the left sidebar.
   - Click the **Run workflow** dropdown on the right and click **Run workflow**.
   - This will immediately test the script without waiting for the daily schedule.

## Files Description

- **`auto_commit.py`**: The core Python script that handles state tracking, makes git commits, and pushes to the current branch.
- **`state.json`**: Tracks the current day in the 5-day cycle.
- **`commit_log.txt`**: The file modified by the Python script to create detectable diffs for git commits.
- **`.github/workflows/auto_commit.yml`**: The cron-based scheduler that runs the script daily using GitHub Actions.
