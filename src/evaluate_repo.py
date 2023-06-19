from src.modules import *
from src.preprocess import preprocess_and_save_files

def pass_code_through_gpt(file_path):
    # Add your code to load code from file,
    # create prompt and pass it through GPT.
    # Return the complexity score.
    a = " "

def evaluate_repo(local_path):
    preprocess_and_save_files(local_path)
    total_score = 0
    num_files = 0
    for root, dirs, files in os.walk(local_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_score = pass_code_through_gpt(file_path)
            total_score += file_score
            num_files += 1
    return total_score / num_files if num_files > 0 else 0
