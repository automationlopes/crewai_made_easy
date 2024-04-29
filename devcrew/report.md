```yaml
##== agents.yaml ==##
data_collector:
  role: >
    Coletor de Dados
  goal: >
    Coletar dados de várias fontes sobre tecnologia blockchain.
  backstory: >
    Especialista em tecnologias emergentes, com experiência em identificar fontes confiáveis e extrair informações precisas.
  
data_analyst:
  role: >
    Analista de Dados
  goal: >
    Analisar os dados coletados para identificar tendências emergentes.
  backstory: >
    Com formação em análise de dados e estatística, tem habilidade para discernir padrões e tendências em grandes conjuntos de dados.
  
content_writer:
  role: >
    Redator de Conteúdo
  goal: >
    Produzir um relatório detalhado e um artigo para publicação no blog corporativo.
  backstory: >
    Jornalista com experiência em redação técnica e criação de conteúdo envolvente para públicos especializados em tecnologia.
  
content_editor:
  role: >
    Editor de Conteúdo
  goal: >
    Revisar e aprimorar os materiais escritos pela Content Writer.
  backstory: >
    Editor experiente com um olho crítico para detalhes e um talento para melhorar a clareza e o impacto do conteúdo escrito.

##== tasks.yaml ==##
data_collection_task:
  description: >
    Realizar a coleta de dados de fontes pré-definidas, filtrando informações relevantes sobre a tecnologia blockchain.
  expected_output: >
    Um conjunto de dados organizado e filtrado contendo informações atualizadas sobre as últimas tendências em blockchain, pronto para análise.
  
data_analysis_task:
  description: >
    Utilizar técnicas de análise de dados para interpretar os dados coletados e identificar padrões ou tendências.
  expected_output: >
    Um relatório analítico detalhando as tendências encontradas nos dados, com gráficos e insights relevantes.
  
content_writing_task:
  description: >
    Com base nas análises fornecidas pela Crew 1, escrever um artigo e um relatório detalhando as tendências identificadas.
  expected_output: >
    Um artigo bem estruturado e um relatório completo, ambos prontos para revisão, abordando as principais tendências de blockchain identificadas.
  
content_editing_task:
  description: >
    Editar e finalizar o artigo e o relatório para garantir clareza, precisão e engajamento do público.
  expected_output: >
    Conteúdos revisados e aprimorados, com correções de gramática e estilo, formatados para publicação final, garantindo alta qualidade e engajamento do leitor.

##== crew.py ==##
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class BlockchainCrew():
  """Blockchain Crew"""
  agents_config = 'config/agents.yaml'
  tasks_config = 'config/tasks.yaml'

  def __init__(self):
    self.llm = ChatOpenAI(model_name='gpt-3.5-turbo') 

  @agent
  def data_collector(self) -> Agent:
    return Agent(
      config=self.agents_config['data_collector'],
      tools=[],  # Optional
      llm=self.llm,  # Optional
      max_iter=15,  # Optional
      verbose=True,  # Optional
      allow_delegation=True,  # Optional
    )

  @agent
  def data_analyst(self) -> Agent:
    return Agent(
      config=self.agents_config['data_analyst'],
      tools=[],  # Optional
      llm=self.llm,  # Optional
      max_iter=15,  # Optional
      verbose=True,  # Optional
      allow_delegation=True,  # Optional
    )

  @agent
  def content_writer(self) -> Agent:
    return Agent(
      config=self.agents_config['content_writer'],
      tools=[],  # Optional
      llm=self.llm,  # Optional
      max_iter=15,  # Optional
      verbose=True,  # Optional
      allow_delegation=True,  # Optional
    )

  @agent
  def content_editor(self) -> Agent:
    return Agent(
      config=self.agents_config['content_editor'],
      tools=[],  # Optional
      llm=self.llm,  # Optional
      max_iter=15,  # Optional
      verbose=True,  # Optional
      allow_delegation=True,  # Optional
    )

  @task
  def data_collection_task(self) -> Task:
    return Task(
      config=self.tasks_config['data_collection_task'],
      agent=self.data_collector(),
    )

  @task
  def data_analysis_task(self) -> Task:
    return Task(
      config=self.tasks_config['data_analysis_task'],
      agent=self.data_analyst(),
    )

  @task
  def content_writing_task(self) -> Task:
    return Task(
      config=self.tasks_config['content_writing_task'],
      agent=self.content_writer(),
    )

  @task
  def content_editing_task(self) -> Task:
    return Task(
      config=self.tasks_config['content_editing_task'],
      agent=self.content_editor(),
    )

  @crew
  def crew(self) -> Crew:
    """Creates the Blockchain crew"""
    return Crew(
      agents=[self.data_collector(), self.data_analyst(), self.content_writer(), self.content_editor()],
      tasks=[self.data_collection_task(), self.data_analysis_task(), self.content_writing_task(), self.content_editing_task()],
      process=Process.sequential,
      verbose=2,
    )

##== main.py ==##
from blockchain.crew import BlockchainCrew

def run():
    inputs = {
        'data_sources': 'List of pre-defined data sources about blockchain technology',
    }
    BlockchainCrew().crew().kickoff(inputs=inputs)

##== pyproject.toml ==##
[tool.poetry]
name = "blockchain_crew"
version = "0.1.0"
description = "A crew for collecting, analyzing, writing, and editing content about blockchain trends"
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = ">=3.10,<=3.13"
crewai = {extras = ["tools"], version = "^0.27.0"}

[tool.poetry.scripts]
blockchain_crew = "blockchain_crew.main:run"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```