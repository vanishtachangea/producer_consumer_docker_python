import asyncio
import random
import logging


async def produce(queue, n):
    '''Asyncio Asyncio is used for coding asynchronous tasks e.g.Produce and Consume Tasks 
    It allows concurrency, on a single thread
    asyncio is really good for IO bound stuff and 
    allows us to support thousands of read and write operations 
    to the disk or network, without using any threads   
    Produce 
    A producer provide a Name which is stored in an asyncio queue. 
    Attributes: 
        queue (asyncio queue): The asyncio queue
        n (int): Number of time the Produce will loop to produce a name
    '''
    try:
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
        # print(produce.__doc__) 
        # print(produce) 
        await queue.put(None)
    except:
        logging.error(sys.exc_info()[0], "occurred.")

async def consume(queue):
    '''
    consume 
    A consumer function gets the name from asyncio queue and print "Hello <Name>"
    Attributes: 
        queue (asyncio queue): The asyncio queue
    '''
    try:
        while True:
            # wait for a name from the producer
            name = await queue.get()
            # the producer emits None if it is done
            if name is None:           
                break
            # process the name
            output('hello {}...'.format(name))
            # simulate i/o operation using sleep
            await asyncio.sleep(random.random())
        output('Consumer is Done')
    except:
        logging.error(sys.exc_info()[0], "occurred.")

async def consume2(queue):
    try:
        while True:
            # wait for a name from the producer
            name = await queue.get()

            # the producer emits None if it is done
            if name is None:            
                break
            # process the name
            print('goodbye {}...'.format(name))
            # simulate i/o operation using sleep
            await asyncio.sleep(random.random())
        print('Consumer2 is Done')
    except:
        logging.error(sys.exc_info()[0], "occurred.")

def output(message):
    print(message)
    return

'''
loop = asyncio.get_event_loop()
queue = asyncio.Queue(loop=loop)
producer_coro = produce(queue, 10)
consumer_coro = consume(queue)
loop.run_until_complete(asyncio.gather(producer_coro, consumer_coro))
loop.close()
'''
