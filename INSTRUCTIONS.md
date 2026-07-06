# Auto-Commit Loop Automation

This repository contains an automated script that makes commits to the repository based on a specific daily loop pattern:
- Day 1: 2 commits
- Day 2: 4 commits
- Day 3: 1 commit
- Day 4: 5 commits
- Day 5: 7 commits
- Day 6 (and beyond): Resets to Day 1

The automation is powered by a Python script (`auto_commit.py`) and executed daily via GitHub Actions (`.github/workflows/auto_commit.yml`).

## How it works

1. **The Script (`auto_commit.py`)**:
   - Tracks the current loop day in `state.json`.
   - Modifies `commit_log.txt` by appending random text and timestamps.
   - For the final commit of the daily batch, the script updates `state.json` to the next day and commits it alongside `commit_log.txt` (to avoid adding an extra commit and violating the loop pattern).
   - Configures git, creates commits with distinct messages, and pushes them back to the repository.

2. **The Automation (`.github/workflows/auto_commit.yml`)**:
   - Runs daily at 12:00 UTC using a cron schedule (`0 12 * * *`).
   - Can also be triggered manually using `workflow_dispatch`.

## Setup Instructions

To deploy this automation to your own GitHub repository, follow these steps:

1. **Ensure all files are in the repository:**
   Make sure `auto_commit.py`, `.github/workflows/auto_commit.yml`, and this `INSTRUCTIONS.md` are pushed to your repository's default branch (usually `main`).

2. **Enable Read and Write Permissions for GitHub Actions:**
   By default, GitHub Actions might only have read access to your repository. Since this script needs to push commits back to the repo, you must grant it write access.
   - Go to your GitHub repository.
   - Click on **Settings**.
   - On the left sidebar, under **Code and automation**, click on **Actions** > **General**.
   - Scroll down to the **Workflow permissions** section.
   - Select **Read and write permissions**.
   - Click **Save**.

3. **Verify the Workflow:**
   - Go to the **Actions** tab in your repository.
   - You should see the `Auto Commit` workflow listed on the left.
   - You can test it immediately by clicking on `Auto Commit`, then clicking the **Run workflow** dropdown on the right side, and clicking the green **Run workflow** button.

4. **Monitor the Setup:**
   The workflow will now run automatically every day at 12:00 UTC. You can view its logs under the **Actions** tab, and you'll see new commits appearing in your commit history.

## Local Testing
To test the script locally, ensure you have Python 3 installed. You can run the script manually:
```bash
python auto_commit.py
```
This will create commits in your local git repository. Ensure your git working directory is clean or you are prepared to push the commits.
