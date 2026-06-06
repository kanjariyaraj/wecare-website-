import json
import os
import random
import string
import subprocess
from datetime import datetime

def setup_git():
    """Configure git with a bot user if it's not already configured."""
    try:
        # Check if user.name is set
        subprocess.run(["git", "config", "user.name"], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print("Setting up git config...")
        subprocess.run(["git", "config", "--global", "user.name", "github-actions[bot]"], check=False)
        subprocess.run(["git", "config", "--global", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"], check=False)
        subprocess.run(["git", "config", "--global", "--add", "safe.directory", "/github/workspace"], check=False)

def get_random_string(length=10):
    """Generate a random alphanumeric string."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def main():
    state_file = 'state.json'
    log_file = 'commit_log.txt'

    # 1. Read state
    if not os.path.exists(state_file):
        state = {"current_day": 1}
    else:
        with open(state_file, 'r') as f:
            state = json.load(f)

    current_day = state.get('current_day', 1)

    # 2. Map day to number of commits based on the loop pattern
    commits_schedule = {
        1: 2,
        2: 4,
        3: 1,
        4: 5,
        5: 7
    }

    num_commits = commits_schedule.get(current_day, 2)

    print(f"Starting automation for Day {current_day}: {num_commits} commits to be made.")

    # 3. Calculate next day
    next_day = current_day + 1
    if next_day > 5:
        next_day = 1

    state['current_day'] = next_day

    # Write updated state so it's staged and committed
    with open(state_file, 'w') as f:
        json.dump(state, f, indent=2)

    setup_git()

    # Determine the branch to push to. Defaulting to main.
    try:
        branch = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
        if branch == "HEAD":
            # We are in a detached HEAD state, let's use the environment variable if available (e.g. GitHub Actions)
            branch = os.environ.get("GITHUB_REF_NAME", "main")
    except subprocess.CalledProcessError:
        branch = "main"

    # 4. Perform the commits
    for i in range(num_commits):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        rand_str = get_random_string(15)

        # Append to log
        with open(log_file, 'a') as f:
            f.write(f"[{now}] Automated commit {i+1}/{num_commits} for Day {current_day}. Ref: {rand_str}\n")

        # Stage files
        subprocess.run(["git", "add", state_file, log_file], check=True)

        # Commit
        commit_msg = f"Automated commit {i+1}/{num_commits} (Day {current_day})"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        print(f"Created commit: {commit_msg}")

    # 5. Push changes
    print(f"Pushing changes to origin {branch}...")
    res = subprocess.run(["git", "push", "origin", f"HEAD:{branch}"], capture_output=True, text=True)
    if res.returncode == 0:
        print("Push successful!")
    else:
        print("Push failed. (This might be expected in a local test environment without a remote)")
        print(res.stderr)

if __name__ == "__main__":
    main()
