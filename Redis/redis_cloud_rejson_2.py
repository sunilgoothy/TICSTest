# Reference: https://github.com/RedisJSON/redisjson-py

from rejson import Client, Path
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)

host = config['host']
port = config['port']
pwd = config['password']

rj = Client(host=host, port=port, password=pwd, decode_responses=True)

# Set the key `obj` to some object
obj = {
    'answer': 42,
    'arr': [None, True, 3.14],
    'truth': {
        'coord': 'out there'
    }
}

rj.jsonset('obj', Path.rootPath(), obj)

# # Get something
get_json = rj.jsonget('obj', Path('.truth.coord'))
print(f'Is there anybody... {get_json}?')

# Delete something (or perhaps nothing), append something and pop it
rj.jsondel('obj', Path('.arr[0]'))
rj.jsonarrappend('obj', Path('.arr'), 'something')
print('{} popped!'.format(rj.jsonarrpop('obj', Path('.arr'))))

# Update something else
rj.jsonset('obj', Path('.answer'), 2.17)

# And use just like the regular redis-py client
jp = rj.pipeline()
jp.set('foo', 'bar')
jp.jsonset('baz', Path.rootPath(), 'qaz')
jp.execute()

# If you use non-ascii character in your JSON data, you can add the no_escape flag to JSON.GET command
obj_non_ascii = {
    'non_ascii_string': 'hyvää'
}
rj.jsonset('non-ascii', Path.rootPath(), obj_non_ascii)
print('{} is a non-ascii string'.format(rj.jsonget('non-ascii', Path('.non_ascii_string'), no_escape=True)))
