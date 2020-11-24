import subprocess

def get_git_hash():
    return subprocess.check_output(['git', 'log', '-n', '1', '--pretty=tformat:%H']).strip()

def get_git_short_hash():
    return subprocess.check_output(['git', 'log', '-n', '1', '--pretty=tformat:%h']).strip()

def get_git_short_hash_and_commit_date():
    return subprocess.check_output(['git', 'log', '-n', '1', '--pretty=tformat:%h-%ad', '--date=short']).strip().decode("utf-8")

def get_git_status():
    return subprocess.check_output(['git', 'status', '-s']).strip().decode("utf-8")

if __name__ == "__main__":
    print(get_git_hash())
    print(get_git_short_hash())
    print(get_git_short_hash_and_commit_date())

    git_status = get_git_status()
    print (git_status)
    if (git_status is None):
        print(f'Repo is CLEAN')
    else:
        print(f'Repo has uncommited changes!!!')

