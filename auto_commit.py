import os
import subprocess
import json
import datetime
import random
import string
import sys

def run_command(cmd, check=True):
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Command failed: {cmd}\nError: {result.stderr}")
        if check:
            sys.exit(1)
    return result.stdout.strip()

def main():
    # Configure git if running in automation
    if os.environ.get("GITHUB_ACTIONS"):
        run_command('git config --global user.name "github-actions[bot]"')
        run_command('git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"')

    state_file = 'state.json'
    log_file = 'commit_log.txt'

    # The 5-day cycle loop: 2, 4, 1, 5, 7
    commits_pattern = [2, 4, 1, 5, 7]

    # Load state
    if os.path.exists(state_file):
        with open(state_file, 'r') as f:
            try:
                state = json.load(f)
            except json.JSONDecodeError:
                state = {'day_index': 0}
    else:
        state = {'day_index': 0}

    day_index = state.get('day_index', 0)

    # Sanity check day_index
    if day_index >= len(commits_pattern) or day_index < 0:
        day_index = 0

    num_commits = commits_pattern[day_index]

    print(f"Starting day {day_index + 1} of cycle. Making {num_commits} commits.")

    for i in range(num_commits):
        # 1. Modify the log file
        now = datetime.datetime.now().isoformat()
        random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

        with open(log_file, 'a') as f:
            f.write(f"Automated execution at {now} - ID: {random_str}\n")

        run_command(f'git add {log_file}')

        # 2. Check if this is the final commit of the day
        if i == num_commits - 1:
            # Update the day index for tomorrow
            state['day_index'] = (day_index + 1) % len(commits_pattern)
            with open(state_file, 'w') as f:
                json.dump(state, f, indent=4)
            # Stage the state file so it is included in this final commit
            run_command(f'git add {state_file}')

        # 3. Create the commit
        commit_msg = f"Automated update: Day {day_index + 1}, commit {i + 1} of {num_commits}"
        run_command(f'git commit -m "{commit_msg}"')
        print(f"Created commit {i + 1}/{num_commits}")

    # Push changes to the repository
    print("Pushing commits to remote...")
    # Push without checking exit code so it doesn't fail locally where there's no remote
    push_result = subprocess.run('git push', shell=True, text=True, capture_output=True)
    if push_result.returncode != 0:
        print(f"Warning: git push failed (expected if running locally without a remote).\n{push_result.stderr}")
    else:
        print("Successfully pushed to remote.")

if __name__ == "__main__":
    main()
