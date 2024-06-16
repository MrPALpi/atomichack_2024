FROM dockerhub.timeweb.cloud/library/python:latest

WORKDIR /app

RUN pip3 install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY ./ ./

RUN poetry install

EXPOSE 5000

CMD ["poetry", "run", "python", "main.py"]
