# GitHub Auto Commit Deployment Instructions

This repository contains a fully automated setup to make a precise number of commits each day based on a predefined 5-day loop:

- Day 1: 2 commits
- Day 2: 4 commits
- Day 3: 1 commit
- Day 4: 5 commits
- Day 5: 7 commits
- Day 6+: Resets back to Day 1

The system works via a Python script (`auto_commit.py`) that manages the commits, a state file (`state.json`) that tracks the loop day, and a GitHub Actions workflow (`.github/workflows/auto_commit.yml`) that schedules it.

## Deployment Steps

To deploy this to your own GitHub repository, follow these steps:

### 1. Copy the necessary files
Copy the following files into the root of your target repository:
- `auto_commit.py`
- `.github/workflows/auto_commit.yml`
- `state.json` (Optional: The script will create this if missing)
- `commit_log.txt` (Optional: The script will create this if missing)

### 2. Enable GitHub Actions Workflows
If your repository is new or has never run Actions before, GitHub may require you to enable them:
- Go to the **Actions** tab of your repository on GitHub.
- If prompted, click **"I understand my workflows, go ahead and enable them"**.

### 3. Ensure Workflow Permissions
By default, GitHub Actions might not have permission to push code back to your repository. You need to verify the permissions:
1. Go to your repository **Settings** on GitHub.
2. Under "Code and automation" on the left sidebar, click on **Actions**, then click on **General**.
3. Scroll down to the **Workflow permissions** section.
4. Ensure that **"Read and write permissions"** is selected.
5. Also, ensure the checkbox for **"Allow GitHub Actions to create and approve pull requests"** is checked (this allows pushing directly to branches).
6. Click **Save**.

### 4. How it works
- The GitHub Actions workflow is scheduled to run every day at midnight (UTC) using a cron job (`0 0 * * *`).
- When it runs, the Python script executes and performs the required number of commits.
- It automatically updates `commit_log.txt` with a random hash and timestamp to ensure Git recognizes the changes.
- In the final commit of the day, it automatically increments `state.json` and bundles it with the commit so the state is carried over for the next day.
- Finally, the workflow executes `git push` to upload the commits back to your main branch.

### Manual Triggering (Testing)
You can manually trigger the workflow to test it:
1. Go to the **Actions** tab on your repository.
2. Click on the **Automated Daily Commits** workflow on the left side.
3. Click the **Run workflow** dropdown button on the right side and click **Run workflow**.
4. The workflow will run and execute the commit logic for the current day.
