import pytest
import asyncio
from producer_consumer import produce
from producer_consumer import consume

@pytest.mark.asyncio
async def test_producer_pass():
    loop = asyncio.get_event_loop()
    queue = asyncio.Queue(loop=loop)
    assert queue.empty() is True
    producer_coro = await produce(queue, 2)
    assert await queue.get() == 'Name1'
    assert await queue.get() == 'Name2'
    consumer_coro = await consume(queue)
    