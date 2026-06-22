# Auto Commit Setup Instructions

This repository is configured with an automated commit script (`auto_commit.py`) managed by a GitHub Actions workflow (`.github/workflows/auto_commit.yml`).

The automation follows a recurring 5-day cycle:
- Day 1: 2 commits
- Day 2: 4 commits
- Day 3: 1 commit
- Day 4: 5 commits
- Day 5: 7 commits

## Setup and Deployment

### 1. File Initialization
The required tracking files `state.json` and `commit_log.txt` have been initialized. Ensure they are pushed to the root of your repository along with `auto_commit.py` and the `.github/workflows` directory.

### 2. Configure GitHub Actions Workflow Permissions
For the script to successfully push commits back to your repository, you must grant write permissions to the `GITHUB_TOKEN`:
1. Go to your repository on GitHub.
2. Click on **Settings** > **Actions** > **General**.
3. Scroll down to the **Workflow permissions** section.
4. Select **Read and write permissions**.
5. Click **Save**.

### 3. Usage
- **Automated Mode:** The GitHub Action is scheduled to run every day at 00:00 UTC using a cron job. It will automatically read `state.json`, determine the number of commits to make, append to `commit_log.txt`, commit the changes, update the state, and push.
- **Manual Mode:** You can trigger the workflow manually at any time:
  1. Go to the **Actions** tab in your repository.
  2. Select the **Auto Commit Loop** workflow on the left.
  3. Click **Run workflow**.

### 4. Running Locally
If you want to run the script locally to test or advance the state manually:
1. Ensure you have Python installed.
2. Run `python auto_commit.py` from the root of the repository.
3. The script will make the commits based on the current state. Note that if you run it locally, it may attempt to push. Make sure your local git environment is authenticated and tracking the remote branch.
