import asyncio
import random
"""
Asyncio Asyncio is used for coding asynchronous tasks e.g.Produce and Consume Tasks 
It allows concurrency, on a single thread
asyncio is really good for IO bound stuff and 
allows us to support thousands of read and write operations 
to the disk or network, without using any threads
"""

async def produce(queue, n):
    for x in range(1, n + 1):
        # Generate a name
        name = "Name"+str(x)
        print(name)
         # put the name in the queue
        await queue.put(name) 

        # simulate i/o operation using sleep
        await asyncio.sleep(random.random())
        
    print('Producer is Done')
    # indicate the producer is done
    await queue.put(None)


async def consume(queue):
    while True:
        # wait for a name from the producer
        name = await queue.get()
        if name is None:
            # the producer emits None if it is done
            break

        # process the name
        print('Hello {}...'.format(name))
        # simulate i/o operation using sleep
        await asyncio.sleep(random.random())
    print('Consumer is Done')

loop = asyncio.get_event_loop()
queue = asyncio.Queue(loop=loop)
producer_coro = produce(queue, 10)
consumer_coro = consume(queue)
loop.run_until_complete(asyncio.gather(producer_coro, consumer_coro))
loop.close()