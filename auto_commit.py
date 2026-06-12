import json
import os
import random
import string
import subprocess
from datetime import datetime

STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

# Rules for the commit loop
# Day 1: 2 commits
# Day 2: 4 commits
# Day 3: 1 commit
# Day 4: 5 commits
# Day 5: 7 commits
COMMIT_PATTERN = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def get_current_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            try:
                state = json.load(f)
                return state.get("day", 1)
            except json.JSONDecodeError:
                return 1
    return 1

def update_state(current_day):
    next_day = current_day + 1
    if next_day > 5:
        next_day = 1
    with open(STATE_FILE, 'w') as f:
        json.dump({"day": next_day}, f, indent=2)

def generate_random_text(length=10):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def run_git_command(command):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {' '.join(command)}")
        print(f"Error output: {e.stderr}")
        raise

def setup_git_config():
    # If run in GitHub Actions, user and email might not be set.
    # Check if they are set, and if not, use default dummy ones.
    try:
        subprocess.run(['git', 'config', '--global', 'user.name'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        run_git_command(['git', 'config', '--global', 'user.name', 'github-actions[bot]'])

    try:
        subprocess.run(['git', 'config', '--global', 'user.email'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        run_git_command(['git', 'config', '--global', 'user.email', 'github-actions[bot]@users.noreply.github.com'])

def main():
    setup_git_config()
    current_day = get_current_state()
    commits_to_make = COMMIT_PATTERN.get(current_day, 1)

    print(f"Current Day: {current_day}")
    print(f"Commits to make today: {commits_to_make}")

    for i in range(commits_to_make):
        # Update log file
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        random_str = generate_random_text()
        log_entry = f"\n[{timestamp}] Automated commit. Random ID: {random_str}"

        with open(LOG_FILE, 'a') as f:
            f.write(log_entry)

        # Stage the log file
        run_git_command(['git', 'add', LOG_FILE])

        # If this is the last commit of the day, update state and stage it too
        if i == commits_to_make - 1:
            update_state(current_day)
            run_git_command(['git', 'add', STATE_FILE])
            commit_message = f"chore: automated update {timestamp} - {random_str} (state updated)"
        else:
            commit_message = f"chore: automated update {timestamp} - {random_str}"

        run_git_command(['git', 'commit', '-m', commit_message])
        print(f"Made commit {i+1}/{commits_to_make}: {commit_message}")

    # Push changes
    print("Pushing changes...")
    try:
        # Assuming pushing to current branch.
        # In GH Actions, it will be the branch that triggered the workflow.
        run_git_command(['git', 'push'])
        print("Push successful.")
    except Exception as e:
        print("Push failed. This is expected if running locally without tracking or permissions set.")
        print(e)

if __name__ == "__main__":
    main()
