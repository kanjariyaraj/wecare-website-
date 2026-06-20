# Auto-Commit Loop Automation Setup

This repository is configured with an automated commit script to simulate a continuous cycle of activity. The loop runs over a 5-day cycle with varying numbers of commits per day, and then repeats indefinitely.

## The Loop Pattern
* **Day 1:** 2 commits
* **Day 2:** 4 commits
* **Day 3:** 1 commit
* **Day 4:** 5 commits
* **Day 5:** 7 commits

## How It Works
1. **`auto_commit.py`:** A Python script that:
   - Reads the current day from `state.json` (defaults to Day 1).
   - Looks up the expected number of commits for that day.
   - For each commit, it generates random text, a timestamp, and appends it to `commit_log.txt`.
   - Modifies `state.json` on the last commit of the current day to point to the next day.
   - Configures the Git user as `github-actions[bot]`.
   - Stages, commits, and pushes to the `main` branch.
2. **GitHub Actions Workflow (`.github/workflows/auto_commit.yml`):**
   - Automatically executes `auto_commit.py` every day at 12:00 UTC using a cron schedule.
   - Has `workflow_dispatch` enabled so you can trigger it manually anytime.
   - Given write permissions to push directly back to the repo.

## Deployment Steps
1. Push this configuration (`auto_commit.py`, `.github/workflows/auto_commit.yml`, and `INSTRUCTIONS.md`) to your GitHub repository on the `main` branch.
2. Ensure GitHub Actions is enabled for your repository:
   - Go to your repository **Settings**.
   - Navigate to **Actions** -> **General**.
   - Make sure **Allow all actions and reusable workflows** is selected.
   - Under **Workflow permissions**, ensure **Read and write permissions** is selected. This allows the bot to push commits back to the repo. Save changes.
3. Once verified, the script will automatically run on schedule.
4. You can also manually trigger it by going to the **Actions** tab, selecting **Daily Auto Commit**, and clicking **Run workflow**.
