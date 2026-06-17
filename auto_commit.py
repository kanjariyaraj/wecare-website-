import os
import json
import random
import string
import subprocess
import datetime
import sys

# Configuration
STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"
PATTERN = [2, 4, 1, 5, 7]

def run_command(command):
    """Run a shell command and return the output."""
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
        print(f"Command failed: {command}")
        print(f"Error: {e.stderr}")
        sys.exit(1)

def get_state():
    """Read the current day from the state file."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            try:
                state = json.load(f)
                return state.get("current_day", 0)
            except json.JSONDecodeError:
                return 0
    return 0

def update_state(next_day):
    """Update the state file with the next day."""
    with open(STATE_FILE, "w") as f:
        json.dump({"current_day": next_day}, f, indent=4)

def setup_git():
    """Configure Git username and email if running in GitHub Actions."""
    if os.getenv("GITHUB_ACTIONS") == "true":
        run_command("git config --global user.name 'github-actions[bot]'")
        run_command("git config --global user.email 'github-actions[bot]@users.noreply.github.com'")

def generate_random_string(length=10):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def main():
    # Set up Git (useful for CI/CD environments like GitHub Actions)
    setup_git()

    # Get current state
    current_day = get_state()
    commits_to_make = PATTERN[current_day]

    print(f"--- Day {current_day + 1} of the cycle ---")
    print(f"Target commits for today: {commits_to_make}")

    for i in range(commits_to_make):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        random_text = generate_random_string(16)
        log_entry = f"Commit {i + 1}/{commits_to_make} on Day {current_day + 1} - {timestamp} - {random_text}\n"

        # Append to log file
        with open(LOG_FILE, "a") as f:
            f.write(log_entry)

        # Stage files
        run_command(f"git add {LOG_FILE}")

        # We also need to stage the state file on the last commit of the day
        if i == commits_to_make - 1:
            next_day = (current_day + 1) % len(PATTERN)
            update_state(next_day)
            run_command(f"git add {STATE_FILE}")

        # Commit
        commit_msg = f"Automated commit {i + 1} of {commits_to_make} for Day {current_day + 1}"
        run_command(f'git commit -m "{commit_msg}"')

        print(f"Created commit: {commit_msg}")

    # Push all commits to the current branch
    # If GITHUB_REF is available, push to the branch. Otherwise just push.
    branch = os.getenv("GITHUB_REF_NAME", "main")

    # In GitHub actions, we can just run git push.
    # We will wrap it in a try-except or just let run_command handle the error if not connected to a remote.
    # Note: locally we might not want to actually push if there's no remote, but for testing let's check if remote exists
    try:
        # Check if remote exists
        has_remote = subprocess.run("git remote", shell=True, stdout=subprocess.PIPE, text=True).stdout.strip()
        if has_remote:
            print("Pushing commits to remote...")
            # We don't want to crash the whole script if the push fails due to lack of credentials locally.
            subprocess.run(
                f"git push origin {branch}",
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            print("Push command executed. (Note: It may fail locally without credentials, but will succeed in GitHub Actions).")
        else:
            print("No remote configured. Skipping git push.")
    except Exception as e:
        print(f"Failed to push: {e}")

if __name__ == "__main__":
    main()
