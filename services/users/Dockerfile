FROM python:3.9

WORKDIR /app

RUN pip install poetry

COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

EXPOSE 8000

COPY app/ /app/

ENTRYPOINT ["/usr/local/bin/python", "app.py"]
