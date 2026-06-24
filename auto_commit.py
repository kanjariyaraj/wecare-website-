import json
import os
import subprocess
import datetime
import sys

STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

# Loop definition: Day -> Number of commits
COMMIT_PATTERN = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def run_command(command, check=True):
    try:
        result = subprocess.run(command, check=check, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {' '.join(command)}")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        if check:
            sys.exit(1)
        return None

def get_state():
    if not os.path.exists(STATE_FILE):
        return {"day": 1}
    with open(STATE_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {"day": 1}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)

def setup_git():
    # Set up git config if it's not already set
    run_command(["git", "config", "user.email", "github-actions[bot]@users.noreply.github.com"], check=False)
    run_command(["git", "config", "user.name", "github-actions[bot]"], check=False)

def main():
    state = get_state()
    current_day = state.get("day", 1)

    if current_day not in COMMIT_PATTERN:
        current_day = 1

    num_commits = COMMIT_PATTERN[current_day]
    print(f"Starting Day {current_day} automation: {num_commits} commits required.")

    setup_git()

    # Calculate next day
    next_day = current_day + 1
    if next_day > 5:
        next_day = 1

    state["day"] = next_day

    for i in range(num_commits):
        timestamp = datetime.datetime.now().isoformat()
        log_entry = f"Commit {i+1}/{num_commits} for Day {current_day} at {timestamp}\n"

        with open(LOG_FILE, "a") as f:
            f.write(log_entry)

        run_command(["git", "add", LOG_FILE])

        commit_message = f"Automated commit {i+1} of {num_commits} for Day {current_day}"

        # If it's the last commit of the day, update the state file and add it to the commit
        if i == num_commits - 1:
            save_state(state)
            run_command(["git", "add", STATE_FILE])
            commit_message += f" (Updated state to Day {next_day})"
            print(f"Updated state to Day {next_day} and staged.")

        run_command(["git", "commit", "-m", commit_message])
        print(f"Created commit: {commit_message}")

    # Push changes
    print("Pushing changes...")
    # In GitHub actions, origin is configured automatically
    # Push to current branch (which should be main)
    push_result = subprocess.run(["git", "push", "origin", "HEAD:main"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if push_result.returncode != 0:
        print(f"Note: Push failed. This is expected when running locally without remote access.")
        print(f"stderr: {push_result.stderr}")
        # In a real GitHub action environment, we want it to fail if it can't push
        if "GITHUB_ACTIONS" in os.environ:
            sys.exit(1)
    else:
        print("Push successful!")

    print("Done!")

if __name__ == "__main__":
    main()