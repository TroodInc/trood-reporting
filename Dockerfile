FROM python:3.6

COPY . /app/.
WORKDIR /app

RUN pip install pipenv && pipenv install

ADD . /app/

CMD ["sh", "docker-entrypoint.sh"]
