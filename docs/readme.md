# Project Name: Mercor ML Assignment

This project is designed to find the most technically complex repository among all the public repositories of a GitHub user. It utilizes Python, OpenAI APIs, langchain, and Cohere APIs to achieve this functionality.

## Directory Structure

```
/github-automated-analysis
|-- .venv
|-- data
|   |-- repos_cloned
|   |-- test_repos
|
|-- src
|   |-- modules.py
|   |-- consts.py
|   |-- preprocess.py
|   |-- evaluate_repo.py
|   |-- main.py
|
|-- tests
|   |-- test_preprocess.py
|   |-- test_evaluate_repo.py
|
|-- docs
|   |-- readme.md
|
|-- requirements.txt
|-- .gitignore
```

## Installation

To set up and run this project locally, please follow the instructions below:

1. Clone the repository:

```bash
git clone https://github.com/singhtanmay6735/github-automated-analysis.git
```

2. Navigate to the project directory:

```bash
cd github-automated-analysis
```

3. Create a virtual environment (optional but recommended):

```bash
python3 -m venv .venv
```

4. Activate the virtual environment:

```bash
# For Windows
.venv\Scripts\activate.bat

# For Unix/Linux
source .venv/bin/activate
```

5. Install the dependencies:

```bash
pip install -r requirements.txt
```

6. Set up API credentials:

   - OpenAI API:
     - Sign up for an account at [OpenAI](https://openai.com/).
     - Retrieve your API key.
     - Set the `OPENAI_API_KEY` environment variable with your API key.

   - Cohere API:
     - Sign up for an account at [Cohere](https://cohere.ai/).
     - Retrieve your API key.
     - Set the `COHERE_API_KEY` environment variable with your API key.

7. Run the application:

```bash
python src/main.py
```

## Usage

Once the application is running, you can access it through the localhost. It prompts you to enter a GitHub user URL. Provide the URL of the user whose repositories you want to analyze for technical complexity.

The application will retrieve the public repositories of the user, calculate their technical complexity using GPT, and display the repository with the highest complexity with justification.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more information.

## Contributors

- [Tanmay Singh](https://www.linkedin.com/in/singhtanmay345/)

## Acknowledgments

- This project uses the [OpenAI API](https://openai.com/) and the [Cohere API](https://cohere.ai/) for natural language processing tasks.
- Special thanks to the creators and maintainers of the libraries and APIs used in this project.