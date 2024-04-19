FROM python:3.11

RUN mkdir /user_service

WORKDIR /user_service

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT bash ./run.sh