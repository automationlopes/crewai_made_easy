from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from crewai_tools import FileReadTool
from devcrew.tools.compiler_tool import CodeCompilerTool
import os

load_dotenv()


@CrewBase
class DevcrewCrew():
	"""Devcrew crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
 
	def __init__(self):
		self.llm = ChatOpenAI(model_name='gpt-4-turbo')

	# Agentes
	@agent
	def process_engineer(self) -> Agent:
		return Agent(
			config=self.agents_config['process_engineer'],
			tools=[FileReadTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True,
			llm=self.llm,
			allow_delegation=False
		)

	@agent
	def prompt_engineer(self) -> Agent:
		return Agent(
			config=self.agents_config['prompt_engineer'],
			verbose=True,
			llm=self.llm,
			allow_delegation=False
		)
	@agent
	def developer(self) -> Agent:
		return Agent(
			config=self.agents_config['developer'],
			verbose=True,
			llm=self.llm,
            tools=[FileReadTool()],
			allow_delegation=False
		)

	@agent
	def compiler(self) -> Agent:
		return Agent(
			config=self.agents_config['compiler'],
			verbose=True,
			llm=self.llm,
            tools=[
                FileReadTool(),
                CodeCompilerTool()
                ],
			allow_delegation=False,
			max_iter=6
		)
 
 
	#Tarefas
	@task
	def planning_task(self) -> Task:
		return Task(
			config=self.tasks_config['planning_task'],
			agent=self.process_engineer(),
		)

	@task
	def prompting_task(self) -> Task:
		return Task(
			config=self.tasks_config['prompting_task'],
			agent=self.prompt_engineer(),
		)
  
	@task
	def coding_task(self) -> Task:
		return Task(
			config=self.tasks_config['coding_task'],
			agent=self.developer(),
   			output_file='report.md',
		)
	
	@task
	def compiling_task(self) -> Task:
		return Task(
			config=self.tasks_config['compiling_task'],
			agent=self.compiler(),
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Dev crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
