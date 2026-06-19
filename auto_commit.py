import os
import json
import random
import subprocess
import string
from datetime import datetime

# Configuration
STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"
LOOP_PATTERN = [2, 4, 1, 5, 7]

def run_command(command):
    """Run a shell command and return its output."""
    try:
        result = subprocess.run(command, check=True, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(f"Error output: {e.stderr}")
        raise

def get_current_day():
    """Read the current day from the state file."""
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, 'r') as f:
                data = json.load(f)
                return data.get("current_day", 1)
        except (json.JSONDecodeError, IOError):
            pass
    return 1

def update_state(next_day):
    """Update the state file with the next day."""
    with open(STATE_FILE, 'w') as f:
        json.dump({"current_day": next_day}, f, indent=4)

def generate_random_text(length=20):
    """Generate random text to append to the log file."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def modify_file(commit_number, total_commits, day):
    """Modify the log file to ensure a change is detected."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_text = generate_random_text()
    log_entry = f"Day: {day} | Commit: {commit_number}/{total_commits} | Time: {timestamp} | Ref: {random_text}\n"

    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)

def main():
    # Setup git config if running in CI
    if os.environ.get("GITHUB_ACTIONS"):
        run_command("git config --global user.name 'github-actions[bot]'")
        run_command("git config --global user.email 'github-actions[bot]@users.noreply.github.com'")

    current_day = get_current_day()

    # Ensure current_day is within valid bounds (1 to 5)
    if current_day < 1 or current_day > len(LOOP_PATTERN):
        current_day = 1

    num_commits = LOOP_PATTERN[current_day - 1]

    print(f"Starting auto-commit process for Day {current_day}. Target commits: {num_commits}")

    # Calculate next day
    next_day = current_day + 1
    if next_day > len(LOOP_PATTERN):
        next_day = 1

    for i in range(1, num_commits + 1):
        # 1. Modify file
        modify_file(i, num_commits, current_day)

        # 2. Stage file
        run_command(f"git add {LOG_FILE}")

        # If this is the last commit for the day, update and stage the state file
        if i == num_commits:
            update_state(next_day)
            run_command(f"git add {STATE_FILE}")

        # 3. Create commit
        commit_message = f"Automated commit: Day {current_day} - {i}/{num_commits}"
        run_command(f'git commit -m "{commit_message}"')
        print(f"Created commit: {commit_message}")

    # Push changes
    print("Pushing commits to remote repository...")
    # NOTE: To test locally without pushing, comment out the line below.
    run_command("git push")
    print("Process completed successfully.")

if __name__ == "__main__":
    main()