# Auto Commit Loop Setup

This repository contains an automated commit script (`auto_commit.py`) that implements a recurring 5-day cycle of commits:
- Day 1: 2 commits
- Day 2: 4 commits
- Day 3: 1 commit
- Day 4: 5 commits
- Day 5: 7 commits

The cycle repeats indefinitely. The script works by appending data to `commit_log.txt` and tracking the current day of the cycle in `state.json`.

## Deployment Instructions

1. **Commit these files to your repository:**
   Ensure all the following files are pushed to the `main` branch of your GitHub repository:
   - `auto_commit.py`
   - `.github/workflows/auto_commit.yml`
   - `state.json`
   - `commit_log.txt`
   - `INSTRUCTIONS.md`

2. **GitHub Actions Permissions:**
   The workflow requires write permissions to push commits back to the repository.
   - Go to your repository settings on GitHub.
   - Navigate to **Actions** > **General**.
   - Scroll down to the **Workflow permissions** section.
   - Select **Read and write permissions** and click **Save**.

3. **Verify the Workflow:**
   - Go to the **Actions** tab in your repository.
   - You should see the `Auto Commit Loop` workflow listed on the left sidebar.
   - It will automatically run every day at 00:00 UTC.
   - To test it immediately, click on `Auto Commit Loop`, click **Run workflow**, choose the `main` branch, and click the green **Run workflow** button.

## Local Execution (Optional)

If you want to run the script locally to test the behavior:
1. Ensure you have Python installed.
2. Run `python auto_commit.py` from the root of the repository.
3. The script will make commits to your local git repository. You can verify them with `git log`.
4. (Note: If you run it locally without a remote configured, it will make the commits but gracefully skip the push).
