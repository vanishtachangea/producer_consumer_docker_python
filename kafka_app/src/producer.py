
'''
Kafka:
Queuing (One-to-one ) And Publish-subscribe(one-to-many): One-to-many.
Scale: Can send millions of messages/second.
Persistency: yes
Any message queue that allows publishing messages decoupled from 
consuming them is effectively acting as a storage system for 
the in-flight messages. 
What is different about Kafka is that it is a very good storage system. 
It provides data persistency and stores streams of records that render 
it capable of exchanging quality messages.
https://github.com/wurstmeister/kafka-docker/wiki/Connectivity
'''

from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(
   value_serializer=lambda m: dumps(m).encode('utf-8'), 
   #bootstrap_servers=['172.17.0.1:32783','172.17.0.1:32782','172.17.0.1:32781'])
   bootstrap_servers=['localhost:32783','localhost:32782','localhost:32781'])

producer.send("test", value={"name": "producer"})