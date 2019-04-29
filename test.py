#!/usr/bin/env python3
from rasa_nlu.model import Metadata, Interpreter
import json


def pprint(o):

 # small helper to make dict dumps a bit prettier
    print(json.dumps(o, indent=2))


interpreter = Interpreter.load('./models/current/nlu')


def assertIntent(text, intent):
    firstIntent = interpreter.parse(text)["intent"]
    assert(firstIntent["name"] == intent)
    assert(firstIntent["confidence"] >= 0.5)


pprint(interpreter.parse("再见"))

pprint(interpreter.parse("你是谁"))

pprint(interpreter.parse('你的主人是谁'))

pprint(interpreter.parse("你好"))
