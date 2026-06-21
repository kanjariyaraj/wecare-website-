# Auto-Commit Loop Setup Instructions

This repository is configured with an automated commit script (`auto_commit.py`) managed by a GitHub Actions workflow (`.github/workflows/auto_commit.yml`).
The automation follows a recurring 5-day cycle:
- Day 1: 2 commits
- Day 2: 4 commits
- Day 3: 1 commit
- Day 4: 5 commits
- Day 5: 7 commits

## 1. Initial Setup and Deployment
To activate the automation in your GitHub repository, follow these steps:

1. **Push Code to Remote:** Ensure all the files (`auto_commit.py`, `state.json`, `commit_log.txt`, and `.github/workflows/auto_commit.yml`) are committed and pushed to the `main` branch of your repository.
2. **Enable Workflow Permissions:**
   - Go to your repository on GitHub.
   - Click on **Settings** > **Actions** > **General**.
   - Under the **Workflow permissions** section, select **Read and write permissions**.
   - Check the box for "Allow GitHub Actions to create and approve pull requests" (optional but good practice).
   - Click **Save**.

## 2. Triggering the Workflow
The workflow is scheduled to run automatically every day at 00:00 UTC.
If you want to trigger it manually to test the setup:
1. Go to the **Actions** tab in your GitHub repository.
2. Select **Auto Commit Loop** from the left sidebar.
3. Click the **Run workflow** dropdown on the right and click **Run workflow**.

## 3. Running Locally
If you want to run the script locally to see how it works:
1. Ensure you have Python 3 installed.
2. In your terminal, navigate to the repository folder.
3. Run `python auto_commit.py`.
4. The script will output its progress, modify `commit_log.txt` and `state.json`, make the commits locally, and attempt to push to your remote branch.