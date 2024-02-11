import redis, time

rclient = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

msgq = rclient.pubsub()
msgq.subscribe("test_redis")

while True:
    msg = msgq.get_message(ignore_subscribe_messages=True)
    if msg:
        print(msg)

    time.sleep(1)