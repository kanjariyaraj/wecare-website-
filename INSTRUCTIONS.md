# Auto Commit Loop - Setup and Deployment Instructions

This repository is configured with an automated commit script (`auto_commit.py`) managed by a GitHub Actions workflow (`.github/workflows/auto_commit.yml`).

The automation follows a strict 5-day recurring cycle:
- **Day 1:** 2 commits
- **Day 2:** 4 commits
- **Day 3:** 1 commit
- **Day 4:** 5 commits
- **Day 5:** 7 commits

The loop tracks its current day using `state.json` and creates genuine git changes by appending timestamped lines to `commit_log.txt`.

## 1. Setup GitHub Actions Permissions

For the automated bot to push commits back to the main branch, you must ensure the repository grants write permissions to the default `GITHUB_TOKEN`.

1. Go to your repository on GitHub.
2. Click on **Settings**.
3. In the left sidebar, click on **Actions** > **General**.
4. Scroll down to the **Workflow permissions** section.
5. Select **Read and write permissions**.
6. Ensure **Allow GitHub Actions to create and approve pull requests** is checked.
7. Click **Save**.

## 2. Triggering the Workflow Manually

By default, the workflow runs every day at 12:00 PM UTC. You can also trigger it manually:

1. Go to your repository on GitHub.
2. Click on the **Actions** tab.
3. In the left sidebar, click on **Auto Commit Loop** under "All workflows".
4. On the right side, click the **Run workflow** dropdown.
5. Select the branch (e.g., `main`) and click the **Run workflow** button.

## 3. Testing Locally

If you want to test the script locally without pushing to GitHub:

1. Ensure you have Python 3 installed.
2. Ensure you have Git installed and initialized in the repository.
3. Run the script:
   ```bash
   python auto_commit.py
   ```
4. The script will output its progress, update `state.json`, modify `commit_log.txt`, and create the appropriate number of local commits.
5. Because you are running it locally, it may print an expected error if it cannot push to a remote repository.
6. Check the local commit history to verify:
   ```bash
   git log --oneline
   ```
