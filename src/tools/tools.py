from crewai_tools import GithubSearchTool
from config import EnvConfig

class Tools:

    def __init__(self):
        pass
    
    def github_tool(self):
        return GithubSearchTool(
            github_repo=EnvConfig().get_github_repo(),
            gh_token=EnvConfig().get_github_token(),
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