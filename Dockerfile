ARG PLATFORM=linux/amd64

FROM --platform=${PLATFORM} python:3.11.10-slim AS dev
RUN apt-get update
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip &&pip install -r requirements.txt
CMD ["sh", "-c", "uvicorn app.main:app --reload --port=8000 --host=0.0.0.0"]

FROM --platform=${PLATFORM} python:3.11.10-slim AS prod
RUN apt-get update
WORKDIR /app
COPY . /app
RUN rm -rf /app/app/dev/
RUN pip install --upgrade pip &&pip install -r requirements.txt
CMD ["sh", "-c", "uvicorn app.main:app --reload --port=8000 --host=0.0.0.0"]