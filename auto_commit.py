import os
import json
import random
import string
import datetime
import subprocess

# The loop pattern mapping day number to number of commits
commits_per_day = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

def run_command(cmd):
    try:
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {' '.join(cmd)}")
        print(f"Stderr: {e.stderr}")
        raise

def get_current_day():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, 'r') as f:
                data = json.load(f)
                return data.get('current_day', 1)
        except Exception:
            return 1
    return 1

def save_current_day(day):
    with open(STATE_FILE, 'w') as f:
        json.dump({'current_day': day}, f, indent=4)

def generate_random_text(length=20):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def setup_git():
    run_command(["git", "config", "--local", "user.name", "github-actions[bot]"])
    run_command(["git", "config", "--local", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"])

def main():
    current_day = get_current_day()
    num_commits = commits_per_day.get(current_day, 2)

    print(f"Starting auto-commit for Day {current_day}. Expected commits: {num_commits}")

    setup_git()

    for i in range(num_commits):
        # Update log file
        timestamp = datetime.datetime.now().isoformat()
        random_text = generate_random_text()
        log_entry = f"Commit {i+1}/{num_commits} for Day {current_day} | Timestamp: {timestamp} | Rand: {random_text}\n"

        with open(LOG_FILE, "a") as f:
            f.write(log_entry)

        # Update state on the last commit of the loop so it's committed
        if i == num_commits - 1:
            next_day = (current_day % 5) + 1
            save_current_day(next_day)

        # Stage files
        run_command(["git", "add", LOG_FILE])
        if os.path.exists(STATE_FILE):
            run_command(["git", "add", STATE_FILE])

        # Commit
        commit_message = f"Automated commit {i+1}/{num_commits} for Day {current_day}"
        run_command(["git", "commit", "-m", commit_message])

        print(f"Created commit {i+1}/{num_commits}")

    # Push changes
    print("Pushing changes to remote repository...")
    try:
        run_command(["git", "push", "origin", "HEAD:main"])
        print("Done!")
    except subprocess.CalledProcessError as e:
        print(f"Push failed, this might be expected if running locally without origin set up or without correct permissions. Error: {e}")

if __name__ == "__main__":
    main()
