import json
import os
import subprocess
import time
import random
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

def run_command(command):
    """Runs a shell command and returns the output."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error running command: {command}\n{stderr.decode('utf-8')}")
        raise Exception(f"Command failed: {command}")
    return stdout.decode('utf-8')

def get_current_day():
    """Reads the current day from the state file."""
    if not os.path.exists(STATE_FILE):
        return 1

    with open(STATE_FILE, 'r') as f:
        try:
            state = json.load(f)
            return state.get("day", 1)
        except json.JSONDecodeError:
            return 1

def update_state(current_day):
    """Updates the state file with the next day."""
    next_day = current_day + 1 if current_day < 5 else 1
    with open(STATE_FILE, 'w') as f:
        json.dump({"day": next_day}, f, indent=4)
    return next_day

def make_commit(commit_number, total_commits, current_day):
    """Modifies a file, stages it, and makes a commit."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_str = ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=8))

    log_entry = f"Commit {commit_number}/{total_commits} on Day {current_day} - {timestamp} - {random_str}\n"

    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)

    run_command(f"git add {LOG_FILE} {STATE_FILE}")
    commit_msg = f"Auto-commit {commit_number}/{total_commits} for Day {current_day} - {timestamp}"
    run_command(f'git commit -m "{commit_msg}"')

def configure_git():
    """Configures Git username and email if they are not already set."""
    try:
        run_command("git config user.name")
    except Exception:
        run_command('git config user.name "Auto Commit Bot"')

    try:
        run_command("git config user.email")
    except Exception:
        run_command('git config user.email "auto-commit-bot@users.noreply.github.com"')

def main():
    print("Starting auto-commit script...")

    configure_git()

    current_day = get_current_day()
    num_commits = COMMIT_PATTERN.get(current_day, 2)

    print(f"Today is Day {current_day}. Planning to make {num_commits} commits.")

    # Update state for the next run, but we will commit it in this run
    update_state(current_day)

    for i in range(1, num_commits + 1):
        make_commit(i, num_commits, current_day)
        time.sleep(1) # Sleep slightly to ensure distinct timestamps

    # Push changes
    print("Pushing commits to remote...")
    try:
        run_command("git push")
    except Exception as e:
        print(f"Failed to push (this is expected if running locally without an upstream branch): {e}")

    print("Auto-commit process completed successfully.")

if __name__ == "__main__":
    main()
