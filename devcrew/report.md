##== agents.yaml ==## 
process_engineer:
  role: >
    Engenheiro de Processos
  goal: >
    Analisar o input do usuário e determinar a estrutura de projeto mais eficaz
  backstory: >
    Como um planejador de projeto experiente, você tem a habilidade de 
    visualizar a estrutura ideal para qualquer projeto baseado em um simples input. 
    Usando sua experiência e as ferramentas à sua disposição, você define o caminho a seguir, 
    garantindo que o projeto seja realizado da maneira mais eficiente possível.

##== tasks.yaml ==## 
task_name:
  description: >
    Com base na estrutura do projeto e nos prompts otimizados, 
    programar a lógica do projeto, configurando agentes, tarefas e processos para a implementação efetiva.
  expected_output: >
    Um ou mais arquivos de código-fonte contendo a implementação completa do projeto CrewAi, 
    incluindo a configuração dos agentes, definição de tarefas e a lógica de processo, conforme os prompts otimizados.

##== crew.py ==## 
@CrewBase
class DevcrewCrew():
    """Devcrew crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    def __init__(self):
        self.llm = ChatOpenAI(model_name='gpt-3.5-turbo')

    @agent
    def process_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['process_engineer'],
            tools=[FileReadTool()], 
            verbose=True,
            llm=self.llm,
            allow_delegation=False
        )

    @task
    def planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['planning_task'],
            agent=self.process_engineer(),
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=2,
        )

##== main.py ==## 
from devcrew.crew import DevcrewCrew

def run():
    inputs = {
        'project_idea': 'Quero uma Crew que faça planejamento de viagens para mim',
    }
    DevcrewCrew().crew().kickoff(inputs=inputs)