FROM alpine as source

WORKDIR /app
COPY . /app
RUN rm -rf words docker

FROM python:3.8-buster

RUN pip install pipenv \
    && apt update \
    && apt install -y \
    libgnat-7 \
    && rm -rf /var/lib/apt/lists/*

COPY words /opt/words
COPY docker/config.yaml /app/config.yaml

RUN useradd -ms /bin/bash flask
USER flask

WORKDIR /app
COPY Pipfile* /app/
RUN pipenv install

COPY --from=source /app /app

EXPOSE 5000

CMD ["pipenv", "run", "python", "hello.py"]
