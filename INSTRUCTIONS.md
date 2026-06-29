# Auto Commit Setup Instructions

This repository contains an automated commit script (`auto_commit.py`) that creates a specific pattern of daily commits to maintain continuous GitHub activity according to a repeating 5-day cycle.

## Commit Loop Pattern

The script follows a strict 5-day rotating cycle for the number of commits:
- **Day 1:** 2 commits
- **Day 2:** 4 commits
- **Day 3:** 1 commit
- **Day 4:** 5 commits
- **Day 5:** 7 commits

After Day 5, the sequence resets back to Day 1.

## How It Works

1. **State Management:** The current position in the 5-day cycle is stored in `state.json`.
2. **Commit Actions:** For each commit, the script appends a timestamp and random string to `commit_log.txt`.
3. **State Updates:** During the *final* commit of the day, `state.json` is updated to the next day in the cycle and committed, ensuring the commit count exactly matches the intended loop pattern.

## Local Testing

To test the automation script locally:

1. Ensure Python 3 is installed.
2. Ensure you are inside the repository root.
3. Run the script:
   ```bash
   python auto_commit.py
   ```
4. Check the `commit_log.txt` and `state.json` files to verify changes.
5. Check `git log` to see the new automated commits.

## GitHub Actions Deployment

The automation is deployed via a GitHub Actions workflow defined in `.github/workflows/auto_commit.yml`.

### Setup

1. **Push Files:** Ensure `auto_commit.py`, `state.json`, `commit_log.txt`, and `.github/workflows/auto_commit.yml` are committed and pushed to the `main` branch.
2. **Permissions:** The workflow uses the default `GITHUB_TOKEN`. Ensure that the workflow has read and write permissions in the repository settings:
   - Go to **Settings > Actions > General**.
   - Scroll down to **Workflow permissions**.
   - Ensure **Read and write permissions** is selected.

### Execution

- **Scheduled:** The workflow automatically runs at 00:00 UTC every day via cron schedule.
- **Manual:** You can manually trigger the workflow from the "Actions" tab in GitHub by selecting the "Auto Commit Loop" workflow and clicking "Run workflow".
