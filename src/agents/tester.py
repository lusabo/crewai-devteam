from crewai import Agent
from config import EnvConfig

class TesterAgent:

    def __init__(self, tools):
        self.tools = tools

    def tester(self):
        return Agent(
            role="Unit Testing Specialist in Go",
            goal="Create unit tests for the Go project"
                 "contained in the provided repository."  ,
            backstory="This agent is an expert in testing with broad "
                      "knowledge in testing applications developed in Go. "
                      "It reviews existing tests, identifies gaps in"
                      "tests and writes new unit tests to ensure the"
                      "project is robust and reliable.",
            allow_delegation=False,
            tools=self.tools,  
            verbose=True,
            llm=EnvConfig().get_llama3()
        )