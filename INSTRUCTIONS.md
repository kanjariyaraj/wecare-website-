# Automated Commit Setup Instructions

This project includes a daily automated commit loop setup. The loop runs on a 5-day cycle with a specific pattern:
- Day 1: 2 commits
- Day 2: 4 commits
- Day 3: 1 commit
- Day 4: 5 commits
- Day 5: 7 commits

The loop automatically resets after Day 5.

## How it works

1. **`auto_commit.py`**: A Python script that reads the current day from `state.json`, performs the required number of commits, appends logs to `commit_log.txt`, updates the state, and pushes the changes to the `main` branch.
2. **GitHub Actions**: A workflow `.github/workflows/auto_commit.yml` runs every day at 00:00 UTC using a cron job, running the `auto_commit.py` script.

## Setup & Deployment Instructions

### 1. Push Code to GitHub
Ensure all tracking files (`auto_commit.py`, `state.json`, `commit_log.txt`, and `.github/workflows/auto_commit.yml`) are committed and pushed to your `main` branch.

### 2. Grant GitHub Actions Permissions
By default, GitHub Actions might not have write access to push commits back to the repository. To enable this:
1. Go to your repository on GitHub.
2. Navigate to **Settings** > **Actions** > **General**.
3. Scroll down to **Workflow permissions**.
4. Select **Read and write permissions**.
5. Click **Save**.

### 3. Trigger the Workflow (Optional)
The workflow will run automatically at midnight UTC. However, you can manually trigger it to test the setup:
1. Go to the **Actions** tab in your repository.
2. Select **Automated Daily Commits** from the left sidebar.
3. Click the **Run workflow** dropdown on the right side.
4. Click the green **Run workflow** button.

### 4. Verify Commits
After the workflow runs, check your repository's commit history to verify that the automated commits were successfully pushed.
