import os
import warnings
from config import llama3
from crewai import Crew, Process
from src.agents.developer import go_developer
from src.agents.tester import go_test_specialist
from src.tasks.developer_task import analyze_repository_architecture
from src.tasks.developer_task import identify_code_improvements
from src.tasks.developer_task import suggest_refactorings
from src.tasks.tester_task import review_existing_tests
from src.tasks.tester_task import identify_missing_tests
from src.tasks.tester_task import write_unit_and_integration_tests

trip_crew = Crew(
    agents=[go_developer, go_test_specialist],
    tasks=[
        analyze_repository_architecture,
        identify_code_improvements,
        suggest_refactorings,
        review_existing_tests,
        identify_missing_tests,
        write_unit_and_integration_tests
    ],
    process=Process.sequential,
    verbose=True
)