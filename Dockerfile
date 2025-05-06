FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "run.py"]
