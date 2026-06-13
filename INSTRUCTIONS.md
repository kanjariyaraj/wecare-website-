# Auto Commit Loop Setup Instructions

This repository contains a Python script and a GitHub Actions workflow to automate daily commits based on a specific loop pattern.

## The Loop Pattern
The commits follow a 5-day cycle that repeats indefinitely:
- **Day 1:** 2 commits
- **Day 2:** 4 commits
- **Day 3:** 1 commit
- **Day 4:** 5 commits
- **Day 5:** 7 commits

## Files Included
- `auto_commit.py`: The main Python script that handles the logic, updates the state, modifies the log file, and executes git commands.
- `state.json`: A simple JSON file that tracks the current day in the loop (1-5).
- `commit_log.txt`: A text file where the script appends random text and timestamps to ensure genuine file modifications for each commit.
- `.github/workflows/auto_commit.yml`: The GitHub Actions workflow file that schedules the script to run daily at 12:00 UTC.

## Deployment Instructions

### 1. Push to GitHub
Ensure all the provided files are committed and pushed to the `main` branch of your GitHub repository.

```bash
git add auto_commit.py state.json commit_log.txt .github/workflows/auto_commit.yml INSTRUCTIONS.md
git commit -m "Add auto-commit automation setup"
git push origin main
```

### 2. Verify Workflow Permissions
GitHub Actions needs permission to push commits back to the repository. The `.github/workflows/auto_commit.yml` file includes the `permissions: contents: write` block, which usually handles this.
However, you should also ensure your repository settings allow it:
1. Go to your repository on GitHub.
2. Click on **Settings**.
3. Under the **Code and automation** sidebar section, click on **Actions** > **General**.
4. Scroll down to the **Workflow permissions** section.
5. Ensure **Read and write permissions** is selected.
6. Click **Save** if you made a change.

### 3. Manually Trigger the Workflow (Optional)
You can manually test the workflow to ensure it's working correctly:
1. Go to the **Actions** tab in your GitHub repository.
2. Under "All workflows" on the left, click on **Auto Commit Loop**.
3. Click the **Run workflow** dropdown on the right.
4. Click the green **Run workflow** button.
5. Watch the action run and check your repository history for the new commits!

### 4. Automatic Execution
Once pushed, the workflow is automatically scheduled to run every day at 12:00 UTC using the cron schedule defined in `.github/workflows/auto_commit.yml`. No further action is required.

## Testing Locally
If you want to test the script locally without pushing to GitHub, simply run:

```bash
python auto_commit.py
```

The script will detect that it is not running in GitHub Actions (by checking for the `GITHUB_ACTIONS` environment variable) and will make the commits locally, updating the state, but will skip the `git push` step to avoid accidental pushes.
