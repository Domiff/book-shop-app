set dotenv-load

run:
    uv run python manage.py runserver

migrate:
    uv run python manage.py migrate

lint:
    uv run ruff check .

format:
    uv run ruff format .
