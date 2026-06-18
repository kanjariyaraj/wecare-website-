import json
import os
import random
import string
import subprocess
import datetime

STATE_FILE = "state.json"
LOG_FILE = "commit_log.txt"

# Number of commits for each day (1 to 5)
COMMIT_PATTERN = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def load_state():
    if not os.path.exists(STATE_FILE):
        return {"current_day": 1}
    with open(STATE_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {"current_day": 1}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)

def run_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {cmd}\n{result.stderr}")
    return result

def setup_git():
    run_command('git config --global user.name "GitHub Action Bot"')
    run_command('git config --global user.email "action@github.com"')
    run_command('git config --global pull.rebase false')

def make_commit(commit_num, day, is_last_commit=False, new_day=None):
    random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as f:
        f.write(f"Commit {commit_num} for Day {day} at {timestamp} - {random_text}\n")

    run_command(f'git add {LOG_FILE}')

    if is_last_commit and new_day is not None:
        save_state({"current_day": new_day})
        run_command(f'git add {STATE_FILE}')

    run_command(f'git commit -m "Automated commit {commit_num} for Day {day}"')

def main():
    setup_git()

    state = load_state()
    current_day = state.get("current_day", 1)

    num_commits = COMMIT_PATTERN.get(current_day, 2)
    next_day = current_day + 1 if current_day < 5 else 1

    print(f"Starting automation for Day {current_day} - Making {num_commits} commits.")

    for i in range(num_commits):
        is_last = (i == num_commits - 1)
        make_commit(i + 1, current_day, is_last_commit=is_last, new_day=next_day)

    # Push the changes
    print("Pushing commits to remote...")
    run_command('git push origin main')
    print("Done!")

if __name__ == "__main__":
    main()
