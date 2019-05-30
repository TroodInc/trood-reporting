-include .env

APP := trood_reporting


default: run

build:
	@echo Building container ...
	@docker-compose build

release: build
	@echo Pushing image to private registry ...
	@docker push registry.tools.trood.ru/trood_reporting

test:
	@pipenv run pytest --create-db

install:
	@echo Install dependicices ...
	@pipenv install

run:
	@echo Start server ...
	@pipenv run ./manage.py migrate --no-input
	@pipenv run ./manage.py runserver 0.0.0.0:10000

.PHONY: run default install test build release
