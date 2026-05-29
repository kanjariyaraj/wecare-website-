import os
import json
import random
import string
import subprocess
import datetime
from typing import Dict

STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

# Define the loop pattern: {day: number_of_commits}
COMMIT_PATTERN = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def load_state() -> Dict:
    """Load the current state from the state.json file."""
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass
    return {"current_day": 1}

def save_state(state: Dict):
    """Save the current state to the state.json file."""
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=4)

def run_git_command(command: list):
    """Run a git command and return its output."""
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running git command: {' '.join(command)}")
        print(f"Output: {e.output}")
        print(f"Stderr: {e.stderr}")
        raise

def generate_random_text(length: int = 10) -> str:
    """Generate a random alphanumeric string."""
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def main():
    # Set default Git configuration if not set (useful for local testing / initial setup)
    # The GitHub action will also configure the git user and email.
    try:
        run_git_command(["git", "config", "user.name"])
    except subprocess.CalledProcessError:
        run_git_command(["git", "config", "user.name", "github-actions[bot]"])
    try:
        run_git_command(["git", "config", "user.email"])
    except subprocess.CalledProcessError:
        run_git_command(["git", "config", "user.email", "github-actions[bot]@users.noreply.github.com"])

    # Load current state
    state = load_state()
    current_day = state.get("current_day", 1)

    # Ensure current_day is within valid bounds (1-5)
    if current_day not in COMMIT_PATTERN:
        current_day = 1

    num_commits = COMMIT_PATTERN[current_day]
    print(f"Starting auto-commit process for Day {current_day}. Expecting {num_commits} commits.")

    # Generate commits
    for i in range(num_commits):
        now = datetime.datetime.now(datetime.timezone.utc).isoformat()
        random_str = generate_random_text()
        log_entry = f"Commit {i+1}/{num_commits} on Day {current_day} - Time: {now} - Rand: {random_str}\n"

        # Modify the log file
        with open(LOG_FILE, 'a') as f:
            f.write(log_entry)

        # Stage the file
        run_git_command(["git", "add", LOG_FILE])

        # If it's the last commit of the day, update the state and include it in this commit
        if i == num_commits - 1:
            next_day = current_day + 1
            if next_day > 5:
                next_day = 1

            state["current_day"] = next_day
            save_state(state)
            print(f"Updated state to Day {next_day} for the next run.")
            run_git_command(["git", "add", STATE_FILE])

        # Commit changes
        commit_message = f"Automated commit: Day {current_day}, Commit {i+1}/{num_commits} [{random_str}]"
        run_git_command(["git", "commit", "-m", commit_message])
        print(f"Made commit: {commit_message}")

if __name__ == "__main__":
    main()
