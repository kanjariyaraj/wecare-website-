# Auto-Commit Loop Automation Setup

This repository contains a complete, production-ready script and GitHub Actions setup to automate commits on a 5-day cycle.

## Loop Pattern
The commit loop strictly follows this pattern:
- **Day 1:** 2 commits
- **Day 2:** 4 commits
- **Day 3:** 1 commit
- **Day 4:** 5 commits
- **Day 5:** 7 commits
- *After Day 5, the loop resets back to Day 1.*

## Files Involved

1. **`auto_commit.py`**: The core Python script that manages the logic.
   - Reads the current day from `state.json`.
   - Determines the number of commits to make based on the schedule.
   - Configures Git (if running in GitHub Actions).
   - Appends random text and a timestamp to `commit_log.txt`.
   - Stages `commit_log.txt` and `state.json`.
   - Creates distinct commits with unique timestamps.
   - Pushes the commits to the `main` branch.

2. **`state.json`**: A JSON file that tracks the current day in the 5-day cycle. It is automatically updated by the script during each run.

3. **`commit_log.txt`**: A log file that is modified by the script to ensure genuine code changes are detected by Git for each commit.

4. **`.github/workflows/auto_commit.yml`**: The GitHub Actions workflow file.
   - Configured to run every day at 12:00 UTC using a cron schedule.
   - Requires `contents: write` permissions to push commits back to the repository.

## How to Deploy / Configure in Your Repository

1. **Copy the Files**: Ensure that all four files mentioned above are present in your repository, matching their respective paths (`.github/workflows/auto_commit.yml` must be in the correct directory).

2. **Ensure Workflow Permissions**:
   - Navigate to your repository on GitHub.
   - Go to **Settings** > **Actions** > **General**.
   - Scroll down to **Workflow permissions**.
   - Make sure **Read and write permissions** is selected. Check the box for **Allow GitHub Actions to create and approve pull requests** if you intend to extend the script's capabilities later, though it is not strictly required for direct pushes to `main`.
   - Click **Save**.

3. **Check Default Branch Name**:
   - The script is configured to push to the `main` branch (`git push origin main`). If your repository uses `master` or a different default branch, update the `push_changes()` function in `auto_commit.py` to target the correct branch.

4. **Test the Action Manually (Optional)**:
   - Go to the **Actions** tab in your repository.
   - Select the **Auto Commit Loop** workflow on the left.
   - Click **Run workflow** on the right side of the screen.
   - Wait for the action to complete, then check your commit history and the updated `state.json`/`commit_log.txt` files to verify it's working.

5. **Sit Back and Relax**:
   - The cron job (`0 12 * * *`) will automatically run the script every day, perpetuating the 5-day cycle.
