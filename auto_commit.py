import json
import os
import random
import string
import subprocess
import time
from datetime import datetime

# Configuration
STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"
BRANCH = "main"

# Commit mapping based on the 5-day cycle
COMMITS_PER_DAY = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def run_cmd(cmd):
    """Run a shell command and print the output."""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error executing command: {result.stderr}")
    return result

def setup_git():
    """Setup git configuration for commits."""
    # We use local config so we don't mess up global user settings
    run_cmd(["git", "config", "user.name", "Auto Commit Bot"])
    run_cmd(["git", "config", "user.email", "auto-commit-bot@users.noreply.github.com"])

def get_state():
    """Read the current state from the state file."""
    if not os.path.exists(STATE_FILE):
        return {"current_day": 1}
    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {"current_day": 1}

def save_state(state):
    """Save the updated state back to the state file."""
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)

def generate_random_text():
    """Generate a random alphanumeric string."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=15))

def main():
    # Ensure git config is ready
    setup_git()

    # Read state and determine current day
    state = get_state()
    current_day = state.get("current_day", 1)

    # Fallback in case of an invalid state
    if current_day not in COMMITS_PER_DAY:
        current_day = 1

    num_commits = COMMITS_PER_DAY[current_day]
    print(f"--- Starting Daily Run ---")
    print(f"Day {current_day} of 5-day cycle. Scheduled commits: {num_commits}")

    for i in range(1, num_commits + 1):
        # 1. Modify the log file to generate a distinct diff
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        random_text = generate_random_text()
        log_entry = f"{timestamp} - Day {current_day} | Commit {i}/{num_commits} | ID: {random_text}\n"

        with open(LOG_FILE, "a") as f:
            f.write(log_entry)

        # 2. On the final commit of the loop, update state.json
        if i == num_commits:
            next_day = current_day + 1 if current_day < 5 else 1
            state["current_day"] = next_day
            save_state(state)

        # 3. Stage the files
        run_cmd(["git", "add", LOG_FILE])
        if i == num_commits:
            run_cmd(["git", "add", STATE_FILE])

        # 4. Commit the changes
        commit_message = f"Automated update: Day {current_day}, commit {i} of {num_commits}"
        run_cmd(["git", "commit", "-m", commit_message])

        # Short pause to guarantee distinct commit timestamps
        time.sleep(1)

    # 5. Push the changes to the main branch
    print("Pushing all commits to remote...")
    run_cmd(["git", "push", "origin", BRANCH])
    print("Run completed successfully.")

if __name__ == "__main__":
    main()
