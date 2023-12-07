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

bump:
	poetry version minor

release:
	git add .
	git commit -m "Release $(shell poetry version -s)"
	git tag v$(shell poetry version -s)
	git push origin --tags

version:
	poetry version --short

changelog:
	poetry run towncrier build --yes --version v$(shell poetry version -s)

build:
	poetry build

publish:
	poetry publish

clean:
	rm -rf dist
	rm -rf .pytest_cache
	rm -rf poetry.lock
	find . -type f -name '*.pyc' -delete

.PHONY: all build lint test clean
