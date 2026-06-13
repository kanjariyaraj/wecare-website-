import os
import json
import subprocess
import datetime
import random
import string

# Configuration
STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"
BRANCH = "main"

# Commit loop mapping
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

def load_state():
    """Loads the current day from the state file."""
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r") as f:
                state = json.load(f)
                return state.get("day", 1)
        except json.JSONDecodeError:
            return 1
    return 1

def save_state(day):
    """Saves the current day to the state file."""
    with open(STATE_FILE, "w") as f:
        json.dump({"day": day}, f, indent=4)

def generate_random_string(length=10):
    """Generates a random alphanumeric string."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def make_commit(day, commit_index, total_commits):
    """Modifies the log file and makes a git commit."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_str = generate_random_string()

    # Modify the log file
    with open(LOG_FILE, "a") as f:
        f.write(f"Commit for Day {day} ({commit_index}/{total_commits}) - Timestamp: {timestamp} - ID: {random_str}\n")

    # Configure git (ensure these are set, usually good for CI environments)
    # We use local config so it only applies to this repo
    subprocess.run(["git", "config", "user.name", "github-actions[bot]"], check=False)
    subprocess.run(["git", "config", "user.email", "github-actions[bot]@users.noreply.github.com"], check=False)

    # Stage files
    subprocess.run(["git", "add", LOG_FILE, STATE_FILE], check=True)

    # Create commit
    commit_message = f"Auto commit: Day {day} - {commit_index}/{total_commits} [{random_str}]"
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

def main():
    current_day = load_state()
    commits_to_make = COMMIT_PATTERN.get(current_day, 2)

    print(f"Starting auto-commit script for Day {current_day}. Target commits: {commits_to_make}")

    for i in range(1, commits_to_make + 1):
        # Update the state file on the LAST commit to point to the next day
        if i == commits_to_make:
            next_day = current_day + 1
            if next_day > 5:
                next_day = 1
            save_state(next_day)
            print(f"Updated state to Day {next_day} for the next run.")
        else:
            save_state(current_day)

        make_commit(current_day, i, commits_to_make)
        print(f"Successfully made commit {i}/{commits_to_make}")

    # Push to origin
    try:
        # Push only if running in CI to avoid accidental pushes during local testing
        if os.environ.get("GITHUB_ACTIONS"):
            print(f"Pushing changes to origin/{BRANCH}...")
            # Authenticate using standard GITHUB_TOKEN provided by Actions
            subprocess.run(["git", "push", "origin", BRANCH], check=True)
            print("Push successful.")
        else:
            print("Not running in GitHub Actions. Skipping git push.")
    except subprocess.CalledProcessError as e:
        print(f"Error pushing to repository: {e}")
        exit(1)

if __name__ == "__main__":
    main()
