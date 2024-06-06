import os
import warnings
from config import llama3
from crewai import Crew, Process
from agents.developer import go_developer
from agents.tester import go_test_specialist
from tasks.developer_task import analyze_repository_architecture
from tasks.developer_task import identify_code_improvements
from tasks.developer_task import suggest_refactorings
from tasks.developer_task import consolidate_suggestions
from tasks.tester_task import review_existing_tests
from tasks.tester_task import identify_missing_tests
from tasks.tester_task import write_unit_and_integration_tests

def main():
        
    dev_crew = Crew(
        agents=[go_developer, go_test_specialist],
        tasks=[
            analyze_repository_architecture,
            identify_code_improvements,
            suggest_refactorings,
            review_existing_tests,
            identify_missing_tests,
            write_unit_and_integration_tests,
            consolidate_suggestions
        ],
        process=Process.sequential,
        verbose=True
    )

    result = dev_crew.kickoff()
    print(result)

if __name__ == "__main__":
    main()