from crewai import Agent
from config import EnvConfig

class DeveloperAgent:

    def __init__(self, tools):
        self.tools = tools

    def developer(self):
        return Agent(
            role="Experienced Software Developer in Go",
            goal="Analyze and provide improvements to the architecture "
                 "and code of the Go project contained in the provided repository.",
            backstory="This agent is an experienced software developer"
                      "with deep familiarity with the Go language. He is "
                      "able to analyze code repositories, identify "
                      "points for improvement in the architecture and suggest "
                      "refactorings to improve code quality.",
            allow_delegation=False,
            tools=self.tools, 
            verbose=True,
            llm=EnvConfig().get_llama3()
        )