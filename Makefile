train-nlu:
	python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose

train-core:
	python -m rasa_core.train -d domain.yml -c policy.yml -s stories.md -o models/dialogue

run-actions:
	python3 -m rasa_core_sdk.endpoint --actions demo.actions

run-cmdline:
	make run-actions&
	python3 -m rasa_core.run -d models/dialogue -u models/current/nlu --endpoints endpoints.yml

debug-cmdline:
	make run-actions&
	python3 -m rasa_core.run -d models/dialogue -u models/current/nlu --debug --endpoints endpoints.yml