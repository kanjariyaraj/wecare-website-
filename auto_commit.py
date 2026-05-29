import os
import random
import time
import json
import subprocess

def make_commit():
    timestamp = str(time.time())

    with open('commit_log.txt', 'a') as f:
        f.write(f"Commit at {timestamp}\n")

    state = {'last_commit': timestamp}
    with open('state.json', 'w') as f:
        json.dump(state, f)

    subprocess.run(['git', 'add', 'commit_log.txt', 'state.json'])
    subprocess.run(['git', 'commit', '-m', f"Auto commit at {timestamp}"])

def main():
    num_commits = random.randint(5, 10)
    print(f"Making {num_commits} commits...")
    for i in range(num_commits):
        make_commit()
        time.sleep(1) # Sleep to get distinct timestamps
    print("Done!")

if __name__ == '__main__':
    main()
