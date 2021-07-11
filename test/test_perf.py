import time
from TICSUtil import *


MILLION = 1_000_000
BILLION = 1_000_000_000
def loop():
    start_time = time.perf_counter()
    for i in range(MILLION):
        print(i)
    end_time = time.perf_counter()
    print("Execution Time:", (end_time - start_time), "seconds")

if __name__ == '__main__':
    print('Running Test Script')
    loop()

    # config_value = readconfigfile('config.ini', 'test_section', 'url')
    # print(f'Config value in file is {config_value}')

    # print('End Test Script')
    # input('Any to exit')
    # print(input('Please Input something'))