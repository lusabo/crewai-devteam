from crewai_tools import GithubSearchTool

github_tool = GithubSearchTool(
    github_repo="https://github.com/lusabo/transporteescolar",
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