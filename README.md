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
## Solution 2 - Kafka
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
For messaging, we could use RabbitMQ, But we could use Kafka because Kafka is designed for holding and distributing large volumes of messages and is faster.