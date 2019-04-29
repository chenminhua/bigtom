from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import time

interpreter = RasaNLUInterpreter('models/current/nlu')
agent = Agent.load('models/dialogue', interpreter=interpreter)


while True:
    time.sleep(0.3)
    a = input()
    if a == 'stop':
        break
    responses = agent.handle_message(a)
    print(responses)
