# Auto Commit Automation Setup

This repository contains an automation setup to commit changes on a specific 5-day cycle.

## Loop Pattern
- Day 1: 2 commits
- Day 2: 4 commits
- Day 3: 1 commit
- Day 4: 5 commits
- Day 5: 7 commits
- Cycle repeats indefinitely.

## Files
- `auto_commit.py`: The Python script that runs the commit logic. It appends to `commit_log.txt` and manages the state via `state.json`.
- `state.json`: Tracks the current day (1-5) in the loop pattern. It is updated and committed only on the final commit of each day's cycle to maintain strict commit counts.
- `commit_log.txt`: A log file that the script modifies to generate genuine code changes for each commit.
- `.github/workflows/auto_commit.yml`: The GitHub Actions workflow file that runs the `auto_commit.py` script automatically at 12:00 UTC every day.

## How to Deploy
1. Simply commit these files (`auto_commit.py`, `state.json`, `commit_log.txt`, `.github/workflows/auto_commit.yml`, and `INSTRUCTIONS.md`) to the `main` branch of your GitHub repository.
2. The GitHub Actions workflow will automatically start running every day at 12:00 UTC based on the schedule defined in `.github/workflows/auto_commit.yml`.
3. To trigger it manually for testing, go to the "Actions" tab in your GitHub repository, select "Auto Commit Loop", and click "Run workflow".
4. Make sure that the GitHub Actions bot has permission to push to your repository (this is typically enabled by default, but can be checked under Settings -> Actions -> General -> Workflow permissions: "Read and write permissions").
