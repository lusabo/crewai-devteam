from crewai import Task
from src.agents.developer import go_developer
from src.tools.github import github_tool

analyze_repository_architecture = Task(
    description="Analisar a arquitetura do repositório para identificar pontos de melhoria.",
    expected_output="Relatório detalhado das áreas da arquitetura que podem ser melhoradas, "
                    "incluindo sugestões específicas.",
    tools=[github_tool],
    agent=go_developer
)

identify_code_improvements = Task(
    description="Examinar o código do repositório e identificar pontos de melhoria, como "
                "refatorações e otimizações.",
    expected_output="Lista de recomendações de melhorias no código, com exemplos de "
                    "refatorações e otimizações sugeridas.",
    tools=[github_tool],
    agent=go_developer
)

suggest_refactorings = Task(
    description="Sugerir refatorações no código para melhorar a qualidade, manutenção e "
                "desempenho.",
    expected_output="Plano de refatoração detalhado, incluindo quais partes do código "
                    "precisam ser refatoradas e como.",
    tools=[github_tool],
    agent=go_developer
)
