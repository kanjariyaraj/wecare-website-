import json
import os
import random
import string
import subprocess
from datetime import datetime

# Commit counts per day based on the 5-day loop pattern
COMMIT_PATTERN = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

def run_cmd(cmd, check=True):
    """Utility to run shell commands"""
    print(f"Running: {cmd}")
    return subprocess.run(cmd, shell=True, check=check)

def main():
    # Setup git config
    run_cmd('git config user.name "GitHub Actions Bot"', check=False)
    run_cmd('git config user.email "actions@github.com"', check=False)

    # Read the current state
    if not os.path.exists(STATE_FILE):
        state = {"day": 1}
    else:
        with open(STATE_FILE, "r") as f:
            try:
                state = json.load(f)
            except json.JSONDecodeError:
                state = {"day": 1}

    current_day = state.get("day", 1)
    if current_day not in COMMIT_PATTERN:
        current_day = 1

    num_commits = COMMIT_PATTERN[current_day]
    print(f"Current Day: {current_day}. Expected Commits: {num_commits}")

    # Calculate next day for the state update
    next_day = current_day + 1
    if next_day > 5:
        next_day = 1

    for i in range(1, num_commits + 1):
        # 1. Modify the log file
        timestamp = datetime.now().isoformat()
        random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        log_entry = f"Day {current_day}, Commit {i}/{num_commits} at {timestamp} - {random_suffix}\n"

        with open(LOG_FILE, "a") as f:
            f.write(log_entry)

        run_cmd(f'git add {LOG_FILE}')

        # If this is the last commit of the day, update and stage the state file
        if i == num_commits:
            state["day"] = next_day
            with open(STATE_FILE, "w") as f:
                json.dump(state, f, indent=2)
                f.write('\n') # Ensure newline at EOF
            run_cmd(f'git add {STATE_FILE}')

        # Commit with distinct message
        commit_message = f"Auto commit: Day {current_day} - {i}/{num_commits}"
        run_cmd(f'git commit -m "{commit_message}"')

    # Push all commits made today
    # We use check=False so it doesn't crash during local testing if remote isn't setup
    run_cmd("git push origin HEAD", check=False)

if __name__ == "__main__":
    main()
