# Asynchronous “hello world” consumer - producer application
Please build an asynchronous “hello world” consumer - producer application, over your choice of tooling.
A producer should provide a Name, and the consumer should output "hello <NAME>".

The project contains tests that prove the implementation works as intended.

In addition to the “hello name” consumer, a separate consumer output "goodbye <NAME>".

## Solution 1 - Using Asyncio 

### How to run 
- run the following commands
```
sudo docker-compose up --build
```
### Downfalls
- Delays:
-- Standard, largely unavoidable overhead
-- Situations where all consumers are sleeping when an item appears in the queue
### WorkAround 
## Solution 2 - Using Kafka
In Progress
In a microservice architecture or distributed architecture, we should use message broker between 
the producer and consumer. 
There are numerous asynchronous messaging techniques:
- RabbitMQ
- Kafka 
### RabbitMQ (AMQP):
    -   Queuing (One-to-one ) And Publish-subscribe(one-to-many): Both.
    -   Scale: Can send thousands of messages/second.
    -   Persistency: both persistent and transient messages are supported.
### Kafka:
    -   Queuing (One-to-one ) And Publish-subscribe(one-to-many): One-to-many.
    -   Scale: Can send millions of messages/second.
    -   Persistency: yes
## Kafka Details
Kafka is a distributed messaging system.
#### Common use-cases: 

- messaging between applications, where you can have applications "talk" to each using messages
- data processing pipelines from source systems to target destinations, thereby processing information on a *streaming* basis, rather than in *batches* as with your traditional ETL jobs
#### Architecture: 
![kafka architecture](https://www.confluent.io/wp-content/uploads/Screenshot-2017-07-19-19.14.28-1024x626.png)

*From [Confluent.io](https://www.confluent.io/blog/apache-kafka-for-service-architectures/)*
![](https://images.ctfassets.net/h6vh38q7qvzk/446ibu2GSQY886sasUwwOm/7864307b92b89afdb572d45fbc307f4a/backend.jpeg)

### Downfalls
- Doesn’t possess a full set of management and monitoring tools. This makes enterprise support staff a bit apprehensive about choosing Kafka and supporting it in the long run.
- The broker uses certain system calls to deliver messages to the consumer, but if the message needs some tweaking, doing so reduces Kafka’s performance significantly. If the message is unchanged, it can perform quite well, as it uses the ...
### WorkAround

# Conclusion

For messaging, we could use RabbitMQ, But we could also use Kafka because Kafka is designed for holding and distributing large volumes of messages and is faster.