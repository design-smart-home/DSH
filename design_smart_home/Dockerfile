FROM python:3.12

WORKDIR /design_smart_home

RUN pip install --upgrade pip && pip install poetry==2.0.1
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY . .

ENV PYTHONPATH="${PYTHONPATH}:/design_smart_home/app"

CMD [ "poetry", "run", "python", "app/main.py" ]