import os 
from git import Repo, exc
import re

repo = os.getenv('git_repo')
if 'https' in repo:
    repo_name = re.sub(r'https:\/\/github.com\/.*\/',"", repo)
elif 'ssh' in repo:
    repo_name = re.sub(r'git@github.com:\/.*\/',"", repo)
else:
    print('Repo name not recognised or is not git repo.')

folder_name = os.path.join('~', repo_name)
repo = Repo.init(os.path.join('~', repo_name))
origin = repo.remote(name='origin')
try:
    origin.pull('origin', 'main')
except:
    print('Pulling failed, is the repo empty?')

file_changes = [ item.a_path for item in repo.index.diff(None) ] + repo.untracked_files

if file_changes:
    repo.git.add(file_changes)
    listeee = ', '.join(file_changes)
    repo.index.commit(f'Updating {listeee}')
    origin.push()
