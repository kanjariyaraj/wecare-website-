import json
import os
import random
import subprocess
import time
from datetime import datetime

STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

# Rules mapping day to number of commits
COMMITS_PER_DAY = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def load_state():
    if not os.path.exists(STATE_FILE):
        return {"current_day": 1}
    with open(STATE_FILE, "r") as f:
        return json.load(f)

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)

def make_commit(commit_number, total_commits, current_day, is_last_commit=False):
    # Append random text and timestamp to the log file to ensure a real change
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_hex = f"{random.randint(0, 0xFFFFFF):06x}"

    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] Loop Day {current_day} - Commit {commit_number}/{total_commits} [ID: {random_hex}]\n")

    # Stage the log file
    subprocess.run(["git", "add", LOG_FILE], check=True)

    commit_msg = f"Auto commit {commit_number}/{total_commits} for loop day {current_day} ({random_hex})"

    # If this is the last commit of the loop, advance the state and bundle it in this commit
    if is_last_commit:
        next_day = current_day + 1
        if next_day > 5:
            next_day = 1

        state = {"current_day": next_day}
        save_state(state)
        subprocess.run(["git", "add", STATE_FILE], check=True)
        commit_msg += f" (Advanced to loop day {next_day})"

    # Create the commit
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)
    print(f"Created commit: {commit_msg}")

def main():
    state = load_state()
    current_day = state.get("current_day", 1)

    # Validation in case the state somehow gets corrupted
    if current_day not in COMMITS_PER_DAY:
        current_day = 1

    num_commits = COMMITS_PER_DAY[current_day]
    print(f"--- Starting automated commits for Loop Day {current_day} ({num_commits} commits) ---")

    for i in range(1, num_commits + 1):
        is_last = (i == num_commits)
        make_commit(i, num_commits, current_day, is_last_commit=is_last)
        # Small sleep to ensure timestamps differ slightly if needed
        time.sleep(1)

if __name__ == "__main__":
    # Ensure git is tracking state and log
    if not os.path.exists(STATE_FILE):
        save_state({"current_day": 1})
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("Auto-Commit Log\n================\n")

    main()
