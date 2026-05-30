# GitHub Auto Commit Setup Instructions

This repository contains a setup to automate Git commits on a recurring 5-day cycle.

## Cycle Details
The script tracks a 5-day cycle where the number of commits changes depending on the day:
- **Day 1**: 2 commits
- **Day 2**: 4 commits
- **Day 3**: 1 commit
- **Day 4**: 5 commits
- **Day 5**: 7 commits
After Day 5, it resets to Day 1.

## Setup Instructions

### 1. Add Files to Your Repository
Copy the following files from this repository to your target repository:
- `auto_commit.py` (The main automation script)
- `state.json` (The state tracker, initialized to `{"day": 1}`)
- `commit_log.txt` (The file that will be modified by the script)
- `.github/workflows/auto_commit.yml` (The GitHub Actions workflow)

### 2. Ensure GitHub Actions Permissions
By default, GitHub Actions might not have permission to push code back to the repository. To fix this:
1. Go to your repository on GitHub.
2. Click on **Settings**.
3. Under the **Security** or **Code and automation** section on the left sidebar, click on **Actions**, then **General**.
4. Scroll down to **Workflow permissions**.
5. Select **Read and write permissions**.
6. Check the box that says "Allow GitHub Actions to create and approve pull requests" if necessary.
7. Click **Save**.

### 3. Testing It Out
You can test the GitHub Action manually:
1. Go to the **Actions** tab in your repository.
2. Click on the **Auto Commit Loop** workflow on the left.
3. Click the **Run workflow** dropdown on the right and select the branch (usually `main`).
4. Click **Run workflow**.

Wait for the action to complete, then check your commits history. You should see new automated commits, and `state.json` will be updated for the next day.

### 4. How It Works Under the Hood
The `auto_commit.yml` workflow triggers daily at midnight (UTC) via a cron schedule (`0 0 * * *`). It runs `auto_commit.py`.
The Python script:
1. Configures the local git credentials.
2. Reads `state.json` to find out which day it is.
3. Modifies `commit_log.txt` with random data and timestamps, staging and committing it multiple times based on the loop.
4. On the final commit of the loop, it modifies and stages `state.json` with the updated day number.
5. Pushes all the new commits to `main` using the Actions `GITHUB_TOKEN`.