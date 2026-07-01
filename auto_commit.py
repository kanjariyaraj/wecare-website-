import json
import os
import random
import string
import subprocess
import datetime
import time
import sys

# Constants
STATE_FILE = 'state.json'
LOG_FILE = 'commit_log.txt'
COMMIT_CYCLE = [2, 4, 1, 5, 7]  # Days 1 to 5 commit counts

def setup_git():
    """Configures git for the local environment, useful for CI/CD."""
    try:
        # Use existing git config if available, otherwise set defaults
        subprocess.run(["git", "config", "user.name"], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError:
        print("Git user.name not set. Configuring defaults...")
        subprocess.run(["git", "config", "user.name", "github-actions[bot]"], check=True)
        subprocess.run(["git", "config", "user.email", "github-actions[bot]@users.noreply.github.com"], check=True)

def read_state():
    """Reads the current state from the JSON file."""
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, 'r') as f:
                state = json.load(f)
                return state
        except json.JSONDecodeError:
            print(f"Error reading {STATE_FILE}. Starting fresh.")

    return {"current_day_index": 0}

def write_state(state):
    """Writes the current state back to the JSON file."""
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=4)

def generate_random_string(length=10):
    """Generates a random string of fixed length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def perform_commit(commit_number, total_commits, is_final_commit, next_day_index):
    """Performs a single commit by modifying the log file."""
    timestamp = datetime.datetime.now().isoformat()
    random_text = generate_random_string(16)
    log_entry = f"Commit {commit_number}/{total_commits} on {timestamp} - {random_text}\n"

    # Modify the log file
    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)

    # Stage the log file
    subprocess.run(["git", "add", LOG_FILE], check=True)

    # If it's the final commit of the day, update and stage the state file too
    if is_final_commit:
        print(f"Final commit for today. Updating state to next day index: {next_day_index}")
        new_state = {"current_day_index": next_day_index}
        write_state(new_state)
        subprocess.run(["git", "add", STATE_FILE], check=True)

    # Make the commit
    commit_msg = f"Automated commit: {commit_number} of {total_commits} [{timestamp}]"
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)
    print(f"Committed: {commit_msg}")

def main():
    print("Starting automated commit process...")
    setup_git()

    # Ensure log file exists
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w') as f:
            f.write("Automated Commit Log\n====================\n")

    # Read current state
    state = read_state()
    current_day_index = state.get("current_day_index", 0)

    # Validate state
    if not isinstance(current_day_index, int) or current_day_index < 0 or current_day_index >= len(COMMIT_CYCLE):
        print(f"Invalid state detected: {current_day_index}. Resetting to 0.")
        current_day_index = 0

    commits_to_make = COMMIT_CYCLE[current_day_index]
    print(f"Today is Day {current_day_index + 1} of the cycle.")
    print(f"Targeting {commits_to_make} commits for today.")

    # Calculate next day index (wrap around if needed)
    next_day_index = (current_day_index + 1) % len(COMMIT_CYCLE)

    # Perform commits
    for i in range(1, commits_to_make + 1):
        is_final_commit = (i == commits_to_make)
        perform_commit(i, commits_to_make, is_final_commit, next_day_index)

        if not is_final_commit:
            # Small sleep to ensure unique timestamps if they are very fast
            time.sleep(1)

    # Push the changes
    try:
        # Check if we are running in CI context (GitHub Actions)
        if os.environ.get("GITHUB_ACTIONS") == "true":
             print("Running in CI, pushing changes...")
             subprocess.run(["git", "push", "origin", "main"], check=True)
        else:
             print("Running locally. Skipping push to avoid accidental local issues.")
             print("You can manually push with: git push origin main")
    except subprocess.CalledProcessError as e:
        print(f"Failed to push changes: {e}")
        sys.exit(1)

    print("Automated commit process completed successfully!")

if __name__ == "__main__":
    main()
