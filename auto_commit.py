import json
import os
import subprocess
import time
import random
import string
from datetime import datetime

STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

# Commit loop rules
COMMIT_RULES = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr)
        # Note: Depending on environment, we might want to raise an exception or just continue
        # but for commits, if it fails, it might be because nothing changed, which shouldn't happen here.
    return result.stdout.strip()

def get_current_day():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            try:
                state = json.load(f)
                return state.get("current_day", 1)
            except json.JSONDecodeError:
                return 1
    return 1

def save_next_day(current_day):
    next_day = current_day + 1
    if next_day > 5:
        next_day = 1

    with open(STATE_FILE, "w") as f:
        json.dump({"current_day": next_day}, f, indent=4)
    return next_day

def generate_random_string(length=10):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def setup_git():
    # Set git config if not already set (useful for local runs or CI without pre-configured git)
    run_command('git config --local user.email "action@github.com"')
    run_command('git config --local user.name "GitHub Action"')

def main():
    setup_git()
    current_day = get_current_day()

    if current_day not in COMMIT_RULES:
        current_day = 1

    num_commits = COMMIT_RULES[current_day]
    print(f"Starting auto-commits for Day {current_day}: {num_commits} commits.")

    for i in range(1, num_commits + 1):
        # Generate some content to append
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        random_str = generate_random_string(12)
        log_entry = f"{timestamp} - Day {current_day} - Commit {i}/{num_commits} - {random_str}\n"

        # Write to log file
        with open(LOG_FILE, "a") as f:
            f.write(log_entry)

        # Update state file on the last commit so it gets committed too
        if i == num_commits:
            save_next_day(current_day)
            files_to_add = f"{LOG_FILE} {STATE_FILE}"
        else:
            files_to_add = LOG_FILE

        # Git operations
        run_command(f'git add {files_to_add}')
        commit_msg = f"Auto commit {i} of {num_commits} for Day {current_day}"
        run_command(f'git commit -m "{commit_msg}"')

        # Sleep briefly to ensure distinct timestamps if needed (not strictly necessary but good practice)
        time.sleep(1)

    print("Pushing to remote...")
    # Push changes. If running in GitHub Actions, the default token allows pushing back.
    run_command("git push")
    print("Done!")

if __name__ == "__main__":
    main()
