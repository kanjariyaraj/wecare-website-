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
COMMIT_PATTERN = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def setup_git():
    """Configures git user inside GitHub Actions."""
    if os.environ.get("GITHUB_ACTIONS") == "true":
        subprocess.run(["git", "config", "--global", "user.name", "github-actions[bot]"], check=True)
        subprocess.run(["git", "config", "--global", "user.email", "github-actions[bot]@users.noreply.github.com"], check=True)

def read_state():
    """Reads the current day from the state file."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            try:
                data = json.load(f)
                return data.get("current_day", 1)
            except json.JSONDecodeError:
                return 1
    return 1

def update_state(current_day):
    """Updates the state file to the next day in the cycle."""
    next_day = current_day + 1 if current_day < 5 else 1
    with open(STATE_FILE, "w") as f:
        json.dump({"current_day": next_day}, f, indent=4)
    return next_day

def generate_random_text(length=20):
    """Generates random string of characters."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def modify_log_file():
    """Appends a new line to the log file with a timestamp and random text."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_text = generate_random_text()
    entry = f"[{timestamp}] Automated commit entry: {random_text}\n"

    with open(LOG_FILE, "a") as f:
        f.write(entry)

def make_commits(current_day):
    """Performs the required number of commits for the current day."""
    num_commits = COMMIT_PATTERN.get(current_day, 1)
    print(f"Day {current_day} of cycle. Making {num_commits} commits.")

    for i in range(num_commits):
        print(f"Executing commit {i+1}/{num_commits}")

        # Modify the log file for genuine code change
        modify_log_file()

        # On the last commit of the day, update the state file as well
        if i == num_commits - 1:
            update_state(current_day)

        # Stage files
        subprocess.run(["git", "add", LOG_FILE, STATE_FILE], check=True)

        # Commit with distinct message
        commit_msg = f"Automated update: Day {current_day}, Commit {i+1} of {num_commits} [{generate_random_text(8)}]"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)

        # Slight delay to ensure distinct timestamps
        time.sleep(1)

    # Push all commits to remote
    # Only push if running in GitHub Actions, or allow it to fail gracefully in local testing.
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print("Pushing commits to remote...")
        subprocess.run(["git", "push", "origin", "HEAD"], check=True)
        print("Push successful.")
    else:
        print("Skipping push to remote since GITHUB_ACTIONS is not true.")

if __name__ == "__main__":
    try:
        setup_git()
        current_day = read_state()
        make_commits(current_day)
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
