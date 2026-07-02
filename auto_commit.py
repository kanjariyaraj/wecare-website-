import os
import json
import random
import string
import subprocess
from datetime import datetime

# Configuration
STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

# Commit sequence
COMMIT_CYCLE = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def run_git_command(command):
    """Run a git command using subprocess."""
    try:
        result = subprocess.run(
            command,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {' '.join(command)}")
        print(f"Error message: {e.stderr}")
        raise

def get_current_day():
    """Read the current day from the state file."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            try:
                state = json.load(f)
                return state.get("day", 1)
            except json.JSONDecodeError:
                return 1
    return 1

def update_day(current_day):
    """Update the day in the state file and reset to 1 if > 5."""
    next_day = current_day + 1
    if next_day > 5:
        next_day = 1

    with open(STATE_FILE, "w") as f:
        json.dump({"day": next_day}, f)

    return next_day

def generate_random_text():
    """Generate a random string to append to the log."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(20))

def configure_git():
    """Configure git user if not running in CI."""
    if not os.environ.get("GITHUB_ACTIONS"):
        try:
            # Check if user.name is set
            run_git_command(["git", "config", "--get", "user.name"])
        except subprocess.CalledProcessError:
            print("Configuring local git user...")
            run_git_command(["git", "config", "user.name", "Auto Commit Bot"])
            run_git_command(["git", "config", "user.email", "bot@example.com"])

def main():
    configure_git()

    current_day = get_current_day()
    num_commits = COMMIT_CYCLE.get(current_day, 2)

    print(f"--- Starting Daily Auto-Commit Sequence ---")
    print(f"Current Day: {current_day}")
    print(f"Commits to make: {num_commits}")

    for i in range(num_commits):
        is_last_commit = (i == num_commits - 1)

        # 1. Update the log file
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        random_text = generate_random_text()
        log_entry = f"Commit {i+1}/{num_commits} on Day {current_day} - {timestamp} - Hash: {random_text}\n"

        with open(LOG_FILE, "a") as f:
            f.write(log_entry)

        print(f"\nMaking commit {i+1}/{num_commits}...")

        # 2. If it's the last commit, also update the state file
        if is_last_commit:
            next_day = update_day(current_day)
            print(f"Updating state.json. Next day will be {next_day}")
            # Stage state file
            run_git_command(["git", "add", STATE_FILE])

        # 3. Stage the log file
        run_git_command(["git", "add", LOG_FILE])

        # 4. Commit changes
        commit_message = f"Auto-commit: Day {current_day}, Commit {i+1} of {num_commits} [{random_text[:6]}]"
        run_git_command(["git", "commit", "-m", commit_message])
        print(f"Created commit: {commit_message}")

    # 5. Push changes
    print("\nPushing changes to remote...")
    try:
        # In GitHub actions, we just push to the current branch
        run_git_command(["git", "push"])
        print("Successfully pushed changes.")
    except subprocess.CalledProcessError:
        print("Warning: Failed to push. This might be expected if running locally without a remote, or if authentication fails.")

if __name__ == "__main__":
    main()
