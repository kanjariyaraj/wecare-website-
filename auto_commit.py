import os
import json
import random
import subprocess
import string
from datetime import datetime

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

def run_cmd(cmd):
    """Executes a shell command and returns its output."""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error executing command: {' '.join(cmd)}")
        print(f"STDOUT: {result.stdout}")
        print(f"STDERR: {result.stderr}")
        raise RuntimeError(f"Command failed: {' '.join(cmd)}")
    return result.stdout.strip()

def setup_git():
    """Sets up git configuration if running in GitHub Actions."""
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print("Configuring git for GitHub Actions...")
        run_cmd(["git", "config", "--global", "user.name", "github-actions[bot]"])
        run_cmd(["git", "config", "--global", "user.email", "github-actions[bot]@users.noreply.github.com"])

def load_state():
    """Loads the current day from state.json. Defaults to day 1 if not found."""
    if not os.path.exists(STATE_FILE):
        return {"day": 1}

    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"day": 1}

def save_state(state):
    """Saves the current day to state.json."""
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)

def generate_random_text(length=20):
    """Generates random alphanumeric text to make each commit unique."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def main():
    # Setup git (especially useful for CI/CD)
    setup_git()

    # Determine current day and number of commits to make
    state = load_state()
    current_day = state.get("day", 1)

    # Ensure current_day is within the 1-5 range (safety check)
    if current_day not in COMMITS_PER_DAY:
         current_day = 1

    num_commits = COMMITS_PER_DAY[current_day]

    print(f"Current Day: {current_day}")
    print(f"Target Commits: {num_commits}")

    # Determine next day
    next_day = current_day + 1
    if next_day > 5:
        next_day = 1
    state["day"] = next_day

    # Make the required number of commits
    for i in range(num_commits):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        random_str = generate_random_text()
        log_entry = f"Commit {i+1}/{num_commits} for Day {current_day} - {timestamp} - {random_str}\n"

        # Append to log file
        with open(LOG_FILE, "a") as f:
            f.write(log_entry)

        # Git add log file
        run_cmd(["git", "add", LOG_FILE])

        # On the last commit of the day, update the state file and stage it
        if i == num_commits - 1:
            save_state(state)
            run_cmd(["git", "add", STATE_FILE])
            commit_msg = f"Automated commit: Day {current_day}, Commit {i+1} of {num_commits} (State updated to Day {next_day})"
        else:
            commit_msg = f"Automated commit: Day {current_day}, Commit {i+1} of {num_commits}"

        run_cmd(["git", "commit", "-m", commit_msg])

        print(f"Created commit {i+1}/{num_commits}")

    # Push all changes
    print("Pushing changes to remote...")
    # Using 'git push' directly assumes the remote branch is already set up and permissions are granted
    try:
        run_cmd(["git", "push"])
        print("Successfully pushed commits!")
    except RuntimeError as e:
         print(f"Push failed. This is expected if running locally without proper remote setup. Error: {e}")

if __name__ == "__main__":
    main()
