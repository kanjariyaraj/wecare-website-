# Auto Commit Script Deployment Instructions

This repository is configured with an automated script that makes daily commits in a specific loop pattern (2, 4, 1, 5, 7 commits over 5 days, then repeats).

## Files Included
- `auto_commit.py`: The Python script that performs the commits and tracks state.
- `state.json`: A file that tracks which day (1-5) of the loop we are currently on.
- `commit_log.txt`: A log file that gets modified to create genuine code changes for the commits.
- `.github/workflows/auto_commit.yml`: The GitHub Actions workflow file that runs the script automatically.

## How to Deploy and Setup

1. **Push Code to Repository**: Make sure all these files are pushed to the `main` branch of your GitHub repository.
2. **Enable Workflows (If Needed)**:
   - Go to your repository on GitHub.
   - Click on the **Actions** tab.
   - If prompted, click "I understand my workflows, go ahead and enable them" or simply ensure the workflow is listed.
3. **Check Workflow Permissions**:
   - Go to your repository **Settings**.
   - Navigate to **Actions** > **General**.
   - Scroll down to the **Workflow permissions** section.
   - Ensure that **Read and write permissions** is selected. This allows the GitHub Action to push new commits back to your repository.
   - Click **Save**.

## How to Test / Trigger Manually

The workflow is configured to run automatically every day at 12:00 PM UTC using a cron schedule. You can also trigger it manually:

1. Go to the **Actions** tab in your repository.
2. Under "All workflows" on the left, click on **Auto Commit Loop**.
3. On the right side, click the **Run workflow** dropdown button.
4. Select the `main` branch and click the green **Run workflow** button.
5. You can then click into the running workflow job to see the logs and ensure it completed successfully.

## How It Works Locally

You can also run this script manually on your local machine:
```bash
python auto_commit.py
```
This will configure your git (if in Actions), make the appropriate number of commits for the current day, update the `state.json` file to the next day, and attempt to push to `origin main`.
