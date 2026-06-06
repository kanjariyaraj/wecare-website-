# Automated Commit Deployment Instructions

This repository is configured with an automated commit script (`auto_commit.py`) that is run daily by a GitHub Actions workflow (`.github/workflows/auto_commit.yml`).

The script follows a specific 5-day cycle for making commits:
- Day 1: 2 commits
- Day 2: 4 commits
- Day 3: 1 commit
- Day 4: 5 commits
- Day 5: 7 commits
(Then the cycle resets to Day 1)

## Setup and Deployment

This setup requires no manual intervention once pushed to your default branch (e.g., `main`), assuming standard GitHub Actions settings are in place.

### 1. Push to Repository
Ensure all three key files are merged into your default branch (`main` or `master`):
1. `auto_commit.py` (The main automation script)
2. `state.json` (Tracks the current day of the loop)
3. `commit_log.txt` (The file that receives dummy modifications to register commits)
4. `.github/workflows/auto_commit.yml` (The GitHub Actions workflow)

### 2. Verify GitHub Actions Permissions
By default, GitHub Actions workflows might not have permission to push changes back to the repository. You must ensure your repository is configured to allow this:
1. Go to your repository **Settings** on GitHub.
2. Click on **Actions** -> **General** in the left sidebar.
3. Scroll down to **Workflow permissions**.
4. Select **Read and write permissions**.
5. Click **Save**.

### 3. Monitoring and Manual Trigger
- The automation is scheduled to run every day at 12:00 PM UTC.
- To trigger it manually (for testing or debugging):
  1. Go to the **Actions** tab in your repository.
  2. Select the **Automated Commits** workflow on the left.
  3. Click the **Run workflow** button on the right side.

### How it Works
When the GitHub Actions workflow triggers:
1. It checks out the current branch.
2. It runs `python auto_commit.py`.
3. The script reads `state.json` to see what "Day" it is.
4. It performs the necessary number of commits for that day by appending timestamps to `commit_log.txt`.
5. It increments the "Day" in `state.json` and stages it.
6. It commits the changes and pushes them back to the repository on the current branch.
