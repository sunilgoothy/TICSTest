import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
# r.set('foo','bar')
# r.set('Sunil','GOOTHY')

# rs = r.get('foo')
# print(rs.decode('utf-8'))

# rs = r.get('Sunil')
# print(rs.decode('utf-8'))

for i in range(1000):
    r.hset('test', 'field', i)

print("Completed!!!")
