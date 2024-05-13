#!/usr/bin/env python
from devcrew.crew import DevcrewCrew


def run():
    # Solicita ao usuário uma ideia de projeto
    project_idea = input("Por favor, insira sua ideia de projeto: ")
    
    # Cria uma instância de DevcrewCrew e inicia o processo com a ideia do projeto
    inputs = {
        'project_idea': project_idea,
    }
    DevcrewCrew().crew().kickoff(inputs=inputs)
    
    
    