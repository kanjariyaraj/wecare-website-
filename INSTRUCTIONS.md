# Auto-Commit Loop Automation

This repository contains a fully automated setup to create commits in a looping 5-day pattern:
- **Day 1**: 2 commits
- **Day 2**: 4 commits
- **Day 3**: 1 commit
- **Day 4**: 5 commits
- **Day 5**: 7 commits

After Day 5, the loop resets back to Day 1.

## How It Works

1. **`auto_commit.py`**: A Python script that:
   - Reads the current day from `state.json`.
   - Modifies `commit_log.txt` by appending random text and a timestamp for each commit.
   - Stages and commits the files using a bot profile.
   - On the final commit of the day, updates `state.json` to the next day in the loop.
   - Pushes all commits to the `main` branch.
2. **`state.json`**: Keeps track of the current day in the loop (1 through 5).
3. **`commit_log.txt`**: The file being intentionally modified by the script so git detects a change.
4. **`.github/workflows/auto_commit.yml`**: A GitHub Actions workflow that executes the Python script every day at midnight (UTC) via a cron schedule, or on-demand manually.

## Deployment Setup

To deploy this in your own GitHub repository, follow these steps:

### 1. Ensure Files Exist
Ensure all the files (`auto_commit.py`, `state.json`, `commit_log.txt`, and `.github/workflows/auto_commit.yml`) are present in your `main` branch.

### 2. Configure GitHub Actions Permissions
By default, GitHub Actions might not have permission to push code back to the repository.
To enable this:
1. Go to your repository on GitHub.
2. Click on **Settings** > **Actions** > **General**.
3. Scroll down to the **Workflow permissions** section.
4. Select **Read and write permissions**.
5. Ensure that the option to **Allow GitHub Actions to create and approve pull requests** is checked (optional depending on strictness, but write permission is required).
6. Click **Save**.

### 3. Testing the Action Manually
Instead of waiting for the cron schedule (midnight UTC), you can run the workflow manually to test it:
1. Go to the **Actions** tab in your repository.
2. Under "All workflows", click on **Auto Commit Loop**.
3. Click the **Run workflow** dropdown on the right side.
4. Leave the branch as `main` and click **Run workflow**.

Wait for the action to complete. Check your commit history, and you should see the new commits added, and `state.json` incremented to the next day!

## Local Testing
If you wish to test the script locally without pushing:
1. Clone the repository.
2. Edit `auto_commit.py` to comment out the `run_command(f'git push origin {BRANCH}')` line temporarily.
3. Run `python auto_commit.py`.
4. Inspect your local git history with `git log` and see the changes made to `commit_log.txt` and `state.json`.
