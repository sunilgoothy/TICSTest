import redis
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)

host = config['host']
port = config['port']
pwd = config['password']

r = redis.Redis(host=host, port=port, password=pwd)

version = r.info()['redis_version']
test_dict = {"Sunil":"Manohar", "Company":"TMEIC"}
test_json = json.dumps(test_dict)
r.set('foo','bar')
r.set('Sunil','GOOTHY')
r.set('test_json_py', test_json)

test_json_get = json.loads(r.get('test_json_py'))
print(f"ping response: {r.ping()}")
print(f"version: {version}")
print(r.get('foo'))
print(r.get('Sunil'))
print(type(test_json_get), test_json_get)

print("Completed!!!")
