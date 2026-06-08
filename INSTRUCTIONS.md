# Automated Commit Setup Instructions

This repository contains an automated commit script designed to run on a continuous 5-day cycle.

## Loop Rules
- Day 1: 2 commits
- Day 2: 4 commits
- Day 3: 1 commit
- Day 4: 5 commits
- Day 5: 7 commits
- Day 6+: Resets back to Day 1

## State Management
The state is managed using `state.json` at the root of the repository. This file keeps track of what day of the cycle the repository is currently on. The script automatically updates this file.
Modifications are made to `commit_log.txt` by appending random text and timestamps, ensuring Git detects valid file changes for each commit.

## How it Works
1. `auto_commit.py` reads `state.json` to find the current day (1-5).
2. It looks up how many commits to make for that day based on the loop rules.
3. It updates `state.json` to point to the next day in the cycle.
4. For each commit, it appends data to `commit_log.txt`, stages `state.json` and `commit_log.txt`, and commits using Git.
5. It then pushes the commits back to the main branch.

## Testing Locally
To test the script locally, simply run:
```bash
python auto_commit.py
```
This will read the current state, make the commits locally, update `state.json`, and attempt to push to `main`. If you have pushed your current branch, this will successfully update the remote.

## GitHub Actions Automation
The project uses GitHub Actions to run the script automatically every day at 12:00 UTC. The workflow is located in `.github/workflows/auto_commit.yml`.

### Important Workflow Requirements
1. **Repository Settings**: Go to `Settings -> Actions -> General -> Workflow permissions` and ensure it is set to "Read and write permissions" so the Action can push back to the repository.
2. **Triggering**: You can manually trigger the workflow via the "Actions" tab by selecting the "Daily Automated Commits" workflow and clicking "Run workflow".
