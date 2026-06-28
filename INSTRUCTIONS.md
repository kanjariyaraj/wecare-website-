# Auto Commit Loop Automation Setup

This repository is configured with an automated GitHub Actions setup that creates a specific number of commits based on a 5-day cycle:
- **Day 1:** 2 commits
- **Day 2:** 4 commits
- **Day 3:** 1 commit
- **Day 4:** 5 commits
- **Day 5:** 7 commits

It then resets back to Day 1.

## Setup Instructions

1. **Commit these files** to your repository's main branch:
   - `.github/workflows/auto_commit.yml`
   - `auto_commit.py`
   - `state.json`
   - `commit_log.txt`

2. **GitHub Actions Permissions:**
   - Go to your repository settings on GitHub.
   - Navigate to `Settings` > `Actions` > `General`.
   - Scroll down to **Workflow permissions**.
   - Make sure **Read and write permissions** is selected.
   - Click **Save**.
   *(This step is crucial, otherwise the GitHub Actions bot will not be allowed to push the new commits to your main branch).*

3. **Running the Automation:**
   - By default, it runs every day at midnight UTC via the cron schedule (`0 0 * * *`).
   - You can also trigger it manually from the **Actions** tab in your repository: select the **Auto Commit Loop** workflow and click **Run workflow**.

## File Descriptions

- **`auto_commit.py`:** The main Python script that modifies `commit_log.txt`, updates the current day in `state.json` on the final commit, and pushes the changes.
- **`.github/workflows/auto_commit.yml`:** The GitHub Actions configuration that runs the script on a schedule.
- **`state.json`:** Tracks the current day in the loop (1 to 5).
- **`commit_log.txt`:** The dummy file that is appended to in order to generate valid, detectable Git diffs for each commit.
