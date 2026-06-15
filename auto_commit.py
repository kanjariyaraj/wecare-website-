import os
import json
import subprocess
import datetime
import random
import string

# Constants
STATE_FILE = 'state.json'
LOG_FILE = 'commit_log.txt'
BRANCH = 'main'

# Daily commit loop pattern
COMMIT_PATTERN = {
    1: 2,
    2: 4,
    3: 1,
    4: 5,
    5: 7
}

def run_command(command):
    """Executes a shell command and returns the output."""
    try:
        result = subprocess.run(command, check=True, text=True, shell=True, capture_output=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error message: {e.stderr}")
        # Allow failing to push if testing locally
        if "git push" not in command:
            raise e

def get_current_day():
    """Reads the current day from the state file. Defaults to 1 if not found."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            try:
                state = json.load(f)
                return state.get('day', 1)
            except json.JSONDecodeError:
                return 1
    return 1

def update_state(day):
    """Updates the state file with the next day in the loop."""
    next_day = (day % 5) + 1
    with open(STATE_FILE, 'w') as f:
        json.dump({'day': next_day}, f, indent=4)
    return next_day

def generate_random_string(length=10):
    """Generates a random alphanumeric string."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def make_commits(day, num_commits):
    """Makes the required number of commits for the day."""
    print(f"Day {day} in loop: Making {num_commits} commits.")

    for i in range(1, num_commits + 1):
        # 1. Modify the log file
        timestamp = datetime.datetime.now().isoformat()
        random_text = generate_random_string()
        log_entry = f"Commit {i}/{num_commits} on Day {day} - {timestamp} - {random_text}\n"

        with open(LOG_FILE, 'a') as f:
            f.write(log_entry)

        # 2. Stage the log file
        run_command(f'git add {LOG_FILE}')

        # 3. If it's the last commit of the day, update and stage the state file
        if i == num_commits:
            next_day = update_state(day)
            print(f"Updating state to Day {next_day} for the next run.")
            run_command(f'git add {STATE_FILE}')

        # 4. Commit the changes
        commit_message = f"Auto-commit: Day {day}, Commit {i}/{num_commits}"
        run_command(f'git commit -m "{commit_message}"')
        print(f"Created commit: {commit_message}")

def configure_git():
    """Configures git username and email for the automation."""
    run_command('git config user.name "github-actions[bot]"')
    run_command('git config user.email "41898282+github-actions[bot]@users.noreply.github.com"')

def main():
    # Ensure git is configured (useful for CI/CD environments)
    configure_git()

    # Get current day
    day = get_current_day()

    # Ensure day is within 1-5
    if day not in COMMIT_PATTERN:
        day = 1

    num_commits = COMMIT_PATTERN[day]

    # Make the commits
    make_commits(day, num_commits)

    # Push the changes
    print(f"Pushing commits to {BRANCH}...")
    run_command(f'git push origin {BRANCH}')
    print("Push complete.")

if __name__ == "__main__":
    main()
