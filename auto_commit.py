import os
import json
import random
import string
import subprocess
from datetime import datetime, timezone

STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

# Number of commits for each day in the loop
COMMIT_PATTERN = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def get_state():
    """Reads the current day from state.json, defaults to 1 if not found."""
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r") as f:
                data = json.load(f)
                return data.get("day", 1)
        except json.JSONDecodeError:
            return 1
    return 1

def update_state(current_day):
    """Updates state.json with the next day in the loop."""
    next_day = current_day + 1
    if next_day > 5:
        next_day = 1

    with open(STATE_FILE, "w") as f:
        json.dump({"day": next_day}, f, indent=4)

def generate_random_text(length=20):
    """Generates random string of characters."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def run_git_command(command):
    """Runs a git command and handles potential errors."""
    try:
        subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"Error running command '{command}': {e.stderr.decode('utf-8')}")
        raise

def setup_git():
    """Configures git user for automated commits."""
    print("Setting up Git config...")
    run_git_command("git config --local user.email 'github-actions[bot]@users.noreply.github.com'")
    run_git_command("git config --local user.name 'github-actions[bot]'")

def main():
    print("Starting auto_commit process...")
    setup_git()

    current_day = get_state()
    num_commits = COMMIT_PATTERN.get(current_day, 2) # default to day 1 (2 commits) if invalid state

    print(f"Current Day: {current_day}, Scheduled Commits: {num_commits}")

    for i in range(1, num_commits + 1):
        # 1. Modify the log file
        now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        random_text = generate_random_text()
        log_entry = f"Commit {i}/{num_commits} for Day {current_day} - {now_str} - {random_text}\n"

        with open(LOG_FILE, "a") as f:
            f.write(log_entry)

        print(f"Prepared commit {i}/{num_commits}...")

        # 2. Stage the log file
        run_git_command(f"git add {LOG_FILE}")

        # 3. If it's the final commit for the day, update and stage the state file
        if i == num_commits:
            print("Final commit of the day, updating state file...")
            update_state(current_day)
            run_git_command(f"git add {STATE_FILE}")

        # 4. Commit changes
        commit_message = f"Auto-commit day {current_day}: entry {i} of {num_commits}"
        run_git_command(f"git commit -m \"{commit_message}\"")

    # 5. Push all commits to the repository
    print("Pushing commits to remote...")
    # Using '|| true' on push if there's no remote, to allow testing locally
    try:
        # Check if we have a remote
        subprocess.run("git remote -v", check=True, shell=True, stdout=subprocess.PIPE)
        # Push changes. If inside GH Actions, it will push using GITHUB_TOKEN
        run_git_command("git push")
        print("Push successful!")
    except subprocess.CalledProcessError:
        print("No remote configured or push failed, skipping push step (safe for local testing).")

if __name__ == "__main__":
    main()
