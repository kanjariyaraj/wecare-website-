# Auto Commit Loop Setup and Deployment Instructions

This repository contains an automated script that performs a daily commit loop based on the following pattern:
- Day 1: 2 commits
- Day 2: 4 commits
- Day 3: 1 commit
- Day 4: 5 commits
- Day 5: 7 commits
- Day 6+: Resets back to Day 1

The system automatically manages state and pushes the commits to the repository using GitHub Actions.

## Requirements
- A GitHub Repository.
- `auto_commit.py`: The core automation script in the root directory.
- `.github/workflows/auto_commit.yml`: The GitHub Actions workflow file.

## Deployment Steps

### 1. Enable GitHub Actions Workflows
1. Navigate to your GitHub repository in your web browser.
2. Click on the **Actions** tab at the top of your repository.
3. If this is a new repository or Actions are disabled, you may see a prompt to "Enable Actions on this repository". Click the green button to enable them.

### 2. Configure Repository Permissions
By default, GitHub Actions may only have read access to your repository. Since the script creates and pushes commits, it needs write access.
1. In your repository, click on the **Settings** tab.
2. In the left sidebar, scroll down and click on **Actions**, then click on **General**.
3. Scroll down to the **Workflow permissions** section.
4. Select the radio button for **Read and write permissions**.
5. Click **Save**.

### 3. Commit and Push the Files
Ensure that `auto_commit.py` and `.github/workflows/auto_commit.yml` are committed and pushed to your default branch (e.g., `main` or `master`).

### 4. Test the Automation Manually
Instead of waiting for the daily schedule (which runs at 12:00 UTC), you can manually trigger the workflow to ensure it works correctly.
1. Go to the **Actions** tab.
2. In the left sidebar, under "All workflows", click on **Auto Commit Loop**.
3. On the right side, click the **Run workflow** dropdown button.
4. Select your main branch and click **Run workflow**.
5. Refresh the page to see the job start. Once finished, check your repository's commit history to verify that the commits were added successfully.

## State Management
The script maintains the loop's state in a file named `state.json`. If you ever need to reset the loop manually, simply edit `state.json` to have `"current_day": 1` or delete the file entirely. The log file `commit_log.txt` serves as the modified file to ensure Git detects legitimate file changes.