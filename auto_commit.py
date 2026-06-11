import os
import json
import time
import random
import string
import subprocess
from datetime import datetime

STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

# Commit loop rules: Day -> Number of commits
COMMIT_PATTERN = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def run_command(command, check=True):
    """Utility to run a shell command."""
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if check and result.returncode != 0:
        print(f"Error running command: {command}")
        print(f"STDOUT: {result.stdout}")
        print(f"STDERR: {result.stderr}")
        raise RuntimeError(f"Command failed with code {result.returncode}")
    return result

def get_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {"current_day": 1}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)

def setup_git():
    # Setup git configs
    run_command("git config user.name 'github-actions[bot]'")
    run_command("git config user.email 'github-actions[bot]@users.noreply.github.com'")

def append_to_log():
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    timestamp = datetime.now().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] Automated commit. Hash: {random_str}\n")

def main():
    setup_git()
    state = get_state()
    current_day = state.get("current_day", 1)

    num_commits = COMMIT_PATTERN.get(current_day, 2)
    print(f"--- Day {current_day}: Making {num_commits} commits ---")

    for i in range(num_commits):
        append_to_log()
        run_command(f"git add {LOG_FILE}")

        # If it's the last commit of the day, update the state file as well
        if i == num_commits - 1:
            next_day = current_day + 1
            if next_day > 5:
                next_day = 1
            state["current_day"] = next_day
            save_state(state)
            run_command(f"git add {STATE_FILE}")

        commit_msg = f"Automated commit {i+1}/{num_commits} for Day {current_day}"
        run_command(f"git commit -m \"{commit_msg}\"")

        # Small sleep to ensure timestamps are slightly different
        time.sleep(1)

    print("Pushing to remote...")
    # Push the commits. We don't want the script to fail locally if there's no remote configured.
    try:
        run_command("git push origin main", check=True)
        print("Pushed successfully.")
    except Exception as e:
        print("Push failed or no remote configured (expected when testing locally without a remote).")

if __name__ == "__main__":
    main()
