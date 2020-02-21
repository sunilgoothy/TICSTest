import redis

r = redis.Redis( host= 'localhost', port= '6379')
r.set('foo','bar')
r.set('Sunil','GOOTHY')

rs = r.get('foo')
print(rs.decode('utf-8'))

rs = r.get('Sunil')
print(rs.decode('utf-8'))