FROM python:3.11-slim-bookworm

WORKDIR /app

RUN apt-get update && apt-get install -y gcc libpq-dev && \
    pip install --no-cache-dir --upgrade pip pip-tools

COPY requirements.txt .
COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

RUN pip-sync requirements.txt || pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["./entrypoint.sh"]

CMD ["python", "main.py"]
