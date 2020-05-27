import time
import asyncio


def send_async_website_event(count: int):
    """ Async Amazon Kinesis Data Firehose example"""

    start = time.time()
    client = firehose().client  # your own firehose class
    extra_msg = {"aws_service": "firehose"}
    loop = asyncio.get_event_loop()
    tasks = []
    # your own logging function
    Log.info(f"sending async events [count: {count}]", extra=extra_msg)
    for c in range(count):
        tasks.append(asyncio.ensure_future(
            put_record(gen_uuid_events(), client)))
        Log.info(f"Sending async events: COUNT {c}/{count}")
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    log.info(f"Total time taken: {time.time()-start}")

# More on this type:
# https://vivekanandxyz.wordpress.com/2017/09/09/realtime-events-using-tornado-and-rabbitmq/
# https://pika.readthedocs.io/en/stable/examples/tornado_consumer.html
# https://developer.ibm.com/depmodels/cloud/articles/cl-optimizepythoncloud2/
