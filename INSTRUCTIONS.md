# Auto Commit Loop Automation Setup

This repository is configured with an automated daily loop that makes commits back to the repository using GitHub Actions.

## Commit Pattern
The loop is a 5-day cycle:
- **Day 1**: 2 commits
- **Day 2**: 4 commits
- **Day 3**: 1 commit
- **Day 4**: 5 commits
- **Day 5**: 7 commits

After Day 5, the loop resets to Day 1.

## Architecture

* **`auto_commit.py`**: The core Python script that manages the logic.
* **`state.json`**: Stores the current day (1-5) of the loop.
* **`commit_log.txt`**: A tracker log file modified by the Python script (with random strings and timestamps) to create genuine file changes.
* **`.github/workflows/auto_commit.yml`**: The GitHub Actions workflow file. It runs on a daily cron schedule (`0 12 * * *` which is 12:00 PM UTC every day).

## Step-by-Step Deployment Instructions

1. **Commit and Push:** Add all four files (`auto_commit.py`, `state.json`, `commit_log.txt`, and `.github/workflows/auto_commit.yml`) to your repository and push to the `main` branch.
   ```bash
   git add auto_commit.py state.json commit_log.txt .github/workflows/auto_commit.yml
   git commit -m "Add auto commit loop automation"
   git push origin main
   ```

2. **Verify GitHub Actions Setup:**
   - Go to your repository on GitHub.
   - Click the "Actions" tab.
   - You should see the workflow named "Auto Commit".

3. **Manual Trigger (Optional):**
   - In the "Actions" tab, select the "Auto Commit" workflow.
   - Click "Run workflow" on the right side to manually trigger a run. This is a great way to verify it works without waiting for the scheduled time.

4. **Permissions:**
   - The workflow uses `permissions: contents: write` to allow the GitHub Actions runner to push commits back to the repository. No Personal Access Tokens (PATs) are required for default setups.

## How It Works Locally (Testing)

You can run the script locally to see what it does.
```bash
python auto_commit.py
```
This will append lines to `commit_log.txt`, update `state.json` appropriately, and commit the changes to your local Git repository. You can verify the commits using `git log`.
