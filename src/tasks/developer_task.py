from crewai import Task
from agents.developer import go_developer
from tasks.tester_task import review_existing_tests, identify_missing_tests, write_unit_and_integration_tests
from tools.github import github_tool

analyze_repository_architecture = Task(
    description="Analisar a arquitetura do repositório para identificar pontos de melhoria.",
    expected_output="Relatório detalhado das áreas da arquitetura que podem ser melhoradas, "
                    "incluindo sugestões específicas com exemplo de código.",
    tools=[github_tool],
    agent=go_developer
)

identify_code_improvements = Task(
    description="Examinar o código do repositório e identificar pontos de melhoria, como "
                "refatorações e otimizações.",
    expected_output="Lista de recomendações de melhorias no código, com exemplos de "
                    "código refatorados e otimizações sugeridas.",
    tools=[github_tool],
    agent=go_developer
)

suggest_refactorings = Task(
    description="Sugerir refatorações no código para melhorar a qualidade, manutenção e "
                "desempenho.",
    expected_output="Plano de refatoração detalhado, incluindo quais partes do código "
                    "precisam ser refatoradas indicando o nome do arquivo e a sugestão "
                    "de como o código ficaria.",
    tools=[github_tool],
    agent=go_developer
)

consolidate_suggestions = Task(
    description="Consolidar todas as informações de suas atividades e do tester.",
    expected_output="Plano consolidado em formato markdown.",
    agent=go_developer,
    context=[
        analyze_repository_architecture,
        identify_code_improvements,
        suggest_refactorings,
        review_existing_tests,
        identify_missing_tests,
        write_unit_and_integration_tests
    ]
)
