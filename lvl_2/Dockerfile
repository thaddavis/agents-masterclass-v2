FROM python:3.12-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN python -m venv venv

RUN source venv/bin/activate

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src /usr/src/app/src

CMD ["python", "src/main.py"]