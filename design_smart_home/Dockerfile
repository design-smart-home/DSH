FROM python:3.12

COPY pyproject.toml pyproject.toml
RUN pip install poetry
RUN poetry install

COPY . .

CMD [ "python", "main.py" ]