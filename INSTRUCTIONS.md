# GitHub Auto Commit Setup

This repository contains an automated script and a GitHub Actions workflow to make daily commits following a specific pattern:
- Day 1: 2 commits
- Day 2: 4 commits
- Day 3: 1 commit
- Day 4: 5 commits
- Day 5: 7 commits
- Loop resets to Day 1

## Components

1. **`auto_commit.py`**: The core Python script that manages state (`state.json`), modifies a tracked file (`commit_log.txt`), commits the changes using Git, and pushes back to the `main` branch.
2. **`state.json`**: Tracks the current day in the commit cycle (1 through 5).
3. **`commit_log.txt`**: The target file modified by the Python script to trigger genuine Git diffs.
4. **`.github/workflows/auto_commit.yml`**: The GitHub Actions pipeline that triggers the script every day at `00:00 UTC`.

## Deployment Instructions

To deploy this in your repository:

1. Copy the `auto_commit.py` script into the root of your repository.
2. Copy the `.github/workflows/auto_commit.yml` file into your `.github/workflows/` directory.
3. Make sure GitHub Actions is enabled for your repository (Settings -> Actions -> General -> Allow all actions and reusable workflows).
4. Make sure the workflow has write permissions. This is already handled by `permissions: contents: write` in the `auto_commit.yml` file. However, in your GitHub Repo settings (Settings -> Actions -> General), ensure "Workflow permissions" is set to "Read and write permissions" and "Allow GitHub Actions to create and approve pull requests" is checked if you have restricted settings.
5. Create an initial `state.json` file in the root with `{"current_day": 1}`.
6. Create an empty `commit_log.txt` in the root.
7. Push these initial files to the `main` branch.

## How it works

The GitHub action will trigger automatically daily due to the cron job schedule (`0 0 * * *`). You can also manually trigger the loop using the "Run workflow" button under the Actions tab.

During execution:
- It checks the current day from `state.json`.
- Makes the corresponding amount of commits.
- It will modify `commit_log.txt` in a loop, commit each step.
- In the final commit for the day, it updates `state.json` to the next day's number and commits the file.
- Finally, it pushes all new commits to the remote.