FROM python:3.10-slim

WORKDIR /app

COPY todo.py requirements.txt ./

RUN mkdir -p data

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3", "todo.py"]
