FROM python:3.12-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY watcher.py .

CMD ["python", "./watcher.py"]