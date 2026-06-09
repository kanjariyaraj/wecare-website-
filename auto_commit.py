import os
import json
import random
import string
import datetime
import subprocess

STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

# Define the commit pattern for each day
COMMIT_PATTERN = {
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
        return False
    return True

def get_current_day():
    if not os.path.exists(STATE_FILE):
        return 1
    with open(STATE_FILE, "r") as f:
        try:
            state = json.load(f)
            return state.get("current_day", 1)
        except json.JSONDecodeError:
            return 1

def update_state(day):
    next_day = day + 1
    if next_day > 5:
        next_day = 1

    with open(STATE_FILE, "w") as f:
        json.dump({"current_day": next_day}, f)

def generate_random_string(length=10):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def make_commit(commit_number, day):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_str = generate_random_string()

    # Append to log file
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] Day {day}, Commit {commit_number} - Random data: {random_str}\n")

    # Stage the files
    run_command("git add " + LOG_FILE)
    run_command("git add " + STATE_FILE)

    # Commit the changes
    commit_msg = f"Auto-commit: Day {day}, Commit {commit_number} ({timestamp})"
    run_command(f'git commit -m "{commit_msg}"')

def main():
    # Configure git if running in CI environment
    if os.environ.get("GITHUB_ACTIONS"):
        run_command('git config --global user.email "github-actions[bot]@users.noreply.github.com"')
        run_command('git config --global user.name "github-actions[bot]"')

    day = get_current_day()
    num_commits = COMMIT_PATTERN.get(day, 2) # Default to Day 1 if something goes wrong

    print(f"Starting auto-commit process for Day {day}. Making {num_commits} commits.")

    # Update state before committing so it gets included in the commits
    update_state(day)

    for i in range(1, num_commits + 1):
        make_commit(i, day)

    # Push changes back to main branch
    print("Pushing changes to remote repository...")
    run_command("git push origin main")
    print("Done!")

if __name__ == "__main__":
    main()
