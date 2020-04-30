import time
MILLION = 1000000
def loop():
    start_time = time.perf_counter()
    val = 0
    while(val<MILLION):
        val+=1
    end_time = time.perf_counter()
    print("Execution Time:", (end_time - start_time), "seconds")

if __name__ == '__main__':
    loop()
    print('Running Test Script')