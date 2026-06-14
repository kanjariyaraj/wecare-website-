import json
import os
import subprocess
import time
from datetime import datetime
import random
import string

# Configuration
STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

# Commit loop mapping: Day -> Number of commits
COMMIT_SCHEDULE = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def run_command(command):
    """Run a shell command and return its output."""
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
        print(f"Error running command: {command}")
        print(f"Output: {e.output}")
        print(f"Error: {e.stderr}")
        raise

def setup_git():
    """Setup git config if not running locally, or rely on existing config."""
    # We will try to set up generic git configs if they aren't set
    # Using local git config to avoid interfering with global system config
    try:
        run_command("git config user.name")
    except subprocess.CalledProcessError:
        print("Setting git user.name...")
        run_command('git config user.name "github-actions[bot]"')

    try:
        run_command("git config user.email")
    except subprocess.CalledProcessError:
        print("Setting git user.email...")
        run_command('git config user.email "github-actions[bot]@users.noreply.github.com"')

def get_current_day():
    """Read the current day from the state file."""
    if not os.path.exists(STATE_FILE):
        return 1

    try:
        with open(STATE_FILE, "r") as f:
            data = json.load(f)
            return data.get("day", 1)
    except Exception as e:
        print(f"Error reading {STATE_FILE}: {e}")
        return 1

def save_next_day(current_day):
    """Update the state file to the next day in the loop."""
    next_day = current_day + 1
    if next_day > len(COMMIT_SCHEDULE):
        next_day = 1

    with open(STATE_FILE, "w") as f:
        json.dump({"day": next_day}, f, indent=4)

    return next_day

def generate_random_string(length=10):
    """Generate a random string to make commits unique."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def make_commit(commit_index, total_commits, is_last_commit, current_day):
    """Make a single commit."""
    # Generate content
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_str = generate_random_string()
    log_entry = f"Commit {commit_index}/{total_commits} on Day {current_day} - {timestamp} - {random_str}\n"

    # Write to log file
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

    # Stage log file
    run_command(f"git add {LOG_FILE}")

    # If it's the last commit, also update and stage the state file
    if is_last_commit:
        next_day = save_next_day(current_day)
        print(f"Advancing to Day {next_day} for the next run.")
        run_command(f"git add {STATE_FILE}")

    # Commit
    commit_message = f"Automated commit {commit_index}/{total_commits} for Day {current_day} ({random_str})"
    run_command(f'git commit -m "{commit_message}"')
    print(f"Created commit: {commit_message}")

def main():
    print("Starting automated commit script...")

    setup_git()

    current_day = get_current_day()
    if current_day not in COMMIT_SCHEDULE:
        print(f"Invalid day {current_day}. Resetting to Day 1.")
        current_day = 1

    num_commits = COMMIT_SCHEDULE[current_day]
    print(f"Today is Day {current_day}. Required commits: {num_commits}")

    for i in range(1, num_commits + 1):
        is_last = (i == num_commits)
        make_commit(i, num_commits, is_last, current_day)

        # Add a small delay between commits to ensure distinct timestamps
        if not is_last:
            time.sleep(1)

    print("Pushing commits to remote repository...")
    try:
        run_command("git push")
        print("Successfully pushed commits.")
    except Exception as e:
        print("Failed to push commits. You might need to set up credentials or run locally.")

if __name__ == "__main__":
    main()
