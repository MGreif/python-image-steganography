.PHONY: test
test:
	pytest ./tests/integration_cli.py
	rm test.encoded.png