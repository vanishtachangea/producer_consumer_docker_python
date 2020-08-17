import pytest
import asyncio

from producer_consumer import produce
from producer_consumer import consume

#from unittest.mock import patch, ANY
#from unittest.mock import MagicMock
from async_timeout import timeout


def with_timeout(t):
    def wrapper(corofunc):
        async def run(*args, **kwargs):
            with timeout(t):
                return await corofunc(*args, **kwargs)
        return run       
    return wrapper

@pytest.fixture
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

@pytest.fixture
def mock_queue(event_loop):
    return asyncio.Queue(loop=event_loop)


@pytest.mark.asyncio
async def test_produce(event_loop, mock_queue):
    await produce(mock_queue, 1)
    assert await mock_queue.get() == 'Name1'
    #assert await mock_queue.get() == 'Name2'
    assert await mock_queue.get() is None
'''
@pytest.mark.asyncio
async def test_consume(event_loop, mock_queue):
    await produce(mock_queue, 2)
    await consume(mock_queue)
    assert await mock_queue.get() is None
'''
@pytest.fixture()
async def queue_data():
    q = asyncio.Queue()
    await q.put('x')
    await q.put('y')
    await q.put('z')
    return q


'''
@pytest.fixture(autouse=True)
async def test_consume(queue_data,monkeypatch):
    data = []
    import producer_consumer

    def mockoutputfunc(message):
        #data.append(False if 'not' in msg else True)
        data.append(message)
    mockoutputfunc()

    #monkeypatch.setattr(coroutine, "output", mockfunc)
    #mocker.patch('producer_consumer.output', return_value=mockoutputfunc)
    print('asdad')
    mock = Mock(side_effect=mockoutputfunc)
    #monkeypatch.setattr(producer_consumer, 'output', mockoutputfunc)
    await consume(queue_data)
    print(data[0])
    assert data[0] == 'hello x'
    assert data[1] == 'hello y'
'''