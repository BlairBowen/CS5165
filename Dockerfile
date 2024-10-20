FROM python:3.11-slim
WORKDIR /home
COPY ./scripts.py ./scripts.py
COPY ./data /home/data
CMD ["python", "./scripts.py"]
