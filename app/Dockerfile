FROM python:3.8-alpine
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src /src
CMD python producer_consumer.py
# pytest producer_consumer_test.py 