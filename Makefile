all: build demo

build:
	python tools/chatflow_to_json.py exemplos/chatflow_rules_example.cf exemplos/from_rules.json

demo:
	python tools/simulate_chatflow.py exemplos/from_rules.json --script exemplos/fluxo1.txt
	python tools/simulate_chatflow.py exemplos/from_rules.json --script exemplos/fluxo2.txt
	python tools/simulate_chatflow.py exemplos/from_rules.json --script exemplos/fluxo3.txt

test:
	python -m unittest discover -s tests -p "*.py"
