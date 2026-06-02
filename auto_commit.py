import os
import json
import random
import string
import subprocess
from datetime import datetime

# Configuration
STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"
BRANCH = "main"

# Commit cycle pattern
COMMIT_PATTERN = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def run_cmd(cmd):
    """Run a shell command and return its output."""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
    return result.stdout.strip()

def setup_git():
    """Configure Git username and email."""
    try:
        run_cmd("git config user.name 'github-actions[bot]'")
        run_cmd("git config user.email 'github-actions[bot]@users.noreply.github.com'")
    except subprocess.CalledProcessError as e:
        print(f"Error configuring git: {e}")

def get_current_day():
    """Read the current day from the state file."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            try:
                state = json.load(f)
                return state.get("day", 1)
            except json.JSONDecodeError:
                return 1
    return 1

def update_state(next_day):
    """Update the state file with the next day."""
    with open(STATE_FILE, "w") as f:
        json.dump({"day": next_day}, f, indent=4)

def generate_random_text(length=10):
    """Generate random text to append to the log."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def make_commit(commit_number, total_commits, day, is_last_commit=False, next_day=None):
    """Create a single commit by modifying the log file.
    If it's the last commit, also update and commit the state file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_str = generate_random_text()
    log_entry = f"Day {day} - Commit {commit_number}/{total_commits} - {timestamp} - {random_str}\n"

    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

    run_cmd(f"git add {LOG_FILE}")

    if is_last_commit and next_day is not None:
        update_state(next_day)
        run_cmd(f"git add {STATE_FILE}")
        commit_msg = f"Automated commit: Day {day}, {commit_number} of {total_commits} (State updated to Day {next_day})"
    else:
        commit_msg = f"Automated commit: Day {day}, {commit_number} of {total_commits}"

    run_cmd(f"git commit -m \"{commit_msg}\"")

def main():
    setup_git()

    current_day = get_current_day()
    if current_day not in COMMIT_PATTERN:
        current_day = 1

    commits_to_make = COMMIT_PATTERN[current_day]
    print(f"Starting auto-commit process for Day {current_day}. Making {commits_to_make} commits.")

    # Calculate next day
    next_day = current_day + 1
    if next_day > 5:
        next_day = 1

    for i in range(1, commits_to_make + 1):
        is_last = (i == commits_to_make)
        make_commit(i, commits_to_make, current_day, is_last, next_day)

    # Push all changes
    print(f"Pushing changes to origin/{BRANCH}...")
    try:
        run_cmd(f"git push origin HEAD:{BRANCH}")
    except subprocess.CalledProcessError as e:
        # Re-raise to fail the CI job if we can't push, except if running locally with no remote
        if os.environ.get("GITHUB_ACTIONS") == "true":
            raise
        else:
            print(f"Warning: git push failed. This is expected if running locally without origin configured: {e}")

    print("Auto-commit process completed successfully.")

if __name__ == "__main__":
    main()