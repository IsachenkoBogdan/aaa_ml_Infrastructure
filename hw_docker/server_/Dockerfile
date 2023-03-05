FROM python:3.10-slim-bullseye
LABEL maintainer="B. Isachenko" version="alpha-0.0.1"
ENV PROJECT_DIR=. FLASK_APP=server.py

COPY $PROJECT_DIR ./app
WORKDIR app
RUN pip install -r requirements.txt

EXPOSE 8080
CMD python $FLASK_APP
