FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN mkdir -p /home && cp model/deepcnn_edgeimpulse.onnx /home/model.onnx

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "run.py"]
