################
# BASE IMAGE
################

FROM python:3.10-slim as base
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src ./src
COPY watcher.py .

################
# DEBUGGER
################

FROM base as debugger
RUN pip install debugpy
ENTRYPOINT [ "python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "--wait-for-client"]

################
# PRIMARY
################

FROM base as primary

CMD ["python", "./watcher.py"]