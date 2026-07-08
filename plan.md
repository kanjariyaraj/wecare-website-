1. **Create auto_commit.py**: Write a Python script that reads a `state.json`, determines how many commits to make based on the 5-day cycle (2, 4, 1, 5, 7), modifies `commit_log.txt`, and commits the changes using Git. The final commit of the day will also include the updated `state.json` to maintain exact commit counts.
2. **Create state files**: Initialize `state.json` with `{"current_day": 1}` and create an empty `commit_log.txt`.
3. **Create GitHub Action**: Create `.github/workflows/auto_commit.yml` configured to run `auto_commit.py` daily using a cron schedule. It will have permissions to push changes back to the repository.
4. **Create INSTRUCTIONS.md**: Provide clear, step-by-step instructions on how the loop works and how to set it up or modify it.
5. **Pre-commit checks**: Run `pre_commit_instructions` and ensure all quality checks pass.
6. **Submit**: Once verified, commit and submit the code.
