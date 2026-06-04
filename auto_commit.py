import json
import os

STATE_FILE = "state.json"

def load_state():
    """Loads the current day from the state file."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            try:
                state = json.load(f)
                return state.get("day", 1)
            except json.JSONDecodeError:
                return 1
    return 1

def save_state(day):
    """Saves the current day to the state file."""
    with open(STATE_FILE, "w") as f:
        json.dump({"day": day}, f, indent=4)

def get_next_day(current_day):
    """Calculates the next day in the 5-day cycle."""
    if current_day >= 5:
        return 1
    return current_day + 1

import subprocess
import time
import random
import string

LOG_FILE = "commit_log.txt"

def setup_git():
    """Sets up git configuration if running in CI environment."""
    # Check if we are in GitHub Actions
    if os.environ.get("GITHUB_ACTIONS"):
        subprocess.run(["git", "config", "--global", "user.name", "github-actions[bot]"], check=True)
        subprocess.run(["git", "config", "--global", "user.email", "github-actions[bot]@users.noreply.github.com"], check=True)

def append_to_log(commit_num, total_commits, day):
    """Appends random text and timestamp to the log file."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] Loop Day {day} - Commit {commit_num}/{total_commits} - Hash: {random_str}\n")

    return timestamp

def make_commit(commit_num, total_commits, day):
    """Makes a single commit."""
    timestamp = append_to_log(commit_num, total_commits, day)

    subprocess.run(["git", "add", LOG_FILE], check=True)
    subprocess.run(["git", "add", STATE_FILE], check=True)

    commit_msg = f"Auto-commit: Loop Day {day} ({commit_num}/{total_commits}) - {timestamp}"
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)

def push_changes():
    """Pushes changes to the main branch."""
    # We will try to push to main, if not specified, it will push to the current branch
    try:
        subprocess.run(["git", "push", "origin", "main"], check=True)
    except subprocess.CalledProcessError:
        # Fallback to just git push if origin/main is not set up correctly or we are on a different branch locally
        print("Pushing to main failed, trying default push...")
        subprocess.run(["git", "push"], check=True)

if __name__ == "__main__":
    # Commits per day mapping
    commits_schedule = {
        1: 2,
        2: 4,
        3: 1,
        4: 5,
        5: 7
    }

    # 1. Setup git (if needed)
    setup_git()

    # 2. Load state
    current_day = load_state()
    commits_to_make = commits_schedule.get(current_day, 2)
    print(f"Starting auto-commit process for Day {current_day}. Making {commits_to_make} commits.")

    # 3. Update state for the next run (we do this now so it's included in the commits)
    next_day = get_next_day(current_day)
    save_state(next_day)

    # 4. Make commits
    for i in range(1, commits_to_make + 1):
        print(f"Making commit {i}/{commits_to_make}...")
        make_commit(i, commits_to_make, current_day)
        # Sleep briefly to ensure distinct timestamps
        if i < commits_to_make:
            time.sleep(1)

    # 5. Push changes
    print("Pushing changes to remote...")
    try:
        push_changes()
        print("Successfully completed auto-commit process.")
    except Exception as e:
        print(f"Error pushing changes: {e}")
        # Note: If running locally without a remote, push will fail.
        # But the commits are still created.
