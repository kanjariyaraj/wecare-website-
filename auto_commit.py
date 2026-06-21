import json
import os
import random
import string
import subprocess
from datetime import datetime

# Configuration
STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

# Commit sequence mapping
COMMITS_PER_DAY = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def run_command(command):
    """Utility to run a shell command."""
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {command}")
        print(f"Error: {e.stderr}")
        raise

def get_current_state():
    """Load the state file or initialize it if missing."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            try:
                state = json.load(f)
                return state.get("day", 1)
            except json.JSONDecodeError:
                pass
    return 1

def save_state(day):
    """Save the next day to the state file."""
    with open(STATE_FILE, 'w') as f:
        json.dump({"day": day}, f, indent=4)

def generate_random_string(length=12):
    """Generate a random string for the log file."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def modify_log_file():
    """Append a new log entry to the log file."""
    timestamp = datetime.now().isoformat()
    random_str = generate_random_string()
    log_entry = f"[{timestamp}] Automated update. ID: {random_str}\n"

    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)

def main():
    # Set up git config if running in GitHub Actions
    if os.environ.get("GITHUB_ACTIONS"):
        print("Configuring Git for GitHub Actions...")
        run_command('git config --global user.name "github-actions[bot]"')
        run_command('git config --global user.email "github-actions[bot]@users.noreply.github.com"')

    day = get_current_state()
    commits_to_make = COMMITS_PER_DAY.get(day, 2)

    print(f"Current Day: {day} | Commits to make: {commits_to_make}")

    for i in range(commits_to_make):
        print(f"Making commit {i + 1}/{commits_to_make}...")
        modify_log_file()

        # Stage the log file
        run_command(f'git add {LOG_FILE}')

        # On the last commit of the day, also save and stage the state file
        if i == commits_to_make - 1:
            next_day = day + 1 if day < 5 else 1
            save_state(next_day)
            run_command(f'git add {STATE_FILE}')

        commit_message = f"Auto-commit: Day {day}, Commit {i + 1} of {commits_to_make}"
        run_command(f'git commit -m "{commit_message}"')

    # Push changes
    print("Pushing commits to remote...")
    try:
        run_command("git push origin HEAD")
        print("Push complete.")
    except Exception as e:
        print("Push failed. If running locally without remote or push rights, this is expected.")

if __name__ == "__main__":
    main()
