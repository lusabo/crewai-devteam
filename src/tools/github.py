from crewai_tools import GithubSearchTool
from config import get_github_token, get_github_repo

github_tool = GithubSearchTool(
    github_repo=get_github_repo(),
    gh_token=get_github_token(),
    #search_query="Review Go code in Github Repo and provide feedback on issues and corrections that need to be made. Be sure to name each file and provide a brief description of the issues found.",
    content_types=['code'],
    config={
        "llm": {
            "provider": "ollama",
            "config": {
                "model": "llama3"
            },
        },
        "embedder": {
            "provider": "google",
            "config": {
                "model": "models/embedding-001",
                "task_type": "retrieval_document"
            }
        }
    }
)