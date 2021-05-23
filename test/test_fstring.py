import datetime

now = datetime.datetime.now()
print(f'{now:%Y-%m-%d %H:%M:%S}')


val = 12.3
print(f'{val:.2f}')
print(f'{val:.5f}')

for x in range(1, 11):
    print(f'{x:02} {x*x:3} {x*x*x:4}')

x = 55
msg_format = "Values in dict are @xvalue, @2"
val_dict = {'xvalue':55, 2:66}
for key, value in val_dict.items():
    msg_format = msg_format.replace(f'@{key}', str(value))

# field = 'xvalue'
# msg = msg_format.replace(field, str(x))
print('msg -> ', msg_format)
input('Any key to exit')


    
    