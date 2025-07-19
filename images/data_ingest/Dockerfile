# images/data_ingest/Dockerfile

FROM python:3.11

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY data_ingest.py ./

CMD ["python", "data_ingest.py"]
