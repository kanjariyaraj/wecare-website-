# Daily Automated Commits Setup

This repository contains a Python script and a GitHub Actions workflow to automate daily commits based on a 5-day cycle:
- Day 1: 2 commits
- Day 2: 4 commits
- Day 3: 1 commit
- Day 4: 5 commits
- Day 5: 7 commits

## How to Deploy in Your Repository

1. **Copy the Files**: Ensure the following files are in the root of your GitHub repository:
   - `auto_commit.py`
   - `state.json` (Initialize with `{"day": 1}`)
   - `commit_log.txt` (Can be empty)
   - `.github/workflows/auto_commit.yml` (Must be in `.github/workflows/` directory)

2. **Commit and Push**: Commit these files to your `main` branch and push to GitHub.

3. **Check Workflow Permissions**:
   - Go to your repository settings on GitHub: `Settings` -> `Actions` -> `General`.
   - Scroll down to "Workflow permissions".
   - Ensure "Read and write permissions" is selected. This allows the GitHub Action to push the automated commits back to your repository.
   - Click "Save".

4. **Verify Workflow**:
   - Go to the "Actions" tab in your repository.
   - You should see the "Automated Daily Commits" workflow.
   - You can manually trigger it to test by clicking "Run workflow" (thanks to the `workflow_dispatch` configuration).
   - Once it runs successfully, check your commit history. You should see new automated commits and updates to `state.json` and `commit_log.txt`.

5. **Let it Run**: The workflow is configured to run automatically every day at 00:00 UTC using a cron schedule.