import os
import json
import subprocess
import datetime
import random
import string

def run_command(command):
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        raise Exception(f"Command failed: {command}\nError: {result.stderr}")
    return result.stdout.strip()

def get_random_string(length=10):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def main():
    state_file = 'state.json'
    log_file = 'commit_log.txt'

    # Ensure git config is set (useful for local testing and CI)
    git_user = os.getenv('GIT_USER_NAME', 'github-actions[bot]')
    git_email = os.getenv('GIT_USER_EMAIL', '41898282+github-actions[bot]@users.noreply.github.com')

    run_command(f'git config user.name "{git_user}"')
    run_command(f'git config user.email "{git_email}"')

    # Read current state
    if os.path.exists(state_file):
        with open(state_file, 'r') as f:
            try:
                state = json.load(f)
                day = state.get('day', 1)
            except json.JSONDecodeError:
                day = 1
    else:
        day = 1

    # Mapping of day to number of commits required
    commits_per_day = {
        1: 2,
        2: 4,
        3: 1,
        4: 5,
        5: 7
    }

    num_commits = commits_per_day.get(day, 2)
    print(f"Today is Day {day} in the loop. Making {num_commits} commits.")

    for i in range(1, num_commits + 1):
        # Update log file to create a genuine modification
        now = datetime.datetime.now().isoformat()
        rand_str = get_random_string(8)
        log_entry = f"{now} - Day {day}, Commit {i}/{num_commits} - {rand_str}\n"

        with open(log_file, 'a') as f:
            f.write(log_entry)

        run_command(f'git add {log_file}')

        # On the last commit of the day, we also update the state file for the next run
        if i == num_commits:
            next_day = (day % 5) + 1
            with open(state_file, 'w') as f:
                json.dump({'day': next_day}, f, indent=4)
            run_command(f'git add {state_file}')

        commit_msg = f"Automated commit: Day {day}, commit {i} of {num_commits}"
        run_command(f'git commit -m "{commit_msg}"')
        print(f"Created commit {i}/{num_commits}")

    # Push the changes
    print("Pushing changes to origin...")
    try:
        # Pushing HEAD to main branch
        run_command('git push origin HEAD:main')
        print("Push successful.")
    except Exception as e:
        print(f"Push warning/error (this can happen in local environments without correct setup): {e}")

if __name__ == '__main__':
    main()
