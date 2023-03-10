FROM python:3.11

# DO NOT copy .env or ./data dir
ADD esr /app/esr
ADD model /app/model
ADD run.py /app
ADD requirements.txt /app

WORKDIR /app
RUN pip install -r requirements.txt

CMD python3 run.py