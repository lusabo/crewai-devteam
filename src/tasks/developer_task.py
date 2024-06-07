from crewai import Task
from tasks.tester_task import TesterTasks

class DeveloperTasks: 

    def __init__(self, tools, agent):
        self.tools = tools
        self.agent = agent
        self.tester_task = TesterTasks(self.tools, self.agent).enhance_test_coverage()

    def repository_review(self):
        return Task(
            description="Analyze the provided repository to identify points for improvement "
                        "in the architecture and code. This includes examining the code for "
                        "potential refactorings and optimizations to enhance quality, maintainability, "
                        "and performance.",
            expected_output="A detailed report outlining architecture improvement points, code "
                            "refactoring recommendations with examples, and a comprehensive "
                            "refactoring plan with specific file names and suggested code changes.",
            tools=self.tools,
            agent=self.agent
        )

    def consolidate_suggestions(self, ctx: any):
        return Task(
            description="Consolidate all the information made by me and the tester.",
            expected_output="Consolidated plan in markdown format.",
            agent=self.agent,
            context=ctx
        )
