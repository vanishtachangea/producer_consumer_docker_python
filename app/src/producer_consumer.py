import asyncio
import random


async def produce(queue, n):
    for x in range(1, n + 1):
        # produce an item
        print('Name{}'.format(x, n))
        # simulate i/o operation using sleep
        await asyncio.sleep(random.random())
        name = "name"+str(x)
        # put the name in the queue
        await queue.put(name)

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


loop = asyncio.get_event_loop()
queue = asyncio.Queue(loop=loop)
producer_coro = produce(queue, 10)
consumer_coro = consume(queue)
loop.run_until_complete(asyncio.gather(producer_coro, consumer_coro))
loop.close()