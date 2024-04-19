FROM python:3.11

RUN mkdir /post_service

WORKDIR /post_service

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT bash ./run.sh
