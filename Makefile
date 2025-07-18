#!make

all: install lint test

install:
	uv sync

example:
	uv run python -m wordplex -f "Porsche-91#"

lint:
	uv run ruff check . --fix
	uv run mypy .

test:
	uv run pytest

version:
	uv version --short

changelog:
	uv run towncrier build --yes --version v$(shell uv version --short)

publish-test:
	uv build
	uv config repositories.testpypi https://test.pypi.org/legacy/
	uv publish --no-interaction -r testpypi -u __token__ -p ${PYPI_TOKEN}

clean:
	rm -rf dist
	rm -rf .pytest_cache
	rm -rf uv.lock
	find . -type f -name '*.pyc' -delete

.PHONY: all build lint test clean
