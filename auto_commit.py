import os
import json
import datetime
import subprocess
import random
import string
import sys

STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

COMMITS_PER_DAY = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {cmd}")
        print(result.stderr)
        raise Exception(result.stderr)
    return result.stdout.strip()

def setup_git():
    run_cmd('git config --local user.name "github-actions[bot]"')
    run_cmd('git config --local user.email "github-actions[bot]@users.noreply.github.com"')

def get_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {"day": 1}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)

def append_log():
    timestamp = datetime.datetime.now().isoformat()
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - Auto commit entry: {random_str}\n")

def main():
    setup_git()

    state = get_state()
    current_day = state.get("day", 1)

    if current_day not in COMMITS_PER_DAY:
        current_day = 1

    num_commits = COMMITS_PER_DAY[current_day]
    print(f"Today is day {current_day} of the loop. Making {num_commits} commits.")

    # Calculate next day
    next_day = current_day + 1
    if next_day > 5:
        next_day = 1

    for i in range(num_commits):
        append_log()
        run_cmd(f'git add {LOG_FILE}')

        # If this is the last commit of the day, update the state file
        if i == num_commits - 1:
            state["day"] = next_day
            save_state(state)
            run_cmd(f'git add {STATE_FILE}')

        commit_msg = f"Auto commit {i+1}/{num_commits} for day {current_day}"
        run_cmd(f'git commit -m "{commit_msg}"')
        print(f"Created commit: {commit_msg}")

    # Push changes
    print("Pushing changes to main branch...")
    try:
        run_cmd("git push origin main")
        print("Successfully pushed changes.")
    except Exception as e:
        print("Could not push changes:")
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
