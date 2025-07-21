FROM python:3.11-slim
WORKDIR /app

COPY ./app /app
COPY ../../infra/.env /app/.env

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]