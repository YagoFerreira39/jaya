FROM python:3.11-alpine
COPY . .

ENV PATH=/root/.local:$PATH
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry add pyfiglet
RUN poetry install --no-dev


CMD ["python3", "main.py"]
