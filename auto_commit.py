import os
import json
import subprocess
import time
import random

STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

# Number of commits for each day in the 5-day cycle
# 1-based index (Day 1 to 5)
COMMIT_SCHEDULE = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def run_command(cmd, check=True):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"Error executing: {cmd}")
        print(result.stderr)
        result.check_returncode()
    return result.stdout.strip()

def get_current_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r") as f:
                state = json.load(f)
                return state.get("day_index", 1)
        except json.JSONDecodeError:
            print("Error reading state file, starting at day 1")
    return 1

def update_state(current_day):
    next_day = current_day + 1
    if next_day > 5:
        next_day = 1

    with open(STATE_FILE, "w") as f:
        json.dump({"day_index": next_day}, f)
    print(f"Updated state: next day is {next_day}")

def main():
    # Setup git configuration (useful for CI/CD environments)
    # Checking if we are running in GitHub actions (usually CI=true)
    if os.environ.get("GITHUB_ACTIONS"):
        run_command('git config --global user.name "github-actions[bot]"')
        run_command('git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"')
    else:
        # Fallback for local testing or custom environments
        run_command('git config user.name "Auto Committer"', check=False)
        run_command('git config user.email "auto-committer@example.com"', check=False)

    current_day = get_current_state()
    num_commits = COMMIT_SCHEDULE.get(current_day, 2)

    print(f"Current Day: {current_day}, Scheduled Commits: {num_commits}")

    for i in range(num_commits):
        # Modify the log file to ensure a distinct commit
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        random_hash = f"{random.getrandbits(32):08x}"

        log_entry = f"Commit {i+1}/{num_commits} for Day {current_day} - {timestamp} - {random_hash}\n"

        with open(LOG_FILE, "a") as f:
            f.write(log_entry)

        print(f"Added entry: {log_entry.strip()}")

        # Stage the log file
        run_command(f'git add {LOG_FILE}')

        # If it is the last commit of the day, also update and stage the state file
        if i == num_commits - 1:
            update_state(current_day)
            run_command(f'git add {STATE_FILE}')

        # Commit the changes
        commit_message = f"chore: automated commit {i+1} for day {current_day}"
        if i == num_commits - 1:
            commit_message += " and update state"

        run_command(f'git commit -m "{commit_message}"')

    # Push the changes
    # Use the current branch which should be main
    # Ensure it handles push correctly
    try:
        run_command('git push')
        print("Successfully pushed changes to remote repository.")
    except subprocess.CalledProcessError as e:
        print("Failed to push changes. Ensure you have the correct permissions.")
        # If in a GitHub Action, GITHUB_TOKEN is usually provided.

if __name__ == "__main__":
    main()
