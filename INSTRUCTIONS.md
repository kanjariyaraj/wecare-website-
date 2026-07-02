# Auto-Commit Loop Automation

This repository includes a fully automated system that generates artificial git activity.
It makes continuous contributions on a 5-day cycle:

- Day 1: 2 commits
- Day 2: 4 commits
- Day 3: 1 commit
- Day 4: 5 commits
- Day 5: 7 commits
- Day 6: resets back to Day 1.

## Setup Instructions

1. Ensure `state.json` exists in the repository root. Initially, it should look like:
   ```json
   {"day": 1}
   ```
2. Ensure `commit_log.txt` exists. This file is modified to simulate meaningful file changes for the commits.
3. Ensure `.github/workflows/auto_commit.yml` and `auto_commit.py` are present.
4. The workflow will automatically run every day at `12:00 UTC` and perform the necessary commit operations.

## Local Testing

You can verify the script behavior locally:

1. Open your terminal in the repository root.
2. Run the script: `python auto_commit.py`
3. The script will look at `state.json`, determine the current day, generate the appropriate number of commits, modify `commit_log.txt`, and update `state.json` on the last commit of that cycle to increment the day.
4. It uses local git configuration. If the username or email is not set, it configures dummy default bot values.
5. Review the new commits in the local branch (`git log -n 10`).

## Notes
* **State Updates**: Updates to `state.json` are performed only as part of the *final commit* for the daily cycle. This ensures the daily commit count perfectly matches the requested schedule.
* **Authentication**: When run in GitHub Actions, it utilizes the default `GITHUB_TOKEN` to push to the repository. The workflow must have `contents: write` permissions.