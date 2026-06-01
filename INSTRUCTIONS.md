# Auto Commit Setup Instructions

This repository is configured with an automated commit script (`auto_commit.py`) managed by a GitHub Actions workflow (`.github/workflows/auto_commit.yml`). The automation follows a recurring 5-day cycle where the number of commits made per day follows this specific pattern:

- Day 1: 2 commits
- Day 2: 4 commits
- Day 3: 1 commit
- Day 4: 5 commits
- Day 5: 7 commits

After Day 5, it resets back to Day 1. The script maintains state via `state.json` and updates `commit_log.txt` to generate genuine Git changes.

## Deployment Steps

1. **Commit these files to the main branch of your repository:**
   Ensure the following files are pushed to `main`:
   - `auto_commit.py`
   - `state.json`
   - `commit_log.txt`
   - `.github/workflows/auto_commit.yml`

2. **Verify Workflow Permissions:**
   The `auto_commit.yml` has `permissions: contents: write` which allows it to push back to the repository. Ensure your repository settings allow actions to read and write. Go to **Settings > Actions > General > Workflow permissions** and select **Read and write permissions** if it's not already enabled.

3. **Monitor Execution:**
   The workflow is scheduled to run daily at `00:00 UTC`. You can view its execution status under the **Actions** tab of your GitHub repository.

4. **Manual Trigger (Optional):**
   You can manually trigger the workflow to test it by going to the **Actions** tab, selecting **Auto Commit Loop** from the left sidebar, clicking **Run workflow**, and choosing the main branch. Note that each run will execute one day of the loop and update the state.
