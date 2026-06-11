# Commit Automation

This repository contains an automated commit script (`auto_commit.py`) that executes via GitHub Actions.

## Loop Rules
The script operates on a 5-day cycle:
- **Day 1**: 2 commits
- **Day 2**: 4 commits
- **Day 3**: 1 commit
- **Day 4**: 5 commits
- **Day 5**: 7 commits

After Day 5, it resets back to Day 1. The current day state is tracked inside `state.json`.

## How it works
- `auto_commit.py` reads `state.json` to find out what day it is in the cycle.
- It determines how many commits to make based on the day.
- For each commit, it appends a random string and timestamp to `commit_log.txt` to generate valid changes that Git can detect.
- It then commits and pushes the changes, moving the state forward to the next day when it completes.

## Setup Instructions

1. Ensure the `.github/workflows/auto_commit.yml` file is pushed to the `main` branch.
2. The workflow requires write permissions to the repository to push the commits. The workflow YAML explicitly sets `permissions: contents: write`.
3. If you run into permission issues, check your repository settings:
   - Go to **Settings > Actions > General**.
   - Under **Workflow permissions**, make sure **Read and write permissions** is selected.

## Local Testing
You can manually test the script locally:
```bash
python auto_commit.py
```
This will run the automation for the current day tracked in `state.json` and attempt to commit locally. It will also try to push, but will catch the error safely if no upstream is configured or you do not have permissions to push locally.
