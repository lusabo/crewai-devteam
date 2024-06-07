from crewai import Crew, Process
from agents.developer import DeveloperAgent
from agents.tester import TesterAgent
from tasks.developer_task import DeveloperTasks
from tasks.tester_task import TesterTasks
from tools.tools import Tools
class DeveloperTeamCrew:
    
    def run(self):

        #Tools
        tools = [Tools().github_tool()]

        #Agents
        dev = DeveloperAgent(tools).developer()
        tester = TesterAgent(tools).tester()
        
        #Tasks
        dev_tasks = DeveloperTasks(tools, dev)
        test_tasks = TesterTasks(tools, tester)

        crew = Crew(
            agents=[dev, tester],
            tasks=[dev_tasks.consolidate_suggestions(
                        [dev_tasks.repository_review(), 
                        test_tasks.enhance_test_coverage()]
                   )],
            process=Process.sequential,
            verbose=True
        )

        result = crew.kickoff()
        return result
        

# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("\n-------------------------------")
    print("## Team starting with full steam.")
    print("-------------------------------")
    devteam_crew = DeveloperTeamCrew()
    result = devteam_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)