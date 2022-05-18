FROM python:3.9-bullseye

RUN mkdir /app
ADD . /app
WORKDIR /app

ENV TZ=Europe/Bucharest

RUN pip install -r Scan_files/requirements.txt

CMD python /app/Scan_files/main_scan.py