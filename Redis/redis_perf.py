# importing the required modules
import timeit
import redis
import time

r = redis.StrictRedis()


def hash_write_ns(val):
    r.hset('test:hset', 'field1', val)

def hash_write(val):
    r.hset('hset', 'field2', val)

def hash_write_val():
    start_time = time.perf_counter()
    r.hset('test:hset', 'field3', 1.1)
    end_time = time.perf_counter()
    print("Execution Time hash_write_val:", (end_time - start_time), "seconds")


def hash_write_perf():
    SETUP_CODE = '''from __main__ import hash_write'''

    TEST_CODE = 'hash_write(1.1)'

    # timeit.repeat statement
    time = timeit.repeat(setup=SETUP_CODE,
                         stmt=TEST_CODE,
                         repeat=1,
                         number=10000)

    # printing minimum exec. time
    print('Execution Time hash_write_perf: {} seconds'.format(time))

def hash_write_ns_perf():
    SETUP_CODE = '''from __main__ import hash_write_ns'''

    TEST_CODE = 'hash_write_ns(1.1)'

    # timeit.repeat statement
    time = timeit.repeat(setup=SETUP_CODE,
                         stmt=TEST_CODE,
                         repeat=1,
                         number=10000)

    # printing minimum exec. time
    print('Execution Time hash_write_ns_perf: {} seconds'.format(time))


if __name__ == "__main__":
    hash_write(5)
    hash_write_val()
    hash_write_perf()
    hash_write_ns_perf()

