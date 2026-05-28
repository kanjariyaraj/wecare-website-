import json
import os
import random
import string
import subprocess
from datetime import datetime

# Configuration
STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

# Commit loop rules: day -> number of commits
# Day 1: 2 commits
# Day 2: 4 commits
# Day 3: 1 commit
# Day 4: 5 commits
# Day 5: 7 commits
COMMIT_PATTERN = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def run_cmd(command):
    """Utility to run shell commands."""
    try:
        result = subprocess.run(
            command,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {' '.join(command)}")
        print(f"Stderr: {e.stderr}")
        raise

def get_current_day():
    """Reads the current day from the state file."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            try:
                state = json.load(f)
                return state.get("day", 1)
            except json.JSONDecodeError:
                return 1
    return 1

def save_current_day(day):
    """Saves the current day to the state file."""
    with open(STATE_FILE, "w") as f:
        json.dump({"day": day}, f, indent=4)

def generate_random_text(length=12):
    """Generates a random string of fixed length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def make_commit(commit_index, total_commits, day):
    """Modifies the log file, stages files, and makes a commit."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_str = generate_random_text()

    # Append to the log file
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] Loop Day: {day} | Commit: {commit_index}/{total_commits} | ID: {random_str}\n")

    # Stage the changed files
    run_cmd(["git", "add", LOG_FILE, STATE_FILE])

    # Commit changes
    commit_msg = f"Automated commit: Day {day} - {commit_index}/{total_commits}"
    run_cmd(["git", "commit", "-m", commit_msg])

    print(f"Created commit: '{commit_msg}'")

def setup_git():
    """Configures git user details. Primarily for CI/CD environments."""
    # Check if inside GitHub Actions
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print("Configuring git for GitHub Actions...")
        run_cmd(["git", "config", "--global", "user.name", "github-actions[bot]"])
        run_cmd(["git", "config", "--global", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"])

def main():
    setup_git()

    current_day = get_current_day()

    # Ensure current day is within 1-5 loop
    if current_day not in COMMIT_PATTERN:
        current_day = 1

    commits_to_make = COMMIT_PATTERN[current_day]
    print(f"Starting loop for Day {current_day}. Making {commits_to_make} commits.")

    # Update day for tomorrow (loop back to 1 after 5)
    # We save this BEFORE making commits, so that the new state
    # is staged and committed during the commit loop!
    next_day = current_day + 1
    if next_day > 5:
        next_day = 1

    save_current_day(next_day)

    # Create the commits for today
    for i in range(1, commits_to_make + 1):
        make_commit(i, commits_to_make, current_day)

    # Push changes back to remote
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print("Pushing commits to remote...")
        # Using 'git push' works automatically in GH Actions assuming we use checkout@v3
        # with the standard GITHUB_TOKEN
        run_cmd(["git", "push"])
        print("Successfully pushed to remote.")
    else:
        print("Skipping push as this is not running in GitHub Actions.")

if __name__ == "__main__":
    main()
