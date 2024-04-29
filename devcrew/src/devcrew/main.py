#!/usr/bin/env python
from devcrew.crew import DevcrewCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'project_idea': 'Quero uma equipe de inteligência artificial configurada para me ajudar a identificar e analisar as últimas tendências em tecnologia blockchain. Preciso que essa equipe seja capaz de coletar dados de várias fontes, analisá-los para entender as tendências emergentes e então produzir um relatório detalhado e um artigo que possam ser publicados em meu blog corporativo. A equipe deve ser composta por agentes especializados que possam não só realizar a pesquisa de forma autônoma, mas também preparar materiais escritos que sejam fáceis de entender e compartilhar com um público mais amplo. Espero que esta solução automatize grande parte do processo de coleta e síntese de informações para economizar tempo e aumentar a eficiência da minha equipe editorial.',
    }
    DevcrewCrew().crew().kickoff(inputs=inputs)
    
    
    