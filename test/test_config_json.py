import json

# Read config file
with open("config.json", "r") as config_file:
    config = json.load(config_file)
    
print(type(config))
print(config)

# Assign config to local variables
host =  config['host']
print(f"host = {host}")

port =  config['port']
print(f"port = {port}")

pwd =  config['pwd']
print(f"pwd = {pwd}")

user =  config['user']
print(f"user = {user}")

# Add/modify
config['pwd'] = 'helios'
config['znewkey'] = 'znewvalue' 

# write to json file
with open("config.json", "w") as config_file:
    json.dump(config, config_file, indent=4)
