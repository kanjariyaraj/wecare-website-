# Auto Commit Bot Instructions

This repository contains an automated script and a GitHub Actions workflow to create daily automated commits following a specific loop pattern.

## Overview

The `auto_commit.py` script runs on a 5-day cycle:
- Day 1: 2 commits
- Day 2: 4 commits
- Day 3: 1 commit
- Day 4: 5 commits
- Day 5: 7 commits
- Day 6: Resets to Day 1 (2 commits), and repeats indefinitely.

## How it works

1. **State Tracking**: `state.json` tracks the current day index in the loop.
2. **Commit Activity**: The script appends timestamps to `commit_log.txt` to create genuine file changes.
3. **Commit Details**: For each required commit, it stages the log file, creates a commit message indicating the day and commit count. On the last commit of the day, it updates `state.json` for the next day.
4. **Automation**: A GitHub Actions workflow (`.github/workflows/auto_commit.yml`) is scheduled to run every day at midnight UTC.

## Setup and Deployment

The setup is already included in this repository. Ensure the following configurations:

1. **Enable Workflows**: Navigate to the "Actions" tab in your GitHub repository and ensure workflows are enabled if this is a newly pushed workflow.
2. **Workflow Permissions**: The GitHub Action needs permission to push code back to the repository. The workflow file (`auto_commit.yml`) already sets `permissions: contents: write`, but you must ensure your repository settings allow this:
   - Go to your repository **Settings** -> **Actions** -> **General**.
   - Under **Workflow permissions**, make sure **Read and write permissions** is selected.
   - Click Save.

## Testing Locally

If you want to run the script locally to test it:

```bash
# Ensure state.json and commit_log.txt exist
# Run the script
python auto_commit.py
```

This will create commits in your local git history and attempt to push them to `main`.

## Manual Triggering

You can manually trigger the action at any time without waiting for the scheduled cron run:
1. Go to the **Actions** tab on GitHub.
2. Select **Automated Commit Loop** on the left.
3. Click the **Run workflow** dropdown on the right and select **Run workflow**.
