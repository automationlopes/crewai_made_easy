#!/usr/bin/env python
from devcrew.crew import DevcrewCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'project_idea': 'Quero uma crew que faça planejamento de viagens.',
    }
    DevcrewCrew().crew().kickoff(inputs=inputs)
    
    
    