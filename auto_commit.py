import json
import os
import subprocess
import time
from datetime import datetime

STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

# Commit loop pattern for each day
COMMIT_PATTERN = [2, 4, 1, 5, 7]

def run_command(cmd, check=False):
    """Utility to run a shell command."""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Command failed: {cmd}\nError: {result.stderr}")
        if check:
            raise Exception(f"Command failed: {cmd}")
    return result

def get_current_day_index():
    """Reads the current day index from the state file."""
    if not os.path.exists(STATE_FILE):
        return 0
    with open(STATE_FILE, "r") as f:
        try:
            data = json.load(f)
            return data.get("day_index", 0)
        except json.JSONDecodeError:
            return 0

def set_current_day_index(index):
    """Saves the given day index to the state file."""
    with open(STATE_FILE, "w") as f:
        json.dump({"day_index": index}, f)

def main():
    # 1. Configure Git
    # Only set local config if user.name/email are missing, or we are in GHA
    if os.environ.get("GITHUB_ACTIONS") == "true":
        run_command('git config --local user.name "github-actions[bot]"')
        run_command('git config --local user.email "github-actions[bot]@users.noreply.github.com"')
    else:
        name_check = run_command('git config user.name')
        if name_check.returncode != 0 or not name_check.stdout.strip():
            run_command('git config --local user.name "Auto Committer"')
        email_check = run_command('git config user.email')
        if email_check.returncode != 0 or not email_check.stdout.strip():
            run_command('git config --local user.email "auto@committer.local"')

    # 2. Read State
    day_index = get_current_day_index()
    num_commits = COMMIT_PATTERN[day_index]

    print(f"--- Day {day_index + 1} of cycle. Making {num_commits} commits ---")

    # Ensure log file exists
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("Auto Commit Log\n================\n")

    # 3. Perform Commits
    for i in range(num_commits):
        # Modify the log file to ensure a real change is detected by Git
        now = datetime.now().isoformat()
        with open(LOG_FILE, "a") as f:
            f.write(f"Commit {i+1}/{num_commits} on cycle day {day_index + 1}. Timestamp: {now}\n")

        # Stage the log file
        run_command(f"git add {LOG_FILE}", check=True)

        # In the very last commit of the day, update the state file for the next day
        if i == num_commits - 1:
            next_day_index = (day_index + 1) % len(COMMIT_PATTERN)
            set_current_day_index(next_day_index)
            run_command(f"git add {STATE_FILE}", check=True)
            print(f"Updating state file for next day index: {next_day_index}")

        # Create a distinct commit message
        commit_msg = f"Auto commit {i+1} of {num_commits} (Day {day_index + 1})"
        run_command(f'git commit -m "{commit_msg}"', check=True)

        # Sleep briefly to avoid identical timestamps in fast execution
        time.sleep(1)

    # 4. Push Changes
    print("Pushing commits to main branch...")
    # Pushing specifically to main branch as required
    run_command("git push origin HEAD:main", check=True)
    print("Automation complete.")

if __name__ == "__main__":
    main()
