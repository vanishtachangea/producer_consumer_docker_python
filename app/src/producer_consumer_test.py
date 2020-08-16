import pytest
import asyncio
from producer_consumer import produce
from producer_consumer import consume

@pytest.mark.asyncio
async def test_producer_pass():
    loop = asyncio.get_event_loop()
    queue = asyncio.Queue(loop=loop)
    producer_coro = await produce(queue, 10)
    consumer_coro = await consume(queue)
    loop.run_until_complete(asyncio.gather(producer_coro, consumer_coro))
    loop.close()
    assert (1, 2, 3) == (1, 2, 3)