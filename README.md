# Asynchronous “hello world” consumer - producer application
Please build an asynchronous “hello world” consumer - producer application, over your choice of tooling.
A producer should provide a Name, and the consumer should output "hello <NAME>".

The project contains tests that prove the implementation works as intended.

In addition to the “hello name” consumer, a separate consumer output "goodbye <NAME>".

## Solutions Options
There are 3 options 
 1. Asyncio
 2. RabbitMQ
 3. Kafka

 All 3 solutions use a queue system. But the way the queue system is architected is very different. 


## Solution 1 - Using Asyncio 
Asyncio uses one queue. The producer adds messages to the queue. The Consumer reads from the queue. 
![](http://blogs.quovantis.com/wp-content/uploads/2015/09/Selection_010.png)


### How to run 
- run the following commands
```
sudo docker-compose -f docker-compose.1.yaml up --build
```
### Downfalls
- Delays:
-- Standard, largely unavoidable overhead
-- Situations where all consumers are sleeping when an item appears in the queue
### WorkAround 


## Solution 3 for Distributed Systems - Using Kafka
In Progress
### How to run 
- run the following commands
```
sudo docker-compose -f docker-compose.yaml up --build
```
In a microservice architecture or distributed architecture, we should use message broker between 
the producer and consumer. 
There are numerous asynchronous messaging techniques:
- RabbitMQ
- Kafka 
### RabbitMQ (AMQP):
    -   Queuing (One-to-one ) And Publish-subscribe(one-to-many): Both.
    -   Scale: Can send thousands of messages/second.
    -   Persistency: both persistent and transient messages are supported.

In the case of RabbitMQ producer sends message to “EXCHANGE” and exchange pushes it to multiple queues and consumers get message from queues to which it has binded with.
![](http://blogs.quovantis.com/wp-content/uploads/2015/09/Selection_009.png)


### Kafka:
    -   Queuing (One-to-one ) And Publish-subscribe(one-to-many): One-to-many.
    -   Scale: Can send millions of messages/second.
    -   Persistency: yes
## Kafka Details
Kafka is a distributed messaging system.
In the case of Kafka, the Producers send messages over many partitions/queues, on many machines/clusters. 

#### Common use-cases: 

- messaging between applications, where you can have applications "talk" to each using messages
- data processing pipelines from source systems to target destinations, thereby processing information on a *streaming* basis, rather than in *batches* as with your traditional ETL jobs
#### Architecture: 
![kafka architecture](https://www.confluent.io/wp-content/uploads/Screenshot-2017-07-19-19.14.28-1024x626.png)

*From [Confluent.io](https://www.confluent.io/blog/apache-kafka-for-service-architectures/)*
![](https://images.ctfassets.net/h6vh38q7qvzk/446ibu2GSQY886sasUwwOm/7864307b92b89afdb572d45fbc307f4a/backend.jpeg)

### Advantages of Using Kafka
- High-throughput
- Low Latency
- Fault-Tolerant
- Durability
- Scalabilit
- Distributed
- Message Broker Capabilities
- High Concurrency

### Downfalls
- Doesn’t possess a full set of management and monitoring tools. This makes enterprise support staff a bit apprehensive about choosing Kafka and supporting it in the long run.
- The broker uses certain system calls to deliver messages to the consumer, but if the message needs some tweaking, doing so reduces Kafka’s performance significantly. 
- Not support wildcard topic selection
There is an issue that Kafka only matches the exact topic name, that means it does not support wildcard topic selection. Because that makes it incapable of addressing certain use cases.
### WorkAround
- Use Confluent : (https://docs.confluent.io/current/quickstart/ce-docker-quickstart.html)
The Confluent Platform is a stream data platform that enables you to organize and manage the massive amounts of data
- Use Amazon MSK : Amazon Managed Streaming for Apache Kafka (Amazon MSK) is a fully managed service that enables you to build and run applications that use Apache Kafka to process streaming data. 
# Conclusion
For simple messaging workload, we could use asyncio or RabbitMQ. But complex distributed systems,we could also use Kafka because Kafka is designed for holding and distributing large volumes of messages and is faster.
