from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter

interpreter = RasaNLUInterpreter('../models/current/nlu')

# load your trained agent
agent = Agent.load("../models/dialogue", interpreter=interpreter)

input_channel = SlackInput(
    slack_token="YOUR_SLACK_TOKEN",
    # this is the `bot_user_o_auth_access_token`
    slack_channel="#awesome-project"
    # the name of your channel to which the bot posts (optional)
)

# set serve_forever=True if you want to keep the server running
s = agent.handle_channels([input_channel], 5000, serve_forever=True)