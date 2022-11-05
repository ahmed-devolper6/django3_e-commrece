FROM python:3.10
ENV PYTHONBUFFERED=1

WORKDIR /app
COPY requmenets.txt /app/requmenets.txt
RUN pip3 install -r requmenets.txt
COPY . /app/ 