FROM python:3.9

RUN apt update -y

RUN apt install -y python3-pip

WORKDIR /main

COPY ./requirements.txt ./

RUN pip3 install -r requirements.txt

COPY docker-entrypoint.sh ./

COPY src/ ./

CMD ./docker-entrypoint.sh