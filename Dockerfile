FROM python:3.12-rc-slim-buster

# DO NOT copy .env or ./data dir
ADD esr /app/esr
ADD model /app/model
ADD run.py /app
ADD requirements.txt /app

# OS reqs for tk
RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python-tk python3-tk tk-dev

# Python reqs
WORKDIR /app
RUN pip install -r requirements.txt

CMD python3 run.py