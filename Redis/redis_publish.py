import redis, time

rclient = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

rclient.publish("test_redis", "Message from Python program")