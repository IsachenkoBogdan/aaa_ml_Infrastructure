FROM python:3.10
LABEL maintainer="B. Isachenko" version="alpha-0.0.1"
ENV FLASK_APP=./src/app.py F_PIP_LINK=https://download.pytorch.org/whl/torch_stable.html
WORKDIR app

COPY requirements.txt ./
RUN pip install -r requirements.txt -f $F_PIP_LINK

CMD python $FLASK_APP
