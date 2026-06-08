import os
import json
import random
import string
import subprocess
from datetime import datetime
import sys

def run_command(command, check=True):
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Command failed: {command}")
        print(f"Error: {result.stderr}")
        if check:
            sys.exit(1)
    return result.stdout.strip()

def setup_git():
    run_command('git config --global user.name "github-actions[bot]"', check=False)
    run_command('git config --global user.email "github-actions[bot]@users.noreply.github.com"', check=False)

def get_state():
    try:
        with open('state.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"day": 1}

def save_state(state):
    with open('state.json', 'w') as f:
        json.dump(state, f)

def append_to_log(day, commit_num):
    timestamp = datetime.now().isoformat()
    random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    with open('commit_log.txt', 'a') as f:
        f.write(f"Day {day} - Commit {commit_num} at {timestamp} - {random_text}\n")

def main():
    setup_git()

    state = get_state()
    day = state.get('day', 1)

    # Rules:
    # Day 1: 2 commits
    # Day 2: 4 commits
    # Day 3: 1 commit
    # Day 4: 5 commits
    # Day 5: 7 commits
    commit_counts = {1: 2, 2: 4, 3: 1, 4: 5, 5: 7}
    num_commits = commit_counts.get(day, 2)

    print(f"Running commits for Day {day}. Total commits to make: {num_commits}")

    # Update day for next execution
    next_day = day + 1 if day < 5 else 1
    state['day'] = next_day
    save_state(state)

    for i in range(1, num_commits + 1):
        append_to_log(day, i)

        # Stage files (state.json will be modified and committed on the first iteration)
        run_command('git add commit_log.txt state.json')

        commit_msg = f"Automated commit {i}/{num_commits} for Day {day}"
        run_command(f'git commit -m "{commit_msg}"')

    # Push changes back to main
    print("Pushing changes...")
    run_command('git push origin HEAD:main')
    print(f"Successfully completed {num_commits} commits for Day {day}.")

if __name__ == "__main__":
    main()
