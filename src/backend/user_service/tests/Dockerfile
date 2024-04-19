FROM python:3.11

RUN mkdir /test_app

WORKDIR /test_app

COPY . .

RUN pip install -r requirements.txt

CMD python -m pytest -vv tests/ -s 2>&1 > test_results.log
