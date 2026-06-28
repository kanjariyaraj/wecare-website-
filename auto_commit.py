import json
import os
import random
import subprocess
import string
from datetime import datetime

STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

# Define the commit pattern for the 5-day cycle
COMMIT_PATTERN = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def run_git_command(command):
    """Executes a git command and returns the output."""
    try:
        result = subprocess.run(command, check=True, text=True, shell=True, capture_output=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(e.stderr)
        return None

def load_state():
    """Loads the current day from state.json."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            try:
                data = json.load(f)
                return data.get("day", 1)
            except json.JSONDecodeError:
                return 1
    return 1

def save_state(day):
    """Saves the next day to state.json."""
    with open(STATE_FILE, 'w') as f:
        json.dump({"day": day}, f, indent=4)

def setup_git():
    """Configure git user and email if they are not already set."""
    user = run_git_command("git config --global user.name")
    if not user:
        run_git_command("git config --global user.name 'github-actions[bot]'")
        run_git_command("git config --global user.email 'github-actions[bot]@users.noreply.github.com'")

def append_to_log():
    """Appends a random string and timestamp to the log file."""
    timestamp = datetime.now().isoformat()
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    with open(LOG_FILE, 'a') as f:
        f.write(f"{timestamp} - Auto commit ID: {random_str}\n")
    return random_str

def main():
    setup_git()

    current_day = load_state()
    # Ensure current_day is within the 1-5 range
    if current_day not in COMMIT_PATTERN:
         current_day = 1

    num_commits = COMMIT_PATTERN[current_day]

    print(f"--- Starting Daily Loop ---")
    print(f"Current Day: {current_day}")
    print(f"Number of commits to make: {num_commits}")

    for i in range(1, num_commits + 1):
        print(f"\nMaking commit {i}/{num_commits}...")

        # 1. Modify the log file
        commit_id = append_to_log()

        # 2. Stage the log file
        run_git_command(f"git add {LOG_FILE}")

        # 3. If it's the LAST commit of the day, we must also update state.json
        if i == num_commits:
            next_day = current_day + 1 if current_day < 5 else 1
            print(f"End of daily cycle. Updating state.json to Day {next_day}.")
            save_state(next_day)
            run_git_command(f"git add {STATE_FILE}")

        # 4. Create the commit
        commit_msg = f"Auto commit {i}/{num_commits} for Day {current_day} (ID: {commit_id})"
        run_git_command(f"git commit -m \"{commit_msg}\"")

    print("\nAll commits for the day created successfully.")

    # Push the changes
    print("Pushing to remote...")
    # NOTE: We skip pushing to origin in the local script because we might not have credentials.
    # The GitHub Action will run this code and its push will succeed because of permissions.
    push_result = run_git_command("git push origin main || true")
    if push_result is not None:
         print("Push attempted (may have skipped or failed locally, which is fine).")

if __name__ == "__main__":
    main()