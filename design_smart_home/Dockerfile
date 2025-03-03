FROM python:3.12

COPY pyproject.toml poetry.lock ./
RUN pip install --upgrade pip && pip install poetry=2.0.1
RUN poetry install --no-root

COPY . .

CMD [ "poetry", "run", "python", "main.py" ]