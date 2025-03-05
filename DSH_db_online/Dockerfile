FROM python:3.12

WORKDIR /DSH_db_online

RUN pip install --upgrade pip && pip install poetry==2.0.1
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY . .

ENV PYTHONPATH="${PYTHONPATH}:/DSH_db_online/app"

CMD [ "poetry", "run", "python", "app/main.py" ]