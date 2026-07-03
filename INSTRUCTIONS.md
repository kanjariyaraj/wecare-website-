# GitHub Actions Auto-Commit Loop

This repository contains a Python script and GitHub Actions workflow designed to automate commits based on a 5-day cycle.

## Cycle Pattern

The automated script (`auto_commit.py`) follows this exact pattern of commits:
- Day 1: 2 commits
- Day 2: 4 commits
- Day 3: 1 commit
- Day 4: 5 commits
- Day 5: 7 commits

After day 5, the script automatically resets the counter to day 1.

## Files Involved

- `auto_commit.py`: The Python script that generates random strings, modifies a text file, handles git state updates, and executes the git commits.
- `.github/workflows/auto_commit.yml`: The GitHub Actions workflow file that schedules the script to run daily at 12:00 UTC.
- `state.json`: Tracks the current day in the cycle.
- `commit_log.txt`: The text file that gets appended to make each commit unique.

## Setup Instructions

If you want to deploy this automation to another repository or configure it for the first time, follow these steps:

### 1. Enable GitHub Actions Permissions

By default, GitHub Actions might not have permission to push changes back to the repository.

1. Go to your repository **Settings**.
2. On the left sidebar, click on **Actions** > **General**.
3. Scroll down to the **Workflow permissions** section.
4. Select **Read and write permissions**.
5. Check the box for **Allow GitHub Actions to create and approve pull requests** (optional but recommended if using branches).
6. Click **Save**.

### 2. File Placement

Make sure the following files are in the exact structure in your repository:
- `auto_commit.py` (in root directory)
- `state.json` (in root directory)
- `commit_log.txt` (in root directory)
- `.github/workflows/auto_commit.yml` (in the `.github/workflows` directory)

### 3. Verify the Initial State

Make sure `state.json` has valid JSON indicating the start day:
```json
{
    "day": 1
}
```

### 4. Triggering the Action Manually (Optional)

You can trigger the workflow manually to test it:

1. Go to the **Actions** tab in your repository.
2. Under "All workflows" on the left, click on **Auto Commit**.
3. On the right, click the **Run workflow** dropdown button.
4. Click **Run workflow**.

The workflow will run the script, read `state.json`, commit to `commit_log.txt` the required number of times for that day, update `state.json` on the final commit, and push the results back to the repository.

## Technical Notes
- The automation uses the `GITHUB_TOKEN` provided automatically by the actions runner. No personal access token is required if Workflow Permissions are set correctly.
- The script adds a fallback for local testing by configuring a generic bot user name and email.
- If pushing fails (e.g. testing locally with no remote), the script continues without crashing.