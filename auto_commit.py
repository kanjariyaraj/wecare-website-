import os
import json
import random
import subprocess
from datetime import datetime

# Configuration
STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"
BRANCH = "main"

# Commit loop rules
COMMIT_LOOP = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def run_command(command):
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result

def get_state():
    if not os.path.exists(STATE_FILE):
        return {"day": 1}
    with open(STATE_FILE, "r") as f:
        try:
            state = json.load(f)
            return state
        except json.JSONDecodeError:
            return {"day": 1}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)

def update_log(commit_num, total_commits, current_day):
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"Day {current_day} - Commit {commit_num}/{total_commits} at {timestamp} - {random.randint(1000, 9999)}\n")

def main():
    state = get_state()
    current_day = state.get("day", 1)

    if current_day not in COMMIT_LOOP:
        current_day = 1

    num_commits = COMMIT_LOOP[current_day]
    print(f"--- Day {current_day} - Making {num_commits} commits ---")

    # Ensure git config exists (mostly for GitHub Actions)
    # We use a generic bot if none is configured
    try:
        subprocess.run(["git", "config", "user.name"], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        run_command(["git", "config", "--global", "user.name", "github-actions[bot]"])
        run_command(["git", "config", "--global", "user.email", "github-actions[bot]@users.noreply.github.com"])

    for i in range(1, num_commits + 1):
        update_log(i, num_commits, current_day)
        run_command(["git", "add", LOG_FILE])

        if i == num_commits:
            # Last commit of the day, update the state file
            next_day = current_day + 1 if current_day < 5 else 1
            state["day"] = next_day
            save_state(state)

            run_command(["git", "add", STATE_FILE])
            commit_msg = f"Automated commit: Day {current_day}, Commit {i}/{num_commits} (State updated to day {next_day})"
        else:
            commit_msg = f"Automated commit: Day {current_day}, Commit {i}/{num_commits}"

        run_command(["git", "commit", "-m", commit_msg])

    print("Pushing to remote...")
    run_command(["git", "push", "origin", BRANCH])

    print("Automated commits completed successfully.")

if __name__ == "__main__":
    main()
