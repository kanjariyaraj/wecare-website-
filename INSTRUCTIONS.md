# Automated Commits Setup

This repository contains an automated script (`auto_commit.py`) that makes daily commits based on a 5-day cycle:
- Day 1: 2 commits
- Day 2: 4 commits
- Day 3: 1 commit
- Day 4: 5 commits
- Day 5: 7 commits

The cycle resets to Day 1 after Day 5.

## Deployment Instructions

1. **Commit these files to the main branch:**
   Ensure `auto_commit.py`, `state.json`, `commit_log.txt`, and `.github/workflows/auto_commit.yml` are committed and pushed to the repository.

2. **GitHub Actions Settings:**
   - The workflow uses the `permissions: contents: write` block to automatically give the GitHub Actions bot permission to push back to the repository.
   - If you have branch protection rules on `main`, you might need to allow the `github-actions[bot]` to bypass pull requests or use a Personal Access Token (PAT) instead of the default `GITHUB_TOKEN`.

3. **Manual Trigger:**
   You can manually trigger the workflow from the "Actions" tab in your GitHub repository by selecting the "Automated Commits" workflow and clicking "Run workflow".

## Local Testing

If you want to run the script locally to test the behavior:

1. Ensure you have Python 3 installed.
2. Run the script: `python auto_commit.py`
3. The script will create commits and push them to your current branch. Make sure you are on the right branch before running it locally!
