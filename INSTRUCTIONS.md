# GitHub Auto Commit Setup Instructions

This repository is set up with an automated script that loops through a 5-day cycle, making a specific number of commits each day to simulate regular activity.

## Setup Instructions

1. **Commit these files to the default branch (e.g., `main` or `master`)**
   Make sure you commit and push the following files to your GitHub repository:
   - `auto_commit.py`
   - `.github/workflows/auto_commit.yml`
   - `state.json`
   - `commit_log.txt`

2. **Verify Workflow Permissions**
   - Go to your repository on GitHub.
   - Navigate to **Settings** -> **Actions** -> **General**.
   - Under **Workflow permissions**, ensure that **"Read and write permissions"** is selected. This is necessary because the action needs to push new commits back to the repository.
   - Click **Save**.

3. **Monitor the Automation**
   - You can see the workflow runs in the **Actions** tab of your repository.
   - It will run automatically every day at 00:00 UTC.
   - If you want to trigger it manually to test or start the cycle right away, you can use the **Run workflow** button on the workflow page.

## How it works

- The state of the 5-day cycle is stored in `state.json`. It tracks which day (1 to 5) the script is currently on.
- The `auto_commit.py` script reads the state, makes the corresponding number of commits by appending to `commit_log.txt`, updates the state to the next day on its final commit of the day, and then pushes back to the remote branch.

### Commit Loop Rules
- **Day 1**: 2 commits
- **Day 2**: 4 commits
- **Day 3**: 1 commit
- **Day 4**: 5 commits
- **Day 5**: 7 commits
- **Day 6**: Resets back to Day 1.
