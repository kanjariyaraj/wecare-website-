# Auto Commit Workflow Instructions

This repository contains an automated script and a GitHub Actions workflow to create a varying number of commits every day based on a specific 5-day cycle.

## Cycle Details

- **Day 1:** 2 commits
- **Day 2:** 4 commits
- **Day 3:** 1 commit
- **Day 4:** 5 commits
- **Day 5:** 7 commits
*(Loop resets after Day 5)*

## How it Works

1. `auto_commit.py` reads `state.json` to find out which day in the cycle we are currently on.
2. It generates the required number of distinct commits by appending timestamps and random hashes to `commit_log.txt`.
3. It creates an individual git commit for each entry.
4. It updates `state.json` to the next day in the cycle (resetting to 1 if it goes past 5) and creates a final commit for that state change.
5. It pushes the changes to the `main` branch.

## Deployment Steps

To deploy this in your repository:

1. **Copy Files**: Ensure the following files are in your repository:
   - `auto_commit.py`
   - `state.json`
   - `commit_log.txt`
   - `.github/workflows/auto_commit.yml`

2. **Commit the Setup**:
   Commit these files to your `main` branch (or whichever is your default).

3. **Check Workflow Permissions**:
   Make sure your GitHub Actions have write permissions to your repository.
   - Go to your repository settings on GitHub.
   - Go to **Actions** > **General**.
   - Under **Workflow permissions**, make sure **Read and write permissions** is selected. Check "Allow GitHub Actions to create and approve pull requests" if necessary. Save the changes.

4. **Monitor / Test**:
   - The action is set up to run every day at 12:00 UTC.
   - You can also trigger it manually by going to the **Actions** tab in GitHub, selecting the "Daily Auto Commit Loop" workflow, and clicking the **Run workflow** button.
   - Verify that the workflow runs successfully and check the commit history on your main branch to ensure the correct number of commits were made.
