import json
import os
import random
import string
import subprocess
import datetime

STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

# Commit counts per day in the 5-day cycle
COMMIT_PATTERN = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def run_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command {' '.join(command)}:")
        print(e.stderr)
        raise

def get_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            state = json.load(f)
            return state.get("day", 1)
    return 1

def save_state(day):
    with open(STATE_FILE, "w") as f:
        json.dump({"day": day}, f, indent=4)

def configure_git():
    # Set default git config if not present, useful for GH Actions
    try:
        run_command(["git", "config", "user.name", "github-actions[bot]"])
        run_command(["git", "config", "user.email", "github-actions[bot]@users.noreply.github.com"])
    except Exception:
        pass

def main():
    configure_git()

    current_day = get_state()
    if current_day not in COMMIT_PATTERN:
        current_day = 1

    num_commits = COMMIT_PATTERN[current_day]
    print(f"Starting auto-commit for Day {current_day}. Target commits: {num_commits}")

    for i in range(1, num_commits + 1):
        # Generate random text and timestamp
        timestamp = datetime.datetime.now().isoformat()
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        log_entry = f"[{timestamp}] Auto-commit {i}/{num_commits} for Day {current_day}. Random: {random_string}\n"

        # Append to log file
        with open(LOG_FILE, "a") as f:
            f.write(log_entry)

        run_command(["git", "add", LOG_FILE])

        # If this is the last commit for today, update the state file
        if i == num_commits:
            next_day = current_day + 1
            if next_day > 5:
                next_day = 1
            save_state(next_day)
            run_command(["git", "add", STATE_FILE])
            print(f"Updated state to Day {next_day}")

        commit_message = f"Auto-commit: Day {current_day}, Commit {i}/{num_commits}"
        run_command(["git", "commit", "-m", commit_message])
        print(f"Committed: {commit_message}")

    # Push all commits to the remote repository
    print("Pushing commits to remote...")
    try:
        run_command(["git", "push"])
        print("Push successful.")
    except Exception as e:
        print(f"Push failed (expected if local without remote): {e}")

if __name__ == "__main__":
    main()
