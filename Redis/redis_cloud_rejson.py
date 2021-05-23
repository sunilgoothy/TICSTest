import redis
import json

data_from_py = {
    'foo': 'bar'
}

with open("config.json", "r") as config_file:
    config = json.load(config_file)

host = config['host']
port = config['port']
pwd = config['password']

r = redis.Redis(host=host, port=port, password=pwd)

r.execute_command('JSON.SET', 'doc_py', '.', json.dumps(data_from_py))
reply = json.loads(r.execute_command('JSON.GET', 'doc_py'))
print(type(reply), reply)

reply = json.loads(r.execute_command('JSON.GET', 'obj', 'truth.coord'))
print(type(reply), reply)