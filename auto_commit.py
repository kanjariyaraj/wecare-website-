import os
import json
import random
import string
import subprocess
from datetime import datetime

STATE_FILE = 'state.json'
LOG_FILE = 'commit_log.txt'
BRANCH_NAME = 'main'

# Daily commit pattern
COMMIT_PATTERN = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def run_command(cmd, check=True):
    """Utility to run shell commands."""
    try:
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, check=check, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {' '.join(cmd)}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        raise

def get_current_day():
    """Reads the current day from state.json."""
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, 'r') as f:
                state = json.load(f)
                return state.get('day', 1)
        except (json.JSONDecodeError, ValueError):
            return 1
    return 1

def save_next_day(current_day):
    """Updates state.json with the next day."""
    next_day = current_day + 1
    if next_day > 5:
        next_day = 1

    with open(STATE_FILE, 'w') as f:
        json.dump({'day': next_day}, f, indent=4)
    print(f"Updated state to Day {next_day}")

def generate_random_string(length=10):
    """Generates a random string of fixed length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def setup_git():
    """Configures git for the commit."""
    run_command(['git', 'config', '--local', 'user.name', 'github-actions[bot]'], check=False)
    run_command(['git', 'config', '--local', 'user.email', 'github-actions[bot]@users.noreply.github.com'], check=False)

def create_commit(day, commit_num, total_commits):
    """Creates a single commit by modifying the log file."""
    timestamp = datetime.now().isoformat()
    random_str = generate_random_string()

    log_entry = f"Day {day} - Commit {commit_num}/{total_commits} - {timestamp} - {random_str}\n"

    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)

    run_command(['git', 'add', LOG_FILE])

    # After the last commit for the day, also stage the state file
    if commit_num == total_commits:
        run_command(['git', 'add', STATE_FILE])

    commit_message = f"Auto commit: Day {day} ({commit_num}/{total_commits})"
    run_command(['git', 'commit', '-m', commit_message])

def main():
    setup_git()

    current_day = get_current_day()
    if current_day not in COMMIT_PATTERN:
        current_day = 1

    num_commits = COMMIT_PATTERN[current_day]

    print(f"Starting automation for Day {current_day}: making {num_commits} commits.")

    # Save the next day state before committing, so the last commit includes the updated state
    save_next_day(current_day)

    for i in range(1, num_commits + 1):
        create_commit(current_day, i, num_commits)

    print(f"Successfully made {num_commits} commits.")

    # Try to push, handle potential failures (e.g., if local test without remote)
    try:
        run_command(['git', 'push', 'origin', BRANCH_NAME])
        print("Successfully pushed changes.")
    except Exception as e:
        print("Could not push changes. This is expected if running locally without a remote configured.")
        print(e)

if __name__ == '__main__':
    main()
