import os
import json
import random
import string
import datetime
import subprocess
import sys

STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

# Number of commits per day in the 5-day cycle
COMMITS_PER_DAY = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def run_cmd(cmd):
    """Run a shell command and return the output."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {cmd}\n{result.stderr}")
        sys.exit(1)
    return result.stdout.strip()

def load_state():
    """Load the current state from state.json, or initialize it."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            state = json.load(f)
            return state
    return {"current_day": 1}

def save_state(state):
    """Save the state to state.json."""
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)

def generate_random_string(length=12):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters + string.digits
    return "".join(random.choice(letters) for _ in range(length))

def setup_git():
    """Configure git user if not already set (useful for CI environments)."""
    try:
        run_cmd("git config user.name")
    except:
        run_cmd('git config user.name "GitHub Actions Auto Committer"')

    try:
        run_cmd("git config user.email")
    except:
        run_cmd('git config user.email "actions@github.com"')

def make_commit(commit_msg, is_last_commit, next_state):
    """Make a commit. If it's the last commit of the day, include the state update."""
    # Append to log file
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_str = generate_random_string()
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - Auto commit entry: {random_str}\n")

    run_cmd(f"git add {LOG_FILE}")

    if is_last_commit:
        # Save the new state before the final commit
        save_state(next_state)
        run_cmd(f"git add {STATE_FILE}")

    # Commit changes
    run_cmd(f'git commit -m "{commit_msg}"')

def main():
    setup_git()

    state = load_state()
    current_day = state.get("current_day", 1)

    # Ensure current_day is within valid range (1-5)
    if current_day < 1 or current_day > 5:
        current_day = 1

    num_commits = COMMITS_PER_DAY[current_day]
    print(f"Starting loop for Day {current_day}. Making {num_commits} commit(s).")

    next_day = current_day + 1
    if next_day > 5:
        next_day = 1

    next_state = {"current_day": next_day}

    for i in range(1, num_commits + 1):
        is_last = (i == num_commits)
        msg = f"Auto commit: Day {current_day}, Commit {i}/{num_commits}"
        print(f"Making commit: {msg}")
        make_commit(msg, is_last, next_state)

    print("All commits for the day are complete.")

if __name__ == "__main__":
    main()
