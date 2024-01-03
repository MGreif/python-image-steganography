.PHONY: test
test:
	pytest -s ./tests/integration_cli.py
	pytest -s ./src
	rm test.encoded.png
