from crewai import Task
from agents.tester import go_test_specialist
from tools.github import github_tool

review_existing_tests = Task(
    description="Revisar os testes existentes no repositório para avaliar sua cobertura "
                "e eficácia.",
    expected_output="Relatório de avaliação dos testes existentes, destacando os pontos "
                    "fortes e fracos, bem como a cobertura de código.",
    tools=[github_tool],
    agent=go_test_specialist
)

identify_missing_tests = Task(
    description="Identificar testes unitários e de integração que estão faltando para "
                "garantir a robustez do projeto.",
    expected_output="Lista de casos de teste que estão faltando, incluindo quais "
                    "funcionalidades ou módulos precisam de testes adicionais.",
    tools=[github_tool],
    agent=go_test_specialist
)

write_unit_and_integration_tests = Task(
    description="Escrever novos testes unitários e de integração para cobrir as lacunas "
                "identificadas.",
    expected_output="Conjunto de novos testes unitários e de integração escritos e "
                    "integrados no repositório, com relatórios de cobertura.",
    tools=[github_tool],
    agent=go_test_specialist
)
