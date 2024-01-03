.PHONY: test
test:
	pytest -s ./tests/integration_cli.py
	rm test.encoded.png
