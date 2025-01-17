FROM python:3.11.5-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml ./

RUN poetry lock && poetry install --no-dev

ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PATH="/app/.venv/bin:$PATH"

COPY . .

EXPOSE 8000

CMD poetry run alembic upgrade head && poetry run uvicorn main:app --host 0.0.0.0 --port 8000