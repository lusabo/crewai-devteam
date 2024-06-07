from crewai import Task

class TesterTasks:

    def __init__(self, tools, agent):
            self.tools = tools
            self.agent = agent

    def enhance_test_coverage(self):
        return Task(
            description="Evaluate the current test suite for coverage and effectiveness, "
                        "identify gaps in unit tests, and create new tests to improve the "
                        "project's robustness.",
            expected_output="A comprehensive report detailing the strengths, weaknesses, "
                            "and code coverage of existing tests, a prioritized list of missing "
                            "test cases for specific features or modules, and a set of newly written "
                            "unit and integration tests to fill identified gaps.",
            tools=self.tools,
            agent=self.agent
        )