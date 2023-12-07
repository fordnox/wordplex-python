#!make

all: install lint test

install:
	poetry lock
	poetry install --with test,dev

example:
	poetry run python -m wordplex -f "Porsche-99#"

lint:
	poetry run black .
	poetry run isort .

test:
	poetry run pytest

version:
	poetry version --short

changelog:
	poetry run towncrier build --yes --version v$(shell poetry version -s)

publish-test:
	poetry build
	poetry config repositories.testpypi https://test.pypi.org/legacy/
	poetry publish --no-interaction -r testpypi -u __token__ -p ${PYPI_TOKEN}

clean:
	rm -rf dist
	rm -rf .pytest_cache
	rm -rf poetry.lock
	find . -type f -name '*.pyc' -delete

.PHONY: all build lint test clean
