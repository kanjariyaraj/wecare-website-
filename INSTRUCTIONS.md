# Auto Commit Automation Setup Instructions

This repository contains a Python script and a GitHub Actions workflow to automate a specific 5-day cycle of Git commits:
- **Day 1**: 2 commits
- **Day 2**: 4 commits
- **Day 3**: 1 commit
- **Day 4**: 5 commits
- **Day 5**: 7 commits

After Day 5, it resets to Day 1. The script maintains state in `state.json` and logs commits in `commit_log.txt`.

## Prerequisites
- A GitHub repository.
- Python 3.x installed locally (if you want to test locally).

## Local Testing
1. Ensure `state.json` and `commit_log.txt` exist or will be created on the first run.
2. Run the script:
   ```bash
   python auto_commit.py
   ```
3. This will create local commits based on the current day in `state.json`, update the day, and attempt to push. (Note: the push will fail if you haven't set up your remote tracking or if you're not authenticated to push).

## Deployment to GitHub

1. **Commit the Configuration Files**: Ensure `auto_commit.py`, `.github/workflows/auto_commit.yml`, `state.json`, and `commit_log.txt` are committed to your repository's main branch.
2. **Enable GitHub Actions**:
   - Go to your repository on GitHub.
   - Click the **Actions** tab.
   - If prompted, click **I understand my workflows, go ahead and enable them**.
3. **Workflow Permissions**:
   - Go to **Settings** > **Actions** > **General** in your repository.
   - Under **Workflow permissions**, ensure **Read and write permissions** is selected. This allows the bot to push commits back to the repository.
   - Save your changes.
4. **Triggering the Workflow**:
   - The workflow runs automatically at midnight UTC every day.
   - To trigger it manually for testing, go to the **Actions** tab, select the **Auto Commit** workflow on the left, and click the **Run workflow** dropdown on the right side. Select your branch and click **Run workflow**.

## Modifying the Cycle
If you wish to change the commit counts or cycle duration, modify the `COMMITS_PER_DAY` dictionary in `auto_commit.py` and adjust the wrapping logic in the `make_commit` function.