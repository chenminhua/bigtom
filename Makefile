train-nlu:
	python -m rasa_nlu.train -c nlu_config.yml --data data/nlu/nlu.md -o models --fixed_model_name nlu --project current --verbose

train-core:
	python -m rasa_core.train -d domain.yml -c policy.yml -s data/core -o models/dialogue

run-actions:
	python3 -m rasa_core_sdk.endpoint --actions demo.actions

run-cmdline:
	make run-actions&
	python3 -m rasa_core.run -d models/dialogue -u models/current/nlu --endpoints endpoints.yml

debug-cmdline:
	make run-actions&
	python3 -m rasa_core.run -d models/dialogue -u models/current/nlu --debug --endpoints endpoints.yml

visualize:
	python3 -m rasa_core.visualize -s data/core/ -d domain.yml -o story_graph.png

# slack endpoint 为 /webhooks/slack/webhook
slackbot:
	python -m rasa_core.run --enable_api -d models/dialogue -u models/current/nlu --port 5000 --credentials credentials.yml
