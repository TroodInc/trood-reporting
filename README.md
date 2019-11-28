# Trood Reporting

## Requirements

* Python 3.6
* PostgreSQL

## Settings

`DEBUG` - режим отладки.

`DATABASE_URL` - DSN строка подключения к БД.

`SECRET_KEY` - соль.

`SENTRY_ENABLED` - включение логирования ошибок.

`SENTRY_DSN` - DSN строка поключени к Sentry.

`SENTRY_ENV` - метка развертывания.

## Getting started

```bash
sudo pip install pipenv
pipenv install
cp .env-example .env
pipenv run ./manage.py runserver
```

## Docker

```bash
docker-compose up --build
```

## Links

* [API Reference](http://127.0.0.1:8000/swagger/)
* [Demo API](http://127.0.0.1:8000/v1/)

## Contributing

* Use Pull Requests!
* Always keep clean diffs.
* Use [http://editorconfig.org/](EditorConfig) and plugin for your IDE.

