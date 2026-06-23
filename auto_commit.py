import json
import os
import subprocess
import datetime
import random
import string

STATE_FILE = 'state.json'
LOG_FILE = 'commit_log.txt'

# Commit pattern: Day -> Number of commits
COMMIT_PATTERN = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    return {"current_day": 1}

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=4)

def run_git_command(args):
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {' '.join(args)}: {result.stderr}")
        raise subprocess.CalledProcessError(result.returncode, args, output=result.stdout, stderr=result.stderr)
    return result.stdout

def make_commit(commit_message, include_state_update=False):
    # Append to log file
    timestamp = datetime.datetime.now().isoformat()
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    log_entry = f"{timestamp} - Auto commit entry: {random_str}\n"

    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)

    # Git add and commit
    run_git_command(['git', 'add', LOG_FILE])

    if include_state_update:
        run_git_command(['git', 'add', STATE_FILE])

    run_git_command(['git', 'commit', '-m', commit_message])

def main():
    # Set Git config if not set (useful for GitHub Actions environment)
    if os.getenv("GITHUB_ACTIONS"):
        run_git_command(['git', 'config', '--global', 'user.email', 'actions@github.com'])
        run_git_command(['git', 'config', '--global', 'user.name', 'GitHub Actions Auto Committer'])

    state = load_state()
    current_day = state.get("current_day", 1)

    commits_to_make = COMMIT_PATTERN.get(current_day, 2)

    print(f"Executing Day {current_day} - Making {commits_to_make} commits.")

    # Calculate next day
    next_day = current_day + 1 if current_day < 5 else 1

    for i in range(commits_to_make):
        # On the last commit of the day, update the state file
        is_last_commit = (i == commits_to_make - 1)

        if is_last_commit:
            state["current_day"] = next_day
            save_state(state)

        commit_message = f"Auto commit {i+1}/{commits_to_make} for Day {current_day}"
        make_commit(commit_message, include_state_update=is_last_commit)

    print(f"Finished making commits. Next day will be {state['current_day']}")

    # Push changes if running in GitHub Actions
    if os.getenv("GITHUB_ACTIONS"):
        run_git_command(['git', 'push'])

if __name__ == "__main__":
    main()
