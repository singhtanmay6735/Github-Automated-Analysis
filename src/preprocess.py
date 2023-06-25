from src.modules import *
from src.const import LOADER_MAPPING, EXCLUDE_FILES, ipynb

def get_repositories(user):                                                           #change user in get_repositories to user_url.
    response = requests.get(f'https://api.github.com/users/{user}/repos')
    if response.status_code == 200:
        repos = json.loads(response.text)
        return repos
    else:
        return None

def clone_repo(repo_url, local_path):
    Repo.clone_from(repo_url, local_path)

def delete_repo(local_path):
    shutil.rmtree(local_path)

def get_repo(root_dir):
    try:
        return Repo(root_dir)
    except:
        return None


def is_ignored(path, root_dir):
    repo = get_repo(root_dir)
    if repo is None:
        return False
    if not os.path.exists(path):
        return False
    ignored = repo.ignored(path)
    return len(ignored) > 0


def fetch_ipynb_content(content):
    notebook = nbformat.reads(content, as_version=4)
    python_exporter = PythonExporter()
    python_code, _ = python_exporter.from_notebook_node(notebook)
    return python_code

@Halo(text='📂 Loading files', spinner='dots')
def load_files(root_dir):
    num_cpus = multiprocessing.cpu_count()
    loaded_files = []
    with multiprocessing.Pool(num_cpus) as pool:
        futures = []
        for file_path in glob.glob(os.path.join(root_dir, '**/*'), recursive=True):
            if is_ignored(file_path, root_dir):
                continue
            if any(
                    file_path.endswith(exclude_file) for exclude_file in EXCLUDE_FILES):
                continue
            for ext in LOADER_MAPPING:
                if file_path.endswith(ext):
                    loader = LOADER_MAPPING[ext]['loader']
                    args = LOADER_MAPPING[ext]['args']
                    load = loader(file_path, **args)
                    futures.append(pool.apply_async(load.load_and_split))
                    loaded_files.append(file_path)
                if file_path.endswith(ipynb):
                    python_code = fetch_ipynb_content(file_path)
                    loaded_files.append(python_code)
            
        docs = []
        for future in futures:
            docs.extend(future.get())

    print('\n' + '\n'.join([f'📄 {os.path.abspath(file_path)}:' for file_path in loaded_files]))
    return len(loaded_files), loaded_files, docs


def calculate_cost(texts, model_name):
    enc = tiktoken.encoding_for_model(model_name)
    all_text = ''.join([text.page_content for text in texts])
    tokens = enc.encode(all_text)
    token_count = len(tokens)
    cost = (token_count / 1000) * 0.0004
    return cost

@Halo(text=' Splitting texts', spinner='dots')
def divide_chunks(texts, model_name):
    enc = tiktoken.encoding_for_model(model_name)
    all_text = ''.join([text.page_content for text in texts])
    tokens = enc.encode(all_text)
    token_count = len(tokens)
    chunk_size = (token_count / 1000) * 0.0004
    chunks = []
    for i in range(0, len(tokens), int(chunk_size)):
        chunks.append(tokens[i:i + int(chunk_size)])
    return chunks

def preprocess_and_save_files(local_path):
    # Add your code to preprocess files here.
    # The code should iterate over files in the repository,
    # preprocess the code and save it into chunks if necessary.
    a = " "