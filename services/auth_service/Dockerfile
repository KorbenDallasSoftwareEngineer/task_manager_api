FROM python:3.11-slim

WORKDIR /app

COPY ./app /app
COPY ../../infra/.env /app/.env

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]