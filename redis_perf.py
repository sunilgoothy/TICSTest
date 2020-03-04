# importing the required modules
import timeit
import redis
import time

r = redis.StrictRedis()


def hash_write(val):
    r.hset('test:hset', 'field', val)


def hash_write_val():
    start_time = time.perf_counter()
    r.hset('test:hset', 'field', 1.1)
    end_time = time.perf_counter()
    print("Execution Time:", (end_time - start_time), "seconds")


def hash_write_perf():
    SETUP_CODE = '''from __main__ import hash_write
import redis
hash_write(100000)
'''

    TEST_CODE = 'hash_write(100000)'

    # timeit.repeat statement
    time = timeit.repeat(setup=SETUP_CODE,
                         stmt=TEST_CODE,
                         repeat=1,
                         number=10000)

    # priniting minimum exec. time
    print('Execution Time: {}'.format(time))


if __name__ == "__main__":
    hash_write_val()

