import os
import json
import time
import random
import string
import subprocess
import datetime

STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

# Define the commit sequence pattern
# Day index is 1-based in our state.json, but 0-based in list if we prefer.
COMMIT_PATTERN = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def run_command(command, check=True):
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if check and result.returncode != 0:
        print(f"Error running command: {command}")
        print(f"Stdout: {result.stdout}")
        print(f"Stderr: {result.stderr}")
        raise Exception(f"Command failed with exit code {result.returncode}")
    return result.stdout.strip()

def get_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r") as f:
                state = json.load(f)
                return state.get("current_day", 1)
        except Exception as e:
            print(f"Error reading state file: {e}")
            return 1
    return 1

def save_state(day):
    with open(STATE_FILE, "w") as f:
        json.dump({"current_day": day}, f, indent=4)

def setup_git():
    # If running in GitHub Actions, these might be set. But we should ensure fallback.
    try:
        run_command("git config user.name")
    except Exception:
        run_command("git config user.name 'github-actions[bot]'")

    try:
        run_command("git config user.email")
    except Exception:
        run_command("git config user.email 'github-actions[bot]@users.noreply.github.com'")

def append_to_log():
    timestamp = datetime.datetime.now().isoformat()
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    with open(LOG_FILE, "a") as f:
        f.write(f"Commit on {timestamp} - Random data: {random_str}\n")

def make_commit(message, include_state=False):
    run_command(f"git add {LOG_FILE}")
    if include_state:
        run_command(f"git add {STATE_FILE}")
    run_command(f'git commit -m "{message}"')

def main():
    setup_git()
    current_day = get_state()
    commits_to_make = COMMIT_PATTERN.get(current_day, 2)

    print(f"Starting auto-commit for Day {current_day}. Will make {commits_to_make} commits.")

    for i in range(1, commits_to_make + 1):
        append_to_log()

        is_final_commit = (i == commits_to_make)
        if is_final_commit:
            next_day = current_day + 1
            if next_day > 5:
                next_day = 1
            save_state(next_day)
            print(f"Final commit of the day. Advancing state to Day {next_day}.")

            commit_message = f"Auto-commit: Day {current_day}, Commit {i}/{commits_to_make} (State updated to Day {next_day})"
            make_commit(commit_message, include_state=True)
        else:
            commit_message = f"Auto-commit: Day {current_day}, Commit {i}/{commits_to_make}"
            make_commit(commit_message, include_state=False)
            # Sleep slightly to ensure distinct timestamps if needed, though isoformat has high precision
            time.sleep(1)

    print("Pushing commits...")
    try:
        # Determine the current branch
        branch = run_command("git rev-parse --abbrev-ref HEAD", check=False)
        if not branch or branch == "HEAD":
            branch = "main"
        run_command(f"git push origin HEAD:{branch}")
        print("Push successful.")
    except Exception as e:
        print(f"Error pushing: {e}")

if __name__ == "__main__":
    main()
