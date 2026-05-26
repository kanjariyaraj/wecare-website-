import json
import os
import random
import string
import subprocess
import time
from datetime import datetime

STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

# Commit rules based on the current day
COMMIT_RULES = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def get_random_string(length=10):
    """Generates a random string of fixed length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def read_state():
    """Reads the current day from the state file."""
    if not os.path.exists(STATE_FILE):
        return {"current_day": 1}
    with open(STATE_FILE, "r") as f:
        return json.load(f)

def write_state(state):
    """Writes the updated state to the state file."""
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)

def run_git_command(command_list):
    """Runs a git command using subprocess."""
    try:
        subprocess.run(command_list, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {' '.join(command_list)}")
        print(e.stderr.decode("utf-8"))
        raise

def make_commit(day, commit_num, total_commits, is_last_commit=False, next_day=None):
    """Modifies the log file and creates a git commit."""
    # Append random text and timestamp to the log file
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_text = get_random_string(15)

    with open(LOG_FILE, "a") as f:
        f.write(f"Day {day} - Commit {commit_num}/{total_commits} | Timestamp: {timestamp} | Rand: {random_text}\n")

    # Stage the log file
    run_git_command(["git", "add", LOG_FILE])

    # If this is the last commit of the day, update the state file and stage it
    if is_last_commit and next_day is not None:
        state = read_state()
        state["current_day"] = next_day
        write_state(state)
        run_git_command(["git", "add", STATE_FILE])

    # Create the commit
    commit_msg = f"Auto commit: Day {day} - Commit {commit_num} of {total_commits}"
    run_git_command(["git", "commit", "-m", commit_msg])
    print(f"Successfully created commit: {commit_msg}")

def main():
    # Read the current day
    state = read_state()
    current_day = state.get("current_day", 1)

    # Make sure current_day is within valid bounds (1-5)
    if current_day not in COMMIT_RULES:
        current_day = 1

    num_commits = COMMIT_RULES[current_day]
    print(f"--- Starting Auto Commit Script ---")
    print(f"Current Day: {current_day}")
    print(f"Commits to make today: {num_commits}")

    # Calculate next day
    next_day = current_day + 1
    if next_day > 5:
        next_day = 1

    # Make the required number of commits
    for i in range(1, num_commits + 1):
        is_last_commit = (i == num_commits)
        make_commit(current_day, i, num_commits, is_last_commit, next_day)
        # Small sleep to ensure timestamps are slightly different
        if not is_last_commit:
            time.sleep(1)

    print(f"Finished making commits. Next day will be Day {next_day}")

if __name__ == "__main__":
    main()
