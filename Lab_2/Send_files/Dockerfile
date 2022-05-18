FROM python:3.9-bullseye

RUN mkdir /app
ADD . /app
WORKDIR /app

ENV TZ=Europe/Bucharest

RUN pip install -r Send_files/requirements.txt

CMD python /app/Send_files/main_events.py