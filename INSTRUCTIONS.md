# Auto Commit Bot Instructions

This repository is configured with an automated script that runs on a 5-day cycle to make a specific number of commits each day.

## How It Works

The cycle follows this strict daily pattern:
- **Day 1**: 2 commits
- **Day 2**: 4 commits
- **Day 3**: 1 commit
- **Day 4**: 5 commits
- **Day 5**: 7 commits
- *Resets to Day 1 after Day 5.*

### Components
1. **`auto_commit.py`**: The main Python script that determines how many commits to make, updates the commit log, stages the files, and pushes them to the repository.
2. **`state.json`**: A tracking file that stores the current day of the loop.
3. **`commit_log.txt`**: A log file that gets updated by the script. This ensures each commit contains genuine file modifications.
4. **`.github/workflows/auto_commit.yml`**: The GitHub Actions workflow that executes the script daily at 12:00 UTC.

## Setup & Deployment

1. Make sure `auto_commit.py`, `state.json`, `commit_log.txt`, and `.github/workflows/auto_commit.yml` are committed and pushed to the `main` branch.
2. Ensure GitHub Actions is enabled for your repository.
3. Under **Repository Settings -> Actions -> General**, scroll down to **Workflow permissions** and make sure "Read and write permissions" is selected. This allows the Action to push commits back to the repo.
4. The workflow will run automatically based on the cron schedule. You can also trigger it manually from the "Actions" tab by selecting the "Auto Commit Loop" workflow and clicking "Run workflow".

## Modification

- **Changing the cycle**: Open `auto_commit.py` and modify the `COMMITS_PER_DAY` dictionary to adjust how many commits happen on each day.
- **Changing the schedule**: Open `.github/workflows/auto_commit.yml` and modify the cron expression under `on.schedule`.
