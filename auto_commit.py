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
COMMIT_PATTERN = [2, 4, 1, 5, 7]  # Commits per day in the cycle

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
        print(f"Command failed: {command}")
        print(f"Error output: {e.stderr}")
        raise

def setup_git():
    """Sets up git config if running in GitHub Actions."""
    if os.environ.get("GITHUB_ACTIONS"):
        print("Setting up git configuration for GitHub Actions...")
        run_command('git config --global user.name "github-actions[bot]"')
        run_command('git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"')

def load_state():
    """Loads the current state from the state file."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {"day_index": 0}

def save_state(state):
    """Saves the current state to the state file."""
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def generate_random_string(length=10):
    """Generates a random string of letters and digits."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def make_commit(commit_message, include_state=False):
    """Makes a single commit, optionally including the state.json file."""
    # Append random text and timestamp to log file
    timestamp = datetime.now().isoformat()
    random_str = generate_random_string()

    with open(LOG_FILE, "a") as f:
        f.write(f"Commit at {timestamp} - {random_str}\n")

    # Stage the log file
    run_command(f'git add {LOG_FILE}')

    # Stage the state file if this is the final commit
    if include_state:
        run_command(f'git add {STATE_FILE}')
        print(f"Staged {STATE_FILE} with the final commit.")

    # Create the commit
    run_command(f'git commit -m "{commit_message}"')
    print(f"Created commit: {commit_message}")

def main():
    setup_git()

    # Read the current state
    state = load_state()
    day_index = state.get("day_index", 0)

    # Determine the number of commits for today
    commits_to_make = COMMIT_PATTERN[day_index]
    print(f"Day {day_index + 1} of cycle. Making {commits_to_make} commits today.")

    # Calculate the next day index (loops back to 0 after 4)
    next_day_index = (day_index + 1) % len(COMMIT_PATTERN)
    state["day_index"] = next_day_index

    for i in range(commits_to_make):
        # Is this the final commit of the day?
        is_final_commit = (i == commits_to_make - 1)

        if is_final_commit:
            # Update the state file before making the final commit
            save_state(state)

        # Create commit message
        commit_message = f"Auto-commit {i + 1}/{commits_to_make} for Day {day_index + 1}"

        # Make the commit, including the state file only on the last commit
        make_commit(commit_message, include_state=is_final_commit)

        # Small delay between commits
        time.sleep(1)

    # Push changes to the repository
    print("Pushing commits to remote repository...")
    run_command('git push origin HEAD:main')
    print("Done!")

if __name__ == "__main__":
    main()
