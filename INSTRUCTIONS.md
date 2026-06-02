# Auto-Commit Loop Setup Instructions

This repository is configured with an automated commit loop that runs daily using GitHub Actions. It follows a specific 5-day cycle:
- Day 1: 2 commits
- Day 2: 4 commits
- Day 3: 1 commit
- Day 4: 5 commits
- Day 5: 7 commits
- Loop resets to Day 1

## Prerequisites

No external dependencies are required. The script uses standard Python libraries.

## Setup Steps

1. **Enable Workflows (if disabled):**
   - Go to your GitHub repository.
   - Click on the **Actions** tab.
   - If prompted, click **"I understand my workflows, go ahead and enable them"**.

2. **Verify Repository Permissions:**
   - Go to **Settings** > **Actions** > **General**.
   - Under **Workflow permissions**, ensure that **"Read and write permissions"** is selected so the action can push commits back to the repository.
   - Also check the box for **"Allow GitHub Actions to create and approve pull requests"** if you intend to use PRs in the future (though this workflow commits directly to `main`).
   - Click **Save**.

## Manual Testing

You can trigger the workflow manually to test it without waiting for the scheduled time:

1. Go to the **Actions** tab.
2. Select **"Auto Commit"** from the left sidebar.
3. Click the **"Run workflow"** dropdown button on the right.
4. Select the branch (default: `main`) and click **"Run workflow"**.
5. The workflow will run, execute the `auto_commit.py` script, and push new commits to the repository.

You can view the progress of the loop in the `state.json` file and see the actual commit history in the `commit_log.txt` file and your repository's commit history.