from crewai import Agent,Task,Crew,Process
import os

os.environ["OPENAI_API_KEY"]="Your API Key"

#AGENTS

Researcher = Agent(
    role="Market Researcher",
    goal="Find competitors of tesla",
    backstory="Ev market expert",
    llm="gpt-4o-mini",
    verbose=True
)

analyst =Agent(
    role="Business Analysis",
    goal="Analyse the strengths and weaknesses",
    backstory="stategy consultant",
    llm="gpt-4o-mini",
    verbose=True
)

writer =Agent(
    role="Report Writer",
    goal="Create a final Report",
    backstory="Business Writer",
    llm="gpt-4o-mini",
    verbose=True
)

# Task 1
Research_task =Task(
    description="Identify Tesla Competitors",
    expected_output="""
    Competitors list and their vehicle list
""",
agent=Researcher
)

Analyst_task =Task(
    description="Analyze the copetitors identified by researcher task also evaluate their potential strenghs and weakness",
    expected_output="""
     Compettiors comparison with strengths and weaknesses
""",
agent=analyst,
context=[Research_task]
)

Writer_task =Task(
    description="Prepare a professional business report on Tesla's competitors. Clearly identify the limitations based on the available research",
    expected_output="""
     Compile a structured business report suitable for management audience
""",
agent=writer,
context=[Research_task,Analyst_task]
)


#Crew
crew =Crew(
    agents=[Researcher,analyst,writer],
    tasks=[Research_task,Analyst_task,Writer_task],
    process=Process.sequential,
    Vebose=True
)
#Run
result =crew.kickoff()
print(result)

# Agent =Who
# Task =What
# Crew =Team
#Process=How workflow is organized
# LLM= Intelligence 

#Task for Learners :

#Researcher: Identify the leading automobile manufacturers in India.
#Analyst: Compare their market positions and competitive strengths.
#Writer: Prepare an executive summary for management.