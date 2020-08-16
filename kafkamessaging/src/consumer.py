from kafka import KafkaConsumer
consumer = KafkaConsumer('Hello World')
for msg in consumer:
    print (msg)