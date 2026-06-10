import os
import json
import random
import string
import datetime
import subprocess

# Configuration
STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"
COMMITS_PER_DAY = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            try:
                state = json.load(f)
                return state.get("current_day", 1)
            except json.JSONDecodeError:
                return 1
    return 1

def save_state(day):
    with open(STATE_FILE, "w") as f:
        json.dump({"current_day": day}, f, indent=4)

def setup_git():
    # If running in GitHub Actions, we need to configure git user and email
    if os.environ.get("GITHUB_ACTIONS") == "true":
        subprocess.run(["git", "config", "--global", "user.name", "github-actions[bot]"], check=True)
        subprocess.run(["git", "config", "--global", "user.email", "github-actions[bot]@users.noreply.github.com"], check=True)

def generate_random_string(length=12):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def make_commit(commit_index, total_commits, day, is_last):
    # Modify the log file
    timestamp = datetime.datetime.now().isoformat()
    random_str = generate_random_string()

    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - Day {day} Commit {commit_index}/{total_commits} - {random_str}\n")

    # If it's the last commit, we also save the state for the NEXT day
    if is_last:
        next_day = day + 1
        if next_day > 5:
            next_day = 1
        save_state(next_day)

    # Stage files
    subprocess.run(["git", "add", LOG_FILE], check=True)
    if os.path.exists(STATE_FILE):
        subprocess.run(["git", "add", STATE_FILE], check=True)

    # Commit
    commit_msg = f"Auto commit: Day {day} - {commit_index}/{total_commits} [{random_str}]"
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)

def main():
    setup_git()

    # Ensure state file exists to start with
    if not os.path.exists(STATE_FILE):
        save_state(1)

    current_day = load_state()

    # Ensure current_day is within 1-5
    if current_day not in COMMITS_PER_DAY:
        current_day = 1

    num_commits = COMMITS_PER_DAY[current_day]
    print(f"Starting auto commit for Day {current_day}. Total commits to make: {num_commits}")

    for i in range(1, num_commits + 1):
        is_last = (i == num_commits)
        make_commit(i, num_commits, current_day, is_last)
        print(f"Made commit {i}/{num_commits}")

    # Push changes if running in GitHub Actions or if push is desired
    # We will try to push, and if it fails (e.g. no remote), we just print
    try:
        print("Pushing to remote...")
        subprocess.run(["git", "push"], check=True)
        print("Push successful.")
    except subprocess.CalledProcessError:
        print("Git push failed. You may need to push manually or set up the remote.")

if __name__ == "__main__":
    main()
