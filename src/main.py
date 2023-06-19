from src.modules import * 
from src.preprocess  import clone_repo, get_repositories, delete_repo
from src.evaluate_repo import evaluate_repo 

def find_most_complex_repo(user):
    repos = get_repositories(user)
    max_score = 0
    max_repo = None
    for repo in repos:
        local_path = f'data/repos_clone/{user}/{repo["name"]}'
        clone_repo(repo["clone_url"], local_path)
        score = evaluate_repo(local_path)
        if score > max_score:
            max_score = score
            max_repo = repo        
        delete_repo(local_path)
    return max_repo, max_score


most_complex_repo = find_most_complex_repo('username')
