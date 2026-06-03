import os
import json
import random
import string
import subprocess
from datetime import datetime

# File paths
STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

# Commit loop pattern
COMMIT_PATTERN = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def run_command(command):
    """Executes a shell command and returns the output."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error message: {e.stderr}")
        raise

def get_current_day():
    """Reads the current day from the state file. Defaults to 1 if file doesn't exist."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            try:
                data = json.load(f)
                return data.get("current_day", 1)
            except json.JSONDecodeError:
                return 1
    return 1

def update_state(day):
    """Updates the state file with the next day in the loop."""
    next_day = day + 1 if day < 5 else 1
    with open(STATE_FILE, "w") as f:
        json.dump({"current_day": next_day}, f, indent=4)

def generate_random_string(length=10):
    """Generates a random string of fixed length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def setup_git():
    """Sets up git config."""
    # Ensure git user is set for automated commits
    run_command('git config user.name "github-actions[bot]" || git config --global user.name "github-actions[bot]"')
    run_command('git config user.email "github-actions[bot]@users.noreply.github.com" || git config --global user.email "github-actions[bot]@users.noreply.github.com"')

def make_commit(commit_number, total_commits, day):
    """Modifies the log file and creates a git commit."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_str = generate_random_string()

    # Append to log file
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] Day {day} - Commit {commit_number}/{total_commits} - {random_str}\n")

    # Stage and commit
    run_command(f'git add {LOG_FILE} {STATE_FILE}')
    commit_msg = f"Automated commit {commit_number} of {total_commits} for Day {day} - {random_str}"
    run_command(f'git commit -m "{commit_msg}"')
    print(f"Created commit: {commit_msg}")

def main():
    print("Starting automated commit script...")

    # Ensure log file exists
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("Automated Commit Log\n====================\n")

    setup_git()

    current_day = get_current_day()
    commits_to_make = COMMIT_PATTERN.get(current_day, 2)

    print(f"Today is Day {current_day} of the loop. Making {commits_to_make} commits.")

    # Update the state file to the next day, so the first commit includes this change
    update_state(current_day)

    for i in range(1, commits_to_make + 1):
        make_commit(i, commits_to_make, current_day)

    print("Pushing changes to main branch...")
    try:
        run_command("git push origin HEAD:main")
        print("Successfully pushed changes.")
    except subprocess.CalledProcessError:
        print("Failed to push changes. (If running locally without auth, you can safely ignore this or push manually.)")

    print("Done.")

if __name__ == "__main__":
    main()
