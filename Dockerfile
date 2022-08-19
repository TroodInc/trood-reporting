FROM python:3.6

COPY . /app/.
WORKDIR /app

RUN apt update && apt install -y python3-dev
RUN pip install pipenv && pipenv install

ADD . /app/

CMD ["sh", "docker-entrypoint.sh"]